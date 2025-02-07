Embedded Baremetal
==================

.. note::

   This is a work in progress.

Introduction
~~~~~~~~~~~~

This workshop is designed to explore the fascinating world of baremetal programming, where you’ll learn to operate software that runs directly on the hardware.
We’ll start by understanding what baremetal programming is and why it’s important.
Through interactive demonstrations and hands-on activities, you’ll gain practical experience and see how these concepts apply to real-world projects. Let’s dive in and start our journey into the world of embedded systems!

Theoretical content
~~~~~~~~~~~~~~~~~~~

- Baremetal Background
- What is no-OS
- no-OS Device Drivers
- No-OS API and Platforms
- No-OS Projects
- IIO Concepts
- ADXL355 part
- NO-OS Device Drivers Takeaways
- Hands-on Activity

**Baremetal Background**

Traditionally, industry chip manufacturers would sell ICs without accompanying software:

- Chip

- Datasheet

- Pseudocode with an initialization sequence and/or sequence of data acquisition

Complex parts require complex software.

ICs are everywhere.

.. grid::
   :widths: 50% 50%

   .. image:: noos.png
      :width: 300
      :alt: no os

   .. image:: noos1.png
      :width: 300
      :alt: no os

ADI addressed this issue and started providing software for its parts as well.

There is a market advantage in selling parts with accompanying software.

Baremetal projects deliverables 10 years ago consisted of:

- A .zip file containing the driver files
- A .zip file containing a project

.. figure:: noos10.png
   :align: center
   :width: 300

   Old Drivers structure

What ADI tried to do back then was to write an ADI driver for an ADI part, provided that we were selling the evaluation board with ADI part on it
The communication driver would be specific for each microcontroller or system board we would use: Maxim, Microchip, STM, etc
The structure was mainly containing buffers instantiations and functions calling
The users would have to fill-in the code with their specific functions

The initial approach had two targets:

- Provide bare-metal ADI drivers for ADI parts to users
- Leverage the driver code in a reference project running on hardware

`Advantages`

Driver code was MCU independent

`Disadvantages`

- Customer responsibility to port reference project on a different MCU
- .zip file distribution led to no version control and code duplication

`Evolution provided`

- Provide a way for reference projects to run on multiple hardware combinations
- Provide a build system that generates binaries and run them on hardware
- Expose parts as IIO devices to PC applications
- Improve code quality

**What is No-OS**

- A software framework for embedded bare-metal development
- Open-source
- ADI-BSD license
- Free
- Large collection of platform agnostic device drivers for ADI parts
- Significant collection of reference projects leveraging ADI evaluation boards
- Reference projects can run on a wide range of hardware
- Provides IIO enabled devices, making them accessible to PC applications that use libiio

**What is a No-OS device driver**

No-OS device driver provides a software interface to hardware devices.
Software application can access hardware functionality without knowing in detail how the driver operates: register map, bit fields, are directly handled by the driver, as well as communication interface specific sequences and timings

- A piece of code implemented in C, in a .c and .h pair, stored under /drivers on repo

- Its programming interface is directly called by the application code

.. figure:: api.png
   :align: center
   :width: 400

- Defines its own descriptor structures and init_param

.. figure:: struct.png
   :align: center
   :width: 400

- Contains minimum init() and remove() functions -  take as parameter the specific init_param structure

Puts the devide into the desired state
Allocates memory
Provides the descriptor for being called in other driver function calls, the remove functions frees the resources allocated by the init()

.. figure:: init.png
   :align: center
   :width: 400


- Performs no-OS API calls, does not perform platform specific function calls, it’s platform agnostic

.. figure:: api1.png
   :align: center
   :width: 400

- Software application can access hardware functionality without knowing in detail how the device operates


.. figure:: no-os-stack.png
   :align: center
   :width: 300

   No-OS Software Stack

**No-OS Platforms**

Platform drivers – represent an implementations of peripheral related no-OS API on a specific platform
Platform drivers use vendor HAL - Hardware Abstraction Layer
No-OS platform drivers are implementations of peripheral no-OS API on a particular platform.

