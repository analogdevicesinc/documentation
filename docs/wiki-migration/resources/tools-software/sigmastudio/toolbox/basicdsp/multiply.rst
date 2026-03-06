Multiply
========

| 
| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| There are four kinds of multiplication supported.

-  Multiply(Real Signals)
-  Multiply(Complex Signals)
-  Multiply(Complex-Real Signals)
-  Multiply(Complex-Conjugate Complex Signals)

| 
| =====Multiply (Real Signals) ===== |multiplypic1.png| The Multiply block multiplies two signals together. This can be used for modulation or other design situations where a multiply operation is needed.

Right-click the block to add more pins by selecting **Add Algorithm > IC N > Multiplication**.

Care must be taken in using this block to avoid computational overflows, for example, putting in a value of 16 in 5.23 format, whose limit is 15.999999.

Multiply (Complex Signals)
--------------------------

| This module can be used to multiply two complex signals in block schematic.
| |image1|
| (x+iy) \* (u+iv) = (xu - yv) + i(xv + yu)
| Note:- The Context Menu "Input Source" option added to this module to select the algorithm for Complex FFT and Real FFT as shown below

Input Pins
~~~~~~~~~~

+------------------+------------------------------------+------------------------+
| Name             | Format [int/dec] - [control/audio] | Function Description   |
+==================+====================================+========================+
| Pin 0: Operand 1 | complex                            | Input complex signal 1 |
+------------------+------------------------------------+------------------------+
| Pin 1: Operand 2 | complex                            | Input Complex signal 2 |
+------------------+------------------------------------+------------------------+

| 
| ====Output Pins====

+----------------------+------------------------------------+-----------------------+
| Name                 | Format [int/dec] - [control/audio] | Function Description  |
+======================+====================================+=======================+
| Pin 0: Output Signal | Complex                            | Complex output signal |
+----------------------+------------------------------------+-----------------------+

| 
| ====Grow Algorithm==== input pins can be grown up to 8 channels.

| 

Multiply (Complex-Real Signals)
-------------------------------

| This module can be used to multiply one complex-one real signal in block schematic.
| |image2|
| (x+iy) \* r = (xr) + i (yr)
| ====Input Pins====

+----------------------+------------------------------------+----------------------+
| Name                 | Format [int/dec] - [control/audio] | Function Description |
+======================+====================================+======================+
| Pin 0: Complex Input | complex                            | Input complex signal |
+----------------------+------------------------------------+----------------------+
| Pin 1: Real Input    | Dec                                | Input Real Signal    |
+----------------------+------------------------------------+----------------------+

| 
| ====Output Pins====

+----------------------+------------------------------------+-----------------------+
| Name                 | Format [int/dec] - [control/audio] | Function Description  |
+======================+====================================+=======================+
| Pin 2: Output Signal | Complex                            | Complex output signal |
+----------------------+------------------------------------+-----------------------+

| 
| ====Grow Algorithm==== Grow Algorithm is not supported. Add Algorithm is supported.

Multiply(Complex-Conjugate Complex Signals)
-------------------------------------------

| This module can be used to multiply one complex-one conjugate complex signal in block schematic.
| |image3|
| (x+iy) \* conj(u+iv) = (xu + yv) -i (xv - yu)
| Note:- The Context Menu "Input Source" option added to this module to select the algorithm for Complex FFT and Real FFT as shown below

.. _input-pins-1:

Input Pins
~~~~~~~~~~

+----------------------+------------------------------------+------------------------+
| Name                 | Format [int/dec] - [control/audio] | Function Description   |
+======================+====================================+========================+
| Pin 0: Complex Input | complex                            | Input complex signal 1 |
+----------------------+------------------------------------+------------------------+
| Pin 1: Complex Input | Dec                                | Input Complex signal 2 |
+----------------------+------------------------------------+------------------------+

| 
| ====Output Pins====

+----------------------+------------------------------------+-----------------------+
| Name                 | Format [int/dec] - [control/audio] | Function Description  |
+======================+====================================+=======================+
| Pin 2: Output Signal | Complex                            | Complex output signal |
+----------------------+------------------------------------+-----------------------+

| 
| ====Grow Algorithm==== Grow Algorithm is not supported. Add Algorithm is supported.

| 
| ====Supported DSPs===== ADAU145x (Block Schematic only)
| ====Example Usage===== This can be used to multiply two signals' FFT results as shown below. |image4|

.. |multiplypic1.png| image:: https://wiki.analog.com/_media/multiplypic1.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/cmul.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/complexrealmult.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/compconjcompmult.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/cmul2.jpg
