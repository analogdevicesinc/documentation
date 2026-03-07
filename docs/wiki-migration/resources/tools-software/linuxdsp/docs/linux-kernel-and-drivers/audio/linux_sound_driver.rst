Linux Sound Driver
==================

Introduction
------------

This section describes the steps required to build and use sound driver to record and play audio files on Linux using an ADSP-SC5xx board.

The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI functionality to the Linux operating system.

For more information about the Advanced Linux Sound Architecture (ALSA), please refer to http://www.alsa-project.org/main/index.php/Main_Page.

Hardware Setup
--------------

-  An ADSP-SC5xx EZ-Board:

   -  ADSP-SC589 Ezkit v1.1 and above, or,

      -  ADSP-SC584 Ezkit v1.0 and above, or,
      -  ADSP-SC589 MINI, or,
      -  ADSP-SC573 Ezkit v1.2 (BOM 1.8) and above

-  Two line cables, a line-in and line-out cables

Take the ADSP-SC573 EZ-Board as an example, connect line-in cables to J3 and line-out cables to J11, or you can plug one headphone into the Headphone JACK directly for DAC.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/audio/lkad-linux_sound_driver-hw.jpg
   :width: 400px

Software Configuration
----------------------

The following configuration should be done on top of the SC589-ezkit/SC584-ezkit/SC573-ezkit/SC589-MINI default configuration.

Package Configuration
~~~~~~~~~~~~~~~~~~~~~

The ALSA utility provides many simple and powerful tools for testing the ALSA drivers to make sure they are working correctly, such as arecord, aplay, amixer, speaker-test, etc. arecord is a command-line soundfile recorder for the ALSA soundcard driver, it supports several file formats and multiple soundcards with multiple devices, aplay is much the same, only it plays instead of recording; amixer allows command-line control of the mixer for the ALSA soundcard driver; speaker-test is a command-line speaker test tone generator for ALSA, it can be used to test the speakers of a device.

Add the alsa-utils and alsa-lib packages in the filesystem, they're enabled in adsp-sc5xx-full image by default.

Enable alsa-lib and alsa-utils support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   vim build/conf/local.conf
   IMAGE_INSTALL_append = "alsa-utils alsa-lib"

Then run “bitbake adsp-sc5xx-minimal -C compile” or “bitbake adsp-sc5xx-full -C compile” to generate the filesystem.

Configure Linux Kernel
~~~~~~~~~~~~~~~~~~~~~~

Run "bitbake linux-adi -c menuconfig" and configure the kernel as follows:

**Enable ADAU1962 sound card driver:**

::

   Device Drivers  --->
           <*> Sound card support  --->
                     <*>   Advanced Linux Sound Architecture  --->
                         <*>   ALSA for SoC audio support  --->
                             <*>   SoC Audio for the ADI SC5XX chip
                             <*>   Support for the ADAU1962 board on SC5XX ezkit board

**Enable ADAU1979 sound card driver:**

::

   Device Drivers  --->
        <*> Sound card support  --->
              <*>   Advanced Linux Sound Architecture  --->
                  <*>   ALSA for SoC audio support  --->
                        <*>   SoC Audio for the ADI SC5XX chip
                        <*>     Support for the ADAU1979 board on SC5XX ezkit board

**Enable ADAU1761 sound card driver for ADSP-SC589 MINI board:**

::

   Device Drivers  --->
        <*> Sound card support  --->
              <*>   Advanced Linux Sound Architecture  --->
                  <*>   ALSA for SoC audio support  --->
                        <*>   SoC Audio for the ADI SC5XX chip
                        <*>     Support for the ADAU1761 Machine driver on SHARC Audio board

Example
-------

Find the device
~~~~~~~~~~~~~~~

After the configuration in above steps, you are able to find the audio device information in boot log:


|image1|

You are able to use arecord -l and aplay -l to find the card number.

::

   # arecord -l
   **** List of CAPTURE Hardware Devices ****
   card 0: sc5xxasoccard [sc5xx-asoc-card], device 1: ADAU1979 adau1977-hifi-1 []
      Subdevices: 1/1
      Subdevice #0: subdevice #0
   # aplay -l
   **** List of PLAYBACK Hardware Devices ****
   card 0: sc5xxasoccard [sc5xx-asoc-card], device 0: ADAU1962 adau1962-hifi-0 []
      Subdevices: 1/1
      Subdevice #0: subdevice #0

 In **capture** case, you can find "0" is the **card number**, and "1" is the **device number**;

