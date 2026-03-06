EVALUATING THE AD9467-FMC-250EBZ ANALOG-TO-DIGITAL CONVERTER
============================================================

Preface
-------

| This user guide describes the :adi:`AD9467` evaluation board :adi:`AD9467-FMC-250EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9467.html#eb-overview>` which provides all the support circuitry required to operate the ADC in its various modes and configurations. The application software to interface with the devices is also described.
| The :adi:`AD9467` data sheet provides additional information and should be consulted when using the board. All documents and software tools are available at :adi:`www.analog.com/hsadcevalboard <hsadcevalboard>`. For additional information or questions send an email to highspeed.converters@analog.com.

AD9467-FMC-250EBZ
-----------------

|image1|\

.. container:: centeralign

   *Figure 1.* :adi:`AD9467-FMC-250EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9467.html#eb-overview>` *Evaluation Board*\


Typical Measurement Setup
-------------------------

|image2|\

.. container:: centeralign

   *Figure 2. Evaluation Board Connection—*\ :adi:`AD9467-FMC-250EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9467.html#eb-overview>` *(on Left) and* :adi:`SDP-H1` *(on Right)*


Features
--------

-  Full feature evaluation board for the :adi:`AD9467`
-  SPI interface for setup and control
-  Uses 12V. 3.3V from the FMC connection
-  Internal and external reference options
-  VisualAnalog® and SPI controller software interfaces

Helpful Documents
-----------------

-  :adi:`AD9467` Data Sheet
-  EVAL-SDP-CH1Z data capture kit :adi:`SDP-H1 <en/system-demonstration-platform/controller-boards/evaluation/EVAL-SDP-H1/eb.html>`
-  :adi:`AN-905 Application Note <an-905>`, *VisualAnalog Converter Evaluation Tool Version 1.0 User Manual*
-  :adi:`AN-878 Application Note <an-878>`, *High Speed ADC SPI Control Software*
-  `ADI SPI Application Note </>resources/technical-guides/adispi>>`__ // ADI Serial Control Interface Standard//
-  :adi:`AN-835 Application Note <an-835>`, *Understanding ADC Testing and Evaluation*

Software Needed
---------------

-  :adi:`VisualAnalog`
-  :adi:`SPIController </en/design-center/interactive-design-tools/spicontroller.html>`

Design and Integration Files
----------------------------

-  `SDP-H1 bin file (Unzip before use) <https://wiki.analog.com/_media/resources/eval/ad9467fmc/ad9467_sdp_h1.zip>`__
-  :doc:`Schematics, Bill Of Materials, and Gerber Layout/Fabrication Files </wiki-migration/resources/fpga/xilinx/fmc/ad9467>`

Equipment Needed
----------------

-  Analog signal source and antialiasing filter
-  Sample clock source
-  12V, 2.5A switching power supply connected to the data capture board (:adi:`SDP-H1`)
-  PC running Windows®
-  USB 2.0 port
-  :adi:`AD9467-FMC-250EBZ <AD9467>` board

::

   *[[:adi:`en/system-demonstration-platform/controller-boards/evaluation/EVAL-SDP-H1/eb`.html|SDP-H1]]  FPGA-based data capture kit

Getting Started
---------------

| This section provides quick start procedures for using the :adi:`AD9467-FMC-250EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9467.html#eb-overview>` board.

Configuring the Board
~~~~~~~~~~~~~~~~~~~~~

Before using the software for testing, configure the evaluation board as follows:

-  Connect the :adi:`AD9467-FMC-250EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9467.html#eb-overview>` evaluation board to the :adi:`SDP-H1` data capture board, as shown in Figure 2.
-  Connect one 12V, 2.5A switching power supply (such as the one supplied) to the :adi:`SDP-H1` board. Connect the Mini-B USB port of the :adi:`SDP-H1` board to the PC with the supplied USB cable.
-  The :adi:`SDP-H1 <en/system-demonstration-platform/controller-boards/evaluation/EVAL-SDP-H1/eb.html>` will appear in the Device Manager as shown in Figure 3. |image3|\

.. container:: centeralign

   
   //Figure 3. Device Manager Showing SDP-H1 //


