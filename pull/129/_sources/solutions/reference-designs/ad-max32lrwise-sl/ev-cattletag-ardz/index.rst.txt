.. _ev-cattletag-ardz:

EV-CATTLETAG-ARDZ
=================

Sensor for Livestock Tracking and Health Monitoring
"""""""""""""""""""""""""""""""""""""""""""""""""""

Overview
--------

The :adi:`EV-CATTLETAG-ARDZ` is an Arduino board with a fully integrated solution
for harvesting energy from single-/multicell solar sources. The device includes
battery chargers for small lithium-ion systems, and a digital temperature sensor
for applications such as Wearables and IoT. The system is consisting of a
:adi:`MAX20361` power harvester, :adi:`MAX20335 BMS <MAX20335>`, and a :adi:`MAX30210`
temperature sensor and a buzzer with an option for vibration motor.

.. figure:: ev-cattletag-ardz.jpg
   :width: 500 px

Features
~~~~~~~~

- Monitors the health and vitality of livestock in real-time, enabling farmers
  to quickly treat animals and prevent the spread of illness or disease.
- Tracks grazing animals to prevent loss and to identify grazing patterns.
- Gathers and analyzes historical data to identify trends in cattle health or to
  track the spread of illness.
- Monitors readiness to mate or give birth, preventing the loss of new calves
  and optimizing breeding practices.

Applications
~~~~~~~~~~~~

- Asset location
- Asset recovery
- Asset traceability
- Inventory management
- Asset loss and theft prevention

System Architecture
-------------------

.. figure:: ev-cattletag-ardz_block_diagram.png

Hardware Design
---------------

Components and Connections
~~~~~~~~~~~~~~~~~~~~~~~~~~

Power Supply
^^^^^^^^^^^^

When using the board, the power supply may come from different sources,
and these are listed below:

.. figure:: ev-cattletag-ardz_power_supply_input.png

- **Solar Panel** - use to recharge the lithium-ion connected to either P8 or to the
  2x AAA battery. An example of a probe that can be used is a product from
  AnySolar and its datasheet can be found
  `here <https://waf-e.dubudisk.com/anysolar.dubuplus.com/techsupport@anysolar.biz/O18Ae08/DubuDisk/www/Gen3/KXOB25-14X1F%20DATA%20SHEET%20202007.pdf>`__.
- **P6 Terminal block** - external power source (e.g., solar panel)

.. note:: When using an external power source, it is required to
      disconnect the on-board solar panel by removing the resistor **R30**.

.. figure:: ev-cattletag-ardz_solar_panel_option.png

- **P8 Terminal block** - external power supply, between 3V to 4.2V allowable
  input
- **Battery holder** - 2xAAA battery is required.
- **Arduino Power** - external power supply that comes directly from the host board
  it is connected to.

.. note:: When power supply directly from the host board is used, it is
      required to remove the **R84** resistor and placed a 0Ω resistor at **R86**.

.. figure:: ev-cattletag-ardz_power_source_option.png

Digital Interface (Arduino)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Arduino interface is a standardized digital interface for various digital
communication protocols such as SPI, I2C, and UART. These interface types were
standardized by Arduino, which is hardware and software company. Complete
details on the PMOD specification can be found
`here <https://www.arduino.cc/en/hardware>`__.

The pin map for the Arduino pins is described in the table and its schematic
diagram below.

.. figure:: ev-cattletag-ardz_arduino_connector.png

Applications
------------

The :adi:`EV-CATTLETAG-ARDZ` can be used with the :adi:`MAX32670-LR-ARDZ` Base Board,
which is a long-range wireless radio development platform based on MAX32670
ultralow power Arm Cortex-M4 microcontroller and LR1110 RF transceiver.

Using these platforms together enables users to design solutions based on
low-power, long range proprietary radio communication technique that is
suitable for customized heat/flow meters.

To learn more about the Long Range Wireless Radio solution developed by Analog
Devices, visit the
:ref:`AD-MAX32LRWISE-SL Long Range Wireless Radio Development Kit User Guide <ad-max32lrwise-sl>`.

System Setup
------------

PHASE 1: Hardware Setup
~~~~~~~~~~~~~~~~~~~~~~~~

Note that this setup only applies for MAX32670-LR-ARDZ Base Board. Users may use
a different base board or microcontroller, however the firmware built for this
demo application cannot be used as this is specifically designed for the
MAX32670-LR-ARDZ.

Equipment Needed
^^^^^^^^^^^^^^^^

- One (1) :adi:`MAX32670-LR-ARDZ` Base Board
- One (1) :adi:`EV-CATTLETAG-ARDZ` Sensor Node
- One (1) MAX32625PICO Rapid Development Platform with 10-pin ribbon cable
  with firmware image:
  `MAX32625PICO Firmware Image for MAX32670 <https://github.com/analogdevicesinc/max32625pico-firmware-images/raw/master/bin/max32625_max32670evkit_if_crc_swd_v1.0.3.bin>`__
- One (1) CR123A Battery or any equivalent external DC power supply (+3V to +4.7V)
  **Note that this is not included in the kit**
- One (1) Micro USB to USB cable
- Host PC (Windows 10 or later)

.. figure:: hardware_setup.png

#. Insert one CR123A battery (3V to 4.7V) into the battery holder (BT1
   connector) of the :adi:`MAX32670-LR-ARDZ` Base Board.

   **Make sure to check for the battery polarity in
   the BT1 connector, refer to the figure below. The DS3 LED will light up
   indicating that you have inserted the battery correctly and that power is
   provided in the base board.**

   .. figure:: max32670-lr-ardz_with_battery.png

#. Connect the :adi:`EV-CATTLETAG-ARDZ` Sensor Node to the
   :adi:`MAX32670-LR-ARDZ` Base Board by aligning the
   corresponding Arduino headers on each board.
#. Connect the :adi:`MAX32625PICO` programming adapter to the
   :adi:`MAX32670-LR-ARDZ` Base Board through the 10-pin
   ribbon cable.

   **Make sure that the MAX32625PICO programming adapter has been flashed with the
   correct image before connecting it to the MAX32670-LR-ARDZ Base Board. If you do
   not know how to load the image, click on the instructions below:**

How to flash the firmware image in the MAX32625PICO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Download the firmware image: `MAX32625PICO Firmware Image for
   MAX32670 <https://github.com/analogdevicesinc/max32625pico-firmware-images/raw/master/bin/max32625_max32670evkit_if_crc_swd_v1.0.3.bin>`__
#. Do not connect the MAX32625PICO to the
   :adi:`MAX32670-LR-ARDZ` Base Board yet.
#. Connect the MAX32625PICO to the Host PC using the micro USB to USB cable.
#. Press the button on the MAX32625PICO. **(Do not release the button until the
   MAINTENANCE drive is mounted)**.

   .. figure:: max32625pico_maxdap.png
      :width: 300 px

#. Release the button once the MAINTENANCE drive is mounted.
#. Drag and drop (to the MAINTENANCE drive) the firmware image.
#. After a few seconds, the MAINTENANCE drive will disappear and be replaced by
   a drive named DAPLINK. This indicates that the process is complete, and the
   MAX32625PICO can now be used to flash the firmware of the
   :adi:`MAX32670-LR-ARDZ` Base Board.

#. Connect the :adi:`MAX32625PICO` programming adapter to the
   Host PC using the micro USB to USB cable.

   .. figure:: max32670-lr-ardz_to_maxpico.png

Once you have completed this setup, proceed to PHASE 2 found in
:dokuwiki:`ADI Long Range Wireless Radio Software UserGuide </resources/eval/user-guides/longrangewirelessradio/software>`.

Resources
---------

- :adi:`MAX20361 Product Page <MAX20361>`
- :adi:`MAX20335 Product Page <MAX20335>`
- :adi:`MAX30210 Product Page <MAX30210>`

Design and Integration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

   :download:`EV-CATTLETAG-ARDZ Design Support Package Rev. C <ev-cattletag-ardz-designsupport.zip>`

   - Schematic
   - Bill of Materials
   - Layout
   - Fabrication Files

Help and Support
~~~~~~~~~~~~~~~~

For questions and more information about this product, connect with us through
the :ez:`Analog Devices Engineer Zone </>`.
