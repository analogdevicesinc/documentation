Linux Video Driver
==================

Introduction
------------

This section describes the steps required to build and use video driver to capture or display video images on Linux using an ADSP-SC5xx board, a Video Decoder EI3 Extender Board and a Video Encoder EI3 Extender Board.

The Linux Kernel Media Subsystems provides support for devices like webcams, streaming capture and output, analog TV, digital TV, AM/FM  radio, Sofware Digital Radio (SDR) and remote controllers.

The Linux Media Infrastructure API converges the kernel to userspace APIs used on media drivers. It has 4 parts:

-  Part I: The V4L2 API
-  Part II: The Linux DVB API
-  Part III: The Remote Controller API
-  Part IV: The Media Controller API

For more information about the Linux Kernel Media Subsystems, please refer to http://linuxtv.org/.

Hardware Required
-----------------

-  An ADSP-SC5XX EZ-Board

   -  ADSP-SC589 Ezkit v1.1 and above, or,
   -  ADSP-SC573 Ezkit v1.2 (BOM 1.8) and above

-  A Video Decoder EI3 Extender Board, or
-  A Video Encoder EI3 Extender Board
-  HDMI Cable and 3RCA Cable

EPPI on ADSP-SC5XX EZ-Board
---------------------------

The Enhanced Parallel Peripheral Interface (EPPI) is a half-duplex, bidirectional port with a dedicated clock pin and three frame sync (FS) pins directly output from the processor. It can support direct connections to active TFT LCDs, parallel A/D and D/A converters, video encoders and decoders, image sensor modules and other general-purpose peripherals. We can find EPPI port from P1A connector on the back of ADSP-SC5XX EZ-Board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/video/1.jpg
   :width: 600px

| 
| Refer below pages for the detailed useage of ADI video encoders and decoders ADV7842, ADV7511, ADV7343 on ADSP-SC5XX EZ-Board.

-  :doc:`Video Decoder EI3 Extender Example </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/video/adv7842>`
-  :doc:`Video Encoder EI3 Extender Example </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/video/encoder_adv7511_adv7343>`

| 
| ---- **Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`  
