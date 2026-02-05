.. _adsp setup:

Getting started
===============

ADSP evaluation boards do not ship with pre-installed software. The chips also
do not support booting directly from SD cards. Therefore the evaluation boards
need to be bootstrapped over JTAG using a :adi:`ADI ICE-1000 or ICE-2000 JTAG
debugger <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/emulators.html>`.

JTAG & OpenOCD Setup
-----------------------------

To communicate with the board, you must build and run the ADI fork of OpenOCD.

Install Dependencies
~~~~~~~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Ubuntu

      .. shell:: sh

         $ sudo apt install -y git autoconf automake libtool pkg-config \
                libjim-dev gcc g++ make texinfo gdb-multiarch

   .. tab-item:: Fedora

      .. shell:: sh

         $sudo dnf install -y git autoconf automake libtool pkgconfig \
               jimtcl-devel gcc gcc-c++ make texinfo gdb

   .. tab-item:: Windows (MSYS2)

      .. shell:: sh

         #Open a MinGW64 shell and run:
         $pacman -Syu
         $pacman -S --needed git mingw-w64-x86_64-toolchain \
            mingw-w64-x86_64-libusb mingw-w64-x86_64-hidapi \
            mingw-w64-x86_64-libtool mingw-w64-x86_64-pkgconf \
            autoconf automake make
         #Jim Tcl must also be built from source before building OpenOCD.


Build OpenOCD
~~~~~~~~~~~~~

.. shell:: sh

   $git clone https://github.com/analogdevicesinc/openocd
   $cd openocd
   $./bootstrap
   $./configure
   $make -j$(nproc)

On Windows, the resulting ``openocd.exe`` can be run directly.

Run OpenOCD
~~~~~~~~~~~

Run ``openocd`` from the cloned repository. For the ICE-1000 and EV-SC598-SOM run the following:

.. shell:: sh

    ~/openocd
    $ sudo src/openocd -f ice1000.cfg \
           -f adspsc59x_a55.cfg \
           --search tcl/ \
           --search tcl/interface/ \
           --search tcl/target/

* For the ADSP-SC594 (Cortex-A5) use ``adspsc59x.cfg``
* For the ADSP-SC598 (Cortex-A55) use  ``adspsc59x_a55.cfg``

The ``*_single_SHARC.cfg`` variants are for devices with only one SHARC core enabled (e.g. SC592).

Serial Console Setup
-----------------------------

A serial console is highly recommended for interacting with U-Boot and Linux.

Connect a standard USB-C cable from your PC to the SoM.

When connecting to SC598 evaluation boards, the console appears as a CP2102N USB-to-UART bridge with a unique serial number:

.. tab-set::

   .. tab-item:: Linux

      .. shell:: sh

         $ tree /dev/serial/by-id
          /dev/serial/by-id
          ├── usb-Silicon_Labs_CP2102N_USB_to_UART_Bridge_Controller_1e574c842d...-if00-port0 -> ../../ttyUSB1
          └── usb-Silicon_Labs_CP2102N_USB_to_UART_Bridge_Controller_8624ff6b12...-if00-port0 -> ../../ttyUSB0

   .. tab-item:: Windows

      .. shell:: sh

         $ pnputil /enum-devices /class Ports

          Microsoft PnP Utility

          Devices in class "Ports":

          Instance ID:    USB\VID_10C4&PID_EA60\8624FF6B1261ED11A8D3518009472825
          Device Name:    Silicon Labs CP210x USB to UART Bridge (COM7)

Configure the serial terminal for 115200 baud, 8 data bits, no parity, 1 stop bit (8-N-1), and disable all flow control.

.. tab-set::

   .. tab-item:: Linux

      .. shell:: sh

         # Example with Minicom
         # Replace the device path with your specific path found above
         $ sudo minicom -D /dev/serial/by-id/<your-device> -b 115200

   .. tab-item:: Windows

      .. shell:: sh

         # Example with PuTTY
         # Replace the device port with your specific port found above
         $ putty.exe -serial COM<port-of-device> -sercfg 115200,8,n,1,N

Booting the System
---------------------------

Download Release
~~~~~~~~~~~~~~~~~~

Navigate to the :git-br2-external:`br2-external releases page <releases+>` and
download the appropriate ``images-*.tar.xz`` release archive that matches your
hardware.

Boot U-Boot Proper
~~~~~~~~~~~~~~~~~~

.. warning::
   **Check Boot Mode Switch (S1)**

   Before powering on, locate the rotary switch labeled "S1 (Boot Mode Select)" on the board.
   Ensure the arrow on the dial is pointing to position "0".

You need a multi-architecture GDB to load the bootloader.

.. tab-set::

   .. tab-item:: Ubuntu/Debian

      .. shell:: sh

         $ sudo apt-get install -y gdb-multiarch

   .. tab-item:: Windows

      .. shell:: sh

        $ pacman -S mingw-w64-x86_64-gdb

   .. tab-item:: Fedora/RHEL

      .. shell:: sh

         $ sudo dnf install -y gdb

Run GDB:

.. tab-set::

   .. tab-item:: Ubuntu/Debian

      .. shell:: sh

         $ cd images-*   # Navigate to extracted release directory
         $ gdb-multiarch -x u-boot.gdb

   .. tab-item:: Windows/Fedora/RHEL

      .. shell:: sh

         $ cd images-*   # Navigate to extracted release directory
         $ gdb -x u-boot.gdb

Boot Linux
~~~~~~~~~~

Start a file server in a new terminal on your PC in the release directory:

.. tab-set::

   .. tab-item:: Linux

      .. shell:: sh

         $ cd images-*   # Navigate to extracted release directory
         $ python3 -m http.server 8000

   .. tab-item:: Windows

      .. shell:: sh

         $ cd images-*   # Navigate to extracted release directory
         $ python -m http.server 8000

Find your IP address:

.. tab-set::

   .. tab-item:: Linux

      .. shell:: sh

         $ ip a

   .. tab-item:: Windows

      .. shell:: sh

         $ ipconfig

In the U-Boot console, run the following (replace ``<your-pc-ip>`` with the IP you found above):

.. code-block:: console

   => dhcp
   => wget ${kernel_addr_r} <your-pc-ip>:/Image
   => wget ${fdt_addr_r} <your-pc-ip>:/sc598-som-ezkit.dtb
   => booti ${kernel_addr_r} - ${fdt_addr_r}

Note: Make sure to use the ``.dtb`` file name that matches your board (e.g. ``sc598-som-ezkit.dtb``).

Install U-Boot
~~~~~~~~~~~~~~

After Linux boots, the system automatically enters an installer environment.

Serial console displays a prompt:

.. code-block:: console

   ======== Installer Environment ========
   Install U-Boot to SPI Flash

   This will erase and program SPI flash.
   Continue? [y/N]:

Type ``y`` to erase the flash contents and install U-Boot. After programming completes, 
the console instructs you to move the S1 boot mode switch to the SPI boot position.

.. code-block:: console

   SPI install complete

   Set the switch S1 to position 1 (SPI boot).
   Waiting for switch...

Once the position change is detected, the system reboots automatically from SPI flash and the U-Boot console appears.
