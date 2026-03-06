Navigation
==========

You can return to the ACE Application User Guide Homepage here: :doc:`Application User Guide </wiki-migration/resources/tools-software/ace/applicationuserguide>`

-  :doc:`Previous (Chip View) </wiki-migration/resources/tools/software/ace/understandingtheui/chipview>`
-  :doc:`Next (Capture View) </wiki-migration/resources/tools/software/ace/understandingtheui/captureview.txt>`

Memory Map View
---------------

The Memory Map View shows all registers and bit fields that make up the component


|Memory Map View – Registers Visible|

Display Types
~~~~~~~~~~~~~

The data contained in the memory map of the component can be viewed in the following ways:

-  **Registers View –** Displays all registers in the component, Figure 12. These registers can be expanded to show the bit fields within.

-  **Bit Fields View –** Displays all bit fields in the component, Figure 13.

.. image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/BitFields.png
   :alt: Memory Map View - Bit Fields Visible

Component Styles
~~~~~~~~~~~~~~~~

When the value of a register or bit field is changed so that the value in the software doesn’t match the expected value in the hardware, the register or bit field will be highlighted by the text being bolded.

The colors of the bits indicate the access type of the bit:

| |WriteReadBit.png|
| A bit with a “Write Read” access type which can be written to and read from where the software value matches the expected hardware value.

| |ReadOnlyBit.png|
| A bit with a “Read Only” access type which can only be read from.

| |NABit.png|
| A bit which does not exist in the bit field.

Configuration
~~~~~~~~~~~~~

The Register view, allows you to configure registers at a bit level. The value can be changed either by changing the hexadecimal value in the hex data column or by clicking on individual bits in the binary data column. Registers can be expanded to show the bit fields that make them up and these bit fields can also be controlled by toggling the bits.

The Bit Fields view, allows bit field values to be modified by changing a control’s value. Changing the value of a control will modify the bit field value to that which the control selection represents. The hex data column displays the hexadecimal value of the bit field’s control state.

Filtering the Display Content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Both of these views can be filtered based on functional groups, register maps, or pages groups from the filter view pane. These filters will be maintained when switching between the register and bit field views.

Searching for a Bit Field
~~~~~~~~~~~~~~~~~~~~~~~~~

The search section allows you to search for particular bit fields based on the name or address. Clicking on the desired result will highlight it in the main grid.

Paging
~~~~~~

Paging or local channeling is available on components which are made up of multiple channels that need to be configured separately

Selecting a Page
~~~~~~~~~~~~~~~~

The different page groups are displayed in the page selector selection at the top of the view. Each group has an associated drop-down menu where you can select which page in a page group is the currently selected page. The selected pages value is the value visible in the register or bit fields grid. When the selected page group is changed the software will update to show the values for the newly selected page.

When the registers are visible and expanded, the page group associated with a bit field is displayed beside the name of that bit field,If the bit fields view is selected the page group associated with the bit field will be displayed in the page group column.

Paging With Bit Fields View
===========================

.. image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/pagingbitfields.png
   :alt: pagingbitfields.png

Paging With Registers View
==========================

.. image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/pagingregisters.png
   :alt: pagingregisters.png

Duplicating Pages across a Page Group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The copy button under each page group in the page selector group allows values to be copied from one page in a page group to others in the same group. To perform this select the page you want to copy the value from in the drop down menu and then check the boxes of the pages you want to copy the values to. Clicking the copy button will perform the change while clicking close or outside of the copy pop-up will close the pop-up without performing the copy.

.. |Memory Map View – Registers Visible| image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/MemoryMap.png
.. |WriteReadBit.png| image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/WriteReadBit.png
   :width: 30px
   :height: 30px
.. |ReadOnlyBit.png| image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/ReadOnlyBit.png
   :width: 30px
   :height: 30px
.. |NABit.png| image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/NABit.png
   :width: 30px
   :height: 30px
