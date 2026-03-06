Demo Title
==========

FIXME - You need to fix the header here, the page names itself after this heading.

General Description/Overview
----------------------------

FIXME - Add text, picture, images, that describe what you are doing. Focus on the application, sensor types, end goal, any important themes or theories, equations or other important tables/information. The more info here the better.

Demo Requirements
-----------------

FIXME - Add text, part numbers, hyper links and other important information and where to get it in order to recreate this demo.

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP360
   -  EVAL-CN0397-ARDZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  ADICUP360_CN0397 software
   -  CrossCore Embedded Studio (2.7.0 or higher)
   -  ADuCM36x DFP (1.0.2 or higher)
   -  CMSIS ARM Pack (4.3.0 or higher)
   -  Serial Terminal Program

      -  Such as Putty or Tera Term

Setting up the Hardware
-----------------------

FIXME - Add text, picture, images, that describe how to setup the example application hardware. A list of boards, sensors, equipment, cables, etc needed to recreate the demo. Step by step picture here are helpful with block diagrams on how to connect things, how to setup options on the boards (Like what UART switch position is the ADICUP3029 in? What power switch position? Is there a chip select jumper on the add-on board that needs to be set?)

Obtaining the Source Code
-------------------------

We recommend not opening the project directly, but rather import it into CrossCore Embedded Studios and make a local copy in your workspace.

The source code and include files of the FIXME!\ **file_name_of_demo** can be found here:

.. admonition:: Download
   :class: download

   
   FIXME - This will be either a link to a Git repository or a pack file somewhere, but make sure this is accessible to the customer. We want them to take our code and use it because that means they are going to use our hardware, and we get paid when that happens.
   
   :git-EVAL-ADICUP360:`AduCM360_demo_cn0398 at Github <projects/ADuCM360_demo_cn0398>`
   


.. note::

   For more information on importing, debugging, or other tools related questions, please see the `tools user guide. <:doc:`/wiki-migration/resources/eval/user-guides/eval-adicup360/tools/cces_user_guide`>`__


Configuring the Software Parameters
-----------------------------------

FIXME - Add text, picture, images, code blocks that describe how to configure the software. Things like changing the accelerometer range from 2g to 4g should be a trivial change for the customer. We don't have to show them everything, but think of the application, and what parameters are most likely need to be customized by the user. (like providing a an ID or password for a local gateway using WI-FI)

Outputting Data
---------------

FIXME - Add text, picture, images, that describe how to output data from the setup/application. Is this a UART output, then show the customer a putty serial terminal with the correct baud rate and commands that need to be entered to get data. Are there any calibrations that need to happen? Show/explain how customers can run the calibration steps. If this is a wireless demo, how do you get the information after it is sent to the cloud? We can use our apps and tools, but the customer should be able to recreate this demo using the same tools/plugins/components you used to view the data.

Serial Terminal Output
~~~~~~~~~~~~~~~~~~~~~~

Following is the UART configuration.

::

     Select COM Port
     Baud rate: 9600
     Data: 8 bit
     Parity: none
     Stop: 1 bit
     Flow Control: none

     | 

How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP360 is CrossCore Embedded Studio. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tools Overview page. </wiki-migration/resources/eval/user-guides/eval-adicup360/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studios tools, please view our :doc:`How to import existing projects into your workspace </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide>` section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studios tools, please view our :doc:`How to configure the debug session </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide>` section.

Project Structure
~~~~~~~~~~~~~~~~~

FIXME - Add text, picture, images, that describe the project structure. Any software flow diagrams or decision trees can be added her to help customers understand how the applications are structures.

The **RTE** folder contains device and system related files:

-  **Device Folder** – contains low levels drivers for ADuCM360 microcontroller.(try not to edit these files)
-  **system.rteconfig** - Allows the user to select the peripherial components they need, along with the startup and ARM cmsis files needed for the project.

|

| // End of Document //
