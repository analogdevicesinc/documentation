.. _eval-cn0564-ardz:

EVAL-CN0564-ARDZ
================

Long-Distance SPI/I2C Communication Using Robust Differential Transceivers.

Overview
--------

.. figure:: pcb_main.png
   :width: 600 px
   :align: center

   EVAL-CN0564-ARDZ Evaluation Board

Monitoring and data acquisition systems require direct access to sensors and
actuators, preferably from a remote location and by means of a standardized
communication method. I2C and SPI are examples of highly ubiquitous digital
interfaces using synchronous serial communication. However, the distance
limitation is one of the key disadvantages of these interfaces.

The :adi:`EVAL-CN0564-ARDZ <CN0564>` solves the problem of long-distance,
robust SPI/I2C communication simply and easily without sacrifices to
component count, operating speed, or software complexity. The solution uses
the :adi:`LTC4331` (I2C extender) and :adi:`LTC4332` (SPI extender) to extend
I2C/SPI signals up to 1200 m over a twisted pair cable.

.. figure:: final_figure_1.png
   :width: 800 px
   :align: center

   EVAL-CN0564-ARDZ System Topology

The SPI/I2C extenders feature robust transceivers which operate over an
extended common mode range of +/-25 V (for SPI communication) and +/-15 V
(for I2C communication) for distances up to 1200 m. Each link consists of a
single device at either end of the cable, capable of being powered from 3 V
to 5.5 V, while a separate logic supply allows the I2C or SPI interface to
operate from 1.62 V to 5.5 V.

Features
~~~~~~~~

- Extends SPI/I2C communication up to 1200 m over twisted pair cable
- +/-60 V fault-protected differential transceivers
- +/-40 kV HBM ESD protection on interface pins
- Selectable baud rates to balance performance with cable length
- Interrupt/alert signal mirroring from remote to local network
- Arduino shield form factor for easy evaluation
- Splittable PCB with V-groove for local/remote pair separation
- Supports galvanic isolation using digital isolators

Applications
~~~~~~~~~~~~

.. figure:: apps_diagram.png
   :width: 600 px
   :align: center

   EVAL-CN0564-ARDZ Application Examples

- Condition-based monitoring
- Factory automation
- Building automation
- Structural monitoring
- Remote sensing in harsh environments

Required Equipment
------------------

- :adi:`EVAL-CN0564-ARDZ <CN0564>` Evaluation Board
- EVAL-ADXL357 Evaluation Board (for SPI extender example)
- EVAL-XLMOUNT1 Mechanical Interface
- `Arduino UNO Rev 3 <https://www.arduino.cc/en/Main/arduinoBoardUno>`__
- USB Type A to USB Type B cable
- Jumper wires
- 3 V to 5.5 V supply

Hardware Configuration
----------------------

The EVAL-CN0564-ARDZ features a local-remote pair of both :adi:`LTC4331`
(I2C extender) and :adi:`LTC4332` (SPI extender). It has Arduino headers for
easy evaluation and integration with the widely available Arduino UNO and
other Arduino-compatible devices. The remote-local pair can be split at the
V-groove on the PCB.

I2C Extender (LTC4331)
~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`LTC4331` enables data transmission required for I2C communication
between two devices. It encodes I2C signals from the controller into
differential signals with up to 1 MHz, which are transmitted through twisted
pair cables. At the remote end, another :adi:`LTC4331` decodes the
differential signals back into I2C signals.

**Power Supply Configuration:**

- Local side VCC is powered via the Arduino header (5 V or 3.3 V selectable
  via P10 jumper)
- VL (logic supply) is connected to the IOREF pin of the Arduino header
- Remote side can be powered from the local side VCC or from an external
  supply

SPI Extender (LTC4332)
~~~~~~~~~~~~~~~~~~~~~~

The :adi:`LTC4332` enables SPI communication between two devices over the
differential link with up to 2 MHz. SPI write requests to remote slave
devices are software transparent, but SPI read requests incur a one-byte
latency.

.. note::

   The SPI read command needs to be extended by one byte. If not, the last
   byte will be lost in the :adi:`LTC4332` MISO shift register when the
   slave select is de-asserted.

Galvanic Isolation
~~~~~~~~~~~~~~~~~~

The local :adi:`LTC4331`/:adi:`LTC4332` can be galvanically isolated from
the remote side using digital isolators like the :adi:`ADUM141E`/
:adi:`ADUM140E` and isolated power supply using the :adi:`ADUM5020`.

Accelerometer Example Using the SPI Extender
---------------------------------------------

The following example describes how to set up the EVAL-CN0564-ARDZ SPI
extender with a remote :adi:`ADXL357` MEMS accelerometer.

#. Download the Arduino sketch provided for evaluating the SPI extenders and
   program the Arduino.
#. Plug the EVAL-CN0564-ARDZ into the Arduino UNO Rev 3.
#. Connect the remote :adi:`LTC4332` to the EVAL-ADXL357 accelerometer
   breakout board (SS, MOSI, MISO, SCK, power, and ground connections).
#. Configure jumpers as described in the hardware documentation (P10, JP1,
   JP5, JP3, P1, P2, P19 settings).
#. Connect the local side :adi:`LTC4332` to the remote side via the P3/P6
   differential link headers.
#. Power up the boards. Three LEDs should illuminate on the EVAL-CN0564-ARDZ
   (2 on local, 1 on remote side).
#. Open the Serial Monitor or run the Python real-time plotter to view
   acceleration data from the remote :adi:`ADXL357`.

Schematic, PCB Layout, Bill of Materials
----------------------------------------

`EVAL-CN0564-ARDZ Design & Integration Files <https://www.analog.com/cn0564-designsupport>`__

- Schematics
- PCB Layout
- Bill of Materials

More Information and Useful Links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`CN0564 Circuit Note Page <CN0564>`
- :adi:`LTC4332 Product Page <LTC4332>`
- :adi:`LTC4331 Product Page <LTC4331>`
- :adi:`ADXL357 Product Page <ADXL357>`
- :adi:`ADUM141E Product Page <ADUM141E>`
- :adi:`ADUM140E Product Page <ADUM140E>`
- :adi:`ADUM5020 Product Page <ADUM5020>`

Help and Support
~~~~~~~~~~~~~~~~

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
