.. _ad485x_fmcz quickstart zed:

ZedBoard Quickstart
===================

This guide provides quick instructions on how to set up the
:adi:`EVAL-AD4858` on:

- `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`__
  FMC LPC

.. image:: ../images/ad4858-zedboard-quick-setup.png
   :width: 900

.. esd-warning::

Hardware setup
--------------

.. note::

   As for the signal generator, you can use whichever Signal Generator you want.
   In this setup, we chose to use :adi:`M2K <adalm2000>` (with a
   :dokuwiki:`BNC adapter board <university/tools/m2k/accessories/bnc>`) as
   signal generator for channel 0, while testing the system in LVDS mode.
   Using :external+scopy:doc:`Scopy <index>`, we set the amplitude, frequency,
   offset and phase of the generated signals.

#. Connect the **EVAL-AD4858** evaluation board to the **Zedboard** carrier board.
#. Connect **M2K** to PC via Micro-B USB cable (provides power and data communication)
#. Connect **ZedBoard** UART port to PC via second Micro-B USB cable (for serial monitoring)
#. Connect 2x BNC to SMA cables from SMA0+/- (**EVAL-AD4858**) to W1/W2 (BNC adapter board)
#. Configure **Zedboard** for SD BOOT by placing the jumpers: **JP7** on pins 1-2,
   **JP8** on pins 2-3, **JP9** on pins 2-3 , **JP10** on pins 1-2 and **JP11** on pins 1-2.

   See picture below.

   .. image:: ../images/jumpers_boot_sd_zedboard.jpg
      :width: 400

#. Connect a signal generator.
#. Turn on the power switch on the carrier board using **SW8**.
#. Observe kernel and serial console messages on your terminal. (Use the first
   ttyUSB or COM port registered, Baud rate 115200 (8N1))

Messages
--------

.. admonition:: Info

   This specifies any shell prompt running on the target

.. collapsible:: Complete boot log

   .. shell::
      :show-user:

      Xilinx Zynq MP First Stage Boot Loader

      TBD

Make sure all devices are present
----------------------------------

.. admonition:: Info

   This specifies any shell prompt running on the target

.. shell::
   :show-user:

   .. TBD. Below is an example:

   ..   root@analog:~# iio_info | grep iio:device
         iio:device0: ams
         iio:device1: hmc7044-car
         iio:device2: adm1177
         iio:device3: hmc7044
         iio:device4: adrv9009-phy
         iio:device5: adrv9009-phy-b
         iio:device6: axi-adrv9009-rx-obs-hpc (buffer capable)
         iio:device7: axi-adrv9009-tx-hpc (buffer capable)
         iio:device8: axi-adrv9009-rx-hpc (buffer capable)

IIO Oscilloscope Remote
-----------------------

The :dokuwiki:`IIO Oscilloscope <resources/tools-software/linux-software/iio_oscilloscope>`
application can be used to connect to another platform that has a connected
device in order to configure the device and read data from it.
