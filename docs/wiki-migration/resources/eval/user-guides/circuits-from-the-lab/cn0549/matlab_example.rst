Streaming Data from the CN0549 into MATLAB
==========================================

This page is going to discuss how to use the :adi:`CN0549` Machine Learning Enablement Platform for streaming high fidelity analog sensor data from a device under test (DUT), into MATLAB for data analysis. The goal is that once you have the data in these tools, you'll be able to create your own algorithms and train your system using your own data.

This page will outline how to get the data from the sensor all the way to MATLAB, using open-source hardware and software from Analog Devices. At the end of this page, links will also be provided to specific examples done in MATLAB, where you can recreate each example using the training data and scripts provided.

Requirements
------------

.. important::

   This user guide page assumes that you have the complete CN0549 system put together. This includes both hardware and software setup. If you have not completed this step, please refer back to the :doc:`CN0549 user guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0549>` on how to get setup.


Hardware:

-  Ethernet Cable
-  Router or network connection
-  Mini USB to USB type A cable
-  PC or Laptop

Software:

-  `MATLAB 2020a+ <https://www.mathworks.com/products/matlab.html>`__
-  `Download libiio <https://github.com/analogdevicesinc/libiio>`__
-  :doc:`ADI Sensor Toolbox </wiki-migration/resources/tools-software/sensor-toolbox>`

   -  *Note this toolbox has other dependent toolboxes from MathWorks*

Preparing your PC/Laptop
~~~~~~~~~~~~~~~~~~~~~~~~

-  Install MATLAB onto your laptop
-  Install libiio onto your laptop
-  :doc:`Install the ADI Sensor Toolbox from GitHub </wiki-migration/resources/tools-software/sensor-toolbox>` or directly from within MATLAB using `Add-On explorer <https://www.mathworks.com/products/matlab/add-on-explorer.html>`__ by searching for the Analog Devices Sensor Toolbox

System Setup
------------

-  Ensure your CN0549 System is connected together. If you need to setup the CN0549, please refer back to the :doc:`user guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0549>`.

.. tip::

   
   The user guide shows the USB OTG connector and the HDMI cable installed, but those two steps will not be needed here since we are streaming data over the network into the laptop.


-  Connect one end of the Ethernet cable into the DE10-Nano, and the other end of the Ethernet cable into a router or other network connection.
-  Plug the mini USB cable into the UART connector of the DE10-Nano.
-  Plug in the USB cable(from the UART of DE10-Nano) into your PC's USB port.

   -  A driver for the board should automatically be detected and installed on your PC. If this does not happen you may have to manually install that driver in order to continue. Here is a link to the `UART Serial Driver <https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers>`__

-  Plug the power supply into the wall outlet and use the DC barrel jack to power up the CN0549 setup.

System Block Diagram
~~~~~~~~~~~~~~~~~~~~

PPT picture of high level block diagram for the hardware and software

Finding your DE10-Nano
~~~~~~~~~~~~~~~~~~~~~~

Before you can start gathering data, you first must locate the CN0549 system setup on your network.

-  Setup a UART serial communication between your PC and the DE10-Nano board using the micro USB cable to USB type A
-  Using your device manager, locate the COM port assigned to the DE10-Nano board\

|image1|

-  Open Putty, Tera Term, or other serial terminal program and open a terminal between the COM port the DE10-Nano board by setting the Baud rate to 115200, and connect.
-  You'll now be prompted to provide a user name and password.

.. note::

   
   | For Analog Devices Kuiper Linux
   | Username = **analog** and Password = **analog**.
   | Press the Enter key between each.


-  Type **ifconfig** into the terminal, hit "Enter"
-  That should echo back some information where you can pull out the inet address of eth0.\

|image2|

.. _system-block-diagram-1:

System Block Diagram
~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/cn0549_matlab_generic_sw_blk_dig.png
   :align: center
   :width: 1200px

Connecting to the CN0549 via MATLAB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With your system fully setup, it's now time to stream data directly into MATLAB.

Data streaming and device control are provided through the specialized classes called `MATLAB system objects <https://www.mathworks.com/help/matlab/matlab_prog/what-are-system-objects.html>`__ in :doc:`ADI's Sensor Toolbox </wiki-migration/resources/tools-software/sensor-toolbox>`. Devices or sensors which connect through the CN0540, such as the CN0549, will share a common base class called :git-SensorToolbox:`adi.CN0540Base.m <%2Badi/CN0540Base.m>`. However, each specific sensor will have its own class that will contain documentation, methods, and properties specific to it. Therefore, end-users should always use the python class associated with the sensor and not the CN0540.

Below is a basic example where we will talk to a CN0540 with CN0549 attached. This is done remotely from a host PC, but can be done locally on the board or through another backend. See the :doc:`libiio doc for more information </wiki-migration/resources/tools-software/linux-software/libiio>`. This example can be downloaded from :git-SensorToolbox:`GitHub directly <sensor_examples/cn0549.m>`.

.. code:: matlab

   %% Configure device for initialization
   xl = adi.CN0532();
   xl.uri = uri;
   xl.SampleRate = '16000';
   xl.SamplesPerRead = 2^14;
   xl.FDAMode = 'FullPower';
   xl.ShiftVoltageMV = 4240;
   %% Collect data
   data = xl();
   %% Plot data
   ts = 1/str2double(xl.SampleRate);
   t = 0:ts:(length(data)-1)*ts;
   plot(t,data);
   xlabel('Time (s)');ylabel('ADC Codes');grid on;
   ylim([min(data)-abs(min(data)*0.01) max(data)+abs(max(data)*0.01)]);

Once run the return data ``data`` will be an array of 32-bit integers of shape ``(2^12,1)``. These are ADC codes as captured from the CN0540 board connected to the CN0532 sensor board.

For further details about ADI's Sensor Toolbox consult the doc available directly in the toolbox, or look at more examples in the :git-SensorToolbox:`sensor_examples folder <sensor_examples>`.

Machine Learning Examples
-------------------------

*End of Document*

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/com_port.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/serial_terminal_linux_ifconfig_inet.png
   :width: 600px
