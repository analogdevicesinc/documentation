ARRADIO Terasic C5 SoCkit Quick Start Guide
===========================================

|image1| This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the ARRADIO board on `Terasic C5 SoCkit <https://www.arrow.com/en/products/sockit/arrow-development-tools>`_

Prerequisites
-------------

Required Hardware
~~~~~~~~~~~~~~~~~

-  `Terasic C5 SoCkit <https://www.arrow.com/en/products/sockit/arrow-development-tools>`_
-  `ARRADIO <https://www.arrow.com/en/products/arradio/terasic-technologies>`_ board
-  An 8GB Micro-SD Card
-  USB keyboard and mouse
-  OTG Cable (for the USB keyboard and mouse)
-  A VGA compatible monitor
-  Ethernet cable
-  1 x Micro-USB cable

Required Software
~~~~~~~~~~~~~~~~~

-  You need a Host PC (Linux)
-  A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1)
-  `IIO Oscilloscope <https://github.com/analogdevicesinc/iio-oscilloscope/releases>`_

Creating the Micro-SD Card
--------------------------

.. tip::

   \ `Create SD Image for Terasic C5 SoCkit board. (it is a single image for all boards). <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_\

Required files
~~~~~~~~~~~~~~

The root of 'BOOT' should contain the following files:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  ``socfpga.dtb``
-  ``zImage``
-  ``u-boot.scr``
-  ``soc_system.rbf``

The root of preloader partition should contain the following file:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  ``preloader_bootloader.img``

Configuring the Micro-SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   analog@analog:~ $ lsblk

   NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
   sdb           8:16   1 29.7G  0 disk
   ├─sdb1        8:17   1    1G  0 part /media/analog/BOOT
   ├─sdb2        8:18   1  9.8G  0 part /media/analog/rootfs
   └─sdb3        8:19   1    4M  0 part

   analog@analog:~ $ cd /media/analog/BOOT/socfpga_cyclone5_sockit_arradio
   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ ls -l

   total 10248
   -rwxr-xr-x 1 root root  500432 Jul 27 15:06 preloader_bootloader.img
   -rwxr-xr-x 1 root root   25291 Jul 27 15:06 socfpga.dtb
   -rwxr-xr-x 1 root root 2685848 Jul 27 15:06 soc_system.rbf
   -rwxr-xr-x 1 root root     200 Jul 27 15:06 u-boot.scr
   -rwxr-xr-x 1 root root 7269944 Jul 27 15:06 zImage

   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ sudo cp socfpga.dtb /media/analog/BOOT/socfpga.dtb
   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ sudo cp zImage /media/analog/BOOT/zImage
   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ sudo cp u-boot.scr /media/analog/BOOT/u-boot.scr
   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ sudo cp soc_system.rbf /media/analog/BOOT/soc_system.rbf
   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ sudo dd if=preloader_bootloader.img of=/dev/sdb3

   977+1 records in
   977+1 records out
   500432 bytes (500 kB, 489 KiB) copied, 0.138791 s, 3.6 MB/s

   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ sync
   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ cd ../../
   analog@analog:/media/analog $ sudo umount /dev/sdb1
   analog@analog:/media/analog $ sudo umount /dev/sdb2
   analog@analog:/media/analog $ lsblk

   NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
   sdb           8:16   1 29.7G  0 disk
   ├─sdb1        8:17   1    1G  0 part
   ├─sdb2        8:18   1  9.8G  0 part
   └─sdb3        8:19   1    4M  0 part

--------------

Setting up the hardware (Terasic C5 SoCkit)
-------------------------------------------

You will need to:

- Get the ` Terasic C5 SoCkit <https://www.arrow.com/en/products/sockit/arrow-development-tools >`_

|resources-eval-user-guides-arradio-quickstart-terasic_c5_sockit.jpg|

- Insert the Micro-SD Card into the Micro-SD Card  Connector
- Connect the ARRADIO board to the FPGA carrier HSMC connector
- Plug your monitor device into the VGA Video Connector
- Plug your USB mouse/keyboard into the USB 2.0 OTG Port
- Plug the Power Supply into 12V Power Supply connector (DO NOT turn the device on)
- Set the jumpers according to the following table:

======= ========= ========= ======== ======== ========
\       CLOCKSEL0 CLOCKSEL1 BOOTSEL0 BOOTSEL1 BOOTSEL2
======= ========= ========= ======== ======== ========
**POS** 2-3       2-3       2-3      2-3      1-2
======= ========= ========= ======== ======== ========

+--------------+

| JP2          |

+==============+

| 2.5V or 1.8V |

+--------------+

======= ===== ===== ===== ===== ===== =========
SW6     MSEL0 MSEL1 MSEL2 MSEL3 MSEL4 CODEC_SEL
======= ===== ===== ===== ===== ===== =========
**POS** 0     1     0     1     0     0
======= ===== ===== ===== ===== ===== =========

.. esd-warning::

Booting the Micro-SD Card
-------------------------

Local IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~

::

   -Ignore your PC, and now interact on the USB mouse/keyboard on the Terasic C5 SoCkit device
   -You should see two screens:

.. image:: ../images/print_iio_linux_arradio_c5soc.png
   :alt: print_iio_linux_arradio_c5soc.png
   :align: center
   :width: 700

Remote IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~~

::

   -Connect USB UART (Micro USB) to your host PC.
   -Plug your ethernet cable into the RJ45 ethernet connector
   -Run the ifconfig command on your UART terminal and get your board IP

