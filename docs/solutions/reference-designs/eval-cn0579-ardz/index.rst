.. _eval-cn0579-ardz:

EVAL-CN0579-ARDZ
===============================================================================

Quad-Channel IEPE Vibration Sensor Measurement System.

Overview
-------------------------------------------------------------------------------

Condition-based monitoring (CbM) enables early detection and diagnosis of
machine and system abnormalities. Identifying and isolating these issues
creates opportunities for optimizing replacement part inventories,
scheduling downtime for planned maintenance, and making run-time process
adjustments that can extend the life of equipment.

The :adi:`EVAL-CN0579-ARDZ` is a 4-channel, high resolution,
wide bandwidth, high dynamic range, IEPE-compatible interface data
acquisition (DAQ) system that interfaces with IC piezoelectric
(ICP®)/IEPE sensors. While most solutions that interface with
piezoelectric sensors in the market are AC-coupled and lack DC and
subhertz measurement capabilities, this solution is DC-coupled. By
looking at the complete data set from an IEPE vibration sensor in the
frequency domain (DC to 50 kHz), the type and source of a machine fault
can be better predicted using the position, amplitude, and number of
harmonics found in the fast Fourier transform (FFT) spectrum.

Features:

- Quad Channel IEPE-Compatible Vibration Sensor Interface
- Channel Independent Excitation Source and Sensor Bias Removal
  Circuitry
- Analog Overvoltage and Undervoltage Protection
- Sensor Frequency Response from DC up to 54 kHz
- Synchronized, Full Bandwidth Data Measurement and Capture

Applications:

- Machine condition-based monitoring and predictive maintenance
- Industrial vibration sensing and fault detection
- IEPE/ICP piezoelectric and MEMS sensor data acquisition
- DC-coupled wideband vibration analysis (DC to 50 kHz)

.. figure:: images/eval-cn0579-ardz_top-web.gif
   :alt: Photo of the EVAL-CN0579-ARDZ evaluation board
   :align: center
   :width: 800

   EVAL-CN0579-ARDZ Evaluation Board

.. toctree::
   :hidden:

   Prerequisites <prerequisites>
   User Guide <user-guide>
   Quick Start Guides <quickstart/index>

Recommendations
-------------------------------------------------------------------------------

People who follow the flow outlined below have a much better experience.
If you have any questions, feel free to ask on our
:ez:`ez/reference-designs`, but before that, please make sure you read
our documentation thoroughly.

To better understand the :adi:`EVAL-CN0579-ARDZ`, we recommend
using it together with a supported FPGA carrier board - either the
`Terasic DE10-Nano
<https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046>`__
or the `Digilent Cora Z7
<https://store.digilentinc.com/cora-z7-zynq-7000-single-core-and-dual-core-options-for-arm-fpga-soc-development>`__
- running the ADI Kuiper Linux image.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <eval-cn0579-ardz prerequisites>` - what you
      need to get started
   #. :ref:`User Guide <eval-cn0579-ardz user-guide>`
   #. :ref:`Quick start guides <eval-cn0579-ardz quickstart>`:

      #. :ref:`DE10-Nano <eval-cn0579-ardz quickstart de10-nano>`
      #. :ref:`Cora Z7 <eval-cn0579-ardz quickstart coraz7>`

   #. Linux Applications:

      #. :ref:`iio-oscilloscope`
      #. :ref:`pyadi-iio`

#. Design with the CN0579

   - :ref:`eval-cn0579-ardz block-diagram`

     - :adi:`CN0579 Circuit Note <CN0579>`

   - :ref:`Schematic, PCB Layout, Bill of Materials
     <eval-cn0579-ardz schematic>`

   - :ref:`Reference Demos and Software <eval-cn0579-ardz demos>`

#. :ref:`More Information <eval-cn0579-ardz more-info>`

#. :ref:`Help and Support <eval-cn0579-ardz help-and-support>`

.. _eval-cn0579-ardz block-diagram:

Block Diagram
-------------------------------------------------------------------------------

.. figure:: images/cn0579_simplified_block_diagram.png
   :alt: EVAL-CN0579-ARDZ simplified block diagram
   :align: center
   :width: 1000

   EVAL-CN0579-ARDZ simplified block diagram.

.. _eval-cn0579-ardz schematic:

Schematic, PCB Layout, Bill of Materials
-------------------------------------------------------------------------------

Design support files for the :adi:`EVAL-CN0579-ARDZ`,
including schematics, PCB layout, bill of materials, and Allegro project
files, are available for download: :download:`EVAL-CN0579-ARDZ Design and Integration Files <./files/cn0579-designsupport.zip>`

.. _eval-cn0579-ardz demos:

Reference Demos and Software
-------------------------------------------------------------------------------

- :ref:`PyADI-IIO Installation Guide <pyadi-iio>`
- :ref:`iio-oscilloscope`
- :ref:`Kuiper Images <kuiper>`
- :git-hdl:`CN0579 HDL Reference Design </projects/cn0579>`

.. _eval-cn0579-ardz more-info:

More Information
-------------------------------------------------------------------------------

- :adi:`CN0579 Circuit Note Page <CN0579>`
- :adi:`AD7768-4 Product Page <AD7768-4>`
- :adi:`AD5696R Product Page <AD5696R>`
- :adi:`ADA4807-2 Product Page <ADA4807-2>`
- :adi:`AD8605 Product Page <AD8605>`
- :adi:`ADA4945-1 Product Page <ADA4945-1>`
- :adi:`ADR4540 Product Page <ADR4540>`
- :adi:`ADP1613 Product Page <ADP1613>`
- :adi:`ADP7142 Product Page <ADP7142>`
- :adi:`ADG5421F Product Page <ADG5421F>`
- :adi:`ADP7118 Product Page <ADP7118>`
- :adi:`LT3092 Product Page <LT3092>`
- :adi:`LT8333 Product Page <LT8333>`

.. _eval-cn0579-ardz help-and-support:

Help and Support
-------------------------------------------------------------------------------

For questions and more information about this product, connect with us
through the Analog Devices :ez:`ez/reference-designs`.

Warning
-------------------------------------------------------------------------------

.. esd-warning::