-  If the Device Manager does not show the :adi:`SDP-H1` listed as shown in Figure 2, unplug all USB devices from the PC, uninstall and re-install SPIController and VisualAnalog and restart the hardware setup from step 1.
-  On the ADC evaluation board, provide a clean, low jitter 250MHz clock source to connector J201 and set the amplitude to 16dBm. This is the ADC Sample Clock.
-  On the ADC evaluation board, provide a clean, low jitter clock source to connector J100. Use a shielded, RG-58, 50Ohm, coaxial cable to connect the signal generator output to the ADC Evaluation Board. For best results, use a narrow-band, pass filter with 50Ohm terminations and appropriate center frequency. (ADI uses TTE, Allen Avionics, and K & L band-pass filters)\*.

::

             //*When connecting the ADC clock and analog source, use clean signal generators with low phase noise, such as Rohde & Schwarz SMA or HP8644B signal generators or equivalent*//

Visual Analog Setup
~~~~~~~~~~~~~~~~~~~

-  Click Start :math:`right` All Programs :math:`right` Analog Devices :math:`right` VisualAnalog :math:`right` VisualAnalog.
-  On the VisualAnalog “New Canvas” window, click **ADC** :math:`right` **Single** :math:`right` **AD9467** :math:`right` **FFT**.\ |image4|\

.. container:: centeralign

   
   //Figure 4. Selecting the AD9467 canvas *


\* If VisualAnalog opens with a collapsed view, click on the “Expand Display” icon (see Figure 5).\

.. container:: centeralign

   *\ Figure 5. Expanding the Display *


\* Click the* **Settings** *button in the* **ADC Data Capture** *block as shown in Figure 6\ \

.. container:: centeralign

   *\ Figure 6. Changing the ADC Capture Settings\ *


\* On the* **General** *tab make sure the clock frequency is set to* **250MHz** *(or other clock frequency). \

.. container:: centeralign

   *\ Figure 7. Setting the clock frequency and capture length\ *


\* Click on the* **Capture Board** *tab and browse to the* **ad9467_sdp_h1.bin** *file. Click the* **Program** *button. The* **FPGA_DONE** *LED should illuminate on the EVAL-SDP-CH1Z board indicating that the FPGA has been correctly programmed. The bin file is available at the ftp site* ftp://ftp.analog.com/pub/HSC_ADC_Apps/SDP-H1/ad9467_sdp_h1.bin\ *\* Click* **OK**\ *==== SPIController Setup ==== \* Click Start :math:`right` All Programs :math:`right` Analog Devices :math:`right` SPIController :math:`right` SPIController \

.. container:: centeralign

   *\ Figure 8. Control Window for AD9647\ *


\* Select the* **AD9467_16Bit_250MSspiR03.cfg** *if prompted. \* If necessary, click File :math:`right` Cfg Open :math:`right`* **AD9467_16Bit_250MSsspiR03.cfg**\ *\* To enable SPI communications, click File :math:`right` Config :math:`right`* **Controller Dialog** *and un-check the* **SDO Active** *button \

.. container:: centeralign

   *\ Figure 9. Un-Selecting SDO Active in SPIController\ *


==== Obtaining an FFT ==== \* Click the Run button in VisualAnalog , you should see the captured data similar to the plot shown in Figure 9

.. container:: centeralign

   *\ Figure 10. AD9467-FMC-250 FFT at 5MHz Analog Input\ *


\* Adjust the amplitude of the input signal so that the fundamental is at the desired level. (Examine the* **Fund Power** *reading in the left panel of the VisualAnalog FFT window). Usually about 16dBm of signal power from the signal generator will result in a -1dBFS Fundamental signal. \* To save the FFT plot do the following \* Click on the Float Form button in the FFT window\ \

.. container:: centeralign

   *\ Figure 11. Floating the FFT window//


-  Click on File :math:`right` Save Form As button and save it to a location of choice

Troubleshooting Tips
--------------------

\*\* FFT plot appears abnormal \*\*

