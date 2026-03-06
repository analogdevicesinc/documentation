EVALUATING THE AD9265 ANALOG-TO-DIGITAL CONVERTER
=================================================

|

.. warning::

   \ **NOTE:**

   | Support for the AD9265-fmc is discontinued starting with 2022_R2 Kuiper Linux release and it will not be supported in future releases. Last release in which pre-build files can be found is 2021_r2. Check this :doc:`link </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images/release_notes>` to see all Kuiper releases.


Preface
-------

| This user guide describes the evaluation board,\ :adi:`AD9265-FMC-125EBZ <AD9265>`, that is used to evaluate the following Analog Devices, Inc., product: :adi:`AD9265`. These evaluation board provide all of the support circuitry required to operate these parts in their various modes and configurations. The application software used to interface with the devices is also described.
| The :adi:`AD9265` data sheet provide additional information and should be consulted when using the evaluation board. All documents and software tools are available at :adi:`www.analog.com/sdp <sdp>`. For additional information or questions, send an email to highspeedproductssupport@analog.com.

Typical Measurement Setup
-------------------------

|image1|

.. container:: centeralign

   *Figure 1. Evaluation Board Connection—*\ :adi:`AD9265-FMC-125EBZ <AD9265>` *(on Left) and

   *\ :adi:`EVAL-SDP-CH1Z <sdp>` *SDP-H1 (on Right)*


Features
--------

-  Full featured evaluation board for the :adi:`AD9265`.
-  SPI interface for setup and control
-  External, on-board oscillator, and :adi:`ad9517` clocking options
-  Balun/transformer or amplifier input drive option
-  LDO regulator or switching power supply options
-  VisualAnalog® and SPI controller software interfaces

Helpful Documents
-----------------

-  :adi:`AD9265` data sheet
-  :adi:`EVAL-SDP-CH1Z <sdp>`, *SDP-H1 High Speed Controller Board for System Development Platform*
-  :adi:`AN-905 Application Note <an-905>`, *VisualAnalog Converter Evaluation Tool Version 1.0 User Manual*
-  :adi:`AN-878 Application Note <an-878>`, *High Speed ADC SPI Control Software*
-  :adi:`AN-877 Application Note <an-877>`, *Interfacing to High Speed ADCs via SPI*
-  :adi:`AN-835 Application Note <an-835>`, *Understanding ADC Testing and Evaluation*
-  :adi:`UG-074 User Guide <media/en/technical-documentation/user-guides/UG-074.pdf>`, *User Guide for FIFO5 AD9265 Evaluation Board*

Software Needed
---------------

-  :adi:`SPI Controller <en/design-center/interactive-design-tools/spicontroller.html>`
-  :adi:`Visual Analog <en/design-center/interactive-design-tools/visualanalog.html>`

Design and Integration Files
----------------------------

-  Schematics: `AD9265-FMC-125EBZ RevA <https://wiki.analog.com/_media/resources/eval/ad9265_fmc_125ebz_sch.pdf>`__
-  Layout: `AD9265-FMC-125EBZ RevA <https://wiki.analog.com/_media/resources/eval/ad9265_fmc_125ebz_lay.pdf>`__
-  Bill of Materials: `AD9265-FMC-125EBZ RevA <https://wiki.analog.com/_media/resources/eval/ad9265_fmc_125ebz_bom.xls>`__
-  FPGA Program File: `ad9265_sdph1.bin <https://wiki.analog.com/_media/resources/eval/ad9265_sdph1.zip>`__

Equipment Needed
----------------

-  Analog signal source (preferably SMA 100A Signal Generator)
-  Antialiasing filter
-  Sample clock source (if not using the on-board oscillator)
-  12V Power Supply
-  1-meter SMA Cable
-  PC running Windows®
-  USB-Mini-B Cable
-  :adi:`AD9265-FMC-125EBZ <AD9265>` board
-  :adi:`EVAL-SDP-CH1Z <sdp>` System Development Platform Kit

Getting Started
---------------

| This section provides quick start procedures for using the :adi:`AD9265-FMC-125EBZ <AD9265>` board. Both the default and optional settings are described.

Configuring the Board
~~~~~~~~~~~~~~~~~~~~~

Before using the software for testing, configure the evaluation board as follows:

-  Connect the evaluation board to the data capture board, as shown in Figure 1.
-  Connect one 12V switching power supply to the :adi:`EVAL-SDP-CH1Z <sdp>` SDP-H1 board.
-  Connect the :adi:`EVAL-SDP-CH1Z <sdp>` SDP-H1 board to the PC with a USB cable. (Connect to J1)
-  On using the on-board clock in the board, connect the Pin 1 and Pin 3 in P2.
-  On the ADC evaluation board, use a clean signal generator with low phase noise to provide an input signal to the input channel (J100). Use a 1 m, shielded, RG-58, 50 Ω coaxial cable to connect the signal generator: For best results, use a narrow-band, band-pass filter with 50 Ω terminations and an appropriate center frequency. (Analog Devices uses TTE, Allen Avionics, and K & L band-pass filters)
-   If using external clock signal, remove the connector in P2 and use a clean signal generator to J201.

Using The Software for Testing
------------------------------

Setting up the ADC Data Capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After configuring the board, set up the ADC data capture using the following steps:

