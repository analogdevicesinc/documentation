:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

Adaptive MFxLMS Filter
======================

| 
| |mfxfilter.png|
| |mfxpopup1.png| |mfxpopup2.png|

Description
-----------

| This module implements the Modified Filtered-X LMS algorithm which is an adaptive FIR filter based on minimizing the least mean squared value of the error signal. The algorithm is applied to noise cancellation applications where it takes into account the fact that the point of cancellation is not at the anti-noise output speaker but at the position of the error microphone.
| The module provides a training mode which enables training and estimating the secondary paths between the output speakers and the error microphones as FIR filter coefficients. These coefficients are then used in the run-time mode of the module to take into account the paths and provide effective noise cancellation based on the reference inputs.
| ===== Targets Supported =====

+------------------------+------------+------------------+---------------+------------------+
| Name                   | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+========================+============+==================+===============+==================+
| Adaptive MFxLMS Filter | NA         | NA               | S             | NA               |
+------------------------+------------+------------------+---------------+------------------+

Pins
----

Input
~~~~~

========================= ======= ========================
Name                      Type    Description
========================= ======= ========================
Input<fc #ff0000>X</fc>   Audio   Reference noise signal X
ErrorIN<fc #ff0000>Y</fc> Control Error signal Y
========================= ======= ========================

Note:

-  <fc #ff0000>X</fc> - Input Channel Index

Output
~~~~~~

========================== ======= ========================
Name                       Type    Description
========================== ======= ========================
Output<fc #ff0000>Z</fc>   Audio   Anti-Noise Signal
ErrorOUT<fc #ff0000>Y</fc> Control Mean square error signal
========================== ======= ========================

Note:

-  <fc #ff0000>Y</fc> - Error Channel Index
-  <fc #ff0000>Z</fc> - Output Channel Index

| 
| ===== Configurable Parameters =====

Sec Path Training
^^^^^^^^^^^^^^^^^

+------------------------------+---------------+------------------------------+------------------------------------------------------------------------+
| GUI Parameter Name           | Default Value | Range                        | Function Description                                                   |
+==============================+===============+==============================+========================================================================+
| Current Output               | 0             | 0 to OutputChannel Count - 1 | Output selection for which secondary paths are to be estimated         |
+------------------------------+---------------+------------------------------+------------------------------------------------------------------------+
| Step Size                    | 0.9           | 0.000001- 0.999999           | Secondary path LMS filter step size                                    |
+------------------------------+---------------+------------------------------+------------------------------------------------------------------------+
| Start                        | 0             | 0 or 1                       | Starts or stops secondary path training                                |
+------------------------------+---------------+------------------------------+------------------------------------------------------------------------+
| Upload LMS                   | NA            | NA                           | Opens up SP coefficient form from where SP coefficients can be saved ​ |
+------------------------------+---------------+------------------------------+------------------------------------------------------------------------+
| Secondary Path Filter Length | 32            | 8 to 256                     | Secondary path LMS filter tap length                                   |
+------------------------------+---------------+------------------------------+------------------------------------------------------------------------+

| 
| ===RunTime ===

+-----------------------------+---------------+--------------------+--------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name          | Default Value | Range              | Function Description                                                                                         |
+=============================+===============+====================+==============================================================================================================+
| Filter Length               | 32            | 8 to 256           | MFXLMS Filter length                                                                                         |
+-----------------------------+---------------+--------------------+--------------------------------------------------------------------------------------------------------------+
| Step Size                   | 0.9           | 0.000001- 0.999999 | LMS step size                                                                                                |
+-----------------------------+---------------+--------------------+--------------------------------------------------------------------------------------------------------------+
| Secondary Path coefficients | NA            | NA                 | Secondary path LMS coefficient                                                                               |
+-----------------------------+---------------+--------------------+--------------------------------------------------------------------------------------------------------------+
| Initial LMS coefficients    | NA            | NA                 | Opens up LMS coefficient form from where the initial LMS coefficients can be loaded                          |
+-----------------------------+---------------+--------------------+--------------------------------------------------------------------------------------------------------------+
| Current LMS coefficients    | NA            | NA                 | Opens up LMS coefficient form from where the current converged LMS coefficients can be saved to a text file  |
+-----------------------------+---------------+--------------------+--------------------------------------------------------------------------------------------------------------+
| Pause                       | 0             | 0 or 1             | Pause or resume MFXLMS coefficient update                                                                    |
+-----------------------------+---------------+--------------------+--------------------------------------------------------------------------------------------------------------+
| Reset                       | 0             | 0 or 1             | Resets the MFXLMS Filter coefficients and states ​                                                           |
+-----------------------------+---------------+--------------------+--------------------------------------------------------------------------------------------------------------+

DSP Parameters
--------------

+----------------+--------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                      | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+==================================================+========================+===============+
| Start          | Starts or stops secondary path training          | NA                     | FixPoint8d24  |
+----------------+--------------------------------------------------+------------------------+---------------+
| Pause          | Pause or resume MFXLMS coefficient update        | NA                     | FixPoint8d24  |
+----------------+--------------------------------------------------+------------------------+---------------+
| Reset          | Resets the MFXLMS Filter coefficients and states | NA                     | FixPoint8d24  |
+----------------+--------------------------------------------------+------------------------+---------------+
| StepSizeLMS    | Run-time LMS filter step size                    | NA                     | FixPoint8d24  |
+----------------+--------------------------------------------------+------------------------+---------------+
| StepSizeSP     | Secondary path LMS filter step size              | NA                     | FixPoint8d24  |
+----------------+--------------------------------------------------+------------------------+---------------+
| CurrentOutput  | Output selection for secondary path training     | NA                     | Integer32     |
+----------------+--------------------------------------------------+------------------------+---------------+

| 

.. |mfxfilter.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/mfxfilter.png
.. |mfxpopup1.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/mfxpopup1.png
.. |mfxpopup2.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/mfxpopup2.png
