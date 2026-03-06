Solar Battery Charger Application for CN0509
============================================

Overview
--------

Solar energy has become one of the top sources of renewable energy especially during natural disasters that may result in prolonged power shortages. Harnessing solar energy can be difficult and may require longer process to set up in times of disasters. The :doc:`EVAL-CN0509-EBZ </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0509>` is a DC-DC converter that accepts wide input voltage range from 5V to 100V that produces isolated voltages up to 5V and a current of up to 2A via USB Type A power delivery, perfect for mobile devices and low voltage USB devices. This guide focuses on setting up a portable dual USB port solar energy battery charger for mobile devices and portable power banks that can be used during power shortages.

Features/Highlights
-------------------

-  Wide DC input voltage range (5V-100V) USB Charger
-  Reverse polarity protection
-  Dual port charging capable with one Dedicated charging port (DCP)
-  Provides isolated and regulated 5V output
-  Provides up to 2A output current

Scope and Limitations
---------------------

This guide showcases a solar-powered USB charging demo using the :doc:`EVAL-CN0509-EBZ </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0509>` reference design. The system utilizes a solar panel as the primary power source to simulate renewable energy applications, delivering regulated 5V USB output suitable for low-power devices. The demo highlights key features such as wide input voltage support, reverse polarity indication, and fast charging capability on one USB port. Limitations including the absence of MPPT, sensitivity to input voltage fluctuations, and thermal behavior under load are addressed to provide a realistic overview of solar-powered USB charging performance in off-grid scenarios.

Limitations
~~~~~~~~~~~

-  This demo design is not intended for direct deployment or integration into final commercial products. It is solely intended as a demo application for educational and prototyping purposes.
-  The :doc:`EVAL-CN0509-EBZ </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0509>` does not include Maximum Power Point Tracking (MPPT), which limits its ability to optimize power extraction from the solar panel.
-  Input voltage must be maintained above 12V to ensure full charging current; performance may degrade under low sunlight or partial shading.
-  The design does not support automatic polarity correction. Incorrect polarity will trigger a warning LED, but manual intervention is required.
-  Voltage fluctuations from the solar panel may cause unstable operation or reduced output performance.
-  The D3 diode can reach temperatures up to 83.8°C under full load, especially in direct sunlight, which may affect long-term reliability.
-  Maximum output power is limited to 10W (5V at 2A), which may not be sufficient for high-power or multiple USB devices.
-  Only one USB port supports fast charging via a Dedicated Charging Port (DCP) controller; the second port is limited to standard charging.
-  Charging efficiency is sensitive to USB cable quality. Long or thin-gauge cables may result in significant voltage drops.

Reference Design and Solution
-----------------------------

CN0509 Wide Input Voltage Range, Dual USB Port Charger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :doc:`EVAL-CN0509-EBZ </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0509>` is a reference design that provides an isolated USB charging solution with a wide input voltage range, developed by Analog Devices. It is designed to convert high-voltage DC sources such as solar panels, industrial power supplies, or automotive systems into stable 5V USB output. The board includes two USB Type-A ports, with one port supporting fast charging through a dedicated charging port controller. Key features include input polarity indication, thermal monitoring, and LED status indicators. This reference design offers a compact and efficient platform for evaluating USB charging performance in renewable energy, industrial, and off-grid environments.

Material Requirements
---------------------

.. image:: https://wiki.analog.com/_media/ajaxperflookupdelay/screenshot_2025-10-15_131411.png
   :align: center
   :width: 400px

Setup Guide
-----------

Basic Setup
~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0509/nsetup.png
   :align: center
   :width: 400px

Setup Assembly
~~~~~~~~~~~~~~

-  Connect the solar panel to the CN0509 using the correct polarity of the device.


|image1|

.. note::

   You may add an on/off switch connected to the solar panel output to isolate the voltage before turning on CN0509


.. warning::

   Use of solar panels with high output ratings requires strict adherence to safety protocols. Ensure proper installation, utilize appropriate protective equipment, and follow all manufacturer guidelines. High-voltage systems present serious hazards if not handled correctly. Consultation with a certified professional is strongly recommended.


-  Connect the USB-Cable to the CN0509 and connect the other end to a rechargeable device, in this demo Type-C USB device is used.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0509/step2.jpg
   :align: center
   :width: 300px

Actual Setup
~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0509/picture5.png
   :align: center
   :width: 300px

Demo and Results
----------------

Readings
~~~~~~~~

-  Initial Input Voltage from the Solar Panel

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0509/picture7.png
   :align: center
   :width: 300px

-  Output Voltage from CN0509

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0509/picture6.png
   :align: center
   :width: 300px

.. note::

   While the solar panel used in this setup is rated at 12V, 10W, the actual input voltage and power delivered to the :doc:`EVAL-CN0509-EBZ </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0509>` will vary significantly depending on environmental conditions such as sunlight intensity, angle of incidence, cloud cover, and temperature. These factors can lead to reduced input voltage and current, which may affect charging performance and stability. Users should be aware that optimal performance is typically achieved under full, direct sunlight, and results may vary in shaded or low-light conditions.


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0509/step1-1.png
   :width: 300px
