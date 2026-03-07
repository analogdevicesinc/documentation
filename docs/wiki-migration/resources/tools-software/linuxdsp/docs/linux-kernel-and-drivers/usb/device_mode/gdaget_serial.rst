USB Gadget serial
=================

Hardware Configuration
----------------------

Connect the USB micro-B plug cable into the USB HS Device port, as showing below:


|image1|

**Note** we can also connect the cable to the OTG port, in this case OTG port will work as Device.

Software Configuration
----------------------

On the Yocto, Configure the linux-kernel as below to set the USB controller in Gadget only mode, and enable the USB Mass Storage support. check the directory of "yocto/build" and Clean up and setup the linux-kernel configuration with commands:

.. code:: c++

   $ bitbake linux-adi -c cleansstate
   $ bitbake linux-adi -c menuconfig

And In the pop-up window of linux-kenel configuration, configure as follows Configure the USB drivers to host mode

.. code:: shell

   Device Drivers  --->
       [*] USB support  --->
                   <N>   Support for Host-side USB
                   <*>   Inventra Highspeed Dual Role Controller
                           MUSB Mode Selection (Gadget only mode)  --->
                           *** Platform Glue Layer *** 
                   <*>     ADI
                           *** MUSB DMA mode ***
                   [N]     Disable DMA (always use PIO)  
                   [*]       Inventra
                         USB Physical Layer drivers  --->
                      <*> NOP USB Transceiver Driver 
                   <*>   USB Gadget Support  --->
                         

Gadget Serial Configuration

.. code:: shell

   Device Drivers  --->
       [*] USB support  --->
                   <*>   USB Gadget Support  --->
                         <M>   USB Gadget precomposed configurations
                         <M>     Serial Gadget (with CDC ACM and CDC OBEX support)

Then save the linux-kernel configuration and build the target images:

.. code:: shell

   $ bitbake adsp-sc5xx-full

--------------

Example Usage
-------------

**Ez-Kit target board**

.. code:: c++

   root@adsp-sc589-ezkit:~# modprobe g_serial use_acm=1
   g_serial gadget: Gadget Serial v2.4
   g_serial gadget: g_serial ready
   g_serial gadget: full-speed config #2: CDC ACM config
   g_serial gadget: full-speed config #2: CDC ACM config
   root@adsp-sc589-ezkit:~# setsid getty 9600 /dev/ttyGS0

**linux-Host PC**

Get the target board usb serial information:

.. code:: c++

   test@madara:~# dmesg|tail
   [777890.073364] usb 1-1.4.1.2: New USB device found, idVendor=0525, idProduct=a4a7
   [777890.073367] usb 1-1.4.1.2: New USB device strings: Mfr=1, Product=2, SerialNumber=0
   [777890.073368] usb 1-1.4.1.2: Product: Gadget Serial v2.4
   [777890.073370] usb 1-1.4.1.2: Manufacturer: Linux 4.19.0-yocto-standard with musb-hdrc
   [777890.083605] cdc_acm 1-1.4.1.2:2.0: ttyACM0: USB ACM device
   test@madara:~# ls /dev/ttyACM*
   /dev/ttyACM0

Open a new Minicom terminal and configure as below:

.. code:: 

   A - Serial Device : /dev/ttyACM0
   E -bPS/Par/Bits   : 9600 8N1

And you will get into the kernel of the target board via the USB Serial protocol:

.. code:: c++

   Port /dev/ttyACM0, 18:19:06                                                  
                                                                                
   Press CTRL-A Z for help on special keys                                      

        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
        @@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@            @@@@@@@@@@@@@@@@@@@
        @@@@@@@@               @@@@@@@@@@@@@@@@
        @@@@@@@@                   @@@@@@@@@@@@
        @@@@@@@@                     @@@@@@@@@@
        @@@@@@@@                        @@@@@@@
        @@@@@@@@                     @@@@@@@@@@
        @@@@@@@@                   @@@@@@@@@@@@
        @@@@@@@@               @@@@@@@@@@@@@@@@
        @@@@@@@@            @@@@@@@@@@@@@@@@@@@
        @@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

           Analog Devices Yocto Distribution
                    www.analog.com
                 www.yoctoproject.org
        
   adsp-sc589-ezkit login: root
   Password: 
   Last login: Thu Jul  2 11:28:33 +0000 2020 on /dev/ttySC0.
   root@adsp-sc589-ezkit:~# 

--------------

**Go TO** :doc:`USB Interface </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/start>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/gadget-mode/002_usb_interface-device_application.jpg
   :width: 600px
