Variant Editor Window
=====================

| :doc:`Click here to return to the Hardware Windows page </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows>`
| This page describes how to utilize the ADAU145x (ADAU1450, ADAU1451, ADAU1452) and ADAU146x (ADAU1467, ADAU1463, ADAU1466, and ADAU1462) Variant Editor to post modify an external memory program using GPIO pins as input selectors. The Variant Editor supports both I2C and SPI bus interfaces.

--------------

Introduction
------------

The Variant Editor is a SigmaStudio tool that helps the user utilize different variations of his original audio program flow already programmed into an external memory. Using this editor, provides the following advantages:

-  Test the variations before they’re programmed into an external memory.
-  Suggests a memory address for each variation, these addresses can be overwritten by the user as well.
-  Keeps a revision history number (in Hex), manually configurable.
-  Allows the user select any GPIO available.
-  Chose memory parameters.
-  Enable / Disable variant compilation code.

Basic Usage
-----------

The Variant Editor is designed to be used for the ADAU145x and ADAU146x family only. We will create an example that uses only 4 variants. The steps to create a variation of an audio program flow are as follows:

1) Create a SigmaStudio audio flow that compiles with no errors.

2) Compile the project and save it.

3) After compilation is successful, go to “Hardware Configuration” tab. Right click on the IC cell and choose “Self-boot Memory” -> “Launch Variant Editor”. Refer to Figure 1.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/launchvarianteditor.png
   :align: center
   :width: 800px

::

                                      Figure 1: Launch Variant Editor  

4) A brand new Variant Editor window will appear ready to be populated with parameter, memory, and GPIO information. Refer to Figure 2.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/newvariantwindow.png
   :align: center
   :width: 800px

::

                                     Figure 2: New Variant Editor Window                                    

5) Start populating the Variant Editor with parameters from the audio flow. To do this we encourage the use of SigmaStudio “Capture Window”. The Example below depicted on Figure 3 explains the use of Capture Window while writing parameters from a simple second order filter.


|image1|

::

                                     Figure 3: Modifying schematic parameters to create variants

Select the desired parameter writes (including Safeload writes) from the Capture window. Drag and drop these parameters into the Variant Editor. The variant editor should look like Figure 4.


|image2|

::

                           Figure 4: Drag & Drop from capture window to Variant Editor to create the first variant

Once the first variant is completed, proceed to the next variant.

6) Add another variant. To do this, simply right click on the left side of the window, under the previous mode. A menu item window box will appear with many options. Select “Add Mode” as depicted on Figure 5 and the variant window will look like Figure 6.


|image3|

::

                                       Figure 5: Adding a new variant mode

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/newvariantmodecreated.png
   :align: center

::

                                      Figure 6: New variant mode created

7) Change variant mode names. In order to give relevance to the variant design, it is good practice to give variants a descriptive name. To do so, just double click on the variant name, the name will be highlighted and ready to be edited. An alternative way to change the name is by right clicking on it and select “Rename…” as illustrated on Figure 7.


|image4|

::

                                      Figure 7: Renaming a variant mode

8) Once all variants are finished and given descriptive names, is time to look at the editor tabs.

a.- The Variant Editor tab is the tab that will allow us to allocate variant address to the external memory, configure GPIO pins, and program the external memory. To start programming the external memory we need first to click on the “Update” button. This button will calculate the whole program length and give an address range within the external memory, see Figure 8. At the same time, the names of each variant will appear in a table format along with a suggested memory allocation and a default revision history number “0” (in Hex). By default, GPIO 6 and GPIO 7 are checked. The maximum variant number is governed by a factor of 2^(number of selected GPIOs). This example we have 2^(2 used GPIO) = 4. Before loading the EEPROM we must configure the external memory using the EEPROM Editor tab.


|image5|

::

                                     Figure 8: Updating Variant Editor using the "Update" button

b.- The EEPROM Editor tab contains read only memory settings to set the Master Port AFTER the program is loaded, see Figure 9. In other words, these settings will be used when accessing variant code (only) during self-boot time. The protocol can be either SPI or I2C. On the properties group, we can set the Memory Size, Page Size, Write Speed, and Number of Address Bytes according to the memory manufacturer data sheet. For SPI, there is a special section to be filled.


|image6|

::

                                     Figure 9: EEPROM Editor tab

9) Test Variant information before programming the external memory. Save the Editor first by clicking on the disk icon located on the Variant Editor main menu. Then, find the button with a green arrow over a white window icon (last button). When hovering over this button it should read “Launch Sequencer Window”. Click on it and the stand-alone sequencer window will pop up displaying four buttons in a grid. By clicking to any of these buttons, the current program that runs on the DSP should start changing accordingly; refer to Figures 10 and 11. In a similar fashion, by selecting the variant name and clicking the grey arrow will download that variant parameters to the DSP.


|image7|

::

                            Figure 10: Saving Variant Editor and launching stand-alone sequencer window                     

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/standalonesequencerwindow.png
   :align: center

::

                                           Figure 11: Stand-alone Sequencer Window

