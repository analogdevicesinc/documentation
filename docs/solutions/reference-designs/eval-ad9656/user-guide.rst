.. _ad9656_fmc user-guide:

User guide
===============================================================================

This user guide describes the :adi:`AD9656` evaluation board :adi:`EVAL-AD9656`,
which provides the support circuitry required to operate the ADC in its various
modes and configurations.

The :adi:`AD9656` data sheet provides additional information and should be
consulted when using the evaluation board.

Evaluation board hardware
-------------------------------------------------------------------------------

The evaluation board provides the support circuitry required to operate the
:adi:`AD9656` in its various modes and configurations. It is critical that the
signal sources used for the analog input and clock have very low phase noise
(ideally ~100 fs rms jitter) to realize the optimum performance of the signal
chain. Proper filtering of the analog input signal to remove harmonics and
lower the integrated or broadband noise at the input is necessary to achieve
the specified noise performance.

.. _ad9656_fmc user-guide hardware-configuration:

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set the jumper settings/link options on the evaluation board for the required
operating modes before powering on the board. The functions of the jumpers are
described in the table below. The default jumper settings are shown in
Figure 1.

.. list-table:: Jumper Settings
   :header-rows: 1
   :widths: 15 85

   * - Jumper
     - Description
   * - P101, P103
     - These jumpers determine the power source for the
       :adi:`AD9656EBZ <EVAL-AD9656>`.

       - Connect Pin 1 to Pin 2 on both P101 and P103 to power the ADC board
         through the FMC connector.
       - Connect Pin 2 to Pin 3 on both P101 and P103 to power the ADC board
         from the wall supply connected to P102.
       - Leave both P101 and P103 unjumpered if using headers P104 and P105.
   * - J304
     - This jumper enables the on-board crystal oscillator. Remove this jumper
       (and optionally C302) if an external off-board clock source is used.
   * - J206
     - This jumper selects between internal V\ :sub:`REF` and external
       V\ :sub:`REF`.

       - To choose the ADC's internal reference, connect Pin 3 (DUT_SENSE) to
         Pin 5 (GND) as shown in Figure 1. The default value of the internal
         reference is 1 V. SPI Register 0x18 Bits[7:6] can be used to program
         the internal reference voltage to values from 1 V to 1.4 V, in 0.1 V
         increments.
       - To use the on-board :adi:`AD822` buffered reference, connect Pin 2
         (DUT_SENSE) to Pin 1 (AVDD), and connect Pin 4 (DUT_VREF) to Pin 6
         (EXT_REF). Adjust external VREF to the desired value (from 1.0 V to
         1.4 V) using potentiometer R247.
       - To apply a reference voltage from an external off-board source, connect
         Pin 2 (DUT_SENSE) to Pin 1 (AVDD) and apply the reference voltage to
         Pin 4 (DUT_VREF). The AD9656 reference voltage is specified to be from
         1.0 V to 1.4 V.

.. figure:: images/ad9656_125ebz_default_jumpers.png
   :align: center
   :width: 600

   Default Jumper Connections for :adi:`EVAL-AD9656` Board

