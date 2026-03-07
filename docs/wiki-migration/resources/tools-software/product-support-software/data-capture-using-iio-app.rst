Precision ADC Data Capture Using IIO Firmware Applications
==========================================================

This page gives an overview of using the IIO based firmware applications for Precision ADC data capturing. The firmware applications are developed on the ARM 32-bit microcontrollers and 'ARM Mbed' is the primary development platform used. The visualization of ADC data is done using various IIO clients such as IIO oscilloscope, ACE, Pyadi-iio drivers, Matlab Precision toolbox, which are developed and supported by Analog Devices.

Data Capture With IIO Firmware Application
------------------------------------------

This page focuses on the firmware part of 'Data Capturing. The ":doc:`AD7606 IIO Application </wiki-migration/resources/tools-software/product-support-software/ad7606_mbed_iio_application>`" is used as a reference for this discussion.

IIO Oscilloscope can be used to capture and visualize the continuous analog or discrete signals from any ADC device using a IIO firmware application developed for that particular device. This allows user to monitor a real-time data. Using this firmware, a user can perform device calibration, change the gain, voltage range, data rate, etc. (based on device used) and observe the effects that different configurations have on the data displayed on IIO Oscilloscope. IIO Oscilloscope also allows users to save the data, which can further be used to process and analyze it.

The diagram below shows the continuous capture of signals on an AD7606 ADC, which is an 8-channel DAS. A 1Khz signal is applied on inputs of all 8 analog channels. The max data capturing rate in firmware is ~30 to 40 KSPS. The data is transmitted from firmware application at 230400 baud rate using UART serial link.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/iio_osc_sine_wave_capture.jpg
   :align: center

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/iio_osc_trapezoidal_wave_capture.jpg
   :align: center

-

The channels for which data is to be captured can be selected from the GUI window, along with the number of samples to display on screen in a single data read query. As shown below, all 8 channels are selected for data capture and the number of requested samples is set at 400 (default). This means, IIO oscilloscope requests 400 samples per channel, so in this case total 3200 samples. The channels are stored as shown below:

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/iio_osc_select_chn_samples.jpg
   :align: center

-

Limitations of Data Capture Using IIO Application
-------------------------------------------------

IIO oscilloscope is intended as a debugging tool and can only be used for data visualization/capture. It does not perform any sort of data processing. There are multiple factors which can potentially impact the data capturing and visualization.

-  Data Capturing/Sampling Rate
-  Data Transmission Rate (serial link)
-  Buffer size limitations in firmware

-

Data Capturing/Sampling Rate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The data capturing or sampling rate defines the maximum rate/speed at which data can be sampled and captured from the ADC using the IIO firmware application. For ADC's, typical time to capture single ADC sample is defined as:

**Time to capture single sample: ADC acquisition time + ADC sampling time + ADC data read time over digital interface**

For AD7606, this time is typically 28usec for all 8-channels (obtained in IIO firmware). AD7606 captures all 8-channels in single conversion cycle. When calculating the sample rate per second, it is obtained as ~284 KSPS per 8 channels (28usec / 8 = 3.5usec. Sample rate/second = 1/3.5usec = 284 KSPS). This gives sample rate per channel as ~35KSPS.

35Khz therefore can be considered as the sampling frequency. As per 'Nyquist–Shannon sampling theorem', the sampling frequency should theoretically be greater than twice the analog input frequency for faithful reproduction of the signal after conversion. However, in practice sampling frequency should be high enough to capture multiple slices/samples in given period, so that the input signal is replicated smoothly.

Due to this limitations, IIO oscilloscope can capture frequencies which are very less than max possible data rate. In case of AD7606, it is possible to capture the signals with frequencies of 4Khz and less when no oversampling is present. At OSR > 0, the data rate drops down and so higher frequency signals can't be reproduced correctly. Below plot is captured with 17Khz analog input on channel 1 and it can be seen that the signal is not a pure sine wave.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/iio_osc_high_frequency_graph.jpg
   :align: center

-

Data Transmission Rate (serial link)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the rate or speed at which data cane be transmitted to IIO oscilloscope over the serial link (e.g. UART). The data transmission rate and serial link used to capture the data plays an important role while capturing data at higher OSR's Or in scenarios where transmission rate is higher or lower than data capturing/sampling rate. The IIO oscilloscope requests the data in aperiodic manner, meaning that new data capture request is sent immediately when data from previous request is received.

