USB Gadget Audio
================

This page provides how to use the USB Gadget Audio on ADSP-SC5XX board which makes the the Board as an audio card.

.. note::

   The USB Gadget Audio feature can be enabled when following the Quickstarguides within :doc:`Linux for ADSP-SC5xx Processors 3.0.0 (develop) </wiki-migration/resources/tools-software/linuxdsp/releaselandingpages/3.0.0>`. You have to append the following line in the ``conf/local.conf`` file: ``DISTRO_FEATURES:append = " adi_usb_gadget_audio"``\


Hardware Configuration
----------------------

Connect the USB micro-B plug cable into the USB HS/OTG Device port, as showing below:


|image1|

--------------

Example Usage
-------------

Class 2.0
~~~~~~~~~

EZ-KIT target board
^^^^^^^^^^^^^^^^^^^

.. code:: bash

   root@adsp-sc589-mini:~# ls /dev/snd/
   by-path  controlC0  controlC1  pcmC0D0c  pcmC0D0p  pcmC1D0c  pcmC1D0p  timer
   root@adsp-sc589-mini:~# modprobe g_audio c_srate=48000
   g_audio gadget: Linux USB Audio Gadget, version: Feb 2, 2012
   g_audio gadget: g_audio ready

A new sound card ``UAC2Gadget`` is generated both for playback and capture on the EZ-KIT board:

.. code:: bash

   rroot@adsp-sc589-mini:~# arecord -l
   **** List of CAPTURE Hardware Devices ****
   card 0: sc5xxasoccard [sc5xx-asoc-card], device 0: adau1761 adau-hifi-0 []
     Subdevices: 1/1
     Subdevice #0: subdevice #0
   card 1: UAC2Gadget [UAC2_Gadget], device 0: UAC2 PCM [UAC2 PCM]
     Subdevices: 1/1
     Subdevice #0: subdevice #0
   root@adsp-sc589-mini:~# aplay -l
   **** List of PLAYBACK Hardware Devices ****
   card 0: sc5xxasoccard [sc5xx-asoc-card], device 0: adau1761 adau-hifi-0 []
     Subdevices: 1/1
     Subdevice #0: subdevice #0
   card 1: UAC2Gadget [UAC2_Gadget], device 0: UAC2 PCM [UAC2 PCM]
     Subdevices: 1/1
     Subdevice #0: subdevice #0

Record audio data from the new generated UAC2 sound card (arecord **``card 1``**, **``device 0``**) and play the record data via normal playback device (aplay **``card 0``**, **``device 1``**)

.. code:: bash

   root@adsp-sc589-mini:~# arecord -f dat -t wav -D hw:1,0 -c 2 -r 48000 -f S16_LE |aplay -D hw:0,0
   Recording WAVE 'stdin' : Signed 16 bit Little Endian, Rate 48000 Hz, Stereo
   Playing WAVE 'stdin' : Signed 16 bit Little Endian, Rate 48000 Hz, Stereo

Play audio over USB on Host
^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the Linux-Host PC
""""""""""""""""""""

With following command you should be able to see the USB Gadget Audio device is there on your HOST:

.. code:: bash

   test@madara:~$ lsusb
   Bus 002 Device 033: ID 1d6b:0101 Linux Foundation Audio Gadget

Then we list the available sound card on host PC, to decide which sound card is associated with mini board

.. code:: bash

   test@madara:~$ cat /proc/asound/cards
    0 [PCH            ]: HDA-Intel - HDA Intel PCH
                         HDA Intel PCH at 0xf7d00000 irq 28
    1 [Gadget         ]: USB-Audio - Linux USB Audio Gadget
                         Linux 4.19.0-yocto-standard with musb-hdrc Linux USB Audio Gadget at usb-0000:0

.. code:: bash

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

USB Audio Gadget is the sound card 1 (aplay **``card 1``**, **``device 0``**) and Play audio file

.. code:: bash

   test@madara:~$ aplay -D hw:1,0 sample_s16_le.wav
   Playing WAVE 'sample_s16_le.wav' : Signed 16 bit Little Endian, Rate 48000 Hz, Stereo

Now, from the headset we can hear music is playing out.

--------------

**Go TO** :doc:`USB Interface </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/start>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/gadget-mode/002_usb_interface-device_application.jpg
   :width: 600px
