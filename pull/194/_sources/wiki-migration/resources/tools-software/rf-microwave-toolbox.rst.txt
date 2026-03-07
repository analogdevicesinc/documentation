Analog Devices RF Microwave Toolbox For MATLAB and Simulink
===========================================================

ADI maintains a set of tools to interface with ADI RF and microwave devices within MATLAB and Simulink. These are combined into single Toolbox which contains a set of Board Support Packages (BSP). The list of supported boards is provided :doc:`below </wiki-migration/resources/eval/user-guides/matlab_bsp>`.

Quick Start with Toolbox
------------------------

The current stable Toolbox can be downloaded from the :git-RFMicrowaveToolbox:`RF Microwave Toolbox GitHub Release Page <releases>`. Download the latest mltbx file then open that file within MATLAB. Opening the file will automatically install the Toolbox, adding the necessary components to your MATLAB path. The "Analog Devices, Inc. RF Microwave Toolbox" will appear in your `Add-Ons Explore <https://www.mathworks.com/help/matlab/matlab_env/manage-your-add-ons.html>`_ within MATLAB.

.. admonition:: Download
   :class: download

   
   -  :git-RFMicrowaveToolbox:`Analog Devices Inc, RF Microwave Toolbox Release Page <releases>`
   


To interface and stream data with hardware will require installation of :doc:`libiio </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz/software/linux/applications/libiio>` and one of two Hardware Support Packages from MathWorks. The libiio library can be obtained on the `Github <http://github.com/analogdevicesinc/libiio>`_ page of the project.

Libiio Installers
~~~~~~~~~~~~~~~~~

.. admonition:: Download
   :class: download

   
   -  :git-libiio:`Installers and source for latest stable build <releases>`
   -  `Installer for latest nighty build (Windows 32-bit / 64-bit) <https://ci.appveyor.com/project/analogdevicesinc/libiio/build/artifacts?branch=master>`_ (may be unstable / buggy)
   


Installation of either:

.. admonition:: Download
   :class: download

   
   -  `Communications Toolbox Support Package for Xilinx Zynq-Based Radio <https://www.mathworks.com/help/supportpkg/xilinxzynqbasedradio/index.html>`_
   -  `Communications Toolbox Support Package for Analog Devices ADALM-Pluto Radio <https://www.mathworks.com/help/supportpkg/plutoradio/index.html>`_
   


.. important::

   Skip the Zynq SDR or ADALM-PLUTO post-installation steps. They are not used. The FPGA carrier board SD card images are available on the :doc:`AD-FMC-SDCARD for Zynq & Altera SoC Quick Start Guide page </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`.


is required to use the streaming system objects or blocks. These support packages provide the necessary libIIO MATLAB bindings used by ADI's system objects.

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

   git clone https://github.com/analogdevicesinc/RFMicrowaveToolbox.git
   cd RFMicrowaveToolbox

To build the toolbox run the following:

::

   make -C CI/scripts build

To create a installable tlbx file run:

::

   make -C CI/scripts gen_tlbx

Device Control and Data Streaming
---------------------------------

Device interfaces which provide control and data streaming are implemented with MATLAB System Objects and Simulink Blocks. These System Objects can be access under the "adi" namespace in MATLAB and are followed by their part number or board name and finally Tx or Rx:

::

   adi.<Part or Board Name>.<Tx or Rx>

For example, to instantiate a Stingray object to control the X-Band Development Platform it can be created as follows:

::

   bf = adi.Stingray;

The Stingray Evaluation board contains an ADXUD1AEBZ, ADF4371 and LTC2314. Therefore, it uses the objects corresponding to these devices along with ADAR100x, a genric ADAR1000 superclass under the hood. Similarly, ADALM-PHASER class is also derived from low level objects based on their parts.

For example usage of certain objects, it can be useful to inspect their related test code which exercises initiations in different configurations. The available code is available in the GitHub repo folder :git-RFMicrowaveToolbox:`here <test>`, where object tests have the naming convention <Object>Tests.m.

To get a list of currently available objects with the BSP installed simply run:

::

   help adi

To get more information on a given object run:

::

   help adi.<Part or Board Name>

or

::

   doc adi.<Part or Board Name>

Common Attributes
~~~~~~~~~~~~~~~~~

There are some common attributes that need to be set for system objects and parts.

-  ``uri`` Context address of IIO device.

   -  IP with usage ''bf.uri = 'ip:192.168.2.1' ''

Extending Interfaces
~~~~~~~~~~~~~~~~~~~~

If a driver attribute or setting is not available in the standard objects it can be easily extended to cover more IIO attributes. See this :doc:`guide </wiki-migration/resources/eval/user-guides/matlab_bsp_extend>`.

Examples
--------

Examples for streaming data and targeting FPGAs are listed within the Toolbox documentation itself. To view run the following with MATLAB:

::

   doc adi

Help & Support
--------------

.. hint::

   
   -  Questions? :ez:`Ask Help & Support <sw-interface-tools>`.
   

