ADI vs MathWorks Support
========================

MATLAB and Simulink support is currently provided from ADI and through the MathWorks. However, implementations and board support will differ between these sources. Official MathWork support is for:

-  `ADALM-PLUTO <https://www.mathworks.com/hardware-support/adalm-pluto-radio.html>`_
-  `FMComms2/3/4 with Zedboard or ZC706 <https://www.mathworks.com/hardware-support/zynq-sdr.html>`_
-  `ADRV9361-Z7035 (PicoZed) with ADRV1CRR-FMC carrier <https://www.mathworks.com/hardware-support/zynq-sdr.html>`_.

ADI maintains support for all FMComms, ADALM-PLUTO, and ADRV board variants, as well as devices that support libiio. If your board has official support from MathWorks we would recommend starting with their implementations linked above.

ADI libiio Support
==================

IIO System Object
=================

.. warning::

   These interfaces are deprecated. Please use the :doc:`Transceiver Toolbox </wiki-migration/resources/tools-software/transceiver-toolbox>` or the :doc:`High Speed Converter Toolbox </wiki-migration/resources/tools-software/hsx-toolbox>`\


The **IIO System Object** is based on the `MATLAB System Objects™ <https://www.mathworks.com//help/matlab/matlab_prog/what-are-system-objects.html>`_ specification. It is designed to exchange data over Ethernet with an ADI hardware system connected to a FPGA/SoC platform running the ADI Linux distribution.

The **IIO System Object** is available in both MATLAB and Simulink:

-  By calling it from a MATLAB script, it can be used for HIL simulation of `MATLAB <https://www.mathworks.com/products/matlab/>`_ targeting different ADI platforms.
-  By incorporating it into a `MATLAB System Block <https://www.mathworks.com/help/simulink/ug/what-is-matlab-system-block.html>`_, it can be used for HIL simulation of `Simulink <https://www.mathworks.com/products/simulink/>`_ models targeting different ADI platforms.

The IIO System Object is built upon the :doc:`libiio library </wiki-migration/resources/tools-software/linux-software/libiio>` and enables a MATLAB or Simulink model to:

-  Stream data to and from a target
-  Control the settings of a target
-  Monitor different target parameters

Below is presented a top level diagram showing the architecture of a system.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/clients/sys_obj.png
   :alt: System architecture
   :width: 600px

For more information about System objects, please refer to the MathWorks documentation on how to do `Stream Processing in MATLAB <https://www.mathworks.com/discovery/stream-processing.html>`_.

Configuration File
------------------

The configuration file for a device has the .cfg extension and the name must match the device name set in the block's configuration dialog. It is a text file containing a set of fields that define the Linux drivers for the target device and the configuration channels that will be exposed by the Simulink block or MATLAB script. Entries in the configuration file can be commented by placing *#* at the begining of a line. The following entries can be found in a configuration file:

-  **data_in_device** - name of the Linux driver used for sending data to the device
-  **data_out_device** - name of the Linux driver used for reading data from the device
-  \**ctrl_device \*\* - name of the Linux driver used for controlling and monitoring the device
-  **channel** - defines a control/monitoring channel. A channel is defined by a sequence of parameters as follows *<channel name, channel type, Linux attribute, associated device>*

::

       * //channel name// - represents the name of the channel to be displayed on the corresponding Simulink block port
       * //channel type// - can be either IN or OUT
       * //Linux attribute// - the Linux attribute that will be called to set/get data for the channel
       * //associated device// - the device to which the Linux attribute is associated to. This parameter can have the values //'data_in_device'//, //'data_out_device'// or //'ctrl_device'//. The parameter is optional, if it isn't specified then it is implied to be //'ctrl_device'//.  

Below is presented a configuration file example for the AD9361.

::

   data_in_device = cf-ad9361-dds-core-lpc
   data_out_device = cf-ad9361-lpc
   ctrl_device = ad9361-phy
   channel = RX_LO_FREQ,IN,out_altvoltage0_RX_LO_frequency,
   channel = RX_SAMPLING_FREQ,IN,in_voltage_sampling_frequency,
   channel = RX_RF_BANDWIDTH,IN,in_voltage_rf_bandwidth,
   channel = RX1_GAIN_MODE,IN,in_voltage0_gain_control_mode,
   channel = RX1_GAIN,IN,in_voltage0_hardwaregain,
   channel = RX1_RSSI,OUT,in_voltage0_rssi,
   channel = RX2_GAIN_MODE,IN,in_voltage1_gain_control_mode,
   channel = RX2_GAIN,IN,in_voltage1_hardwaregain,
   channel = RX2_RSSI,OUT,in_voltage1_rssi,
   channel = TX_LO_FREQ,IN,out_altvoltage1_TX_LO_frequency,
   channel = TX_SAMPLING_FREQ,IN,out_voltage_sampling_frequency,
   channel = TX_RF_BANDWIDTH,IN,out_voltage_rf_bandwidth,

