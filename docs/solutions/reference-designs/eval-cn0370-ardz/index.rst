.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0370

.. _eval-cn0370-ardz:

EVAL-CN0370-PMDZ
=================

Low Noise LED Current Source Driver.

Overview
--------

:adi:`CN0370` is a complete single-supply, low noise LED current source driver
controlled by a 16-bit digital-to-analog converter (DAC). The system maintains
+/-1 LSB integral and differential nonlinearity and has 0.1 Hz to 10 Hz noise
of less than 45 nA peak-to-peak for a full-scale output current of 20 mA.

The :adi:`AD5542A` is a single-supply, 16-bit, serial-input, voltage-output
DAC that is used to control the voltage-to-current conversion. The
:adi:`ADA4500-2` is a single-supply, dual low-power amplifier with no
zero-crossover distortion offering high linearity over the full, rail-to-rail
common-mode input range. The :adi:`ADA4500-2` is used to buffer the reference
voltage of the DAC and is also used in a buffer configuration to convert the
voltage output of the DAC into current. The :adi:`ADR4525` is a high-precision,
low-power, low-noise voltage reference that provides a precise 2.5 V reference
voltage for the DAC.

The evaluation board has provisions to read the output voltage of the DAC and
an option to use an external supply voltage for the LED.

.. figure:: cn0370.jpg
   :align: center

   EVAL-CN0370-PMDZ evaluation board

Required Equipment
------------------

- PC with a USB port and Windows XP (32-bit), Windows Vista (32-bit), or
  Windows 7 (32-bit)
- :adi:`EVAL-SDP-CB1Z` SDP evaluation board
- SDP-PMD-IB1Z interposer board (SDP-to-PMOD)
- EVAL-CN0370-PMDZ circuit evaluation board
- CN0370 Evaluation Software
- 6 V wall wart power supply
- Agilent 34401A multimeter or equivalent
- GPIB-to-USB cable (required only for linearity tests)

Hardware Setup
--------------

.. figure:: cn0370-1.1.png
   :align: center

   CN0370 system block diagram

#. Connect the 120-pin connector **J4** on the SDP-PMD-IB1Z interposer board
   to the connector marked **CON A** on the :adi:`EVAL-SDP-CB1Z` (SDP)
   evaluation board. Place the shunt on **JP1** in the +5.0 V configuration.

   .. figure:: cn0370-2.jpg
      :align: center

      SDP-PMD-IB1Z interposer board connected to EVAL-SDP-CB1Z

#. Connect the EVAL-CN0370-PMDZ to the PMOD connector **J3** on the
   interposer board.

   .. figure:: cn0370-3.png
      :align: center

      EVAL-CN0370-PMDZ connected to PMOD connector J3

#. Connect a +6 V wall wart supply to connector **J1** of the interposer
   board.

   .. figure:: cn0370-4.png
      :align: center

      Power supply connected to connector J1

#. Use the USB cable to connect the :adi:`EVAL-SDP-CB1Z` to the PC.

Board Connections
~~~~~~~~~~~~~~~~~~

.. figure:: eval-cn0370-pmdz-1.jpg
   :align: center

   EVAL-CN0370-PMDZ board connection points

The EVAL-CN0370-PMDZ board has the following connection points:

- **LED_SUPPLY** -- The supply for the LED. It can be taken from the PMOD
  supply or an external voltage supply (VEXT). It is shorted by a shunt to
  PMOD by default.
- **VCC and AGND test points** -- Used to take voltage measurements.
- **VEXT** -- Used to supply an external voltage to the LED supply (input
  range: 0 to +20 V max).

Installing the Software
------------------------

#. Extract the file **CN0370_Evaluation_Software.zip** and open the file
   **setup.exe**.

   .. figure:: sw-1.png
      :align: center

      CN0370 Evaluation Software installer

#. Click **Next** to view the installation review page.

   .. figure:: sw-2.png
      :align: center

      Installation review page

#. Click **Next** to begin the installation.

   .. figure:: sw-3.png
      :align: center

      Installation in progress

#. Upon completion of the installation of the CN0370 Evaluation Software, the
   installer for the **ADI SDP Drivers** will execute.

   .. figure:: sw-4.png
      :align: center

      ADI SDP Drivers installer

#. Click **Next** to set the installation location for the SDP Drivers.

   .. figure:: sw-5.png
      :align: center

      SDP Drivers installation location

#. Press **Install** to install the SDP Drivers and complete the installation
   of all software. Click **Close** when done.

Using the Evaluation Software
------------------------------

Main Tab Controls
~~~~~~~~~~~~~~~~~~

.. figure:: sw-gui.png
   :align: center

   CN0370 Evaluation Software main tab

The evaluation software provides the following controls:

#. **Write Data** -- This button is used to write the data into the DAC.

#. **Input Mode** -- A selector where the user can choose the input mode:

   - **Input Current Mode** -- The amount of current desired for the LED is
     adjusted. Pushing the Write Data button writes the data to the board.
   - **Input Code Mode** -- The exact code is written in the Code box. The
     amount of current output is automatically adjusted by pushing the Write
     Data button.

#. **External Resistor** -- Enable this if the resistor on R_LIMIT has been
   changed.

#. **Iout** -- This control enables the user to change the amount of current
   flowing through the LED.

#. **R_LIMIT** -- The value of the resistor that limits the amount of current
   through the LED. It is set to a default value of 124 Ohm.

Writing Data -- Input Current Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. If the external resistor is replaced, enable the External Resistor button
   and write the new value for R_LIMIT.
#. Select **Input Current Mode**.
#. Adjust the amount of desired current by using the slider or the text box.
#. Push the **Write Data** button to write the code to the board.

Writing Data -- Input Code Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. If the external resistor is replaced, enable the External Resistor button
   and write the new value for R_LIMIT.
#. Select **Input Code Mode**.
#. Write the exact code to be written in the Code text box.
#. Push the **Write Data** button to write the code to the board.

Documents
---------

- :adi:`CN0370 Circuit Note <CN0370>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0370-PMDZ Design & Integration Files
   <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/CN0370-DesignSupport.zip>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Layout Files

Additional Information
----------------------

- :adi:`AD5542A Product Page <AD5542A>`
- :adi:`ADA4500-2 Product Page <ADA4500-2>`
- :adi:`ADR4525 Product Page <ADR4525>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
