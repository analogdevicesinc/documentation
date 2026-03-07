Windows Drivers
===============

There are different aspects of the software for the ADALM-PLUTO and ADALM2000:

-  device drivers, which allows your PC to properly set up communication between your PC and the actual device, and
-  application code, like MATLAB, Simulink, GNU Radio, iio-oscilloscope (aka osc), or scopy.

To install the drivers, it's a simple matter of downloading and executing the driver installer.

.. important::

   Before running the installer, please ensure that the hardware supported by the drivers is not already connected. If the hardware is connected when the installer is run, the installation of the driver files may fail.


.. admonition:: Download
   :class: download

   This download should support all of: Windows 11, Windows 10, Windows 8.1, Windows 8, Windows 7 Service Pack 1. If you run into issues, please :ez:`let us know <community/university-program>`.

   
   -  :git-plutosdr-drivers-win:`Windows USB drivers for PlutoSDR and M2k (Windows 32-bit / 64-bit) <releases>`
   


At the end, you should see a picture like (either for Pluto or M2k):

|image1| |image2| |image3|

DFU Mode
--------

If you don't see the above, and see something like this instead, this means the device is in :doc:`firmware#dfu_update </wiki-migration/university/tools/pluto/users/firmware>` mode. It's likely in this mode since a bad firmware is in the device; or a firmware update failed for some reason. To recover from this, ensure the latest firmware is installed on the device.

.. image:: https://wiki.analog.com/_media/university/tools/pluto/drivers/dfu.png
   :width: 300px

--------------

Drivers uninstall
-----------------

From the control panel navigate to Programs and Features. Double click or right click and select Uninstall. Uninstalling the PlutoSDR-M2k-USB-Win-Drivers package will automatically remove the Windows Driver Packages (USBser, WinUSB and Net) shown below as well.

.. image:: https://wiki.analog.com/_media/university/tools/pluto/drivers/drivers-uninst.png
   :align: center
   :width: 800px

USB Devices
-----------

Once the drivers are installed, and the device (Pluto or M2k) is plugged in, the following subsystems should be ready to use:

-  USB Composite Device (The device is a single USB gadget that has the ability to perform more than one function, and needs to be exposed to the operating system as multiple devices)
-  USB Ethernet/RNDIS Gadget (Remote Network Driver Interface Specification (`RNDIS <https://en.wikipedia.org/wiki/RNDIS>`_) is a Microsoft proprietary protocol used mostly on top of USB. It provides a virtual Ethernet link to most versions of the Windows, Linux and OS X operating systems. To the host, the usb device acts as an external Ethernet card)
-  USB Mass Storage (`USB Mass Storage <https://en.wikipedia.org/wiki/USB_mass_storage_device_class>`_ is a set of protocols defined by the USB Implementers Forum that makes a USB device accessible to any host computing device and enables file transfers between the host and the USB device. To a host, the USB device acts as an external hard drive.)
-  Serial Console (115200-8N1), in this case COM15, but it will be different on your PC.
-  IIO USBD
-  Linux File-Stor Gadget USB Device (which allows the USB mass storage to work properly).

Serial
------