Property Dialog for Simulink
----------------------------

The input and output ports of the Simulink block corresponding to an IIO System Object are defined through the properties dialog of the object's block as well as through a configuration file that is specific to the targeted ADI device. The input and output ports are categorized as data and control ports. The data ports are used to receive/transmit buffers of continuous data from/to the target system in a frame based processing mode, while the control ports are used to configure and monitor different target system parameters. The number and size of the data ports are configured from the block's configuration dialog while the control ports are defined in the configuration file.

Below is presented an example of how an IIO System Object Simulink block looks like for the AD9361 device and what options can be configured from the block's properties dialog.

|AD9361 System Object| |Configuration Dialog|

The block's properties dialog contains the following parameters:

-  **IP address** - represents the IP address of the target platform. This can be found by typing “ifconfig” in a terminal on the Linux side
-  **Device name** - the name of the ADI device that block will communicate with. The name of the device determines the configuration file that will be associated with the block. The configuration file name and device name must be the same.
-  **Number of input data channels** - represents the number of input data ports that the block will have
-  **Input data channel size** - number of samples that an input data buffer will have
-  **Number of output data channels** - represents the number of output data ports that the block will have
-  **Output data channel size** - number of samples that an output data buffer will have

Downloads
=========

.. note::

   In order to use the IIO System Object, your `MATLAB <https://www.mathworks.com/products/matlab/>`_ license needs to include the following component:

   
   -  MATLAB (R2015a or higher version is required)
   
   If you would like to use it in Simulink, your `MATLAB <https://www.mathworks.com/products/matlab/>`_ license needs to include the following component:
   
   -  Simulink
   
   Besides, you need to have two things ready on your PC:
   
   -  Microsoft Visual C++ 2013 Redistributable
   -  A proper complier for your MATLAB. (For example, Microsoft Windows SDK is a good option.) And set it up using 'mex -setup' in the MATLAB command window.
   


Before using the IIO System Object, the **libiio** library must be installed in the system. The installer for Windows can be found here:

.. admonition:: Download
   :class: download

   **Windows libiio installer:**

   
   -  :git-libiio:`libiio Windows Installer <releases>` (the .exe file)
   
   **Libiio source code:**
   
   -  :git-libiio:`libiio source code <tree/2014_R2>`
   


The IIO System object source code and example models can be found here:

.. admonition:: Download
   :class: download

   
   -  :git-libiio-matlab>`__
   
      -  `iio_sys_obj.m <https::`IIO System Object </github.com/analogdevicesinc/libiio-matlab/blob/master/iio_sys_obj.m>` is for Simulink
      -  :git-libiio-matlab:`iio_sys_obj_matab.m <iio_sys_obj_matlab.m>` is for MATLAB
   
   -  :git-mathworks_tools:`Example models <hil_models>`
   


.. note::

   The example models need to have either the source code of the IIO system object copied to the folder where the model resides or to have the path to the IIO System Object source code added to the MATLAB path.


Setup
=====

In order to establish the connection between the host PC and the target, there are several steps you need to follow on both sides.

Target side:

#. Get the latest libiio library by following the :doc:`instructions </wiki-migration/resources/tools-software/linux-software/libiio>`.

PC side:

#. Run the Windows libiio installer provided in "Downloads" section, which will install all the dlls and dependencies on your PC.
#. Find out the IP address of the target by typing "ifconfig" in a terminal on the Linux side

   #. If used in MATLAB: Assign the IP address of the target to your object.
   #. If used in Simulink: Open the Simulink block and type the IP address of the target in the block. Please note even if the IP address in the System objects property window seems correct, it is a good idea to edit it and click 'Apply' to avoid any caching issues.

Next Generation System Objects
==============================

