Adaptive Mixer Single (Graph)
=============================

| 
| :doc:`Click here to return to the Advanced DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/advanceddsp>`
| The Adaptive Mixer single (graph) cell is an advanced method of mixing two signals based on a third control signal. The two green pins designate the two input signals mix together and the third orange pin is for the control signal.

| Note: usually orange pins indicate that this channel is not for true audio, but this is not the case for this cell. The orange pin here indicates that the input control signal will be converted to a RMS average value, eliminating the need to use the RMS table for this application. The RMS table value is used to determine the scale factors for the signals to be mixed. This cell is very similar to the Adaptive Mixer Single (graph), but allows more advanced control over the scale factors for the signals to be mixed. In the Single case, one scale factor is determined as the compliment of the other, whereas with the Dual control, you can select and change the curves for both signals to be mixed.\|\ |image1|\ \|

Input Pins
----------

+-----------------+------------------------------------+--------------------------------------------------+
| Name            | Format [int/dec] - [control/audio] | Function Description                             |
+=================+====================================+==================================================+
| Pin 0: Audio In | decimal - audio                    | Audio Input                                      |
+-----------------+------------------------------------+--------------------------------------------------+
| Pin 1: Audio In | decimal - audio                    | Audio Input                                      |
+-----------------+------------------------------------+--------------------------------------------------+
| Pin 2: Audio In | decimal - audio                    | Calculates the RMS average for this input signal |
+-----------------+------------------------------------+--------------------------------------------------+

Output Pins
-----------

+------------------+------------------------------------+------------------------------+
| Name             | Format [int/dec] - [control/audio] | Function Description         |
+==================+====================================+==============================+
| Pin 0: Audio Out | decimal - audio                    | Compressed mono audio output |
+------------------+------------------------------------+------------------------------+

| 
| ==== GUI Controls ====

+------------------+---------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range      | Function Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+==================+===============+============+=======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| RMS TC (db/s)    | 150           | 1 - 1000   | Controls the Time Constant (TC) setting the attack time of the RMS average computation. The RMS time constant determines how rapidly the gain will adapt to abrupt changes in the input signal level.                                                                                                                                                                                                                                                                                                                 |
+------------------+---------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| step             | 8             | 1 - 23     | Controls the slew ram rate in terms of how quickly the algorithm ramps to the next value.The step is usually calculated by: Step = (Target Data - Slew Data) / Number of Steps , Here, you have control over this value and the ramp will be calculated according to 2-step                                                                                                                                                                                                                                           |
+------------------+---------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Smooth           | False         | True/False | This checkbox determines whether the ratio curve of the levels will be exactly linear from graph point to graph point, or if it will be smoothed out.                                                                                                                                                                                                                                                                                                                                                                 |
+------------------+---------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Show Graph       |               |            | This button allows you to bring up the mix ratio window. For the case of the Single mixer, you only have control over the level of the 2nd input pin. You can change the curve by moving, adding, or removing graph points.The output curve scale value for the 1st pin is automatically calculated as the compliment of the 2nd pin. The RMS table value gives you the x-value on this graph and the corresponding y-values will be the scale factors for the output levels of the mix between the 1st and 2nd pins. |
+------------------+---------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/advanceddsp/adaptivemixerdual.jpg
