.. _libiio matlab_simulink:

IIO System Object
=================

.. note::

   These interfaces are deprecated. Please use the
   :ref:`Transceiver Toolbox <matlab transceiver-toolbox>` or the
   :ref:`High Speed Converter Toolbox <hsx-toolbox>`.

The IIO System Object is based on the
`MATLAB System Objects <https://www.mathworks.com/help/matlab/matlab_prog/what-are-system-objects.html>`__
specification. It is designed to exchange data over Ethernet with an ADI
hardware system connected to a FPGA/SoC platform running the ADI Linux
distribution.

.. image:: sys_obj.png

The IIO System Object enables a model to:

- Stream data to and from a target
- Control the settings of a target
- Monitor different target parameters

Configuration File
------------------

The IIO System Object requires a configuration file to know how to communicate
with the hardware platform. The configuration file uses the .cfg extension and
must reside in the same directory as the model. The name of the configuration
file must match the name of the device specified in the 'Device name' parameter
of the block property dialog.

Lines beginning with the '#' character are treated as comments and are ignored.
The other entries supported by the configuration file are:

- **data_in_device** - the name of the Linux driver used for transmitting data
  to the device
- **data_out_device** - the name of the Linux driver used for receiving data
  from the device
- **ctrl_device** - the name of the Linux driver used for controlling and
  monitoring the device
- **channel** - defines a control/monitoring channel

The following example is for the :adi:`AD9361` device.

.. code::

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

A channel definition contains the following parameters:

- **channel name** - determines how the channel will appear on the Simulink
  block port
- **channel type** - can be either IN or OUT
- **Linux attribute** - represents the Linux attribute that will be called to
  set or retrieve the channel data
- **associated device** - can be 'data_in_device', 'data_out_device', or
  'ctrl_device'. This parameter is optional. If not specified, it defaults to
  'ctrl_device'.

Property Dialog for Simulink
----------------------------

.. image:: ad9361_sys_obj.png

.. image:: sys_obj_block_cfg.png

- **IP address** - represents the IP address of the target platform
- **Device name** - determines the configuration file that will be associated
  with the block
- **Number of input data channels** - specifies the number of input data ports
- **Input data channel size** - specifies the number of samples that an input
  data buffer will have
- **Number of output data channels** - specifies the number of output data ports
- **Output data channel size** - specifies the number of samples that an output
  data buffer will have

Downloads
---------

The IIO System Object requires:

- MATLAB R2015a or higher for standalone usage
- Simulink for Simulink usage
- Microsoft Visual C++ 2013 Redistributable
- A proper compiler must be set up inside of MATLAB. Consult 'mex -setup' for
  information on setting up a compiler

Resources:

- `libiio Windows Installer <https://github.com/analogdevicesinc/libiio/releases>`__
  (the .exe file)
- `libiio source code <https://github.com/analogdevicesinc/libiio>`__
- `IIO System Object <https://github.com/analogdevicesinc/libiio-matlab>`__
  iio_sys_obj.m for Simulink, iio_sys_obj_matlab.m for MATLAB
- `Example models <https://github.com/analogdevicesinc/mathworks_tools/tree/master/hil_models>`__

Setup
-----

Target Setup
~~~~~~~~~~~~

Get the current libiio library per the instructions found here:
:ref:`libiio`.

PC Setup
~~~~~~~~

#. Install the libiio library for Windows.
#. Determine the IP address of the target. This can be found by running the
   'ifconfig' command on the target's terminal.
#. Insert the IP address in the iio_sys_obj_matlab.m file or in the property
   dialog of the IIO System Object block.
#. When using Simulink, make sure to write the IP address in the block and press
   'Apply' before running. The system is caching the IP address and it requires
   the user to input it and apply again for this caching to be done correctly.

Next Generation System Objects
------------------------------

Starting with MATLAB R2018b, ADI is moving toward a new common infrastructure
developed in close collaboration with MathWorks. Once the related board support
package has been installed, documentation should be available within MATLAB
documentation.