No-OS modularity allow it to run a lot of its code on different platforms like:

- Xilinx (Zynq7000, ZynqMP, Microblaze)
- Maxim (32650, 32655, 32660, 32670, 78000), ADuCM (3029)
- STM32 (almost any)
- RaspberryPi Pico
- Mbed

.. figure:: platform.png
   :align: center
   :width: 600

   No-OS Platform Drivers

**No-OS Projects**

A project is basically an application that can be built, run and debugged on hardware

Specifications:

- Located under projects/
- It has a main() function
- It uses drivers/ and drivers/platforms directories
- It uses no-OS API
- It uses various libraries
- User interaction – serial, iio-oscilloscope
- makefiles

Project hardware typically is made of:

- An evaluation board
- A carrier board

No-OS projects are used for

- ADI parts evaluation
- Starting development based on a no-OS project

**IIO Concepts**

What is IIO – is a framework in the Linux kernel designed for devices such as adcs, dacs, etc..
There is a tree concept inside kernel, there is the context concept which is specific to a board and has a set of drivers
Context has a backend associated with it, it can be local or remote
Is has an attribute associated with it – give various descriptions of the board: name, version, etc.
Underneath the context comes the device, specific to the board and has also attributes, along with debug attributes – components you normally don’t interact with and require extra configuration or settings – ex. Advanced adc settings
Each device has two components - buffer and channel – buffer is associated with data
Channel represents the number of paths for signal to be acquired/generated

The Linux Industrial I/O (IIO)  subsystem is intended to provide  support for devices that, in some  sense, are analog-to-digital or digital-  to-analog converters
Devices that fall into this category are:
- ADCs
- DACs
- Accelerometers, gyros, IMUs
- Capacitance-to-Digital converters  (CDCs)
- Pressure, temperature, and light  sensors, etc.
- RF Transceivers (like the AD9361 /  AD9364 / AD9371 / ADRV9009)
- It can be used on ADCs ranging from a  1MSPS SoC ADC to >5 GSPS ADCs

.. _fig-iio:

.. figure:: iio.png
   :align: center
   :width: 500

`Libiio`

It’s written in C, but has bindings in Python, C++, etc.
All the high-level apps that talk to libiio are built on top of the stack, 
The stack preserves its functionality, because of the way things are built, no need to change it, for becoming compatible to use with for ex GNU, Matlab, etc.

.. _fig-libiio:

.. figure:: libiio.png
   :align: center
   :width: 500

Hands-on activity
~~~~~~~~~~~~~~~~~

.. TODO IN PROGRESS

By the end of this workshop, you will learn:

**Activities**

**Pre-requisites**

**Hands-on activity 1**

*Materials*

*Hardware setup*

Steps

**Hands-on activity 2**

*Theory of operation*

Steps:

*Results*

**Challenge**

**Hands-on activity 3**

*Materials*

*Theory of operation*

*Hardware setup*

Steps

**Challenge**

Slide Deck, booklet and additional materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since this tutorial is also designed to be presented as a live, hands-on
workshop, a slide deck is provided here:

.. admonition:: Download

   :download:`Emebdded Software Slide Deck <No-OS Workshop 2025.pdf>`

A complete booklet of the hands-on activity is also provided, as a companion to
following the tutorial yourself:

.. admonition:: Download

  :download:`Embedded Software Booklet <No-OS Booklet.pdf>`

Takeaways
~~~~~~~~~

Resources
~~~~~~~~~

No-OS Wiki:

* :external+no-OS:doc:`index`
* :dokuwiki:`no-OS API <resources/no-os/api>`
* :git-no-OS:`/`
* :adi:`en/analog-dialogue/articles/understanding-and-using-the-no-os-and-platform-drivers.html`

*Specific hardware resources*

:dokuwiki:`resources/eval/user-guides/eval-adxl355-pmdz/no-os-setup?s[]=no&s[]=os#adxl355_driver`

*Inspiration*

* https://www.pcbtrain.co.uk/
* https://res.cloudinary.com/
