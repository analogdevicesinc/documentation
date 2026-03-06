Analog Devices Precision Toolbox For MATLAB and Simulink
========================================================

ADI maintains a set of tools to interface with ADI precision converter devices within MATLAB and Simulink. These are combined into a single Toolbox. The list of supported converters is provided :doc:`below </wiki-migration/resources/tools-software/pcx-toolbox>`.

Quick Start with Toolbox
------------------------

The current stable Toolbox can be downloaded from `MathWorks File Exchange <https://www.mathworks.com/matlabcentral/fileexchange/125890-analog-devices-inc-precision-toolbox>`__.

Alternatively, the toolbox can also be installed using the .mltbx installer file from :git-PrecisionToolbox:`Precision Toolbox GitHub Release Page <releases>`. Download the latest .mltbx file then open that file within MATLAB. Opening the file will automatically install the Toolbox, adding the necessary components to your MATLAB path. The "Analog Devices, Inc. Precision Toolbox" will appear in your `Add-Ons Explorer <https://www.mathworks.com/help/matlab/matlab_env/manage-your-add-ons.html>`__ within MATLAB.

.. admonition:: Download
   :class: download

   
   -  :git-PrecisionToolbox:`Analog Devices Inc, Precision Toolbox Release Page <releases>`
   -  `Analog Devices Inc, Precision Toolbox - MathWorks File Exchange <https://www.mathworks.com/matlabcentral/fileexchange/125890-analog-devices-inc-precision-toolbox>`__
   


To interface and stream data with hardware will require installation of :doc:`libiio </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz/software/linux/applications/libiio>` and one of two Hardware Support Packages from MathWorks. The libiio library can be obtained on the `Github <http://github.com/analogdevicesinc/libiio>`__ page of the project.

Libiio Installers
~~~~~~~~~~~~~~~~~

.. admonition:: Download
   :class: download

   
   -  :git-libiio:`Installers and source for latest stable build <releases>`
   -  `Installer for latest nighty build (Windows 32-bit / 64-bit) <https://ci.appveyor.com/project/analogdevicesinc/libiio/build/artifacts?branch=master>`__ (may be unstable / buggy)
   


Installation of one of the following:

.. admonition:: Download
   :class: download

   
   -  `Communications Toolbox Support Package for Xilinx Zynq-Based Radio <https://www.mathworks.com/help/supportpkg/xilinxzynqbasedradio/index.html>`__
   -  `Communications Toolbox Support Package for Analog Devices ADALM-Pluto Radio <https://www.mathworks.com/help/supportpkg/plutoradio/index.html>`__
   


.. important::

   Skip the Zynq SDR or ADALM-PLUTO post-installation steps. They are not used. The FPGA carrier board SD card images are available on the :doc:`AD-FMC-SDCARD for Zynq & Altera SoC Quick Start Guide page </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`.


is required to use the streaming system objects or blocks. These support packages provide the necessary libIIO MATLAB bindings used by ADI's system objects.

Useful Articles
---------------

-  `Installation <https://analogdevicesinc.github.io/PrecisionToolbox/common/installation>`__
-  `Device control and streaming <https://analogdevicesinc.github.io/PrecisionToolbox/common/data_streaming>`__
-  `Supported hardware <https://analogdevicesinc.github.io/PrecisionToolbox>`__
-  `Known limitations <https://analogdevicesinc.github.io/PrecisionToolbox/common/limitations>`__
-  :git-PrecisionToolbox:`Examples <examples>`

Building the Toolbox Manually
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The toolbox can only be built under Linux or with Cygwin on a Windows platform. Conveniently, the entire process is automated with a Makefile located in the CI/scripts folder of the repository. The following is required on the system before the build process can be run:

-  A supported MATLAB version installed in the default location (/usr/local/MATLAB)
-  Packages: git zip unzip tar make wget sed

.. warning::

   You should only manually build the toolbox if you require a custom branch or no toolbox installer is available


First clone the repo and move into it:

::

   git clone https://github.com/analogdevicesinc/PrecisionToolbox.git
   cd PrecisionToolbox

To build the toolbox run the following:

::

   make -C CI/scripts build

To create an installable tlbx file run:

::

   make -C CI/scripts gen_tlbx

Supported Converters
--------------------

The following have device-specific implementations in MATLAB and Simulink. If a device has an IIO driver, MATLAB support is possible, but a device-specific MATLAB or Simulink interface may not exist yet.

+-----------------+------------+-------------------+-----------+----------------------------------------+
| Evaluation Card | FPGA Board | Streaming Support | Targeting | Variants and Minimum Supported Release |
+=================+============+===================+===========+========================================+
| AD7380          | Zedboard   | Yes               | No        | ADI (2018b) MathWorks (2021b)          |
+-----------------+------------+-------------------+-----------+----------------------------------------+
| AD7768          | Zedboard   | Yes               | No        | ADI (2018b) MathWorks (2021b)          |
+-----------------+------------+-------------------+-----------+----------------------------------------+
| AD7768-1        | Zedboard   | Yes               | No        | ADI (2018b) MathWorks (2021b)          |
+-----------------+------------+-------------------+-----------+----------------------------------------+
| AD4030-24       | Zedboard   | Yes               | No        | ADI (2018b) MathWorks (2021b)          |
+-----------------+------------+-------------------+-----------+----------------------------------------+
| AD4630-16       | Zedboard   | Yes               | No        | ADI (2018b) MathWorks (2021b)          |
+-----------------+------------+-------------------+-----------+----------------------------------------+
| AD4630-24       | Zedboard   | Yes               | No        | ADI (2018b) MathWorks (2021b)          |
+-----------------+------------+-------------------+-----------+----------------------------------------+
| AD4858          | Zedboard   | Yes               | No        | ADI (2018b) MathWorks (2021b)          |
+-----------------+------------+-------------------+-----------+----------------------------------------+

Help & Support
^^^^^^^^^^^^^^

.. hint::

   
   -  Questions? :ez:`Ask Help & Support <linux-device-drivers/linux-software-drivers>`.
   

