.. _eval-ada4355-fmc:

EVAL-ADA4355-FMC
===============================================================================

Evaluating the ADA4355/ADA4356 Receive uModule.

.. image:: images/ada4355_chip.jpg
   :align: left
   :width: 150

.. image:: images/ada4356_chip.jpg
   :align: left
   :width: 150

.. clear-content::

This user guide will discuss how to use the evaluation boards and
software to configure and collect data from the :adi:`EVAL-ADA4355EBZ`
and :adi:`EVAL-ADA4356EBZ` boards.

Overview
-------------------------------------------------------------------------------

The :adi:`ADA4355` and :adi:`ADA4356` are integrated receive
uModules that combine a programmable gain transimpedance amplifier
(PGTIA), a fully differential amplifier (FDA), a low-pass filter,
and a high-speed ADC in a single package. These devices are designed
for optical time-domain reflectometry (OTDR), LiDAR, and fiber
sensing applications.

Two evaluation platforms are available:

- **EVAL-ADA4355EBZ** --- evaluates the :adi:`ADA4355` using a
  Xilinx KC705 FPGA platform with a MATLAB-based GUI.
- **EVAL-ADA4356EBZ** --- evaluates the :adi:`ADA4356` using a
  ZedBoard FPGA platform with Linux, HDL, PyADI-IIO, and
  IIO Oscilloscope.

.. note::

   Although the GitHub URLs and filenames refer to ADA4355, the
   software is for ADA4356 as well.

.. image:: images/ada4356_front.jpg
   :align: center
   :width: 500

.. image:: images/ada4356_bottom.jpg
   :align: center
   :width: 500

Features:

- Programmable gain transimpedance amplifier (PGTIA)
- Fully differential amplifier (FDA)
- Programmable low-pass filter
- Integrated high-speed ADC (14-bit, 125 MSPS)
- On-board buffered Howland current source (BHCS)
  (EVAL-ADA4356EBZ)
- On-board high-voltage APD bias generator (EVAL-ADA4355EBZ)

Applications:

- Optical time-domain reflectometry (OTDR)
- LiDAR
- Fiber sensing
- Optical power monitoring

.. toctree::
   :hidden:

   eval-ada4355ebz
   eval-ada4356ebz
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

   #. :ref:`eval-ada4355ebz` --- ADA4355 on KC705 (MATLAB GUI)
   #. :ref:`eval-ada4356ebz` --- ADA4356 on ZedBoard
      (Linux/HDL)
   #. :ref:`Prerequisites <eval-ada4355-fmc prerequisites>` - what
      you need to get started
   #. :ref:`Quick start guides <eval-ada4355-fmc quickstart>`:

      #. Using the
         :ref:`ZedBoard <eval-ada4355-fmc quickstart zed>` (FPGA)

#. Use the board to better understand the :adi:`ADA4356`

   #. :external+kuiper:doc:`Configure a SD Card <hardware-configuration>`
   #. :external+kuiper:doc:`Update the SD Card <repositories>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`
      #. :external+scopy:doc:`Scopy <index>`

#. Design with the ADA4355/ADA4356

   #. HDL software

      #. :git-hdl:`ADA4355-FMC HDL Reference Design <projects/ada4355_fmc>`

   #. Python software

      #. :git-pyadi-iio:`PyADI-IIO ADA4355 driver <adi>`

#. :ref:`Help and Support <help-and-support>`

More Information and Useful Links
-------------------------------------------------------------------------------

- :adi:`ADA4355 Product Page <ADA4355>`
- :adi:`ADA4356 Product Page <ADA4356>`
- `EVAL-ADA4356EBZ User Guide (PDF) <https://www.analog.com/media/en/technical-documentation/user-guides/eval-ada4356ebz.pdf>`__

Software Projects and Platforms
-------------------------------------------------------------------------------

- :ref:`EVAL-ADA4356EBZ + ZedBoard <eval-ada4355-fmc quickstart zed>`
- :git-hdl:`ADA4355-FMC HDL project <projects/ada4355_fmc>`
- :git-pyadi-iio:`PyADI-IIO ADA4355 driver <adi>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
