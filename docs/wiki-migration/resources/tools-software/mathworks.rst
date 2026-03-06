MathWorks Support: MATLAB and Simulink Integrations
===================================================

.. image:: https://wiki.analog.com/_media/resources/tools-software/mlsl-12062018.jpg
   :align: center
   :width: 600px

Analog Devices, Inc. (ADI) works directly with MathWorks to provide tools and interfaces to end-users to help in their evaluation, development, and configuration of ADI hardware. This page outlines the different tools available for different products from ADI which can be used in different stages of a development cycle. For a complete list of supported boards see the :doc:`table here </wiki-migration/resources/tools-software/mathworks_supported_boards>`.

Simulation Models
=================

.. image:: https://wiki.analog.com/_media/resources/tools-software/simulation.png
   :align: center
   :width: 600px

Simulation models of hardware devices are available from MathWorks directly or from ADI. These are behavioral models of specific parts, and should not be considered transistor-level simulation. The models are typically used to understand device configuration, digital signal path frequency responses, and non-idealities. Since they are pure simulation models they can be integrated with other channels models and receiver/transmitter algorithms. Models are available in the following places:

-  :adi:`ADI authored behavioral models <en/design-center/simulation-models/mathworks-behavioral-models.html>`
-  :doc:`RF Transceiver Models </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/simrf>` `Download <https://www.mathworks.com/hardware-support/analog-devices-rf-transceivers.html>`__

Device Data Streaming and Configuration
=======================================

.. image:: https://wiki.analog.com/_media/resources/tools-software/dataflowmatlab.png
   :align: center
   :width: 1200px

For users looking to configure a device and stream data directly back into MATLAB or Simulink, there are two main options available. Both rely on the :doc:`libIIO </wiki-migration/resources/tools-software/linux-software/libiio>` user library and related IIO drivers. The first option are interfaces provided directly from MathWorks for the following devices and related toolboxes:

-  FMComms 2/3/4/5 and ADRV9361 RFSOM:`Zynq SDR Support from Communications Toolbox <https://www.mathworks.com/hardware-support/zynq-sdr.html>`__
-  ADALM-PLUTO: `ADALM-PLUTO Radio Support from Communications Toolbox <https://www.mathworks.com/hardware-support/adalm-pluto-radio.html>`__

If MathWorks does not support your current board or additional customization is required for a toolbox, ADI offers third-party open toolboxes which fills these gaps depending on your product category:

-  :doc:`Transceiver Toolbox </wiki-migration/resources/tools-software/transceiver-toolbox>`
-  :doc:`Sensor Toolbox </wiki-migration/resources/tools-software/sensor-toolbox>`
-  :doc:`High-Speed Converter Toolbox </wiki-migration/resources/tools-software/hsx-toolbox>`
-  :doc:`Time of Flight Toolbox </wiki-migration/resources/tools-software/tof-toolbox>`

Device-specific interfaces may not exist for all ADI products, but if a driver exists already adding support in MATLAB is a simple process. For a complete list of available drivers see :doc:`this page </wiki-migration/resources/tools-software/linux-drivers-all>`.

Code Generation and Targeting
=============================

.. image:: https://wiki.analog.com/_media/resources/tools-software/targeting.png
   :align: center
   :width: 1200px

When moving beyond simulation it becomes necessary to deploy algorithms onto embedded hardware. This can be done directly through the code generation tools from MathWorks, specifically HDL-Coder and Embedded-Coder. Since ADI has worked closely with MathWorks in these areas, a highly integrated workflow exists to move code from MATLAB scripts and Simulink models onto ADI systems, even without the need to go into compilers or synthesis tools directly. This is very attractive for algorithms engineers traditionally unseasoned in HDL, and makes their HDL engineering counterparts more productive.

MathWorks offers direct HDL and C++ targeting support in the following Hardware Support Packages:

-  FMComms 2/3/4/5 and ADRV9361 RFSOM:`Zynq SDR Support from Communications Toolbox <https://www.mathworks.com/hardware-support/zynq-sdr.html>`__
-  AD9361 based Ettus E310: `USRP® E310 Support from Communications Toolbox <https://www.mathworks.com/hardware-support/usrp-e310.html>`__

As part of the relevant toolboxes, ADI provides support for varies different FPGA and ADI part combinations:

-  :doc:`Transceiver Support Configurations </wiki-migration/resources/tools-software/transceiver-toolbox>`
-  :doc:`High Speed Converter Support Configurations </wiki-migration/resources/tools-software/hsx-toolbox>`

Support
=======

Support for the toolboxes is provided online at EngineerZone under the :ez:`Linux Software Drivers <linux-device-drivers/linux-software-drivers>` subforum.
