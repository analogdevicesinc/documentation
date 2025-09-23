.. _hsx-toolbox:

High Speed Converter Toolbox
============================

.. note::

   This section only gives an overview on the High Speed Converter Toolbox,
   for all details, see
   `the dedicated doc <https://analogdevicesinc.github.io/HighSpeedConverterToolbox/master>`__.

Analog Devices High Speed Converter Toolbox for MATLAB and Simulink is a
set of tools to model, interface, and target with ADI high-speed
converter devices within MATLAB and Simulink. These are combined into single
Toolbox which contains a set of Board Support Packages (BSP). The list of
supported boards is provided
:dokuwiki:`here <resources/eval/user-guides/matlab_bsp#supported_boards>`.

Quick Start with Toolbox
------------------------

The current stable Toolbox can be downloaded from the
:git-HighSpeedConverterToolbox:`releases+`.
Download the latest mltbx file then open that file within MATLAB. Opening the
file will automatically install the Toolbox, adding the necessary components to
your MATLAB path. The "Analog Devices, Inc. High Speed Converter Toolbox" will
appear in your :mw:`Add-Ons Explore <help/matlab/matlab_env/manage-your-add-ons.html>`
within MATLAB.

.. admonition:: Download

   :git-HighSpeedConverterToolbox:`releases+`.

To interface and stream data with hardware will require installation of :ref:`libiio`
and one of two Hardware Support Packages from MathWorks.
The libiio library can be obtained on :git-libiio:`/` page
of the project.

Libiio Installer
~~~~~~~~~~~~~~~~

.. admonition:: Download

   Stable releases are available at :git-libiio:`releases+`.


.. admonition:: Download

   | Installation of either:
   | :mw:`Communications Toolbox Support Package for Xilinx Zynq-Based Radio <help/supportpkg/xilinxzynqbasedradio/index.html>`
   | :mw:`Communications Toolbox Support Package for Analog Devices ADALM-Pluto Radio <help/supportpkg/plutoradio/index.html>`

.. important::

   Skip the Zynq SDR or ADALM-PLUTO post-installation steps. They
   are not used.
   The FPGA carrier board SD card images are available on :external+adi-kuiper-gen:doc:`use-kuiper-image`.

is required to use the streaming system objects or blocks. These support
packages provide the necessary libIIO MATLAB bindings used by ADI's system
objects.

Useful Articles
---------------

-  `Installation <https://analogdevicesinc.github.io/HighSpeedConverterToolbox/master/install/>`__
-  `Device control and streaming <https://analogdevicesinc.github.io/HighSpeedConverterToolbox/master/streaming/>`__
-  `HDL targeting <https://analogdevicesinc.github.io/HighSpeedConverterToolbox/master/targeting/>`__
-  `Behavioral simulations <https://analogdevicesinc.github.io/HighSpeedConverterToolbox/master/models/>`__
-  `Supported hardware <https://analogdevicesinc.github.io/HighSpeedConverterToolbox/master/>`__
-  :ref:`matlab bsp-extend`.

Building the Toolbox Manually
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The toolbox can only be built under Linux or with Cygwin on a Windows platform.
Conveniently, the entire process is automated with a Makefile located in the
CI/scripts folder of the repository. The following is required on the system
before the build process can be run:

-  A supported MATLAB version installed in the default location
   (*/usr/local/MATLAB*)
-  A supported Vivado version installed in the default location
   (*/opt/Xilinx*)
-  Packages: ``git`` ``zip`` ``unzip`` ``tar`` ``make`` ``wget`` ``sed``

.. warning::

   You should only manually build the toolbox if you require a custom
   branch or no toolbox installer is available.

First clone the repo and move into it:

.. shell::

   $git clone https://github.com/analogdevicesinc/HighSpeedConverterToolbox.git
   $cd HighSpeedConverterToolbox

To build the toolbox run the following:

.. shell::

   ~/HighSpeedConverterToolbox
   $make -C CI/scripts build

To create an installable ``tlbx`` file run:

.. shell::

   ~/HighSpeedConverterToolbox
   $make -C CI/scripts gen_tlbx

Further Reading
^^^^^^^^^^^^^^^

:adi:`Four Quick Steps to Production: Using Model-Based Design for Software-Defined Radio - Part 4 <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

Help & Support
~~~~~~~~~~~~~~

Questions? :ez:`Ask Help & Support <linux-device-drivers/linux-software-drivers>`.
