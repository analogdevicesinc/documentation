:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio>`

Export program and Parameter data
=================================

| Once a project is compiled you can export the data that is sent to the DSP out to disk files. These files, which can be opened in any text editor for analysis, are essential for finding parameters and addresses to integrate into microcontroller code. These files include C/C++ compatible header files defining the projects parameters and registers.
| Following project compilation, click the Export System Files toolbar button or choose Action - Export System Files circled below. (Be sure to re-compile your project each time you wish to generate the parameter file, so you have up-to-date information.)
| You will be prompted to enter a location for the files, choose a name and press the Save button. Several files will be generated, \*.params and \*.hex files and 2 header files for each schematic/core in the project.
| \* \*.params: lists all schematic algorithm parameters names, memory addresses, and values.

-  \*.h: header file which defines all schematic parameter's names, addresses and values.
-  \*_Defines.h: Schematic default download data definitions.
-  \*NumBytes.dat: has the number of bytes that are used to download the program data
-  \*.json :Project description in .json format along with hex data values

| Example - for a schematic like this one:
| |image1|
| You will see the following in the \*.param file:
| Module Name = MediumSizeEq_0
| Parameter Name = Stage0_B0
| Parameter Address = 3
| Parameter Value = 1
| Parameter Data :
| 0x3F, 0x80, 0x00, 0x00,
| Module Name = MediumSizeEq_0
| Parameter Name = Stage0_B1
| Parameter Address = 2
| Parameter Value = 0
| Parameter Data :
| 0x00, 0x00, 0x00, 0x00

| Module Name = MediumSizeEq_0
| Parameter Name = Stage0_B2
| Parameter Address = 1
| Parameter Value = 0
| Parameter Data :
| 0x00, 0x00, 0x00, 0x00,
| Module Name = MediumSizeEq_0
| Parameter Name = Stage0_A1
| Parameter Address = 5
| Parameter Value = 0
| Parameter Data :
| 0x00, 0x00, 0x00, 0x00,
| Module Name = MediumSizeEq_0
| Parameter Name = Stage0_A2
| Parameter Address = 4
| Parameter Value = 0
| Parameter Data :
| 0x00, 0x00, 0x00, 0x00,

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/exportngss.jpg
   :width: 600px
