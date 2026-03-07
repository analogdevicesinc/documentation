:doc:`Click here to return to the GPIO Conditioning page </wiki-migration/resources/tools-software/sigmastudiov2/modules/gpioconditioning>`

Push and Hold
=============

| 
| |push_and_hold_ssp.jpg|
| ===== Description =====
| This block can be used for functions like a pushbutton, to condition a GPIO input to create pulses in response to the user pushing or holding the button.
| ===== Usage =====
| A typical application would be a volume control comprising two buttons, one for up and the other for down.

-  Drag the block into the workspace.
-  Right-click it and select the algorithm:

   -  **push_hold**
   -  **push/hold 2-in 2-out**
   -  **push/hold with two-button mute**

-  Set the parameters to fit your application:


| 
|

.. hint::

   Note: For the picture above right, push_hold was selected. Use push/hold 2-in 2-out to condition two GPIO inputs, for example one up and one down. Push/hold with mute works the similarly but with the extra feature that if both buttons are pressed, a mute pulse is generated (bottom output pin). To un-mute, any of the buttons can be pressed.


| ===== Targets Supported =====

+---------------+------------+-----------------------+---------------+------------------+
| Name          | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+===============+============+=======================+===============+==================+
| Push and Hold | NA         | NA                    | S             | NA               |
+---------------+------------+-----------------------+---------------+------------------+

| 
| ===== Pins =====

Input
-----

+--------+---------+------------------------------------------------------------+
| Name   | Type    | Description                                                |
+========+=========+============================================================+
| Input0 | Control | Control Signal input that is detected by the push and hold |
+--------+---------+------------------------------------------------------------+

Output
------

======= ======= ====================
Name    Type    Description
======= ======= ====================
Output0 Control Push and hold output
======= ======= ====================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+------------+-----------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range      | Function Description                                                                    |
+====================+===============+============+=========================================================================================+
| Hold               | 500           | 0 to 10000 | Determines how long the signal is held before the repeat pulses are generated.          |
+--------------------+---------------+------------+-----------------------------------------------------------------------------------------+
| Repeat             | 250           | 0 to 10000 | Sets the interval between repeated pulses. Enter the time in milliseconds in the field. |
+--------------------+---------------+------------+-----------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

============== ====================== =================
Parameter Name Description            ADAU145x/ADAU146x
============== ====================== =================
holdtime       hold time in samples   Integer32
repeattime     repeat time in samples Integer32
============== ====================== =================

| 
| ===== DSP Parameter Computation =====
| holdtime= Hold\*0.001\*FS
| repeattime= Repeat\*0.001\*FS
| FS - sampling rate

.. |push_and_hold_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gpioconditioning/push_and_hold_ssp.jpg