10) Once all the variants are working as expected, is time to program the external memory. To begin this process, click on the “Load EEPROM With Current Program and Variants” button, located at the Variant Editor tab. The “EEPROM Properties” window will appear. Fill this window with the proper memory manufacturer specifications. On this example we’re using a 1 Mbit SPI Bus Serial EEPROM. Thus, the parameters depicted on Figure 12. This information will be used to program the whole program and data memory along with variant information to the EEPROM, using these parameters to load the program at boot time into the DSP while self-boots.


|image8|

::

                                           Figure 12: EEPROM Properties window

11) GPIO configuration: By now, there is nothing else to do, the Variant Editor already set the proper registers of the selected GPIO pins. In this example we used GPIO 6 and GPIO 7. Their register settings were automatically set to serve as input pins as shown on Figure 13.


|image9|

::

                                    Figure 13: GPIO register settings    

Other Functionalities
---------------------

Compile Using Variant Code
~~~~~~~~~~~~~~~~~~~~~~~~~~

After creating our first variation code and programming it to the external memory, there are some extra functionalities to consider. At this point the EEPROM contains variant information, illustrated on Figure 14, at a previously selected memory address, driven by the GPIO pins. Every time the SigmaStudio project is compiled, the variant code will access the EEPROM and will try to write whatever is on the specified address and GPIO configuration. For example, if GPIO 6 is selected and GPIO 7 is not, then Table 1 will help us understand the output after compilation.\


|image10|

::

                             Figure 14: Variant Modes Reference

====== ====== ========================
MSB    LSB    
====== ====== ========================
GPIO 7 GPIO 6 Variant Output
0      0      High Pass Filter 1500 Hz
0      1      Vol at -20 dB
1      0      Low Pass Filter 450 Hz
1      1      Vol at 0 dB
====== ====== ========================

::

      Table 1: Truth table and Variant output

As noticed on Table 1, the result will point to “Vol at -20 dB” parameters on which will be accessed after every compilation. If we decide to move the GPIO configuration to GPIO 6 and 7 enabled and compile again, we will experience the “Vol at 0 dB” parameters as our audio flow output. One last thing to note is that on one hand the GPIO selection has been designed in such a way that the smallest index value will become the LSB, and on the other hand, the highest index value is mapped to be the MSB.

If the user chooses to disable this functionality, he simply need to un-check the “Compile Using Variant Code” check box, depicted on Figure 15.


|image11|

::

                       Figure 15: Compile using Variant Code checkbox

Clear/Update
~~~~~~~~~~~~

The “Clear” button will erase the variant modes, suggested memory addresses, and revision as shown on Figure 16. Along with this, the “Load EEPROM With Current Program and Variants” button will be disabled. To get an updated version of the variant modes, the “Update” button will re populate the suggested values.


|image12|

::

                      Figure 16: Clear Variant Modes

Save
~~~~

Saving the Variant Editor will create one XML file with a \*.var extension. At the same time, all the information will also be stored as binary format. The latter will only be saved if the “Save” button is clicked from SigmaStudio’s main menu. If the “Save” button is clicked on SigmaStudio’s main menu, then both XML and Binary formats will be saved. Both files will be saved on the same folder. Refer to Figures 17 through 19.


|image13|

::

                     Figure 17: Saving Variant in XML format

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/savingsigmastudioprojectwvariantinfo.png
   :align: center

::

                     Figure 18: Saving SigmaStudio project and Variant information in binary format

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/sigmastudioprojectandvariantfiles.png
   :align: center

::

                     Figure 19: SigmaStudio project and Variant files

The \*.var file can be edited with any text editor, however it is strongly recommended not to manually modify this document. As an example, the file looks like Figure 20.


|image14|

::

                     Figure 20: Variant Modes in XML format

Import File
~~~~~~~~~~~

When importing a file, we’re replacing an old Variant Mode information with another previously saved Variant Modes (\*.var) file. Saving after importing a file will affect the imported file and not the original replaced file. The user must be aware that the addresses may not match with the schematic audio flow. Extra caution is advised when importing files.


|image15|

::

                     Figure 21: Import File Button

SigmaStudio will save all the Variant parameters from the last \*.var file, and will assume this until changed and saved with a different file. In a similar fashion, SigmaStudio will execute and compile with the latest imported file.

Create New
~~~~~~~~~~

The Variant Editor window has a “White Paper Sheet” icon to the left of its menu (the first menu button). When clicked, a new variant file will be created. WARNING: Your previously saved file *will* be replaced when saving the window. However, if the “Save” button is not clicked from SigmaStudio main menu, and the project closes unsaved, then there is a chance to revert these changes if desired. If that is not the intention, then after replacing the \*.var file, a “Save” from SigmaStudio main menu is required to completely replace the file.

Variant Window Closed
~~~~~~~~~~~~~~~~~~~~~

SigmaStudio will keep all variant information even if the Variant Editor window remains closed. If the user wants to compile with or without using Variant code, then the window must be re-opened and change the checkbox state. Refer to Figure 15.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/modifyingschematicparameters.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/dragndropfromcapturewinw.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/addinganewvariantmode.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/renamingavariantmode.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/updatevewithupdatebutton.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/eepromeditortab.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/savingvarianteditor.png
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/eeprompropertieswndw.png
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/gpioregistersettings.png
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/variantmodesreference.png
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/compileusingvariantcheckbox.png
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/clearvariantmodes.png
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/savingvariantinxml.png
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/variantmodesinxmlformat.png
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows/importfilebutton.png