::

   root@analog:~# ifconfig

   eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
           inet your_board_ip  netmask 255.255.255.0  broadcast
           inet6 fe80::e6e7:b2c:f962:dc57  prefixlen 64  scopeid 0x20<link>
           ether 1c:76:ca:01:23:45  txqueuelen 1000  (Ethernet)
           RX packets 25208  bytes 4726181 (4.5 MiB)
           RX errors 0  dropped 0  overruns 0  frame 0
           TX packets 5987  bytes 2260634 (2.1 MiB)
           TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
           device interrupt 29  base 0x2000

::

   -Open IIO Scope application and type ip:board_ip in the URI tab.

.. image:: ../images/iio_remote_c5soc_arradio.png
   :alt: iio_remote_c5soc_arradio.png
   :align: center
   :width: 600

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with ``sudo shutdown -h now``

   |image2|

More Information
----------------

-  :doc:`ARRADIO User Guide </solutions/reference-designs/arradio/index>`

Useful links
------------

-  `AD9081/AD9082/AD9988/AD9986 Quick Start Guides <https://wiki.analog.com/resources/eval/user-guides/ad9081_fmca_ebz/quickstart>`_

   -  `Zynq-7000 SoC ZC706 Quick Start Guide <https://wiki.analog.com/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynq>`_
   -  `Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide <https://wiki.analog.com/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynqmp>`_
   -  `Virtex UltraScale+ VCU118 Quick Start Guide <https://wiki.analog.com/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/microblaze>`_
   -  `Versal ACAP VCK190 Quick Start Guide <https://wiki.analog.com/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/versal>`_
   -  `Arria10 SoC Quick Start Guide <https://wiki.analog.com/resources/eval/user-guides/ad9081/quickstart/a10soc]>`_

-  `AD9081-FMCA-EBZ (Single MxFE) HDL Reference Design <https://wiki.analog.com/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_fmca_ebz_hdl>`_

   -  `ADI Reference Designs HDL User Guide <https://wiki.analog.com/resources/fpga/docs/hdl>`_
   -  `Generic JESD204B block designs <https://wiki.analog.com/resources/fpga/docs/hdl/generic_jesd_bds>`_
   -  `JESD204B High-Speed Serial Interface Support <https://wiki.analog.com/resources/fpga/peripherals/jesd204>`_

-  `AD9081/AD9082/AD9988/AD9986 Linux Driver Support <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`_

::

         - `JESD204 (FSM) Interface Linux Kernel Framework <https://wiki.analog.com/resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>`_
         - `HMC7044 Clock Jitter Attenuator with JESD204B Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-pll/hmc7044>`_
         - `AXI-DMAC DMA Controller Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/axi-dmac>`_
         - `JESD204B Transmit Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`_
           - `JESD204B Status Utility <https://wiki.analog.com/resources/tools-software/linux-software/jesd_status>`_ 
         - `JESD204B Receive Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`_
           - `JESD204B Status Utility <https://wiki.analog.com/resources/tools-software/linux-software/jesd_status>`_ 
         - `JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`_
           - `JESD204 Eye Scan <https://wiki.analog.com/resources/tools-software/linux-software/jesd_eye_scan>`_
         - `AXI ADC HDL Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`_
         - `AXI DAC HDL Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`_
   * `MATLAB Support <https://wiki.analog.com/resources/tools-software/hsx-toolbox>`_
        * MATLAB support is provided through the `High Speed Converter Toolbox <https://wiki.analog.com/resources/tools-software/hsx-toolbox>`_
   * `Python Support <https://wiki.analog.com/resources/tools-software/linux-software/pyadi-iio>`_
        * PYTHON support is provided through the `Device Specific Python Interfaces For IIO Drivers <https://wiki.analog.com/resources/tools-software/linux-software/pyadi-iio>`_ 
        * `PyADI-IIO Documentation <https://analogdevicesinc.github.io/pyadi-iio/>`_
        * `AD9081 class documentation <https://analogdevicesinc.github.io/pyadi-iio/devices/adi.ad9081.html>`_
   * Product Datasheet
       * :adi:`AD9081 <media/en/technical-documentation/data-sheets/AD9081.pdf>`
       * :adi:`AD9082 <media/en/technical-documentation/data-sheets/AD9082.pdf>`
       * :adi:`AD9988 <media/en/technical-documentation/data-sheets/AD9988.pdf>`
       * :adi:`AD9986 <media/en/technical-documentation/data-sheets/AD9986.pdf>`
   * :adi:`UG-1578, Device User Guide <media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578.pdf>`
   * :adi:`UG-1829, Evaluation Board User Guide <media/en/technical-documentation/user-guides/ad9081-fmca-ebz-9082-fmca-ebz-ug-1829.pdf>`

Support
-------

Analog Devices will provide limited online support for anyone using the reference design with Analog Devices components via the :ez:`EngineerZone <community/fpga>`.

Software support
----------------

-  `AD9081/AD9082/AD9988/AD9986 Linux Driver Support <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`_

.. |image1| image:: ../images/terasic_c5_sockit_arradio.jpg
   :width: 550
.. |image2| image:: ../images/shutdown.png
   :width: 300

.. |resources-eval-user-guides-arradio-quickstart-terasic_c5_sockit.jpg| image:: ../images/terasic_c5_sockit.jpg
