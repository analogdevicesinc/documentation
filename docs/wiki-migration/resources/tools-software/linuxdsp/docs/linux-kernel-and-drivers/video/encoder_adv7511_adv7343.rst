Video Encoder EI3 Extender Example
==================================

The Video Encoder EI3 Extender Board is a separately daughter board that plugs onto the EI3 of an EZ-KIT LITE/EZ-Board, it extends the capabilities of the EZ-KIT LITE/EZ-Board by providing a connection between the enhanced parallel peripheral interface (EPPI) of the processor and the **ADV7511** and **ADV7341 ** video encoder. For more information about the ADV7511, ADV7341 or Video Encoder EI3 Extender Board, go to www.analog.com and search for ADV7511 or ADV7341 or Video Encoder EI3 Extender Board.

Hardware Connection
-------------------

Connect the Video Encoder EI3 Extender Board board to the P1A connector on the ADSP-SC5XX EZ-Board.

Only HD format is supported for **ADV7511**, so connect an HDMI cable to a TV to display captured HD yuv file (720p).


|image1|

**ADV7341** supports NTSC and PAL format video. Connect the Composite port on the adapter board to TV video port using 3RCA cable.


|image2|

| 
| ===== Software Configuration ===== The following configuration should be done on top of the sc589-ezkit/sc573-ezkit default configuration.

| 
| ==== Package Configuration ==== Add the v4l2-video-test package in the filesystem, it's enabled in adsp-sc5xx-full image by default.

::

   vim build/conf/local.conf
   IMAGE_INSTALL_append = "v4l2-video-test"

| 
| ==== Kernel Configuration ==== Run "**bitbake linux-adi -c menuconfig**" to configure the linux kernel. Due to the conflicts with audio module, users should disable the audio driver before enable video drivers.

-  **Disable audio driver**

::

   Device Drivers  --->
       < > Sound card support  ----

-  **Enable I2C support**

::

   Device Drivers  --->
       I2C support  --->
           I2C Hardware Bus support  --->
                   <*> ADI TWI I2C support
                   (50) ADI TWI I2C clock (kHz) 

-  **Enable Microchip MCP23xxx I/O expander support**

::

   Device Drivers  --->
       -*- Pin controllers  --->
            <*> Microchip MCP23xxx I/O expander

-  **Enable V4L2 display platform driver and ADV7343 video encoder drivers**

As there is only one PPI on the ADSP-SC5xx board, **please don't select V4L2 capture and display platform driver at the same time. You can't select ADV7511 and ADV7343 either.** If you want to display HD video, please select ADV7511 HDMI transmitter driver. For SD video you should choose ADV7343 video encoder driver, it should be noted that driver for ADV7343 works for ADV7341 as well.

::

   Device Drivers  --->
       <*> Multimedia support  --->
           [*]   Cameras/video grabbers support
           [*]   Media Controller API
           [*]   V4L2 sub-device userspace API
           [*]   V4L platform devices  --->
                 <*>   ADI SC5XX  Video Display Driver
           [N]   Autoselect ancillary drivers (tuners, sensors, i2c, spi, frontends)
           I2C Encoders, decoders, sensors and other helper chips  --->
                 <*> ADV7343 video encoder
   or
                 <*> Analog Devices ADV7511 encoder
                 [*]   Enable Analog Devices ADV7511 CEC support 

-  \*\* Disable SPI Driver*\*

As the PPI hardware pin conflicts with SPI on the **ADSP-SC573 EZ-Board**, you should disable SPI before using ppi, otherwise you will get a pin request error message from pinctrl. So extra configuration only for ADSP-SC573 EZ-Board:

::

   Device Drivers  --->
       [*] SPI support  --->
           <>   SPI controller v3 for ADI

| 
| ==== Device Tree ==== Run "**bitbake linux-adi -c devshell**" to enter into the kernel source code and then change the device tree files.

-  **Device node for soft switch on Video Encoder EI3 Extender Board**

Please add following child node ssw2 to i2c0 master node in the device tree(sc589-ezkit.dts/sc573-ezkit.dts). We need to setup soft switch before we start display streaming.

