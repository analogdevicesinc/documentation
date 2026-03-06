Demo Title
==========

FIXME! - You need to fix the header here, the page names itself after this heading.

General Description/Overview
----------------------------

FIXME! - Add text, picture, images, that describe what you are doing. Focus on the application, sensor types, end goal, any important themes or theories, equations or other important tables/information. The more info here the better.

Demo Requirements
-----------------

FIXME! - Add text, part numbers, hyper links and other important information and where to get it in order to recreate this demo.

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029
   -  EVAL-CN0397-ARDZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  ADICUP3029_CN0397 software

      -  Inside Sensor_Sw Pack (1.0.0 or higher)

   -  CrossCore Embedded Studio (2.6.0 or higher)
   -  ADuCM302x DFP (2.0.0 or higher)
   -  ADICUP3029 BSP (1.0.0 or higher)
   -  Android IoTNode App (optional)
   -  Serial Terminal Program (Required for running in release mode only)

      -  Such as Putty or Tera Term

Setting up the Hardware
-----------------------

FIXME! - Add text, picture, images, that describe how to setup the example application hardware. A list of boards, sensors, equipment, cables, etc needed to recreate the demo. Step by step picture here are helpful with block diagrams on how to connect things, how to setup options on the boards (Like what UART switch position is the ADICUP3029 in? What power switch position? Is there a chip select jumper on the add-on board that needs to be set?)

Configuring the Software
------------------------

FIXME! - Add text, picture, images, code blocks that describe how to configure the software. Things like changing the accelerometer range from 2g to 4g should be a trivial change for the customer. We don't have to show them everything, but think of the application, and what parameters are most likely need to be customized by the user. (like providing a an ID or password for a local gateway using WI-FI)

Serial Terminal Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following is the UART configuration.

::

     Select COM Port
     Baud rate: 9600
     Data: 8 bit
     Parity: none
     Stop: 1 bit
     Flow Control: none

     | 

Wireless Local Area Network (WLAN) Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following is the Wi-Fi configuration settings in file !FIXME XXXXXXXX.

::

   char ssid[] = "<Enter WLAN SSID >"                                      /* WLAN SSID */
   char password[] = "<Enter WLAN Password>"                    /* WLAN Password */
   char security_type[] = "<Enter WLAN Security Mode>"    /* WLAN Security Type */

|

-  Select the security mode number for your local wireless network from the list given below.

+---------------------+---------------------+-----------------------------------------------------+
| Wi-Fi Security Type | Wi-Fi Security Mode | Description                                         |
+=====================+=====================+=====================================================+
| Open                | 0                   | No Wi-Fi Security                                   |
+---------------------+---------------------+-----------------------------------------------------+
| WEP                 | 1                   | Wired Equivalent Privacy                            |
+---------------------+---------------------+-----------------------------------------------------+
| WPA                 | 2                   | Wi-Fi Protected Access TKIP                         |
+---------------------+---------------------+-----------------------------------------------------+
| WPA2                | 3                   | Wi-Fi Protected Access 2 AES                        |
+---------------------+---------------------+-----------------------------------------------------+
| WPA + WPA2          | 4                   | Wi-Fi Protected Access and Wi-Fi Protected Access 2 |
+---------------------+---------------------+-----------------------------------------------------+
| WPA2 TKIP           | 5                   | Wi-Fi Protected Access 2 TKIP                       |
+---------------------+---------------------+-----------------------------------------------------+

Cloud Configuration
~~~~~~~~~~~~~~~~~~~

Following is the **Analog Devices Connect Cloud Instance** configuration and can be set in the !FIXME XXXXXXXX file .

::

   char instance_url[] = "<Enter Instance URL>"        /* Instance URL */
   char appkey[] = "<Enter WLAN Password>"           /* Application Key */

| 
| Following is the **Analog Devices Connect Thing** configuration and can be set in the !FIXME XXXXXXXX file .

::

   char Thing_Name[] = "<Enter Thing name>"                    /* Thing Name */
   char Thing_Description[]="<Enter thing Description>"  /*Thing Description*/ 

| 
| Following is your **Device Location** configuration and can be set in the !FIXME XXXXXXXX file .

::

   char latitude[] = "<Enter Device Latitude>"          /* Device latitude*/
   char longitude[] = "<Enter Device Longitude>"   /* Device longitude*/
   char elevation[] = "<Enter Device Elevation>"    /* Device elevation*/

| 

Outputting Data in Thingworx
----------------------------

FIXME! - Add text, picture, images, that describe how to output data from the setup/application. Is this a UART output, then show the customer a putty serial terminal with the correct baud rate and commands that need to be entered to get data. Are there any calibrations that need to happen? Show/explain how customers can run the calibration steps. If this is a wireless demo, how do you get the information after it is sent to the cloud? We can use our apps and tools, but the customer should be able to recreate this demo using the same tools/plugins/components you used to view the data.

Analog Devices Connect Specific content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

!FIXME - Add anything here about registering or other features you can use. Talk about using other Thingworx frameworks

Viewing the Data (Mashup)
~~~~~~~~~~~~~~~~~~~~~~~~~

!FIXME - Add content here from your tutorials, links to videos, pics, other stuff like that.

Obtaining the Source Code
-------------------------

We recommend not opening the project directly, but rather import it into CrossCore Embedded Studios and make a local copy in your workspace.

The source code and include files of the FIXME!\ **file_name_of_demo** can be found here:

.. admonition:: Download
   :class: download

   
   FIXME! - This will be either a link to a Git repository or a pack file somewhere, but make sure this is accessible to the customer. We want them to take our code and use it because that means they are going to use our hardware, and we get paid when that happens.
   
   :git-EVAL-ADICUP360:`AduCM360_demo_cn0398 at Github <projects/ADuCM360_demo_cn0398>`
   


How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore Embedded Studio. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tools Overview page. </wiki-migration/resources/eval/user-guides/eval-adicup360/quickstart>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studios tools, please view our `How to import existing projects into your workspace <https://wiki.analog.com/resources/eval/user-guides/eval-adicup360/quickstart/eclipse_user_guide>`__ section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studios tools, please view our `How to configure the debug session <https://wiki.analog.com/resources/eval/user-guides/eval-adicup360/quickstart/eclipse_user_guide>`__ section.

Project Structure
~~~~~~~~~~~~~~~~~

FIXME! - Add text, picture, images, that describe the project structure. Any software flow diagrams or decision trees can be added her to help customers understand how the applications are structures.

// End of Document //
