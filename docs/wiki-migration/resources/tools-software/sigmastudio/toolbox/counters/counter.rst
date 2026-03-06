Counter
=======

| :doc:`Click here to return to the Counters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/counters>`
| ----------------------------------------------------------------------------------------------------

|counterpic1.png| The Counter block can be used with a State Machine to process your input at a particular time interval, in ms. The counter starts from 0 (or any other user-defined value).\|

Controls (parameters)
---------------------

+---+---+---+
| Max   | This is the maximum value for the counter. The value can be changed by clicking in the text field and typing a new value, or by clicking the adjacent up/down arrows. If the counter reaches the maximum value, its output will stay at that value until it is reset. | |counterpic2.png| |
+---+---+---+
| Start | This switch starts or stops the counter. If the counter is stopped in mid-operation, its output value will freeze at its most recent value.                                                                                                                           | |counterpic3.png| |
+---+---+---+
| Init  | This is the initial value of the counter, which is the starting value for the counter when it is reset. Enter the start count value in the Init field, or use the adjacent up/down arrows.                                                                            | |counterpic4.png| |
+---+---+---+
| Reset | This button resets the counter back to its initial value, set in the Init field.                                                                                                                                                                                      | |counterpic5.png| |
+---+---+---+
| Step  | This controls rate at which the counter increments. The counter value will increase by the value in this field at the end of every audio sample. The value can be changed by entering the desired value in the text field or using the adjacent up/down arrows.       | |counterpic6.png| |
+---+---+---+

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/counters/2012.11.01_14.10.30.jpg
   :align: center

Counter example:
----------------

| This schematic shows how the Counter (in conjunction with a `tone <https://wiki.analog.com/resources/tools-software/sigmastudio/toolbox/sources/tonelookupsine>`__ cell) can be used with the State Machine. The :doc:`state machine </wiki-migration/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers/statemachine>` block passes signal (green pin to blue pin) only when the Counter's control value to the red pin is between the given limits.
| |counterpic7.png|

.. |counterpic1.png| image:: https://wiki.analog.com/_media/counterpic1.png
.. |counterpic2.png| image:: https://wiki.analog.com/_media/counterpic2.png
.. |counterpic3.png| image:: https://wiki.analog.com/_media/counterpic3.png
.. |counterpic4.png| image:: https://wiki.analog.com/_media/counterpic4.png
.. |counterpic5.png| image:: https://wiki.analog.com/_media/counterpic5.png
.. |counterpic6.png| image:: https://wiki.analog.com/_media/counterpic6.png
.. |counterpic7.png| image:: https://wiki.analog.com/_media/counterpic7.png
