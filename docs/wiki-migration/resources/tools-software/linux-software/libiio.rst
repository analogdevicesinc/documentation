What is libiio?
===============

Libiio is a library that has been developed by Analog Devices to ease the development of software interfacing Linux :doc:`Industrial I/O (IIO) </wiki-migration/software/linux/docs/iio/iio>` devices.

The library abstracts the low-level details of the hardware, and provides a simple yet complete programming interface that can be used for advanced projects.

The library is composed by one high-level API, and several backends:

-  the "local" backend, which interfaces the Linux kernel through the sysfs virtual filesystem,
-  the "network" backend, which interfaces the ``iiod`` server through a network link.

The IIO Daemon (IIOD) server is a good example of an application that uses *libiio*. It creates a libiio context that uses the "local" backend, and then share it on the network to any client application using the "network" backend of libiio and connected to the server.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio_diagram.png
   :align: center
   :width: 400px

Network Backends
================

If you just want to use libiio and iiod, which may be on a pre-compiled image - there are many places you can stream data to.

-  :doc:`MATLAB and Simulink </wiki-migration/resources/tools-software/linux-software/libiio/clients/matlab_simulink>`
-  :doc:`Visual Analog </wiki-migration/resources/tools-software/linux-software/libiio/clients/visual_analog>`
-  `IIO oscilloscope for Windows <https://wiki.analog.com/../../tools-software/linux-software/iio_oscilloscope>`_
-  `GNU Radio <https://wiki.analog.com/../../tools-software/linux-software/gnuradio>`_
-  :doc:`pyadi-iio: Device Specific Python Interfaces For IIO Drivers </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`

Where to get libiio?
====================

.. include:: ../../eval/user-guides/ad-fmcomms2-ebz/downloads.rst

How to build it?
================

Building on the Linux/Zynq Target
---------------------------------

Check out how to :doc:`stay up to date </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`. This will check out and build the latest version.

Building on the Linux Host Target
---------------------------------

Building libiio is pretty straightforward.

The first step is to fetch the dependencies, which as of now is only libxml2.

Debian based distributions
~~~~~~~~~~~~~~~~~~~~~~~~~~

On a Debian-flavoured GNU/Linux distribution, like Ubuntu for instance:

::

   rgetz@pinky:~$ **sudo apt-get install build-essential libxml2 libzstd-dev libxml2-dev bison flex libcdk5-dev cmake**

Depending on the backend (how you want to attach the IIO device), you may need at least one of:

::

   rgetz@pinky:~$ **sudo apt-get install libaio-dev libusb-1.0-0-dev libserialport-dev libxml2-dev libavahi-client-dev doxygen graphviz**

RedHAT based distributions
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   [liveuser@localhost-live ~]$ **sudo dnf install libxml2 libzstd-dev libxml2-devel bison flex make gcc cmake rpmdevtools**

Depending on the backend (how you want to attach the IIO device), you may need at least one of:

::

   [liveuser@localhost-live ~]$ **sudo dnf install libaio-devel libusb1-devel libserialport-devel avahi-devel doxygen graphviz**

FreeBSD based distributions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   rgetz@freebsd:~ $ **sudo pkg update && sudo pkg upgrade && sudo pkg install libzstd libxml2 bison flex gcc cmake git**

Depending on the backend (how you want to attach the IIO device), you may need at least one of:

::

   rgetz@freebsd:~ $ **sudo pkg install libserialport avahi doxygen graphviz**

add these lines to ``/etc/rc.conf``:

::

   dbus_enable="YES"
   avahi_daemon_enable="YES"
   avahi_dnsconfd_enable="YES"

FreeBSD does not automount USB drives by default, so you need to install an automounter:

::

   rgetz@freebsd:~ $ **sudo pkg install automount**

Remaining steps1
~~~~~~~~~~~~~~~~

.. warning::

   At this time the main branch of libiio in under heavy development. It is recommended to use the latest release if not a developer. That would be a v0.XX release.


Now you have the prerequisite installed, you can clone a release branch from the GIT repository:

::

   rgetz@pinky:~$ **git clone https:%%//%%github.com/analogdevicesinc/libiio.git --branch v0.25**

Finally, in the ``libiio/`` directory,

::

   rgetz@pinky:~/libiio$ **mkdir build && cd build && cmake ../ && make && sudo make install**

This will build ``libiio`` in the ``build`` subdirectory, and install it to ``/usr``. Note that it is possible to install to a different location by setting the PREFIX variable.

To build iio oscilloscope you'll have to make sure libiio directories can be found, one way to do this given it installed to /usr/lib is add it to your sessions PATH:

::

   /libiio$ PATH=/usr/lib/:$PATH

Understanding which libiio is being used
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

During development, sometimes it can be a puzzle which version of libiio is being used. An easy way to tell is to do something like:

::

   analog@imhotep:~/github/libiio$ **git describe --tags**
   v0.8-13-g6847e22

To check what is running:

::

   analog@imhotep:~/github/libiio/build$ **iio_info**
   Library version: 0.8 (git tag: 6847e22)
   Unable to create IIO context

If you are running an application, and want to find out:

