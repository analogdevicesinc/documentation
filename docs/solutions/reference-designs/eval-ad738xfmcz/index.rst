.. _eval-ad738xfmcz:

EVAL-AD738xFMCZ
===============================================================================

Evaluating the AD738x Family of Simultaneous Sampling SAR ADCs.

.. image:: images/ad7380_dual_chip.jpg
   :width: 150
   :align: left

.. image:: images/ad7380_quad_chip.png
   :width: 150
   :align: left

.. clear-content::

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD738xFMCZ` evaluation board enables quick and easy
evaluation of the performance and features of the AD738x family of
devices.

The AD7380 family are dual and quad 16-bit, 14-bit, and 12-bit
pin-compatible, simultaneous sampling, high-speed, low-power,
successive approximation analog-to-digital converters (ADCs) that
operate from a 3.3 V power supply and feature throughput rates up to
4 MSPS. The analog input type is differential for the :adi:`AD7380`,
:adi:`AD7381`, :adi:`AD4680`, :adi:`AD4681`, :adi:`AD7380-4`,
:adi:`AD7389-4`, :adi:`AD7381-4` — these can accept a wide
common-mode input voltage and are sampled and converted on the
falling edge of CS. The :adi:`AD7383`, :adi:`AD7384`, :adi:`AD4682`
and :adi:`AD4683` have pseudo-differential inputs, while the
:adi:`AD7386`, :adi:`AD7387`, :adi:`AD7388`, :adi:`AD4684` and
:adi:`AD4685` have single-ended inputs. The AD7380 family has
optional integrated on-chip oversampling blocks to improve dynamic
range and reduce noise at lower bandwidths. An internal 2.5 V
reference is included; alternatively, an external reference up to
3.3 V can be used.

The dual devices are available in a 16-lead 3 mm x 3 mm LFCSP
package, while the quad devices are available in a 4 mm x 4 mm LFCSP
package. Both operate over a specified temperature range of -40 C to
+125 C.

.. list-table::
   :widths: auto

   * - .. figure:: images/eval-ad7380.jpg
          :width: 300

          EVAL-AD7380FMCZ
     - .. figure:: images/eval-ad7386-4.jpg
          :width: 300

          EVAL-AD7386-4FMCZ
     - .. figure:: images/eval-ad7381.jpg
          :width: 300

          EVAL-AD7381FMCZ

Features:

- Simultaneous sampling on all channels
- Throughput rates up to 4 MSPS
- 3.3 V single-supply operation
- Internal 2.5 V reference (external reference up to 3.3 V
  supported)
- On-chip oversampling and averaging blocks
- SPI-compatible serial interface
- Compatible with 1.8 V, 2.5 V, and 3.3 V logic interfaces
- FMC form factor for easy connection to FPGA carrier boards

Applications:

- Motor control position feedback and current sense
- Data acquisition systems
- EDFA applications
- I and Q demodulation
- SONAR
- Power quality monitoring

.. toctree::
   :hidden:

   user-guide
   linux-driver
   eval-ad7380-4fmcz
   eval-ad7386fmcz
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined have a much better
experience with things. However, like many things, documentation is
never as complete as it should be. If you have any questions, feel
free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that,
please make sure you read our documentation thoroughly.

Table of Contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we
   offer:

   #. :ref:`eval-ad738xfmcz user-guide` - what you need to know
      about the evaluation board
   #. :ref:`eval-ad738xfmcz linux-driver` - Linux IIO driver,
      devicetree configuration and driver testing
   #. :ref:`Prerequisites <eval-ad738xfmcz prerequisites>` - what
      you need to get started
   #. :ref:`Quick start guides <eval-ad738xfmcz quickstart>`:

      #. Using the
         :ref:`ZedBoard <eval-ad738xfmcz quickstart zed>` (FPGA)

#. Use the board to better understand the :adi:`EVAL-AD738xFMCZ`

   #. :external+kuiper:doc:`Configure a SD Card <hardware-configuration>`
   #. :external+kuiper:doc:`Update the SD Card <repositories>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`
      #. :external+scopy:doc:`Scopy <index>`

#. Design with the EVAL-AD738xFMCZ

   #. :ref:`eval-ad738xfmcz block-diagram`

      #. :adi:`AD7380 Product Page <AD7380>`
      #. :adi:`AD7381 Product Page <AD7381>`
      #. :adi:`AD7386 Product Page <AD7386>`

   #. Design a custom EVAL-AD738xFMCZ-based platform

      #. HDL software

         #. :git-hdl:`AD738x-FMC HDL Reference Design <projects/ad738x_fmc>`
            which you must use in your FPGA.

      #. No-OS software

         #. :git-no-OS:`AD738x No-OS Project <projects/ad738x_fmcz>`

      #. Linux software

         #. :git-linux:`AD738x Linux driver source code <drivers/iio/adc/ad7380.c>`
         #. :git-linux:`EVAL-AD7380FMCZ Linux device tree <arch/arm/boot/dts/xilinx/zynq-zed-adv7511-ad7380.dts>`

      #. More information

         #. :dokuwiki:`SPI Engine Framework <resources/fpga/peripherals/spi_engine>`

#. :ref:`Help and Support <help-and-support>`

.. _eval-ad738xfmcz block-diagram:

Simplified functional block diagram
-------------------------------------------------------------------------------

.. figure:: images/AD7380-7381-block_diagram.png

   AD7380/AD7381 Block Diagram

.. figure:: images/AD7380-7381-block_diagram1.png

   AD7380/AD7381 Block Diagram (Alternate)

.. figure:: images/AD7380-4-block-diagram.png

   AD7380-4 Block Diagram

More Information and Useful Links
-------------------------------------------------------------------------------

- :adi:`AD7380 Product Page <AD7380>`
- :adi:`AD7381 Product Page <AD7381>`
- :adi:`AD7383 Product Page <AD7383>`
- :adi:`AD7386 Product Page <AD7386>`
- :adi:`AD7380-4 Product Page <AD7380-4>`
- :adi:`ADAQ4380-4 Product Page <ADAQ4380-4>`

Software Projects and Platforms
-------------------------------------------------------------------------------

- :ref:`EVAL-AD738xFMCZ + ZedBoard <eval-ad738xfmcz quickstart zed>`
- :git-hdl:`AD738x-FMC HDL project <projects/ad738x_fmc>`
- :git-no-OS:`AD738x No-OS project <projects/ad738x_fmcz>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
