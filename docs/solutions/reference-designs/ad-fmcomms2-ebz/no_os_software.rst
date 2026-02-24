.. _ad-fmcomms2-ebz-noos:

No-OS Software
===============

The AD9361 No-OS software provides bare-metal hardware access without a Linux
operating system. The software together with the Generic Platform Driver can be
used as a base for any microprocessor platform.

Supported Devices
-----------------

- :adi:`AD9361`
- :adi:`AD9363`
- :adi:`AD9364`

Supported Platforms
-------------------

- :xilinx:`AC701 <products/boards-and-kits/ek-a7-ac701-g.html>`
- :xilinx:`KC705 <products/boards-and-kits/ek-k7-kc705-g.html>`
- :xilinx:`VC707 <products/boards-and-kits/ek-v7-vc707-g.html>`
- :xilinx:`ZC702 <products/boards-and-kits/ek-z7-zc702-g.html>`
- :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>`
- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__

Source Code
-----------

- :git-no-OS:`projects/ad9361`
- :git-no-OS:`drivers/rf-transceiver/ad9361`
- `Doxygen Documentation <https://analogdevicesinc.github.io/no-OS/>`__

Generic Platform
----------------

The Platform Driver implements the communication with the device and hides the
actual details of the communication protocol to the AD9361 driver. When the
desired type of processor is chosen, the specific communication functions have
to be implemented.

Code Size Information
~~~~~~~~~~~~~~~~~~~~~

The following information was obtained compiling the AD9361 project (with the
Generic Platform Driver integrated) using gcc v4.7.2 and the *Optimize for
size (-Os)* option enabled:

.. code-block::

   text     data     bss      dec      hex    filename
   45159    1624     24       46807    b6d7   ad9361_generic

No-OS API Reference
-------------------

The No-OS API provides all necessary functions to control the AD9361. Below is
a summary of the available functions grouped by category.

Device Global Settings
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Function
     - Description
   * - ``ad9361_init(init_param)``
     - Initializes the AD9361 device. Returns a structure containing the current
       state on success, or a negative error code.
   * - ``ad9361_set_en_state_machine_mode(phy, mode)``
     - Sets the Enable State Machine (ENSM) mode. Supported modes: SLEEP,
       ALERT, FDD, PINCTRL.
   * - ``ad9361_get_en_state_machine_mode(phy, *mode)``
     - Gets the current ENSM mode.
   * - ``ad9361_set_trx_path_clks(phy, *rx_path_clks, *tx_path_clks)``
     - Sets the RX and TX path clock rates.
   * - ``ad9361_get_trx_path_clks(phy, *rx_path_clks, *tx_path_clks)``
     - Gets the RX and TX path clock rates.
   * - ``ad9361_set_no_ch_mode(phy, no_ch_mode)``
     - Sets the number of channels mode (1 = 1x1, 2 = 2x2).
   * - ``ad9361_do_mcs(phy_master, phy_slave)``
     - Performs multi-chip synchronization between master and slave devices.
   * - ``ad9361_set_trx_fir_en_dis(phy, en_dis)``
     - Enables or disables the TRX FIR filters.
   * - ``ad9361_set_trx_rate_gov(phy, rate_gov)``
     - Sets the OSR rate governor (HIGHEST_OSR or NOMINAL_OSR).
   * - ``ad9361_get_trx_rate_gov(phy, *rate_gov)``
     - Gets the OSR rate governor.
   * - ``ad9361_do_calib(phy, cal, arg)``
     - Performs the selected calibration (TX_QUAD_CAL or RFDC_CAL).
   * - ``ad9361_trx_load_enable_fir(phy, rx_fir_cfg, tx_fir_cfg)``
     - Loads and enables TRX FIR filter configurations.
   * - ``ad9361_do_dcxo_tune_coarse(phy, coarse)``
     - Performs DCXO coarse tuning.
   * - ``ad9361_do_dcxo_tune_fine(phy, fine)``
     - Performs DCXO fine tuning.
   * - ``ad9361_get_temperature(phy, *temp)``
     - Gets the device temperature (degrees C x 1000).

