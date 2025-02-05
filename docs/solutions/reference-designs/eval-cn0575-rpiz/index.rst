.. _eval-cn0575-rpiz:

EVAL-CN0575-RPIZ
================

10BASE-T1L Field Device Development Platform with Class 12 and 13 SPoE
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

General Description
-------------------

.. figure:: 63305_2.jpg
   :width: 400 px
   :align: right

   EVAL-CN0575-RPIZ Board

The :adi:`EVAL-CN0575-RPIZ <CN0575>` is a 10BASE-T1L MAC/PHY interface with
Single Pair Power over Ethernet (SPoE) for development of field devices and
applications on a Raspberry Pi platform board. The SPoE powered device (PD) and
isolated flyback regulator provide 5 V power to the platform board and attached
application circuitry. SPoE Class 12 (8.4 W, 24 V nominal) and Class 13 (7.7 W,
55 V nominal) are supported.

Designed for use on the Raspberry Pi platform, the CN0575 hardware features a
40-pin GPIO header, and follows the same mechanical dimensions as a standard HAT.

To allow board stacking and development of field device applications using
Raspberry Pi HATs, an additional GPIO header with extended leads is included
with each evaluation board. However, the :adi:`CN0575` can also be used on its
own as a basic temperature sensing field device with remote user input/output
via an onboard button and LED.

Evaluation Board Hardware
-------------------------

Primary Side
~~~~~~~~~~~~

.. figure:: eval-cn0575-rpiz-top-with-labels.png

   EVAL-CN0575-RPIZ Primary Side

