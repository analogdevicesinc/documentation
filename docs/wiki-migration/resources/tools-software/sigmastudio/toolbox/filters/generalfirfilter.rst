General FIR Filter
==================

| :doc:`Click here to return to the filters section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| \|\| The General FIR filter block lets you design LowPass, HighPass, BandPass or BandStop FIR filters using windowing technique. Following windows are supported in filter design:
| \* Hanning

-  Rectangular
-  Hamming
-  Blackman

| 
| |image1|

Input Pins
----------

+--------------+------------------------------------+--------------------------------+
| Name         | Format [int/dec] - [control/audio] | Function Description           |
+==============+====================================+================================+
| Pin 0: Input | decimal - audio                    | Input signal to the FIR filter |
+--------------+------------------------------------+--------------------------------+

| 

Output Pins
-----------

============= ================================== ====================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== ====================
Pin 0: Output decimal - audio                    FIR filtered output
============= ================================== ====================

|

GUI Controls
------------

+------------------+---------------+------------+-------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range      | Function Description                                                                                  |
+==================+===============+============+=======================================================================================================+
| Enable/Bypass    | Enabled       | True/False | Enables or disables the filter. On bypass, the input signal is passed through without any processing. |
+------------------+---------------+------------+-------------------------------------------------------------------------------------------------------+
| Frequency        | 1000Hz        | 0-96Khz    | Cutoff frequency of the filter                                                                        |
+------------------+---------------+------------+-------------------------------------------------------------------------------------------------------+

| 
| Click on the image |image2| to configure the filter parameters.
| ^GUI Control Name^Default Value^Range^Function Description^

+--------------+--------+----------+--------------------------------------------------------------------------------------------------+
| Frequency    | 1000Hz | 0-96Khz  | Cutoff frequency of the filter. (Lower cutoff frequency in the case of Bandpass/Bandstop filters |
+--------------+--------+----------+--------------------------------------------------------------------------------------------------+
| Select Type  | 0      | 0-3      | Selects filter type(LowPass/HighPass/BandPass/BandStop)                                          |
+--------------+--------+----------+--------------------------------------------------------------------------------------------------+
| Window Type  | 0      | 0-3      | Selects the Window(Hanning/Rectangular/Hamming/Blackman)                                         |
+--------------+--------+----------+--------------------------------------------------------------------------------------------------+
| Gain         | 0db    | -15-15db | Sets the gain of the filter                                                                      |
+--------------+--------+----------+--------------------------------------------------------------------------------------------------+
| BW           | 1.41   | 0-11     | BW in octaves(only for BandPass and Bandstop filters)                                            |
+--------------+--------+----------+--------------------------------------------------------------------------------------------------+
| Filter Order | 10     | 2-10000  | Sets the order of the filter. Filter length = Order + 1                                          |
+--------------+--------+----------+--------------------------------------------------------------------------------------------------+

| 

Grow Algorithm
--------------

When the General FIR filter algorithm is grown, an extra pair of input/output pins is added to the control. The filtering on each of the grown Input pins is affected by the parameters chosen in the GUI in the same manner.

+----------+
| |nolink| |
+----------+

Configurations
--------------

| General FIR filter block designs a LowPass , HighPass, BandPass or BandStop filter using Windowing technique. Order, Cutoff frequency , Window Type and Gain are configured in the GUI for LowPass and HighPass filter design. Bandwidth has to be additionally configured for BandPass and BandStop filter design.
| |image3| |image4|
| The coefficients of the filter are calculated and downloaded to the DSP based on the design chosen by the user in the GUI. FIR coefficient calculation steps are shown below.

| Ideal filter response h(n) is calculated based on the filter configuration as per the table below
| |image5|
| **Note**: **N** -Filter Order , **w\ c** - Cutoff frequency, **w\ l** - Lower cutoff frequency, **w\ h** - Higher cutoff frequency, **w\ h**\ =\ **w\ l** \* **2\ BW**
| Coefficients of the window, w(n) are chosen based on the type of the window selected in the GUI.
| |image6|
| Filter coefficients are calculated as h(n) = h(n) \* w(n) over the filter length (Order + 1).
| In the case of HighPass and BandStop filter, filter order is increased by 1 when odd filter Order is entered in the GUI. Filter order must be even because odd-order symmetric FIR filters has zero gain at the Nyquist frequency.

DSP Parameter Information
-------------------------

+--------------------------------------------------------------------------------------+-------------------------+-------------------------------------------------------------+
| GUI Control Name                                                                     | Compiler Name           | Function Description                                        |
+======================================================================================+=========================+=============================================================+
| NA (Filter coefficients are calculated based on the filter configuration set in GUI) | FIRAlgSigma3001fircoeff | Calculated Filter coefficients based on the designed filter |
+--------------------------------------------------------------------------------------+-------------------------+-------------------------------------------------------------+

Supported ICs
-------------

-  ADAU145x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/genfirfilter1.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/filterparam.png
.. |nolink| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/genfiltergrowth.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/filtsettingslp.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/filtsettingbp.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/coefftable.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/windowtable.png
