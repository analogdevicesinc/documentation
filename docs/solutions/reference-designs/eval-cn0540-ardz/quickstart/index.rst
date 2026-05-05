.. _eval-cn0540-ardz quickstart:

Quickstart
===============================================================================

The Quick Start Guides provide step by step instructions on how to set up the
:adi:`EVAL-CN0540-ARDZ` board on various supported platforms, including FPGA
development boards (HDL/Linux) and MCU boards running a bare-metal MBED
application.

.. toctree::

   CoraZ7-07s <coraz7s>
   DE10-Nano <de10nano>
   SDP-K1 <sdp-k1>
   STM Discovery Kit <stm-discovery>

.. _eval-cn0540-ardz carriers:

Supported carriers
-------------------------------------------------------------------------------

The carriers we support are:

- `Cora Z7S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__ on Arduino shield connector
- :intel:`DE10-Nano <content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>` on Arduino shield connector
- :adi:`SDP-K1` on Arduino shield connector
- `32F746GDISCOVERY <https://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-mpu-eval-tools/stm32-mcu-mpu-eval-tools/stm32-discovery-kits/32f746gdiscovery.html>`__ on Arduino shield connector

Supported Environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - Board
     - HDL
     - Linux Software
     - No-OS Software
     - MBED
   - - `Cora Z7S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__
     - Yes
     - Yes
     - Yes
     - No
   - - :intel:`DE10-Nano <content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>`
     - Yes
     - Yes
     - Yes
     - No
   - - :adi:`SDP-K1`
     - No
     - No
     - No
     - Yes
   - - `32F746GDISCOVERY <https://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-mpu-eval-tools/stm32-mcu-mpu-eval-tools/stm32-discovery-kits/32f746gdiscovery.html>`__
     - No
     - No
     - No
     - Yes

Hardware Setup
-------------------------------------------------------------------------------

The :adi:`EVAL-CN0540-ARDZ` board connects to the Arduino
Shield connector (unless otherwise noted). The carrier setup requires power,
UART (115200), ethernet (Linux), HDMI (if available) and/or JTAG (no-OS)
connections.

A few typical setups are shown below.

CoraZ7-07s + EVAL-CN0540-ARDZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../images/cn0540_cora.jpg
   :align: center
   :width: 500

DE10-Nano + EVAL-CN0540-ARDZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../images/cn0540_de10nano.jpg
   :align: center
   :width: 500
