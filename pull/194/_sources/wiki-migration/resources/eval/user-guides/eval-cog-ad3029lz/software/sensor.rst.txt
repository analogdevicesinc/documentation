Sensor Application Software Packs and Drivers
=============================================

General Description/Overview
----------------------------

Sensor software pack contains sensor software components. Sensor components are based on the sensor classes which abstract the functionality across sensor types. The Sensors software pack provides access to all the necessary add-on module digital drivers that attach to the :adi:`EV-COG-AD3029LZ` development platform. This software layer is the highest layer of abstraction from the microprocessor, and because of this can be useful to jump start code development for your application using any microprocessor. For example, if you are using the ADXL362, the Sensor software pack contains drivers and code snippets on the application level, so that can be transported to other microprocessor, with confidence that Analog Devices provided the application framework pieces. When combined with the :adi:`ADuCM3029` and :adi:`EV-COG-AD3029LZ` software packs there are many great Internet of Things(IoT) applications.

ADI Sensor Software requires CrossCore Embedded Studio 2.6.0 ® , ADuCM3029 Device Family Pack 2.0.0 and EV-COG-AD3029LZ Board Support Package 1.0.0.

The following application examples and sensor drivers are provided as part of the Sensor software pack:

-  Accelerometer Demo
-  Temperature Sensor Demo
-  Visible Light Sensor Demo

For detailed information regarding the Sensor software pack, please see our complete Sensor software user guide.

.. hint::

   
   ADD LINK HERE Sensor Software Pack Release Notes.
   


.. important::

   
   You **MUST** have this software package installed on your laptop or PC in order to compile, debug, and run the applications for the EC-COG-AD3029LZ platform.
   


Downloading the Sensor Software Pack
------------------------------------

The software pack can be downloaded in following ways.

-  Downloaded via the tools program

   -  It is **recommended** to download the Sensor software pack through from the tools program you are using. That way, all the files, directories structure, and project structure for the various applications is properly saved and accessed. For a detailed description on how to download the Sensor software pack through CrossCore Embedded Studio please see our :doc:`CrossCore Embedded Studio Quickstart User Guide </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide>`.

-  Downloaded to local directory

   -  However if you do decide to download the Sensor software pack to your PC/laptop directly, please use the link below, and make sure you save the software pack to the correct local directory for your applications/projects.

-  Cloning the EC-COG-AD3029LZ Github Repository

   -  Cloning a public facing Git repository can be done through the CrossCore Embedded Studios tools or directly from the Github website (which will store it to a local directory on your computer.) The same general rules apply from above, where importing the example from Github through the tools package is **recommended**, over downloading the zip file and storing it to a directory of your choice.

.. admonition:: Download
   :class: download

   
   Download the Sensor Software Pack.
   
   `Sensor Software Pack 1.1.0 <http://download.analog.com/tools/Sensor_Software/Releases/>`_
   
   | 
   | Link to Github Repository for Cloning or Viewing.
   
   ADD GITHUB LINK HERE
   


// End of Document //
