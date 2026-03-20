.. _eval-cn0363-pmdz:

EVAL-CN0363-PMDZ
================================================================================

Dual-Channel Colorimeter with Synchronous Detection.

.. image:: images/colorimeter_photo.png
   :align: left

.. clear-content::

Overview
--------------------------------------------------------------------------------

The :adi:`EVAL-CN0363-PMDZ <CN0363>` is a dual channel colorimeter
featuring a modulated light source transmitter, programmable gain
transimpedance amplifiers on each channel, and a very low noise, 24-bit
sigma delta ADC. The output of the ADC connects via a standard PMOD
connector to a FPGA. The FPGA takes the sampled data from the ADC and
implements a synchronous detection algorithm. By using modulated light
and digital synchronous detection, rather than a constant (dc) source,
the system strongly rejects any noise sources at frequencies other than
the modulation frequency, providing excellent accuracy.

The dual channel circuit measures the ratio of light absorbed by the
liquids in the sample and reference containers at three different
wavelengths. This forms the basis of many chemical analysis and
environmental monitoring instruments used to measure concentrations and
characterize materials through absorption spectroscopy.

.. tip::

   Further details of the circuit can be found in the circuit note
   :adi:`CN0363`

.. _eval-cn0363-pmdz-introduction:

.. image:: images/cn0363_sch.jpg
   :align: center
   :width: 500

A clock set to a user-programmable frequency modulates one of the
three LED colors (R,G,B) with a constant current driver built around
the :adi:`AD8615` op amp, the :adi:`ADG819` switch, and the
:adi:`AD5201` digital potentiometer. The beam splitter sends half the
light through the
sample container and half through the reference container. The
:adi:`ADA4528-1`, configured as a transimpedance amplifier, then converts
the photodiode current into an output voltage square wave, whose amplitude
is proportional to the light transmitted through the sample or reference
containers. The transimpedance amplifiers use the ADG633 single-pole,
double-throw (SPDT) switches to select one of two transimpedance gains.
The :adi:`AD7175-2` Σ-Δ ADC samples the voltage and sends the digital
data to an FPGA for digital demodulation.

For a thorough circuit description, please visit
:adi:`CN0363 Circuit Note
<media/en/reference-design-documentation/reference-designs/CN0363.pdf>`.

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index
   Colorimeter Application <software/linux/colorimeter>

Recommendations
--------------------------------------------------------------------------------

People who follow the flow that is outlined have a much better
experience with things. However, like many things, documentation is
never as complete as it should be. If you have any questions, feel free
to ask on our EngineerZone forums,
but before that, please make sure you read our documentation thoroughly.

Table of contents
--------------------------------------------------------------------------------

#. Using the evaluation board:

   #. :ref:`User Guide <eval-cn0363-pmdz-user-guide>` - hardware and
      software guide
   #. :ref:`Prerequisites <eval-cn0363-pmdz-prerequisites>` - what you
      need to get started
   #. :ref:`Quick start guides <eval-cn0363-pmdz-quickstart>`:

      #. Using the :ref:`ZED Board <eval-cn0363-pmdz-quickstart-zynq>`

#. Software:

   #. :ref:`Colorimeter application <eval-cn0363-pmdz-colorimeter>`

Warning
--------------------------------------------------------------------------------

.. esd-warning::

Registration
--------------------------------------------------------------------------------

.. tip::

   Receive software update notifications, documentation updates, view
   the latest videos, and more when you register your hardware.
   `Register <https://form.analog.com/Form_Pages/FeedBack/EVAL-CN0363-PMDZ?&v=RevA>`_
   to receive all these great benefits and more!