.. figure:: images/ad9656_jumper_location_wiki_figure_3_-_white_box.png
   :align: center

   Silkscreen error on 9656CE01C board — the correct numbering is shown in the green box.

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD9656` can be powered in one of three ways:

**FMC connector power (default)**

The default configuration powers the board through the FMC connector from the
carrier board. P101 and P103 both need to have Pin 1 tied to Pin 2. If P101 and
P103 have Pin 1 jumpered to Pin 2, do not connect the supplied 6V wall supply to
the AD9656 evaluation board. When changing the configuration of P101 and P103,
please remove both jumpers and then place them in their desired positions.

**Wall supply power**

Alternatively, the board can obtain its power from the wall-mountable 6V, 2A
switching power supply. For this mode, P101 and P103 both need to have Pin 2
tied to Pin 3. Connect the supply to a 100V ac to 240V ac, 47Hz to 63Hz wall
outlet. The output from the supply is provided through a 2.1mm inner diameter
jack that connects to the PCB at P102. The 6V supply is fused and conditioned
on the PCB before connecting to the low dropout linear regulators that supply
the proper bias to each of the various sections on the board.

**External bench power supplies**

The evaluation board can also be powered using external bench power supplies.
To do this, remove the E104, E105, E106, and E108 ferrite beads to disconnect
the on-board LDOs from the power planes. Note that in some board configurations
some of these might already be uninstalled. P104 and P105 headers can be
installed to facilitate connection of external bench supplies to the board.
E110, E111, E112 and E113 need to be populated to connect P104 and P105 to the
board power domains. A 1.8V, 0.5A supply is needed for 1.8V_DUT_AVDD,
1.8V_DRVDD and 1.8V_DVDD. Although the voltage requirements are the same for
these three, it is recommended that separate supplies be used for each of these.
A 3.3V, 0.5A supply is needed for 3.3V_DIG, which is used to power additional
on-board circuitry.

Analog inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The four channel inputs on the evaluation board are set up for a double
balun-coupled analog input with a 50Ω impedance. When connecting the ADC clock
and analog source, use clean signal generators with low phase noise, such as the
Rohde & Schwarz SMA, or an equivalent. Use a shielded, RG-58, 50Ω coaxial cable
(optimally 1 m or shorter) for connecting to the evaluation board. Enter the
desired frequency and amplitude (see the Specifications section in the data
sheet). When connecting the analog input source, use of a multipole, narrow-band
band-pass filter with 50Ω terminations is recommended. Analog Devices uses
band-pass filters from TTE and K&L Microwave, Inc. Connect the filters as close
to the evaluation board as possible.

Clock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default clock input circuit is derived from an on-board 125MHz crystal
oscillator feeding through a transformer-coupled circuit using a high bandwidth
1:1 impedance ratio transformer (T302) that adds negligible jitter to the clock
path. The external clock input (J302) is 50Ω terminated and ac-coupled to handle
single-ended sinusoidal inputs. The transformer converts the single-ended input
to a differential signal that is clipped by CR301 before entering the ADC clock
inputs. The :adi:`AD9656` ADC is equipped with an internal clock divider
(programmable divide ratios of 1 through 8) to facilitate usage with higher
frequency clocks. When using the internal divider and a higher input clock
frequency, remove CR301 to preserve the slew rate of the clock signal.

The :adi:`EVAL-AD9656` board is set up to be clocked through the
transformer-coupled input network from the 125MHz crystal oscillator, Y801. If
an external clock source is desired, remove C302 (optionally) and Jumper J304 to
disable the oscillator from running and connect the external clock source to the
SMA connector, J302 (labeled CLOCK+).

If an external clock source is used instead of the onboard crystal oscillator,
it should also be supplied with a clean signal generator as previously specified
for the analog input signals. Analog Devices evaluation boards typically can
accept ~2.8V p-p or 13 dBm sine wave input for the clock at the board SMA
clock connector.

Output signals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The JESD204B outputs from the ADC are routed to P2 using 100Ω differential
traces.

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`Schematics, layout files, bill of materials <media/en/technical-documentation/evaluation-documentation/AD9656_Evaluation_Board_Design_Integration_Files.zip>`

These diagrams demonstrate the routing and grounding techniques that should be
applied at the system level when designing application boards using these
converters.

Software guide
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9656` platform development environment supports no-OS
applications and IIO interfaces.

.. include-template:: ../common/using-iio-osc.rst.jinja

   has_no_os: true
   show_no_os_connection_image: true
   no_os_connection_image: images/no_os_ad9656_zcu102_iio.png
   iio_show_data_capture: true
   iio_show_time_domain: true
   iio_time_domain_image: images/no_os_ad9656_zcu102_iio_time_domain.png
   iio_show_frequency_domain: true
   iio_frequency_domain_image: images/no_os_ad9656_zcu102_iio_frequency.png
