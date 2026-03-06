:doc:`Click here to return to the GPIO Conditioning page </wiki-migration/resources/tools-software/sigmastudiov2/modules/gpioconditioning>`

Push Button Volume With Mute
============================

| |pushbuttonvolumewithmute.png|
| ===== Description =====
| The Push Button Volume with Mute block can be used with the GPIO push buttons to control the volume of an input audio signal. This block has the functionality of the Push and Hold, Up/Down Control, Index lookup Table, and SW External Volume control all in one block. The user has the flexibility to define a custom volume curve, used for taper, that is indexed through the pushbuttons.
| ===== Usage =====
| ===== Targets Supported =====

+--------------------------------------+------------+-----------------------+---------------+------------------+
| Name                                 | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+======================================+============+=======================+===============+==================+
| Push Button Volume Control with Mute | NA         | NA                    | S             | NA               |
+--------------------------------------+------------+-----------------------+---------------+------------------+

| 
| ===== Pins =====

Input
-----

====== ======= ============
Name   Type    Description
====== ======= ============
Input0 Control Up Volume
Input1 Control Down Volume
Input2 Control Interface In
Input4 Control Audio Data
====== ======= ============

Output
------

======= ======= =============
Name    Type    Description
======= ======= =============
Output0 Control Interface Out
Output1 Data    Audio Data
======= ======= =============

.. |pushbuttonvolumewithmute.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gpioconditioning/pushbuttonvolumewithmute.png
