Using MATLAB With the DPG
=========================

This page describes using MATLAB with DPG2 and DPG3 pattern generators. For the ADS7 series of devices, see `Using MATLAB with ADS7 <https://wiki.analog.com/matlab-ads7>`_ for information and code samples.

MATLAB R2008b and Earlier
-------------------------

To begin, use the MATLAB command actxserver to connect to the DPG Software Suite.

For the DPG2, use:

.. code:: matlab

   >> h = actxserver('AnalogDevices.DPG2');

Most of the commands found in the `programming_reference <https://wiki.analog.com/programming_reference>`_ can then be used with the DPG. For example, the following code opens a DPG2, downloads an interleaved vector, and begins playback of the vector:

.. code:: matlab

   >> h = actxserver('AnalogDevices.DPG2');
   >> devices = h.AttachedDevices;
   >> devices{1}.DownloadConfiguration('LVDS (DCO)')
   >> devices{1}.DownloadInterleavedVectorDouble2D(vector,2,true);
   >> devices{1}.PlayMode=0
   >> dpg2devices{1}.StartPlayback;

.. hint::

   
   -  MATLAB always sends its data as a 2D array (matrix). Even if you only have one column of data, you will still need to use the "2D" download vector commands.
   -  The "Int" integer format referenced in the `programming_reference <https://wiki.analog.com/programming_reference>`_ is the same as the MATLAB data type int32. The "Double" data type is the same as MATLAB's type double. Most matrices in MATLAB are type double, unless specifically cast to a different data type.
   -  When setting the idle pattern, the SetPatternInt2D(int[,] pattern) method will need to be used. Setting the IdlePattern.Pattern property is not supported by MATLAB. The idle pattern will need to be an array (matrix) of type int32 (as opposed to the default of type double). An array x which is of type double can be converted to an integer array by the MATLAB command int32(x).
   -  Be aware of any vector length restrictions for the particular pattern generator you are communicating to. For example, the length of a vector on the DPG2 must be divisible by 256.
   -  The Interleaved commands take one vector and split it between the two output ports on the pattern generator. For single ports DACs which take interleaved data, you will need to interleave the channels before providing the data to the pattern generator.
   


Vector Downloading
~~~~~~~~~~~~~~~~~~

Because of the above restrictions with MATLAB, only the following DownloadVector commands are valid:

+---------------------+--------------------------------+-----------------------------------+
|                     | int32                          | double                            |
+=====================+================================+===================================+
| Independent Vectors | DownloadDataVectorInt2D        | DownloadDataVectorDouble2D        |
+---------------------+--------------------------------+-----------------------------------+
| Interleaved Vectors | DownloadInterleavedVectorInt2D | DownloadInterleavedVectorDouble2D |
+---------------------+--------------------------------+-----------------------------------+

MATLAB R2009a and Later
-----------------------

In versions of MATLAB starting with R2009a, a direct connection to the DPG libraries is now possible. To begin, follow these steps:

Connect to the top-level DPG library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: matlab

   >> NET.addAssembly('AnalogDevices.DPG.Interfaces');
   >> hpf = AnalogDevices.DPG.PluginFinder.HardwarePluginFinder;
   >> hardwarePlugins = hpf.FindPlugins;

The array *hardwarePlugins* now contains a list of all the hardware interfaces that you currently can connect to. The number of available interfaces will vary depending on what you have installed. For example, you may have the DPG2 Interface, and a DPGI/O Interface, and possibly others. These interfaces are software interfaces. They represent the different types of hardware you could connect to, if that hardware was connected to your computer. The interfaces will show up regardless of if the hardware is connected or not. To get a description of each interface, the *FriendlyName* function can be called:

.. code:: matlab

   >> hardwarePlugins(1).FriendlyName
   ans = 
   DPG2 Interface

This example will connect to a DPG2:

.. code:: matlab

   >> dpg2_interface = hardwarePlugins(1);

.. hint::

   The index of *hardwarePlugins* corresponding to a particular hardware type could change if you ever update your DAC Software Suite. It is advisable to select the index of the *hardwarePlugins* array by querying the *FriendlyName* and selecting the one that has the correct name.


Connect to a specific device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now you can query the interface to see if any hardware of this type (in this case, a DPG2) is actually connected:

.. code:: matlab

   >> devices = dpg2_interface.AttachedDevices;

The *devices* array now contains a reference to each physically attached pattern generator of the specified type (DPG2 in this example). We'll create a reference to the first device, to make the code afterwards cleaner:

