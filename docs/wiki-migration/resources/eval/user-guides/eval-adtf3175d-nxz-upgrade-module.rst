Module Upgrade
==============

If you have an EVAL-ADTF317D-NXZ kit with serial numbers starting with 'CR' or 'DV11', the ADTF3175 modules on the kits are no longer supported (Release 4.3.0+). Please order a replacement module to update your system.

To do this please contact your local FAE to place a replacement order for ADTF3175XMLZ. Please provide the SO number for the previous order.

Why this is needed
------------------

The new ADTF3175 modules use updated sensor firmware which contain the following changes:

-  Thermal Compensation model added
-  Updated integration times
-  Updated laser safety features

Installation Instructions
-------------------------

What is needed
~~~~~~~~~~~~~~

-  EVAL-ADTF3175D-NXZ module
-  ADTF3175 module
-  Phillips head screw driver
-  For some evaluation kits

   -  Soldering iron

Installation Steps
~~~~~~~~~~~~~~~~~~

-  Kit should be disconnected from power
-  Unscrew module cover from backplate

|image1| |image2|

-  **Carefully** unscrew module from backplate, keeping track of screw and spacers

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/unscrew-module.jpg
   :align: center
   :width: 400px

-  Pull up the module from backplate and disconnect the flex cable from the module. Leave the small aluminum blocks on the backplate

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/pullout-module.jpg
   :align: center
   :width: 400px

-  Kit should look like this with module removed

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/module_removed.jpg
   :align: center
   :width: 400px

-  Connect the new module to the flex. This can be done by carefully pulling out the flex cable.

|image3| |image4|

-  Place the spacers under the module

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/module-spacer-undermodule.jpg
   :align: center
   :width: 400px

-  Slowly screw the module down, cycling between each corner to ensure that the aluminum thermal conductors are seated correctly.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/unscrew-module.jpg
   :align: center
   :width: 400px

-  Pictures of module screwed down to backplate

|image5| |image6|

-  Screw the module cover to the backplate

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/module-cover.jpg
   :align: center
   :width: 400px

-  Connect the module to your pc and run FW Update to update ADSD3500 to latest revision: :doc:`eval-adtf3175d-nxz-upgrade-firmware </wiki-migration/resources/eval/user-guides/eval-adtf3175d-nxz-upgrade-firmware>`

   -  Please note that ADSD3500 fw version below 4.2.0.0 are not supported

-  Run 4.3.0+ Release software : ` <https://github.com/analogdevicesinc/ToF/releases/>`__

What to do if your module does not stream
-----------------------------------------

-  If you are able to connect to the camera (Log reads back adsd3500 firmware version) but unable start stream please try the following steps
-  Unscrew back cover of evaluation kit and check if R57 is populated. If the resistor is on your 068977 board please unsolder it\

|image7|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/module-cover.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/module-cover-unscrewed.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/module-flex-pulledout.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/module-flex-pullout-wmodule.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/module-rescrewed-side1.jpg
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/module-rescrewed-side2.jpg
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/r57_remove.png
   :width: 400px
