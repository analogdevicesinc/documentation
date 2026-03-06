Geiger Counter demo (EVAL-CN0536-ADRZ)
======================================

The **ADuCM3029_demo_cn0536** project provides a solution to measure radiation levels using most of Geiger-Muller tube sensors available in the market. It uses the precision programmable oscillator :adi:`LTC6906` to generate high voltage output for the tube and the :adi:`LTC1540` nano power comparator to set and regulate it. With the :adi:`LTC1441` ultralow power dual comparator the Geiger pulse is translated to logic level 3V or 5V and the :adi:`LTC6994 <LTC6994-1>` robust built in delay block timer chip will generate a Geiger clicking sound to a regular buzzer.

Also, onboard LEDs are used to indicate radiation levels and information about the counts per minute and microSieverts per minute are sent over **UART** or over the internet through **MQTT**.

A sample python code is available to **plot** MQTT data into a graph with a radiation threshold.

The **ADuCM3029_demo_cn0536** project is using the the :adi:`CN0536` and :adi:`EVAL-ADICUP3029` prototyping board.

This page will go through how to build and run the demo from the **software** point of view and for more detailed information about the :adi:`CN0536` from the **hardware** side can be found :doc:`here </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0536>`.

An overview about the theme can be seen in the following diagram:


|image1|

Software flow
-------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0536/flow.png
   :align: center

Demo Video
----------

.. image:: https://wiki.analog.com/_media/youtube>moclurd4uis
   :alt: youtube>moclurd4uis

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  :adi:`EVAL-ADICUP3029` (**optional** with ESP8266)
   -  :adi:`EVAL-CN0536-ARDZ`
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port
   -  24V and 1A limited power supply (**optional**)

-  Software

   -  Serial Terminal Program (for **UART** demo) such as:

      -  Arduino Serial Monitor from `Arduino IDE <https://www.arduino.cc/en/Guide#install-the-arduino-desktop-ide>`__
      -  `Putty <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`__
      -  `Tera Term <https://osdn.net/projects/ttssh2/releases>`__

   -  :adi:`CrossCore Embedded Studio <en/design-center/evaluation-hardware-and-software/software/adswt-cces.html#software-relatedsoftware>` (:doc:`Installation wiki </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`) (**Optional** to edit the software)
   -  ADuCM302x DFP and ADICUP3029 BSP (see this :doc:`guide </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide>`) (**Optional** to edit the software)
   -  :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0536 demo application <projects/ADuCM3029_demo_cn0536>` (**Optional**, software code)
   -  `Python 3 <https://www.python.org/downloads>`__ (**Optional**, to plot MQTT data)

UART demo with precompiled program
----------------------------------



.. raw:: html

   <details><summary>Click to expand</summary>

-  Set the :doc:`UART switch </wiki-migration/resources/eval/user-guides/eval-adicup3029/hardware/adicup3029>` to USB. |\||
-  Place the **EVAL-CN0536-ARDZ** on top of the **EVAL-ADICUP3029**.

|image2|

-  Connect a micro-USB cable to the :doc:`USB connector </wiki-migration/resources/eval/user-guides/eval-adicup3029/hardware/adicup3029>` and then to the PC.
-  Download the **UART** precompiled program

.. admonition:: Download
   :class: download

   
   | 
   | Precompiled **ADuCM3029_demo_cn0536** project with **UART** communication:
   | :git-EVAL-ADICUP3029:`releases/download/Latest/ADuCM3029_demo_cn0536_uart.hex`


-  :doc:`Upload </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/adicup3029_hw_drivers>` the precompiled .hex file to the board. (Copy the .hex file to the DAPLINK drive)
-  Reset the board from the :doc:`RESET </wiki-migration/resources/eval/user-guides/eval-adicup3029/hardware/adicup3029>` push button.

|image3|

-  Start the serial terminal program.
-  Connect it to the desired port. Eg. COM4, check :doc:`step by step guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/eval-adxrs290-pmdz/uart_serial_terminal>` if needed.
-  Set the **BAUDRATE** to **115200**
-  Watch the output. Data will be send every 10 seconds by default.

