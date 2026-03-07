:doc:`Click here to return to the Gain page </wiki-migration/resources/tools-software/sigmastudiov2/modules/gain>`

Linear Gain with Slew
=====================

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gain/lineargainslew.png
   :alt: lineargainslew.png

Description
-----------

| The Gain block scales the input signal by the specified value in the text field.
| The value (Linear) specified in the textbox is the multiplication factor. The value of “1” will not change the gain value and the value of “0” will mute the audio. The major functionality of Linear Gain module with slew is that, RAM gradually ramps the signal from original to target value rather than a sudden jump of signal.
| ===== Usage ===== Linear or dB value can be entered by clicking on "Lin" or "dB" selection on the UI ( Multiple Control Gain has Linear input only)

Pins
----

Input
~~~~~

+-------------------------+-------------------------------------+-----------------+
| Name                    | Type                                | Description     |
+=========================+=====================================+=================+
| Input<fc #ff0000>X</fc> | Audio(Complex pin for Complex Gain) | Input channel X |
+-------------------------+-------------------------------------+-----------------+

Output
~~~~~~

+--------------------------+-------------------------------------+------------------+
| Name                     | Type                                | Description      |
+==========================+=====================================+==================+
| Output<fc #ff0000>X</fc> | Audio(Complex pin for Complex Gain) | Output channel X |
+--------------------------+-------------------------------------+------------------+

| Note: <fc #ff0000>X</fc> - Channel Index
| ===== Configurable Parameters =====

+--------------------+---------------+--------------+-----------------------------------------------------------+
| GUI Parameter Name | Default Value | Range        | Function Description                                      |
+====================+===============+==============+===========================================================+
| Gain               | 1             | -128 to 128  | Scales the input signal by the specified gain             |
+--------------------+---------------+--------------+-----------------------------------------------------------+
| NumChannels        | 1             | 1            | Number of input channels. Growth option not available     |
+--------------------+---------------+--------------+-----------------------------------------------------------+
| IsDB               | True          | True / False | Controls the gain control is either in dB or linear scale |
+--------------------+---------------+--------------+-----------------------------------------------------------+
| Slew Duration (ms) | 10            | 1 to 2000    | Slew Duration in milliseconds                             |
+--------------------+---------------+--------------+-----------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-----------------------------------------------+------------------------+
| Parameter Name | Description                                   | ADSP-214xx/SC5xx/215xx |
+================+===============================================+========================+
| Gain           | Scales the input signal by the specified gain | Float                  |
+----------------+-----------------------------------------------+------------------------+
| SlewStep       | Smoothness for scaling the signal             | Float                  |
+----------------+-----------------------------------------------+------------------------+

| 
| Following graphs represent how the module behaves when Gain and Slew are set in certain conditions and when Sine wave is given as input to this module:
| |image1|

.. container:: centeralign

   \ **Figure:** Signal behavior when the Slew Duration (ms) is set to 100 ms and the Gain value transitions from 1 to 0


| |image2|

.. container:: centeralign

   \ **Figure:** Signal behavior when the Slew Duration (ms) is set to 1000 ms and the Gain value transitions from 0 to 1


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gain/100milliseconds.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gain/1000milliseconds.png
   :width: 600px
