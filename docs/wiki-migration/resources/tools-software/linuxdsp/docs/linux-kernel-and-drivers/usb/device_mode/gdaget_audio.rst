USB Gadget Audio
================

This page provides how to use the USB Gadget Audio on ADSP-SC5XX board which makes the the Board as an audio card, and it will include the below test:

-  USB gadget Audio Class 1.0
-  USB Gadget Audio Class 2.0

--------------

Hardware Configuration
----------------------

Connect the USB micro-B plug cable into the USB HS/OTG Device port, as showing below:


|image1|

--------------

Software Configuration
----------------------

On the Yocto, Configure the linux-kernel as below to set the USB controller in Gadget only mode, and enable the USB Gadget Audio relevant options.

Package Configuration
~~~~~~~~~~~~~~~~~~~~~

Add the alsa-utils and alsa-lib packages in the filesystem, they're enabled in adsp-sc5xx-full image by default.

Enable alsa-lib and alsa-utils support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   vim build/conf/local.conf
   IMAGE_INSTALL_append = "alsa-utils alsa-lib"

Then run “bitbake adsp-sc5xx-minimal -C compile” or “bitbake adsp-sc5xx-full -C compile” to generate the filesystem.

Kernel Configuration
~~~~~~~~~~~~~~~~~~~~

.. code:: c++

   $ bitbake linux-adi -c menuconfig

Configure the USB drivers to Gadget only mode (or Dual role mode )
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   Device Drivers  --->
       [*] USB support  --->
                   <*>   Support for Host-side USB  
                   <*>   Inventra Highspeed Dual Role Controller
                           MUSB Mode Selection (Dual role mode)  --->
                           *** Platform Glue Layer *** 
                   <*>     ADI
                           *** MUSB DMA mode ***
                   [N]     Disable DMA (always use PIO)  
                   [*]       Inventra
                   <*>   USB Gadget Support  --->

Configure the Gadget Audio support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Enable the corresponding :doc:`sound card </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/audio/linux_sound_driver>` and the **USB sound device feature:**

.. code:: shell

   Device Drivers  --->  
        <*> USB support 
              <*>   Support for Host-side USB  
        <*> Sound card support  ---> 
             <*>   Advanced Linux Sound Architecture  ---> 
                 [*]   USB sound devices

-  **<fc #ff00ff>For Class 1.0</fc>**

