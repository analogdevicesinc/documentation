Chime Freq-Gain
===============

:doc:`Click here to return to the Sources section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`

.. important::

   To Do: This page currently shows information for the Chime Freq-Gain algorithm. It needs to be changed to show the Chime Frequency algorithm.


+---------------------------------------------------------------------------------------------------------------------+--------------------+
| The Chime Freq-Gain algorithm plays back a chime sound with programmable, independent frequency and gain envelopes. | |chimefreq024.jpg| |
+---------------------------------------------------------------------------------------------------------------------+--------------------+

| 
| There are two versions of the algorithm available:

-  Chime Freq – Gain
-  Chime Freq – Gain Continuous Play

| 
| ===== Input Pins =====

+-----------------------+------------------------------------+-------------------------------+
| Name                  | Format [int/dec] - [control/audio] | Function Description          |
+=======================+====================================+===============================+
| Pin 0: Chime Activate | int - control                      | Switch used to activate chime |
+-----------------------+------------------------------------+-------------------------------+

Output Pins
-----------

+---------------------+------------------------------------+----------------------+
| Name                | Format [int/dec] - [control/audio] | Function Description |
+=====================+====================================+======================+
| Pin 0: Audio Output | decimal - audio                    | Chime Audio Output   |
+---------------------+------------------------------------+----------------------+

GUI Controls
------------

+-------------------+---------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name  | Default Value | Range       | Function Description                                                                                                                                                                                                                            |
+===================+===============+=============+=================================================================================================================================================================================================================================================+
| Maximum Time (ms) | 1004          | 10 to 4400  | Determines the length of the x axis in the envelope control window                                                                                                                                                                              |
+-------------------+---------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Envelope Control  | n/a           | n/a         | Allows the frequency and gain curves to be manually adjusted. Double-clicking on the graph creates a new point. Right clicking on the graph allows points to be removed. The graph can be zoomed using the zoom icons in the upper left corner. |
+-------------------+---------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Frequency (Hz)    | n/a           | 20 to 20000 | Controls the frequency coordinate of the corresponding point on the envelope                                                                                                                                                                    |
+-------------------+---------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Time (ms)         | n/a           | 0 to max    | Controls the time coordinate of the corresponding point on the envelope                                                                                                                                                                         |
+-------------------+---------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Gain (dB)         | n/a           | -120 to +24 | Controls the gain coordinate of the corresponding point on the envelope                                                                                                                                                                         |
+-------------------+---------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| GUI Name                                             | Compiler Name                                                 | Function Description                               |
+======================================================+===============================================================+====================================================+
| Envelope Control                                     | Optimized2ChimeAlgWGainGUI1numberofpoints                     | Number of points in the timing table               |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| Envelope Control                                     | Optimized2ChimeAlgWGainGUI1table                              | First point in the timing table                    |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| Envelope Control                                     | Optimized2ChimeAlgWGainGUI1table_autoincremented              | Timing table values (continued)                    |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| ...                                                  | ...                                                           | ...                                                |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| Envelope Control                                     | Optimized2ChimeAlgWGainGUI1numberofgainpoints                 | Number of points in the gain table                 |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| Envelope ControlOptimized2ChimeAlgWGainGUI1gaintable | First point in the gain table                                 |                                                    |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| Envelope Control                                     | Optimized2ChimeAlgWGainGUI1gaintable_autoincremented          | Gain table values (continued)                      |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| ...                                                  | ...                                                           | ...                                                |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| Envelope Control                                     | Optimized2ChimeAlgWGainGUI1freqincrement                      | Increment value for frequency table                |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| Envelope Control                                     | Optimized2ChimeAlgWGainGUI1freqincrement_autoincremented      | Frequency table values (continued)                 |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| ...                                                  | ...                                                           | ...                                                |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| Envelope Control                                     | Optimized2ChimeAlgWGainGUI1startfreq                          | Beginning frequency of the chime                   |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| Envelope Control                                     | Optimized2ChimeAlgWGainGUI1lowestfreq                         | Lowest frequency in the chime’s frequency envelope |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| Envelope Control                                     | Optimized2ChimeAlgWGainGUI1gainincrementtable                 | First point in the gain increment table            |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| Envelope Control                                     | Optimized2ChimeAlgWGainGUI1gainincrementtable_autoincremented | Gain increment table values (continued)            |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| ...                                                  | ...                                                           | ...                                                |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| Envelope Control                                     | Optimized2ChimeAlgWGainGUI1startgain                          | Starting gain value of the gain envelope           |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| Envelope Control                                     | Optimized2ChimeAlgWGainGUI1lowestgain                         | Lowest gain value in the gain envelope             |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+
| Envelope Control                                     | Optimized2ChimeAlgWGainGUI1mask                               | Mask                                               |
+------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------+

Algorithm Description
---------------------

| The chime algorithm has fully programmable frequency and gain envelopes. The envelopes are accessible by clicking the cell’s icon.
| |image1|
| The length of the chime is controlled by the Maximum Time control, which is set in milliseconds.
| The envelope control window has two tabs: Frequency and Gain. The Frequency envelope is displayed in blue, and the Gain envelope is displayed in red. Points on the curve can be moved by click-dragging. New points can be added by double-clicking. Points can be removed by right-clicking and selecting “remove point.” In this case, the point closest to the mouse cursor will be removed. Each envelope must have at least 3 points. Point values can be fine-tuned using the text input boxes on the right side of the envelope control window.
| |image2|
| When the control input goes to 1, the chime begins. When the control input goes to 0, the chime output stops, regardless of whether the envelope has completed or not.
| In the case of the Chime Freq – Gain Continuous Play algorithm, the envelope will loop continuously until the control input goes to 0.
| The example below shows the chime algorithm’s input and output signals using the gain envelope shown above.
| |image3|
| The example below has the input going to zero before the envelope has completed. The output will immediately go to zero.
| |image4|
| ===== Example ===== The following schematic image shows the Chime Freq-Gain cell being used with a 28.0 switch and being output to a DAC. The schematic below uses the Switch, Chime Freq-Gain, and Output cells.
| |image5|
| ===== Algorithm Details =====

+----------------------------+------------------------------------------------+
| Toolbox Path               | Sources – Chime – Modulated Frequency and Gain |
+----------------------------+------------------------------------------------+
| Cores Supported            | AD1940                                         |
|                            | ADAU144x                                       |
|                            | ADAU176x                                       |
|                            | ADAU178x                                       |
+----------------------------+------------------------------------------------+
| "Grow Algorithm" Supported | no                                             |
+----------------------------+------------------------------------------------+
| "Add Algorithm" Supported  | no                                             |
+----------------------------+------------------------------------------------+
| Subroutine/Loop Based      | no                                             |
+----------------------------+------------------------------------------------+
| Program RAM                | 96                                             |
+----------------------------+------------------------------------------------+
| Data RAM                   | 21                                             |
+----------------------------+------------------------------------------------+
| Parameter RAM              | 31                                             |
+----------------------------+------------------------------------------------+

.. |chimefreq024.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/chimefreq024.jpg
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/chimefreqgain025.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/chimefreqgain027.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/chimefreqgain028.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/chimefreqgain029.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/chimefreqgain030.jpg
