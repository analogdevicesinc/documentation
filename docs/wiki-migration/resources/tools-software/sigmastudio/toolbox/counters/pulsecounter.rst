Pulse Counter
=============

| :doc:`Click here to return to the Counters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/counters>`
| ------------------------------------------------------------------------------------------------------

+---+---+
| The Pulse Counter block, counts the number of non-zero inputs it receives. There is a start/stop pin to initiate and pause the count, and also a reset pin to set the count back to zero. Any non-zero input on the pulse input pin, is considered a pulse and will be counted when the count is enabled. | |pulsecounterpic1.png| |
+---+---+

Input Pins
----------

+--------------------+------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Name               | Format [int/dec] - [control/audio] | Function Description                                                                                                       |
+====================+====================================+============================================================================================================================+
| Pin 0: Start/Stop  | int - control                      | When this pin is high, the algorithm is counting the Pulse input. When it is low, the algorithm holds the last count value |
+--------------------+------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Pin 1: Reset       | int - control                      | When this pin is high, it clears the count value back to zero.                                                             |
+--------------------+------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Pin 2: Pulse Input | int - control                      | Input signal to monitor and count pulses                                                                                   |
+--------------------+------------------------------------+----------------------------------------------------------------------------------------------------------------------------+

Output Pins
-----------

+---------------------+------------------------------------+-----------------------------------------+
| Name                | Format [int/dec] - [control/audio] | Function Description                    |
+=====================+====================================+=========================================+
| Pin 0: Count Output | int - control                      | Count Value indicating number of pulses |
+---------------------+------------------------------------+-----------------------------------------+

Algorithm Description
---------------------

The purpose of the Pulse counter, is to count the number of pulses during a specified amount of time. The time is dictated by the signal on the start/stop pin. When the start/stop pin is high, the algorithm is counting pulses, otherwise the last count value is output. The reset pin clears the count value and counting can resume from 0 whenever the start pin is high.

| The graph below shows the interaction between the start/stop and reset pins when a pulse train signal is present on the Pulse Input pin. The reset signal is in red. The start/stop signal is in blue, and the counter output is the second graph in yellow.
| |pulsecounterpic2.png|

Example
-------

| The Pulse Counter is very useful to use with the Value Cross Detection algorithm. For an application in which you need to monitor the number of value-crossings (zero-cross counter) during a specified time the two blocks together can help achieve this. The following image uses a :doc:`sine tone </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources/sinetone>` input, :doc:`on/off switches </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources/onoffswitch>`, Pulse Counter, :doc:`Readback </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp/dspreadback>` cell, and :doc:`GPIO output </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/generalpurposeoutput>`.
| |pulsecounterpic3.png|

Algorithm Details
-----------------

========================== ===================================
Toolbox Path               Counters - Counters - Pulse Counter
Cores Supported            AD1940
                           ADAU170x
                           ADAU144x
                           ADAU176x
                           ADAU178x
"Grow Algorithm" Supported no
"Add Algorithm" Supported  no
Subroutine/Loop Based      no
Program RAM                12
Data RAM                   3
Parameter RAM              0
========================== ===================================

.. |pulsecounterpic1.png| image:: https://wiki.analog.com/_media/pulsecounterpic1.png
.. |pulsecounterpic2.png| image:: https://wiki.analog.com/_media/pulsecounterpic2.png
.. |pulsecounterpic3.png| image:: https://wiki.analog.com/_media/pulsecounterpic3.png