|image4|

.. raw:: html

   </details>


MQTT (Wi-Fi) demo with precompiled program
------------------------------------------



.. raw:: html

   <details><summary>initialState="visible"</summary>

-  Set the :doc:`UART switch </wiki-migration/resources/eval/user-guides/eval-adicup3029/hardware/adicup3029>` to ARDUINO. |\||
-  Place the **EVAL-CN0536-ARDZ** on top of the **EVAL-ADICUP3029**.

|image5|

-  Connect the ESP8266 EN pin to 3.3V or solder it like below.\

|image6|

-  Connect the ESP8266 module to the Arduino Header.

|image7|

-  Connect a micro-USB cable to the :doc:`USB connector </wiki-migration/resources/eval/user-guides/eval-adicup3029/hardware/adicup3029>` and then to the PC.
-  Download the **MQTT** precompiled program

.. admonition:: Download
   :class: download

   
   | 
   | Precompiled **ADuCM3029_demo_cn0536** project with **MQTT** communication:
   | :git-EVAL-ADICUP3029:`releases/download/Latest/ADuCM3029_demo_cn0536_mqtt.hex`


-  Create a hotspot or set a WiFi network with the following values (It must have **Internet** connection):

   -  SSID: **analog_hotspot**
   -  Password: **12345678**

-  Reset the board from the :doc:`RESET </wiki-migration/resources/eval/user-guides/eval-adicup3029/hardware/adicup3029>` push button.


|image8|

-  During **setup** the **blue** led will be turned **on**:

|image9|

-  If the setup completed **succesfully**, the **green** led will be turned **on** (blue will be turned off). This means that the program is sending data to the server.

|image10|

-  In case of an **error** during setup or during program execution, both leds will **blink alternated** with a 1 second period.
-  Data will be sent to:

   -  MQTT Server: **broker.hivemq.com**
   -  MQTT Topic: **analog_test_topic**

-  Use one of the below methods to view the data

XHIDDENSTART Use MQTT Web Client to view data initialState="visible" XHIDDENSTARTSTOP

-  Open the `MQTT Web Client <http://www.hivemq.com/demos/websocket-client>`__
-  Set the above server to connect to:

|image11|

-  After succesfull connection, subscribe to the mentioned topic:

|image12|

-  View the published data under messages:

|image13|

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Use MQTT local html client to view data</summary>

-  Download the `HTML MQTT client <https://raw.githubusercontent.com/analogdevicesinc/EVAL-ADICUP3029/master/projects/ADuCM3029_demo_cn0536/demo.html>`__ (Rigth click on the link -> *Save link as...*)
-  Open the saved file into your browser.
-  In the upper of the page the server connection status is shown
-  A Graph with the data sent by the Geiger Counter is ploted:|image14|

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Use MQTT python client to view data</summary>

-  Get the `python script <https://raw.githubusercontent.com/analogdevicesinc/EVAL-ADICUP3029/master/projects/ADuCM3029_demo_cn0536/scripts/main.py>`__ (Rigth click on the link -> *Save link as...*).
-  Run a terminal (cmd in windows) where the file was downloaded.
-  Install the needed python dependencies with: ``python -m pip install paho-mqtt matplotlib parse``
-  Run the python sample script: ``python main.py``
-  A new plot windows will be created and the recieved data will be printed also in to the terminal:

|image15|

.. raw:: html

   </details>


XHIDDENEND

Working with the software
-------------------------



.. raw:: html

   <details><summary>Getting started with the software</summary>

