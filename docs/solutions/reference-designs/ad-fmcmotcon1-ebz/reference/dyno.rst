.. _ad_fmcmotcon1_ebz dyno:

Dynamometer Drive System
===============================================================================

.. warning::

   The :adi:`AD-FMCMOTCON1-EBZ` is a **legacy product** and is no longer
   actively supported. This documentation is provided for reference only.

.. figure:: ../images/ad-dyno1-ebz.jpg
   :alt: AD-DYNO1-EBZ dynamometer drive system
   :align: center
   :width: 400

   AD-DYNO1-EBZ dynamometer drive system

Features
-------------------------------------------------------------------------------

-  Two BLDC motors connected in a dyno setup (BLY171S-24V-4000 and
   BLY171D-24V-4000)
-  Electronically adjustable load — the load value is set using the onboard
   buttons and LCD
-  Programmable step and ramp load changes
-  Measurement and display of load motor phase currents
-  Measurement and display of load motor speed
-  External control using Analog Discovery

Block Diagram
-------------------------------------------------------------------------------

.. figure:: ../images/dyno_diagram.jpg
   :alt: AD-DYNO1-EBZ block diagram
   :align: center
   :width: 800

   AD-DYNO1-EBZ block diagram

Key Parts
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Part
     - Description
   * - **Power**
     -
   * - :adi:`ADuM5000`
     - isoPower® integrated isolated dc-to-dc converter
   * - :adi:`ADP3335`
     - High accuracy ultralow quiescent current, 500 mA, AnyCAP® LDO
   * - **Isolation**
     -
   * - :adi:`ADUM3223`
     - 3 kV rms isolated precision half-bridge driver, 4 A output

User Guide
-------------------------------------------------------------------------------

The system is equipped with an LCD which displays information about the state
of the load. Together with the three push buttons placed below it, the LCD can
be used to display and configure different system parameters. The **+/−**
buttons navigate through the menu and change parameter values, while the
**Enter** button confirms changes or enters / exits menu screens.

.. figure:: ../images/dyno_menu.jpg
   :alt: Dyno LCD menu structure
   :align: center
   :width: 500

   Dyno LCD menu structure

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Menu screen
     - Description
   * - Main menu
     - Displayed at power up.
   * - Measurement menu
     - Displays RMS phase currents and motor speed. The load can be adjusted
       by pressing the "+" or "−" buttons. Press "Enter" to go back to the
       main menu.
   * - Waveforms menu
     - Select ramp or step load. Select "..." and press "Enter" to go back.
   * - Step load menu
     - Select "Step" to start toggling the load. Press "+" or "−" to toggle
       between preset step values. Press "Enter" to go back.
   * - Maximum duty cycle
     - Set maximum duty cycle. Press "Enter" to go back.
   * - Minimum duty cycle
     - Set minimum duty cycle. Press "Enter" to go back.
   * - Ramp load menu
     - Press "+" or "−" to change ramp period. Press "Enter" to go back.
   * - Settings menu
     - Select "..." and press "Enter" to go back.
   * - Duty cycle step
     - Change duty cycle step.
   * - About
     - System information.

Analog Discovery™
-------------------------------------------------------------------------------

To interface the Dyno with the Analog Discovery™ USB Oscilloscope:

-  Slide switch S2 to the EXT_CTRL position.
-  Insert the Analog Discovery™ into connector P1 with the Analog Devices
   logo facing the user.

.. figure:: ../images/dyno_discovery_control.jpg
   :alt: Analog Discovery connected to AD-DYNO1-EBZ
   :align: center
   :width: 400

   Analog Discovery connection to AD-DYNO1-EBZ

The signals available to the Analog Discovery™ are:

.. list-table::
   :header-rows: 1
   :widths: 15 35 50

   * - Dyno Signal
     - Analog Discovery Channel
     - Description
   * - I_A
     - Scope Channel 1 Positive
     - Phase A motor current (185 mV/A)
   * - I_B
     - Scope Channel 2 Positive
     - Phase B motor current (185 mV/A)
   * - PWM1
     - Digital Channel 0
     - Phase A PWM (3.3 V levels)
   * - PWM2
     - Digital Channel 2
     - Phase B PWM (3.3 V levels)
   * - PWM3
     - Digital Channel 2
     - Phase C PWM (3.3 V levels)

.. warning::

   The system requires a 5 V, 500 mA power supply. The power connector is a
   2.1 x 5.5 mm jack with the center pin positive (+).

.. _ad_fmcmotcon1_ebz dyno-test:

Test Procedure
-------------------------------------------------------------------------------

Required hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ZedBoard with mouse and keyboard
- SD card with ADI Linux image
- HDMI monitor
- AD-FMCMOTCON1-EBZ
- AD-DYNO1-EBZ

Running the test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Connect the hardware.
- In the Linux IIO Scope go to the **Motor Control** tab and select the
  following configuration:

  - **Delta**: ON
  - **Direction**: Clockwise
  - **Sensors**: hall
  - **Controller type**: Manual PWM
  - **PWM**: 90.96%

- Set **Run** to ON.

.. figure:: ../images/s1.jpg
   :alt: Motor Control tab configuration
   :align: center
   :width: 400

   Motor Control tab configuration

- Make sure that there are no vibrations in the DYNO system.
- On the DYNO board open the *Measurements* menu.
- Check the speed & current on the DYNO LCD: should read
  **5300 rpm ± 250 rpm** for speed and **0.3 A** for current (no load).

.. figure:: ../images/s2.jpg
   :alt: Dyno LCD — no load measurements
   :align: center
   :width: 200

   Dyno LCD — no load measurements

- Set the load to 100%.
- Check the speed & current: should read **3900 rpm ± 250 rpm** and
  **1.5 A ± 0.1 A**.

.. figure:: ../images/s3.jpg
   :alt: Dyno LCD — full load measurements
   :align: center
   :width: 200

   Dyno LCD — full load measurements
