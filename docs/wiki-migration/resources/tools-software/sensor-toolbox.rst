Analog Devices Sensor Toolbox For MATLAB and Simulink
=====================================================

ADI maintains a set of tools to model, interface, and target with ADI :adi:`Accelerometers <en/product-category/accelerometers.html>`, :adi:`Gyroscopes <en/product-category/gyroscopes.html>` and :adi:`Inertial Measurement Units <en/product-category/inertial-measurement-units.html>` devices within MATLAB and Simulink. These are combined into a single Toolbox which contains a set of Board Support Packages (BSP). The list of supported boards is provided :doc:`below </wiki-migration/resources/eval/user-guides/matlab_bsp>`.

Quick Start with Toolbox
------------------------

The current stable Toolbox can be downloaded from the :git-SensorToolbox:`Sensor Toolbox GitHub Release Page <releases>`. Download the latest mltbx file then open that file within MATLAB. Opening the file will automatically install the Toolbox, adding the necessary components to your MATLAB path. The "Analog Devices, Inc. Sensor Toolbox" will appear in your `Add-Ons Explore <https://www.mathworks.com/help/matlab/matlab_env/manage-your-add-ons.html>`__ within MATLAB.

.. admonition:: Download
   :class: download

   
   -  :git-SensorToolbox:`Analog Devices Inc, Sensor Toolbox Release Page <releases>`
   


To interface and stream data with hardware will require installation of :doc:`libiio </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz/software/linux/applications/libiio>` and one of two Hardware Support Packages from MathWorks. The libiio library can be obtained on the `Github <http://github.com/analogdevicesinc/libiio>`__ page of the project.

Libiio Installers
~~~~~~~~~~~~~~~~~

.. admonition:: Download
   :class: download

   
   -  :git-libiio:`Installers and source for latest stable build <releases>`
   -  `Installer for latest nighty build (Windows 32-bit / 64-bit) <https://ci.appveyor.com/project/analogdevicesinc/libiio/build/artifacts?branch=master>`__ (may be unstable / buggy)
   


Installation of either:

.. admonition:: Download
   :class: download

   
   -  `Communications Toolbox Support Package for Xilinx Zynq-Based Radio <https://www.mathworks.com/help/supportpkg/xilinxzynqbasedradio/index.html>`__
   -  `Communications Toolbox Support Package for Analog Devices ADALM-Pluto Radio <https://www.mathworks.com/help/supportpkg/plutoradio/index.html>`__
   


is required to use the streaming system objects or blocks. These support packages provide the necessary libIIO MATLAB bindings used by ADI's system objects.

Builds for the master branches are available as well if you want to use something newer:

Master Branch (Pre-release) Installer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download
   :class: download

   
   -  :git-SensorToolbox:`Sensor Toolbox Master Branch Installer README <README.md>`
   


Toolbox Dependencies
^^^^^^^^^^^^^^^^^^^^

Depending on your needs, different toolboxes will be required. For basic data streaming into MATLAB or Simulink only the following MathWorks toolboxes are required:

-  `Communications Toolbox <https://www.mathworks.com/products/communications/>`__
-  `DSP System Toolbox <https://www.mathworks.com/products/dsp-system/>`__
-  `Signal Processing Toolbox <https://www.mathworks.com/products/signal/>`__
-  `Communications Toolbox Support Package for Xilinx Zynq-Based (FREE) <https://www.mathworks.com/hardware-support/zynq-sdr.html>`__

Device Control and Data Streaming
---------------------------------

Device interfaces which provide control and data streaming are implemented with MATLAB System Objects and Simulink Blocks. These System Objects can be access under the "adi" namespace in MATLAB and are followed by their part number or board name:

::

   adi.<Part or Board Name>

For example, to instantiate an ADIS16460 object to control IMU it can be created as follows:

::

   imu = adi.ADIS16460;

For example usage of certain objects, it can be useful to inspect their related test code which exercises initiations in different configurations. The available code is available in the GitHub repo folder :git-SensorToolbox:`here <test>`, where object tests have the naming convention <Object>Tests.m.

To get a list of currently available objects with the BSP installed simply run:

::

   help adi

To get more information on a given object run:

::

   help adi.<Part of Board Name>

or

::

   doc adi.<Part of Board Name>

Common Attributes
^^^^^^^^^^^^^^^^^

There are some common attributes that need to be set for system objects and parts.

-  ``uri`` Context address of IIO device. Possible options include:

   -  IP with usage ''rx.uri = 'ip:192.168.2.1' ''
   -  USB with usage ''rx.uri = 'usb:1.2.3' ''

Extending Interfaces
^^^^^^^^^^^^^^^^^^^^

If a driver attribute or setting is not available in the standard objects it can be easily extended to cover more IIO attributes. See this :doc:`guide </wiki-migration/resources/eval/user-guides/matlab_bsp_extend>`.

Simulation Models of Hardware
-----------------------------

Supported Boards
----------------

The following have device-specific implementations in MATLAB and Simulink. If a device has an :doc:`Accelerometer </wiki-migration/resources/tools-software/linux-drivers-all>`, :doc:`Gyroscope </wiki-migration/resources/tools-software/linux-drivers-all>` or :doc:`IMU </wiki-migration/resources/tools-software/linux-drivers-all>` IIO driver, MATLAB support is possible, but a device-specific MATLAB or Simulink interface may not exist yet. Just ask on ` <https://ez.analog.com/sw-interface-tools/>`__.

+------------------------+-------------------+-----------+----------------------------------------+
| Evaluation Card        | Streaming Support | Targeting | Variants and Minimum Supported Release |
+========================+===================+===========+========================================+
| ADIS16375              | Yes               | No        | ADI (R2019b)                           |
+------------------------+-------------------+-----------+----------------------------------------+
| ADIS16460              | Yes               | No        | ADI (R2019b)                           |
+------------------------+-------------------+-----------+----------------------------------------+
| ADIS16480              | Yes               | No        | ADI (R2019b)                           |
+------------------------+-------------------+-----------+----------------------------------------+
| ADIS16485              | Yes               | No        | ADI (R2019b)                           |
+------------------------+-------------------+-----------+----------------------------------------+
| ADIS16488              | Yes               | No        | ADI (R2019b)                           |
+------------------------+-------------------+-----------+----------------------------------------+
| CN0549 (CN0540+CN0532) | Yes               | No        | ADI (R2020a)                           |
+------------------------+-------------------+-----------+----------------------------------------+

Examples
--------

Examples for streaming data are listed within the Toolbox documentation itself. To view run the following with MATLAB:

::

   doc adi

Help & Support
--------------

.. hint::

   
   -  Questions? :ez:`Ask Help & Support <linux-device-drivers/linux-software-drivers>`.
   

