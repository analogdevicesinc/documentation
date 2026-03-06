:doc:`Click here to return to A2B Bus Analyzer Homepage. </wiki-migration/resources/tools-software/a2b-bus-analyzer>`

A2B Bus Analyzer SDK User Guide
===============================

Introduction
------------

This guide describes the main features of the A\ :sup:`2`\ B Bus Analyzer SDK (the SDK) and how developers can leverage it in their own applications.

The SDK offers developers a C and a python interface to directly access many features of the A\ :sup:`2`\ B Bus Analyzer hardware without interacting with the GUI software, and often with a finer degree of control. In addition, the SDK allows the Analyzer to be used in a range of testing and automation scenarios where control via the GUI is impractical.

**Note:** The A\ :sup:`2`\ B Bus Analyzer Software only runs on 64-bit versions of Windows, Linux and macOS. There are no plans to support 32-bit versions of any OS.

Exporting the SDK
-----------------

The SDK comes bundled as part of the A\ :sup:`2`\ B Bus Analyzer GUI software and must be exported to your computer before it can be used:

1. Select Help → Export User-Accessible SDK... from the application's menu bar:


|image1|

Browse for a suitable location to save the SDK (e.g. your Desktop). Press the Export button when you have selected a destination:

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/export_2.png
   :width: 600px

The SDK is saved inside a folder named 'uasdk' in your chosen location:

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/export_3.png
   :width: 600px

**Note** Exporting the SDK to a folder with spaces will cause problems building the examples so it is not recommended.

The SDK C/C++ Interface
-----------------------

The C/C++ interface to the SDK is provided as a shared library found in the directory ``uasdk/C/lib`` . On Windows this file is named ``a2ba_sdk.dll``  and ``a2ba_sdk.lib`` on Linux and macOS.

To access the library's functionality in your your own projects, you must include the SDK header file ``a2ba_sdk.h`` in the directory ``uasdk/C``.

Example applications
~~~~~~~~~~~~~~~~~~~~

Several example applications are included in the SDK demonstrating different capabilities of the Analyzer as a bus monitor and/or node emulator.

The example projects are located in the ``uasdk/examples/C++`` directory. Also there is a README.md file which repeats these instructions and gives brief descriptions of the example applications.

Each example resides in its own sub-directory, e.g. ``uasdk/examples/C++/emulator/emulator_basic`` .

Building the examples
^^^^^^^^^^^^^^^^^^^^^

To build the examples you will need a C++ compiler for your platform (e.g. GCC for Linux or Visual Studio for Windows). You will also need CMake, version 3.16.3 or later, which can be downloaded from https://cmake.org/download/.

To build the examples, launch your terminal or command prompt in the ``uasdk/examples/C++`` directory.

For the first command, you will need to supply CMake with the correct generator string and architecture for your configuration: please refer to https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html .

For example, using Visual Studio 2017 on Microsoft Windows:

::

   WINDOWS
   > mkdir build
   > cd build
   > cmake .. -G "Visual Studio 15 2017" -A x64
   > cmake --build . --config Release

   LINUX/MAC
   $mkdir build
   $cd build
   $cmake .. -DCMAKE_BUILD_TYPE=Release
   $cmake --build .

\* Replace with the appropriate arguments for your compiler and platform—please refer to https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html  

Running the examples
^^^^^^^^^^^^^^^^^^^^

The built executables are terminal/command prompt programs which CMake places in ``uasdk/examples/C++`` folder with a copy of the shared libraries. For example, the 'emulator_basic' executable can be found in ``uasdk/examples/C++emulator_basic``.

**Note**: While there is a copy of the binaries in the "Release" folder, since the shared libraries are not in the path, the example will fail to run.

::

   WINDOWS:
   > cd uasdk\examples\C++
   > a2ba_sdk_emulator_basic.exe

   LINUX/MAC:
   $ cd uasdk/examples/C++
   $ ./a2ba_sdk_emulator/basic

Using the SDK in your applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default CMake configuration used to build the examples ensures the required runtime libraries are copied to the correct location. However, if you want to run the examples from a different location, or when using the SDK in your own applications, you must update your system's environment variables to point to the libraries in ``uasdk/lib`` .