In **playback** case, you can find "0" is the **card number**, and "0" is the **device number**.

Amixer setting
~~~~~~~~~~~~~~

If you want to unmute the ADC and DAC or adjust the volume, you can use the **amixer** tool.

::

   # amixer -c 0 controls
   numid=41,iface=MIXER,name='ADC1 Capture Volume'
   numid=49,iface=MIXER,name='ADC1 DC Substraction Capture Switch'
   numid=45,iface=MIXER,name='ADC1 Highpass-Filter Capture Switch'
   numid=42,iface=MIXER,name='ADC2 Capture Volume'
   numid=50,iface=MIXER,name='ADC2 DC Substraction Capture Switch'
   numid=46,iface=MIXER,name='ADC2 Highpass-Filter Capture Switch'
   numid=43,iface=MIXER,name='ADC3 Capture Volume'
   numid=51,iface=MIXER,name='ADC3 DC Substraction Capture Switch'
   numid=47,iface=MIXER,name='ADC3 Highpass-Filter Capture Switch'
   numid=44,iface=MIXER,name='ADC4 Capture Volume'
   numid=52,iface=MIXER,name='ADC4 DC Substraction Capture Switch'
   numid=48,iface=MIXER,name='ADC4 Highpass-Filter Capture Switch'
   numid=3,iface=MIXER,name='DAC Deemphasis Switch'
   numid=40,iface=MIXER,name='DAC Oversampling Rate'
   numid=2,iface=MIXER,name='DAC Playback Switch'
   numid=1,iface=MIXER,name='DAC Playback Volume'
   numid=5,iface=MIXER,name='DAC1 Playback Switch'
   numid=4,iface=MIXER,name='DAC1 Playback Volume'
   numid=6,iface=MIXER,name='DAC1 Power Adjust'
   numid=32,iface=MIXER,name='DAC10 Playback Switch'
   numid=31,iface=MIXER,name='DAC10 Playback Volume'
   numid=33,iface=MIXER,name='DAC10 Power Adjust'
   numid=35,iface=MIXER,name='DAC11 Playback Switch'
   numid=34,iface=MIXER,name='DAC11 Playback Volume'
   numid=36,iface=MIXER,name='DAC11 Power Adjust'
   numid=38,iface=MIXER,name='DAC12 Playback Switch'
   numid=37,iface=MIXER,name='DAC12 Playback Volume'
   numid=39,iface=MIXER,name='DAC12 Power Adjust'
   numid=8,iface=MIXER,name='DAC2 Playback Switch'
   numid=7,iface=MIXER,name='DAC2 Playback Volume'
   numid=9,iface=MIXER,name='DAC2 Power Adjust'
   numid=11,iface=MIXER,name='DAC3 Playback Switch'
   numid=10,iface=MIXER,name='DAC3 Playback Volume'
   numid=12,iface=MIXER,name='DAC3 Power Adjust'
   numid=14,iface=MIXER,name='DAC4 Playback Switch'
   numid=13,iface=MIXER,name='DAC4 Playback Volume'
   numid=15,iface=MIXER,name='DAC4 Power Adjust'
   numid=17,iface=MIXER,name='DAC5 Playback Switch'
   numid=16,iface=MIXER,name='DAC5 Playback Volume'
   numid=18,iface=MIXER,name='DAC5 Power Adjust'
   numid=20,iface=MIXER,name='DAC6 Playback Switch'
   numid=19,iface=MIXER,name='DAC6 Playback Volume'
   numid=21,iface=MIXER,name='DAC6 Power Adjust'
   numid=23,iface=MIXER,name='DAC7 Playback Switch'
   numid=22,iface=MIXER,name='DAC7 Playback Volume'
   numid=24,iface=MIXER,name='DAC7 Power Adjust'
   numid=26,iface=MIXER,name='DAC8 Playback Switch'
   numid=25,iface=MIXER,name='DAC8 Playback Volume'
   numid=27,iface=MIXER,name='DAC8 Power Adjust'
   numid=29,iface=MIXER,name='DAC9 Playback Switch'
   numid=28,iface=MIXER,name='DAC9 Playback Volume'
   numid=30,iface=MIXER,name='DAC9 Power Adjust'

 