Capturing Rate < Transmission Rate:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If data capturing rate is lower than transmission rate, the firmware can wait for certain period of time before sufficient samples are captured in the buffer. If time to capture these samples is higher than IIO oscilloscope timeout period, the firmware returns the empty/invalid data. Therefore the user must always ensure that the data rate is always higher than the transmission rate at any instance. If this is not the case, transmission rate can be reduced by lowering the baud rate (for UART medium). Also, the requested number of samples must also be modified according to a data rate of device to avoid IIO oscilloscope getting timed-out or to have a huge discontinuity in the data visualization.

Another factor that determines the IIO oscilloscope timeout is 'sampling_frequency' attribute. If this attribute is not defined, the timeout period for IIO oscilloscope during data capture is set to 2sec default, however, if this attribute is defined, the time is calculated as: number of requested samples \* (1 / sampling_frequency). For example, if sampling frequency is set as 400SPS, the timeout period is:

timeout = 400 (requested samples) \* (1 / 10000 SPS) + 1sec = 1.4 sec

.. _capturing-rate-transmission-rate-1:

Capturing Rate > Transmission Rate:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If data capturing rate is too high compared to the transmission rate, the data acquisition into a buffer happens faster. So data buffer might fill faster compared to emptying operation. This might lead to a discontinuity on data visualization on IIO oscilloscope side as data visualization is limited by data transmission rate in this case (with slower serial communication link). If communication link is faster and matches to capturing/sampling rate, the visualization of data would be more continuous.

-

Buffer size limitations in firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The requested number of samples set in IIO oscilloscope must always be less than half the buffer size set in the IIO firmware. For the case of AD7606 devices, the max samples to be requested in a single query should not be greater than 4096 for a buffer size of 8192 samples. This is explained below:

The buffer read and write happens in parallel through 2 different events. The data from buffer is read when new request from IIO oscilloscope occurs while write operation continues in the background typically through interrupt event which monitors the end of conversion (new sample available to read). While reading the data from buffer, at-least 128 samples offset must be present b/w read and write index of a buffer (this is shown in below diagram). In other words, the write index must always be greater than read index. The write index always increments faster compared to read index for devices with fast data capturing speed compared to transmit speed. For instance, AD7606 can capture 128 samples in 3.5msec, while time it takes to transmit 128 samples is 18msec @230.4 KBPS rate. So, buffer fills faster than emptying it. For slower capturing devices, this situation is reversed. In those device it is always ensured in the firmware that read index does not cross the write index at any instance.

So, considering this limitation, the firmware ensures that the buffer is always read completely after it is full, and before it starts writing new data from it's head (start index). If this is not done, there is always a possibility that old data is overwritten when the buffer starts filling from the start or head. The write index stops at the end of the buffer when it is full and once the buffer is read completely it is moved to the start to begin filling data from the head in a circular fashion.

The IIO data is always sent in chunks of 256 bytes. When converted into samples, it becomes 128 (256 / 2) for the AD7606B device due to its 16-bit (2-byte) resolution. If requested samples are 400, the number of loops becomes 400 / 128 = 3.21. So samples are transmitted as: 128, 128, 128, 84. This is done in single loop, so firmware reads the buffer for 128 samples, transmit them over UART link and then repeat the cycle until all 400 samples are sent. In the last loop, only 84 samples are read and sent to IIO oscilloscope.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/iio_data_capture_in_firmware.jpg
   :align: center
   :width: 600px

Now, consider the scenario where more than 4096 samples are requested. So assume 5000 samples are requested by IIO oscilloscope for 2 channels. The buffer will start filling the data and will reach the end of the buffer, thus write index pointing to 8192. The read is assumed to slower than write, so read index would be less than write (say read index is pointing to 2000). At this instance, the write buffer can't really start capturing new data because it can override old data as a read is still in progress. Assume the read of 5000 samples is complete in the first request and read index has reached 5000. In the next request a further 5000 samples would be requested. But the problem now is that the buffer size is only 8192 and there are no extra samples ((5000 + 5000) - 8192 = 1808) available to transmit. If samples are not transmitted back to IIO oscilloscope or dummy/old data is sent, the misalignment of channel data occurs (when more than 1 channels are selected). This effects the data visualization on IIO oscilloscope. To avoid this problem, the number of requested samples should always be less than 4096 for buffer size of 8192 at any instance (or to be precise, the total requested samples must always be less than half the size of buffer). This however does not mean only 4096 sample size of buffer is utilized as described below:

