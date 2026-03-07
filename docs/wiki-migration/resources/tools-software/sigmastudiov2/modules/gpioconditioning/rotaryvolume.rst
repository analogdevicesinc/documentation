:doc:`Click here to return to the GPIO Conditioning page </wiki-migration/resources/tools-software/sigmastudiov2/modules/gpioconditioning>`

Rotary Volume
=============

| 
| |rotary_vol_ssp.jpg|
| ===== Description =====
| The Rotary Volume block controls the volume level of an input audio signal, using the GPIO rotary encoder inputs. This block has the functionality of the Rotary Encoder, Up/Down Control, Index lookup Table, and SW External Volume control blocks all in one algorithm control. The user has the flexibility to define a custom volume curve that will be scrolled through by the rotary encoder.

| 
| ===== Usage =====
| The Rotary Volume control allows a GPIO inputs from a rotary encoder to control a custom volume curve. The volume curve can be any linear, logarithmic, or custom curve designed with any number of points. When the encoder is turned the volume will increase or decrease according to the volume curve in the table. The transition between points in the table has a smooth transition and the rate is determined by the Slew rate parameter. The Debounce time is used to smooth the actual physical input of the GPIO rotary encoder.

| The following image shows how two GPIO inputs are used to control the volume algorithm in the Rotary Volume block. The Rotary Volume algorithm has been grown in order to support stereo audio. A mux switch allows comparison between the direct signal from the Inputs, and the volume adjusted signal, routed to the Outputs. The Interface Read and Write blocks allow the last volume level to be saved and recalled.
| |rotary_vol_eg_ssp.jpg|
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

+-------------+---------+----------------------------------------------------------------------------------+
| Name        | Type    | Description                                                                      |
+=============+=========+==================================================================================+
| Up Volume   | Control | Control Signal input for rotary volume increment                                 |
+-------------+---------+----------------------------------------------------------------------------------+
| Down Volume | Control | Control Signal input for rotary volume decrement                                 |
+-------------+---------+----------------------------------------------------------------------------------+
| InterfaceIn | Logic   | Interface Read register to load previous constant volume data value to algorithm |
+-------------+---------+----------------------------------------------------------------------------------+
| Input0      | Audio   | Audio to the volume control                                                      |
+-------------+---------+----------------------------------------------------------------------------------+

Output
------

+--------------+-------+-------------------------------------------------------------------+
| Name         | Type  | Description                                                       |
+==============+=======+===================================================================+
| InterfaceOut | Logic | Interface Write register to store constant volume data for recall |
+--------------+-------+-------------------------------------------------------------------+
| Output0      | Audio | Volume adjusted audio output                                      |
+--------------+-------+-------------------------------------------------------------------+

| 
| ===== Growth =====
| Audio channels can be grown upto 20 channels.

Configurable Parameters
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------+---------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range        | Function Description                                                                                                                                                                                                                                                                                                                     |
+====================+===============+==============+==========================================================================================================================================================================================================================================================================================================================================+
| CountMax           | 20            | [0, 1000]    | Sample counter for the Debounce time on the Rotary Encoder                                                                                                                                                                                                                                                                               |
+--------------------+---------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NoOfTableValues    | 33 pts        | [2, 800]     | Sets the table size: the  number of points used in the volume table curve.                                                                                                                                                                                                                                                               |
+--------------------+---------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TableValues        | 1             | [-16, 15.99] | The table points are the actual gain values for the volume curve in linear representation. Although the range supports the full values of [-16, 15.99] the table values should generally be between [0, 1] for proper gain adjustments. The user has full control in this table to add a linear, logarithmic of custom gain volume curve |
+--------------------+---------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWSlew             | 12            | [1, 23]      | Controls the slew ramp speed for the volume transition between consecutive volume gain points                                                                                                                                                                                                                                            |
+--------------------+---------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+--------------------------------------------------------------------------------+-------------------+
| Parameter Name | Description                                                                    | ADAU145x/ADAU146x |
+================+================================================================================+===================+
| countmax       | The integer number is directly written to the DSP                              | Integer32         |
+----------------+--------------------------------------------------------------------------------+-------------------+
| table_p0       | All the points in the table are written to the DSP in their linear gain format | FixPoint8d24      |
+----------------+--------------------------------------------------------------------------------+-------------------+
| step           | The value for the slew rate                                                    | FixPoint8d24      |
+----------------+--------------------------------------------------------------------------------+-------------------+

| 
| ===== DSP Parameter Computation =====
| step = 2^(-1\*SWSlew)

.. |rotary_vol_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gpioconditioning/rotary_vol_ssp.jpg
.. |rotary_vol_eg_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gpioconditioning/rotary_vol_eg_ssp.jpg