-  Start Visual Analog. |image2|\

.. container:: centeralign

   \ *Figure 2. VisualAnalog, Start Button*\


-  Select AD9265 and double click FFT |image3|\

.. container:: centeralign

   \ *Figure 3. VisualAnalog, New Canvas Window*\


-  Click settings under ADC Data Capture section. |image4|\

.. container:: centeralign

   \ *Figure 4. VisualAnalog, ADC Data Capture Section*\


-  Set device to AD9265.
-  Navigate to Capture Board and browse your file directory for the FPGA Image called. (ad9265_sdph1.bin)
-  Click Program and check if LED0 on the SDP-H1 lights up. Then, click OK. |image5|\

.. container:: centeralign

   \ *Figure 5. VisualAnalog, ADC Data Capture Settings*\


Evaluation And Test
-------------------

Setting up the SPI Controller Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Start SPIController |image6|\

.. container:: centeralign

   \ *Figure 6. SPIController Start Button*\


-  If a message opens saying "Read Test Failure", select Ignore. |image7|\

.. container:: centeralign

   \ *Figure 7. 1st Ignore Test Failure*\


-  Click File > Cfg Open then find the file named "ad9265_16bit_125MSspiR03.cfg" and double click it. |image8|\

.. container:: centeralign

   \ *Figure 8. Configuration Settings*\


-  Again, if a message opens saying "Read Test Failure", select Ignore. |image9|\

.. container:: centeralign

   \ *Figure 9. 2nd Ignore Test Failure*\


-  Click Config > Controller Dialog. |image10|\

.. container:: centeralign

   \ *Figure 10. Controller Dialog Guide*\


-  Un-select SDO Active and click OK. |image11|\

.. container:: centeralign

   \ *Figure 11. Controller Dialog Setting*\


-  Click Read chip ID and Read Chip Grade. |image12|\

.. container:: centeralign

   \ *Figure 12. Read Chip ID and Read Chip Grade Section*\


-  Go Back to Visual Analog and click Play button.

Adjusting the Amplitude of the Input Signal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The next step is to adjust the amplitude of the input signal for each channel as follows:

-  Adjust the amplitude of the input signal so that the fundamental is at -1.0 dBFS. Examine the **Fund Power** reading in the left panel of the **VisualAnalog Graph - AD9265 Average FFT** window (see Figure 13) to verify this.\ |image13|\

.. container:: centeralign

   //Figure 13. Graph Window of VisualAnalog *


\* Click the disk icon within the* **Graph** *window to save the performance plot data as .csv formatted file. \

.. container:: centeralign

   *\ Figure 14. VisualAnalog Disk Icon //


Testing Additional AD9265 Boards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Power down the :adi:`EVAL-SDP-CH1Z <sdp>` SDP-H1 board first before swapping them.

Troubleshooting Tips
--------------------

If the FFT plot appears abnormal, do the following:

-  If you see a normal noise floor when you disconnect the signal generator from the analog input, be sure you are not overdriving the ADC. Reduce the input level, if necessary.
-  In **VisualAnalog**, click the **Settings** button in the **Input Formatter** block. Check that **Number Format** is set to correct encoding (offset binary by default).

If the FFT appears normal but the performance is poor, check the following:

-  Make sure that an appropriate band-pass filter is used on the analog input.
-  Make sure that the signal generators for the clock and the analog input are clean (low phase noise).
-  Change the analog input frequency slightly if noncoherent sampling is being used, or use coherent frequencies.
-  Make sure that the SPI configuration file matches the product being evaluated.
-  Make sure the there isn't any extra stress/torque on the clock and analog input connectors.

If the FFT window remains blank after **Run** is clicked, do the following:

-  Make sure that the evaluation board is securely connected to the :adi:`EVAL-SDP-CH1Z <sdp>` SDP-H1 board.
-  Make sure that the FPGA has been programmed by verifying that the **FPGA_DONE** LED is illuminated on the :adi:`EVAL-SDP-CH1Z <sdp>` board. If this LED is not illuminated, reprogram the FPGA through VisualAnalog. If the LED still does not illuminate, disconnect the USB and power cord for 15 seconds. Connect again and repeat the *SDP-H1* setup process.
-  Make sure the correct FPGA bin file was used to program the FPGA.
-  Be sure that the correct sample rate is programmed. Click on the **Settings** button in the **ADC Data Capture** block in VisualAnalog and verify that he **Clock Frequency** is properly set.
-  Ensure that he ADC has valid clock input.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ad9265_fmc_125ebz_typical_setup.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ad9265_va_start_button.png
   :width: 100px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ad9265_va_new_canvas.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/ad9265_va_adc_data_capture_2.png
   :width: 300px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/ad9265_va_adc_data_capture_setting_fpga.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/ad9265_spicontroller_start_button.png
   :width: 100px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/ad9265_spicontroller_msg_ignore.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/ad9265_spicontroller_cfg_open.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/ad9265_spicontroller_msg_ignore.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/ad9265_spicontroller_controller_dialog.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/ad9265_spicontroller_unselect_sdo_2.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/ad9265_spicontroller_read_chip_id_grade.png
   :width: 300px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/ad9265_typical_window_2.png
   :width: 500px
