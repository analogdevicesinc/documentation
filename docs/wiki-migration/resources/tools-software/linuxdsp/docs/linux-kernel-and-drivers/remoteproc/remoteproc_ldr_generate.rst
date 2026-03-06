How to Generate Remoteproc LDR File in CCES
===========================================

Introduction
------------

This document introduces the steps to generate the ldr file for remoteproc function in one SHARC core(Core1 or Core2) CCES project. Take the remoteproc sharc template example as the SHARC core CCES project.

Project Configuration
---------------------

Before configuring the CCES project, we need to import the SHARC CCES project into CCES then change the settings of the **Debug** or **Release** Configuration in the CCES project as below:

::

   Project properties -> C/C++ Build -> Settings -> Build Artifact -> Artifact Type: Loader File

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/remoteproc/remoteproc-1.png
   :align: center

::

   Project properties -> C/C++ Build -> Settings -> Tools Settings -> CrossCore SHARC Loader -> General -> Boot mode: SPI master
   Project properties -> C/C++ Build -> Settings -> Tools Settings -> CrossCore SHARC Loader -> General -> Boot format: Binary
   Project properties -> C/C++ Build -> Settings -> Tools Settings -> CrossCore SHARC Loader -> General -> Boot code: 1

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/remoteproc/remoteproc-2.png
   :align: center

::

   Project properties -> C/C++ Build -> Settings -> Tools Settings -> CrossCore SHARC Loader -> Additional Options: -MaxBlockSize 2048

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/remoteproc/remoteproc-3.png
   :align: center

::

   Project properties -> C/C++ Build -> Settings -> Tools Settings -> CrossCore SHARC Loader -> Executable Files:
         For SHARC Core1, specify the core executable file in Core1 part;
         For SHARC Core2, specify the core executable file in Core2 part;

|image1| |image2|

The ldr file will be generated in the Debug or Release folder of the CCES project after building the project.

| 
| ---- **Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/remoteproc/remoteproc-4.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/remoteproc/remoteproc-5.png
