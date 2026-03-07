Adjustable Volume Control
=========================

:doc:`Click here to return to the Volume Controls section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/volumecontrols>`

+-------------------------------------------------------------------------------------------------------+-------------------------------+
| This block lets you control which slew curve, and which time constant for the slew algorithm, to use. | |adjustablevolumecontrol.jpg| |
+-------------------------------------------------------------------------------------------------------+-------------------------------+

Choose slew type using the top drop-down control, Linear, Const[ant] dB, and RC-type:

-  Linear: Slews to target using a fixed step size. The ramp ranges from 6.75 to 213.4 ms.
-  Constant dB: Slews to target using the current value to calculate the step size. The resulting curve has a constant rise and decay when measured in dB. The ramp ranges from 6.1 ms to 1.27 s.
-  RC-type: Slews to target using the difference between the target and current values to calculate the step size. This produces a simple RC-type curve for both rising and falling. The ramp ranges from 6.1 ms to 1.27 s.

With the bottom drop-down control, choose a time-constant value between 0 (fastest volume change) and -15 (slowest volume change). The default block comes with the Gain slew algorithm; right-click the block border or title, per usual, to add input/output pins. The slider controls the input(s) / output(s) the same, and the time constant applies to all inputs. The example at above right shows the default block with one algorithm added.

.. |adjustablevolumecontrol.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/adjustablevolumecontrol.jpg