Receive Chain Settings
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Function
     - Description
   * - ``ad9361_set_rx_rf_gain(phy, ch, gain_db)``
     - Sets the receive RF gain for the selected channel (0 or 1).
   * - ``ad9361_get_rx_rf_gain(phy, ch, *gain_db)``
     - Gets the current receive RF gain for the selected channel.
   * - ``ad9361_set_rx_rf_bandwidth(phy, bandwidth_hz)``
     - Sets the RX RF bandwidth in Hz.
   * - ``ad9361_get_rx_rf_bandwidth(phy, *bandwidth_hz)``
     - Gets the current RX RF bandwidth.
   * - ``ad9361_set_rx_sampling_freq(phy, sampling_freq_hz)``
     - Sets the RX sampling frequency in Hz.
   * - ``ad9361_get_rx_sampling_freq(phy, *sampling_freq_hz)``
     - Gets the current RX sampling frequency.
   * - ``ad9361_set_rx_lo_freq(phy, lo_freq_hz)``
     - Sets the RX LO frequency in Hz.
   * - ``ad9361_get_rx_lo_freq(phy, *lo_freq_hz)``
     - Gets the current RX LO frequency.
   * - ``ad9361_set_rx_lo_int_ext(phy, int_ext)``
     - Switches between internal (INT_LO) and external (EXT_LO) LO.
   * - ``ad9361_get_rx_rssi(phy, ch, *rssi)``
     - Gets the RSSI for the selected channel.
   * - ``ad9361_set_rx_gain_control_mode(phy, ch, gc_mode)``
     - Sets the gain control mode: GAIN_MGC, GAIN_FASTATTACK_AGC,
       GAIN_SLOWATTACK_AGC, or GAIN_HYBRID_AGC.
   * - ``ad9361_get_rx_gain_control_mode(phy, ch, *gc_mode)``
     - Gets the current gain control mode.
   * - ``ad9361_set_rx_fir_config(phy, fir_cfg)``
     - Sets the RX FIR filter configuration.
   * - ``ad9361_get_rx_fir_config(phy, rx_ch, *fir_cfg)``
     - Gets the RX FIR filter configuration.
   * - ``ad9361_set_rx_fir_en_dis(phy, en_dis)``
     - Enables or disables the RX FIR filter.
   * - ``ad9361_set_rx_rfdc_track_en_dis(phy, en_dis)``
     - Enables or disables RX RFDC Tracking.
   * - ``ad9361_set_rx_bbdc_track_en_dis(phy, en_dis)``
     - Enables or disables RX Baseband DC Tracking.
   * - ``ad9361_set_rx_quad_track_en_dis(phy, en_dis)``
     - Enables or disables RX Quadrature Tracking.
   * - ``ad9361_set_rx_rf_port_input(phy, mode)``
     - Sets the RX RF input port (A_BALANCED, B_BALANCED, C_BALANCED,
       A_N, A_P, B_N, B_P, C_N, C_P, TX_MON1, TX_MON2, TX_MON1_2).
   * - ``ad9361_rx_fastlock_store(phy, profile)``
     - Stores RX fastlock profile (0-7).
   * - ``ad9361_rx_fastlock_recall(phy, profile)``
     - Recalls specified RX fastlock profile.
   * - ``ad9361_rx_fastlock_load(phy, profile, *values)``
     - Loads a previously saved RX fastlock profile into a slot.
   * - ``ad9361_rx_fastlock_save(phy, profile, *values)``
     - Saves an RX fastlock profile for external storage.
   * - ``ad9361_rx_lo_powerdown(phy, option)``
     - Powers down the RX Local Oscillator (ON/OFF).

