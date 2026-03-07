Troubleshooting Guide for ADI Kuiper Linux for ACE Evaluation
=============================================================

If you are having problems connecting to an ADI Product Evaluation Board on a supported Linux platform with ACE, the following suggestions may help. This guide will cover common issues seen for the ZedBoard and CoraZ7. If your issue is not addressed here, please search in the EngineerZone forums, and ask a question in the corresponding product support forum.

.. note::

   Ensure your Product Evaluation Board is supported by ADI Kuiper Linux for ACE Evaluation. You can search for Product Evaluation board information using :adi:`evaluation-boards-kits.html <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits.html>` - look for references to ACE Linux support in these search results


It is also important that your software stack is up to date - ADI is committed to continually improving and updating our software.

-  ADI Kuiper Linux for ACE Evaluation SD Card - The latest release and how to create an SD card image is here: :doc:`ADI Kuiper Linux for ACE Evaluation </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images_for_ace>`
-  ACE Application - Use the 'Check For Updates' option in the ACE sidebar
-  ACE Evaluation Board Plug-ins - Open the 'Plug-in Manager' using the option in the ACE sidebar, and select 'Available Updates' and click refresh. Use the search field (magnifying glass) to filter relevant updates.

ZedBoard Hardware
-----------------

POWER Green LED does not turn on
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This LED indicates that the 12V is present and SW8/POWER is turned on.

**Solution:** Check the mains power adapter is properly plugged in and mains power is turned on, and switch SW8/POWER is in the 'ON' position.

DONE Blue LED does not turn on
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This LED indicates that the FPGA has been programmed during the boot process. If this LED does not turn on, it indicates the the FPGA has not been programmed. It may take 20-30 seconds for this LED to turn on - Linux versions post October 2024 enable this LED at the end of the boot process. For earlier versions this LED can turn on almost immediately.

**Solution:** Check the boot mode jumpers are set to select the SD Card as the primary boot device, per the table below, and that the SD Card is correctly orientated and fully inserted into the card slot on the underside of the board.

============ ========= ========= ======== ======== ========
**Jumper**   JP11/MIO6 JP10/MIO5 JP9/MIO4 JP8/MIO3 JP7/MIO2
============ ========= ========= ======== ======== ========
**Position** GND       3V3       3V3      GND      GND
============ ========= ========= ======== ======== ========

The SD card image may not be correct or may have been corrupted. Follow the instruction here to re-image the card: :doc:`ADI Kuiper Linux for ACE Evaluation </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images_for_ace>`

No Red LED flashes
~~~~~~~~~~~~~~~~~~

At least one Red LED should (LD0) start to flash 20-30 seconds after powering on the Zedboard to indicate that the boot process is complete, and the system is ready for use.

.. note::

   For ADI Kuiper Linux for Evaluation versions prior to Version:2024-08-27 LD7 will blink to indicate boot is complete. For versions after this release, and depending on the connected evaluation-board, other RED LED's may also blink to indicate various status information - see the individual eval-board guides for further details. If both LD0 and LD1 are blinking, this indicates that an existing configuration has been restored.


**Solution:** The SD card image may not be correct or may have been corrupted. Follow the instruction here to re-image the card: :doc:`ADI Kuiper Linux for Evaluation </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images_for_ace>`

LD11 Orange LED is Continuously on
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LD11 Orange LED is the USB UART activity light that flashes on to indicate when there is serial traffic on the UART. In some cases, typically when the board is being rebooted, this LED may remain on continuously, that corresponds to the board failing to reboot.

**Solution:** A physical reset of the ZedBoard is required, either by pressing BTN6/PS-RST or by power cycling with SW8/POWER.

Cora Z7 Hardware
----------------

POWER Red LED (LD7) does not turn on
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This LED indicates that the 5V is present from the USB.

**Solution:** Check the USB is connected correctly and that the correct Jumper configuration is set

+-----------------+--------------------------------------------------------------------------------+---------------------------------+
| Jumper Location | Description                                                                    | Shunt Placement                 |
+=================+================================================================================+=================================+
| JP3             | Selects how the CoraZ7-07s board is powered. We are powering from the USB port | Across Pins 3 & 2 (labeled USB) |
+-----------------+--------------------------------------------------------------------------------+---------------------------------+

DONE Green LED (LD6) does not turn on
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This LED indicates that the FPGA has been programmed during the boot process. If this LED does not turn on, it indicates the FPGA has not been programmed. It may take 20-30 seconds for this LED to turn on.

**Solution:** Check the boot mode jumpers are set to select the SD Card as the primary boot device, per the table below, and that the SD Card is correctly orientated and fully inserted into the card slot on the underside of the board.

