gr-m2k
======

gr-m2k contains blocks that represent all major components of ADAML-2000. These GNU Radio blocks are build around ADI's libm2k library.

gr-m2k offers the possibility of interfacing with a variety of peripherals, in order to use the ADALM2000 as a master to configure/use them.

How to build it?
----------------

Linux
~~~~~

Dependencies
^^^^^^^^^^^^

-  :doc:`GNU Radio </wiki-migration/resources/tools-software/linux-software/gnuradio>`
-  :doc:`libiio </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz/software/linux/applications/libiio>`
-  :doc:`libm2k </wiki-migration/university/tools/m2k/libm2k/libm2k>`

Download and build gr-m2k

::

   git clone https://github.com/analogdevicesinc/gr-m2k.git
   cd gr-m2k
   mkdir build
   cd build
   cmake ..
   make 
   sudo make install
   cd ../..
   sudo ldconfig

In order to use the digital interfaces please enable the digital option:

::

   cmake -DDIGITAL=ON ..
   make 
   sudo make install

Blocks
------

Common
~~~~~~

-  **uri**: Describes the context location: usb:XX.XX.X, ip: XXX.XXX.XXX.XXX

M2k Analog In Source
~~~~~~~~~~~~~~~~~~~~

Controls the analogical input component of ADALM2000.


|image1|

-  **Buffer size**: Size of the internal buffer in samples.
-  **Enable ch 1**: Enables the receive data path for the first channel.
-  **Enable ch 2**: Enables the receive data path for the second channel.
-  **Range ch1**: Selects one of the available ranges: low, high
-  **Range ch2**: Selects one of the available ranges: low, high
-  **Calibrate ADC**: Calibrates the ADC
-  **Stream voltage**: Set to “true” in order to stream processed values, converted into volts.
-  **Sampling frequency**: Frequency at which the hardware will input samples - 1000, 10000, 100000, 1000000, 10000000, 100000000
-  **Oversampling ratio**: Oversamples the signal with the given integer factor.
-  **Kernel buffers**: The number of the internal buffers.
-  **Trigger condition ch 1**: Selects one of the available conditions: rising edge, falling edge, low level, high level
-  **Trigger condition ch 2**: Selects one of the available conditions: rising edge, falling edge, low level, high level
-  **Trigger mode ch 1**: Selects one of the available modes: always, analog
-  **Trigger mode ch 2**: Selects one of the available modes: always, analog
-  **Trigger source**: Selects one of the available sources: channel 1, channel 2, channel 1 or channel 2, channel 1 and channel 2, channel 1 xor channel 2
-  **Trigger delay**: The number of samples in buffer before the triggered sample.
-  **Trigger level ch 1**: The value in volts in which the triggering condition should be reach.
-  **Trigger level ch 1**: The value in volts in which the triggering condition should be reach.

M2k Analog Out Sink
~~~~~~~~~~~~~~~~~~~

Controls the analogical output component of ADALM2000.


|image2|

-  **Buffer size**: Size of the internal buffer in samples for both channels.
-  **Cyclic channel 1**: Set to “true” if the “cyclic” mode is desired. In this case, the first buffer of samples will be repeated.
-  **Cyclic channel 2**: Set to “true” if the “cyclic” mode is desired. In this case, the first buffer of samples will be repeated.
-  **Calibrate DAC**: Calibrates both DACs.
-  **Stream voltage**: Set to “true” in order to stream processed values, converted into volts.
-  **Sampling frequency ch1**: Frequency at which the hardware will output samples - 750, 7500, 75000, 750000, 7500000, 75000000
-  **Sampling frequency ch2**: Frequency at which the hardware will output samples - 750, 7500, 75000, 750000, 7500000, 75000000
-  **Oversampling ratio ch1**: Oversamples the first signal with the given integer factor.
-  **Oversampling ratio ch1**: Oversamples the second signal with the given integer factor.
-  **Kernel buffers ch 1**: The number of the internal buffers of the first channel.
-  **Kernel buffers ch 1**: The number of the internal buffers of the second channel.

M2k Analog In Converter
~~~~~~~~~~~~~~~~~~~~~~~

Converts raw ADC samples into voltage values

.. image:: https://wiki.analog.com/_media/university/tools/m2k/libm2k/m2k_analog_in_conv.png
   :width: 400px

M2k Analog Out Converter
~~~~~~~~~~~~~~~~~~~~~~~~

Converts raw DAC samples into voltage values.

Examples
--------

**Loopback**

In this example we are going to generate two signal(sine and square) using ADALM2000. These signal will be read back and plotted.

-  Hardware setup:

::

     1+ ---> W1
     2+ ---> W2

-  Flowgraph:

.. image:: https://wiki.analog.com/_media/university/tools/m2k/libm2k/gr_m2k_analog.png

**Build a radio with ADALM2000**

Process radio signals with ADALM2000 and GNU Radio Companion as front-end. Please check this :doc:`link </wiki-migration/university/tools/m2k/tutorials/buildingaradiowithm2k>`.

.. |image1| image:: https://wiki.analog.com/_media/university/tools/m2k/libm2k/m2k_analog_in_source.png
   :width: 350px
.. |image2| image:: https://wiki.analog.com/_media/university/tools/m2k/libm2k/m2k_analog_out_source.png
   :width: 350px