10BASE-T1L Port (P1 and P2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: 10base-t1l-port.jpg

   10BASE-T1L Port

The :adi:`EVAL-CN0575-RPIZ <CN0575>` evaluation board uses a single
port 10BASE-T1L device and can be connected to a link partner using either one
of the two physical connectors provided:

- The **P1 terminal block** is used for connecting individual wires. Connect the
  twisted pair to pins 1 and 2, and the shield (if available) to pin 3. Secure
  the connections by tightening the screws on the terminal block.
- The **P2 port** is used for connecting standard IEC 63171-6 cables directly
  from a 10BASE-T1L-capable controller unit.

PHY Status Indicators (LED0 and LED1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**LED0** and **LED1** are the :adi:`ADIN1110`
status indicators, and can be configured to display various activities via the
device registers.

By default, **LED0** is set to turn on when a link is established and blink
when there is activity; while **LED1** is disabled. Refer to the LED Control

Register in the :adi:`ADIN1110` data sheet for a full list of
available functions.

General Purpose LED and Button (ALERT and TEST)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :adi:`EVAL-CN0575-RPIZ <CN0575>` evaluation board includes a simple
button (**TEST**) and LED (**ALERT**) circuit that can be respectively used as
a digital input and a general purpose indicator. This circuit is controlled by
the Raspberry Pi by default (via **GPIO16** and **GPIO26**), but can
alternatively be used with external hardware by changing the appropriate
jumper settings (refer to Connecting the General Purpose LED and Button to
External Hardware).

.. figure:: adin1110-leds.jpg

   General Purpose LED and Test Button

The **GPIO16** pin is normally pulled high in this circuit, but will read low
when the **TEST** button is pressed.

SPoE PD Power Class Selection (JP1 and JP2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, the :adi:`LTC9111` SPoE PD
controller included in the :adi:`CN0575` circuit is configured for
PD Class 12. If a different PD class is required for the application, the
**JP1** and **JP2** solder jumpers should be reconfigured to match the desired
class.

.. figure:: ltc9111-jumpers.jpg

   SPoE PD Power Class Jumpers

.. csv-table::
   :file: SPoE_PD_Power_Class_Selection.csv

The :adi:`EVAL-CN0575-RPIZ <CN0575>` was designed and evaluated for PD Classes
12 and 13. However, Classes 10 and 11 may still be
usable, depending on the power requirements of the Raspberry Pi model used (and
its peripherals).

.. warning::

   Do not use PD Classes 14 and 15.

   The :adi:`EVAL-CN0575-RPIZ <CN0575>` evaluation board is not designed to
   handle these higher power specifications.

Secondary Side
~~~~~~~~~~~~~~

.. figure:: eval-cn0575-rpiz-bottom-with-labels.png

   EVAL-CN0575-RPIZ Secondary Side

ADIN1110 SW Power-Down Enable and SPI Configuration (JP3 to JP5)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :adi:`EVAL-CN0575-RPIZ <CN0575>` evaluation board uses
the default hardware configuration for the PHY specified in the
:adi:`ADIN1110` data sheet. If a different operating mode is
required for the application, the :adi:`ADIN1110` should first be
placed into software power-down and then configured appropriately via the
device registers.

.. figure:: jp3-jp4-jp5.jpg

   ADIN1110 SW Power-Down Enable and SPI Configuration Pin

Refer to the table below on setting the **JP3** jumper to enable/disable the
software power-down feature:

.. csv-table::
   :file: JP3-Setting.csv

The :adi:`ADIN1110` supports both generic SPI and the OPEN
Alliance SPI protocol in its communication. Refer to the table below on
setting **JP4** and **JP5** to select the SPI protocol:

.. csv-table::
  :file: jp4-jp5-settings.csv

ADT75 I²C Bus Address Selection (JP6 to JP8)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The I²C bus address of the onboard :adi:`ADT75`
temperature sensor is dependent on the settings of the **JP13**, **JP14**, and
**JP15** solder jumpers. **Note:** The CN0575 device tree overlay in ADI
Kuiper Linux has the temperature sensor I²C address set to the default 0x48.

.. figure:: jp6-jp7-jp8.jpg

   ADT75 I²C Bus Address Selection

If there is a need to reassign the :adi:`ADT75` address, refer to the
following table:

.. csv-table::
  :file: I2C-Bus-Address-Selection.csv

Optional GPIO Pins (JP9 to JP13)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: jp11-jp12-jp13.jpg

   Optional GPIO Pins

By default, some functions of the :adi:`ADT75` are
connected to various GPIO pins of the Raspberry Pi. If these features will not
be used in the application, the corresponding jumpers can be removed - doing
this will allow these GPIO pins to be used for other external hardware.

.. csv-table::
  :file: Optional-GPIO-Pins.csv

General Purpose LED and Button Connections (JP14 and JP15)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: jp14-jp15.jpg

   General Purpose LED and Button Connections

While normally functioning as a digital input and general
purpose indicator respectively, the **TEST** button and **ALERT** LED can
alternatively be used for external applications by changing the settings of
the appropriate jumpers. **JP14** is used to set the button connection, while
**JP15** is used to set the LED connection.

.. csv-table::
  :file: JP14-setting.csv

.. csv-table:: JP15 Setting
  :file: JP15-Setting.csv

.. tip::

   External hardware can be connected to the **TEST**
   button and **ALERT** LED using the **BTN_IO** and **LED_IO** test points,
   respectively.

System Setup
------------

**Required Equipment**

**Hardware**

- :adi:`EVAL-CN0575-RPIZ <CN0575>` Circuit Evaluation Board
- Raspberry Pi Model 3B (or higher)
- Micro-SD Card for Raspberry Pi
- 10BASE-T1L media converter, either:

  - :adi:`EVAL-ADIN1100EBZ <eval-adin1100>` Product Evaluation Board
  - Other 10BASE-T to 10BASE-T1L media converter
  - USB to 10BASE-T1L

- Power Source, either:

  - 10BASE-T1L Power Coupling Network Board w/ SPoE PSE or DC Power Supply
  - USB-C or USB-Micro 5V wall adapter (plugged directly into Raspberry Pi)

- Host Windows, Linux, or Mac computer

**Software**

- :ref:`kuiper`
- `PuTTY <https://www.putty.org/>`__

**Documentation**

- :adi:`CN0575` Circuit Note

Block Diagram
~~~~~~~~~~~~~

Setup with SPoE via PSE or DC Power Supply
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Power coupling boards compatible with the EVAL-ADIN1100 for
various SPoE classes and droop levels are in development. Alternatively, use a
media converter that supports SPoE PSE functionality.

Refer to the LTC4296-1 datasheet for example coupling networks.

.. figure:: test-setup-block-diagram.png

   Test Setup with SPoE via PSE or DC Power Supply

Setup without SPoE (USB-Powered Application)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: block_diagram-new-2.png

   Test Setup without SPoE (USB-Powered Application)

Software Setup
~~~~~~~~~~~~~~

Downloading and Flashing the Micro-SD Card
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To use the :adi:`EVAL-CN0575-RPIZ <CN0575>` with the Raspberry Pi, the
micro-SD card should be preloaded with :ref:`kuiper`,
a distribution based on Raspbian from the Raspberry Pi Foundation that
incorporates Linux drivers for ADI products as well as tools and other
software products.

Complete instructions, including where to download the SD card image, how to
write it to the micro-SD card, and how to configure the system are provided at
:ref:`kuiper`.

.. figure:: command_prompt.png

   Flashing the Micro-SD using Kuiper Linux

Configuring the Micro-SD Card
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Linux kernel requires a matching device tree overlay to identify the
devices on the CN0575. The overlay table is included with the :ref:`kuiper`
and simply needs to be enabled.

To do this, follow the Hardware Configuration procedure under **Configuring
the SD Card for Raspberry Pi Projects** in the :ref:`kuiper` page.
Enable the CN0575 overlay by adding the following line to *config.txt*:

::

   dtoverlay=rpi-cn0575

Save the table and reboot the system by entering the following command in the console:

.. shell::
   :user: analog
   :group: analog
   :show-user:

   $sudo reboot

Determining the IP Address of the CN0575
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow the below procedure to determine the IP address assigned by the Raspberry
Pi to the :adi:`EVAL-CN0575-RPIZ <CN0575>`:

#. Complete the hardware setup described in the Basic Operation section.
#. Remove the Ethernet cable from the :adi:`EVAL-ADIN1100EBZ <eval-adin1100>`
   evaluation board and connect it directly to the Raspberry Pi.
#. Run PuTTY and connect to the Raspberry Pi via SSH. For the Host Name (or IP
   address), use **analog.local**.
#. Enter the command *ifconfig* in the console.
#. The IP address of the :adi:`EVAL-CN0575-RPIZ <CN0575>` board will be listed
   as inet under adin1110-0. In the example below, the IP address is
   169.254.158.120.

.. figure:: ifconfig.png

   EVAL-CN0575-RPIZ IP Address

Basic Operation
~~~~~~~~~~~~~~~

.. figure:: setup.jpg

   Complete Evaluation Setup

To establish a 10BASE-T1L connection to a Raspberry Pi using the
:adi:`EVAL-CN0575-RPIZ <CN0575>` evaluation board and run a basic temperature
measurement example, follow the below procedure:

#. Ensure that the jumpers and switches of the :adi:`EVAL-ADIN1100EBZ <eval-adin1100>` are configured to the default settings.

#. Insert the micro-SD card into its slot on the Raspberry Pi.

#. Connect the :adi:`EVAL-CN0575-RPIZ <CN0575>` circuit evaluation board to the Raspberry Pi GPIO header.

#. Using an Ethernet cable, connect **P5** on the
   :adi:`EVAL-ADIN1100EBZ <eval-adin1100>` evaluation board to an RJ45 port on
   the computer.

#. Using a micro-USB cable, connect **P401** on the
   :adi:`EVAL-ADIN1100EBZ <eval-adin1100>` evaluation board to a USB port on
   the computer.

#. *Operation with SPoE PSE or DC Power Supply: (Skip to step 7 if using a USB
   wall adapter instead)*

   * Set the output of the PSE or DC power supply to either 24V (Class 12) or
     55V (Class 13), depending on the settings of **JP1** and **JP2** on the CN0575 board.
   * Using wires, connect the output of an SPoE power coupler to the **P1**
     terminal block on the :adi:`EVAL-CN0575-RPIZ <CN0575>` circuit evaluation
     board. Similarly, connect the data input of the power coupler to the **P101**
     terminal block on the :adi:`EVAL-ADIN1100EBZ <EVAL-ADIN1100>` evaluation board.

   * Connect the output of the SPoE PSE (or DC power supply) to the power input of the SPoE power coupler and enable it.

#. *Operation without SPoE (USB-Powered Application):*

   * Using wires, connect the **P1** terminal block on the :adi:`EVAL-CN0575-RPIZ <CN0575>`
     circuit evaluation board to the **P101** terminal block on the
     :adi:`EVAL-ADIN1100EBZ <EVAL-ADIN1100>` evaluation board.

   * Connect the USB wall adapter to the power connector on the Raspberry Pi.

#. Wait for the **LINK** LED on the :adi:`EVAL-CN0575-RPIZ <CN0575>` circuit
   evaluation board and the **LED_0** LED on the :adi:`EVAL-ADIN1100EBZ <EVAL-ADIN1100>`
   evaluation board to turn on and start blinking at the same time.
   This indicates that a 10BASE-T1L link has been established.

#. On the host PC, run PuTTY and connect to the Raspberry Pi using the
   :adi:`EVAL-CN0575-RPIZ <CN0575>` IP address.

#. In the Raspberry Pi console, navigate to the examples directory of pyadi-iio.
   Run the temperature measurement example by entering the following command:

.. shell::

   /path/pyadi-iio/examples
   $sudo python lm75_example.py

.. figure:: adt75-example.png

   Sample Readout

More Complete Example with Digital I/O
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A more complete example that blinks the onboard LED and reads the push button
is also provided. Note that this script can be run either directly on the
Raspberry Pi, or remotely from a host computer.
From the Raspberry Pi command line, run:

.. shell::

   /path/pyadi-iio/examples
   $sudo python cn0575_example.py

Or from PowerShell on a Windows remote host, run:

.. shell:: ps1

   /c/path/pyadi-iio/examples
   $python .\cn0575_example.py

The script will attempt to automatically locate the CN0575 over the network
connection. The CN0575’s IIO context URI can also be passed to the script
explicitly, where **www.xxx.yyy.zzz** is the board’s IP address:

.. shell:: ps1

   /c/path/to/pyadi-iio/examples
   $python .\cn0575_example.py ip:www.xxx.yyy.zzz

Typical output is shown below:

.. figure:: cn0575_example_screenshot.png

   CN0575 Output Example

Errata
------

.. figure:: c16_marking.png

   Erroneous Marking on C16

The first batch of :adi:`EVAL-CN0575-RPIZ <CN0575>` circuit
evaluation boards that was produced mistakenly have a 50V capacitor installed
on C16. This voltage rating is insufficient for Class 13 operation where the
SPoE voltage can be as high as 58 V (and potentially even more during surge
events).

These boards can be identified by the last three letters on C16 (HTH, shown
right). If you have one of these and intend to use it in a Class 13
application, either replace C16 with a 100 V capacitor (preferred; this is the
same rating used in later batches of the :adi:`EVAL-CN0575-RPIZ <CN0575>`),
or simply desolder it and leave it empty.

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

  :download:`EVAL-CN0575-RPIZ Design & Integration Files <CN0575-DesignSupport.zip>`

  - Schematics
  - PCB Layout
  - Bill of Materials
  - Allegro Project

Additional Information and Useful Links
---------------------------------------

- :adi:`CN0575 Circuit Note Page <CN0575>`
- :adi:`CN0575 Design Support Package <CN0575-DesignSupport>`
- :adi:`ADIN1110 Product Page <ADIN1110>`
- :adi:`ADT75 Product Page <ADT75>`
- :adi:`LTC9111 Product Page <LTC9111>`
- :adi:`LT8304 Product Page <LT8304>`
- :dokuwiki:`ADIN1110 Linux Driver <resources/tools-software/linux-drivers/net-mac-phy/adin1110>`
- `ADT75 Linux Driver <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm75.c?id=HEAD>`_

Hardware Registration
---------------------

.. tip::

   Receive software update notifications, documentation updates, view the latest
   videos, and more when you :adi:`register <EVAL-CN0575-RPIZ?&v=RevC>` your hardware.

Help and Support
-------------------

For questions and more information about this product, connect with us through the Analog Devices :ez:`/` .
