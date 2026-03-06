====== Appendix D ======

Exporting A2B XML Files for use in the Audio Starter Projects
=============================================================

**\_\_ For this guide, we are going to assume that you have a working network project fully prepared and ready for export. \_\_**

**1.** Save the project and create an "export" directory under the directory where the project was saved.

**2.** Right click on "Target Processor".

**3.** Select "Export System Config Files..."

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/wiki_ss_pic1.png
   :width: 400px

**4.** Navigate to the "Command List Export" tab at the top. Select the File Path where you want your ".xml" and/or ".h" files for export as desired. Once you click "Browse" and navigate to the desired location to export, you will also have the chance to name your export file at this point.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/wiki_ss_pic2.png
   :width: 400px

**5.** It is useful to use a relative path to the project (i.e. ".\\export\\<file>.xml"). This way both the project and exported files can be stored together in version control or zipped together for easy relocation.

**6.** Select "OK" to save, select "Cancel" to close the dialog.

**Note:** If two or more A2B transceivers are located on the same I2C bus, the exports can be merged in the "Command List Merge" subtab (see below for visual).

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/wiki_ss_pic3.png
   :width: 400px

--------------

`Appendix C - Common Problems#.|Advanced Audio Projects#.|Advanced Audio Projects <https://wiki.analog.com/_media/navigation Advanced Audio Projects#.appendix-c>`__
