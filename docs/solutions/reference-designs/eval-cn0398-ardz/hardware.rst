.. _eval-cn0398-ardz-hardware:

Hardware Guide
==============

The EVAL-CN0398-ARDZ shield connects to the :adi:`EVAL-ADICUP360 <ADICUP360>`
base board using the Arduino mating headers.

Equipment
---------

- EVAL-CN0398-ARDZ Evaluation Board
- EVAL-ADICUP360 Base Board
- PC with a USB port and Windows 7 (32-bit) or higher
- Serial Terminal Software (PuTTY/Tera Term or similar)
- 7 V to 12 V / 1 A DC power supply, or equivalent bench supply
- 3-wire moisture sensor
- pH sensor
- PT100 RTD

General Setup
-------------

- The EVAL-CN0398-ARDZ shield board connects to the EVAL-ADICUP360 base board.
- Power the system through the EVAL-ADICUP360 using an external wall wart
  (7 V to 12 V).
- Connect the system to the PC using a USB cable.
- Connect the sensors to the dedicated connectors.

Test Setup Functional Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: cn0398_blockdiagram.png
   :align: center
   :width: 500

   CN0398 test setup functional block diagram

Connectors and Jumper Configurations
-------------------------------------

Chip Select
~~~~~~~~~~~

.. figure:: cn0398_board_cs.png
   :align: center
   :width: 400

   EVAL-CN0398-ARDZ chip select jumper

.. figure:: cn0398_cs_jumper.png
   :align: center
   :width: 300

   Chip select jumper detail

The chip select is configurable to be routed to 3 general purpose I/O pins of
the board (digital pins 8, 9, and 10), allowing multiple boards using SPI
communications protocol to be stacked up.

As default, the shunt is placed across pins 1 and 2 of connector **P5** on the
EVAL-CN0398-ARDZ shield board, which associates to GPIO pin 10 of the
EVAL-ADICUP360.

Moisture Sensor Connector (P2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: cn0398_moisture.png
   :align: center
   :width: 300

   Moisture sensor connector

.. note::

   Any 3-wire moisture sensor with a supply voltage of 3.3 V or 5 V, and an
   output voltage of 0 V to 3 V can be used with the EVAL-CN0398-ARDZ. The
   Vegetronix `VH400 <http://www.vegetronix.com/Products/VH400/>`__ and Decagon
   Devices EC-5 moisture sensors were used during testing.

Moisture Sensor Power Supply Jumper Selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the moisture sensor requires a **5 V** power supply, place the jumpers as
follows:

.. figure:: cn0398_7vin.png
   :align: center
   :width: 300

   Jumper positions for 5 V moisture sensor (VH400)

.. note::

   The VH400 moisture sensor was evaluated in this configuration.

If the moisture sensor requires a **3.3 V** power supply, place the jumpers as
follows:

.. figure:: cn0398_5vin.png
   :align: center
   :width: 300

   Jumper positions for 3.3 V moisture sensor (EC-5)

.. note::

   The EC-5 moisture sensor was evaluated in this configuration. The two jumper
   selections P8 and P10 should always change together.

RTD Connector (P1)
~~~~~~~~~~~~~~~~~~

.. figure:: cn0398_rtd_connector.png
   :align: center
   :width: 300

   RTD connector

Possible RTD Configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The EVAL-CN0398-ARDZ supports 2-wire, 3-wire, and 4-wire RTD configurations:

.. figure:: cn0398_2wire.png
   :align: center
   :width: 200

   2-wire RTD configuration

.. figure:: cn0398_3wire.png
   :align: center
   :width: 200

   3-wire RTD configuration

.. figure:: cn0398_4wire.png
   :align: center
   :width: 200

   4-wire RTD configuration

.. note::

   A 3-wire **PT100** RTD was used during evaluation. Excitation currents are
   set to 500 uA. For the 4-wire configuration, do not connect the RSENSE(+)
   wire.

pH Probe Connector (J1)
~~~~~~~~~~~~~~~~~~~~~~~~

The EVAL-CN0398-ARDZ shield board comes with a BNC connector **J1** for pH
sensors.

.. figure:: cn0398_phprobe.png
   :align: center
   :width: 300

   pH probe BNC connector

The output of the pH sensor is bipolar and gives a maximum signal of +/-414 mV
at 25 C. The :adi:`AD7124-8` operates from a single power supply, therefore the
pH probe must be biased above ground so that it is within the acceptable
common-mode range of the ADC.

One of the integrated features of the :adi:`AD7124-8` is its internal bias
voltage generator that sets the common-mode voltage of a channel to AVDD/2, or
1.65 V. This bias voltage from the ADC is applied to the pH probe shield and
sets the output of the sensor to 1.65 V +/-414 mV at 25 C.

For information about pH calibration, visit the :adi:`CN0398 Circuit Note
<CN0398>`.

.. note::

   An `Atlas Scientific <http://www.atlas-scientific.com/product_pages/probes/ph_probe.html>`__
   pH probe was used during evaluation.