+-----------------+-------------------------------------------------------------------------------+-------------------+
| Jumper Location | Description                                                                   | Shunt Placement   |
+=================+===============================================================================+===================+
| JP2             | Selects how the CoraZ7-07s board boots. We want to boot from the microSD card | Across Pins 1 & 2 |
+-----------------+-------------------------------------------------------------------------------+-------------------+

The SD card image may not be correct or may have been corrupted. Follow the instruction here to re-image the card: :doc:`ADI Kuiper Linux for ACE Evaluation </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images_for_ace>`

No Green LED (LD1) flashes
~~~~~~~~~~~~~~~~~~~~~~~~~~

The Green LED (LD1) should start to flash 20-30 seconds after powering on the CoraZ7 to indicate that the boot process is complete, and the system is ready for use.

**Solution:** The SD card image may not be correct or may have been corrupted. Follow the instruction here to re-image the card: :doc:`ADI Kuiper Linux for Evaluation </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images_for_ace>`

No Green LEDs (LD2 & LD3)
~~~~~~~~~~~~~~~~~~~~~~~~~

LD2 and LD3 Green LEDs indicate link status and activity of the Ethernet port. This Ethernet connection is what ACE uses to connect to the CoraZ7.

**Solution:** Ensure the Ethernet cable is connected correctly. Else a power cycle of the board may be needed to reinitialise the Ethernet connection.

ACE Software
------------

Evaluation Board does not appear in 'Attached Hardware' view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No button appears in the 'Attached Hardware' view on the Start tab representing the Product Evaluation Board attached to the host controller board.

**Solution 1:** Try clicking the 'Refresh Attached Hardware' button in the 'Attached Hardware' section of the ACE window, also, try unplugging and re-plugging the USB device and restarting ACE.

**Solutions 2:** If you're using a ZedBoard/CoraZ7, additional driver support is required. A correctly configured host controller board running the ADI Kuiper Linux for ACE Evaluation image should be visible in the Windows Device Manager under Network adapters - ADI USB Ethernet/RNDIS Gadget

.. note::

   For ADI Kuiper Linux for Evaluation for the ZedBoard versions prior to Version:2024-08-27, a correctly configured host-controller board running the ADI Kuiper Linux for ACE evaluation image should be visible as a number of USB gadgets. Looking at the hardware shown under the 'USB Serial Bus Devices' node in the Windows Device Manager, there should be an 'IIO' child node, and under the 'Ports (COM & LPT) one or more serial ports that are part of a composite USB device. Selecting one of these devices, and choosing the View >> Devices by Connection menu option will show them as group.


If the expected gadget(s) are not shown, ensure the USB micro-B cable is connected to J13/USB_OTG port on the ZedBoard or for the CoraZ7 ensure the Ethernet cable is connected. If one or more of these USB gadgets have warning icon overlays, then the drivers may need to be installed and/or updated. Latest drivers are available :doc:`here </wiki-migration/university/tools/pluto/drivers/windows>` and a link to the version provided with ACE can be found by pressing the 'Help' button, and looking in the 'Application Resources >> IIO Resources' panel section.

**Solution 3:** An Ethernet connection (either via USB OTG or Ethernet) is required for ACE to connect to the ZedBoard / CoraZ7. An IIO Context must be available for this connection. Confirm that this context is available across the Ethernet connection by opening up a Windows Command Prompt (cmd) and typing ``iio_attr -S`` This should return something like the following

::

   Available contexts:
           0: 169.254.AB.CD (EVAL-ADXXXX-FMCZ on Xilinx Zynq ZED), serial=Empty Field [ip:analog.local]

.. note::

   For ADI Kuiper Linux for Evaluation versions prior to Version:2024-08-27, the connection is a USB IIO Gadget and the context should look something like the following


\ ``Available contexts:
        0: 0456:b678 (Analog Devices Inc. ADI Linux Platform), serial=00000000 [usb:3.37.6]`` If a context is not returned, try power-cycling the controller board and re-trying to get the context

No matching plug-in found or Generic IIO plug-in used
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A button appears in the 'Attached Hardware' view on the Start tab representing the Product Evaluation Board attached to the host controller board, but on double-clicking the button ACE reports that no matching plug-in is installed or a generic IIO plug-in is opened instead.

**Solution:** If the board is supported in ACE for used with the ADI Kuiper Linux for ACE Evaluation image, then using the plug-in manager search for the board plug-in and install it from within ACE. If the board is not supported, but is running an IIO software stack, then the Generic IIO board plug-in may be used to provide basic functionality.
