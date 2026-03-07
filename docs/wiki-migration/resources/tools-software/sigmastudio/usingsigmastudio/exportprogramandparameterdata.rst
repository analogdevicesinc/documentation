Export Program and Parameters
=============================

| :doc:`Click here to return to the Using Sigma Studio page </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio>`
| Once a project is compiled you can export the data that is sent to the DSP out to disk files. These files, which can be opened in any text editor for analysis, are essential for finding parameters and addresses to integrate into microcontroller code. These files include C/C++ compatible header files defining the projects parameters and registers.
| |exportprogrampic1.png|

Following project compilation, click the **Export System Files** toolbar button or choose **Action - Export System Files** circled below. (Be sure to re-compile your project each time you wish to generate the parameter file, so you have up-to-date information.)

You will be prompted to enter a location for the files, choose a name and press the Save button. Several files will be generated, \*.params and \*.hex files and 2 header files for each IC in the project.

-  **\*.params** lists all schematic algorithm parameters names, memory addresses, and values.
-  **\*.hex** lists the parameter memory raw byte values in hexadecimal format, this data is also reflected in the Parameter Data field of the params file.
-  **\*.h** header file which defines all schematic parameter's names, addresses and values.
-  **\_REG.h** header file contains definitions for all hardware registers and the settings defined in the register control window.

| **Example - for a schematic like this one:**
| |exportprogrampic2.png|
| You will see the following in the \*.params file:
| |exportprogrampic3.png|

.. |exportprogrampic1.png| image:: https://wiki.analog.com/_media/exportprogrampic1.png
.. |exportprogrampic2.png| image:: https://wiki.analog.com/_media/exportprogrampic2.png
.. |exportprogrampic3.png| image:: https://wiki.analog.com/_media/exportprogrampic3.png
