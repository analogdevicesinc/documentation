.. _pzsdr:

PZSDR
===============================================================================

The PicoZed SDR (PZSDR) family is a collection of software defined radio (SDR)
system on modules (SOMs), carrier cards, and complete portable radio reference
designs built around the :adi:`ADRV9361-Z7035` and :adi:`ADRV9364-Z7020` SOMs.
Each SOM pairs the :adi:`AD9361 <AD9361>` wideband RF transceiver with a Xilinx
Zynq®-7000 All Programmable SoC to provide a wide tuning range RF platform
(70 MHz – 6 GHz) for software developers, system architects, and product
developers moving from evaluation to field deployment.

.. image:: images/pelican_case.jpg
   :alt: ADRV-PackRF portable radio
   :align: center
   :width: 600

Overview
-------------------------------------------------------------------------------

The PZSDR ecosystem covers everything needed to go from a bare SOM to a fully
enclosed, battery backed, field deployable radio: breakout and FMC carrier
cards for bench evaluation, a PCIe carrier for host integration, power
sequencing and timing references, mechanical accessories to protect delicate
RF cabling, and the ADRV-PackRF portable radio reference design with its
carrier card, enclosure, and companion software stack.

Features:

- ADRV9361-Z7035 and ADRV9364-Z7020 SOMs based on the AD9361 RF transceiver
  and Xilinx Zynq-7000 SoC
- ADRV1CRR-BOB breakout and ADRV1CRR-FMC carrier cards for rapid bench
  evaluation
- PCIe carrier for host-connected designs
- ADRV-PackRF portable radio reference design: dual, hot-swappable-power,
  battery backed SDR nodes in a rugged aluminum enclosure
- ADM1166 Super Sequencer based power sequencing with margining and
  nonvolatile fault recording
- 3D-printable cable brackets to protect U.FL connections
- Production SD card creation flow for ADRV9361 RF SOM testing

Applications:

- Wireless communications infrastructure and backhaul
- Point-to-point wireless video and data links
- Portable and man-packable software defined radios
- RF system prototyping and algorithm development

.. figure:: images/blue_scorpion.jpg
   :align: center
   :width: 500

   ADRV-PackRF Portable Radio Reference Design

.. toctree::
   :hidden:

   cable-brackets
   carriers/brk
   carriers/fmc
   carriers/packrf
   carriers/packrf/example-use-case
   carriers/packrf/hardware
   carriers/packrf/system-software-architecture
   carriers/packrf/testing
   carriers/pcie
   carriers/portable-radio-reference-design
   carriers/portable-radio-reference-design/assembly-instructions
   carriers/portable-radio-reference-design/features
   carriers/portable-radio-reference-design/gallery
   power-and-sequencing
   testing/sd-cards

Table of Contents
-------------------------------------------------------------------------------

#. Carrier cards for the ADRV9361-Z7035 / ADRV9364-Z7020 SOMs

   #. :ref:`pzsdr carriers brk` — breakout carrier for bench evaluation
   #. :ref:`pzsdr carriers fmc` — FMC carrier card
   #. :ref:`pzsdr carriers pcie` — host-connected PCIe carrier
   #. :ref:`pzsdr carriers packrf` — dual portable radio reference design overview

      #. :ref:`pzsdr carriers packrf hardware`
      #. :ref:`pzsdr carriers packrf system-software-architecture`
      #. :ref:`pzsdr carriers packrf testing`
      #. :ref:`pzsdr carriers packrf example-use-case`

   #. :ref:`pzsdr carriers portable-radio-reference-design` — mechanical
      enclosure, carrier and software stack details

      #. :ref:`pzsdr carriers portable-radio-reference-design features`
      #. :ref:`pzsdr carriers portable-radio-reference-design assembly-instructions`
      #. :ref:`pzsdr carriers portable-radio-reference-design gallery`

#. :ref:`pzsdr power-and-sequencing` — ADM1166-based power sequencing,
   timing diagrams and margining information

#. :ref:`pzsdr cable-brackets` — 3D-printable U.FL cable protection

#. :ref:`pzsdr testing sd-cards` — building production test SD cards for the
   ADRV9361 RF SOM

#. :ref:`Help and Support <help-and-support>`

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
