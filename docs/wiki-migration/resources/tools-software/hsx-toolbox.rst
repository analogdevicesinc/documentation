Analog Devices High Speed Converter Toolbox for MATLAB and Simulink
===================================================================

ADI maintains a set of tools to model, interface, and target with ADI high-speed converter devices within MATLAB and Simulink. These are combined into single Toolbox which contains a set of Board Support Packages (BSP). The list of supported boards is provided :doc:`below </wiki-migration/resources/eval/user-guides/matlab_bsp>`.

Quick Start with Toolbox
------------------------

The current stable Toolbox can be downloaded from the :git-HighSpeedConverterToolbox:`High Speed Converter Toolbox GitHub Release Page <releases>`. Download the latest mltbx file then open that file within MATLAB. Opening the file will automatically install the Toolbox, adding the necessary components to your MATLAB path. The "Analog Devices, Inc. High Speed Converter Toolbox" will appear in your `Add-Ons Explore <https://www.mathworks.com/help/matlab/matlab_env/manage-your-add-ons.html>`__ within MATLAB.

.. admonition:: Download
   :class: download

   
   -  :git-HighSpeedConverterToolbox:`Analog Devices Inc, High Speed Converter Toolbox Release Page <releases>`
   


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
   


.. important::

   Skip the Zynq SDR or ADALM-PLUTO post-installation steps. They are not used. The FPGA carrier board SD card images are available on the :doc:`AD-FMC-SDCARD for Zynq & Altera SoC Quick Start Guide page </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`.


is required to use the streaming system objects or blocks. These support packages provide the necessary libIIO MATLAB bindings used by ADI's system objects.

Useful Articles
---------------

-  `Installation <https://analogdevicesinc.github.io/HighSpeedConverterToolbox/master/install/>`__
-  `Device control and streaming <https://analogdevicesinc.github.io/HighSpeedConverterToolbox/master/streaming/>`__
-  `HDL targeting <https://analogdevicesinc.github.io/HighSpeedConverterToolbox/master/targeting/>`__
-  `Behavioral simulations <https://analogdevicesinc.github.io/HighSpeedConverterToolbox/master/models/>`__
-  `Supported hardware <https://analogdevicesinc.github.io/HighSpeedConverterToolbox/master/>`__
-  :doc:`Extending the MATLAB interface for more hardware controls </wiki-migration/resources/eval/user-guides/matlab_bsp_extend>`

Building the Toolbox Manually
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The toolbox can only be built under Linux or with Cygwin on a Windows platform. Conveniently, the entire process is automated with a Makefile located in the CI/scripts folder of the repository. The following is required on the system before the build process can be run:

-  A supported MATLAB version installed in the default location (/usr/local/MATLAB)
-  A supported Vivado version installed in the default location (/opt/Xilinx)
-  Packages: git zip unzip tar make wget sed

.. warning::

   You should only manually build the toolbox if you require a custom branch or no toolbox installer is available


First clone the repo and move into it:

::

   git clone https://github.com/analogdevicesinc/HighSpeedConverterToolbox.git
   cd HighSpeedConverterToolbox

To build the toolbox run the following:

::

   make -C CI/scripts build

To create an installable tlbx file run:

::

   make -C CI/scripts gen_tlbx

Further Reading
~~~~~~~~~~~~~~~

:adi:`Four Quick Steps to Production: Using Model-Based Design for Software-Defined Radio - Part 4 <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

Help & Support
^^^^^^^^^^^^^^

.. hint::

   
   -  Questions? :ez:`Ask Help & Support <linux-device-drivers/linux-software-drivers>`.
   

