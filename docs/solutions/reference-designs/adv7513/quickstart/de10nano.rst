.. _adv7513 quickstart de10nano:

DE10-Nano Quick Start
===============================================================================

.. image:: ../../images/de10nano.jpg
   :align: center
   :width: 600

This guide provides quick instructions on how to set up the ADV7513 HDMI
transmitter on `DE10-Nano <https://www.analog.com/en/resources/reference-designs/circuits-from-the-lab/terasic-de10-nano-kit.html>`__.

.. esd-warning::

Using Linux as software
-------------------------------------------------------------------------------

Necessary files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following files are needed for the system to work:

- :external+kuiper:doc:`Kuiper Linux <index>` SD card image
- :git-hdl:`HDL project files <projects/adv7513/de10nano>`

Instructions on how to build the files from source can be found here:

- More HDL build details at :external+hdl:ref:`build_hdl`

Required Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :external+kuiper:doc:`Kuiper Linux <index>`
- Host PC with SD card writer

Required Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `DE10-Nano <https://www.analog.com/en/resources/reference-designs/circuits-from-the-lab/terasic-de10-nano-kit.html>`__
  and its power supply
- MicroSD card (4 GB or larger)
- HDMI monitor
- HDMI cable
- USB cable (UART)
- Ethernet cable (optional, for SSH access)

More details as to why you need these can be found at
:ref:`adv7513 prerequisites`.

Setting up the SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`.

Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow the steps in this order, to avoid damaging the components:

#. Insert the MicroSD card into the DE10-Nano SD card slot
#. Connect an HDMI cable between the HDMI port on the DE10-Nano and the HDMI
   monitor
#. Connect the USB cable to the UART port on the DE10-Nano
#. Connect the Ethernet cable (optional)
#. Connect the power supply to the DE10-Nano
#. Turn on the HDMI monitor
#. Turn on the power switch on the DE10-Nano

Useful commands for the serial terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After the board boots, log in via UART terminal (115200 baud, 8N1) or SSH:

- Username: ``analog``
- Password: ``analog``

To find the IP address of the board:

.. shell::

   $ifconfig

To see the framebuffer device:

.. shell::

   $ls /dev/fb*
    /dev/fb0

To test the HDMI output with a color pattern:

.. shell::

   $cat /dev/urandom > /dev/fb0

To check the current display mode:

.. shell::

   $fbset
    mode "1920x1080-60"
        # D: 148.500 MHz, H: 67.500 kHz, V: 60.000 Hz
        geometry 1920 1080 1920 1080 32
        timings 6734 88 148 4 36 44 5
        accel false
        rgba 8/16,8/8,8/0,0/0
    endmode

To power off the board safely:

.. shell::

   $poweroff

To reboot the board:

.. shell::

   $reboot

.. important::

   This is a persistent file system. Care should be taken not to corrupt the
   file system — please shut down properly rather than cutting power
   abruptly. Use the ``poweroff`` command above, or
   ``sudo shutdown -h now``.

Support
-------------------------------------------------------------------------------

- :ref:`Help and Support <help-and-support>`
- :ez:`FPGA Reference Designs EngineerZone <community/fpga>`