.. code:: matlab

   >> dpg2 = devices(1);

Configure the pattern generator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The FPGA in the pattern generator can be setup for several different interface standards. Select the appropriate configuration for the evaluation board connected to the pattern generator, and configure the FPGA. In this example, an LVDS interface will be used:

.. code:: matlab

   >> dpg2.DownloadConfiguration('LVDS (DCO)')

Load a vector into the pattern generator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first step in loading a vector into a pattern generator is to convert the MATLAB array into a format recognizable by the DPG software:

.. code:: matlab

   >> dpg_array = NET.convertArray(original_array, 'System.Int32');

The new array can now be loaded into the pattern generator. There are numerous ways to load in the data (see the `programming_reference <https://wiki.analog.com/programming_reference>`_ for the complete list). This example will load for a dual-port single DAC, such as the AD9739:

.. code:: matlab

   >> dpg2.DownloadInterleavedVectorInt1D(dpg_array,2,true);

Once the vector is loaded, the Play Mode should be set to Loop, followed by the command to begin vector playback:

.. code:: matlab

   >> dpg2.PlayMode = AnalogDevices.DPG.Interfaces.HardwareDeviceTypes.PlayModeE.Loop;
   >> dpg2.StartPlayback;

Formatting the input data
~~~~~~~~~~~~~~~~~~~~~~~~~

How the data is formatted in *original_array* will vary depending on what DAC the data is being sent to. The data itself is not interpreted by the download functions (bits in = bits out). Therefore, the data format (binary, two's compliment, etc) must match what the DAC is expecting.

The DPG has two LVDS buses, which become interleaved into one vector. The data must be inserted into the data array properly for it to be de-interleaved by the DPG.

For example, on an AD9739 (dual-port, single DAC), the data would look like this:

+----------+


| Sample 1 |

+----------+

| Sample 2 |

+----------+

| Sample 3 |

+----------+

| Sample 4 |

+----------+

| etc.     |

+----------+

On the AD9122 (dual DAC, single port), the data would look like:

+------------+


| I Sample 1 |

+------------+

| 0          |

+------------+

| Q Sample 1 |

+------------+

| 0          |

+------------+

| I Sample 2 |

+------------+

| 0          |

+------------+

| Q Sample 2 |

+------------+

| 0          |

+------------+

Complete Code for Loading Vector into DPG2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: matlab

   % The first section is setting up the pattern generator
   NET.addAssembly('AnalogDevices.DPG.Interfaces');
   hpf = AnalogDevices.DPG.PluginFinder.HardwarePluginFinder;
   hardwarePlugins = hpf.FindPlugins;
   for i=1:hardwarePlugins.Length
       if(strcmp(char(hardwarePlugins(i).FriendlyName),'DPG2 Interface') == true)
           dpg2_interface = hardwarePlugins(i);
       end
   end
   devices = dpg2_interface.AttachedDevices;
   dpg2 = devices(1);
   dpg2.DownloadConfiguration('LVDS (DCO)');

   % This section would be repeated for loading in different vectors
   dpg_array = NET.convertArray(original_array, 'System.Int32');
   dpg2.DownloadInterleavedVectorInt1D(dpg_array,2,true);
   dpg2.PlayMode = AnalogDevices.DPG.Interfaces.HardwareDeviceTypes.PlayModeE.Loop;
   dpg2.StartPlayback;

Creating Data Files
-------------------

Sometimes it is advantageous to create a data file in MATLAB, save it to a file, and then download it with DPGDownloader. This example creates a :doc:`Data File </wiki-migration/resources/eval/dpg/dpgdownloader>` for use with :doc:`DPGDownloader </wiki-migration/resources/eval/dpg/dpgdownloader>`.

.. code:: matlab

   % Signed Example
   resolution = 16;
   desired = 1000000;  % Output frequency in Hz
   FDAC = 10000000;    % Data clock frequency in Hz
   samples = 65536;    % Must be a multiple of 256
   cycles=round(desired\*samples/FDAC);
   actual=cycles\*FDAC/samples
   x=[0:(2\*cycles\*pi/samples):2\*cycles\*pi-(2\*cycles\*pi/samples)];
   Idata = round((2^(resolution-1)-1)*cos(x))';  % I data is a cosine wave
   Qdata = round((2^(resolution-1)-1)*sin(x))';  % Q data is a sine wave
   dlmwrite('QVector.txt', Qdata)
   dlmwrite('IVector.txt', Idata)
