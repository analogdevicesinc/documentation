Production testing of the AD-FMCXMWBR1-EBZ
==========================================

Overview
--------

The production testing of AD-FMCXMWBR1-EBZ (DUT) is automated. The test procedure runs on ADRV9009-ZU11EG RF-SOM.

Required hardware
-----------------

-  Functional (tested) carrier :adi:`ADRV2CRR-FMC`
-  Functional (tested) :adi:`ADRV9009-ZU11EG RF-SOM` with heat plate and heat sink fitted
-  `TE150A1251F01 <https://www.digikey.com/en/products/detail/sl-power-electronics-manufacture-of-condor-ault-brands/TE150A1251F01/9856910>`__ Power supply (or similar)
-  SD card (inserted in the carrier) with testing procedure
-  Power rails cable (custom, available in the :adi:`AD-FMCXMWBR1-EBZ` kit)
-  `FFSD-20-D-12.00-01-N <https://www.digikey.com/en/products/detail/samtec-inc/FFSD-20-D-12-00-01-N/1106590>`__ ribbon cable (available in the :adi:`AD-FMCXMWBR1-EBZ` kit )
-  AD-FMCBRIDGE1A TEST BOARD
-  QR code scanner: QUICKSCAN QD2430 Datalogic
-  USB 3.0 4-Port Hub: Targus ACH154
-  Keyboard Microsoft X891041-008
-  Ethernet cable for network connection of ADRV2CRR-FMC
-  USB Adapter: USB Type C Plug, USB Type A Receptacle

Required software
-----------------

| For the test is needed an SD card with the Kuiper image that has the test procedure installed. If there is no such SD card available, it can be created.
| **Creating a carrier SD test card**

-  Write the latest available SD card image to a spare card and prepare the card to boot into Linux.

.. admonition:: Download
   :class: download

   \*\* Release february 2022 \*\*

   
   -   `Actual file <https://swdownloads.analog.com/cse/prod_test_rel/fmcbridge_test/adrv9009zu11eg_fmcbridge_prod_test_2022.img.xz>`__
   


.. tip::

   To write an image on a SD card you can follow the instructions :doc:`Zynq & Altera SoC Quick Start Guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

   


Required setup
--------------

-  First, the ADRV9009-zu11eg setup should be built. Please refer to the :doc:`ADRV9009-ZU11EG Quick Start Guide </wiki-migration/resources/eval/user-guides/adrv9009-zu11eg/quick-start-guide>`.
-  ADRV2CRR-FMC should be powered with the TE150A1251F01 power supply and connected to a network with the ethernet cable.
-  The screen is connected to ADRV2CRR-FMC through a display port cable. If there is no image shown on the screen at the first boot, please refer to the :doc:`guide </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynqmp>`.
-  Connect the USB OTG adapter and plug the USB Port Hub. In the Port hub will be connected the keyboard and the QR code scanner.
-  Plug the AD-FMCXMWBR1-EBZ into the FMC connector of the ADRV2CRR-FMC.

|TEST|

.. container:: centeralign

   Figure 1. AD-FMCXMWBR1-EBZ on carrier


::

   *

.. important::

   Make sure that the potentiometers R19, R2, R20 are adjusted to maximum . (After the last turn a click sound can be heard.)


   |image1|

.. important::

   Before testing, please make sure that P5, P6, P8, P39, P40, P50, P51 have jumpers connecting pin 1 and pin 2.


-  Use the cables to connect the AD-FMCXMWBR1-EBZ to the TEST BOARD



|image2|

.. container:: centeralign

   Figure 2. AD-FMCXMWBR1-EBZ test setup


Test process
------------

.. important::

   Make sure that the full setup is connected when powering up or rebooting the system.


After the connections are done as explained in the “Required setup for production test” power up by switching S12 of ADRV2CRR-FMC to on position. When booting, it is mandatory to have the full setup, with the AD-FMCXMWBR1-EBZ board connected. This way, the devices on the test board will be probed correctly at startup. The test instructions will prompt on the screen and the testing should be done using the following steps:

-  Select the appropriate command from the list. To start the test press 1 on the keyboard then press enter.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/1_test_procedure.png
   :align: center
   :width: 500px

-  Test procedure will start, then you will be asked to scan the QR/Barcode on the board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/2_test_procedure.png
   :align: center
   :width: 500px

-  The program will start, the tests are performed automatically and will show the message PASSED/FAILED at the end of the procedure.

|image3| |image4|

-  To test a another board, select option (2) to power off the setup, before using the physical switch and disconnecting AD-FMCXMWBR1-EBZ

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/5_test_procedure.png
   :align: center
   :width: 500px

Schematics and CAD files
------------------------

.. admonition:: Download
   :class: download

   
   ::
   
      *[[https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/fmc_bridge_testbrd_update.pdf|AD-FMCXMWBR1-EBZ test board Schematics]]
      *[[https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/test_board_ad-fmcxmwbr1.7z|AD-FMCXMWBR1-EBZ test board CAD files]]
   


.. |TEST| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/picture2.png
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/pot_adjustment.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/fmcxmw_testsetup.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/3_test_procedure.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/4_test_procedure.png
   :width: 300px
