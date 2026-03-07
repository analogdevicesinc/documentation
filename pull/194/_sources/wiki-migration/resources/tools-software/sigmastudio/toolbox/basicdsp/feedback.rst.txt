Feedback
========

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| The feedback algorithm generates a delay in the signal path and reroutes signal to an input occurring earlier in the path. Note that this block must be used if feedback is required in your design. **The standard delay block cannot be used to create feedback systems.**

There are two versions of ' Feedback' algorithm.

-  Feedback(Sample)
-  Feedback(Block)

| 
| =====Feedback(Sample) ===== Generates one sample delay in the signal path and reroutes the signal to an input occurring earlier in the path. |image1|
| =====Feedback(Block) ===== Generates delay equal to one blocksize in the signal path and reroutes the signal to an input occurring earlier in the path. |image2|

Input Pins(Sample)
------------------

+---------------------+------------------------------------+----------------------+
| Name                | Format [int/dec] - [control/audio] | Function Description |
+=====================+====================================+======================+
| Pin 0: Sample Input | decimal- audio                     | Sample Input signal  |
+---------------------+------------------------------------+----------------------+

| 
| ====Output Pins(Sample)====

+------------------------------+------------------------------------+----------------------+
| Name                         | Format [int/dec] - [control/audio] | Function Description |
+==============================+====================================+======================+
| Pin 0: Sample Delayed Output | decimal- audio                     | Sample Output signal |
+------------------------------+------------------------------------+----------------------+

Input Pins(Block)
-----------------

+--------------------+------------------------------------+----------------------+
| Name               | Format [int/dec] - [control/audio] | Function Description |
+====================+====================================+======================+
| Pin 0: Block Input | decimal-audio                      | Block Input Signal   |
+--------------------+------------------------------------+----------------------+

| 
| ====Output Pins(Block)====

+-----------------------------+------------------------------------+----------------------+
| Name                        | Format [int/dec] - [control/audio] | Function Description |
+=============================+====================================+======================+
| Pin 0: Block Delayed Output | decimal- audio                     | Block Output signal  |
+-----------------------------+------------------------------------+----------------------+

| 
| ===== GUI Controls ===== None

Grow and Add Algorithm
----------------------

Grow and Add algorithm are not supported for this module.

DSP Parameter Information
~~~~~~~~~~~~~~~~~~~~~~~~~

None

Supported DSPs
--------------

| ADAU145x
| ====Example Usage===== The Signal Chain shown below feeds back the output of the adder block to the input of the subtractor after a block delay. |image3|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/feedback_sample.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/feedback_block.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/feedback_example.png
