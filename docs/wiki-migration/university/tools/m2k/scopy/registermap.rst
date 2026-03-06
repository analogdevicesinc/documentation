Scopy Register Map
==================

A register map, sometimes referred to as a memory map, is a structured representation of the registers within a computer system or electronic device.

=====1. Base functionality :=====

-   Read register
-   Write register

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/base_functionality.png
   :align: center

=====2. Functionality with XML file associated to the device :=====

-  Generate a table for the device register map based on an xml (the xml does not have to include all the registers of the device and it can be made to contain just some specific registers based on the user’s need)
-   When creating the map we will also treat the case where bits are “Reserved”. This bits can’t be read or written due to various reasons ( example: company confidential information; changing the value of the bit might cause damage to the hardware, etc)
-  If the device used by the user is not one that already has an xml file the user has the option to create one and by adding it where the project is installed the xml file will be available in the application
-   User can search between the registers. The search is made on 2 levels :

   -   Register level : search in register name or description

      -   Bitfield level : search in bit name or description

-  Offers a detailed view of the selected register and possibility to change values at bit level. The detailed view depends on the information provided on each bitfield( one or more bits that contains specific information), if the xml provides a list of possible values and the meaning of those values a dropdown with the options is presented, if not all bit combination for that bitfield are covered the user can also insert the value desired. If the bitfield has no options :

::

        *    If it only has one bit it will be a checkbox
        *    If it has multiple bits will be an editbox

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/regmap_xml.png
   :align: center

If no XML is available for a device the user has the option to create it based on the format below and add the file where where scopy is installed following this path /plugins/regmap/xmls/

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/regmap_xml_example.png
   :align: center
   :width: 400px

3. Settings
-----------

-   Auto read (automatically read registers once selected)
-   Read interval of registers
-   Write all values from a provided file to registers
-   Register dump ( save all current values of the registers in a csv file ). If Auto read is selected and a register interval mentioned the register dump will read and store that set of registers

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/regmap_settings.png
   :align: center
   :width: 400px

4. Preferences
--------------

Option to apply colors to reflect values of the registers ( there are 16 colors available and the logic behind is that the values are modulo 16 based on the value )

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/regmap_pref.png
   :align: center
   :width: 400px
