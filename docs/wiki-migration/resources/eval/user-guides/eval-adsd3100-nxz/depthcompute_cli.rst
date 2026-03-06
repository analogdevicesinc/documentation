Depth Compute Command Line Interface (CLI)
==========================================

.. important::

   This tool has been removed from the host starting with Eval Kit version **5.0.0**.


Description
-----------

The Depth Compute CLI can take data gathered from the :doc:`Data Collect CLI </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-gui/datacollect_cli>`, and compute Depth, IR/Active Brightness, and XYZ frames.

-  The ``RadialDepth`` folder contains depth images where the depth at each pixel is the distance to the corresponding point in the scene measured "radially" from the center of the lens
-  The ``AB`` folder contains Active Brightness images where the value at each pixel is the intensity of the return laser light from the corresponding point in the scene (IR frame)
-  The ``XYZ`` folder contains point cloud images where the values at each pixel are the real world cartesian coordinates (X,Y,Z) of the corresponding point in the scene. The Z image can be used standalone as an image where the value of each pixel is the distance to the corresponding point in the scene measured from the plane of the camera.

EVAL-ADSD3100-NXZ and EVAL-ADTF3175-NXZ Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Run :doc:`Data Collect </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-gui/datacollect_cli>` first
-  In command prompt move to bin folder in GUI install location
-  Run the following command : ``tofi_compute_depth.exe --I=../data_output --CCB=../crXXX.ccb --MODE=10 --O=../proc_data --INI=../config/RawToDepth.ini``

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adsd3100-nxz/run_depthcompute.png
   :align: center
   :width: 800px

-  Processed Data is stored in proc_data folder - Please refer to python scripts in depth_compute folder for visualization examples

EVAL-ADTF3175D-NXZ Example
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Run :doc:`Data Collect </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-gui/datacollect_cli>` first
-  In command prompt move to bin folder in GUI install location
-  Run either one of the following commands, depending on mode of data collected - (**Please check correct mode number and ini file for your module here :** :doc:`mode_table </wiki-migration/resources/eval/user-guides/eval-adtf3175d-nxz/mode_table>`)

   -  MP mode : ``tofi_compute_depth.exe --I=data_output --CCB=../XXX.ccb --MODE=1 --O=proc_data_mp --INI=../config/RawToDepthAdsd3500_lr-native.ini --ISP_Enable=1``
   -  QMP mode : ``tofi_compute_depth.exe --I=data_output_qmp --CCB=../XXX.ccb --MODE=1 --O=proc_data_qmp --INI=../config/RawToDepthAdsd3500_lr-native.ini --ISP_Enable=1``

-  Processed Data is stored in proc_data folder - Please refer to python scripts in depth_compute folder for visualization examples

Processing the outputs
~~~~~~~~~~~~~~~~~~~~~~

If you followed the above steps and are running this from the installer then the following commands should work.

-  ``cd path/of/tofi_compute_depth.exe``

Visualize Depth

-  ``python tools\depth_compute\visualize_depth.py proc_data_mp\RadialDepth\data_output_0.bin 1024 1024``

Vizualize AB

-  ``python tools\depth_compute\visualize_ab.py proc_data_mp\AB\data_output_0.bin 1024 1024``

Vizualize Pointcloud

-  ``python tools\depth_compute\visualize_pointcloud.py 1024 1024 proc_data_mp\XYZ\data_output_0.bin``
