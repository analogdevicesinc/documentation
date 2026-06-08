.. _ad719x_asdz_quickstart:

Quick start
===========

The following steps highlight the process to begin using the
:adi:`EVAL-AD719x-ASDZ <EVAL-AD7192ASDZ>`
evaluation board with a controller board and the ACE software on a Windows PC.

.. toctree::
   :hidden:

   ace-software/ace-software-guide
   coraz7s
   de10nano

.. _ad719x_asdz_carriers:

Supported carriers
------------------

The :adi:`EVAL-AD719x-ASDZ <EVAL-AD7192ASDZ>`
connects to a controller board via a 120-pin connector or alternatively, Arduino
and Pmod connectors.

The controller boards we support are:

.. list-table::
   :header-rows: 1

   - - Controller board
     - Connector
   - - :adi:`EVAL-SDP-CK1Z <SDP-K1>`
     - 120-pin / Arduino
   - - :adi:`EVAL-SDP-CB1Z <SDP-B>`
     - 120-pin
   - - `Cora Z7S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__
     - Pmod JA / Arduino shield
   - - :intel:`DE10-Nano <content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>`
     - Arduino shield

Supported environments
----------------------

.. list-table::
   :header-rows: 1

   - - Controller board
     - HDL
     - Linux software
     - No-OS software
     - ACE Software
   - - :adi:`EVAL-SDP-CK1Z <SDP-K1>`
     - ---
     - ---
     - ---
     - Yes
   - - :adi:`EVAL-SDP-CB1Z <SDP-B>`
     - ---
     - ---
     - ---
     - Yes
   - - `Cora Z7S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__
     - Yes
     - Yes
     - ---
     - ---
   - - :intel:`DE10-Nano <content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>`
     - Yes
     - Yes
     - ---
     - ---
   - - `Zedboard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board/>`__
     - ---
     - ---
     - Yes
     - ---

.. _ad719x_asdz_hardware_setup:

Hardware Setup
--------------

.. warning::

   Ensure the SDP board is not connected to the USB port of the PC before
   connecting the evaluation board.

On most carriers, the EVAL-AD719X-ASDZ boards connect to the Arduino shield
connector (unless otherwise noted). The carrier setup requires power, UART
(115200), Ethernet (Linux), HDMI (if available) and/or JTAG (no-OS) connections.
A few typical setups are shown below.

EVAL-AD719x-ASDZ + EVAL-SDP-CK1Z
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Using the 120-pin connector: screw the two boards together using the
  plastic screw-washer set included in the evaluation board kit to ensure
  that the boards are connected firmly together.
- Using the Arduino connectors:

  .. image:: ../images/sdp_connect.png
     :width: 400

EVAL-AD719x-ASDZ + EVAL-SDP-CB1Z
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Using the 120-pin connector: screw the two boards together using the
  plastic screw-washer set included in the evaluation board kit to ensure
  that the boards are connected firmly together.

EVAL-AD719x-ASDZ + Cora Z7
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Using the Pmod JA connector (default HDL configuration).

  .. image:: ../images/cora_ad719x_pmod.png
     :width: 500

- Using the Arduino shield connector (HDL built with ``ARDZ_Pmod_N=1``).

  .. image:: ../images/cora_ad719x_arduino.png
     :width: 500

EVAL-AD719x-ASDZ + DE10-Nano
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Using the Arduino shield connector.

  .. image:: ../images/de10nano_ad719x_arduino.png
     :width: 500

Getting started
---------------

Once the hardware is set up, follow the
:ref:`Software guide <ad719x_asdz_software_guide>` for ACE plugin installation,
operation, and demo modes.
