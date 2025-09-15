Software User Guide
===================

Required Hardware
~~~~~~~~~~~~~~~~~

- **Development kit**: :adi:`AD-SWIOT1L-SL` Software-configurable Analog and Digital I/O with 10BASE-T1L
- **Power supplies**: 24V power supply at minimum 2A
- **Programmer**: :adi:`MAX32625PICO` or any other similar programmer supporting the SWD interface

System Setup
------------

- Connect the AD-SWIOT1L-SL to the AD-T1LUSB2.0-EBZ using the single pair Ethernet cable.
- Connect the AD-T1LUSB2.0-EBZ to your PC using an USB cable.
- Connect the 24 V power supply to the AD-SWIOT1L-SL.

.. figure:: picture1.jpg
   :width: 600 px
   :align: center

   AD-SWIOT1L-SL Hardware Setup

.. figure:: picture3.jpg
   :width: 600 px
   :align: center

   Connecting the :adi:`MAX32625PICO` Programmer

.. clear-content::
   :side: both
   :break:

Software Setup
--------------

The system is accompanied by an open-source software stack and associated
collateral, enabling a complete experience from evaluation and prototyping all
the way to production firmware and applications development.

The :dokuwiki:`Scopy <university/tools/m2k/scopy/plugins/swiot1l>` PC application
provides system configuration and data visualization tools to enable easy system
evaluation from a PC connected to the AD-SWIOT1L-SL via the 10BASE-T1L
interface.

The :git-no-OS:`AD-SWIOT1L-SL firmware <projects/swiot1l>` is
based on Analog Devices’ open-source no-OS framework, which includes all the
tools required for embedded code development and debugging as well as libraries
enabling host-side connectivity for system configuration and data transfer over
the UART or the 10BASE-T1L interfaces. The firmware source code and related
documentation can be found on the Analog Devices GitHub at the link above.

.. important::

   The system comes pre-programmed with a firmware that
   works with the **Scopy** application, allowing complete system evaluation.

   The firmware should be updated only to switch to a newer version or as part of
   the software development process.

   **Scopy** will work only with the official
   :git-no-OS:`AD-SWIOT1L-SL firmware releases <releases/tag/swiot1l-v0.1+>`

Updating the AD-SWIOT1L-SL Firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To update the board’s firmware, a new bootloader has to be flashed on the
MAX32625PICO.

#. Download the firmware image: `MAX32625PICO firmware <https://github.com/MaximIntegrated/max32625pico-firmware-images/raw/master/bin/max32625_max32650fthr_if_crc_swd_v1.0.6.bin>`__
#. Set the MAX32625PICO in MAINTENANCE mode:

   * Disconnect the MAX32625PICO from the PC and the AD-SWIOT1L-SL board.
   * Plug the micro USB cable only in the MAX32625PICO.
   * Keep the button on the MAX32625PICO pressed.
   * Plug the micro USB cable into the PC.
   * Once you see the MAINTENANCE drive being mounted, you may release the button.

     .. figure:: picture2.jpg
        :width: 300 px

        MAX32625PICO Button

#. Drag and drop (to the MAINTENANCE drive) the firmware image you previously downloaded.
#. After a few seconds, the MAINTENANCE drive will disappear and will be replaced
   by a drive named DAPLINK. Once this is done, the process is complete, and the
   MAX32625PICO may be used to flash the firmware of the AD-SWIOT1L-SL board.

Programming the AD-SWIOT1L-SL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Connect the MAX32625PICO to the PC using the micro USB cable.
- Connect the MAX32625PICO to the AD-SWIOT1L-SL board using the 10-pin ribbon cable.
- Connect the 24 V power supply to the AD-SWIOT1L-SL. Make sure the board is powered up for the next steps.

.. figure:: img_20230912_145550.jpg

   AD-SWIOT1L-SL Programming Setup

* A DAPLINK drive should appear as mounted on your PC.
* Drag and drop the new firmware image into the DAPLINK drive. After a few seconds, the drive will be remounted.
* Check the DAPLINK directory and make sure there is no FAIL.TXT file. In case
  there is, repeat the drag and drop step. Otherwise, you may disconnect the
  MAX32625PICO from the AD-SWIOT1L-SL, since the firmware update is complete.