-  `Make <https://www.gnu.org/software/make>`__ program should be installed and available in the path.
-  Open a **terminal** (linux) or a **cmd** (windows) and navigate to a directory where to start working.
-  Download the EVAL-ADICUP3029 :git-EVAL-ADICUP3029>`__ with ``git clone --recursive https::`repository </github.com/analogdevicesinc/EVAL-ADICUP3029.git``
-  Using the **--recursive** is **important** in order for the submodules to be initialized.
-  Go to `project directory <https://github.com/analogdevicesinc/EVAL-ADICUP3029/tree/master/projects/ADuCM3029_demo_cn0536>`. ``cd projects\ADuCM3029_demo_cn0536``
-  Follow this `guide <:doc:`/wiki-migration/resources/no-os/build`>`__ to create a CCES project. This command should be enough: ``make update_srcs``
-  A folder **build** will be created and inside it the CCES project.
-  Import the new generated project into your workspace. See :doc:`wiki </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide>`
-  Now the project structure should look like this:

|image16|

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Editing software parameters</summary>

-  For Geiger Counter configuration see geiger_counter.h. The default configuration means:

   -  Output data will be calculated at each 10 seconds
   -  A average filter is applied on the last 5 samples
   -  us_per_min = c_per_min \* CONVERSION_FACTOR
   -  Jumper 2 is solder on the back of the CN0536 ``/* Number of seconds between each measurement */
      #define SAMPLING_PERIOD     10//seconds
      /* Number of measurements used for average filtering */
      #define NB_AVARGE_SAMPLES   5
      /* Conversion factor from counts/minute -> microSieverts/minute */
      #define CONVERSION_FACTOR   0.01

      /*
        * Depending of the jumper soldered on the board one of these 3 options is
        * available for reading the Geiger pulses.
        * Avaliable options are:
        *     - 2 : JP2 soldered (default on board)
        *     - 3 : JP3 soldered
        *     - 4 : JP4 soldered
       */
      #define JUMPER_CONFIG   2``

-  For communication configuration see communication.h: The default configuration means:

   -  **MQTT** is used as **default** communication method. If something goes wrong with Wi-fi, communication will start over UART.
      In order to use UART from the beginning, set the **COMUNICATION_METHOD** macro to UART
   -  The program will try to connect to a wifi network with name **analog_hotspot** and password **12345678**
   -  The program will try to publish the data to **test.mosquitto.org MQTT** broker at the topic **analog_test_topic** ``#ifndef COMUNICATION_METHOD
      #define COMUNICATION_METHOD MQTT
      //#define COMUNICATION_METHOD   UART
      #endif

      /* UART configuration parameters */
      #define CONFIG_UART_PARITY  UART_NO_PARITY
      #define CONFIG_UART_STOPBITS    UART_ONE_STOPBIT
      #define CONFIG_UART_WORD_LEN    UART_WORDLEN_8BITS
      #define CONFIG_UART_BAUDRATE    BD_115200

      /* WIFI */
      #define WIFI_SSID       "analog_hotspot"
      #define WIFI_PASS       "12345678"

      /* MQTT Server */
      #define MQTT_SERVER_ADDRESS "test.mosquitto.org"
      #ifndef DISABLE_SECURE_SOCKET
      #define SERVER_PORT     8883
      #else
      #define SERVER_PORT     1883
      #endif

      /* MQTT Client */
      #define MQTT_BUFFER_SIZE    500
      #define MQTT_TIMEOUT        20000 //ms
      #define MQTT_KEEPALIVE      7200 //ms
      #define MQTT_CLIENT_NAME    "analog_client"
      #define MQTT_PUBLISH_TOPIC  "analog_test_topic"``

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Build and debug the project</summary>

:doc:`How to build and a CCES project </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide>`

.. raw:: html

   </details>


// End of Document //

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0536/gc_overview.png
.. |\|| image:: /resources/eval/user-guides/eval-adicup3029/reference_designs/adicup3029_switch.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0536/20200804_1724001.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0536/geiger_counter_reset.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0536/uart_output.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0536/20200804_1724001.jpg
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/reference_design_esp8266_hw_mod_front.png
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0536/cables.png
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0536/geiger_counter_reset.jpg
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0536/blue_led.jpg
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0536/green_led.jpg
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0536/mqtt_connect.jpg
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0536/mqtt_subscribe.jpg
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0536/mqtt_mesages.jpg
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0536/local_html.jpg
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0536/mqtt_plot.png
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0536/proj_structure.png