If requested samples are 1050, the max available size of buffer is: available size = (8192 / 1050) \* 1050 = 7 \* 1050 = 7350. Thus buffer utilizes 7350 samples size from max 8192.

::

                 /* Size of the acquisition buffer (in terms of samples) */
                 #define DATA_BUFFER_SIZE        (8192)

.. important::

   The behavior of data capturing and displaying varies from device to device. Two two major things must be considered while designing IIO firmware for any device is: 1) Device capture speed 2) Data Transmission speed

   
   If capturing is slower for any device (low data rate), the ODR (output data rate) of device must be adjusted accordingly (if applicable) so that time to obtain requested samples is always less than the IIO oscilloscope timeout period. If ODR is fixed in the device, the time to capture number of requested samples by user should always be less than timeout period of IIO oscilloscope, otherwise invalid data is returned back. Therefore the user must provide valid count for requested samples.


If requested samples is set higher than the available buffer size, a constant value is transmitted to IIO oscilloscope to avoid IIO oscilloscope becoming unresponsive. As shown below, requested samples are 1000 \* 8 = 8000, which is greater than 4096 (available buffer size). Therefore oscilloscope displays a constant value as an error indication.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/iio_osc_no_response.jpg
   :align: center

-

Saving Captured Data
--------------------

The data on IIO oscilloscope can be saved for further processing and analysis. The data is saved using a .csv format. The data can be captured for each selected channel during save option and only requested number of samples can be saved. So if 400 samples are requested, the data for only 400 samples would get saved into .csv file. The data is raw adc data and no extra processing is performed it while saving or capturing.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/iio_osc_data_save.jpg
   :align: center

.. note::

   For detailed guide on using IIO based firmware applications, refer :doc:`AD7606 IIO Application code </wiki-migration/resources/tools-software/product-support-software/ad7606_mbed_iio_application>`. Feel free to consult Analog Devices Engineer-Zone for feature requests, feedback, bug-reports etc.


IIO Oscilloscope (Client)
-------------------------

