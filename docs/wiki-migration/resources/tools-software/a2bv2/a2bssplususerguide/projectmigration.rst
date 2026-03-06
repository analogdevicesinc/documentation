:doc:`Click here to return to the A2B SSPLUS User Guide homepage </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide>`

Project Migration
=================

A2B projects from SigmaStudio can be imported and saved in SigmaStudio+ format. The following process can be used to migrate a Sigma studio A2B project into SigmaStudio+.

-  Open an existing A2B SigmaStudio project in SigmaStudio.
-  Link-compile the schematic
-  Right click on Target processor and select ‘Export System Configuration Files…’ shown below.

|image1|

.. container:: centeralign

   **Figure:** Exporting system configuration


-  A dialog box appears as shown in below. Export configuration file in **.xml** format.



|image2|

.. container:: centeralign

   **Figure:** Export SigmaStudio Project as BCF


-  Peripheral XML files which are used in SigmaStudio needs to be copied to "C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Rel2.0.0\\Schematics\\PC\\xml" for a smoother transition or specific path can be provided to avoid any conflicts.

.. note::

   To migrate DSP Projects on SigmaStudio to SigmaStudio+, refer :doc:`DSP Project Migration </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/importsigmastudio>`


-  Open SigmaStudi+, go to the **Action** menu, and choose **Import SigmaStudio Projects**.



|image3|

.. container:: centeralign

   **Figure:** Import SigmaStudio Project


-  Select the **.xml** Bus Configuration file, which is exported in step 4, and click on Open. On successful import of SigmaStudio Project to SigmaStudio+, platforms including peripherals are migrated as `custom platforms <https://wiki.analog.com/resources/tools-software/a2bv2/quickstartguide/_appendix-a>`__ .



|image4|

.. container:: centeralign

   **Figure:** Imported SigmaStudio Project


Double click on the custom platform to view the components of platform - :doc:`transceiver and peripherals </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-a>`

.. note::

   \ `Refer <https://wiki.analog.com/resources/tools-software/sigmastudiov2/usingsigmastudio/_customvsstandard>`__ Standard vs Custom Platforms


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/export_ss_bcf.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/export_ss_bcf_in_xml.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/import_ss_project.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/importbcf.jpg
   :width: 2160px