-  If you see a normal noise floor when you disconnect the signal generator from the analog input, be sure you are not overdriving the ADC. Reduce input level if necessary.
-  In VisualAnalog, Click on the Settings button in the **Input Formatter** block. Check that **Number Format** is set to the correct encoding (Offset Binary by default).

\*\* The FFT plot appears normal, but performance is poor. \*\*

-  Make sure you are using the appropriate band-pass filter on the analog input.
-  Make sure the signal generators for the clock and the analog input are clean (low phase noise).
-  If you are using non-coherent sampling, change the analog input frequency slightly, or use coherent frequencies.
-  Make sure the SPI config file matches the product being evaluated.
-  Make sure there isn't any extra stress/torque on the clock and analog input connectors.

\*\* The FFT window remains blank after the Run button is clicked \*\*

-  Make sure the evaluation board is securely connected to the :adi:`SDP-H1`.
-  Make sure the FPGA has been programmed by verifying that the **FPGA_DONE** LED is illuminated on the EVAL-SDP-CH1Z. If this LED is not illuminated reprogram the FPGA through VisualAnalog. If the LED still does not illuminate disconnect the USB and power cord for 15 seconds. Connect again and repeat the :adi:`SDP-H1`\ setup process.
-  Make sure the correct FPGA *bin* file was used to program the FPGA.
-  Be sure that the correct sample rate is programmed. Click on the **Settings** button in the **ADC Data Capture** block in VisualAnalog, and verify that the **Clock Frequency** is properly set.
-  Ensure that the ADC has a valid clock input

AD9517-4 Configuration (Optional)
---------------------------------

The AD9467-FMC-250EBZ is configured from the factory to use an external clock connected to J201. Alternatively, the AD9467-FMC-250EBZ can be configured to use the on-board 250MHz oscillator and AD9517-4 Clock Generator to generate the 250 Msps clock input. (Note: some boards have shipped with a 25 MHz oscillator and will require a different configuration)

\*\* Hardware Modifications \*\*

::

    *Remove the following components: R209, R210, C209, C210
    *Add the following components: C205, C206, C300, C301, C304, C305
    *Make sure that Jumper P200 is on the "On" Position

**Additional Software Needed**

::

    *[[https://wiki.analog.com/_media/resources/eval/ad9467fmc/configure_ad9517_ad9467-fmc-250ebz_.zip|configure_ad9517_AD9467-FMC-250EBZ MGP file]]

\*\* Setup Instructions \*\*

-  Make sure that a clock source is not connected to J201
-  Configure SPIcontroller and VisualAnalog as described above
-  Launch a 2nd instance of SPIController.
-  Load the AD9517spiR03.cfg configuration file.
-  Click Config>Controller Dialog
-  Select "2" Under FIFO Chip Sel # |image5|\

.. container:: centeralign

   
   *Figure 12. Select Fifo Chip Sel # 2 in SPIController*\


-  Click Apply and OK
-  Click File>Macro Group Open
-  Select the configure_ad9517_AD9467-FMC-250EBZ .mgp file
-  Check the Enable Check Box |image6|\

.. container:: centeralign

   
   *Figure 13. Select Enable Macro in SPIController*\


-  Click Run Macros |image7|\

.. container:: centeralign

   
   *Figure 14. Click Run Macros in SPIController*\


-  Make sure that LED CR300 is illuminated on the AD9467-FMC-250EBZ.

\*\* Obtaining an FFT \*\*

-  Click the Run button in VisualAnalog , you should see the captured data similar to the plot shown in Figure 9


|image8|

.. container:: centeralign

   
   *Figure 15. AD9467-FMC-250 FFT at 140.3MHz Analog Input (performance may be degraded compared to high-quality direct clock)*\


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ad9467_board.png
   :width: 700px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ad9467_datacapture.png
   :width: 900px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/device_manger.png
   :width: 200px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/visualanalog_newcanvas.png
   :width: 650px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/ad9467fmc/SPI_Controller_Cfg_Dialog2.PNG
   :width: 262px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/ad9467fmc/MacroEditor-Enable.PNG
   :width: 375px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/ad9467fmc/run.PNG
   :width: 23px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/ad9467fmc/fft-ad9517.png
   :width: 736px
