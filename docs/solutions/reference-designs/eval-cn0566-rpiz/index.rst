.. _eval-cn0566-rpiz:

CN0566 (ADALM-PHASER) Phased Array Exploration Platform
=======================================================

Introduction
------------

Phased array communications and radar systems are finding increased use in a
variety of applications. This places a greater importance on training
engineers and rapidly prototyping new phased array concepts. However, both
those imperatives have historically been difficult and expensive. That is why
Analog Devices launched the ADALM-PHASER. It is a low cost, simplified phased
array radar which allows real beamforming hardware to be used for education,
project proposals, and even software development.

Most of the labs are run on a Python GUI, with several helper scripts. These
can be run on a remote host computer, or directly on the phaser’s Raspberry Pi
computer with the addition of a keyboard, mouse, and display.

For more advanced application development, the Phaser is also supported in the
MATLAB RF Microwave Toolbox. Equivalent MATLAB lab exercises are in
development, and will be added below as they are completed.

Here is a brief video introduction to beamforming and the Phased Array Platform:

.. video:: https://www.youtube.com/watch?v=dUn2_fiOh94


Quick Start Guide
-----------------

There are a few steps that need to be performed before diving into the lab
exercises. Please visit the :ref:`Quick Start Guide <cn0566_quickstart>`.

Phased Array Hardware
---------------------

To get acquainted with the hardware, see the :ref:`Phaser Hardware
Overview <eval-cn0566-rpiz>` page.

Phased Array Software
---------------------

There are several pieces of software used with the CN0566 Phaser, including a
user-friendly Graphical User Interface (GUI) and a number of command-line
utilities. This page describes the various pieces of software:

- :ref:`Phaser Software Guide (GUI and CLI utilities) <cn0566_software>`
- :ref:`Phaser Software Guide for MATLAB <cn0566_matlab_setup>`

Phased Array Assembly and Testing
---------------------------------

The phaser ships fully assembled and ready to go. Should you need to re-assemble
a disassembled board, or do a quick functionality test, refer to this page:

- :ref:`CN0566 Assembly and Production Test <cn0566_assy_prod_test>`

Labs and Lectures
-----------------

The ADALM-PHASER is meant for you to experience, first hand, phased array
beamforming and radar concepts. But to go along with the hardware, we’ve put
together a series of short lectures followed by hands-on labs that you can
perform with your own Phaser. A complete, printable lab manual is available
here: 

.. admonition:: Download
  
  :download:`Printable Phaser Lab Instructions (DOCX)<phaser_lab_instructions.docx>`

  :download:`Printable Phaser Lab Instructions (PDF)<phaser_lab_instructions.pdf>`

The expanded list of topics is as follows:

- Phaser Hardware Overview, Software Setup, and Frequency Plan

  - :ref:`Phaser Hardware Overview <eval-cn0566-rpiz>`
  - Lecture Video

    .. video::  https://youtu.be/-Vqbgf0MjPk

- Basics of SDR and Beamforming Control

  - :ref:`Lab: Controlling the Phaser with Python <cn0566_basic_example>`
  - :ref:`Lab: Controlling the Phaser with MATLAB <cn0566_matlab_example>`

  - Lecture Video

    .. video:: https://www.youtube.com/watch?v=jBGzOlThpRE
      
  - Lab Video

    .. video:: https://www.youtube.com/watch?v=5lihNPh4Rm0
- Phased Array Beam Steering

  - :ref:`Lab Material <cn0566_lab2>`
  - Lecture and Lab Video

    .. video:: https://www.youtube.com/watch?v=5lihNPh4Rm0
      
- Phased Array Antenna Patterns

  - :ref:`Lab Material <cn0566_lab3>`
  - Lecture and Lab Video

    .. video:: https://www.youtube.com/watch?v=UQgmtWChNfM
      
- Sidelobes and Beam Tapering

  - :ref:`Lab Material <cn0566_lab4>`
  - Lecture and Lab Video

    .. video:: https://www.youtube.com/watch?v=be_5D4eNtCY
      
- Grating Lobes

  - :ref:`Lab Material <cn0566_lab5>`
  - Lecture and Lab Video

    .. video:: https://www.youtube.com/watch?v=qksh4lGysbI


- Beam Squint

  - :ref:`Lab Material <cn0566_lab6>`
  - Lecture and Lab Video

    .. video:: https://www.youtube.com/watch?v=LYVD014ClZI

- Quantization Sidelobes

  - Lecture and Lab Video

    .. video:: https://www.youtube.com/watch?v=51O5FLVZE4c

- Analog, Digital, and Hybrid Beamforming

  - Lecture and Lab Video

    .. video:: https://www.youtube.com/watch?v=hMiJs2NdXZY

- Monopulse Tracking

  - Lecture and Lab Video

    .. video:: https://www.youtube.com/watch?v=hZDopcNjVzY
      
- Radar: Simple FMCW

  - Lecture and Lab Video

    .. video:: https://www.youtube.com/watch?v=CXSbLQgRFAA

- Radar: CFAR, Range Normalization, Clutter Suppression, and Range/Velocity

  - Lab and Lecture Video

    .. video:: https://www.youtube.com/watch?v=igrN_wd_g74
      
Additional Resources
--------------------

This series is partially derived from several sources that also provide valuable
background information.

- Analogue Dialogue Phased array paper series:

  - :adi:`Phased Array Antenna Patterns—Part 1: Linear Array Beam Characteristics and Array Factor </analog-dialogue/articles/phased-array-antenna-patterns-part1>`
  - :adi:`Phased Array Antenna Patterns—Part 2: Grating Lobes and Beam Squint </analog-dialogue/articles/phased-array-antenna-patterns-part2>`
  - :adi:`Phased Array Antenna Patterns—Part 3: Sidelobes and Tapering </analog-dialogue/articles/phased-array-antenna-patterns-part3>`

More Information and Useful Links
---------------------------------

- :adi:`CN0566 Product Page <CN0566>`

.. toctree::
   :titlesonly:
   :maxdepth: 3
   :glob:

   */index
