Optical Gesture Sensor Demo (w/ EVAL-CN0569-PMDZ)
=================================================

The :adi:`EVAL-CN0569-PMDZ` is a PMOD form factor circuit board that allows evaluation of :adi:`ADPD1080` working in tandem with two :adi:`ADPD2140` to create a Infrared Light Gesture Sensor. This example uses the :adi:`EVAL-ADICUP3029` as a motherboard as well as ` <https://github.com/analogdevicesinc/no-OS/>`__ software implementing an IIO server and ` <https://github.com/analogdevicesinc/pyadi-iio/>`__ code that runs on a host computer and implements gesture sensing algorithm.

General Description/Overview
----------------------------

The example software is divided in two parts:

-  Firmware (written in C)
-  Python application

The two parts work together to initialize the hardware, sample de system and implement the gesture sensing algorithm. The firmware is a part of code written in C language that runs on the controller on the :adi:`EVAL-ADICUP3029` and initializes the hardware and runs an IIO server. The python application runs on a host computer connected to the system via an USB serial connection and is responsible for sampling the current passing through the photodiodes and implement different algorithms with it, in this case gesture sensing.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0569/cn0569_concept_diagram.drawio.png
   :alt: Concept diagram
   :align: center

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029
   -  EVAL-CN0569-PMDZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  ` <https://github.com/analogdevicesinc/no-OS/>`__ repository and specifically the :git-no-OS:`example project <projects/iio_adpd1080>`
   -  ` <https://github.com/analogdevicesinc/pyadi-iio/>`__ repository and specifically the :git-pyadi-iio:`examples <examples/cn0569>`
   -  CrossCore Embedded Studio (2.10.1 or higher)
   -  ADuCM302x DFP (3.2.0 or higher)
   -  ADICUP3029 BSP (1.1.0 or higher)
   -  Python 3
   -  GNU make (added in path) or the pre-compiled .hex file

Setting up the Hardware
-----------------------

-  Connect the :adi:`EVAL-CN0569-PMDZ` to the :adi:`EVAL-ADICUP3029` via the P9 connector. Use pins 3-6 on the **CN0569** PMOD connector to connect to the top row of the P9 PMOD connector on the ADICUP3029 board. Pins 1 an 2 will remain unconnected towards the center of the motherboard. Your setup should look like in the picture below.\


|System Overview|

-  Use a mother-to-father breadboard wire to connect pin 1 from the CN0569 to pin 5 on the ADICUP3029 P7 header. The connection should look like in the below picture. What this does is connecting the GPIO0 of the APDP1080 to one of the interrupt GPIOs from the ADuCM3029. We will use theis to calibrate the system clocks.

|GPIO connection|

-  Connect a micro-USB cable to P10 connector of the :adi:`EVAL-ADICUP3029` and connect it to a computer.

Building the software
---------------------

After installing CrossCore Embedded Studio and necessary support pack the user can open a command line terminal (with admin privileges on Windows) and navigate to the project folder in the cloned no-OS repository. There the following list of commands can be used:

No-OS Build System
------------------

::

   make

This is the complete compilation process. It is made up of three rules, that can be used separately: project, update, build

<code> make project </code> - creates the ``build`` directory and the required directory structure

- uses SDK to create a project under the ``build`` directory <code> make update </code> - updates the no-OS sources under the ``build`` directory with files specified in ``src.mk`` <code> make build </code> - performs the build of files under the ``build`` directory using gcc <code> make sdkbuild </code> - performs the build of files under the ``build`` directory using SDK

When modifications are performed, the following three commands trigger the necessary clean actions: <code> make clean </code> - deletes the artifacts generated during build <code> make reset </code> - deletes the ``build`` directory (this results in a fresh setup for starting the complete compilation process) <code> make sdkclean </code> - cleans the artifacts (.o, .elf, .hex, etc.) created by the build command using the SDK

<code> make run </code> - downloads and runs the executable on the target board

<code> make debug </code> - downloads the executable on the target board and opens a command-line ``gdb`` instance to debug it (only on some platforms)

Workflows
~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/no-os/workflows.drawio_1_.svg
   :align: center

Compilation Using Generic Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/no-os/workflownosdk.drawio_1_.svg
   :align: center

Compilation Using Platform-Specific Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/no-os/workflowsdk.drawio_1_.svg
   :align: center


Running the example
-------------------

After the controller has been programmed and the firmware is running on the ADICUP3029 the IIO server is up and a connection to it can be established. This can be done either by using :git-iio-oscilloscope>`__ or the `pyadi-iio code <https::`IIO-Oscilloscope </github.com/analogdevicesinc/pyadi-iio/tree/master/examples/cn0569>`.

To use the gesture sensor and theremin examples, the python library must be installed first using pip:

::

   pip install pyadi-iio

After the installation is complete the example must be configured to connect to the correct COM port. For the theremin example that means :git-pyadi-iio:`changing line 97 accordingly <examples/cn0569>`, with the correct COM port number.

The example can then be run using:

::

   python cn0569_theremin_module.py

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the CN0569.

-  Dragging and Dropping the .Hex to the Daplink drive
-  Building and debugging using CCES and the command line

Using the drag and drop method, the software is going to be a version that Analog Devices creates for testing and evaluation purposes. This is the EASIEST way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters and customize the software to fit your needs, but will be a bit more advanced and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_cn0569** can be found here:

.. admonition:: Download
   :class: download

   
   **Prebuilt CN0569 Hex File for the EVAL-ADICUP3029**
   
   -  :git-no-OS:`Release Folder <releases/tag/Latest>`
   
   .. important::

      The name of the file is currently iio_adpd1080.zip

   
   .. important::

      Github release is in progress. Please use this `pre-generated hex file <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0569/cn0569.zip>`_. (To be removed after release.)

   
   **CN0569 Firmware Source Files**
   
   -  :git-no-OS:`projects/iio_adpd1080`
   
   **CN0569 Python Application Examples**
   
   -  :git-pyadi-iio:`examples/cn0569`
   


How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore Embedded Studio. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tools Overview page. </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools>`

Useful Links
------------

-  :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0569>`
-  :adi:`EVAL-CN0569-PMDZ`
-  :adi:`ADPD1080`
-  :adi:`ADPD2140`

// End of Document //

.. |System Overview| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0569/cn0569_system_picture.jpg
.. |GPIO connection| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0569/cn0569_gpio_connection_picture.jpg
