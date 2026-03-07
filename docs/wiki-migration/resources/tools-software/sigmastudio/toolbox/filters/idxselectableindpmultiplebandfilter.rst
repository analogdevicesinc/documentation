IdxSelectable Indp. Multiple Band Filter
========================================

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| The IdxSelectable Indp. Multiple Band filter has two variants

-  IdxSelectable Indp. Multiple Band Filter (No Slew)
-  IdxSelectable Indp. Multiple Band Filter (Slew)

| 
| =====IdxSelectable Indp. Multiple Band Filter (No Slew)=====

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| The IdxSelectable Indp. Multiple Band filter allows for a data controlled index input to select a bank of filters for processing. The number of rows of possible filters is determined by the "growth" of the algorithm. The number of biquads per row is determined by the number in the numeric text box for each filter "row." Clicking the red button opens the filter editor. This version of the algorithm is a fixed 2-channel stereo filter. | |idxpic1.png| |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+

| 
| ===Input Pins===

+----------------------+-----------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Name                 | Format                      | Function Description                                                                                                    |
|                      | [int/dec] - [control/audio] |                                                                                                                         |
+----------------------+-----------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Pin 0: Index Input   | int - control               | The Index input selects the row of filters to use. The value of this index must be between 0 and the number of rows - 1 |
+----------------------+-----------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Pin 1: Audio Input 1 | decimal - audio             | Left Channel audio                                                                                                      |
+----------------------+-----------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Pin 1: Audio Input 2 | decimal - audio             | Right Channel audio                                                                                                     |
+----------------------+-----------------------------+-------------------------------------------------------------------------------------------------------------------------+

| 
| ===Output Pins===

+-----------------------+-----------------------------+-------------------------------+
| Name                  | Format                      | Function Description          |
|                       | [int/dec] - [control/audio] |                               |
+-----------------------+-----------------------------+-------------------------------+
| Pin 0: Audio Output 1 | decimal - audio             | Filtered output left channel  |
+-----------------------+-----------------------------+-------------------------------+
| Pin 0: Audio Output 2 | decimal - audio             | Filtered output right channel |
+-----------------------+-----------------------------+-------------------------------+

| 
| ===GUI Controls - Top Level Control===

+----------------------+---------------+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name     | Default Value | Range                  | Function Description                                                                                                                         |
+----------------------+---------------+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| Radio Button Select  | Unselected    | [Unselected, Selected] | Selects the row of filters to be displayed in the Probe/Stimulus Transfer Function window. Note: this has no DSP function, only for display. |
+----------------------+---------------+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| Number of Biquads    | 1             | [1, 30]                | Sets the number of biquads in the filter row. This number can be different for each row.                                                     |
+----------------------+---------------+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| Filter Editor Button | n/a           | n/a                    | Clicking this button opens a new window for editing the filter values.                                                                       |
+----------------------+---------------+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===GUI Controls - Filter Editor===

+--------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------+
| GUI Control Name   | Default Value | Range          | Function Description                                                                                       |
+--------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------+
| Filter Type (Icon) | Parametric    | [Parametric    | Clicking on the filter icon in the editor window scrolls through the possible filter structures available. |
|                    | Low Shelf     |                |                                                                                                            |
|                    | Hi Shelf      |                |                                                                                                            |
|                    | Low Pass      |                |                                                                                                            |
|                    | Hi Pass]      |                |                                                                                                            |
+--------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------+
| Boost              | 0             | [-20, 20] dB   | Cut or Boost of the Center Frequency                                                                       |
+--------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------+
| Frequency          | 1000          | [20, 20000] Hz | Sets the Center or Cutoff Frequency                                                                        |
+--------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------+
| Q/Slope            | 1.41          | [0.1, 15]      | Sets the Q or Slope                                                                                        |
+--------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------+
| Gain               | 0             | [-15, 15] dB   | Overall gain of the filter                                                                                 |
+--------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------+

| 
| ===DSP Parameter Information===

+--------------------+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name   | Compiler Name          | Function Description                                                                                                                                                                                                                                 |
+--------------------+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Filter Type (Icon) | IdxSelIndpBandAlg100b2 | Changing any one of the 5 filter GUI controls, will write 5 DSP parameters to the DSP. These are the filter coefficients (b2, b1, b0, -a2, -a1) and they are determined by the formulas found in the algorithm section for General 2nd Order Filters |
| Boost              | IdxSelIndpBandAlg100b1 |                                                                                                                                                                                                                                                      |
| Frequency          | IdxSelIndpBandAlg100b0 |                                                                                                                                                                                                                                                      |
| Q/Slope            | IdxSelIndpBandAlg100a2 |                                                                                                                                                                                                                                                      |
| Gain               | IdxSelIndpBandAlg100a1 |                                                                                                                                                                                                                                                      |
+--------------------+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===Algorithm Description=== The filter algorithm used is a 2nd Order General Filter (Double Precision) based on a Direct Form I structure. Growth of the algorithm allows for multiple rows or EQ banks. The index input pin to the algorithm allows a data control signal to choose which row of filters is used for processing the input signal. The data index must be within the range of 0 to number of filter rows - 1. Independent control is given to each filter row, being able to have different number of biquads per row, and different filter settings. The number of biquads per row is determined by the numeric text box. The image below shows the Top Level Control and corresponding Filter Editor Window:
| |idxpic2.png|
| The IdxSelectable Indp. Multiple Band Filter makes use of the GEN3 SigamDSP core features in order to save program and parameter RAM. The filter structure code is part of a subroutine and is called multiple times for the number of biquads in the selected row. A loop structure also repeats the subroutine code for multiple biquads. This leads to a great savings in program RAM compared to the traditional filters in the library.
| ===Example=== The following image shows a comparison of the IdxSelectable Indp Multiple Band Filter, with traditional General 2nd order filters set-up in a similar manner. The main difference between the two methods, is that for the IdxSelectable filter, a data input index selects which filters are used for processing. In the traditional case, a coefficient parameter from the mux switch, selects the filters to be used. Also, because of the loop and subroutine structures within the algorithm code, the program and parameter savings are much greater for the IdxSelectable filter, than the combination of the traditional filters.
| |idxpic3.png|
| The DC-Input entry is in integer format (28.0), in order to select the row of filters to be used. Since the value is "2" the last set of filters (with 2 biquads) will be used for the processing. The radio-button selection is on row "0" so that when the Probe/Stimulus window is used, the transfer function for the first row of filters with 3 biquads will be displayed. A mux switch allows for comparison between the filter processing between the General 2nd Order and the Index Selectable Band Filter.
| ===Algorithm Details===

