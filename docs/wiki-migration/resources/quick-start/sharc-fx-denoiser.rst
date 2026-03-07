Getting started with NN Denoiser model on SHARC-FX
==================================================

Hardware Requirements
---------------------

To set up and run the NN denoiser model on SHARC-FX, the following hardware is required:

:adi:`ADSP-SC835W-SOM <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adspsc835w-ev-som.html>` - This is a small board containing the SC835 processor (SHARC-FX + M33) and JTAG.

:adi:`EV-SOMCRR-EZKIT <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/ev-somcrr-ezkit.html>` - This adapter board provides all of the peripherals for the denoiser application.

:adi:`ICE-1000 or ICE-2000 <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/emulators.html>` - An in-circuit emulator used to debug and download the application to the processor.

To use the denoiser, an audio source and either headphones or a speaker with a 3.5mm connector are required.

Software Requirements
---------------------

You will need CrossCore Embedded Studio, version 3.0.1 onwards, available from :adi:`analog.com/cces <cces>`.

CrossCore Embedded Studio includes a 90-day full-featured trial license. Alternatively, the SC835W SOM provides a license that is not time-limited but restricted to use with the ADSP-SC835 and ICE-1000.

TFLM Sources
------------

Sources for the TFLM library with associated examples can be found on :git-tflite-micro>`__

Support
-------

Please contact `processor.tools.support@analog.com <https::`GitHub/analogdevicesinc/tflite-micro </wiki.analog.com/mailto/processor.tools.support@analog.com>` for any queries.
