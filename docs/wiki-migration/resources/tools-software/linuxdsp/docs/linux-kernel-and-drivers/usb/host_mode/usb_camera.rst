USB Camera Support
==================

--------------

Hardware Configuration
----------------------

Connect the USB micro-A plug to A receptacle adapter cable (found in the EZ-Board box) to the OTG port, below photo shows when it acts as Host and connected to a USB Camera device.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/host_mode/ca.jpg
   :align: center
   :width: 600px

--------------

Software Configuration
----------------------

On the Yocto, Configure the linux-kernel as below to set the USB controller in Host only mode, and enable the USB Camera relevant supported operations. Check the directory of "yocto/build" and Clean up and setup the linux-kernel configuration with commands:

.. code:: c++

   $ bitbake linux-adi -c cleansstate
   $ bitbake linux-adi -c menuconfig

And In the pop-up window of linux-kenel configuration, configure as follows Configure the USB drivers to host mod or (dual role mode)

.. code:: shell

   Device Drivers  --->
       [*] USB support  --->
           <*>   Support for Host-side USB
                   [*]   Enable USB persist by default 
                   <*>   Inventra Highspeed Dual Role Controller
                           MUSB Mode Selection (Dual role mode)  --->
                           *** Platform Glue Layer *** 
                   <*>     ADI
                           *** MUSB DMA mode ***
                   [N]     Disable DMA (always use PIO)  
                   [*]       Inventra 

Configure the USB camera corresponding options

.. code:: shell

   Device Drivers  --->
           <*> Multimedia support  ---> 
                 *** Multimedia core support ***   
           [*]   Cameras/video grabbers support
           [*]   Media Controller API
           [*]   V4L2 sub-device userspace API
                 *** Media drivers ***  
           [*]   Media USB Adapters  --->
                 <*>   USB Video Class (UVC)
                 [*]     UVC input events device support
                 <M>   GSPCA based webcams (NEW)  --->  
                 <M>   USB Philips Cameras
           [*]   Autoselect ancillary drivers (tuners, sensors, i2c, spi, frontends) (NEW)

Enable the I2C

.. code:: shell

   Device Drivers  --->  
           I2C support  --->
           [*]   Enable compatibility bits for old user-space
           <*>   I2C device interface  
           [*]   Autoselect pertinent helper modules     
                 I2C Hardware Bus support  --->
                     <*> ADI TWI I2C support
                     (50)  ADI TWI I2C clock (kHz) 

XHIDDENSTART Click to expand XHIDDENSTARTSTOP Virtual terminal & frame buffer support (ARM core may not need this configurations)

.. code:: shell

   Device Drivers  --->
           Character devices  --->
            [*] Enable TTY 
            [*]   Virtual terminal
            [*]     Enable character translations in console
            [*]     Support for console on virtual terminal
            -*-     Support for binding and unbinding console drivers             
           Graphics support  --->   
                 Console display driver support  --->  
                 [*] Framebuffer Console support
                 
   Library routines  --->
         [*] Select compiled-in fonts
         [*]   Mac console 6x11 font (not supported by all drivers) 

XHIDDENEND

Include the USB gadget zero module

.. code:: shell

   Device Drivers  --->
       [*] USB support  --->
                   <*>   USB Gadget Support  --->
                         <M>   USB Gadget precomposed configurations
                         <M>     Gadget Zero (DEVELOPMENT)

Then save the linux-kernel configuration and build the target images:

.. code:: shell

   $ bitbake adsp-sc5xx-full

--------------

Example Usage
-------------

Boot the generated Images and connect the USB Camera, kernel outputs messages looks like below:

.. code:: c++

   root@adsp-sc589-ezkit:~# modprobe g_zero
   zero gadget: Gadget Zero, version: Cinco de Mayo 2008
   zero gadget: zero ready
   root@adsp-sc589-ezkit:~# usb 1-1: new high-speed USB device number 2 using musb-hdrc
   uvcvideo: Found UVC 1.00 device <unnamed> (046d:0990)
   uvcvideo 1-1:1.0: Entity type for entity Extension 4 was not initialized!
   uvcvideo 1-1:1.0: Entity type for entity Extension 10 was not initialized!
   uvcvideo 1-1:1.0: Entity type for entity Extension 12 was not initialized!
   uvcvideo 1-1:1.0: Entity type for entity Extension 8 was not initialized!
   uvcvideo 1-1:1.0: Entity type for entity Extension 11 was not initialized!
   uvcvideo 1-1:1.0: Entity type for entity Extension 9 was not initialized!
   uvcvideo 1-1:1.0: Entity type for entity Processing 2 was not initialized!
   uvcvideo 1-1:1.0: Entity type for entity Extension 13 was not initialized!
   uvcvideo 1-1:1.0: Entity type for entity Camera 1 was not initialized!
   input: UVC Camera (046d:0990) as /devices/platform/scb/310c1000.usb/musb-hdrc.1.auto/usb1/1-1/1-1:1.0/input/input0

   root@adsp-sc589-ezkit:~#  modprobe uvcvideo
   root@adsp-sc589-ezkit:~#  ffmpeg -f video4linux2 -r 5 -s 320x240 -i /dev/video0 -vcodec mpeg4 -f mp4 usb_camera.mp4
   ffmpeg version 4.0.2 Copyright (c) 2000-2018 the FFmpeg developers
     built with gcc 8.2.0 (GCC)
     configuration: --disable-stripping --enable-pic --enable-shared --enable-pthreads --disable-libxcb --disable-libxcb-shm --v
     libavutil      56. 14.100 / 56. 14.100
     libavcodec     58. 18.100 / 58. 18.100
     libavformat    58. 12.100 / 58. 12.100
     libavdevice    58.  3.100 / 58.  3.100
     libavfilter     7. 16.100 /  7. 16.100
     libswscale      5.  1.100 /  5.  1.100
     libswresample   3.  1.100 /  3.  1.100
     libpostproc    55.  1.100 / 55.  1.100
   Input #0, video4linux2,v4l2, from '/dev/video0':
     Duration: N/A, start: 137.819364, bitrate: 6144 kb/s
       Stream #0:0: Video: rawvideo (YUY2 / 0x32595559), yuyv422, 320x240, 6144 kb/s, 5 fps, 5 tbr, 1000k tbn, 1000k tbc
   Stream mapping:
     Stream #0:0 -> #0:0 (rawvideo (native) -> mpeg4 (native))
   Press [q] to stop, [?] for help  (Enter q to save your recored)
   Output #0, mp4, to 'usb_camera.mp4':
     Metadata:
       encoder         : Lavf58.12.100
       Stream #0:0: Video: mpeg4 (mp4v / 0x7634706D), yuv420p, 320x240, q=2-31, 200 kb/s, 5 fps, 10240 tbn, 5 tbc
       Metadata:
         encoder         : Lavc58.18.100 mpeg4
       Side data:
         cpb: bitrate max/min/avg: 0/0/200000 buffer size: 0 vbv_delay: -1
   frame= 1029 fps=5.0 q=2.0 Lsize=     947kB time=00:03:25.60 bitrate=  37.7kbits/s speed=   1x
   video:942kB audio:0kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.551482%
   root@adsp-sc589-ezkit:~# ls (To make sure whether the mp4 file is exisited)
   usb_camera.mp4
   root@adsp-sc589-ezkit:~# scp usb_camera.mp4 test@10.100.4.174:/home/test(Copy the mp4 file from board to host PC)
   The authenticity of host '10.100.4.174 (10.100.4.174)' can't be established.
   ECDSA key fingerprint is c1:23:ab:ea:cf:bc:88:20:9b:ac:1f:54:51:30:81:f8.
   Are you sure you want to continue connecting (yes/no)? yes
   Warning: Permanently added '10.100.4.174' (ECDSA) to the list of known hosts.
   test@10.100.4.174's password:
   usb_camera.mp4                                100% 1108KB   1.1MB/s   00:00   

Play the usb_camera.mp4 on the host PC

.. code:: java

   $ ffplay usb_camera.mp4

If the recored could play successfully then the test can pass, if you could not play the video using ffplay command, you could double click the video and then play.

--------------

**Go TO** :doc:`USB Interface </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/start>`
