.. _eval-cn0414-ardz hardware:

Hardware Guide
==============

This section describes the hardware configuration and connector settings for
the :adi:`EVAL-CN0414-ARDZ <CN0414>` evaluation board.

Power Supply Considerations and Configuration (P3)
----------------------------------------------------

Terminal block **P3** is the power supply input (input range: +9.5 V to +36 V
DC). The EARTH terminal can be connected to an external earth connection, to
the GND terminal, or left floating if an external earth connection is not used.

.. figure:: images/cn0414_supply.png
   :align: center
   :width: 500

   Main Power Supply Setup

.. figure:: images/cn0414_p3_description.png
   :align: center
   :width: 300

   P3 Terminal Description

Analog Input Connections (P6 and P9)
-------------------------------------

The analog input circuit is designed for group-isolated industrial analog inputs
and can support voltage and current inputs in the following ranges:

- +/-5 V
- +/-10 V
- 0 V to 5 V
- 0 V to 10 V
- 4 mA to 20 mA
- 0 mA to 20 mA

.. figure:: images/cn0414_p6_p9_description.png
   :align: center
   :width: 400

   P6 and P9 Analog Input Terminal Description

ADC and HART Chip Select Jumper Configurations (P1 and P2)
-----------------------------------------------------------

Single Board Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If only a single board is used, connect jumpers P1 and P2 by shorting pin 1
and pin 2 on each header. This bypasses the decoder and directly selects the
ADC and HART chips.

.. list-table::
   :header-rows: 1

   * - P2 (HART) Position
     - P2 Description
     - P1 (ADC CS) Position
     - P1 Description
   * - Pin 1 & Pin 2
     - Skip decoder
     - Pin 1 & Pin 2
     - Skip decoder

.. figure:: images/hart_selection_single_j.png
   :align: center
   :width: 200

   P2 Jumper Position -- Single Board (HART Select)

.. figure:: images/cs_selection_single_j.png
   :align: center
   :width: 200

   P1 Jumper Position -- Single Board (ADC CS Select)

Multiple Boards Stacked
~~~~~~~~~~~~~~~~~~~~~~~~

If more than one board is stacked (up to four), each board must be set to a
different ADC and HART select address. Connect jumpers P1 and P2 as shown in
the table below, and ensure that the software is configured accordingly. On a
given board, set the ADC and HART address to the same position. If necessary,
the software can be changed to address the ADC and HART differently on a given
board.

.. list-table::
   :header-rows: 1

   * - Board
     - P2 (HART) Position
     - P2 Address
     - P1 (ADC CS) Position
     - P1 Address
   * - Board 0
     - Pin 4 & Pin 6
     - AIN2:AIN3 = 00
     - Pin 4 & Pin 6
     - AIN0:AIN1 = 00
   * - Board 1
     - Pin 3 & Pin 5
     - AIN2:AIN3 = 01
     - Pin 3 & Pin 5
     - AIN0:AIN1 = 01
   * - Board 2
     - Pin 7 & Pin 5
     - AIN2:AIN3 = 10
     - Pin 7 & Pin 5
     - AIN0:AIN1 = 10
   * - Board 3
     - Pin 8 & Pin 6
     - AIN2:AIN3 = 11
     - Pin 8 & Pin 6
     - AIN0:AIN1 = 11

.. figure:: images/cn0414_silkscreen_top.png
   :align: center
   :width: 500

   CN0414 Top Silkscreen with Jumper Locations (P1, P2)

EEPROM Address Configuration
------------------------------

For multiple boards configuration, it is **mandatory** to set a different
EEPROM address for each board. In this way, on software initialization, the
system configuration (how many boards, what type, and at what address) will be
determined.

The EEPROM address is set using the three solder jumpers P10, P11, and P12.
Each jumper can be set to either pin 2 & pin 3 (default) or pin 2 & pin 1.
The following table shows all eight possible address combinations:

.. list-table::
   :header-rows: 1

   * - P10 Jumper Position
     - P11 Jumper Position
     - P12 Jumper Position
     - Address
   * - Pin 2 & Pin 3
     - Pin 2 & Pin 3
     - Pin 2 & Pin 3
     - 0x50 (default)
   * - Pin 2 & Pin 1
     - Pin 2 & Pin 3
     - Pin 2 & Pin 3
     - 0x51
   * - Pin 2 & Pin 3
     - Pin 2 & Pin 1
     - Pin 2 & Pin 3
     - 0x52
   * - Pin 2 & Pin 1
     - Pin 2 & Pin 1
     - Pin 2 & Pin 3
     - 0x53
   * - Pin 2 & Pin 3
     - Pin 2 & Pin 3
     - Pin 2 & Pin 1
     - 0x54
   * - Pin 2 & Pin 1
     - Pin 2 & Pin 3
     - Pin 2 & Pin 1
     - 0x55
   * - Pin 2 & Pin 3
     - Pin 2 & Pin 1
     - Pin 2 & Pin 1
     - 0x56
   * - Pin 2 & Pin 1
     - Pin 2 & Pin 1
     - Pin 2 & Pin 1
     - 0x57

EEPROM Write Protection Configuration (JP1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If only a single board is being used, ensure that JP1 solder jumper is shorting
pins 2 and 3 (write protection enabled). If multiple boards are used, short
pins 1 and 2 (write protection disabled), allowing the EEPROM to be written
with board identification data.

.. list-table::
   :header-rows: 1

   * - JP1 Position
     - Description
   * - Pin 2 & Pin 3 (default)
     - Enable write protection (WP) -- single board operation
   * - Pin 2 & Pin 1
     - Disable write protection (WP) -- multi-board operation

.. figure:: images/jp1_s_d.png
   :align: center
   :width: 200

   JP1 Solder Jumper -- Single Board (WP Enabled)

.. figure:: images/jp1_m_d.png
   :align: center
   :width: 200

   JP1 Solder Jumper -- Multi Board (WP Disabled)

.. figure:: images/cn0414_silkscreen_bottom.png
   :align: center
   :width: 500

   CN0414 Bottom Silkscreen with JP1 and EEPROM Address Jumper Locations

LED Indicators
--------------

There are two LEDs on the board:

- **Power LED** -- On whenever the board is powered
- **Error LED** -- Off by default

.. figure:: images/cn0414_power_led.png
   :align: center
   :width: 400

   Power and Error LED Indicators
