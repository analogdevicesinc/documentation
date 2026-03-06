USB Gadget Filesystem
=====================

This page provides how to use the USB Gadget fs on ADSP-SC5xx board, and it will include the below test:

-  USB gadget filesystem bulk mode
-  USB Gadget filesystem control mode

--------------

Hardware Configuration
----------------------

Connect the USB micro-B plug cable into the USB HS/OTG Device port, as showing below:


|image1|

--------------

Software Configuration
----------------------

On the Yocto, Configure the linux-kernel as below to set the USB controller in Gadget only mode, and enable the USB Gadget Filesystem relevant options.

.. code:: c++

   $ bitbake linux-adi -c menuconfig

**Configure the USB drivers to Gadget only mode (or Dual role mode )**

.. code:: shell

   Device Drivers  --->
       [*] USB support  --->
                   <*>   Inventra Highspeed Dual Role Controller
                           MUSB Mode Selection (Gadget only mode)  --->
                           *** Platform Glue Layer *** 
                   <*>     ADI
                           *** MUSB DMA mode ***
                   [N]     Disable DMA (always use PIO)  
                   [*]       Inventra
                   <*>   USB Gadget Support  --->

\**Configure the Gadget Filesyetm support \*\*

.. code:: shell

   Device Drivers  --
   ->
       [*] USB support  --->
                   <*>   USB Gadget Support  --->
                         <M>   USB Gadget precomposed configurations
                         <M>     Gadget Filesystem   

--------------

Example Usage
-------------

**on the target Ez-Kit board**

.. code:: c++

   root@adsp-sc589-ezkit:~# modprobe gadgetfs
   gadgetfs: USB Gadget filesystem, version 24 Aug 2004
   root@adsp-sc589-ezkit:~# mkdir /dev/gadget
   root@adsp-sc589-ezkit:~# mount -t gadgetfs gadgetfs /dev/gadget
   root@adsp-sc589-ezkit:~# ls /dev/gadget/ -l
   total 0
   -rw-------    1 root     root             0 Jul 13 08:12 musb-hdrc
   root@adsp-sc589-ezkit:~# gadgetfs-test -r "1.3" -v
   gadgetfs: bound to musb-hdrc driver
   /dev/gadget/musb-hdrc ep0 configured
   serial="1.3"
   gadgetfs: connected

   ** Mon Jul 13 08:13:28 2020gadgetfs: disconnected

   CONNECT high speed
   DISCONNECT
   gadgetfs: connected
   read 2 ep0 eventsgadgetfs: configuration #3

   CONNECT high speed
   SETUP 80.06 v0300 i0000 255
   SETUP 80.06 v0302 i0409 255
   SETUP 80.06 v0301 i0409 255
   SETUP 80.06 v0303 i0409 255
   SETUP 00.09 v0003 i0000 0
   CONFIG #3
   SETUP 80.06 v0304 i0409 255
   SETUP 80.06 v0305 i0409 255
   simple_sink_thread start -1234897824 fd 4
   simple_source_thread start -1226505120 fd 5
   SETUP 80.06 v0300 i0000 255
   SETUP 80.06 v0305 i0409 255
   SETUP 80.06 v03ee i0000 1024
   ... protocol stall 80.06

**On the Linux-Host PC**

-  **Get the testusb**

Please following the `usbtest <http://www.linux-usb.org/usbtest>`__ to get the resources:tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/usbtest/testusb.c. and then compile the source code with the command:

.. code:: c++

   gcc -Wall -g -pthread -o testusb testusb.c

-  **run the gadget fs test**

.. code:: c++

   #!/bin/sh
   #set -x
   lsmod |grep usbtest
   sudo modprobe usbtest
   lsmod |grep usbtest
   sudo cat /sys/kernel/debug/usb/devices | grep -i "Manufacturer=Licensed to Code, LLC"
   sudo cat /sys/kernel/debug/usb/devices | grep -i "Product=My Source/Sink Product"

   lsusb|grep -i "Netchip Technology"|awk '{print $2" "$4}'
   gadget_bus=$(lsusb|grep -i "Netchip Technology"|awk '{print $2}')
   gadget_bus=`echo $gadget_bus | tr -cd "[0-9]"`
   gadget_dev=$(lsusb|grep -i "Netchip Technology"|awk '{print $4}')
   gadget_dev=`echo $gadget_dev | tr -cd "[0-9]"`

   do_test()
   {
     sudo ./testusb -D /dev/bus/usb/$gadget_bus/$gadget_dev -t${1}
   }

   echo "Gadget fs bulk mode test "
   for i in $(seq 1 8)  
   do   
   do_test $i
   done 

   echo "Gadget fs control mode test "
   do_test 9
   do_test 10

-  **Test log:**

.. code:: c++

   test@madara:~$ sh usb_gadget_fs.sh
   usbtest                36864  0
   S:  Manufacturer=Licensed to Code, LLC
   S:  Product=My Source/Sink Product
   002 040:
   Gadget fs bulk mode test
   ./testusb: /dev/bus/usb/002/040 may see only control tests
   /dev/bus/usb/002/040 test 1 --> 110 (Connection timed out)
   ./testusb: /dev/bus/usb/002/040 may see only control tests
   /dev/bus/usb/002/040 test 2 --> 110 (Connection timed out)
   ./testusb: /dev/bus/usb/002/040 may see only control tests
   /dev/bus/usb/002/040 test 3 --> 110 (Connection timed out)
   ./testusb: /dev/bus/usb/002/040 may see only control tests
   /dev/bus/usb/002/040 test 4 --> 110 (Connection timed out)
   ./testusb: /dev/bus/usb/002/040 may see only control tests
   /dev/bus/usb/002/040 test 5 --> 110 (Connection timed out)
   ./testusb: /dev/bus/usb/002/040 may see only control tests
   /dev/bus/usb/002/040 test 6 --> 110 (Connection timed out)
   ./testusb: /dev/bus/usb/002/040 may see only control tests
   /dev/bus/usb/002/040 test 7 --> 110 (Connection timed out)
   ./testusb: /dev/bus/usb/002/040 may see only control tests
   /dev/bus/usb/002/040 test 8 --> 110 (Connection timed out)
   Gadget fs control mode test
   ./testusb: /dev/bus/usb/002/040 may see only control tests
   /dev/bus/usb/002/040 test 9 --> 110 (Connection timed out)
   ./testusb: /dev/bus/usb/002/040 may see only control tests
   /dev/bus/usb/002/040 test 10 --> 110 (Connection timed out)

<fc #ff0000>\ **error log one board side**\ </fc>

.. code:: c++

   SETUP 01.0b v0000 i0000 0
   musb_g_ep0_irq 691: SetupEnd came in a wrong ep0stage wait
   musb_g_ep0_irq 691: SetupEnd came in a wrong ep0stage wait
   musb_g_ep0_irq 691: SetupEnd came in a wrong ep0stage wait
   musb_g_ep0_irq 691: SetupEnd came in a wrong ep0stage wait
   musb_g_ep0_irq 691: SetupEnd came in a wrong ep0stage wait
   musb_g_ep0_irq 691: SetupEnd came in a wrong ep0stage wait
   musb_g_ep0_irq 691: SetupEnd came in a wrong ep0stage wait
   musb_g_ep0_irq 691: SetupEnd came in a wrong ep0stage wait
   musb_g_ep0_irq 691: SetupEnd came in a wrong ep0stage wait

--------------

**Go TO** :doc:`USB Interface </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/start>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/gadget-mode/002_usb_interface-device_application.jpg
   :width: 600px
