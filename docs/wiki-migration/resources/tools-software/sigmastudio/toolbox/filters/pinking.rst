Pinking
=======

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| |pinkpic1.png| The classic use of this type of filter is to convert white noise, which is equal energy per hertz, to pink noise, which is equal energy per proportional or constant-percentage (e.g., logarithmic) band.

Such energy displays as flat on any log scale graph when bundled (integrated) appropriately.

The Pinking cell takes any input signal and outputs a signal with a 3dB drop per octave in linear terms.

Navigate to the :doc:`Level Detectors Example </wiki-migration/resources/tools-software/sigmastudio/tutorials/leveldetectorsexamples>` to see the filter used in a schematic.

After you have established your default algorithm, this cell can have algorithms added to it. If you're using more than one DSP board, you will need to add the initial algorithm for the desired board. In either case, right-click the cell and select **Add Algorithm > IC N > Pink Noise Filter** to add another set of input/output pins.

Algorithm Information
---------------------

The Pinking Filter takes any broadband input and outputs a signal with a 3dB drop per octave. The classic use of this filter is to convert white noise (equal energy per hertz) to pink noise (equal energy per constant percentage, e.g., log bundling, as with an octave or subdivision).

To the human ear, which has an approximately logarithmic frequency response, white noise is distinctly trebly, while pink noise sounds broad and smooth, more like a waterfall.

The graph below (generated using simulation stimulus and probe) shows the two responses of white (green line) and pink (red line) noise. But realize that while these graphs are displayed on the familiar audio log scale, the data have not been subjected to, that is, not integrated in, constant-percentage bundling, but remain in constant-frequency depiction. This is in contrast to the RTA-style graphs in example 8.1, Level Detectors / Lookup Tables, where both the data and the graph scale are logarithmic.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/pinkfilter1.png
   :align: center
   :width: 600px

.. |pinkpic1.png| image:: https://wiki.analog.com/_media/pinkpic1.png
