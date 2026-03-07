Level Detectors Examples
========================

:doc:`Click here to return to the Tutorials section. </wiki-migration/resources/tools-software/sigmastudio/tutorials>`

Example 1
---------

| Two Seven-Band Level Detectors show the difference between white and pink noise. They were created using White Noise Source and Pinking Filter blocks. For the difference between these two noise sources, refer to the Pink Filter page.
| There are two outputs to complete the signal flow. Notice in the level detector displays athat the pink noise levels tend to be constant while the white noise level fluctuate.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/leveldetectorsexamples1.jpg
   :alt: leveldetectorsexamples1.jpg

Example 2
---------

This example design shows the State-Variable Filter (Q Input), RMS Table, Mono Nx1 Switch, T Connection, and Input/Output blocks. The Q of the state-variable filter is determined by the RMS table and the Mono Nx1 switch selects the output response: lowpass, highpass, or bandpass.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/leveldetectorsexamples2.jpg
   :alt: leveldetectorsexamples2.jpg

The RMS Table Editor contains the interpolated values, as the input level increases the filter Q increases:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/leveldetectorsexamples3.jpg
   :alt: leveldetectorsexamples3.jpg
