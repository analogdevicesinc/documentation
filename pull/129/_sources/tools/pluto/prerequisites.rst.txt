.. _pluto prerequisites:

Prerequisites
=============

To understand what the prerequisites are for using the ADALM-PLUTO (PlutoSDR),
you need to understand what you are trying to do, and what software environment
you want to do it in. The PlutoSDR is a powerful/flexible device, which can be
used both in a standalone mode, or with a host, in multiple different software
environments. The one that is *best* is unique to the problem at hand, so we
don't specifically recommend a single solution. This page discusses both
hardware and software options, and lists the most common [1]_ configurations:

The PlutoSDR supports USB 2.0 On-The-Go (OTG), and can be used in two different
modes:

#. device, where the PlutoSDR communicates directly to a host, and streams data
   from/to the host.

   -  Host with at least one USB 2.0 Port, which can supply 500mA (no self
      powered hubs), which runs Linux, OS X, or Windows

      -  example: Personal Computer, Laptop, Tablet (running Linux), Raspberry
         Pi, Beagle Board, etc.
      -  The only thing necessary is the included USB cable. If you need
         something longer, it should work, but has not been tested.

#. host, where the PlutoSDR is the "brains" of the system, and communicates to
   other things via USB Wifi or USB Ethernet.

   -  You need a USB OTG Cable, compatible USB dongle, and a USB Power supply
      (must be purchased separately)

You will also need an appropriate antenna for the frequency that you are
interested in. Although there is an :ref:`antenna <pluto users antennas>` included with
the purchase of the ADALM-PLUTO, it may not be appropriate for the frequency
that you are interested in (anything under 350 MHz).

PlutoSDR as a Device
--------------------

You can stream data to any of these visualization tools, or SDR frameworks.

IIO Oscilloscope
~~~~~~~~~~~~~~~~

The :ref:`iio-oscilloscope` is a
simple visualization tool that can be used with the PlutoSDR to control the
device and stream data into/output the device.

It can be run on Linux and Windows (and soon MAC).

MATLAB / Simulink
~~~~~~~~~~~~~~~~~

#. You need to have a license for MATLAB® and/or Simulink®.

   - Depending on who you are, and where you are, you already may have access
     to a license.

      - If you are a student or faculty at a post-secondary institution
        (University, Community College, etc), check out MathWorks
        :mw:`Academic <academia.html>` section. Many schools provide a
        :mw:`Total Academic Headcount (TAH) </academia/tah-support-program/eligibility/?s_tid=srctitle>`
        license or some require/ask their students to obtain :mw:`Student version </academia/student_version.html>` [2]_
      - If you are a hobbyist, enthusiast or maker, check out :mw:`MATLAB Home </products/matlab-home.html>`.
      - There are many license options, if you are unsure, check out the
        MathWorks `store <store>`

   - You need to have a host computer, which supports the minimum :mw:`System Requirements for MATLAB </support/sysreq.html>`.
   - No matter which license you have [3]_, the following toolboxes are
     required to use MATLAB with the PlutoSDR:

      - :mw:`DSP System Toolbox <products/dsp-system.html>`
      - :mw:`Signal Processing Toolbox <products/signal.html>`
      - :mw:`Communications System Toolbox <products/communications.html>`

   - You also will need a :mw:`supported and compatible compiler </support/compilers.html>`, many which are zero cost, or
     free.
   - We have verified things on a subset of what MATHWORKS supports, including
     Windows 10, Windows 8.1, Windows 8, Windows 7 Service Pack 1, macOS Sierra
     10.12, macOS El Capitan 10.11, macOS Yosemite 10.10, Ubuntu 14.04 LTS and
     16.04 LTS, Debian 7.x, 8.x.

GNU Radio
~~~~~~~~~

#. GNU Radio is mostly a
   `Linux <https://wiki.gnuradio.org/index.php/InstallingGR>`__ only tool. It
   can be run on
   `Windows <https://wiki.gnuradio.org/index.php/InstallingGR#Windows>`__, but
   we have not tested in there.

   - We have verified things on Ubuntu 16.04 LTS, Debian 8.x and updated
     versions.

PlutoSDR as a host
------------------

To use PlutoSDR as a host, there are two different modes:

#. Simple, easy, works out of the box.
#. Complex, difficult, requires you to recompile the firmware running on the
   PlutoSDR.

Either mode requires a power supply plugged into the Power USB connector, which
can provide power for both the USB dongle you are plugging in, and the Pluto SDR
itself. We recommend at least 5V, 1A or above, depending on the firmware image.

#. AC adapters we have verified:

   - Farnell's `5.1V, 2.5A, Micro USB <http://www.newark.com/stontronics/t5875dv/psu-raspberry-pi-5v-2-5a-multi/dp/77Y6535>`__
     with international plugs
   - Adafruit's `5V, 1A USB port <https://www.adafruit.com/products/501>`__
     `NEMA 1-15 <https://www.worldstandards.eu/electricity/plugs-and-sockets/ab/>`__
     plug, requires USB cable
   - Adafruit's `5V, 2.4A Power Supply with MicroUSB Cable <https://www.adafruit.com/products/1995>`__,
     `NEMA 1-15 <https://www.worldstandards.eu/electricity/plugs-and-sockets/ab/>`__ plug

#. Batteries we have verified:

   - Adafruit's `USB Battery Pack, 2.2 Ah, 5V @ 1A <https://www.adafruit.com/products/1959>`__
   - Adafruit's `USB Battery Pack, 4 Ah, 5V @ 1A <https://www.adafruit.com/products/1565>`__
   - Adafruit's `USB Battery Pack, 10 Ah, 5V @ 2A <https://www.adafruit.com/products/1566>`__

Simple Host
~~~~~~~~~~~

The default firmware images supports a variety of USB devices including
:ref:`mass storage devices <pluto devs usb_otg>`,
some :ref:`Ethernet and WiFi devices <pluto-m2k usb_otg_host>`
(but not all, since each takes up space in the firmware).

You should be able to just plug things in with a OTG adapter or cable (which
supports OTG - many OTG cables don't properly connect the OTG ID signal, and the
PlutoSDR has no idea anything is plugged in), and have things work out of the
box to stream data over ethernet or Wifi.

If the PlutoSDR finds a mass storage with specific shell or python script, it
will begin to save data to the mass storage device (enabling you to do low cost
`wireless site surveys <https://en.wikipedia.org/wiki/Wireless_site_survey>`__),
which you can load into SDR frameworks later.

Complex hosts
~~~~~~~~~~~~~

Almost every device which you can plug into a Linux host, you will be able to
plug into a PlutoSDR with a kernel re-compile. check out the
:ref:`Developers <pluto devs>` information.

.. [1]
   not all possible configurations are listed

.. [2]
   If you have MATLAB Student edition, you will need the optional
   :mw:`Communications System Toolbox <products/communications.html>`

.. [3]
   to check your installed/licensed toolboxes, type the ``ver``
   :mw:`command <help/matlab/ref/ver.html>` at a MATLAB command prompt