Transmit Chain Settings
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Function
     - Description
   * - ``ad9361_set_tx_attenuation(phy, ch, attenuation_mdb)``
     - Sets the TX attenuation for the selected channel in mdB.
   * - ``ad9361_get_tx_attenuation(phy, ch, *attenuation_mdb)``
     - Gets the current TX attenuation.
   * - ``ad9361_set_tx_rf_bandwidth(phy, bandwidth_hz)``
     - Sets the TX RF bandwidth in Hz.
   * - ``ad9361_get_tx_rf_bandwidth(phy, *bandwidth_hz)``
     - Gets the current TX RF bandwidth.
   * - ``ad9361_set_tx_sampling_freq(phy, sampling_freq_hz)``
     - Sets the TX sampling frequency in Hz.
   * - ``ad9361_get_tx_sampling_freq(phy, *sampling_freq_hz)``
     - Gets the current TX sampling frequency.
   * - ``ad9361_set_tx_lo_freq(phy, lo_freq_hz)``
     - Sets the TX LO frequency in Hz.
   * - ``ad9361_get_tx_lo_freq(phy, *lo_freq_hz)``
     - Gets the current TX LO frequency.
   * - ``ad9361_set_tx_lo_int_ext(phy, int_ext)``
     - Switches between internal (INT_LO) and external (EXT_LO) LO.
   * - ``ad9361_set_tx_fir_config(phy, fir_cfg)``
     - Sets the TX FIR filter configuration.
   * - ``ad9361_get_tx_fir_config(phy, tx_ch, *fir_cfg)``
     - Gets the TX FIR filter configuration.
   * - ``ad9361_set_tx_fir_en_dis(phy, en_dis)``
     - Enables or disables the TX FIR filter.
   * - ``ad9361_get_tx_rssi(phy, ch, *rssi_db_x_1000)``
     - Gets the TX RSSI for the selected channel.
   * - ``ad9361_set_tx_rf_port_output(phy, mode)``
     - Sets the TX RF output port (TXA or TXB).
   * - ``ad9361_get_tx_rf_port_output(phy, *mode)``
     - Gets the current TX RF output port.
   * - ``ad9361_set_tx_auto_cal_en_dis(phy, en_dis)``
     - Enables or disables TX auto calibration.
   * - ``ad9361_tx_fastlock_store(phy, profile)``
     - Stores TX fastlock profile (0-7).
   * - ``ad9361_tx_fastlock_recall(phy, profile)``
     - Recalls specified TX fastlock profile.
   * - ``ad9361_tx_fastlock_load(phy, profile, *values)``
     - Loads a previously saved TX fastlock profile into a slot.
   * - ``ad9361_tx_fastlock_save(phy, profile, *values)``
     - Saves a TX fastlock profile for external storage.
   * - ``ad9361_tx_lo_powerdown(phy, option)``
     - Powers down the TX Local Oscillator (ON/OFF).

Data Structures
~~~~~~~~~~~~~~~

**AD9361_RXFIRConfig** -- used by ``ad9361_set_rx_fir_config()``:

.. code-block:: c

   typedef struct {
       uint32_t rx;        // Channel: 1, 2, or 3 (both)
       int32_t  rx_gain;   // FIR gain: -12, -6, 0, or 6
       uint32_t rx_dec;    // Decimation factor: 1, 2, or 4
       int16_t  rx_coef[64];
   } AD9361_RXFIRConfig;

**AD9361_TXFIRConfig** -- used by ``ad9361_set_tx_fir_config()``:

.. code-block:: c

   typedef struct {
       uint32_t tx;        // Channel: 1, 2, or 3 (both)
       int32_t  tx_gain;   // FIR gain: -6 or 0
       uint32_t tx_int;    // Interpolation factor: 1, 2, or 4
       int16_t  tx_coef[64];
   } AD9361_TXFIRConfig;

**rf_rssi** -- used by ``ad9361_get_rx_rssi()``:

.. code-block:: c

   struct rf_rssi {
       u32 ant;        // Antenna number for which RSSI is reported
       u32 symbol;     // Runtime RSSI
       u32 preamble;   // Initial RSSI
       s32 multiplier; // Multiplier to convert reported RSSI
       u8  duration;   // Duration to be considered for measuring
   };

.. note::

   For complete details on the ``AD9361_InitParam`` initialization structure
   and all its members, refer to the
   `AD9361 Device Driver Customization <https://analogdevicesinc.github.io/no-OS/>`__
   documentation.

Serial Console Commands
-----------------------

The Console Commands Driver is optional for the project. It provides control of
the AD9361 through a serial terminal connected to the UART peripheral of the
development board. The baud rate is 115200 (8N1).