+---+---+---+
| |image5| | Windows | Add %MY_USER_SDK_DIR%\\user_sdk\\lib  to PATH                |
+---+---+---+
| |image6| | Linux   | Add $MY_USER_SDK_DIR/user_sdk/lib/linux  to LD_LIBRARY_PATH  |
+---+---+---+
| |image7| | macOS   | Add %MY_USER_SDK_DIR%/user_sdk/lib/mac  to LD_LIBRARY_PATH   |
+---+---+---+

Documentation
~~~~~~~~~~~~~

A Doxygen-generated SDK API Reference Manual is available in HTML format in the directory ``uasdk\C\docs`` . Double-clicking the ``A2B_Analyzer_UASDK_help.html`` will display the manual in your default web browser:


|image8|

The manual gives an overview of the A\ :sup:`2`\ B technology and the A\ :sup:`2`\ B Analyzer before documenting the API functions and data structures available to your applications.

Python interface
----------------

The Python interface can be used to integrate Analyzer functionality into your Python applications. It is provided as a 64-bit Python 'wheel' located in the ``uasdk/python``  directory.

There is a wheel for each supported operating system:

========= ============ =================================================
\         **Platform** **Details**
========= ============ =================================================
|image9|  Windows      a2ba_sdk-3.0.0-cp38-cp38m-win_amd64.whl
|image10| Linux        a2ba_sdk-3.0.0-cp38-cp38m-linux_x86_64.whl
|image11| macOS        a2ba_sdk-3.0.0-cp38-cp38m-macosx_10_15_x86_64.whl
========= ============ =================================================

**Note:** Currently the SDK supports only Python 3.8. **Python 2 is not supported**.

Installation
~~~~~~~~~~~~

To use the SDK with your Python application or to run the example, you must first install the correct wheel for your platform. We recommend installing and using in a virtual environment to avoid unexpected changes to your system Python installation.

::

   $ cd uasdk/python

   # Create a virtual environment
   $ python3.6 -m venv env

   # Activate your new virtual environment*
   # WINDOWS
   > env\Scripts\activate

   # LINUX/MAC
   $ source env/bin/activate 

   # Install SDK wheel to new virtual environment
   (env) > pip install a2ba_sdk-3.0.0-cp38-cp38m-win_amd64.whl  # WINDOWS - choose correct wheel for your platform

\* When you are finished using the Python SDK, exit your virtual environment by entering deactivate at the terminal/command prompt.

Examples
~~~~~~~~

Configuring the examples
^^^^^^^^^^^^^^^^^^^^^^^^

There are some simple command line example scripts in the directory ``uasdk/examples/python`` . To run them make sure that the python environment that you are using is the one where you installed the wheel in the previous step. For example, if you used a virtual environment, ensure that this environment has been activated. If it is active, you should see the name of your environment (e.g. 'env') in parentheses before your prompt:

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/python_1.png
   :width: 600px

Set up the file config.py to match the network that you have. This is specially important if you are running the emulator example since the example can support emulating main or sub and either AD2433 or AD2435. A failure to set up the file to match your network is likely to result on failures.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/python_config.png
   :width: 600px

.. _running-the-examples-1:

Running the examples
^^^^^^^^^^^^^^^^^^^^

Then, execute the example script with your Python interpreter:

::

   $ python emulator_basic.py

If successful, you should see output similar to:

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/python_example.png
   :width: 600px

.. _documentation-1:

Documentation
~~~~~~~~~~~~~

A Sphinx-generated API Reference is available in HTML format in the directory ``uasdk\python\docs`` . Double-clicking ``index.html`` will display the manual in your default web browser. In the interactive Python interpreter, you can also type ``help()`` with the function name inside the parentheses.


|image12|

Known limitations
-----------------

-  Each instance of the A\ :sup:`2`\ B Analyzer GUI or the SDK library \*\* supports only one Analyzer*\*.
-  The SDK is **not supported in multi-threaded environments.**

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/export_1.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image2.png
   :width: 20px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image3.png
   :width: 20px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image4.png
   :width: 20px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image2.png
   :width: 20px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image3.png
   :width: 20px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image4.png
   :width: 20px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/documentation_a1.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image2.png
   :width: 20px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image3.png
   :width: 20px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image4.png
   :width: 20px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/python_docs.png
   :width: 600px