+----------------------------+------------------------------------------------------------------------------------------------------+
| Toolbox Path               | Filters - Second Order - Lookup - Double Precision - 2 Ch - IdxSelectable Indp. Multiple Band Filter |
+----------------------------+------------------------------------------------------------------------------------------------------+
| Cores Supported            | ADAU144x                                                                                             |
|                            | ADAU176x                                                                                             |
|                            | ADAU178x                                                                                             |
+----------------------------+------------------------------------------------------------------------------------------------------+
| "Grow Algorithm" Supported | yes - See Algorithm Growth for more information                                                      |
+----------------------------+------------------------------------------------------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                                                                   |
+----------------------------+------------------------------------------------------------------------------------------------------+
| Subroutine/Loop Based      | yes                                                                                                  |
+----------------------------+------------------------------------------------------------------------------------------------------+
| Program RAM                | 22\* (+16 subroutine code)  - See Subroutine/Loop Information                                        |
+----------------------------+------------------------------------------------------------------------------------------------------+
| Data RAM                   | 20\* - Based on 1 Row 1 Biquad                                                                       |
+----------------------------+------------------------------------------------------------------------------------------------------+
| Parameter RAM              | 11\* - Based on 1 Row 1 Biquad                                                                       |
+----------------------------+------------------------------------------------------------------------------------------------------+

\*Numbers are based on one instance of the algorithm with no additional "add" or "grow" Depending on the number filters within a given row, more Data RAM and Parameter RAM will be used. For the most accurate count of RAM being used for your instance of this algorithm, check the Output window within SigmaStudio for a full report. Each additional biquad in a given row, will add 12 Data RAM and 5 Parameter RAM.

| 
| ===Algorithm Growith information===

+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| Description              | When the algorithm is grown, a new filter row is added to the control. The input/output pins remains the same since this is still a stereo filter. The growth only affects the number of possible rows of filters. | |idxpic4.png| |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| Program RAM Repetition   | 0 per growth - Based on 1 Biquad for the growth                                                                                                                                                                    |               |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| Data RAM Repetition      | 0 per growth - Based on 1 Biquad for the growth                                                                                                                                                                    |               |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| Parameter RAM Repetition | 7 per growth - Based on 1 Biquad for the growth                                                                                                                                                                    |               |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+

| 
| ===Subroutine/Loop Information=== This algorithm makes use of GEN3 core features for both subroutines and loops. There is a savings on Program RAM because of the use of these features; however it is important to note the MIPS/cycles usage in order to not exceed the core's limit. The subroutine used for this algorithm is called "BiquadLoopingDP" and has 16 instructions. The number of MIPS is dependant on the max number of biquads in a given filter row. The Output window within SigmaStudio reports the both the number of instructions used and the MIPS for the subroutine.

| 
| =====IdxSelectable Indp. Multiple Band Filter (Slew)===== |image1|

Configurations
--------------

Outputs of the current and previously selected filter indexes are slewed to prevent audio pops/clicks during the transition.

DSP Parameter Information
-------------------------

+--------------------+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name   | Compiler Name          | Function Description                                                                                                                                                                                                                                 |
+====================+========================+======================================================================================================================================================================================================================================================+
| Filter Type (Icon) | IdxSelIndpBandAlg100b2 | Changing any one of the 5 filter GUI controls, will write 5 DSP parameters to the DSP. These are the filter coefficients (b2, b1, b0, -a2, -a1) and they are determined by the formulas found in the algorithm section for General 2nd Order Filters |
| Boost              | IdxSelIndpBandAlg100b1 |                                                                                                                                                                                                                                                      |
| Frequency          | IdxSelIndpBandAlg100b0 |                                                                                                                                                                                                                                                      |
| Q/Slope            | IdxSelIndpBandAlg100a2 |                                                                                                                                                                                                                                                      |
| Gain               | IdxSelIndpBandAlg100a1 |                                                                                                                                                                                                                                                      |
+--------------------+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Note :

-  The IdxSelectable Indp. Multiple Band Filter is also supported in SHARC processors (ADSP-SC5xx/215xx)

-  The filter algorithm used is a 2nd Order General Filter (Double Precision) based on a Direct Form II structure

.. |idxpic1.png| image:: https://wiki.analog.com/_media/idxpic1.png
.. |idxpic2.png| image:: https://wiki.analog.com/_media/idxpic2.png
.. |idxpic3.png| image:: https://wiki.analog.com/_media/idxpic3.png
.. |idxpic4.png| image:: https://wiki.analog.com/_media/idxpic4.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/isib1.png
   :width: 400px