.. figure:: software/fmcomms2_uart.png
   :align: center

   UART console example: setting TX LO frequency to 2.4 GHz

.. list-table:: AD9361 Serial Commands
   :header-rows: 1
   :widths: 30 70

   * - Command
     - Description
   * - ``help?``
     - Displays all available commands
   * - ``register?``
     - Gets the specified register value
   * - ``tx_lo_freq?`` / ``tx_lo_freq=``
     - Gets/Sets the TX LO frequency [MHz]
   * - ``tx_samp_freq?`` / ``tx_samp_freq=``
     - Gets/Sets the TX sampling frequency [Hz]
   * - ``tx_rf_bandwidth?`` / ``tx_rf_bandwidth=``
     - Gets/Sets the TX RF bandwidth [Hz]
   * - ``tx1_attenuation?`` / ``tx1_attenuation=``
     - Gets/Sets the TX1 attenuation [mdB]
   * - ``tx2_attenuation?`` / ``tx2_attenuation=``
     - Gets/Sets the TX2 attenuation [mdB]
   * - ``tx_fir_en?`` / ``tx_fir_en=``
     - Gets/Sets the TX FIR state
   * - ``rx_lo_freq?`` / ``rx_lo_freq=``
     - Gets/Sets the RX LO frequency [MHz]
   * - ``rx_samp_freq?`` / ``rx_samp_freq=``
     - Gets/Sets the RX sampling frequency [Hz]
   * - ``rx_rf_bandwidth?`` / ``rx_rf_bandwidth=``
     - Gets/Sets the RX RF bandwidth [Hz]
   * - ``rx1_gc_mode?`` / ``rx1_gc_mode=``
     - Gets/Sets the RX1 gain control mode
   * - ``rx2_gc_mode?`` / ``rx2_gc_mode=``
     - Gets/Sets the RX2 gain control mode
   * - ``rx1_rf_gain?`` / ``rx1_rf_gain=``
     - Gets/Sets the RX1 RF gain
   * - ``rx2_rf_gain?`` / ``rx2_rf_gain=``
     - Gets/Sets the RX2 RF gain
   * - ``rx_fir_en?`` / ``rx_fir_en=``
     - Gets/Sets the RX FIR state
   * - ``dds_tx1_f1_freq?`` / ``dds_tx1_f1_freq=``
     - Gets/Sets the DDS TX1 F1 frequency [MHz]
   * - ``dds_tx1_f2_freq?`` / ``dds_tx1_f2_freq=``
     - Gets/Sets the DDS TX1 F2 frequency [MHz]
   * - ``dds_tx1_f1_phase?`` / ``dds_tx1_f1_phase=``
     - Gets/Sets the DDS TX1 F1 phase [degrees]
   * - ``dds_tx1_f2_phase?`` / ``dds_tx1_f2_phase=``
     - Gets/Sets the DDS TX1 F2 phase [degrees]
   * - ``dds_tx1_f1_scale?`` / ``dds_tx1_f1_scale=``
     - Gets/Sets the DDS TX1 F1 scale
   * - ``dds_tx1_f2_scale?`` / ``dds_tx1_f2_scale=``
     - Gets/Sets the DDS TX1 F2 scale
   * - ``dds_tx2_f1_freq?`` / ``dds_tx2_f1_freq=``
     - Gets/Sets the DDS TX2 F1 frequency [MHz]
   * - ``dds_tx2_f2_freq?`` / ``dds_tx2_f2_freq=``
     - Gets/Sets the DDS TX2 F2 frequency [MHz]
   * - ``dds_tx2_f1_phase?`` / ``dds_tx2_f1_phase=``
     - Gets/Sets the DDS TX2 F1 phase [degrees]
   * - ``dds_tx2_f2_phase?`` / ``dds_tx2_f2_phase=``
     - Gets/Sets the DDS TX2 F2 phase [degrees]
   * - ``dds_tx2_f1_scale?`` / ``dds_tx2_f1_scale=``
     - Gets/Sets the DDS TX2 F1 scale
   * - ``dds_tx2_f2_scale?`` / ``dds_tx2_f2_scale=``
     - Gets/Sets the DDS TX2 F2 scale
