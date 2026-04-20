.. _eval-ad35xxr evb quickstart sdp-h1-ace:

SDP-H1 quick start
===============================================================================

The evaluation board can also be controlled with the
:adi:`EVAL-SDP-H1` controller board and the :adi:`ACE` software, without any
FPGA or Linux system. This is the path for evaluating DC precision and
static DAC behavior directly from a PC.

.. figure:: ../images/EVAL-SDP-H1.jpeg
   :alt: EVAL-SDP-H1 controller board
   :align: center
   :width: 600

   EVAL-SDP-H1 controller board.

**Installing ACE**

- Download and run the latest :adi:`ACE` installer, which also installs
  the drivers for the SDP-H1.
- Open ACE, click **Plugin Manager** on the left-hand menu, go to
  **Available Packages**, select ``Board.AD35X2R``, and click
  **Install Selected**. The plugin moves to **Installed Packages**.

  .. figure:: ../images/ad3552r-plug-in_manager_with_red_squares.jpeg
     :alt: ACE Plugin Manager
     :width: 800

     ACE Plugin Manager.

- Click **Home** on the left-hand menu. If the board is connected it
  appears in **Attached Hardware**. If you don't have the board yet,
  you can still explore the plugin by double-clicking the desired board
  in the **Explore Without Hardware** list.

  .. figure:: ../images/ad3552r-start_tab_with_red_squares.jpeg
     :alt: ACE Start Tab showing Attached Hardware
     :width: 800

     ACE Start Tab showing Attached Hardware.

**Connecting the board (SDP-H1)**

#. Set all links to default positions (see link options table above).
#. Plug the EVAL-AD3552R onto the SDP-H1 controller board.
#. Connect the wall-plug power supply to the SDP-H1 DC jack. Power
   LEDs turn green.
#. With ACE running, connect the USB cable between the SDP-H1 and the
   PC. The board appears in **Attached Hardware** - double-click its
   icon to open the Board View.

**ACE plugin views**

ACE organizes control across several linked views:

.. figure:: ../images/ad3552r-ace_hierarchy.jpeg
   :alt: ACE plugin hierarchy diagram
   :width: 800

   ACE plugin hierarchy diagram.

- **Board View** - simplified diagram of the evaluation board. Use
  **Poll Device** to verify connectivity and **Reset Board** to power
  cycle the evaluation board. Double-click the AD3552R block to open
  the Chip View.

  .. figure:: ../images/ad3552r-board_view.jpeg
     :alt: ACE board view
     :width: 800

     ACE board view.

  .. figure:: ../images/ad3552r-board_view_buttons.jpeg
     :alt: ACE board view action buttons
     :width: 800

     ACE board view action buttons.

- **Chip View** - internal block diagram of the AD3552R with editable
  DAC output register fields. Buttons: **Apply Changes**, **Read All**,
  **Reset Chip**, **Diff**, **Software Defaults**,
  **Memory Map Side-By-Side**.

  .. figure:: ../images/chip_view_with_labels.jpeg
     :alt: ACE chip view
     :width: 800

     ACE chip view.

- **Memory Map View** - complete register map displayed as a list of
  registers or bit fields. Supports sorting, searching, individual or
  bulk read/write, CSV export and import.

  .. figure:: ../images/ad3552r-register_map_with_labels.jpeg
     :alt: ACE memory map view
     :width: 800

     ACE memory map view.

- **Waveform Generator View** - assign waveforms to channels and start
  or stop playback. Key controls: **DAC Mode** (Fast 16-bit or
  Precision 24-bit), **Enable Simultaneous Mode**, **Enable Channel
  1/2**, **Play**. The EVAL-AD3552R LED is blue during playback and
  green when stopped.

  .. figure:: ../images/ad3552r-waveform_generator_view.jpeg
     :alt: ACE waveform generator view
     :width: 800

     ACE waveform generator view.

  .. figure:: ../images/ad3552r-transmit_pane_dual_mode.jpeg
     :alt: Waveform generation in dual channel mode
     :width: 400

     Waveform generation in dual channel mode.

  .. figure:: ../images/ad3552r-transmit_pane_simultaneous_mode.jpeg
     :alt: Waveform generation in simultaneous mode
     :width: 400

     Waveform generation in simultaneous mode.

  Maximum update rates (AD3552R with SDP-H1):

  .. list-table::
     :header-rows: 1

     * -
       - Fast Mode (16-bit)
       - Precision Mode (24-bit)
     * - Dual channel
       - 12.5 MUPS
       - 8.33 MUPS
     * - Single channel / Simultaneous
       - 25 MUPS
       - 16.66 MUPS

- **Vector Generator View** - define or load waveforms (DC, single
  tone, square, triangle, sawtooth, chirp, noise, multi-tone, or from
  file). Parameters: **Vector Name**, **Desired Frequency**,
  **Attenuation** (dB), **Relative Phase**. Includes time-domain
  preview and FFT window.

  .. figure:: ../images/ad3552r-vector_generator_with_labels.jpeg
     :alt: ACE vector generator view
     :width: 800

     ACE vector generator view.

**Creating a dual waveform (step-by-step)**

#. From the start page, double-click the board icon to open the Board
   View.
#. Double-click the AD3552R block to open the Chip View.
#. Click **Proceed to Memory Map** and set the desired output range in
   ``CH0_CH1_OUTPUT_RANGE`` (e.g., ``0x33`` for ±10 V).
   Click **Apply All**.
#. Open the Vector Generator and create a 1 kHz sine wave and a 1 kHz
   sawtooth wave.
#. Go back to the Chip View, click **Proceed to Waveform Generator**,
   select **Fast Mode**, enable both channels, assign the waveforms,
   and click **Play**.

.. figure:: ../images/ad3552r-waveforms-on-oscilloscope.jpeg
   :alt: Simultaneous dual waveform output on oscilloscope
   :width: 800

   Simultaneous dual waveform output on oscilloscope.

.. collapsible:: Manual streaming mode configuration

   If **Auto Register Update** is unchecked, configure the following
   registers before pressing Play:

   .. list-table::
      :widths: 40 60
      :header-rows: 1

      * - Register
        - Setting
      * - ``STREAM_MODE`` (0x0E)
        - Set stream length (see table below)
      * - ``TRANSFER_REGISTER`` (0x0F)
        - Set ``STREAM_LENGTH_KEEP_VALUE`` to 1
      * - ``INTERFACE_CONFIG_D`` (0x14)
        - Set ``SPI_CONFIG_DDR`` to 1

   Stream length values by mode:

   .. list-table::
      :header-rows: 1

      * -
        - Fast Mode (16-bit)
        - Precision Mode (24-bit)
      * - Single channel / Simultaneous
        - 2
        - 3
      * - Dual channel
        - 4
        - 6

**Unsupported features in ACE plugin (v1.2021.38200)**

The following features are not yet supported; ACE notifies when an
update is available:

- DAC output range selection and customization
- CRC checking
- Amplitude and offset control in waveform generation (scaling only
  via Attenuation in dB; offset fixed to mid-scale)
- Using the LDAC line to update the DAC output
