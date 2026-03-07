Nx1 Mixer (Linear)
==================

| 
| :doc:`Click here to return to the Mixers/Splitters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/mixerssplitters>`
| There are three versions of 'NX1 Mixer' algorithm.

-  2x1 (No Slew)
-  3x1 (HW Signals)
-  4x1 (No Slew)

| 
| =====2x1 (No Slew) ===== The 2x1 Mixer has 2 input channels and 1 output channel. 2x1 mixers mixes two input channels to one output channel. Each input mix level can be independently adjusted. There are two combo boxes for setting the gain, one combo box for one input pin. To set the gain, click on the combo box and enter the value in the range of -128.0 to 127.999. |image1|
| ===== Input Pins====

======== ================================== ====================
Name     Format [int/dec] - [control/audio] Function Description
======== ================================== ====================
Pin 0\*: Decimal -                          audio
Pin 1\*: Decimal -                          audio
======== ================================== ====================

+-----------------------------------------------------------------+


| Note : \*Indicated for 2x1 Mixer. Input pins will increase by N |

+-----------------------------------------------------------------+

| 

Output Pins
===========

====== ================================== ====================
Name   Format [int/dec] - [control/audio] Function Description
====== ================================== ====================
Pin 2: Decimal -                          audio
====== ================================== ====================

|

GUI Controls
============

+------------------+---------------+-------------------+---------------------------------------------------------------+
| GUI Control Name | Default Value | Range             | Function Description                                          |
+==================+===============+===================+===============================================================+
| vol              | 1             | -128.0 to 127.999 | This control specifies the gain that applying to input signal |
+------------------+---------------+-------------------+---------------------------------------------------------------+

| 
| ===== Grow and Add Algorithm ===== Growth is supported to maximum of 16 output channels. Add Algorithm is not supported.

| 
| ===== DSP Parameter Information =====

+------------------+------------------------------------------------------------------------------------+-------------------------------+
| GUI Control Name | Compiler Name                                                                      | Function Description          |
+==================+====================================================================================+===============================+
| vol              | <fc #008000>Mixer2x1NoSlewS300Alg</fc><fc #ff0000>1</fc><fc #000080>vol_00_00</fc> | gain to apply to input signal |
+------------------+------------------------------------------------------------------------------------+-------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name

| 
| ====Supported DSPs===== ADAU145x

3x1 (HW Slew)
=============

The 3x1 Mixer has 3 input channels and 1 output channel. 3x1 mixers,mixes three input channels to one output channel. Each input mix level can be independently adjusted. There are three combo boxes for setting the gain, one combo box for one input pin. To set the gain, click on the combo box and enter the value in the range of -128.0 to 127.999. The gain values are slewed to reduce audio clicks. Slewing options can be selected from the context menu.

| |image2| |image3|
| ===== Input Pins====

======== ================================== ====================
Name     Format [int/dec] - [control/audio] Function Description
======== ================================== ====================
Pin 0\*: Decimal -                          audio
Pin 1\*: Decimal -                          audio
Pin 2\*: Decimal -                          audio
======== ================================== ====================

+-----------------------------------------------------------------+


| Note : \*Indicated for 3x1 Mixer. Input pins will increase by N |

+-----------------------------------------------------------------+

| 

.. _output-pins-1:

Output Pins
===========

====== ================================== ====================
Name   Format [int/dec] - [control/audio] Function Description
====== ================================== ====================
Pin 3: Decimal -                          audio
====== ================================== ====================

|

.. _gui-controls-1:

GUI Controls
============

+------------------+---------------+-------------------+---------------------------------------------------------------+
| GUI Control Name | Default Value | Range             | Function Description                                          |
+==================+===============+===================+===============================================================+
| vol              | 1             | -128.0 to 127.999 | This control specifies the gain that applying to input signal |
+------------------+---------------+-------------------+---------------------------------------------------------------+

| 
| ===== Grow and Add Algorithm ===== Growth is supported to maximum of 8 output channels. Add Algorithm is not supported.

| 
| ===== DSP Parameter Information =====

+------------------+-------------------------------------------------------------------------------------+-------------------------------+
| GUI Control Name | Compiler Name                                                                       | Function Description          |
+==================+=====================================================================================+===============================+
| vol              | <fc #008000>Mixer3x1SlewS300Alg</fc><fc #ff0000>1</fc><fc #000080>target_00_00</fc> | gain to apply to input signal |
+------------------+-------------------------------------------------------------------------------------+-------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name

| 
| ====Supported DSPs===== ADAU145x
| =====4x1 (No Slew) ===== The 4x1 Mixer has 4 input channels and 1 output channel. 4x1 mixers mixes four input channels to one output channel. Each input mix level can be independently adjusted. There are four combo boxes for setting the gain, one combo box for each input pin. To set the gain, click on the combo box and enter the value in the range of -128.0 to 127.999. |image4|
| ===== Input Pins====

======== ================================== ====================
Name     Format [int/dec] - [control/audio] Function Description
======== ================================== ====================
Pin 0\*: Decimal -                          audio
Pin 1\*: Decimal -                          audio
Pin 2\*: Decimal -                          audio
Pin 3\*: Decimal -                          audio
======== ================================== ====================

+-----------------------------------------------------------------+


| Note : \*Indicated for 4x1 Mixer. Input pins will increase by N |

+-----------------------------------------------------------------+

| 

.. _output-pins-2:

Output Pins
===========

====== ================================== ====================
Name   Format [int/dec] - [control/audio] Function Description
====== ================================== ====================
Pin 4: Decimal -                          audio
====== ================================== ====================

|

.. _gui-controls-2:

GUI Controls
============

+------------------+---------------+-------------------+---------------------------------------------------------------+
| GUI Control Name | Default Value | Range             | Function Description                                          |
+==================+===============+===================+===============================================================+
| vol              | 1             | -128.0 to 127.999 | This control specifies the gain that applying to input signal |
+------------------+---------------+-------------------+---------------------------------------------------------------+

| 
| ===== Grow and Add Algorithm ===== Grow Algorithm is supported for a maximum of 8 output channels. Add Algorithm is not supported.
| ===== DSP Parameter Information =====

+------------------+---------------------------------------------------------------------------------+-------------------------------+
| GUI Control Name | Compiler Name                                                                   | Function Description          |
+==================+=================================================================================+===============================+
| vol              | <fc #008000>Mixer4x1lewS300Alg</fc><fc #ff0000>1</fc><fc #000080>vol_00_00</fc> | gain to apply to input signal |
+------------------+---------------------------------------------------------------------------------+-------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name

| 
| ====Supported DSPs===== ADAU145x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/2x1mixer.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/3x1.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/3x1_slew_.png
   :width: 300px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/4x1.png
   :width: 400px