.. code:: shell

   Device Drivers  --->
       [*] USB support  --->
                   <*>   USB Gadget Support  --->
                         <M>   USB Gadget precomposed configurations
                          [M] Audio Gadget
                          [*] UAC 1.0
                          [*]  UAC 1.0(Legacy

-  **<fc #ff00ff>For Class 2.0</fc>**

.. code:: shell

   Device Drivers  --->
       [*] USB support  --->
                   <*>   USB Gadget Support  --->
                         <M>   USB Gadget precomposed configurations
                          [M] Audio Gadget
                          [ ] UAC 1.0
                          [ ]  UAC 1.0(Legacy

--------------

Example Usage
-------------

Class 1.0
~~~~~~~~~

Ez-Kit target board
^^^^^^^^^^^^^^^^^^^

.. code:: c++

   root@adsp-sc589-ezkit:~# ls /dev/snd/
   controlC0  pcmC0D0p   pcmC0D1c   timer
   root@adsp-sc589-ezkit:~# modprobe g_audio 
   modprobe g_audio fn_play=/dev/snd/pcmC0D0p fn_cap=/dev/snd/pcmC0D1c   
   g_audio gadget: Hardware params: access 3, format 2, channels 2, rate 48000
   g_audio gadget: Linux USB Audio Gadget, version: Feb 2, 2012
   g_audio gadget: g_audio ready
   g_audio gadget: high-speed config #1: Linux USB Audio Gadget

On the Linux-Host PC
^^^^^^^^^^^^^^^^^^^^

With following command you should be able to see the USB Gadget Audio device is there on your HOST:

.. code:: c++

   test@madara:~$ lsusb
   Bus 002 Device 033: ID 1d6b:0101 Linux Foundation Audio Gadget

Then we list the available sound card on host PC, to decide which sound card is associated with EZKIT board

.. code:: c++

   test@madara:~$ cat /proc/asound/cards
    0 [PCH            ]: HDA-Intel - HDA Intel PCH
                         HDA Intel PCH at 0xf7d00000 irq 28
    1 [Gadget         ]: USB-Audio - Linux USB Audio Gadget
                         Linux 4.19.0-yocto-standard with musb-hdrc Linux USB Audio Gadget at usb-0000:0

.. code:: c++

   test@madara:~$ aplay -l
   **** List of PLAYBACK Hardware Devices ****
   card 0: PCH [HDA Intel PCH], device 0: CX20641 Analog [CX20641 Analog]
     Subdevices: 1/1
     Subdevice #0: subdevice #0
   card 0: PCH [HDA Intel PCH], device 3: HDMI 0 [HDMI 0]
     Subdevices: 1/1
     Subdevice #0: subdevice #0
   card 1: Gadget [Linux USB Audio Gadget], device 0: USB Audio [USB Audio]
     Subdevices: 1/1
     Subdevice #0: subdevice #0

From above list information we can see sound **``card 1``,\ ``device 0``** is the one associated with USB Gadget Audio device, then we play sound file to this card. In this example, we are using aplay to play a PCM wave audio file: ``sample_s16_le.wav`` `sample_s16_le.wav <https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/device_mode/sample_s16_le.wav>`_

.. code:: batch

   test@madara:~$ aplay -D hw:1,0 sample_s16_le.wav
   Playing WAVE 'sample_s16_le.wav' : Signed 16 bit Little Endian, Rate 48000 Hz, Stereo

Now, from the headset we can hear music is playing out.

--------------

Class 2.0
~~~~~~~~~

.. _ez-kit-target-board-1:

Ez-Kit target board
^^^^^^^^^^^^^^^^^^^

.. code:: c++

   root@adsp-sc589-ezkit:~# ls /dev/snd/
   controlC0  pcmC0D0p   pcmC0D1c   timer
   root@adsp-sc589-ezkit:~# modprobe g_audio c_srate=48000
   g_audio gadget: Linux USB Audio Gadget, version: Feb 2, 2012
   g_audio gadget: g_audio ready
   g_audio gadget: high-speed config #1: Linux USB Audio Gadget

New Sound Card UAC2Gadget(card 1) is generated both for playback and capture on ezkit board:

.. code:: c++

   root@adsp-sc589-ezkit:~# arecord -l
   **** List of CAPTURE Hardware Devices ****
   card 0: sc5xxasoccard [sc5xx-asoc-card], device 1: ADAU1979 adau1977-hifi-1 []
     Subdevices: 1/1
     Subdevice #0: subdevice #0
   card 1: UAC2Gadget [UAC2_Gadget], device 0: UAC2 PCM [UAC2 PCM]
     Subdevices: 1/1
     Subdevice #0: subdevice #0
   root@adsp-sc589-ezkit:~# aplay -l
   **** List of PLAYBACK Hardware Devices ****
   card 0: sc5xxasoccard [sc5xx-asoc-card], device 0: ADAU1962 adau1962.0-0004-0 []
     Subdevices: 1/1
     Subdevice #0: subdevice #0
   card 1: UAC2Gadget [UAC2_Gadget], device 0: UAC2 PCM [UAC2 PCM]
     Subdevices: 1/1
     Subdevice #0: subdevice #0

Record audio data from the new generated UAC2 sound card (arecord **``card 1``**, **``device 0``**) and play the record data via normal playback device (aplay **``card 0``**, **``device 1``**)

.. code:: c++

   root@adsp-sc589-ezkit:~# arecord -f dat -t wav -D hw:1,0 -c 2 -r 48000 -f S16_LE |aplay -D hw:0,0
   Recording WAVE 'stdin' : Signed 16 bit Little Endian, Rate 48000 Hz, Stereo
   Playing WAVE 'stdin' : Signed 16 bit Little Endian, Rate 48000 Hz, Stereo

Play audio over USB on Host
^^^^^^^^^^^^^^^^^^^^^^^^^^^

On Iphone
"""""""""

Just play music on your Iphone, you will hear the sound output from ezkit board.

.. _on-the-linux-host-pc-1:

On the Linux-Host PC
""""""""""""""""""""

With following command you should be able to see the USB Gadget Audio device is there on your HOST:

.. code:: c++

   test@madara:~$ lsusb
   Bus 002 Device 033: ID 1d6b:0101 Linux Foundation Audio Gadget

Then we list the available sound card on host PC, to decide which sound card is associated with EZKIT board

.. code:: c++

   test@madara:~$ cat /proc/asound/cards
    0 [PCH            ]: HDA-Intel - HDA Intel PCH
                         HDA Intel PCH at 0xf7d00000 irq 28
    1 [Gadget         ]: USB-Audio - Linux USB Audio Gadget
                         Linux 4.19.0-yocto-standard with musb-hdrc Linux USB Audio Gadget at usb-0000:0

.. code:: c++

   test@madara:~$ aplay -l
   **** List of PLAYBACK Hardware Devices ****
   card 0: PCH [HDA Intel PCH], device 0: CX20641 Analog [CX20641 Analog]
     Subdevices: 1/1
     Subdevice #0: subdevice #0
   card 0: PCH [HDA Intel PCH], device 3: HDMI 0 [HDMI 0]
     Subdevices: 1/1
     Subdevice #0: subdevice #0
   card 1: Gadget [Linux USB Audio Gadget], device 0: USB Audio [USB Audio]
     Subdevices: 1/1
     Subdevice #0: subdevice #0
   test@madara:~$ arecord -l
   **** List of CAPTURE Hardware Devices ****
   card 0: PCH [HDA Intel PCH], device 0: CX20641 Analog [CX20641 Analog]
     Subdevices: 1/1
     Subdevice #0: subdevice #0
   card 0: PCH [HDA Intel PCH], device 2: CX20641 Alt Analog [CX20641 Alt Analog]
     Subdevices: 1/1
     Subdevice #0: subdevice #0
   card 1: Gadget [Linux USB Audio Gadget], device 0: USB Audio [USB Audio]
     Subdevices: 1/1
     Subdevice #0: subdevice #0

USB Auido Gadget is the sound card 1 (aplay **``card 1``**, **``device 0``**) and Play audio file

.. code:: c++

   test@madara:~$ aplay -D hw:1,0 sample_s16_le.wav
   Playing WAVE 'sample_s16_le.wav' : Signed 16 bit Little Endian, Rate 48000 Hz, Stereo

Now, from the headset we can hear music is playing out.

--------------

**Go TO** :doc:`USB Interface </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/start>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/gadget-mode/002_usb_interface-device_application.jpg
   :width: 600px
