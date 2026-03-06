Automatic Speaker EQ
====================

| :doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`

+---+---+
| The Automatic Speaker EQ algorithm is aimed at reducing the design time of speaker systems by automatically tuning filters to create the desired frequency response of the speaker. The algorithm is capable of tuning one, two, and three way systems. | |AutoEQ1.png| |
+---+---+

| 

Input Pins
----------

=============== ================================== ====================
Name            Format [int/dec] - [control/audio] Function Description
=============== ================================== ====================
Pin 0: Audio In decimal - audio                    Audio Input
=============== ================================== ====================

Output Pins
-----------

One Speaker System

+------------------+------------------------------------+----------------------------+
| Name             | Format [int/dec] - [control/audio] | Function Description       |
+==================+====================================+============================+
| Pin 0: Audio Out | decimal - audio                    | Auto filtered audio output |
+------------------+------------------------------------+----------------------------+

Two Speaker System

+-----------------------------+------------------------------------+---------------------------------------+
| Name                        | Format [int/dec] - [control/audio] | Function Description                  |
+=============================+====================================+=======================================+
| Pin 0: Audio Out, Low Band  | decimal - audio                    | Auto filtered audio output, low band  |
+-----------------------------+------------------------------------+---------------------------------------+
| Pin 1: Audio Out, High Band | decimal - audio                    | Auto filtered audio output, high band |
+-----------------------------+------------------------------------+---------------------------------------+

Three Speaker System

+-----------------------------+------------------------------------+---------------------------------------+
| Name                        | Format [int/dec] - [control/audio] | Function Description                  |
+=============================+====================================+=======================================+
| Pin 0: Audio Out, Low Band  | decimal - audio                    | Auto filtered audio output, low band  |
+-----------------------------+------------------------------------+---------------------------------------+
| Pin 1: Audio Out, Mid Band  | decimal - audio                    | Auto filtered audio output, mid band  |
+-----------------------------+------------------------------------+---------------------------------------+
| Pin 2: Audio Out, High Band | decimal - audio                    | Auto filtered audio output, high band |
+-----------------------------+------------------------------------+---------------------------------------+

Algorithm Description
~~~~~~~~~~~~~~~~~~~~~

| The Automatic Speaker EQ is located in the ADI Algorithms section of the SigmaStudio Toolbox. Once included in the project, it is necessary to choose the proper algorithm for the current design. The Automatic Speaker EQ supports up to three-way speaker designs.
| |AutoEQ2.png|

Source Tab
~~~~~~~~~~

| When first opening the control, the source tab will be visible. This is where the response(s) of the desired speakers are loaded. Compatible formats include Impulse Responses with one measurement per line and Frequency responses in the :doc:`MLSSA file format </wiki-migration/resources/tools-software/sigmastudio/toolbox/systemschematicdesign/speakerresponsemlssa>`.
| |AutoEQ3.png|

Controls
--------

-  **Impulse Response Radio Button** – Click this to use an Impulse Response Measurement as the speaker response. Disables the Frequency Response file import.
-  **Frequency Response Radio Button** – Click this to use a Frequency Response Measurement as the speaker response. The :doc:`MLSSA file format </wiki-migration/resources/tools-software/sigmastudio/toolbox/systemschematicdesign/speakerresponsemlssa>` is supported. Disables all Impulse Response related controls. Several example MLSSA response files are included with SigmaStudio. Under a standard SigmaStudio installation, they can be found under your home directory: C:\\Users\\Username\\Documents\\Analog Devices\\SigmaStudio 4.5\\Projects\\Speaker Measurement Samples\\
-  **Click to load Impulse Response**
-  **Click to load Frequency Response**
-  **Impulse Response Graph** – The Impulse response will be displayed here. The blue curve represents the response. The red curve represents the window to be applied. Draggable points will appear to control the window start/length.
-  **dB Scale Checkbox** – Click this to toggle a dB/linear scale in the y-axis.
-  **Window Control Knobs** – These control the window start and length. Changes made via these knobs get reflected to the drag points on the Impulse Response graph.
-  **Apply Windowing Checkbox** – This allows the user to turn off the window and use the entire impulse response measurement.
-  **Frequency Response Graph** – The frequency response, whether from a file or calculated from the impulse response, will be displayed here. This is the raw frequency response of the speaker, before the Auto EQ has been calculated or applied.
-  **Offset Gain Control** – Allows the user to change the level of the frequency response.
-  **Smoothing Control** – Changes the smoothing of the frequency response that is calculated from the impulse response.

Target Response Tab
~~~~~~~~~~~~~~~~~~~

| The next tab provides tools to allow the user to design the desired target response for each transducer.
| |AutoEQ4.png|

.. _controls-1:

Controls
--------

-  **Design Controls**

   -  **Pointer Tool** – Allows the user to create points by double clicking, or move pre-existing points
   -  **Line Tool** – Create straight lines
   -  **Pencil Tool** – Draw curves by hand
   -  **Weighting Toggle** – Enables the weighting graph. Changes made to the weighting graph affect how much the Automatic Speaker EQ algorithm will focus on those sections.

-  **Gain Sliders** – These sliders change the overall gain of either the target or the source. Right click to enter a numerical value.
-  **Individual Band Target Graph** – Design the target using this graph. The blue curve is the source response. The target is defined by the drag points.
-  **Cutoff Points** – These points define the frequency band that the Automatic Speaker EQ algorithm should design in. Areas outside these frequencies will be ignored.
-  **Target From Filters Button** – This allows for the target response to be made using filters instead of by drawing. A separate dialog box will appear with different filter types. Changes in this dialog are reflected in the target graph in real time.
-  **Match Source Response** – This enables speaker modeling instead of speaker equalization. Checking this box will force the algorithm to create filters that match the response of the speaker.
-  **Combined Target Response Graph** – This graph shows exactly which part of each speaker the algorithm is going to design for. In multiband designs, this graph will have different colored sections for each speaker.

Design Settings Tab
~~~~~~~~~~~~~~~~~~~

| This tab provides controls to customize the operation of the Automatic Speaker EQ algorithm.
| |AutoEQ5.png|

.. _controls-2:

Controls
--------

-  **Show Advanced Settings** – Displays the technical settings of the Automatic Speaker EQ algorithm. For information about Advanced Settings, see the Appendix.
-  **# Filters Control** – This defines the number of filters that the Automatic Speaker EQ algorithm should use to match the target response.
-  **Low Cut** – This defines the frequency of the low boundary for the Automatic Speaker EQ algorithm.
-  **High Cut** – This defines the frequency of the high boundary for the Automatic Speaker EQ algorithm.
-  **Initialize Filters** – This will display a dialog that allows the user to initialize filters for the algorithm to use. Changes made in this dialog are displayed on the graph in real time. Note that initializing filters is not necessary for the algorithm to function properly. For more information, see the appendix.
-  **Design Filters Button** – Pushing this button will initiate the Automatic Speaker EQ algorithm for the currently viewed speaker.
-  **Include Crossover Checkbox** – This checkbox is only enabled for multiband designs. It will apply the effects of the crossover to the Equalized response and Filters curves.
-  **Design Graph** – This displays everything about the current design.
-  **Design All Button** – This will initiate the Automatic Speaker EQ algorithm for all speakers.

Filter Tabs
~~~~~~~~~~~

| After running the Automatic Speaker EQ algorithm, the Filters tab is automatically displayed. The Filters tab shows the results of the algorithm and allows the user to change the values of the filters as desired. The control is the same as the Parametric EQ included in Sigma Studio.
| |AutoEQ6.png|

.. _controls-3:

Controls
--------

-  **Graph Controls** – These control the x and y axis zoom, as well as allow the user to add and remove filters.
-  **Filter Table** – This displays all the information available about each filter, as well as allowing the user to edit each parameter.
-  **Graph overlays**

   -  **Show Crossover Effects** – Applies the crossover filter to the composite curve of all the filters.
   -  **Overlay Source** – Displays the source curve as a blue line on the graph
   -  **Overlay Electro**-Acoustic Response – Displays the result curve as a red line on the graph
   -  **Overly Target** – Displays the target curve as a green line on the graph.

-  **Export Results Button** – Exports the filter coefficients in a text file to be used with the General 2nd order EQ filter included with Sigma Studio.

Multiband Controls
~~~~~~~~~~~~~~~~~~

The multiband versions of the Automatic Speaker EQ algorithm contain two extra tabs to aid in designing a crossover for the system.

Crossover Tab
~~~~~~~~~~~~~

| The crossover tab is the same as the crossover control included in Sigma Studio. The initial crossover points are set at the cutoff frequencies defined on the Target Tab. The user is then free to edit them as needed.
| |AutoEQ7.png|

.. _controls-4:

Controls
--------

-  **Crossover Graph** – This is the graphical display of the crossover response. There are two lines per band – the response of the filter and the response of the speaker after the filter is applied.
-  **Enable Control** – In some cases it is necessary to disable to crossover filter. Uncheck this box to do so.
-  **Corner Frequency** – Change the frequency of the crossover filter.
-  **Gain** – Change the gain of the crossover filter.
-  **Filter Type** – Change the type of crossover filter.
-  **Polarity** – Invert the current band, if necessary.
-  **Link Enable** – Link the frequencies of the two crossover filters.

Crossover Tab Alignment
~~~~~~~~~~~~~~~~~~~~~~~

| Because the Automatic Speaker EQ uses IIR filters, the phase of the signal is affected. This creates a need to align the crossover filters to prevent unwanted cancellation due to phase irregularities. The alignment tab will help fix any phase-related cancellation and allow the user to fine-tune the system.
| |AutoEQ8.png|

.. _controls-5:

Controls
--------

-  **Alignment Controls** – These add delay/gain to the currently selected speaker. Results are updated in real time on all graphs.
-  **Individual Magnitude Graph** – This graph displays the response of the currently selected speaker.
-  **Individual Phase Graph** – This graph displays the phase of the currently selected speaker.
-  **Auto Align Button** – The Automatic Speaker EQ has a built-in alignment algorithm. Click this button to initialize the algorithm.
-  **Total Magnitude/Phase Graphs** – These graphs display the total output of the system, as well as the phase of each speaker together on the same graph to aid in aligning the crossover.

Filter Initialization/ Target From Filters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The dialogs for defining a target from filters and for initializing filters are the same.
| |AutoEQ9.png|

-  **Load/Save** – It is possible to load and save both target filter information and initialized filters.
-  **Graph Controls** – These control the scaling of the x and y axes.
-  **Add/Remove Filters** – Add/Removed filters. This is also possible via double clicking on the graph or right clicking on the graph.
-  **Filter Table** – This displays all the information about each filter.
-  **Fixed Checkbox** – This only applies to the initialized filters. Checking this box will make the algorithm “skip over” that filter. It will be applied directly to the transducer without being optimized by the Automatic Speaker EQ algorithm at all.

.. important::

   Some filters are fixed by default because they are special cases. Butterworth, Bessel, and Chebyshev filters are all special cases of high/low pass filters and cannot be modified by the algorithm. To have a high/low pass filter be optimized by the Automatic Speaker EQ, use the general high/low pass.


Advanced Settings
~~~~~~~~~~~~~~~~~

| The advanced settings are located on the Design Settings tab. They are hidden by default, but pushing the “Show Advanced Settings” button will make them appear.
| |AutoEQ10.png|

-  **Design Settings:**

   -  **Post-Optimization Iterations** – This defines how many passes the algorithm should make after designing filters while it tries to make the filters better.
   -  **Default Filter Q** – The initial Q value for designed filters.
   -  **Peak Emphasis** – How much weight to give to Peaks above the target.
   -  **Dip Emphasis** – How much weight to give to Dips below the target.

-  **Filter Tuning:** Applies to both design and optimization loops.

   -  **Tuning Iterations** – How many times the algorithm should change the filter parameters while trying to find the best fit.
   -  **Max Frequency Variation** – The maximum allowable shift in filter frequency
   -  **Max Gain Variation** – The maximum allowable change in gain of the filter
   -  **Max Q Variation** – The maximum allowable change in Q of the filter.

-  **Filter Constraints:**

   -  **Q Min/Max** – The smallest/largest Q value the algorithm can use when designing filters
   -  **Gain Min/Max** – The smallest/largest gain values the algorithm can apply to filters.

Menu Bar
~~~~~~~~

The menu on the Automatic Speaker EQ has some advanced functions associated with it. Under File, there are controls to load/save configurations. The Design menu has functions to import/export the target of the currently viewed tab, as well as to initiate the design process or reset the control.

.. |AutoEQ1.png| image:: https://wiki.analog.com/_media/AutoEQ1.png
.. |AutoEQ2.png| image:: https://wiki.analog.com/_media/AutoEQ2.png
.. |AutoEQ3.png| image:: https://wiki.analog.com/_media/AutoEQ3.png
.. |AutoEQ4.png| image:: https://wiki.analog.com/_media/AutoEQ4.png
.. |AutoEQ5.png| image:: https://wiki.analog.com/_media/AutoEQ5.png
.. |AutoEQ6.png| image:: https://wiki.analog.com/_media/AutoEQ6.png
.. |AutoEQ7.png| image:: https://wiki.analog.com/_media/AutoEQ7.png
.. |AutoEQ8.png| image:: https://wiki.analog.com/_media/AutoEQ8.png
.. |AutoEQ9.png| image:: https://wiki.analog.com/_media/AutoEQ9.png
.. |AutoEQ10.png| image:: https://wiki.analog.com/_media/AutoEQ10.png