You need to have find your favorite Terminal program, here are a few of the ones we use (but don't support - if you have questions, please check with the internet/google).

-  `Putty <http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>`_
-  `Tera Term <https://en.osdn.jp/projects/ttssh2/releases/>`_
-  Or other Terminal program

The terminal settings are 115200 baud, 8 bits, no parity, 1 stop bit. This is referred to as 115200-8N1. The default username is ``root``, and the default root password is ``analog``.

Finding the serial port (which constantly changes, every time you plug a device in), is just matter of checking device manager (see above).

Mass Storage
~~~~~~~~~~~~

It should be a simple matter of opening the drive, in this case, double click on "D", to get at the info.html page.

.. image:: https://wiki.analog.com/_media/university/tools/pluto/drivers/pluto_drive.png
   :align: center

Ethernet
--------

Ethernet Warning
~~~~~~~~~~~~~~~~

.. warning::

   Like most of the network settings on Pluto or the M2k - things are meant to be easy to use. This also means things are inherently insecure.

   
   For example - the root password of Pluto is ``analog``. We post it on the Internet. Think about that for a moment. This could allow anyone with an IP connection to take over the device and use it for malicious purposes.
   
   **Never** set up a bridge between the Internet and a network connected Pluto with the default images.


Unfortunately - nothing on your host understands the what the IP address of the usb device is. You, the human behind the keyboard need to understand this before any sort of networking will work. There are two main ways to do this:

Determine the IP address
~~~~~~~~~~~~~~~~~~~~~~~~

The IP address is set by the device and can be found by looking inside the ADALM-PLUTO's mass storage device, and the ``info.html`` page. Just click on the ``version`` button at the top of the page:

.. image:: https://wiki.analog.com/_media/university/tools/pluto/drivers/version_button.png
   :alt: version_button.png
   :align: center

and then check out the Pluto IP address, and the host IP address.

.. image:: https://wiki.analog.com/_media/university/tools/pluto/drivers/pluto_ip_addr.png
   :alt: pluto_ip_addr.png
   :align: center

In this case, the IP address of the PLUTO device is ``192.168.2.1`` (which is the default for all devices). If you need to change this (if you have multiple devices), please check the `customizing Pluto <https://wiki.analog.com/../users/customizing>`_ documentation.

Checking from serial port
~~~~~~~~~~~~~~~~~~~~~~~~~

Open your favorite serial application:

.. container:: box

   
   ::
   
      Welcome to Pluto
      pluto login: **root**
      Password: **analog**
      Welcome to:
      %%
        ______ _       _        _________________
        | ___ \ |     | |      /  ___|  _  \ ___ \
        | |_/ / |_   _| |_ ___ \ `--.| | | | |_/ /
        |  __/| | | | | __/ _ \ `--. \ | | |    /
        | |   | | |_| | || (_) /\__/ / |/ /| |\ \
        \_|   |_|\__,_|\__\___/\____/|___/ \_| \_|
      %%
      http:%%//%%wiki.analog.com/university/tools/pluto
   
      # ifconfig usb0
      usb0      Link encap:Ethernet  HWaddr 00:05:F7:64:30:10
                inet addr:192.168.2.1  Bcast:192.168.2.255  Mask:255.255.255.0
                UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                RX packets:502 errors:0 dropped:115 overruns:0 frame:0
                TX packets:7 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:1000
                RX bytes:66132 (64.5 KiB)  TX bytes:2420 (2.3 KiB)
   


IIO devices
~~~~~~~~~~~

The IIO device shows up in device manager, and allows you to make native IIO connections to the device.

Bringing up a Windows Console should show you something like this:

::

   c:/ **iio_info -s**
   Library version: 0.16 (git tag: 5cdeaaa)
   Compiled with backends: local xml ip usb serial
   Available contexts:
       0: 0456:b673 (Analog Devices Inc. PlutoSDR (ADALM-PLUTO)), serial=104473222a87000618000600473ed57ae0 [usb:3.8.5]

   c:\ **iio_attr -a -C**
   Using auto-detected IIO context at URI "usb:3.8.5"
   IIO context with 8 attributes:
   local,kernel: 4.6.0-g651ed13
   usb,idVendor: 0456
   usb,idProduct: b673
   usb,release: 2.0
   usb,vendor: Analog Devices Inc.
   usb,product: PlutoSDR (ADALM-PLUTO)
   usb,serial: 104473222a87000618000600473ed57ae0
   usb,libusb: 1.0.22.11312

.. |image1| image:: https://wiki.analog.com/_media/university/tools/pluto/drivers/win_your_device_is_ready_to_use.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/university/tools/pluto/drivers/device_manager_installed.png
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/university/tools/pluto/drivers/device_manager_m2k_installed.png
   :width: 300px