::

   analog@imhotep:~/github/libiio/build$ **strace -ofoo iio_info**
   Library version: 0.8 (git tag: 6847e22)
   Unable to create IIO context
   analog@imhotep:~/github/libiio/build$ **grep -e ^open  foo | grep libiio**
   open("./tls/x86_64/libiio.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
   open("./tls/libiio.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
   open("./x86_64/libiio.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
   open("./libiio.so.0", O_RDONLY|O_CLOEXEC) = 3
   analog@imhotep:~/github/libiio/build$ **ls -l ./libiio.so.0**
   lrwxrwxrwx 1 analog analog 13 Nov 15 10:36 ./libiio.so.0 -> libiio.so.0.8
   analog@imhotep:~/github/libiio/build$ **ls -l ./libiio.so.0.8**
   -rwxr-xr-x 1 analog analog 408432 Nov 15 10:36 ./libiio.so.0.8

This found a version in the same directory.

::

   analog@imhotep:~$ **strace -ofoo iio_info**
   Library version: 0.8 (git tag: 6847e22)
   Unable to create IIO context
   analog@imhotep:~$ **grep -e ^open  foo | grep libiio**
   open("./tls/x86_64/libiio.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
   open("./tls/libiio.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
   open("./x86_64/libiio.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
   open("./libiio.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
   open("/usr/lib/x86_64-linux-gnu/libiio.so.0", O_RDONLY|O_CLOEXEC) = 3
   analog@imhotep:~$ **ls -l /usr/lib/x86_64-linux-gnu/libiio.so.0**
   lrwxrwxrwx 1 root root 13 Nov  9 21:05 /usr/lib/x86_64-linux-gnu/libiio.so.0 -> libiio.so.0.8
   analog@imhotep:~$ **ls -l /usr/lib/x86_64-linux-gnu/libiio.so.0.8**
   -rw-r--r-- 1 root root 408432 Nov 15 10:36 /usr/lib/x86_64-linux-gnu/libiio.so.0.8

This found the version in ``/usr/lib/x86_64-linux-gnu/libiio.so.0``.

Cross-compilation
-----------------

If you want to cross-compile libiio, you can do so by passing the corresponding toolchain information file to cmake. Normally this is done by creating a toolchain file, and passing this to Cmake with a ``-DCMAKE_TOOLCHAIN_FILE=path/to/file`` option, the file will be loaded early to set values for the compilers. This is described in the `mainline cmake doc <https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling>`_.

Building on Windows
-------------------

The instructions for building libiio with Visual Studio are available here: :doc:`/wiki-migration/resources/tools-software/linux-software/building_libiio_for_windows`

Enabling IIOD USB Backend
=========================

In order to use the libIIO USB Backend - support must be built into IIOD. A simple check is shown below:

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# **iiod -F foo**
      ERROR: IIOD was not compiled with USB support.
   


In this case LibIIO / IIOD needs to be built with USBD support. (WITH_IIOD_USBD)

If all the dependencies are met, the USB Backend is built automatically. However the 'WITH_IIOD_USBD' option is only available under certain conditions.

In the log of cmake, if you see: *Check size of struct usb_functionfs_descs_head_v2 - failed*

Although your kernel itself probably is recent enough, your kernel headers are too old.

The fix:

-  Download the file: https://raw.githubusercontent.com/torvalds/linux/master/include/uapi/linux/usb/functionfs.h
-  And place it in /usr/include/linux/usb/functionsfs.h, overwriting the old one.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# cd /usr/include/linux/usb
      root@analog:/usr/include/linux/usb# rm functionfs.h
      root@analog:/usr/include/linux/usb# wget https:<nowiki>//</nowiki>raw.githubusercontent.com/torvalds/linux/master/include/uapi/linux/usb/functionfs.h
   


Rebuild LibIIO
--------------

-  cd /usr/local/src
-  git clone https://github.com/analogdevicesinc/libiio.git
-  cd /usr/local/src/libiio/
-  git clean -d -f -x
-  cmake .
-  make
-  sudo make install

USB Device Mode Kernel Support
------------------------------

In order to use the libIIO USB Backend, the target must support USB Device Mode.

Kernel compiled with USB UDC Gadget support.

::

   CONFIG_USB_CHIPIDEA=y
   CONFIG_USB_CHIPIDEA_UDC=y
   **CONFIG_USB_GADGET=y**
   CONFIG_USB_GADGET_XILINX=y
   **CONFIG_USB_CONFIGFS=y**
   **CONFIG_USB_CONFIGFS_F_FS=y**

Starting IIOD with USB Support
------------------------------

.. admonition:: Download
   :class: download

   
   -  `iiod-usb.conf <http://swdownloads.analog.com/cse/share/iiod-usb.conf>`_
   


Copy (and replace) iiod.conf upstart script into /etc/init

Testing
-------

If everything works out well the USB context should be included in the available context list.

::

   michael@mhenneri-D04:~/devel/pshare/iiod usb$ iio_info -s
   Library version: 0.10 (git tag: c95ff6a)
   Compiled with backends: local xml ip usb
   Available contexts:
       0: Local devices [local:]
       1: 0456:b671 (Analog Devices Inc. Generic USB IIOD), serial=00000000 [usb:1.36.0]

Documentation
=============

API reference
-------------

An automatically generated documentation of the API can be found here: http://analogdevicesinc.github.io/libiio/

Bindings
--------

Python and C# have official bindings available in the repository but third parties have developed others for more languages. Python and C# bindings documentation is available on the :doc:`libiio internals page </wiki-migration/resources/tools-software/linux-software/libiio_internals>` and within the `API documentation <http://analogdevicesinc.github.io/libiio/>`_.

Libiio internals
----------------

See the dedicated page: :doc:`About libiio </wiki-migration/resources/tools-software/linux-software/libiio_internals>`.

Libiio System Considerations Tips & Tricks
------------------------------------------

See the dedicated page: :doc:`System Considerations Tips & Tricks </wiki-migration/resources/tools-software/linux-software/libiio_tips_tricks>`.

libiio Examples
===============

libiio - AD9361 IIO streaming example
-------------------------------------

+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Source                                                                                                      | Description                                                                                  |
+=============================================================================================================+==============================================================================================+
| :git-libiio:`examples/ad9361-iiostream.c`                                                                   | Configures the AD9361 transceiver, receives samples, processes them and sends them back out. |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
