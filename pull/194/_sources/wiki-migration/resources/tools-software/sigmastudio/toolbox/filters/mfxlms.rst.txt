Modified FXLMS(ADAU145x)
========================

| :doc:`Click here to return to the Filters section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| \|\| This module implements the Modified Filtered-X LMS algorithm which is an adaptive FIR filter based on minimizing the least mean squared value of the error signal. The algorithm is applied to noise cancellation applications where it takes into account the fact that the point of cancellation is not at the anti-noise output speaker but at the position of the error microphone. The module provides a training mode which enables training and estimating the secondary paths between the output speakers and the error microphones as FIR filter coefficients. These coefficients are then used in the run-time mode of the module to take into account the paths and provide effective noise cancellation based on the reference inputs.
| The module can be found at the below location in the tree tool box:
| |image1|
| |image2|
| |image3|
| The above figure shows the block diagram of the MFxLMS system where,

-  **P(z)** is the system to be modeled (noise source)
-  **S(z)** is the secondary path in the acoustic domain
-  **W'(z)** is the LMS filter
-  **S'(z)** is the modeled Secondary path
-  **x(n)** is the reference input
-  **d(n)** is the noise signal in the acoustic domain
-  **error** is the residual signal after destructive interference between the noise and anti- noise signal in the acoustic domain
-  **y(n)** is the output on filtering the reference input with the LMS coefficients
-  **yf(n)** is the output on filtering y(n) with the secondary path filter coefficients
-  **xf(n)** is the output on filtering x(n) with the secondary path filter coefficients
-  **y'(n)** is the output of filtering xf(n) with the LMS coefficients
-  **e(n)** is the total error feedback to the LMS system which is computed as e(n) = error+ yf(n)- y'(n)

| the coefficient update equation is given as:
| W(n)= W(n-1)+ step size \*(e(n-1)\* xf(n-1))

Input Pins
----------

+------------------+------------------------------------+-------------------------+
| Name             | Format [int/dec] - [control/audio] | Function Description    |
+==================+====================================+=========================+
| Pin 0: Reference | dec- audio                         | Reference noise signal. |
+------------------+------------------------------------+-------------------------+
| Pin 1: Error     | dec- audio                         | Error signal.           |
+------------------+------------------------------------+-------------------------+

| 
| ===== Output Pins =====

+--------------------------+------------------------------------+---------------------------+
| Name                     | Format [int/dec] - [control/audio] | Function Description      |
+==========================+====================================+===========================+
| Pin 0: Anti-Noise        | decimal - audio                    | Anti-Noise Signal         |
+--------------------------+------------------------------------+---------------------------+
| Pin 1: Mean Square Error | decimal - audio                    | Mean square error signal. |
+--------------------------+------------------------------------+---------------------------+

| 

Grow Algorithm
--------------

| The reference, error and anti-noise can be grown independently. Undo and Redo will not be supported for this module's growth functionality.
| |image4|
| ===== Configurations ===== The module features two modes

-  Training mode- In this mode secondary path estimation is done using an internally generated white noise source for each output selection.
-  Run-time mode- In this mode the adaptive filter converges to provide an anti noise output opposite in phase to the noise signal to be cancelled.

The modes can be selected by selecting the appropriate mode tab in the MFXLMS settings form.

| 
| |image5|
|

.. important::

   NOTE: Changing modes requires a re-download operation to be performed.


| 
| ===== GUI Controls =====
| ==== Training ====
| ^GUI Control Name^Default Value^Range^Function Description^

+------------------------------+-----+-----------------------+----------------------------------------------------------------------+
| Current Output               | 0   | 0-Number of Outputs-1 | Output selection for which secondary paths are to be estimated       |
+------------------------------+-----+-----------------------+----------------------------------------------------------------------+
| Step Size                    | 0.9 | 0.000001- 0.999999    | LMS step size                                                        |
+------------------------------+-----+-----------------------+----------------------------------------------------------------------+
| Start                        | 0   | 0/1                   | Starts or stops secondary path training                              |
+------------------------------+-----+-----------------------+----------------------------------------------------------------------+
| Upload                       | -   | -                     | Opens up SP coefficient form from where SP coefficients can be saved |
+------------------------------+-----+-----------------------+----------------------------------------------------------------------+
| Secondary Path Filter Length | 32  | 8-256                 | Secondary path LMS filter tap length                                 |
+------------------------------+-----+-----------------------+----------------------------------------------------------------------+

| 

Runtime
~~~~~~~

|

| ^GUI Control Name^Default Value^Range^Function Description^

+--------------------------+-----+--------------------+-------------------------------------------------------------------------------------------------------------+
| Filter Length            | 32  | 8-256              | MFXLMS Filter length                                                                                        |
+--------------------------+-----+--------------------+-------------------------------------------------------------------------------------------------------------+
| Step Size                | 0.9 | 0.000001- 0.999999 | LMS step size                                                                                               |
+--------------------------+-----+--------------------+-------------------------------------------------------------------------------------------------------------+
| Pause                    | 0   | 0/1                | Pause or resume MFXLMS coefficient update                                                                   |
+--------------------------+-----+--------------------+-------------------------------------------------------------------------------------------------------------+
| Reset                    | 0   | 0/1                | Resets the MFXLMS Filter coefficients and states                                                            |
+--------------------------+-----+--------------------+-------------------------------------------------------------------------------------------------------------+
| Initial LMS Coefficients | -   | -                  | Opens up LMS coefficient form from where the initial LMS coefficients can be loaded                         |
+--------------------------+-----+--------------------+-------------------------------------------------------------------------------------------------------------+
| Current LMS Coefficients | -   | -                  | Opens up LMS coefficient form from where the current converged LMS coefficients can be saved to a text file |
+--------------------------+-----+--------------------+-------------------------------------------------------------------------------------------------------------+

| 

DSP Parameter Information
-------------------------

|

| ==== Training ====
| ^GUI Control Name^Compiler Name^Function Description^

+---------------+--------------------------------------------------------------------------------------------------+----------------------------------------------+
| coeffsSP      | <fc #008000>MFxLMSS300Alg</fc><fc #ff0000>1</fc><fc #000080>coeffsSP</fc><fc #800000>1</fc>      | Secondary path LMS filter coefficient set    |
+---------------+--------------------------------------------------------------------------------------------------+----------------------------------------------+
| StepSizeSP    | <fc #008000>MFxLMSS300Alg</fc><fc #ff0000>1</fc><fc #000080>StepSizeSP</fc><fc #800000>1</fc>    | Secondary path LMS filter step size          |
+---------------+--------------------------------------------------------------------------------------------------+----------------------------------------------+
| Start         | <fc #008000>MFxLMSS300Alg</fc><fc #ff0000>1</fc><fc #000080>Start</fc><fc #800000>1</fc>         | Start Secondary path LMS training            |
+---------------+--------------------------------------------------------------------------------------------------+----------------------------------------------+
| currentOutput | <fc #008000>MFxLMSS300Alg</fc><fc #ff0000>1</fc><fc #000080>CurrentOutput</fc><fc #800000>1</fc> | Output selection for secondary path training |
+---------------+--------------------------------------------------------------------------------------------------+----------------------------------------------+

| 
| ==== Runtime ====
| ^GUI Control Name^Compiler Name^Function Description^

+-------------+------------------------------------------------------------------------------------------------+-------------------------------------------+
| coeffs      | <fc #008000>MFxLMSS300Alg</fc><fc #ff0000>1</fc><fc #000080>coeffs</fc><fc #800000>1</fc>      | Run-time LMS filter coefficient set       |
+-------------+------------------------------------------------------------------------------------------------+-------------------------------------------+
| coeffsSP    | <fc #008000>MFxLMSS300Alg</fc><fc #ff0000>1</fc><fc #000080>coeffsSP</fc><fc #800000>1</fc>    | Secondary path LMS filter coefficient set |
+-------------+------------------------------------------------------------------------------------------------+-------------------------------------------+
| StepSizeLMS | <fc #008000>MFxLMSS300Alg</fc><fc #ff0000>1</fc><fc #000080>StepSizeLMS</fc><fc #800000>1</fc> | Run-time LMS filter step size             |
+-------------+------------------------------------------------------------------------------------------------+-------------------------------------------+
| Pause       | <fc #008000>MFxLMSS300Alg</fc><fc #ff0000>1</fc><fc #000080>Pause</fc><fc #800000>1</fc>       | Pause/resume LMS training                 |
+-------------+------------------------------------------------------------------------------------------------+-------------------------------------------+
| Reset       | <fc #008000>MFxLMSS300Alg</fc><fc #ff0000>1</fc><fc #000080>Reset</fc><fc #800000>1</fc>       | Reset LMS Filter                          |
+-------------+------------------------------------------------------------------------------------------------+-------------------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name
-  <fc #800000> Brown</fc> - Stage number

Example
-------

Active Noise Cancellation using MFXLMS filter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| This section demonstrates active noise cancellation using the MFXLMS filter module. The module is run at a lower sample rate of 2000Hz by means of a down-sampling module, the output is later up-sampled to the input sample rate by means of a up sampling module.The down and up sampling module chain is constructed in hierarchy boards as show below. the Anti- aliasing filters are included in the signal chain.
| |image6|
| |image7|
| The below schematic shows the module in the training mode. The inputs are muted. To obtain the secondary path coefficients, the training tab is opened in the form, the tap length, step size and the output selection is set and the module is downloaded in the training mode. To start the training the start button is clicked. The training is stopped by clicking on the stop button. Then click on Upload button, the coefficients will be displayed in a window. This can be saved in a text file.
| |image8|
| The below schematic shows the module in the run time mode. The Run-time LMS tap-length, Step size are set. The Secondary path coefficients can be set by using the file exported in the training mode. The input reference approximates the error signal to be cancelled. The error microphone output is fed to the error pin( this error input is the residual from the destructive interference between the noise and the anti-noise signal in the acoustic domain). The Anti noise pin is connected to the cancellation speaker to cancel the noise in the acoustic domain. The schematic is link compile downloaded. The mean square error pin is monitored to observe the drop in the error levels indicating noise cancellation.
| On convergence, the LMS coefficients may be read and saved to a text file by clicking the current LMS coefficients button. These coefficients can be loaded as the initial LMS coefficients using the initial LMS coefficients for faster convergence.
| |image9|
| ===== Supported ICs =====

-  ADAU145x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mfxlms-ttbox.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mfxlms-cell.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mfxlms-block_diagram.png
   :width: 700px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mfxlms-growth.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mxlmswindows.jpg
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mfxlms-down_sampler.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mfxlms-upsampler.png
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mfxlms-training.png
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mfxlms-runtime.png
