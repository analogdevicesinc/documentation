Seven Band Level Detector
=========================

:doc:`Click here to return to the Level Detectors/Lookup Tables page </wiki-migration/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/sevenbandleveldetector_003.jpg
   :align: right

The Seven-Band Level Detector block calculates the input signal level, reading directly from the hardware in real time, and displays the level graphically in seven frequency band meter displays:

-  <100Hz
-  250Hz
-  500Hz
-  1kHz
-  2.5kHz
-  5kHz
-  >10kHz

The level detector performs analysis only and does not modify the input signal. The signal at the output pin is identical to the input.

Use the On / Off button to enable or disable the display. The level detector will not function until the schematic design has been compiled and downloaded to the hardware and a USB communication channel is properly configured.

Note: The refresh rate of the display is approximately 10 Hz. The display's performance is limited by your PC system and USB bandwidth. Using multiple level detectors may degrade the responsiveness.
