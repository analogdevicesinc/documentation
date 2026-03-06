Crossfade (Data-Controlled)
===========================

:doc:`Click here to return to the Multiplexers/Demultiplexers page </wiki-migration/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers/crossfadedatacontrolled042.jpg
   :align: right

This block creates a smooth transition between two input signals: the volume of one signal is decreased while the other input signal level increases, creating a gradual switch (cross-fade) between the inputs.

The output signal is selected by setting a value on the input control pin (top orange pin) to the desired input's index, between 0.0 and 1.0. The control signal should be a 28.0 format integer value, typically from a DC input block or RMS Table. 0.0 selects the lower input pin2, 1.0 selects the upper input pin1, and 0.5 mixes 0.5 times pin1 with 0.5 times pin2, etc.

When the control input value changes, a cross fade is initiated between the current output and the newly selected input signal. The cross-fade transition rate (slew rate) can be adjusted using the numerical control on the block, (the maximum SW Slew Rate value is 23, which is a very slow fade).

This block's algorithm can be grown or added:

-  Select Grow Algorithm from the right-click menu to create an additional output and input pair (sharing the signal select control pin and SW slew ram parameter).

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers/crossfadedatacontrolled043.jpg
   :align: center

-  Select Add Algorithm from the right-click menu to create an additional algorithm with its own independent input select control pin.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers/crossfadedatacontrolled044.jpg
   :align: center

See the Multiplexer/Demultiplexer Example of the Crossfade (Data-Controlled) block.
