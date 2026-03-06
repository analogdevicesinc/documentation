Video Timing and Pattern Generator Tool
=======================================

The video timing and pattern generator is a very helpful debugging tool for checking various aspects of the GMSL signal chain. Both the serializer and deserializer can generate a either a checkerboard or gradient pattern.

.. image:: https://wiki.analog.com/_media/products/gmsl/gui/tools/vpg_full.png
   :align: center
   :width: 400px

Part Selection
--------------

.. container:: group

   
   .. container:: half column

      Select the part from the dropdown and choose either the serializer or deserializer. Additionally for devices with multiple pipes, select a specific pipe if needed.

         
         .. note::

            “Pipe” dropdown is invisible if the selected part only supports single pipe.

         

   
   .. container:: half column


         

   
   |image1|

Video Timing and Setup
----------------------

.. container:: group

   
   .. container:: half column

      Enter “Video Timing and Setup” parameters and click “Calculate PCLK” button. PCLK value will be updated according to the parameters. (PCLK value can be modified later if wanted.)

         
         If PCLK value is modified, user can calculate the FPS of to be generated video by clicking “Calculate FPS” button.
         
         For device types that support discrete PCLK values, there is a dropdown for PCLK parameter instead of a text box.
         
         .. note::

            For the device types that do not support internal clock generation “Internal” combo box is disabled.

         
         .. note::

            For the device types that support only internal clock generation “External” and “Source Video Port” combo boxes are disabled.

         

   
   .. container:: half column


         

   
   |image2|

Pattern Generation and Clock Source
-----------------------------------

.. container:: group

   
   .. container:: half column

      In this section, select the type of pattern to be generated and the parameters of that pattern.

         
      Once all the parameters are input, run the tool by clicking **“Start Video Generation”** button. The tool will give error if any parameter is not a valid value.

   
   .. container:: half column


   
   |image3|

Additional Information
----------------------

You can export the configuration as a script by navigating the top menu: File > Export Script.

Parameters are saved persistently after running the tool. Persistent values can be deleted by navigating to the menu item: Options > Reset Values

To read the current VTPG configuration of the device, navigate to: Options > Read Config

.. important::

   \ **For tunnel mode devices**: The pattern generation tool currently only operates in pixel mode so ensure the devices are configured accordingly.


.. |image1| image:: https://wiki.analog.com/_media/products/gmsl/gui/tools/vpg_part_sel.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/products/gmsl/gui/tools/vpg_vtg.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/products/gmsl/gui/tools/vpg_pattern.png
   :width: 600px
