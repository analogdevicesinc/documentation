Magnitude of Complex Number
===========================

| 
| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| Conjugate Magnitude takes the Complex Signal(x + j y) of input signal and compute the magnitude (squareroot(x^2 + y^2)) of input signal and pass to output. This is a block based module.

| 
| |image1|
| Note:- The Context Menu “Input Source” option added to this module to select the algorithm for Complex FFT and Real FFT as shown below
| |image2|
| ====Input Pins====

+-----------------------+------------------------------------+----------------------+
| Name                  | Format [int/dec] - [control/audio] | Function Description |
+=======================+====================================+======================+
| Pin 0: Complex Signal | Complex                            | Complex input signal |
+-----------------------+------------------------------------+----------------------+

| 
| ====Output Pins====

+--------------------+------------------------------------+---------------------------------------+
| Name               | Format [int/dec] - [control/audio] | Function Description                  |
+====================+====================================+=======================================+
| Pin 1: Real Signal | Real                               | Magnitude of the Complex Input Signal |
+--------------------+------------------------------------+---------------------------------------+

| 
| ====Grow Algorithm==== Grow algorithm not supported for the module.
| ====Add Algorithm==== Add algorithm supported for the module.
| ====Supported DSPs===== IDspSigma300(Block Schematic only)

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/magnitudeofcomplexnumber.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/cmplxmgtdcnxtmenu.png
