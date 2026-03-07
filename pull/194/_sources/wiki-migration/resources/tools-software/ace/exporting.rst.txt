Exporting Interaction With Hardware
===================================

When transitioning from an evaluation platform to custom designed hardware it is often necessary to understand the state of the hardware settings or interactions occurring during an evaluation session. ACE provides two options to export this information.

Register Dump
-------------

The easiest way to export the values of all the registers is to save your session by clicking on "Save Session" under the "File" menu. This will create an XML file that includes the register settings for all of the chips in the session. Each chip will be represented by a "Chip" element, with the name and id stored in attributes. Each chip that contains registers will contain one or more "RegisterMap" element with "Register" elements inside. The Register elements provide the address and value in attributes. Other information is also available in the session file.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/regmap.png
   :width: 400px

Recording Macros
----------------

The actions the user takes using ACE can be recorded as Macros. These actions will include GUI navigation as well as reads and writes to the parameters, consisting of groups of bits, or registers belonging to devices that ACE can control.

First, open the macro recorder from the "View" menu:

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/macro_tools.png
   :width: 200px

Next, you can record a macro by pressing the record icon in the "Macro Tools" tool view. After completing some interactions with the GUI, press the stop icon and a macro editor appears on the left. The macro can be edited by choosing steps to skip or adding comments. Finally, the macro can be exported to be used as a reference for the interactions that happened in the session, or to replay in a different session.


|image1|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/ace/macro_editor.png
   :width: 1000px
