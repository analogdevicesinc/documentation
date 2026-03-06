Wi-Fi connected Soil Moisture and pH Measurement Demo
=====================================================

The **ADICUP360_CN0398_Project** is a pH and moisture measurements demo project, for the EVAL-ADICUP360 base board with additional **EVAL-CN0398-ARDZ** shield and ISMART IoT Patform, created using the GNU ARM Eclipse Plug-ins in Eclipse environment. This project demonstrates how to connect the EVAL-ADICUP360 evaluation board to the **Analog Devices Connect** cloud platform.

General Description/Overview
----------------------------

This project is a good example for how to use EVAL-ADICUP360 board in different combinations with Arduino shields. It expand the list of possible applications that can be done with the base board.

The **ADICUP360_CN0398_Project** uses the **EVAL-CN0398-ARDZ** shield which is a single supply, low power, high precision complete solution for soil moisture and pH measurements, including temperature compensation. The circuit is optimized for capacitive soil moisture sensors that are insensitive to water salinity and do not corrode over time. The circuit also measures soil pH so it increases the range of applications where this shield can be used.

The circuit is divided into three independent measurement front ends: pH, soil moisture, and temperature. After signal conditioning, the three channels share an AD7124-8, 24-bit sigma-delta (Σ-Δ) ADC. The AD7124-8, is a low power, low noise, completely integrated analog front end for high precision measurement applications.

The board offers the possibility to configure Vin supply voltage (**P10** connector) in order to use 5V or 7V-12V. Considering moisture sensor which is used, the P8 connector configure 3.3V or 5V supply. The user has the possibility to select one of the three GPIOs available for ADC CS pin using **P5** connector (default configuration for P5 is 1-2 position). For temperature compensation can be used an RTD PT100 sensor, 2-wire (this is used in the demo), 3-wire or 4-wire connection (see P1 connector). For this demo was used for the moisture measurement the VH400 sensor (**P2**) and for pH measurement Atlas Scientific sensor (**J1**). The **DS1** LED is ON as long the pH value is measured and calculated and the **DS3** is ON as long as the moisture value is measured and calculated. The application processes ADC outputs for all 3 channels (RTD, pH and moisture), calculates pH and moisture values using as input RTD temperature value. The **24-bits** ADC data are received using **SPI** interface of the EVAL-ADICUP360 board.

The temperature value is calculated based on the RTD resistance:

::

                                                           CODE - ADC output
   Rrtd = ((CODE - 2^23)* Rref)/GAIN*2^23                  Rref - Reference resistor (5kΩ)        
                                                           GAIN - used gain for RTD channel (16)

**1. RTD resistance > 100Ω**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/inventek_thinkworx/rtd_morethan_100.png
   :align: center

**2. RTD resistance ≤ 100Ω**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/inventek_thinkworx/rtd_lessthan_100.png
   :align: center

The **pH** value can be calculated using Nernst equation.