Starting with MATLAB R2018b, ADI is transitioning to a new system object infrastructure based on collaboration with MathWorks Inc. When installing the :doc:`latest board support package </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp>`, it also induces documentation.

.. |AD9361 System Object| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/clients/ad9361_sys_obj.png
   :width: 400px
.. |Configuration Dialog| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/clients/sys_obj_block_cfg.png
   :width: 250px


Data Streaming Example in MATLAB
================================

In this section, we will show an example of data streaming using MATLAB libiio. Download the example **ad9361_matlab.m** from GitHub and open it in MATLAB:

.. admonition:: Download
   :class: download

   :git-MathWorks_tools:`hil_models/legacy/fmcomms2_3_data_stream/ad9361_matlab.m`


In this example, *input* defines two sine waves (one for I channel, and the other for Q channel) streaming from MATLAB to target, as well as all the attributes of the device configuration channels. *output* is used to capture the streamed data from target, as well as to record all the attributes of the device monitoring channels, which is RSSI in this example.

There are two other parameters of the AD9361 you can set according to your modeling requirement:

-  Channel size: This is the number of samples buffered at the target before they are sent out together at each time. This number applies to both I and Q channels.
-  Number of data channels: This can be either 2 or 4. If it is 2, it will enable one IQ channel. Otherwise, it will enable two IQ channels.

Since we are streaming two sine waves to the target, we will also receive two sine waves back in MATLAB. This is what you should be able to get in the end:

.. image:: https://wiki.analog.com/_media/iio_matlabexample.png
   :alt: Block diagram

Besides the two sine waves in the plot, we also see the RSSI indicator for both channel 1 and channel 2 in the workspace.

Data Streaming Example in Simulink
==================================

Tx and Rx in One Block
----------------------

In this section, we will show an example of data streaming using Simulink libiio block. Download the Simulink model **ad9361_sim.slx** from GitHub and open the model from Simulink:

.. admonition:: Download
   :class: download

   :git-MathWorks_tools:`hil_models/legacy/fmcomms2_3_data_stream/ad9361_sim.slx`


In this model, DATA_IN1 to DATA_IN4 are four pins used to stream two sine waves (one for I channel, and the other for Q channel) from Simulink to target, and DATA_OUT1 to DATA_OUT4 are four pins used to observe the time-domain streamed data from target in a Time Scope, as highlighted below. The other pins all represent certain settings you can find from :doc:`ADI IIO Scope </wiki-migration/resources/tools-software/linux-software/fmcomms2_plugin>`.

.. image:: https://wiki.analog.com/_media/sinkmodel.png
   :alt: Block diagram
   :width: 600px

There are two other parameters of the Ad9361 Simulink block you can set according to your modeling requirement:

-  Channel size: This is the number of samples buffered at the target before they are sent out together at each time. This number applies to both I and Q channels.
-  Number of data channels: This can be either 2 or 4. If it is 2, it will enable one IQ channel. Otherwise, it will enable two IQ channels.

Make sure:

-  RX LO Frequency = TX LO Frequency
-  DDS Mode = DAC Buffer Output

Since we are streaming two sine waves to the target, we will also see two sine waves in the Time Scope. This is what you should be able to observe:

.. image:: https://wiki.analog.com/_media/iio_example2.png
   :alt: Block diagram
   :width: 800px

Besides the two sine waves in the Time Scope, we also see the RSSI indicator for both channel 1 and channel 2.

Separate Tx and Rx Blocks
-------------------------

In the example above, we use one block for both Tx and Rx settings. You also have the option to have Tx and Rx in two separate blocks. All you have to do is to provide two configuration (.cfg) files.

Download the Simulink model **ad9361_sim.slx** from GitHub and open the model from Simulink:

.. admonition:: Download
   :class: download

   :git-MathWorks_tools:`hil_models/legacy/fmcomms2_3_data_stream/ad9361_sim.slx`


In this Simulink model, you will find the Rx block on the top and the Tx block on the bottom, as shown below:

.. image:: https://wiki.analog.com/_media/TxandRx.png
   :alt: Block diagram
   :width: 600px

In this GitHub directory, along with the Simulink model, you will find two cfg files: ad9361_tx.cfg and ad9361_rx.cfg, which includes the attributes related to Tx and Rx.

Using these two cfg files and the two blocks provided in the Simulink model, you can now make an independent Tx model and an independent Rx model.
