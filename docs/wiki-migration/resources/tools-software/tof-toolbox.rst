Analog Devices Time of Flight Toolbox For MATLAB and Simulink
=============================================================

ADI maintains a set of tools to model, interface, and target with ADI time of flight devices within MATLAB and Simulink. These are combined into single Toolbox which contains a set of Board Support Packages (BSP). The list of supported boards is provided :doc:`below </wiki-migration/resources/tools-software/tof-toolbox>`.

Quick Start with Toolbox
------------------------

The current stable Toolbox can be downloaded from the :git-TimeofFlightToolbox:`Time of Flight Toolbox GitHub Release Page <releases>`. Download the latest mltbx file then open that file within MATLAB. Opening the file will automatically install the Toolbox, adding the necessary components to your MATLAB path. The "Analog Devices, Inc. Time of Flight Toolbox" will appear in your `Add-Ons Explore <https://www.mathworks.com/help/matlab/matlab_env/manage-your-add-ons.html>`_ within MATLAB.

.. admonition:: Download
   :class: download

   
   -  :git-TimeofFlightToolbox:`Analog Devices Inc, Time of Flight Toolbox Release Page <releases>`
   


Building the Toolbox Manually
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

   You should only manually build the toolbox if you require a custom branch or no toolbox installer is available


The toolbox can only be built under Windows platform currently with Cygwin. Conveniently, the entire process is automated with a Makefile located in the CI/scripts folder of the repository. The following is required on the system before the build process can be run:

-  Packages: git zip unzip tar make wget sed

First clone the repo and move into it:

::

   git clone https://github.com/analogdevicesinc/TimeofFlightToolbox.git
   cd TimeofFlightToolbox

To create a installable tlbx file run:

::

   make -C CI/scripts gen_tlbx

Device Control and Data Streaming
---------------------------------

Device interfaces which provide control and data streaming are implemented with MATLAB System Objects and traditional video adaptor object. The System Objects can be access under the "adi" namespace in MATLAB and are followed by their part number or board name:

::

   adi.<Part or Board Name>

For example, to instantiate an AD96TOF1EBZ object to control the Time of Flight it can be created as follows:

::

   tof = adi.AD96TOF1EBZ;

Alternatively, you can use the traditional image adaptor API by importing the adaptor manually:

::

   % Import adaptor with helper function
   imaqregister(adi.TOFAdaptor);
   % Create object with USB connection
   vid = videoinput('aditofadapter');

There are a number of examples included with the toolbox and :git-TimeofFlightToolbox:`available on github <tof_examples>`.

To get a list of currently available objects with the BSP installed simply run:

::

   help adi

To get more information on a given object run:

::

   help adi.<Part of Board Name>

Supported Boards
----------------

The following have device-specific implementations in MATLAB and Simulink. If a device has an IIO driver, MATLAB support is possible, but a device-specific MATLAB or Simulink interface may not exist yet.

+-----------------+--------------+-------------------+-----------+----------------------------------------+
| Evaluation Card | FPGA Board   | Streaming Support | Targeting | Variants and Minimum Supported Release |
+=================+==============+===================+===========+========================================+
| AD96TOF-EBZ     | Dragonboard  | Yes               | No        | ADI (2020a)                            |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
|                 | Raspberry Pi | Yes               | Yes       | ADI (2020a)                            |
+-----------------+--------------+-------------------+-----------+----------------------------------------+

Examples
--------

Examples for streaming data and targeting FPGAs are listed within the Toolbox documentation itself. To view run the following with MATLAB:

::

   doc adi

Help & Support
--------------

.. hint::

   
   -  Questions? :ez:`Ask Help & Support <sw-interface-tools/f/q-a>`.
   

