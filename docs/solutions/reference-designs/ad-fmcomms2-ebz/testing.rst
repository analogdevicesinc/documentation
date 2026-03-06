.. _ad-fmcomms2-ebz-testing:

Production Testing
===================

The production testing is designed to look for gross errors on boards that have
been completely characterized. Multiple test files exist for different boards
(all available in the pyadi-iio GitHub repository):

- ``test_fmcomms2-3_prod.py`` - for AD-FMCOMMS2-EBZ and AD-FMCOMMS3-EBZ
- ``test_fmcomms4_prod.py`` - for AD-FMCOMMS4-EBZ
- ``test_fmcomms5_prod.py`` - for AD-FMCOMMS5-EBZ

The tests cover the following sections: temperature, voltage, RF, peaks,
DCXO, and loopback.

Required Hardware
-----------------

- Zynq ZC706 carrier board
- Raspberry Pi 4
- :adi:`AD-FMCOMMS2-EBZ` (or AD-FMCOMMS3/4/5-EBZ) card
- RF loopback cables (2x for FMCOMMS2/3/4, 4x for FMCOMMS5)
- External monitor connected to Raspberry Pi via micro HDMI
- Keyboard and mouse (with USB hub if not a combo device)
- Ethernet cable (internet connection required)
- QR code scanner
- For FMCOMMS2/3/4: frequency counter with USB-GPIB port (tested with Hameg
  Instruments HM8123) with probe and grounding clip attachment

Required Software
-----------------

**ZC706 carrier SD test card**: Write the latest available SD card image for the
specific board variant.

**Raspberry Pi SD test card**: Based on Raspbian with desktop.

Setup
-----

.. figure:: setup_1.1.png
   :align: center

   Production test setup

#. Attach the RF loopback cables to the board (see loopback placement below).
#. Insert the SD card into the carrier board.
#. Insert the FMCOMMS board onto the carrier.
#. Connect the HDMI cable to Raspberry Pi.
#. Connect USB keyboard to Raspberry Pi.
#. Insert SD card into Raspberry Pi.
#. Connect Ethernet cable between Raspberry Pi and the carrier.
#. Connect the scanner to Raspberry Pi.
#. Connect the frequency counter to Raspberry Pi.
#. Power the carrier board and Raspberry Pi.

.. figure:: picture2.png
   :align: center

   Test hardware connections

.. figure:: frequency_counter.png
   :align: center
   :width: 600

   Frequency counter probe connection

Before testing, add a QR code sticker with the serial number:

.. figure:: qr_code.png
   :align: center

   QR code placement

Test Process
------------

#. Power the carrier board and the Raspberry Pi. The test menu will appear.

   .. figure:: test_1.png
      :align: center

      Test menu screen

#. Start the DCXO test by entering ``1`` in the terminal. The connection with
   the DUT is verified first.

   .. figure:: test_2.png
      :align: center

      DUT connection verification

#. Scan the QR code on the board when prompted.

#. If the DCXO test passes:

   .. figure:: test_4.png
      :align: center

      DCXO test passed

#. Start the board-specific test by entering ``2`` in the terminal.

   .. figure:: test_5.png
      :align: center

      Board test start

#. The tests will run automatically:

   .. figure:: test_6.png
      :align: center

      Test in progress

#. On success:

   .. figure:: test_7.png
      :align: center

      All tests passed

#. On failure, the specific failing test is indicated. The test can be
   repeated immediately:

   .. figure:: test_8.png
      :align: center

      Test failed

#. After completing testing, power off the carrier by entering ``4``. After
   several seconds, turn off the carrier board using the physical switch.
#. Power off the Raspberry Pi by entering ``3``.

.. warning::

   Always power off the ZC706 and Raspberry Pi from the terminal before
   unplugging power, otherwise the SD cards can be corrupted.

RF Loopback Cable Placement
----------------------------

.. list-table::
   :header-rows: 1

   * - FMCOMMS2/3
     - FMCOMMS4
     - FMCOMMS5
   * - .. image:: fmcomms3-loopback.jpg
     - .. image:: fmcomms4-loopback.jpg
     - .. image:: fmcomms5-loopback.jpg
