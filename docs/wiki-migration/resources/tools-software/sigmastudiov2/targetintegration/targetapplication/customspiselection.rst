| :doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication>`
| =======Custom SPI Interface Selection (SPI0/SPI1/SPI2/SPI3)======= The SigmaStudioPlus application interacts with the target processor using the SPI communication protocol via USBi hardware.
| The default Demo/DemoUc/LibIntegration example projects, when run on ADI Eval Boards, are designed to use SPI1 for data transfer. This section provides guidance for users to use other available SPI peripherals for communication in the target application.
|

.. note::

   We are taking ADSP-SC594 Demo Application as reference for this Demonstration


The :doc:`Figure </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/customspiselection>` below shows the default SPI used (SPI1) and the pin-muxing configured in the example target applications provided by ADI.
| |image1|

.. container:: centeralign

   \ **Figure:** Default SPI Pin-Muxing in ADI's Example Target Application


| |image2|

.. container:: centeralign

   \ **Figure:** USBi Hardware's SPI Pinout


| In order to change the communication interface to another SPI peripheral, deselect the existing SPI1 pin configuration as shown below, and then follow the steps provided.
| |image3|

.. container:: centeralign

   \ **Figure:** Deselect SPI1 Configuration


| 
| =====Configuring SPI0 interface===== Changing the communication interface to SPI0, please follow the steps below.
| **Step 1:** Select the corresponding pins for SPI0 under Pin Multixing Tab as shown in below :doc:`Figure </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/customspiselection>`.
| |image4|

.. container:: centeralign

   \ **Figure:** Configuring pins for SPI0 as per requirement


On doing so, the SPI0 related pin muxing will be auto generated within **adi_initComponents() -> adi_initpinmux()** function.
| **Step 2:** In **adi_ss_app_control.c** file, under the **adi_ss_connection_initialize()** function, change the SPI device ID macro from the default **ADI_SS_SPI1_DEVICE** to **ADI_SS_SPI0_DEVICE**, as shown below.
| |image5|

.. container:: centeralign

   \ **Figure:** Configuring SPI0 during connection initialization phase


| With this, the software related changes are complete.
| **Step 3:** If the user is using ADI's Eval Boards (EV-SOM board, EV-SOMCRR-BRKOUT board, and EV-SOMCRR-EZKit board) along with the USBi hardware, the following hardware connections must be made for successful data transfer via SPI0.
| |image6|

.. container:: centeralign

   \ **Figure:** Connecting the USBi's pins to the EV-SOMCRR-BRKOUT board's **P4** connector to establish a hardware connection for SPI0.


| 
| =====Configuring SPI2 interface===== Changing the communication interface to SPI2, please follow the steps below.
| **Step 1:** Select the corresponding pins for SPI2 under Pin Multixing Tab as shown in below :doc:`Figure </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/customspiselection>`.
| |image7|

.. container:: centeralign

   \ **Figure:** Configuring pins for SPI2 as per requirement


On doing so, the SPI2 related pin muxing will be auto generated within **adi_initComponents() -> adi_initpinmux()** function.
| **Step 2:** In processor specific **adi_ss_softconfig** C file, change the default value of **SwitchConfig0**'s 1st element as shown below to enable SPI2's Flash and D2-D3 pins. |image8|

.. container:: centeralign

   \ **Figure:** Configuring Soft pins for SPI2


| **Step 3:** In **adi_ss_app_control.c** file, under the **adi_ss_connection_initialize()** function, change the SPI device ID macro from the default **ADI_SS_SPI1_DEVICE** to **ADI_SS_SPI2_DEVICE**, as shown below.
| |image9|

.. container:: centeralign

   \ **Figure:** Configuring SPI2 during connection initialization phase


| **Step 4:** After the initializing the connection, configure the SPI2's Control register such that the peripheral is set for data transmission and reception as shown in below :doc:`Figure </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/customspiselection>`. |image10|

.. container:: centeralign

   \ **Figure:** SPI2 Control Register Configuration


| With this, the software related changes are complete.
| **Step 5:** If the user is using ADI's Eval Boards (EV-SOM board, EV-SOMCRR-BRKOUT board, and EV-SOMCRR-EZKit board) along with the USBi hardware, the following hardware connections must be made for successful data transfer via SPI2.
| |image11|

.. container:: centeralign

   \ **Figure:** Connecting the USBi's pins to the EV-SOMCRR-BRKOUT board's **P3** connector to establish a hardware connection for SPI2.


| 
| =====Configuring SPI3 interface===== Changing the communication interface to SPI3, please follow the steps below.
| **Step 1:** Select the corresponding pins for SPI3 under Pin Multixing Tab as shown in below :doc:`Figure </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/customspiselection>`.
| |image12|

.. container:: centeralign

   \ **Figure:** Configuring pins for SPI3 as per requirement


On doing so, the SPI3 related pin muxing will be auto generated within **adi_initComponents() -> adi_initpinmux()** function.
| **Step 2:** In **adi_ss_app_control.c** file, under the **adi_ss_connection_initialize()** function, change the SPI device ID macro from the default **ADI_SS_SPI1_DEVICE** to **ADI_SS_SPI3_DEVICE**, as shown below.
| |image13|

.. container:: centeralign

   \ **Figure:** Configuring SPI3 during connection initialization phase


| With this, the software related changes are complete.
| **Step 3:** If the user is using ADI's Eval Boards (EV-SOM board, EV-SOMCRR-BRKOUT board, and EV-SOMCRR-EZKit board) along with the USBi hardware, the following hardware connections must be made for successful data transfer via SPI3.
| |image14|

.. container:: centeralign

   \ **Figure:** Connecting the USBi's pins to the EV-SOMCRR-BRKOUT board's **P1** connector to establish a hardware connection for SPI3.


|

.. note::

   With this, one must be able to Download SigmaStudioPlus schematic to Target ADSP-SC594 (example processor taken here) using SPI0/SPI2/SPI3 via USBi hardware.

   | Tests conducted with these changes:
   | • Download schematic to target
   | • MIPS read
   | • DSP Readback
   | • Tuning of audio processing modules in real-time.
   |


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/default_spi1_pinmuxing.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/usbi_hardware_pinout.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/deselect_spi1_copy.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/spi0_pinmuxing.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/spi0_connectinit.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/spi0_hardwareconnection.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/spi2_pinmuxing.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/spi2_softconfig.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/spi2_connectinit.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/spi2_regconfig.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/spi2_hardwareconnection.png
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/spi3_pinmuxing.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/spi3_connectinit.png
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/spi3_hardwareconnection.png