If you want to increase the volume of ADC1 and ADC2, you can set a bigger value.

::

   # amixer -c 0 cget numid=41
   numid=41,iface=MIXER,name='ADC1 Capture Volume'
      ; type=INTEGER,access=rw—R–,values=1,min=0,max=255,step=0
      : values=95
      | dBminmaxmute-min=-35.62dB,max=60.00dB

::

   # amixer -c 0 cset numid=41 200
   numid=41,iface=MIXER,name='ADC1 Capture Volume'
      ; type=INTEGER,access=rw---R–,values=1,min=0,max=255,step=0
      : values=200
      | dBminmaxmute-min=-35.62dB,max=60.00dB

::

   # amixer -c 0 cset numid=42 200
   numid=42,iface=MIXER,name='ADC2 Capture Volume'
      ; type=INTEGER,access=rw---R–,values=1,min=0,max=255,step=0
      : values=200
      | dBminmaxmute-min=-35.62dB,max=60.00dB

'DAC Playback Switch' is the DAC master mute.

'DAC Playback Volume' is the master volume control.

'DAC1 Playback Switch' is the DAC channel 1 mute control.

::

   # amixer -c 0 cget numid=5
   numid=5,iface=MIXER,name='DAC1 Playback Switch'
      ; type=BOOLEAN,access=rw------,values=1
      : values=on

You can set 0 or 1 to mute or unmute DAC channel 1.

'DAC1 Playback Volume' is the DAC channel 1 volume control.

::

   # amixer -c 0 cget numid=4
   numid=4,iface=MIXER,name='DAC1 Playback Volume'
      ; type=INTEGER,access=rw---R–,values=1,min=0,max=255,step=0
      : values=255
      | dBminmaxmute-min=-95.62dB,max=0.00dB

You can set value 0 - 255. The range is from -95.625 dB to 0 dB. Each 1-bit step corresponds to a 0.375dB change in volume.

'DAC1 Power Adjust' is the DAC channel 1 power adjust control.

::

   # amixer -c 0 cget numid=6
   numid=6,iface=MIXER,name='DAC1 Power Adjust'
      ; type=ENUMERATED,access=rw------,values=1,items=4
      ; Item #0 'Low Power'
      ; Item #1 'Lowest Power'
      ; Item #2 'Best Performance'
      ; Item #3 'Good Performance'
      : values=2

You can choose a power state for this DAC channel.

Record audio file
~~~~~~~~~~~~~~~~~

You can use arecord tool to record audio stream, and we already know "0" is the card number, "1" is the device number for capture case in "Find the device" section, so you can use "-D hw:<card number>, <device number>" to select the pcm device.

For example, record stereo 48KHz 32bits stream:

::

   # arecord -D hw:0,1 -c 2 -r 48000 -f S32_LE -t wav sample.wav

Play audio file
~~~~~~~~~~~~~~~

If you have a sample wav file, you can use **aplay** tool or **speaker-test** tool to test the playback, and we already know "0" is the card number, "0" is the device number for playback case, so you can use **"-D hw:<card number>, <device number>"** to select the pcm device. Also you can use **"-D plug:dmix:<card number>"** for dmix plugin to test the playback.

::

   # aplay -D hw:0,0 sample.wav 
   # aplay -D plug:dmix:0 sample.wav

 Or you can use speaker-test tool:

**Test 2 channels playback:**

::

   # speaker-test -D hw:0,0 -c 2 -t sine -F S32_LE
   # speaker-test -D plug:dmix:0 -c 2 -t sine -f 1000 -r 4800

**Test 4 channels playback:**

::

   # speaker-test -D hw:0,0 -c 4 -t sine -F S32_LE

Loopback
~~~~~~~~

If you want to hear the audio at the ADC input, you can use following command:

::

   # arecord -D hw:0,1 -c 2 -r 48000 -f S32_LE | aplay -D hw:0,0

--------------

**Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/audio/lkad-linux_sound_driver-find_the_device.jpg
   :width: 400px
