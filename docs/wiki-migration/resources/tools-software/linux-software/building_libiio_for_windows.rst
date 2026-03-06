Building libiio in Visual Studio
================================

.. note::

   Unless you really, really want to - don't do this. There are pre-compiled :git-libiio:`binaries <releases/latest>` available for end users to use in their projects. If you are struggling with the binaries - :ez:`ask/complain <linux-software-drivers>`. It's the only way we understand what users are looking for.

   
   You shouldn't really need to follow any of these instructions - the instructions are mainly there for libiio developers wanting to keeps some notes, so they remember how to do things.


Build from the GUI
------------------

-  Libiio can be built using the `CMake <http://www.cmake.org>`__ build system.
   Download CMake: http://www.cmake.org/download/

-  To build libiio under Windows, you will need the `libxml2 <http://xmlsoft.org>`__ DLL as well.
   Optionally, for USB support, you will need the `libusb <http://libusb.info>`__ DLL; and for UART support, you will need the `libserialport <http://sigrok.org/wiki/Libserialport>`__ DLL.
   For convenience, a ZIP containing precompiled DLLs of those libraries can be downloaded here: http://swdownloads.analog.com/cse/build/libiio-win-deps.zip

-  Launch CMake, and specify the location of the source code, and the directory where the build will occur.
   Enable the **Grouped** and **Advanced** options (optional).

   |image1|

-  Then click on **Configure**.
   CMake will ask you what generator to use for the project. Select **Use default native compilers** and the generator that matches your version of Visual Studio.

   |image2|

-  CMake will most likely throw an error, as the `libxml2 <http://xmlsoft.org>`__ library is not in the compiler's default search paths:


|image3|

-  Set the correct paths to **LIBXML2_INCLUDE_DIR**, **LIBXML2_LIBRARIES** and **LIBXML2_XMLLINT_EXECUTABLE** as shown below. Then, click again on **Configure**; the errors should disappear.


|image4|

-  Click on **Generate**.
   Now, CMake generated a Visual Studio solution file in the build directory, named "iio.sln". You can open this file with Visual Studio to build the project.

Build from the command line
---------------------------

::

   C:\Users\rgetz\Documents\GitHub\libiio\build>**cmake -DWITH_USB_BACKEND=OFF -DWITH_SERIAL_BACKEND=OFF -DLIBXML2_LIBRARIES="C:\\deps\\libiio-win-deps\\libs\\64\\libxml2.lib" -DLIBXML2_INCLUDE_DIR="C://deps//libiio-win-deps//include//libxml2"  -DLOG_LEVEL=Debug ..**

   C:\Users\rgetz\Documents\GitHub\libiio\build>**cmake --build . --config Release**

   C:\Users\rgetz\Documents\GitHub\libiio\build>**copy .\Release\* .\tests\Release\**

To test something in a loop (over and over again)

::

   C:\Users\rgetz\Documents\GitHub\libiio\build>**FOR /L %L IN (0,0,1) DO @(.\tests\Release\iio_attr.exe -S)**

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/cmake/cmake-configure.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/cmake/cmake-generator.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/cmake/cmake-libxml2-1.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/cmake/cmake-libxml2-2.png
   :width: 600px
