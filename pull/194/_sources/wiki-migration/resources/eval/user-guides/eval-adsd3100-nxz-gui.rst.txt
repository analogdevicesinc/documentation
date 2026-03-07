ADIToFGUI Eval Kit 5.0.0 or later
=================================

With Eval Kit software 5.0.0 there have been some major updates to ADIToFGUI, starting with the UX.

Usage
-----

Connecting
~~~~~~~~~~

1. Open ADIToFGUI located in the installation "bin" folder.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175d-nxz/adi-tof-nvidia-aditofgui-1.png
   :width: 600px

2. Select "config_adsd3500_adsd3100.json" -> Open

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175d-nxz/adi-tof-nvidia-aditofgui-2.png
   :width: 600px

3. Select the desired mode -> Play

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175d-nxz/adi-tof-nvidia-aditofgui-3.png
   :width: 600px

4. Streaming frames

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175d-nxz/adi-tof-nvidia-aditofgui-4.png
   :width: 600px

New Features
------------

Adjusting the Ini Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is now possible to adjust some of the configuration parameters during use. These parameters are generally stored in ini/JSON files are a per mode basis. The ADSD3500 and depth compute libraries receive the changed parameter values.

The **Ini Parameter** window can be selected at any point. Select **Ini Params** in the **Tools** menu.. To do so follow the image below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175d-nxz/adi-tof-aditofgui-ini-1.png
   :width: 300px

Once opened the **Ini Parameter** window can be use to adjust the parameter.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175d-nxz/adi-tof-aditofgui-ini-2.png
   :width: 600px

**Modify** is needed to write the parameters to the device. Please note, the stream is stopped, the ADSD3500 and depth compute library updated, then the stream is restarted.

**Reset** is used to set the values in the ADSD3500 and depth compute library back to those from the original ini file.

**Save** saves the parameters listed in the window to the a file.

Trouble Shooting
----------------

Slow Point Cloud Rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~

If rendering of the point cloud is slow, it may be necessary to ensure the GPU is rendering and not the CPU. With an NVIDIA GPU you can do the following.

1. NVIDIA Control Panel -> Manage 3D Settings -> Program Settings -> Add

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175d-nxz/adi-tof-nvidia-control_panel_1.png
   :width: 600px

2. Browse

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175d-nxz/adi-tof-nvidia-control_panel_2.png
   :width: 600px

3. Select the folder "C:\\Analog Devices\\TOF_Evaluation_ADTF3175D-Rel5.0.0\\bin" -> ADIToFGUI.exe -> Open

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175d-nxz/adi-tof-nvidia-control_panel_3.png
   :width: 600px

4. For the select program "ADIToFGUI" -> Select "High-performance NVIDIA processor" -> Apply

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175d-nxz/adi-tof-nvidia-control_panel_4.png
   :width: 600px

ADIToFGUI Eval Kit 4.3.0 or earlier
===================================

This is a guide for the ToF module viewer. This page applies to the viewer for the following modules:

-  :doc:`eval-adsd3100-nxz </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz>`
-  :doc:`eval-adtf3175-nxz </wiki-migration/resources/eval/user-guides/eval-adtf3175-nxz>`
-  :doc:`eval-adtf3175d-nxz </wiki-migration/resources/eval/user-guides/eval-adtf3175d-nxz>`

Start
-----

-  Find the ADIToFGUI.exe in the 'viewer' or 'bin' folder located at the install location

   -  v2.x.x

      -  Default location : C:\\Analog Devices\\TOF_Evaluation_BM-RelX.X.X\\viewer\\

   -  v3.x.x

      -  Default location : C:\\Analog Devices\\TOF_Evaluation_BM-RelX.X.X\\bin\\

-  If you are evaluating the **EVAL-ADTF3175D-NXZ**:

   -  Confirm that an unidentified local network has been discovered by the pc - IP address = 10.42.0.1
   -  Run TOF_Evaluation_BM-Relx.x.x
   -  Hit refresh until a Device is found
   -  **Select .json file based on your kits serial number** - Software Release version 4.2.0+

      -  If your serial number starts with 'DV11' or 'CR' select **tof-viewer_config.json**
      -  If your serial number starts with 'am' select **tof_crosby_adsd3500_new_modes_config.json**

-  If you are evaluating the following modules : **EVAL-ADTF3175-NXZ** or **EVAL-ADSD3100-NXZ** (only supported with software release 2.1.1)

   -  Start the viewer to get to the window below

      -  If a camera is connected it should show up in the 'Device' drop down menu
      -  Select your device
      -  Select correct config file (depends on which module you are using)

         -  :doc:`EVAL-ADTF3175-NXZ </wiki-migration/resources/eval/user-guides/eval-adtf3175-nxz>` : **tof-viewer-config-adtf3175.json**
         -  :doc:`EVAL-ADSD3100-NXZ </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz>` : **tof-viewer-config-adsd3100.json**

      -  Click 'Open Device'

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/selecting_config.png
   :align: center

Run Camera
----------

-  Once the device has been initialized the 'ToF Camera Options' menu should be available
-  Available modes will depend on the module serial number : :doc:`mode_table </wiki-migration/resources/eval/user-guides/eval-adtf3175d-nxz/mode_table>`
-  Select preferred view option (described below) and click play to run camera

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/gui_initialization_screen.png

.. important::

   If the user disconnects the camera via USB-C cable while the GUI has initialized the camera. The user must restart the GUI


Active Brightness and Depth
---------------------------

-  If this option is selected, the first window will show active brightness/intensity, while the second window will show depth
-  Depth is shown in mm, the user can hover over the image to see real-time depth data

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ab_and_depth.png
   :align: center

Mode Switching
--------------

-  If the user wants to switch modes while the camera is running frames:

   -  Click 'Stop'
   -  Select mode in drop down menu
   -  Click 'Play'

Point Cloud and Depth
---------------------

-  If camera is already running 'Active Brightness and Depth' viewer:

   -  Click 'Stop'
   -  Select 'Point Cloud and Depth'
   -  Click 'Play'

-  If this option is selected, the first window will show a point-cloud generated from the depth on the second window.
-  Point Cloud Controls:

   -  Zoom In/Out

      -  Use the mouse wheel and scroll forward to zoom in, scroll backwards to zoom out.

   -  Grab image and move it in all directions

      -  Hover over the Point Cloud Image and and drag the mouse while the right mouse button is pressed. Move slowly

   -  Rotate image

      -  Drage the mouse while pressing the left mouse button

   -  Increase / Decrease Point Cloud point size

      -  Grab the slider at the bottom of the Point Cloud window and move it left or right to decrease or increase the point size.

   -  Reset View

      -  Press the “Reset View” button to restore to default image size and position

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adtf3175_depth_pc.png

Recording
---------

-  Recording via the GUI is deprecated, please use :doc:`data_collect </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-gui/datacollect_cli>` for recording data during evaluation.

Troubleshooting
---------------

-  Visit :doc:`Troubleshooting Guide </wiki-migration/resources/eval/user-guides/aditofgui_ts>`
