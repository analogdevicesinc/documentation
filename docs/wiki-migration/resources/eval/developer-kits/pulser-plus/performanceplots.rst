Performance Plots
=================

All measurements were performed with the ADPA1106 evaluation board plugged directly into the Pulser Plus board. To facilitate fast on/off switching when in Gate Pulsed Mode, all of the capacitance on the VGG1 and VGG2 pins was removed except for a 100 pF capacitor on each pin. This configuration was used for both Drain Pulsed Mode and Gate Pulsed Mode. The default capacitors on the VDD1 and VDD2 pins on the evaluation board (1000pF, 390 pF and 100pF with some series resistance) were left in place for operation in Drain Pulsed Mode and Gate Pulsed Mode.

| 

|image1| *Figure 1. Drain Pulsed Mode. VDD_PA (tan trace) response to Drain Pulse Enable (green trace). CW RF input. Horizontal axis is 100 ns/div. Crowbar circuit is enabled and engages at t=725 ns*

| 

|image2| *Figure 2. Drain Pulsed Mode. PA Output Power Envelope (blue trace, observed on ADL6012 RF Envelope Detector) response to Drain Pulse Enable (green trace). CW RF input. Horizontal axis is 100 ns/div. Crowbar circuit is enabled and engages at t=825 ns*

| 

|image3| //Figure 3. Drain Pulsed Mode. PA Output Power Envelope (observed on Spectrum Analyzer in Zero Span Mode) response to Drain Pulse Enable (not shown). CW RF input. Horizontal axis is 2 us/div. Crowbar circuit is enabled. //

| 

|image4| //Figure 4. Drain Pulsed Mode. PA Output Power Envelope (observed on Spectrum Analyzer in Zero Span Mode) response to Drain Pulse Enable (not shown). Pulsed RF input. Horizontal axis is 2 us/div. Crowbar circuit is enabled. //

| 

|image5| *Figure 5. Drain Pulsed Mode. Drain Pulse Enable (tan trace) and RF Input Enable (green trace) signals used in Figure 4. Pulsed RF input. Horizontal axis is 2 us/div. Crowbar circuit is enabled.*

| 

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/pulser-plus/gate_pulse_enable_and_gate_voltage_1us_pulse_cw_rf.png
   :align: center
   :width: 600px

*Figure 6. Gate Pulsed Mode. VGG1 (tan trace) response to Gate Pulse Enable (green trace). CW RF input. Horizontal axis is 200 ns/div.*

| 

|image6| *Figure 7. Gate Pulsed Mode. PA Output Power Envelope (blue trace, observed on ADL6012 RF Envelope Detector) and VGG1 (tan trace) response to Gate Pulse Enable (green trace). CW RF input. Horizontal axis is 200 ns/div.*

| 

|image7| //Figure 8. Gate Pulsed Mode: PA Output Power Envelope (observed on Spectrum Analyzer in Zero Span Mode) response to Gate Pulse Enable (not shown). CW RF input. Horizontal axis is 2 us/div. //

| 

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/pulser-plus/pout_vs_time_gate_pulsed_mode_8us_gated_rf_input.png
   :align: center
   :width: 600px

//Figure 9. Gate Pulsed Mode. PA Output Power Envelope (observed on Spectrum Analyzer in Zero Span Mode) response to Gate Pulse Enable (not shown). Pulsed RF input. Horizontal axis is 2 us/div. //

| 

|image8| //Figure 10. Gate Pulsed Mode. Gate Pulse Enable (tan) and RF Input Enable (green) signals used in Figure 9. Pulsed RF input. Horizontal axis is 2 us/div. //

| 

|image9| //Figure 11. Drain Pulsed Mode. IMONP (LTC7000 Current Monitor Output (green trace)) and ISNSP (LT1999 Current Monitor Output(tan trace)) response to Drain Pulse Enable (blue trace). CW RF RF input. Pulsed output power is equal to approximately 45 dBm. Horizontal axis is 2 us/div. //

| 

|image10| //Figure 12. Gate Pulsed Mode. IMONP (LTC7000 Current Monitor Output (green trace)) and ISNSP (LT1999 Current Monitor Output(tan trace)) response to Gate Pulse Enable (blue trace). CW RF RF input. Pulsed output power is equal to approximately 45 dBm. Horizontal axis is 2 us/div. //

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/pulser-plus/vdd_pa_and_drain_pulse_enable_-_drain_pulse_mode.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/pulser-plus/rf_env_on_adl6012_and_drain_pulse_enable_-_drain_pulse_mode.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/pulser-plus/pout_vs_time_drain_pulse_mode_continuous_rf_input.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/pulser-plus/pout_vs_time_drain_pulse_mode_1us_gated_rf_input.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/pulser-plus/drain_pulse_enable_and_rf_input_enable.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/pulser-plus/gate_pulse_enable_gate_voltage_and_adl6012_output_cw_rfin.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/pulser-plus/pout_vs_time_gate_pulsed_mode_10us_continuous_rf_input.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/pulser-plus/gate_pulse_enable_and_rf_input_enable_for_gated_rf_pulsing_gate_pulse_mode.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/pulser-plus/imonp_isnsp_drain_pulse_enable_mode_pout_45_dbm.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/pulser-plus/imonp_isnsp_gate_pulse_enable_mode_pout_45_dbm.png
   :width: 600px
