:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio>`

Alias Pins
==========

| To organize your project visually, it often helps to create an alias to provide a clear connective reference (a "jump") in the signal flow in the schematic. An Alias consists of a pair of alias input and alias output blocks. Using alias blocks can reduce the visual clutter in the schematic window created by long wire connections.
|

.. tip::

   \ **Ctrl + Right-click** on the pin is the shortcut for creating an Alias for that given pin


| An alias can be created in two ways:

-  Drag and drop '**Alias Pin**' from the toolbox. It is available under the '**Canvas**' category in toolbox. Connect both ethe source and destination manually.
-  **Ctrl+Right-click** on a block's output/input pin. The alias input/output is automatically connected to selected pin. Next, manually connect the alias pair to the next block.

| |image1|
| It is possible to have multiple output alias pins created from the same Alias Input pin.
| |image2|
|

.. note::

   Note: Using an alias is functionally equivalent to connecting two pins with a wire. The signal flow in the example below is identical to the alias example above


| |image3|

Add Alias Output
----------------

| 
| Right clicking on Input Alias will display the context menu. Use the option '**Add Alias Output**' to add output alias. That output Alias can be moved to anywhere in schematic and connected with any block as signal destination. One Input Alias can have multiple output Aliases if required.
| |image4|
| ===== Highlighting All Alias ===== Clicking on any Input/Output Alias will highlight all aliases. All Aliases will be highlighted in “Aqua” color.
| |image5|
| ===== Go to Alias Output ===== User can go to particular output alias of choice by using this option. Example: If user clicks “1” in '**Go to Alias Output**' option, then 'Mute_0' block will come into visible part of schematic even if it is not in visible area of schematic. This helps user to easily navigate between and evaluate the schematic design.
| |image6|
| ===== Go to Alias Input ===== At any time, user can navigate back to Input Alias from any Output Alias using this option. '**Go to Alias Input**' option will be shown in every output alias. After clicking that option, Input Alias block will come into center part of schematic even if it is not in visible area of schematic. This helps user to easily navigate between and evaluate the schematic design.
| |image7|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/alias_2.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/alias_4.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/alias_7.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/alias_3.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/alias_8.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/alias_6.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/alias_5.png
