Cross-Mixer (2 inputs)
======================

:doc:`Click here to return to the Mixers/Splitters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/mixerssplitters>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/crossmixer2input_062.jpg
   :align: right

The Cross-Mixer (2 inputs) allows two input signals to be mixed, with variable gain, down to one output signal.

There are two control knobs for setting the gain, one knob for each input pin. To set the gain, click the knob with the left mouse button and drag while holding the button down. Each knob's range, value, and step size can be customized by right-clicking on the knob control.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/crossmixer2input_063.jpg
   :align: center

To add additional mixer outputs, you can perform Grow Algorithm on this block (right-click and select Grow Algorithm from the menu), increasing the number of output pins, as shown below. This example features growth by 4, resulting in five total outputs. (The maximum is +9.) This allows you to create different mixes from the same inputs.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/crossmixer2input_064.jpg
   :align: center

You can also add additional mixer algorithms to the block by right-clicking and selecting Add Algorithm from the menu. Adding an algorithm creates another set of input/output pins and control knobs. Each block algorithm is independent. See the Add Algorithm topic for more information.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/crossmixer2input_065.jpg
   :align: center

This second mixer control is entirely separate even though it appears on the same block. You can add additional algorithms; the input to output ratio will always be 2:1.

It is also possible to perform Grow and Add Algorithm on the same block. In this situation it is important to keep track of input and output pin relationships. Below is a design with a mixer block containing two algorithms, the first grown by 2, the second grown by 1. The colored boxes indicate the mixer configuration and the corresponding input/output pins.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/crossmixer2input_066.jpg
   :align: center