This is a GUI (Graphical User Interface) based IIO client application for data visualization and device configuration/debugging. The data from IIO devices (ADCs/DACs) is transmitted over Serial/Ethernet/USB link to IIO Oscilloscope client through the abstracted layer of "libiio" (Library developed originally to interface with linux based IIO devices). You can download and install :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>` from the links below.

.. admonition:: Download
   :class: download

   IIO Oscilloscope installer for Windows (Use below link):

   
   -  :git-iio-oscilloscope:`IIO Oscilloscope windows installer (.exe) <releases>`
   
   Libiio installer for Windows (Use below link):
   
   -  :git-libiio:`libiio windows installer (.exe) <releases>`
   


.. _data-capture-with-iio-firmware-application-1:

Data Capture With IIO Firmware Application
------------------------------------------

This page focuses on the firmware part of 'Data Capturing. The ":doc:`AD7606 IIO Application </wiki-migration/resources/tools-software/product-support-software/ad7606_mbed_iio_application>`" is used as a reference for this discussion.

IIO Oscilloscope can be used to capture and visualize the continuous analog or discrete signals from any ADC device using a IIO firmware application developed for that particular device. This allows user to monitor a real-time data. Using this firmware, a user can perform device calibration, change the gain, voltage range, data rate, etc. (based on device used) and observe the effects that different configurations have on the data displayed on IIO Oscilloscope. IIO Oscilloscope also allows users to save the data, which can further be used to process and analyze it.

The diagram below shows the continuous capture of signals on an AD7606 ADC, which is an 8-channel DAS. A 1Khz signal is applied on inputs of all 8 analog channels. The max data capturing rate in firmware is ~30 to 40 KSPS. The data is transmitted from firmware application at 230400 baud rate using UART serial link.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/iio_osc_sine_wave_capture.jpg
   :align: center

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/iio_osc_trapezoidal_wave_capture.jpg
   :align: center

-

The channels for which data is to be captured can be selected from the GUI window, along with the number of samples to display on screen in a single data read query. As shown below, all 8 channels are selected for data capture and the number of requested samples is set at 400 (default). This means, IIO oscilloscope requests 400 samples per channel, so in this case total 3200 samples. The channels are stored as shown below:

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/iio_osc_select_chn_samples.jpg
   :align: center

-

.. _limitations-of-data-capture-using-iio-application-1:

Limitations of Data Capture Using IIO Application
-------------------------------------------------

IIO oscilloscope is intended as a debugging tool and can only be used for data visualization/capture. It does not perform any sort of data processing. There are multiple factors which can potentially impact the data capturing and visualization.

-  Data Capturing/Sampling Rate
-  Data Transmission Rate (serial link)
-  Buffer size limitations in firmware

-

.. _data-capturingsampling-rate-1:

Data Capturing/Sampling Rate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The data capturing or sampling rate defines the maximum rate/speed at which data can be sampled and captured from the ADC using the IIO firmware application. For ADC's, typical time to capture single ADC sample is defined as:

**Time to capture single sample: ADC acquisition time + ADC sampling time + ADC data read time over digital interface**

For AD7606, this time is typically 28usec for all 8-channels (obtained in IIO firmware). AD7606 captures all 8-channels in single conversion cycle. When calculating the sample rate per second, it is obtained as ~284 KSPS per 8 channels (28usec / 8 = 3.5usec. Sample rate/second = 1/3.5usec = 284 KSPS). This gives sample rate per channel as ~35KSPS.

35Khz therefore can be considered as the sampling frequency. As per 'Nyquist–Shannon sampling theorem', the sampling frequency should theoretically be greater than twice the analog input frequency for faithful reproduction of the signal after conversion. However, in practice sampling frequency should be high enough to capture multiple slices/samples in given period, so that the input signal is replicated smoothly.

Due to this limitations, IIO oscilloscope can capture frequencies which are very less than max possible data rate. In case of AD7606, it is possible to capture the signals with frequencies of 4Khz and less when no oversampling is present. At OSR > 0, the data rate drops down and so higher frequency signals can't be reproduced correctly. Below plot is captured with 17Khz analog input on channel 1 and it can be seen that the signal is not a pure sine wave.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/iio_osc_high_frequency_graph.jpg
   :align: center

-

.. _data-transmission-rate-serial-link-1:

Data Transmission Rate (serial link)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the rate or speed at which data cane be transmitted to IIO oscilloscope over the serial link (e.g. UART). The data transmission rate and serial link used to capture the data plays an important role while capturing data at higher OSR's Or in scenarios where transmission rate is higher or lower than data capturing/sampling rate. The IIO oscilloscope requests the data in aperiodic manner, meaning that new data capture request is sent immediately when data from previous request is received.

.. _capturing-rate-transmission-rate-2:

Capturing Rate < Transmission Rate:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If data capturing rate is lower than transmission rate, the firmware can wait for certain period of time before sufficient samples are captured in the buffer. If time to capture these samples is higher than IIO oscilloscope timeout period, the firmware returns the empty/invalid data. Therefore the user must always ensure that the data rate is always higher than the transmission rate at any instance. If this is not the case, transmission rate can be reduced by lowering the baud rate (for UART medium). Also, the requested number of samples must also be modified according to a data rate of device to avoid IIO oscilloscope getting timed-out or to have a huge discontinuity in the data visualization.

Another factor that determines the IIO oscilloscope timeout is 'sampling_frequency' attribute. If this attribute is not defined, the timeout period for IIO oscilloscope during data capture is set to 2sec default, however, if this attribute is defined, the time is calculated as: number of requested samples \* (1 / sampling_frequency). For example, if sampling frequency is set as 400SPS, the timeout period is:

timeout = 400 (requested samples) \* (1 / 10000 SPS) + 1sec = 1.4 sec

.. _capturing-rate-transmission-rate-3:

Capturing Rate > Transmission Rate:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If data capturing rate is too high compared to the transmission rate, the data acquisition into a buffer happens faster. So data buffer might fill faster compared to emptying operation. This might lead to a discontinuity on data visualization on IIO oscilloscope side as data visualization is limited by data transmission rate in this case (with slower serial communication link). If communication link is faster and matches to capturing/sampling rate, the visualization of data would be more continuous.

-

.. _buffer-size-limitations-in-firmware-1:

Buffer size limitations in firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The requested number of samples set in IIO oscilloscope must always be less than half the buffer size set in the IIO firmware. For the case of AD7606 devices, the max samples to be requested in a single query should not be greater than 4096 for a buffer size of 8192 samples. This is explained below:

The buffer read and write happens in parallel through 2 different events. The data from buffer is read when new request from IIO oscilloscope occurs while write operation continues in the background typically through interrupt event which monitors the end of conversion (new sample available to read). While reading the data from buffer, at-least 128 samples offset must be present b/w read and write index of a buffer (this is shown in below diagram). In other words, the write index must always be greater than read index. The write index always increments faster compared to read index for devices with fast data capturing speed compared to transmit speed. For instance, AD7606 can capture 128 samples in 3.5msec, while time it takes to transmit 128 samples is 18msec @230.4 KBPS rate. So, buffer fills faster than emptying it. For slower capturing devices, this situation is reversed. In those device it is always ensured in the firmware that read index does not cross the write index at any instance.

So, considering this limitation, the firmware ensures that the buffer is always read completely after it is full, and before it starts writing new data from it's head (start index). If this is not done, there is always a possibility that old data is overwritten when the buffer starts filling from the start or head. The write index stops at the end of the buffer when it is full and once the buffer is read completely it is moved to the start to begin filling data from the head in a circular fashion.

The IIO data is always sent in chunks of 256 bytes. When converted into samples, it becomes 128 (256 / 2) for the AD7606B device due to its 16-bit (2-byte) resolution. If requested samples are 400, the number of loops becomes 400 / 128 = 3.21. So samples are transmitted as: 128, 128, 128, 84. This is done in single loop, so firmware reads the buffer for 128 samples, transmit them over UART link and then repeat the cycle until all 400 samples are sent. In the last loop, only 84 samples are read and sent to IIO oscilloscope.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/iio_data_capture_in_firmware.jpg
   :align: center
   :width: 600px

Now, consider the scenario where more than 4096 samples are requested. So assume 5000 samples are requested by IIO oscilloscope for 2 channels. The buffer will start filling the data and will reach the end of the buffer, thus write index pointing to 8192. The read is assumed to slower than write, so read index would be less than write (say read index is pointing to 2000). At this instance, the write buffer can't really start capturing new data because it can override old data as a read is still in progress. Assume the read of 5000 samples is complete in the first request and read index has reached 5000. In the next request a further 5000 samples would be requested. But the problem now is that the buffer size is only 8192 and there are no extra samples ((5000 + 5000) - 8192 = 1808) available to transmit. If samples are not transmitted back to IIO oscilloscope or dummy/old data is sent, the misalignment of channel data occurs (when more than 1 channels are selected). This effects the data visualization on IIO oscilloscope. To avoid this problem, the number of requested samples should always be less than 4096 for buffer size of 8192 at any instance (or to be precise, the total requested samples must always be less than half the size of buffer). This however does not mean only 4096 sample size of buffer is utilized as described below:

If requested samples are 1050, the max available size of buffer is: available size = (8192 / 1050) \* 1050 = 7 \* 1050 = 7350. Thus buffer utilizes 7350 samples size from max 8192.

::

                 /* Size of the acquisition buffer (in terms of samples) */
                 #define DATA_BUFFER_SIZE        (8192)

.. important::

   The behavior of data capturing and displaying varies from device to device. Two two major things must be considered while designing IIO firmware for any device is: 1) Device capture speed 2) Data Transmission speed

   
   If capturing is slower for any device (low data rate), the ODR (output data rate) of device must be adjusted accordingly (if applicable) so that time to obtain requested samples is always less than the IIO oscilloscope timeout period. If ODR is fixed in the device, the time to capture number of requested samples by user should always be less than timeout period of IIO oscilloscope, otherwise invalid data is returned back. Therefore the user must provide valid count for requested samples.


If requested samples is set higher than the available buffer size, a constant value is transmitted to IIO oscilloscope to avoid IIO oscilloscope becoming unresponsive. As shown below, requested samples are 1000 \* 8 = 8000, which is greater than 4096 (available buffer size). Therefore oscilloscope displays a constant value as an error indication.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/iio_osc_no_response.jpg
   :align: center

-

.. _saving-captured-data-1:

Saving Captured Data
--------------------

The data on IIO oscilloscope can be saved for further processing and analysis. The data is saved using a .csv format. The data can be captured for each selected channel during save option and only requested number of samples can be saved. So if 400 samples are requested, the data for only 400 samples would get saved into .csv file. The data is raw adc data and no extra processing is performed it while saving or capturing.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/iio_osc_data_save.jpg
   :align: center

.. note::

   For detailed guide on using IIO based firmware applications, refer :doc:`AD7606 IIO Application code </wiki-migration/resources/tools-software/product-support-software/ad7606_mbed_iio_application>`. Feel free to consult Analog Devices Engineer-Zone for feature requests, feedback, bug-reports etc.

