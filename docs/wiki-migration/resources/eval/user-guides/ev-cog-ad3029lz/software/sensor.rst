Analog Devices Sensor Drivers and Examples
==========================================

<note > **There are no seperate toolchain,On-Board Peripheral Drivers & Software for EV-COG-AD3029WZ, the toolchain,On-Board Peripheral Drivers & Software for EV-COG-AD3029LZ works with EV-COG-AD3029WZ.The user needs to change only the pin muxing based on the application.For help regarding pinmapping refer to the Hardware Details section.** </WRAP>

General Description/Overview
----------------------------

Sensor software pack contains sensor software components. Sensor components are based on the sensor classes which abstract the functionality across sensor types. The Sensors software pack provides access to all the necessary add-on module digital drivers that attach to the :adi:`EV-COG-AD3029LZ` development platform. This software layer is the highest layer of abstraction from the microprocessor, and because of this can be useful to jump start code development for your application using any microprocessor. For example, if you are using the ADXL362, the Sensor software pack contains drivers and code snippets on the application level, so that can be transported to other microprocessor, with confidence that Analog Devices provided the application framework pieces. When combined with the :adi:`ADuCM3029` and :adi:`EV-COG-AD3029LZ` software packs there are many great Internet of Things(IoT) applications.

ADI Sensor Software requires CrossCore Embedded Studio 2.6.0 ® , ADuCM3029 Device Family Pack 2.0.0 and EV-COG-AD3029LZ Board Support Package 1.0.0.

The following application examples and sensor drivers are provided as part of the Sensor software pack:

-  Accelerometer Demo
-  Temperature Sensor Demo

For detailed information regarding the Sensor software pack, please see our complete Sensor software user guide.

.. hint::

   
   `Sensor Software Pack Release Notes <http://download.analog.com/tools/Sensor_Software/Releases/Release_1.1.0/ADI-SensorSoftware_1.1.0_Release_Notes.pdf>`__
   


.. important::

   
   You **MUST** have this software package installed on your laptop or PC in order to compile, debug, and run the applications for the EC-COG-AD3029LZ platform.
   


Downloading the Sensor Software Pack
------------------------------------

The software pack can be downloaded in following ways.

-  Downloaded via the tools program

   -  It is **recommended** to download the Sensor software pack through from the tools program you are using. That way, all the files, directories structure, and project structure for the various applications is properly saved and accessed. For a detailed description on how to download the Sensor software pack through CrossCore Embedded Studio please see our :doc:`CrossCore Embedded Studio Quickstart Userguide </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz/tools/cces_guide>`

-  Downloaded to local directory

   -  However if you do decide to download the Sensor software pack to your PC/laptop directly, please use the link below, and make sure you save the software pack to the correct local directory for your applications/projects.

.. admonition:: Download
   :class: download

   
   Download the Sensor Software Pack.
   
   `Sensor Software Pack 1.1.0 <http://download.analog.com/tools/Sensor_Software/Releases/AnalogDevices.ADI-SensorSoftware.1.1.0.pack>`__
   
   | 
   | Link to Github Repository for Cloning or Viewing.
   
   `EV-COG-AD3029LZ Github <https://github.com/analogdevicesinc/EV-COG-AD3029LZ>`__
   


// End of Document //

:doc:`Back </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz>`
