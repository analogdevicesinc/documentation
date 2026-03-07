Data controlled asymmetric soft clipper
=======================================

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| The Data Controlled Clip is a hard-clipper that clips the input data signal using the TanH function according to threshold values set by data input pins. | |image2| |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+----------+

Input Pins
----------

+------------------+------------------------------------+-----------------------------------------------------+
| Name             | Format [int/dec] - [control/audio] | Function Description                                |
+==================+====================================+=====================================================+
| Pin 0: Clip Up   | decimal - control                  | Threshold clip level for the top of the waveform    |
+------------------+------------------------------------+-----------------------------------------------------+
| Pin 1: Clip Down | decimal - control                  | Threshold clip level for the bottom of the waveform |
+------------------+------------------------------------+-----------------------------------------------------+
| Pin 2: Input     | decimal - audio                    | Input audio to be soft clipped                      |
+------------------+------------------------------------+-----------------------------------------------------+

Output Pins
-----------

+---------------+------------------------------------+---------------------------+
| Name          | Format [int/dec] - [control/audio] | Function Description      |
+===============+====================================+===========================+
| Pin 0: Output | decimal - audio                    | soft clipped output audio |
+---------------+------------------------------------+---------------------------+

Algorithm Description
---------------------

The data controlled clipper clips the input signal according to the TanH function once it crosses an upper or lower threshold boundary. The output signal will be retained within values defined by the transfer functiona and the set threshold values so long as the input signal is above the upper threshold limit- tau1, or below the lower threshold limit- tau2. For values within the threshold boundaries, the output signal will equal the input signal.

| 
| :math:`Output = Input, if |Input|<tau1 for Input>0, |Input|<tau2 for Input<0`
| :math:`\displaystyle Output = tau1 + (1 - tau1) \times tanh(\frac{abs(Input) - tau1}{1 - tau1}), if|Input|>=tau1 and Input>0`
| :math:`\displaystyle Output = -tau2 -(1 - tau2) \times tanh(\frac{abs(Input) - tau2}{1 - tau2}), if|Input|>=tau2 and Input<0`
| The graph below shows an input sine tone and the resulting clipped output with threshold values at: Clip Up: 0.8 Clip Down: 0.2
| |image3|

Example
-------

The following image shows the Data Controlled Clip and also the direct signal coming from the Inputs.Two DC Input blocks are used to define the threshold values for the Data Controlled Clip. The output from the clip block will be the same as that of the advanced clipper, but have different ways to control the thresholds (coefficients vs. data inputs).

| 
| |image4|

Algorithm Details
-----------------

+----------------------------+-----------------------------------------------------------------------------------------------------------+
| Toolbox Path               | Non Linear Processors - Clippers - Soft Clip - Asymmetric Data controlled-Data Controlled Asymmetric Clip |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| Cores Supported            | ADAU145x                                                                                                  |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| "Grow Algorithm" Supported | yes - see Algorithm Growth Information                                                                    |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                                                                        |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                                                                        |
+----------------------------+-----------------------------------------------------------------------------------------------------------+

Algorithm Growth Information
----------------------------

+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| Description | When the Data Controlled Clip is grown, an extra pair of Input/Output pins is added to the control. The Clip up and Clip down pins do not grow as the same values will apply to all audio pairs grown on the control. | |image6| |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocessors/asymmdatactrlclip.png
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocessors/asymmdatactrlclip.png
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocessors/datagraph.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocessors/data_schema.png
   :width: 300px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/datacontrolledclip016.jpg
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/datacontrolledclip016.jpg