::

   $ vim arch/arm/boot/dts/sc589-ezkit.dts
   i2c0: twi@31001400 {
   ...
   ssw1: gpio@0x22 {
        compatible = "microchip,mcp23017";
        gpio-controller;
        #gpio-cells = <2>;
        reg = <0x22>;
   };
   +ssw2: gpio@0x25 {
   +     compatible = "microchip,mcp23017";
   +     gpio-controller;
   +     #gpio-cells = <2>;
   +     reg = <0x25>;
   +};
   adau1979@0x11 {
        compatible = "adi,adau1977";
        reg = <0x11>;
   };

| 
| ===== ADV7511 HDMI Transmitter Test ===== One thing to note here is that the ADSP-SC573 can support up to 56.25MHz ppi clock when transmitting data or frame sync, however, ADSP-SC589 can support up to 75MHz ppi clock, and there are two different ppi clock generators on Video Encoder EI3 Extender Board: 27MHz and 74MHz, so we can enable 27MHz clock both for ADSP-SC573 EZ-Board and ADSP-SC589 EZ-Board, and 74MHz clock only for ADSP-SC589 EZ-Board. For more information, please refer to the data sheets of ADSP-SC573/ADSP-SC589 and the Video Encoder EI3 Extender Board Manual.

Setup Soft Switch
~~~~~~~~~~~~~~~~~

The state of pins from IO expander is "uncertain" after we enable Soft Switch on the ADSP-SC573 EZ-Board, some pins are also the OE pins (active low) of modules, as the PPI signal pins are reused by many modules, you should disable related modules by setting Soft Switch first, otherwise the signals from ppi will be interfered. So extra configuration only for **ADSP-SC573 EZ-Board**:

::

   Only for ADSP-SC573 EZ-Board:
   # echo 482 > /sys/class/gpio/export
   # echo high > /sys/class/gpio/gpio482/direction
   # echo 485 > /sys/class/gpio/export
   # echo high > /sys/class/gpio/gpio485/direction
   # echo 505 > /sys/class/gpio/export
   # echo high > /sys/class/gpio/gpio505/direction

**Only for ADSP-SC589 EZ-Board (74MHz PPI clock):**

::

   # echo 466 > /sys/class/gpio/export
   # echo low > /sys/class/gpio/gpio466/direction
   # echo 469 > /sys/class/gpio/export
   # echo low > /sys/class/gpio/gpio469/direction
   # echo 503 > /sys/class/gpio/export
   # echo low > /sys/class/gpio/gpio503/direction

**Both for  ADSP-SC573 EZ-Board and ADSP-SC589 EZ-Board (27MHz PPI clock):**

::

   # echo 466 > /sys/class/gpio/export
   # echo low > /sys/class/gpio/gpio466/direction
   # echo 468 > /sys/class/gpio/export
   # echo low > /sys/class/gpio/gpio468/direction
   # echo 503 > /sys/class/gpio/export
   # echo low > /sys/class/gpio/gpio503/direction

Display Video Images
~~~~~~~~~~~~~~~~~~~~

You can use "v4l2_video_display" provided to play HD yuv file and output the HD signal via ADV7511, the HD signal will be transmitted to TV, then you will see the image on TV.

::

   # v4l2_video_display -F 720p60.yuv

| 
| ===== ADV7341 Video Encoder Test =====

.. _setup-soft-switch-1:

Setup Soft Switch
~~~~~~~~~~~~~~~~~

The state of pins from IO expander is "uncertain" after we enable Soft Switch on the ADSP-SC573 EZ-Board, some pins are also the OE pins (active low) of modules, as the PPI signal pins are reused by many modules, you should disable related modules by setting Soft Switch first, otherwise the signals from ppi will be interfered. So extra configuration only for **ADSP-SC573 EZ-Board**:

::

   Only for ADSP-SC573 EZ-Board:
   # echo 482 > /sys/class/gpio/export
   # echo high > /sys/class/gpio/gpio482/direction
   # echo 485 > /sys/class/gpio/export
   # echo high > /sys/class/gpio/gpio485/direction
   # echo 505 > /sys/class/gpio/export
   # echo high > /sys/class/gpio/gpio505/direction

**Both for ADSP-SC573 and ADSP-SC589 EZ-Boards**

::

   # echo 468 > /sys/class/gpio/export    
   # echo low > /sys/class/gpio/gpio468/direction
   # echo 470 > /sys/class/gpio/export
   # echo low > /sys/class/gpio/gpio470/direction

.. _display-video-images-1:

Display Video Images
~~~~~~~~~~~~~~~~~~~~

You can use "v4l2_video_display" provided to play pal yuv file and output the component analog signal via ADV7341, the analog signal will be transmitted to TV by 3RCA cable, then you will see the image on TV.

::

   # v4l2_video_display -F pal.yuv 

| 
| ---- **Back to** :doc:`Linux Video Driver </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/video/linux_video_driver>`  

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/video/encoder.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/video/cable.jpg
   :width: 600px
