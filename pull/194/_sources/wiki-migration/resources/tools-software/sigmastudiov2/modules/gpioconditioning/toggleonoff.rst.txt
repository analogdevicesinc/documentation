:doc:`Click here to return to the GPIO Conditioning page </wiki-migration/resources/tools-software/sigmastudiov2/modules/gpioconditioning>`

Toggle On-Off
=============

| 
| |toggle_on_off_ssp.jpg|
| ===== Description =====
| The Toggle On/Off cell toggles its output when it detects a rising edge on its input. The amplitude of the output signal can be set using the drop-down control in the cell's GUI.
| ===== Usage =====
| The toggle on/off cell detects rising edges on its input and toggles its output each time another rising edge is encountered. In other words, if the output is zero and a rising edge appears on the input, the output will change to one. Conversely, if the output is one and a rising edge appears on the input, the output will change to zero. The bit to be toggled at the output is chosen using the drop down in the module UI. The other bits (other than the selected one) of the output remain zero.
| ===== Targets Supported =====

+---------------+------------+-----------------------+---------------+------------------+
| Name          | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+===============+============+=======================+===============+==================+
| Toggle On-Off | NA         | NA                    | S             | NA               |
+---------------+------------+-----------------------+---------------+------------------+

| 
| ===== Pins =====

Input
-----

+----------------------+---------+-------------------------------------------------------------------------------------+
| Name                 | Type    | Description                                                                         |
+======================+=========+=====================================================================================+
| Detection input      | Control | Control Signal input that is detected by the toggle on/off cell                     |
+----------------------+---------+-------------------------------------------------------------------------------------+
| Interface read input | Logic   | Connected to a software interface register - reads the last stored value at startup |
+----------------------+---------+-------------------------------------------------------------------------------------+

Output
------

+------------------------+---------+-------------------------------------------------------------------------------------------------+
| Name                   | Type    | Description                                                                                     |
+========================+=========+=================================================================================================+
| Toggle output          | Control | Toggling output. Toggles between zero and one each time a rising edge is detected on the input. |
+------------------------+---------+-------------------------------------------------------------------------------------------------+
| Interface write output | Logic   | Connected to a software interface register - writes the last output value                       |
+------------------------+---------+-------------------------------------------------------------------------------------------------+

| 
| ===== Configurable Parameters =====

+--------------------+---------------+--------+----------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range  | Function Description                                                                                     |
+====================+===============+========+==========================================================================================================+
| BufferVal          | Bit 0         | 0 - 30 | Controls which bit on the output signals will toggle on/off. All other bits remain at zero at all times. |
+--------------------+---------------+--------+----------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+----------------------------------------------------------------------------------------------------------+-------------------+
| Parameter Name | Description                                                                                              | ADAU145x/ADAU146x |
+================+==========================================================================================================+===================+
| BitVal         | Controls which bit on the output signals will toggle on/off. All other bits remain at zero at all times. | Integer32         |
+----------------+----------------------------------------------------------------------------------------------------------+-------------------+

| 
| ===== DSP Parameter Computation =====
| Not applicable

.. |toggle_on_off_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gpioconditioning/toggle_on_off_ssp.jpg
