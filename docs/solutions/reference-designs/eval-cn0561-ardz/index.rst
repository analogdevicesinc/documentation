.. _eval-cn0561-ardz:

EVAL-CN0561-ARDZ
===============================================================================

Overview
--------

Monitoring the health of machinery can help predict changes in a machine’s
condition. There are many methods of tracking a machine’s condition, but
vibration analysis is the most commonly used one. By tracking the vibration
analysis data over time, one can determine when a fault or failure is going to
occur, along with the source of the fault. Knowing the condition of a certain
machine will help not only increase efficiency and productivity, but create a
safer working environment.

The reference design shown below, shows a high resolution, wide-bandwidth, high
dynamic range, Integrated Electronics Piezoelectric (IEPE) compatible interface
data acquisition system (DAQ) for interfacing with Integrated Circuit Piezo
(ICP)/IEPE piezo vibration sensors. This reference design is an AC-coupled
solution targeted for wide band IEPE based sensors.

.. figure:: images/cn0561_eval-cn0561-ardz_angle-evaluation-board.jpg
   :align: center
   :width: 400

   EVAL-CN0561-ARDZ evaluation board.

By looking at the complete data set from the vibration sensor in the frequency
domain (DC – 50 kHz), the type and source of a machine fault can be better
predicted using the; position, amplitude and number of harmonics found in the
FFT spectrum.

The data acquisition board incorporates a precision Alias free quad channel
24-bit, 1.496 MSPS Continuous time Sigma-delta ADC AD4134, instrumentation
amplifier with differential output LTC6373 and a 250mA programmable 2-terminal
current source LT3092. Analog input fault detection and protection is provided
by the switch ADG5462F. The data acquisition board is an Arduino compatible form
factor and can be interfaced and powered directly from most Arduino compatible
development board. :adi:`CN0561` has 2 channels of IEPE interface and has 2
channels for general data acquisition. :adi:`CN0561` shown below is for High
performance Piezo Accelerometer with Fault Protection.

Features
~~~~~~~~

-  Data acquisition solution fully characterized over -40°C to 85°C
-  Throughput of up to 1496 kSPS
-  Alias-free and resistive inputs: No low pass filter or Driver needed
-  Powered and interfaced directly through an Arduino compatible development
   board

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our :ref:`EngineerZone
forums <help-and-support>`, but before that, please make sure you read our
documentation thoroughly.

To better understand the :adi:`CN0561`, we recommend to use the
:adi:`EVAL-CN0561-ARDZ <CN0561>` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <eval-cn0561-ardz prerequisites>` - what you need to
      get started
   #. :ref:`Quick start guides <eval-cn0561-ardz quickstart>`:

      #. Using the :ref:`Zedboard/ Zynq‑7000 SoC <eval-cn0561-ardz quickstart
         zed>`
      #. Using the :ref:`CoraZ7-07s/ Zynq‑7000 SoC <eval-cn0561-ardz quickstart
         coraz7s>`
      #. Using the :ref:`DE10-Nano/ Cyclone V SoC <eval-cn0561-ardz quickstart
         de10nano>`

   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the CN0561

   - :ref:`eval-cn0561-ardz block-diagram`

     - :adi:`CN0561 product page <CN0561>`

   #. HDL reference design

      #. :external+hdl:ref:`HDL reference design <cn0561>` which you must use in
         your FPGA.
      #. :git-hdl:`CN0561 HDL Reference Design <projects/cn0561>` which you must
         use in your FPGA.

   #. More information

      #. :external+hdl:ref:`SPI Engine Framework <spi_engine>`

#. :ref:`Help and Support <help-and-support>`

.. _eval-cn0561-ardz block-diagram:

Simplified Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/cn0561_block_diagram.jpg
   :width: 1000

   CN0561 simplified block diagram.

Simplified Signal Chain Schematic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/cn0561_signal_chain_schematic.png
   :width: 800

   CN0561 simplified signal chain schematic.

.. toctree::
   :hidden:

   user-guide
   quickstart/index
   prerequisites

Additional Information and Useful Links
---------------------------------------

-  :adi:`CN0561 Circuit Note Page <CN0561>`
-  :adi:`CN0561 Design Support Package <CN0561-DesignSupport>`
-  :adi:`AD4134 Product Page <AD4134>`
-  :adi:`ADG5462F Product Page <ADG5462F>`
-  :adi:`ADR444 Product Page <ADR444>`
-  :adi:`ADG3308 Product Page <ADG3308>`
-  :adi:`LT3092 Product Page <LT3092>`
-  :adi:`LTC6373 Product Page <LTC6373>`

Warning
--------

.. esd-warning::

Help and support
----------------

Please go to :ref:`Help and Support <help-and-support>` page.
