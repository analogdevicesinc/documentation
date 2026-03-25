.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0536

.. _eval-cn0536-ardz:

EVAL-CN0536-ARDZ
================

Geiger Counter Radiation Detection System.

Overview
--------

.. figure:: eval-cn0536-ardz.png
   :width: 400 px
   :align: center

   EVAL-CN0536-ARDZ Evaluation Board (GM tube not included)

Geiger counters are one of the most commonly used tools to measure radiation
levels. This type of sensor is generally deployed in numbers across different
areas and linked together to a cloud server for easy monitoring.

The :adi:`EVAL-CN0536-ARDZ <CN0536>` is designed for use with Geiger counter
radiation detectors (GM tube not included) and is in an Arduino shield form
factor compatible with 3 V and 5 V platform boards. The bias power supply is
adjustable from 280 V to 500 V, allowing use with a wide range of
Geiger-Mueller tubes; an SI-29BG tube is used as an example.

The board uses a hysteretic voltage regulation scheme by controlling the power
supplied to the board oscillator, minimizing the overall current consumption.
It has a configurable voltage reference for its output, allowing the board to
safely translate the Geiger pulses to the logic level of the microcontroller.
Additionally, audio and visual indicators qualitatively alert the user as
radiation levels increase.

Simplified Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: cn0536_block_diagram.png
   :width: 800 px
   :align: center

   EVAL-CN0536-ARDZ Simplified Block Diagram

Board Pinout
~~~~~~~~~~~~

The figure below shows the pins used as well as their corresponding functions.
The output pin for the Geiger pulse can be set in four different locations,
allowing flexibility in case other shields are used together with the CN0536.
By default, JP1 is shorted and the Geiger pulse is read from GPIO33. Some pins
have specific alternate functions; all other unlabeled pins are free to be used.

.. figure:: pinout.png
   :width: 800 px
   :align: center

   EVAL-CN0536-ARDZ Board Pinout

System Overview
~~~~~~~~~~~~~~~

The CN0536 system supports data transfer via UART or over Wi-Fi to an MQTT
server for remote monitoring. A sample Python script is available to plot MQTT
data into a graph with a radiation threshold.

.. figure:: cn0536_system_overview.png
   :width: 600 px
   :align: center

   CN0536 System Overview (UART and MQTT Data Paths)

.. figure:: cn0536_software_flow.png
   :width: 600 px
   :align: center

   CN0536 Software Flow Diagram

Features
~~~~~~~~

- Adjustable bias supply from 280 V to 500 V output range
- Hysteretic voltage regulation for low current consumption
- Configurable voltage reference for logic-level translation
- Audio and visual indicators for radiation level feedback
- Arduino shield form factor, compatible with 3 V and 5 V platforms
- Configurable output pin location via jumper (JP1)

Required Equipment
------------------

- EVAL-CN0536-ARDZ with GM tube installed
- :adi:`EVAL-ADICUP3029` platform board
- 280 V to 500 V Geiger-Mueller tube, such as SI-29BG
- Micro-USB cable
- Host computer with a serial terminal program (Tera Term or PuTTY)
- A safe radiation source (optional, for testing)

Getting Started
---------------

This section outlines how to configure the EVAL-CN0536-ARDZ to accommodate
different types of GM tubes.

#. Check the GM tube pin configurations. Refer to the product datasheet and
   note the operating voltage of the GM tube to be used.

   .. figure:: gm_polarities.png
      :width: 600 px
      :align: center

      GM Tube Polarities

#. Measure the set resistance at pins 2 and 3 of the potentiometer R9 and
   adjust it to achieve the desired value. Refer to the figure below for pin
   location.

   .. figure:: adjusting_the_potentiometer_r9.png
      :width: 600 px
      :align: center

      Adjusting the Potentiometer (R9)

#. Solder the GM tube to the EVAL-CN0536-ARDZ and ensure proper grounding.
   For stability and safety, secure the sensor to the board using a cable tie.

   .. figure:: cn0536_with_gm_tube.png
      :width: 600 px
      :align: center

      CN0536 with GM Tube: (a) Unsoldered (b) Soldered

Setup and Test
--------------

.. figure:: cn0536_with_adicup3029.png
   :width: 600 px
   :align: center

   EVAL-CN0536-ARDZ with GM Tube Combined with the EVAL-ADICUP3029

Follow these steps to evaluate the EVAL-CN0536-ARDZ (with installed GM tube)
and the associated software:

#. Connect the EVAL-CN0536-ARDZ on top of the EVAL-ADICUP3029 platform board.

   .. figure:: cn0536_adicup3029_connection.png
      :width: 600 px
      :align: center

      CN0536 with GM Tube and EVAL-ADICUP3029 Connection

#. Connect the EVAL-ADICUP3029 to the PC using the micro-USB cable provided.
#. From the PC, drag and drop the prebuilt ``ADuCM3029_demo_cn0536_uart.hex``
   file onto the DAPLink drive.
#. Open the serial terminal program (for example, Tera Term or PuTTY).
#. Connect the EVAL-ADICUP3029 using the COM port it was assigned to and set
   the baud rate to 115200.

   .. figure:: tera_term_serial_monitor.png
      :width: 400 px
      :align: center

      Using Tera Term as Serial Monitor with Baud Rate Set to 115200

#. Place the radioactive source near the Geiger-Mueller tube and observe the
   terminal output.

   .. figure:: cn0536_uranium_ore_test.jpg
      :width: 600 px
      :align: center

      EVAL-CN0536-ARDZ Connected to the EVAL-ADICUP3029 Next to a Uranium Ore
      Sample

.. figure:: cn0536_mounted.png
   :width: 600 px
   :align: center

   EVAL-CN0536-ARDZ Mounted on the EVAL-ADICUP3029 Platform Board

Supported GM Tubes
------------------

The CN0536 was tested with several different GM tubes. The figures below
present the sensors' sensitivity levels, materials used, and operating ranges.

.. figure:: gm_sensor_tubes.png
   :width: 600 px
   :align: center

   Geiger-Mueller Sensor Tubes

.. figure:: gm_tubes_specifications.png
   :width: 600 px
   :align: center

   Geiger-Mueller Tubes Specifications

Adjusting the R\ :sub:`pot` configurations ensures that each GM tube operates
correctly and efficiently. Test results with different GM tubes are shown below.

.. figure:: gm_tube_7129_test.png
   :width: 800 px
   :align: center

   GM Tube 7129: (a) Serial Display (b) CN0536 with GM Tube and EVAL-ADICUP3029

.. figure:: gm_tube_7121_test.png
   :width: 800 px
   :align: center

   GM Tube 7121: (a) Serial Display (b) CN0536 with GM Tube and EVAL-ADICUP3029

.. figure:: gm_tube_7124_test.png
   :width: 800 px
   :align: center

   GM Tube 7124: (a) Serial Display (b) CN0536 with GM Tube and EVAL-ADICUP3029

Schematic, PCB Layout, Bill of Materials
----------------------------------------

`CN0536 Design & Integration Files <https://www.analog.com/cn0536-DesignSupport>`__

- Schematics
- PCB Layout
- Allegro Project
- Bill of Materials

More Information and Useful Links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`CN0536 Circuit Note Page <CN0536>`
- :adi:`LT6906 Product Page <LT6906-1>`
- :adi:`LTC6994 Product Page <LTC6994-1>`
- :adi:`LTC1540 Product Page <LTC1540>`
- :adi:`LTC1441 Product Page <LTC1441>`

Help and Support
~~~~~~~~~~~~~~~~

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
