.. _eval-cn0506-fmcz:

EVAL-CN0506-FMCZ
===============================================================================

Dual-Channel, Low-Latency, Low-Power Ethernet PHY Evaluation Board.

.. image:: images/EVAL-CN0506-FMCZ-BOTTOM-web.png
   :align: center
   :width: 500

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-CN0506-FMCZ` is a dual-channel, low-latency, and low-power 
Ethernet PHY evaluation board that supports data rates of 10 Mbps, 100 Mbps, 
and 1000 Mbps, making it well-suited for industrial Ethernet applications.

The design integrates two independent 10/100/1000 Mbps PHY devices. Each PHY 
includes an Energy Efficient Ethernet (EEE) core along with the required analog 
front-end circuitry, clock buffering, management interface, subsystem 
registers, MAC interface, and control logic.

The :adi:`EVAL-CN0506-FMCZ` enables flexible interfacing between the MAC and 
PHY through MII, RMII, or RGMII interfaces. It is implemented as a VITA-57 FPGA 
mezzanine card (FMC) and can be connected via the low-pin-count (LPC) FMC 
connector to FPGA platforms such as the ZC706 evaluation board.

This setup provides a complete hardware environment for developing and 
evaluating industrial Ethernet designs.

Features:

- Dual independent 10/100/1000 Mbps Ethernet PHYs
- Energy Efficient Ethernet (EEE) support
- Flexible MAC interface (MII, RMII, RGMII)
- Low latency and power consumption
- VITA-57 FMC form factor
- Support for multiple FPGA carrier platforms

Applications:

- Industrial Ethernet systems
- Networked embedded systems
- FPGA-based data acquisition platforms

.. toctree::
   :hidden:

   prerequisites
   hardware
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`EVAL-CN0506-FMCZ`, we recommend using the 
evaluation board with your preferred FPGA carrier platform.

Table of contents
-------------------------------------------------------------------------------

#. Evaluating the :adi:`EVAL-CN0506-FMCZ`:

   #. :ref:`Prerequisites <eval-cn0506-fmcz prerequisites>` - what you need to 
      get started
   #. :ref:`Hardware User Guide <eval-cn0506-fmcz hardware>` - board overview 
      and specifications
   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`
   #. :ref:`Quick start guides <eval-cn0506-fmcz quickstart index>` - 
      step-by-step instructions for setting up the board with various FPGA 
      platforms:

      #. Using the :ref:`ZC706 <eval-cn0506-fmcz quickstart zc706>`
      #. Using the :ref:`ZCU102 <eval-cn0506-fmcz quickstart zcu102>`
      #. Using the :ref:`Zed Board <eval-cn0506-fmcz quickstart zed>`
      #. Using the :ref:`Arria 10 SoC <eval-cn0506-fmcz quickstart a10soc>`

#. Design with the :adi:`EVAL-CN0506-FMCZ`

   - :external+hdl:ref:`cn0506` - HDL reference design
   - :adi:`ADIN1300 product page <en/products/adin1300.html>`
   - :external+linux:ref:`adin` - Linux driver and software

#. :ref:`Help and Support <help-and-support>`

Registration
-------------------------------------------------------------------------------

.. tip::

   Receive software update notifications, documentation updates, view the 
   latest videos, and more when you register your hardware. 
   `Register <https://my.analog.com/en/app/registration/hardware/EVAL-CN0506-FMCZ?&v=RevB>`__ 
   to receive all these great benefits and more!