::

   ph  = [PH_ISO -((V - a) / ((2.303 * AVOGADRO * (T + 273.1))]    
           
         PH_ISO - reference hydrogen ion concentration (7)
         V - pH channel measured voltage
         a - zero point tolerance (see //ZERO_POINT_TOLERANCE// parameter)
         AVOGADRO - Avogadro's number (8.314)
         T - RTD temperature  

The **moisture** value can be also calculated in two ways. First way is to use piece-wise formulas given by manufacturer (check USE_MANUFACTURER_MOISTURE_EQ parameter. For Vegetronix may use the follow formulas (m - moisture value and Vm - moisture channel measured voltage):

================= ======================
**Voltage Range** **Equation**
================= ======================
0V - 1.1V         m = 10 \* Vm - 1
1.1V - 1.3V       m = 25 \* Vm - 17.5
1.3V - 1.82V      m = 48.08 \* Vm - 47.5
1.82V - 2.2V      m = 26.32 \* Vm - 7.89
================= ======================

Otherwise the moisture value can be calculated using transfer function for the sensor:

::

   m =-1.18467 + 21.5371*Vm - 110.996*Vm^2 + 397.025*Vm^3 - 666.986*Vm^4 + 569.236*Vm^5 -246.005*Vm^6 + 49.4867*Vm^7 -3.37077*Vm^8 

The application also sends the light intensity data to the Analog Devices Connect cloud platform using the ISMART IoT Platform. The sensor data can be visualized in a Mashup within the Analog Devices Connect Cloud Platform.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP360
   -  EVAL-CN0398-ARDZ
   -  Vegetronix VH400 soil moisture sensor
   -  RTD PT100 sensor
   -  Atlas Scientific pH sensor
   -  7V-12V DC Power Supply
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  ADuCM360-IDE
   -  ADICUP360_CN0398 software project
   -  Analog Devices Connect Entities

| 

Thingworx/ Analog Devices Connect
---------------------------------

Login to your Analog Devices Connect instance. The Google Chrome browser is recommended when using the Analog Devices Connect Composer.

**Importing Entities into the Analog Devices Connect Composer**

-  Download the adconnect_adicup360_cn0398_entities.zip file.\ `adconnect_adicup360_cn0398_entities.zip <https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/inventek_thinkworx/adconnect_adicup360_cn0398_entities.zip>`__
-  Unzip it. The ADConnect_ADICUP360_CN0398.xml file within contains the entities that you need to import to the Analog Devices Connect instance.
-  To import these entities to your instance, open the *Import/Export* tab at the top of the window and select *Import -> From File* option.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/inventek_thinkworx/adconnect_importentities1.png
   :align: center

-  Select Entities, navigate to the entities XML file that you downloaded beforehand using the *Choose File* button.
-  Click on *Import*. If you get an *“Import Successful”* message, then all the required entities have been imported to your instance.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/inventek_thinkworx/adconnect_importentities2.png
   :align: center

**Creating an Application Key**

-  Application keys are a way to provide authentication without requiring a user, device, system, or third party application to log into Analog Devices Connect.
-  To create an application key, expand the Security section on the left side of the Homepage.
-  Select Application Keys and click on the New button on the top of the page.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/inventek_thinkworx/adconnectappkeycreation0.png
   :align: center

-  Give a name to your application key. In the User Name Reference field, add the user that will be associated with the application key.
-  Click Save button.

| |image1|

Setting up the Hardware
-----------------------

-  Set the jumpers on the EVAL-ADICUP360 board as shown in the next figure. The important jumpers are highlighted in red.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/inventek_thinkworx/adicup360_jumperconfiguration.png
   :align: center
   :width: 500px

-  Set the jumpers on the EVAL-CN0398-ARDZ board as shown in the next figure. The important jumpers are highlighted in red.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/inventek_thinkworx/cn0398_jumpersettings.png
   :align: center
   :width: 500px

-  The VH400 moisture sensor was used in the example. Since the VH400 moisture sensor requires a 5V power supply, place the jumpers on the EVAL-CN0398-ARDZ shield as shown in the image below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/inventek_thinkworx/vh400_jumpersettings.png
   :align: center
   :width: 200px

-  The 3-wire PT100 RTD was used in the example. Configure the 3-wire RTD as shown in the image below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/inventek_thinkworx/3wirertd.png
   :align: center
   :width: 300px

-  The Atlas Scientific pH probe was used in this example. The EVAL-CN0398-ARDZ shield board comes with a BNC connector J1 for pH sensors as shown in the next figure.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/inventek_thinkworx/ph_probe.png
   :align: center
   :width: 300px

-  Set the power jumper J17 to receive power from EVAL-ADICUP360 base board.Set UART Switch SW3 in position 3 (i.e. away from the module) to allow ISMART IoT Platform to communicate with EVAL-ADICUP360 base board via UART.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/inventek_thinkworx/ismart_iot_platform_jumpersettings.png
   :align: center
   :width: 300px

-  Since all the evaluation boards used in this example are compatible with the Arduino form factor, they can be easily stacked up one on top of the other, starting with the processor board at the bottom followed by the sensor shield in the middle and the Wi-Fi module at the top as shown in the next figure.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/inventek_thinkworx/adicup360_cn0398_ism43340.jpg
   :align: center
   :width: 500px

-  Extremely important to plug in an acceptable power supply to the barrel jack P11 to supply power.

-  Use the Debug USB (P14) of EVAL-ADICUP360 board for flashing and debugging.

| 

Configuring the Project Parameters
----------------------------------

To configure the software, navigate to the *User_Settings.h* file in the include folder of the project.

Following is the Wi-Fi configuration settings in the *User_Settings.h* file

::

   char ssid[]           = "<Enter WLAN SSID >"                  /*  WLAN SSID          */
   char password[]       = "<Enter WLAN Password>"               /*  WLAN Password      */
   char security_type[]  = "<Enter WLAN Security Mode>"          /*  WLAN Security Type */

Select the security mode number for your local wireless network from the list given below.

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

| 
| Following is the **Thingworx/Analog Devices Connect Cloud Instance** configuration and can be set in the *User_Settings.h* file .

::

   char instance_url[]        = "<Enter Instance URL>"             /* Instance URL    */
   char appkey[]              = "<Enter Application Key>"          /* Application Key */

| 
| Following is the **Thingworx/Analog Devices Connect Thing** configuration and can be set in the *User_Settings.h* file .

::

   char Thing_Name[]          = "<Enter Thing name>"               /* Thing Name         */
   char Thing_Description[]   = "<Enter Thing Description>"        /* Thing Description  */ 

| 
| Following is the **Device Location** configuration and can be set in the *User_Settings.h* file .

::

   char latitude[]           = "<Enter Device Latitude>"           /*  Device latitude   */
   char longitude[]          = "<Enter Device Longitude>"          /*  Device longitude  */
   char elevation[]          = "<Enter Device Elevation>"          /*  Device elevation  */

| 
| Following is the **Protocol** configuration and can be set in the *ISM43340.c* file under the src folder. To request a HTTPS (Hyper Text Transfer Protocol Secure) connection to your Thingworx/Analog Devices Connect instance, uncomment the following macro

::

   #define SSL                                                     /* Uncomment for HTTPS protocol, 
                                                                      leave commented for HTTP protocol */

| 
| Following is an example showing how to set project parameters set in the *User_Settings.h* file.

::

   char ssid[]                =  "IoT_Network"                                 /*  WLAN SSID          */
   char password[]            =  "IoT_Network_123"                             /*  WLAN Password      */
   char security_type[]       =  "2"                                           /*  WLAN Security Type */

   char instance_url[]        =  "example.connect.analog.com"                  /*  Instance URL       */
   char appkey[]              =  "d912c028-3214-43d4-81f5-453c9d0749d6"        /*  Application Key    */

   char Thing_Name[]          =  "ADICUP360_CN0398_Thing"                      /*  Thing Name         */
   char Thing_Description[]   =  "Thing created by my device"                  /*  Thing Description  */ 

   char latitude[]            =  "42.2105"                                     /*  Device latitude    */
   char longitude[]           =  "-71.1806"                                    /*  Device longitude   */
   char elevation[]           =  "0"                                           /*  Device elevation   */

| 

Viewing the Mashup
------------------

To view the light intensity measurement data being sent to the cloud, open the ADICUP360_CN0398_Mashup from the Thingworx/Analog Devices Connect Composer. Click on the View Mashup button at the top of the screen. The Mashup will open in a separate tab in the browser. Make sure popups are enabled.

| |image2|
| Select your Thing from the grid to view its data and location in the Mashup.

| |image3|
| ===== Obtaining the Source Code ===== We recommend not opening the project directly, but rather import it into CrossCore Embedded Studios and make a local copy in your workspace.

The source code and include files of the FIXME!\ **file_name_of_demo** can be found here:

.. admonition:: Download
   :class: download

   
   FIXME! - This will be either a link to a Git repository or a pack file somewhere, but make sure this is accessible to the customer. We want them to take our code and use it because that means they are going to use our hardware, and we get paid when that happens.
   
   :git-EVAL-ADICUP360:`AduCM360_demo_cn0398 at Github <projects/ADuCM360_demo_cn0398>`
   


How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP360 is the ADuCM360-IDE, an Eclipse based development environment. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tool Chain Download and Installation Guide </wiki-migration/resources/eval/user-guides/eval-adicup360/quickstart>` page.

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the ADuCM360-IDE tools, please view our Importing a Project section in the :doc:`Tool Chain Setup & User Guide </wiki-migration/resources/eval/user-guides/eval-adicup360/quickstart>`.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the AduCM360-IDE tools, please view our Setting up a Debug Configuration for the Project section in the :doc:`Tool Chain setup & user Guide </wiki-migration/resources/eval/user-guides/eval-adicup360/quickstart>`.

Project Structure
~~~~~~~~~~~~~~~~~

|image4|\ The ADICUP360_CN0398_Project project uses basic ARM Cortex-M C/C++ Project structure. This project contains: system initialization part - disabling watchdog, setting system clock, enabling clock for peripheral; port configuration for SPI1 to communicate with sensor, for UART to communicate with the ISMART IoT Platform and for LCD use; SPI read/write functions for sensor monitoring; UART read/write functions for ISMART IoT Platform control; LCD handle parts; HTTP REST API calls to communicate with Analog Devices Connect instance.

In the src and include folders you will find the source and header files related to the application. The Communication.c/h files contain SPI and UART specific data, meanwhile the CN0398.c/h files contain the sensor information, the Lcd.c/h files contain the LCD related information, the ISM43340.c/h files contain data specific to the ISMART IoT Platform, and the Services.c/h and HTTP_REST_API.c/h files contains REST API Calls to communicate with Analog Devices Connect cloud platform.

In the appropriate header files you can configure next parameters:

-  **Zero point tolerance** - *ZERO_POINT_TOLERANCE* parameter - used in Nerst equation - input voltage value in [V] (*CN0398.h*).

   -  **Terminal refresh** - *DISPLAY_REFRESH* parameter - how often to refresh the output data - input time value in [msec] (*CN0398.h*).

      -  **Moisture calculation formula** - *USE_MANUFACTURER_MOISTURE_EQ* parameter - which formula to use in order to calculate the moisture value - commented -> transfer function, uncommented -> manufacturer formulas(*CN0398.h*).

The system folder contains system related files (try not to change these files):

-  **aducm360** – contains low levels drivers for ADuCM360 microcontroller.
-  **cmsis** – contains files related to ADuCM360 platform, such as: ADuCM360.h (registers definitions), system_ADuCM360.c/h (system clock), vectors_ADuCM360.c (interrupt vector table).
-  **cortexm** – contains files for system management (start-up, reset, exception handler).

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/inventek_thinkworx/adconnect_appkeycreation.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/inventek_thinkworx/viewmashup_cn0398.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/inventek_thinkworx/viewmashup_cn0398.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/inventek_thinkworx/projectstructure_cn0398.png
