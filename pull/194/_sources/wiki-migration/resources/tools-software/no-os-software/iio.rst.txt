no-OS IIO
=========

IIO interfaces and application documentation available at : http://analogdevicesinc.github.io/no-OS/index.html under IIO headline.

BUILD PROJECT WITH IIO SUPPORT
==============================

To build project with no-OS IIO support go to the desired no-OS project folder ``/no-OS/projects/project_name`` and execute:

``make reset``

``make IIOD=y``

Depending on the project and hardware used, the platform might have to be specified inside the Makefile in the project folder, or from command line:

``make PLATFORM=desired_platform clean_all``

``make PLATFORM=desired_platform IIOD=y``

For more information about building projects, go to: :doc:`:git-no-OS:`wiki/Building-no-OS-on-Linux` </wiki-migration/resources/no-os/build>`. After build, execute command:



.. raw:: html

   <details><summary>Xilinx(Click to expand)</summary>

``make run``

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Linux (Click to expand)</summary>

| ``sudo ./build/project.out``

.. important::

   Make sure IIOD is not already running! It can be stopped it with:

   | ``sudo systemctl stop iiod``

.. raw:: html

   </details>


The binaries are loaded to the board. Next, it is possible to connect with a libiio client.

For debugging and development execute command:

``make develop``

Connecting to Clients
---------------------

After building and running a no-Os project, the data can be displayed, processed and visualized through a series of clients, such as command line tools, MATLAB® and Simulink®, IIO-Oscilloscope, etc. Find the complete list of frameworks and applications at http://analogdevicesinc.github.io/libiio/master/index.html

For simply displaying or storing information regarding the devices, :doc:`iio_info </wiki-migration/resources/tools-software/linux-software/libiio/iio_info>`, :doc:`iio_attr </wiki-migration/resources/tools-software/linux-software/libiio/iio_attr>`, :doc:`iio_reg </wiki-migration/resources/tools-software/linux-software/libiio/iio_reg>`, :doc:`iio_readdev </wiki-migration/resources/tools-software/linux-software/libiio/iio_readdev>`, :doc:`iio_writedev </wiki-migration/resources/tools-software/linux-software/libiio/iio_writedev>` are included in the default builds.

Here is an example on how to use ``iio_info`` :

-  For serial context ``iio_info -u serial:/dev/ttyUSB0,115200``
-  For network ``iio_info -u ip:<host>``

For a graphical user interface and plots IIO-Oscilloscope is one possible client. For more information about IIO Oscilloscope go to: :doc:`/wiki-migration/resources/tools-software/linux-software/iio_oscilloscope`

Connecting to IIO-Oscilloscope with the serial context:

.. image:: https://wiki.analog.com/_media/resources/tools-software/no-os-software/iio/iio_osc_uart.png
   :width: 400px

And with network:

.. image:: https://wiki.analog.com/_media/resources/tools-software/no-os-software/screenshot_from_2021-04-29_02-04-15.png
   :width: 400px

Once connected, two windows should pop up.

.. image:: https://wiki.analog.com/_media/resources/tools-software/no-os-software/screenshot_from_2021-04-29_02-04-15.png
   :width: 400px

.. image:: https://wiki.analog.com/_media/resources/tools-software/no-os-software/screenshot_from_2021-04-29_02-06-48.png
   :width: 400px

Python device over iio client
-----------------------------

A python abstraction module for ADI hardware also exists, to make them easier to use. The supported devices can be found at https://analogdevicesinc.github.io/pyadi-iio/devices/index.html

IIO DEMO APPLICATION
====================

A demo iio application can be found in the following location:

:git-no-OS:`projects/iio_demo`

This project is independent of a physical device and should be used as reference, when creating a new iio application for a new iio device. To view information regarding the devices, one can use:

| ``iio_info -u serial:/dev/ttyUSB0,115200``
| or,
| ``iio_info -u ip:host`` (only on Linux)

To load data into RAM, that could be seen in iio-oscilloscope application, execute the following command:

``cat sample_sine.dat | iio_writedev -u serial:/dev/ttyUSB0,115200 -b 400 dac_demo``

This will write 400 samples to “dac_demo” from “sample_sine.dat” file.

FOLDER STRUCTURE
================

.. image:: https://wiki.analog.com/_media/resources/tools-software/no-os-software/iio_folder_structure.png
   :width: 400px

\*\* iio_app*\* – IIO application interface. Sets IIO application communication interface and executes the main application, where commands are received, parsed, and executed. This module is necessary.

\*\* iio_ad9361*\* – This module will register a new interface into iio_interfaces element. Wrapper over ad9361 api, it adapts the interface to iio. This module is optional.

\*\* iio_axi_adc*\* – This module will register a new interface into iio_interfaces element. It also creates an iio_axi_adc device instance and a struct iio_device element, that specifies it’s channels and attributes. Wrapper over axi_adc_core, it adapts the interface to iio. This module is optional.

\*\* iio_axi_dac*\* – This module will register a new interface into iio_interfaces element. It also creates an iio_axi_dac device instance and a struct iio_device element, that specifies it’s channels and attributes. Wrapper over axi_adc_core, it adapts the interface to iio. This module is optional.

SOFTWARE ARCHITECTURE
=====================

The relations between modules can be seen in the following figure.

.. image:: https://wiki.analog.com/_media/resources/tools-software/no-os-software/iio_diagram.png
   :width: 400px
