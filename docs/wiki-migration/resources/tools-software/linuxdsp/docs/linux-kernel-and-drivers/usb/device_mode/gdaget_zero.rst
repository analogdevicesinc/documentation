USB Gadget Zero
===============

This page provides how to use the USB Gadget Zero on ADSP-SC5xx board, and it will include the below test:

-  USB gadget zero bulk
-  USB Gadget zero control
-  USB Gadget zero test

--------------

Hardware Configuration
----------------------

Connect the USB micro-B plug cable into the USB HS/OTG Device port, as showing below:


|image1|

--------------

Software Configuration
----------------------

On the Yocto, Configure the linux-kernel as below to set the USB controller in Gadget only mode, and enable the USB Gadget zero relevant options.

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

\**Configure the Gadget zero support \*\*

.. code:: shell

   Device Drivers  --->
       [*] USB support  --->
                   <*>   USB Gadget Support  --->
                         <M>   USB Gadget precomposed configurations
                         <M>     Gadget Zero (DEVELOPMENT) 

--------------

Example Usage
-------------

**Ez-Kit target board**

.. code:: c++

   root@adsp-sc589-ezkit:~# modprobe g_zero
   zero gadget: Gadget Zero, version: Cinco de Mayo 2008
   zero gadget: zero ready
   zero gadget: high-speed config #3: source/sink

**On the Linux-Host PC**

-  **Get the testusb**

Please following the `usbtest <http://www.linux-usb.org/usbtest>`_ to get the resources:tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/usbtest/testusb.c. and then compile the source code with the command:

.. code:: c++

   gcc -Wall -g -pthread -o testusb testusb.c

-  **run the gadget zero test**

.. code:: c++

   #!/bin/sh
   #set -x
   lsmod |grep usbtest
   sudo modprobe usbtest
   lsmod |grep usbtest
   sudo cat /sys/kernel/debug/usb/devices | grep -i "Gadget Zero"
   lsusb|grep -i "Gadget Zero"|awk '{print $2" "$4}'

   gadget_bus=$(lsusb|grep -i "Gadget Zero"|awk '{print $2}')
   gadget_bus=`echo $gadget_bus | tr -cd "[0-9]"`
   gadget_dev=$(lsusb|grep -i "Gadget Zero"|awk '{print $4}')
   gadget_dev=`echo $gadget_dev | tr -cd "[0-9]"`

   do_test()
   {
     sudo ./testusb -D /dev/bus/usb/$gadget_bus/$gadget_dev -t${1}
   }

   echo "Gadget zero bulk mode test "
   for i in $(seq 1 8)  
   do   
   do_test $i
   done 
   do_test 13

   echo "Gadget zero control mode test "
   do_test 9
   do_test 10
   sudo ./testusb -D /dev/bus/usb/$gadget_bus/$gadget_dev -t14 -c 15000 -s 256 -v 1

-  **Test log:**

.. code:: c++

   test@madara:~$ sh usb_gadget_zero.sh 
   usbtest                36864  0
   S:  Product=Gadget Zero
   002 023:
   Gadget zero bulk mode test 
   unknown speed   /dev/bus/usb/002/023    0
   /dev/bus/usb/002/023 test 1,    0.126166 secs
   unknown speed   /dev/bus/usb/002/023    0
   /dev/bus/usb/002/023 test 2,    0.126849 secs
   unknown speed   /dev/bus/usb/002/023    0
   /dev/bus/usb/002/023 test 3,    0.127574 secs
   unknown speed   /dev/bus/usb/002/023    0
   /dev/bus/usb/002/023 test 4,    0.125543 secs
   unknown speed   /dev/bus/usb/002/023    0
   /dev/bus/usb/002/023 test 5,    1.515107 secs
   unknown speed   /dev/bus/usb/002/023    0
   /dev/bus/usb/002/023 test 6,    0.623720 secs
   unknown speed   /dev/bus/usb/002/023    0
   /dev/bus/usb/002/023 test 7,    1.528005 secs
   unknown speed   /dev/bus/usb/002/023    0
   /dev/bus/usb/002/023 test 8,    0.626151 secs
   unknown speed   /dev/bus/usb/002/023    0
   /dev/bus/usb/002/023 test 13,    2.774978 secs
   Gadget zero control mode test 
   unknown speed   /dev/bus/usb/002/023    0
   /dev/bus/usb/002/023 test 9,    1.920662 secs
   unknown speed   /dev/bus/usb/002/023    0
   /dev/bus/usb/002/023 test 10,    3.265069 secs
   unknown speed   /dev/bus/usb/002/023    0
   /dev/bus/usb/002/023 test 14,    3.812687 secs

--------------

**Go TO** :doc:`USB Interface </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/start>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/gadget-mode/002_usb_interface-device_application.jpg
   :width: 600px
