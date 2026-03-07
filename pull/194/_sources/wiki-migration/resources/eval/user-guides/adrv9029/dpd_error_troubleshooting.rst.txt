ADRV9029 DPD ERROR TROUBLESHOOTING
==================================

ADI_ADRV9025_DPD_NO_PATHDELAY_ERROR
-----------------------------------

**ROOT CAUSE** : Error code to convey that the external path delay calibration was not run prior to enabling DPD tracking cal

**RECOMMENDED RECOVERY ACTIONS**

-  Sanity check to ensure that PA is turned on. Also, ensure that the PA current consumption in standby condition(Iq) matches the specification.
-  Ensure that the external Tx to ORx routing matches the Tx to ORx mapping setup during init
-  Ensure that there exists a valid signal path from Tx to ORx
-  Run the external path delay init cal with mask value 0x200000 and enable the DPD tracking cal post successful execution of the external path delay init cal.

| 

ADI_ADRV9025_DPD_ORX_SIGNAL_TOO_SMALL_ERROR
-------------------------------------------

**ROOT CAUSE** : Error code to convey that post PA data fed back into ORx has a very low signal to noise ratio for DPD tracking cal to perform correlations with Tx data and therefore adaptation will not be performed.

**RECOMMENDED RECOVERY ACTIONS**

-  Sanity check to ensure that PA is turned on. Also, ensure that the PA current consumption in standby condition(Iq) matches the specification.
-  Increase ORx gain to see if this error disappears.
-  Decrease Tx Front End attenuation/baseband digital backoff if the error persists despite ORx gain adjustment.
-  A combination of both(Tx atten and ORx gain adjustment) of the above

|

ADI_ADRV9025_DPD_ORX_SIGNAL_SATURATING_ERROR
--------------------------------------------

**ROOT CAUSE** : Error code to convey that the ORx signal received by DPD is saturating

**RECOMMENDED RECOVERY ACTIONS**

-  Increase Front End Tx attenuation
-  Decrease ORx Front End gain
-  Adjust Digital Backoff if required
-  A combination of both of the above

| 

ADI_ADRV9025_DPD_TX_SIGNAL_TOO_SMALL_ERROR
------------------------------------------

**ROOT CAUSE** : Error code to convey that the Tx signal is too small to perform DPD adaptation

**RECOMMENDED RECOVERY ACTIONS**

-  Increase digital baseband power.
-  Verify CFR settings if ADRV9029 CFR is turned on.
-  Review CLGC or DPD reported Tx power.

|

.. _adi_adrv9025_dpd_tx_signal_too_small_error-1:

ADI_ADRV9025_DPD_TX_SIGNAL_TOO_SMALL_ERROR
------------------------------------------

**ROOT CAUSE** : Error code to convey that the Tx signal is too small to perform DPD adaptation

**RECOMMENDED RECOVERY ACTIONS**

-  Increase digital baseband power.
-  Verify CFR settings if ADRV9029 CFR is turned on.
-  Review CLGC or DPD reported Tx power.

| 

ADI_ADRV9025_DPD_TX_SIGNAL_SATURATING_ERROR
-------------------------------------------

**ROOT CAUSE** : Error code to convey that the Tx signal exceeds the maximum ADC code and could be potentially clipped causing spectral distortion

**RECOMMENDED RECOVERY ACTIONS**

-  Decrease digital baseband power.
-  Verify CFR settings to ensure that a high PAR is not causing the DAC to overrange.
-  Review DPD reported Tx power via adi_adrv9010_DpdStatusGet( ) API.

|

ADI_ADRV9025_DPD_AM_AM_OUTLIERS_ERROR
-------------------------------------

**ROOT CAUSE** : Error code to convey that the DPD adaptation has encountered too many AM-AM outliers (i.e. Big difference in Tx and ORx samples). This could be caused due to memory effect of the PA or Tx attenuation and ORx gain settings. A misalignment in Tx and ORx samples due to a bad path delay estimation could also cause this error.

**RECOMMENDED RECOVERY ACTIONS**

-  Ensure that path delay value is correct. Disable DPD tracking and execute path delay init cal via InitCalsRun() to re-calibrate the delay and enable DPD tracking cal. If the error persists proceed to next step.
-  Ensure that the ORx ADC and Tx DAC are not saturating by decreasing the Tx Front End Gain via TxAttenSet() API, increasing ORx Front End attenuation via RxGainSet() API or both. If the error persists, proceed to next step. Fine tune Tx attenuation and ORx gain settings to see if the AM-AM errors persist
-  Ensure that ORx DC offset calibration is functioning correctly by reading back the ORx DC offset calibration status via TrackingCalStatusGet() API. If the ORx DC offset calibration is enabled and the error persists, proceed to next step.
-  Disable DPD tracking till the signal is steady
-  If there were other cals that were enabled at the same time as DPD, add some delay interval b/w enabling other cals(QEC/LO Leakage) and DPD
-  Investigate the AM-AM and AM-PM graphs of the PA at that power level.
-  Ensure that other cals like TxLOL, TxQEC are functioning correctly (sometimes image performance can cause AM-AM issues).
-  Turn off DPD and see if the AM-AM issues persist.

| 

ADI_ADRV9025_DPD_ACT_I_ASSIGNMENT_CONFLICT_ERROR
------------------------------------------------

**ROOT CAUSE** : The DPD model supplied to guide the internal DPD adaptation via DpdModelConfigSet() contains memory terms that cannot be accomodated due to hardware limitations

| **RECOMMENDED RECOVERY ACTIONS** Please refer to the DPD actuator LUT limitations in the ADRV9029 user guide while generating DPD models.

ADI_ADRV9025_DPD_ACT_K_ASSIGNMENT_EXCEED_LIMIT_ERROR
----------------------------------------------------

**ROOT CAUSE** : The degree of non-linearity for the DPD model supplied to guide the internal DPD adaptation via DpdModelConfigSet() cmd cannot be synthesized into the actuator Look Up Tables

| **RECOMMENDED RECOVERY ACTIONS** Please refer to the DPD actuator LUT limitations in the ADRV9029 user guide while generating prior DPD models to guide adaptation

ADI_ADRV9025_DPD_ACT_MULTIPLIER_ROW_ASSIGNMENT_CONFLICT_ERROR
-------------------------------------------------------------

**ROOT CAUSE** : The DPD model supplied to guide internal DPD adaptation via DpdModelConfigSet() violates the restrictions imposed by the DPD actuator hardware for memory(i) and cross terms(i)

| **RECOMMENDED RECOVERY ACTIONS** Please refer to the DPD actuator LUT limitations in the ADRV9029 user guide while generating prior DPD models to guide adaptation

ADI_ADRV9025_DPD_ACT_LUT_OUT_OF_RANGE_ERROR
-------------------------------------------

**ROOT CAUSE** : The DPD model supplied to guide internal DPD adaptation via DpdModelConfigSet() violates the restrictions imposed by the DPD actuator hardware for LUT usage

| **RECOMMENDED RECOVERY ACTIONS** Please refer to the DPD actuator LUT limitations in the ADRV9029 user guide while generating prior DPD models to guide adaptation

ADI_ADRV9010_DPD_ACT_NO_FREE_MULTIPLIER_ERROR
---------------------------------------------

**ROOT CAUSE** : The DPD model supplied to guide internal DPD adaptation via DpdModelConfigSet() violates the restrictions imposed by the DPD actuator hardware for roaming LUTs.


| **RECOMMENDED RECOVERY ACTIONS** Please refer to the DPD actuator LUT limitations in the ADRV9029 user guide while generating prior DPD models to guide adaptation

ADI_ADRV9025_DPD_ADP_WRITE_LUT_ERROR
------------------------------------

**ROOT CAUSE** : Error code to convey that the firmware could not update the DPD actuator look up tables. This could be due to other transactions in the system which have occupied the AHB bus and as a result the transaction cannot be performed.

**RECOMMENDED RECOVERY ACTIONS**

-  Disable DPD tracking cal via TrackingCalsEnableSet() command and reset DPD via DpdReset() command to put the actuator in unity gain mode
-  Might require a full firmware reset if error persists despite DPD reset

|

ADI_ADRV9025_DPD_HARDWARE_IN_USE_ERROR
--------------------------------------

**ROOT CAUSE** : Error code to convey that the DPD hardware is in use by another feature. Typical root cause of this error might be due to correlators being in use by another hardware. This error should not occur since the scheduler in the firmware takes care of scheduling various tracking cals competing for resources.

**RECOMMENDED RECOVERY ACTIONS**

-  Full DPD reset
-  Might require a full firmware reset if the error persists despite DPD reset.

| 

ADI_ADRV9025_DPD_DATA_CAPTURE_ERROR
-----------------------------------

**ROOT CAUSE** : Error code to convey that there was a DPD data capture failure. This might be caused due to TX/ORx signal paths not being enabled to capture data OR the capture engine paused due to other systemic issues

**RECOMMENDED RECOVERY ACTIONS**

-  Sanity check to ensure that PA is turned on. Also, ensure that the PA current consumption in standby condition(Iq) matches the specification.
-  Disable other cals and see if issue persists. (In case other cals are hogging the datapath/scheduler.)
-  Full reset DPD
-  Enable DPD tracking cal
-  Might require a full system reset if the error persists

|

ADI_ADRV9025_DPD_DATA_XACC_ERROR
--------------------------------

**ROOT CAUSE** : Error code to convey that the cross correlation caused an error due to a timeout in the hardware correlator. This is typically observed when there is not enough headroom in the signal to perform DPD adaptation.

**RECOMMENDED RECOVERY ACTIONS**

-  Sanity check to ensure that PA is turned on. Also, ensure that the PA current consumption in standby condition(Iq) matches the specification.
-  Disable other cals and see if issue persists. (In case other cals are hogging the datapath/scheduler.)
-  Full reset DPD
-  Enable DPD tracking cal
-  Might require a full system reset if the error persists

| 

ADI_ADRV9025_DPD_STABILITY_ERROR
--------------------------------

**ROOT CAUSE** : The DPD algorithm has encountered one or more of the following

-  The Direct EVM(ORx and Pre-DPD actuator data) and Indirect EVM(ORx and Post-DPD actuator data) has exceeded the limits. By default, a 5% limit on direct EVM and an 8% limit on indirect EVM is imposed. 
-  An underflow OR overflow of pre-DPD Tx RMS power/ post-DPD Tx RMS power/ORx RMS power has occured. The threshold is configurable via adi_adrv9010_DpdFaultConditionsSet( ) API
-  An underflow OR overflow of pre-DPD Tx Peak power/ post-DPD Tx Peak power/ORx Peak power has occured. The threshold is configurable via adi_adrv9010_DpdFaultConditionsSet( ) API

**RECOMMENDED RECOVERY ACTIONS**

-  For EVM errors, please ensure that there is no interference in the ORx path such that it could cause a large enough error b/w the Tx and ORx samples.
-  The DPD stability statistics can be retrieved via adi_adrv9010_DpdStatusGet() API for examination.
-  The stability fault conditions including EVM errors and power level thresholds for triggering a stability error is configurable via adi_adrv9010_DpdFaultConditionsSet() API. The thresholds can be relaxed to see if DPD recovers from the error condition.
-  Finally, the recovery actions on occurence of fault conditions is configurable via adi_adrv9010_DpdRecoveryActionSet() API. 

|

ADI_ADRV9025_DPD_TRACK_CLGC_SYNC_ERROR
--------------------------------------

**ROOT CAUSE** :A semaphore based synchronization mechanism was introduced b/w DPD and CLGC algorithms in SW 3.0 to ensure that there is no race condition between the two. With the synchronization mechanism, CLGC is always guarenteed to finish execution before DPD. The DPD-CLGC syncrhonization error indicates that DPD and CLGC semaphores were not exchanged successfully causing this error. 

**RECOMMENDED RECOVERY ACTIONS**

-  Allow for a few DPD update iterations before taking any actions to see if the algorithms synchronize themselves.
-  Disable CLGC and re-enable CLGC.
-  If error persists, disable both CLGC and DPD and re-enable them again.
-  If the error still persists, a full firmware reset is required.

| 

ADI_ADRV9025_DPD_ACT_LUT_ENTRY_SAT_ERROR
----------------------------------------

**ROOT CAUSE** :This error occurs when the degree of GMP polynomial (especially the power term 'k') plus the Tx sample magnitude is high causing an overlflow of the calculated LUT entry.

| **RECOMMENDED RECOVERY ACTIONS** The user can try modifying the DPD model programmed via DpdModelConfigSet() command to reduce the no. of Sum of Product terms in the GMP polynomial used to model the PA(DPD Model) assigned to a LUT.

.. _adi_adrv9025_dpd_act_lut_entry_sat_error-1:

ADI_ADRV9025_DPD_ACT_LUT_ENTRY_SAT_ERROR
----------------------------------------

**ROOT CAUSE** :This error occurs when the degree of GMP polynomial (especially the power term 'k') plus the Tx sample magnitude is high causing an overlflow of the calculated LUT entry.


| **RECOMMENDED RECOVERY ACTIONS** The user can try modifying the DPD model to reduce the no. of Sum of Product terms in the GMP polynomial used to model the PA(DPD Model).

ADI_ADRV9025_DPD_RPC_FAILED_ERROR
---------------------------------

ADI_ADRV9025_DPD_MESSAGE_WAIT_TIMEOUT_ERROR
-------------------------------------------

**ROOT CAUSE** :This error occurs when the Inter-processor communication between ARM-C to ARM-D fails. 

**RECOMMENDED RECOVERY ACTIONS**

-  Ensure that ARM-D has booted up correctly and is still alive. One way to check is to verify that the DPD iteration count retrieved via adi_adrv9025_DpdStatusGet( ) is incrementing.
-  If ARM-D has crashed, a full system reset might be necessary 

|

ADI_ADRV9025_DPD_MUTEX_CREATION_ERROR
-------------------------------------

**ROOT CAUSE** : This error occurs when DPD and CLGC are both enabled. The DPD and CLGC tracking cals are internally synchronized through a semaphore mechanism. 

**RECOMMENDED RECOVERY ACTIONS**

-  Disable CLGC tracking calibration via TrackingCalsEnableSet() cmd and re-enable CLGC tracking. If the error is not resolved move to next step
-  Disable CLGC tracking and DPD tracking via TrackingCalsEnableSet() cmd and enable DPD tracking cal only. If the DPD updates are happening correctly, enable CLGC tracking. If the error persists move to next step
-  Disable all tracking calibrations via TrackingCalsEnableSet() cmd and bringup one cmd at a time. If the error persists a full system reset might be required

| 

ADI_ADRV9025_DPD_DATA_CAPTURE_TIMEOUT_ERROR
-------------------------------------------

**ROOT CAUSE** : Error to convey that the DPD capture has timed out waiting for 1 second or more for a scheduled DPD capture to finish.  

**RECOMMENDED RECOVERY ACTIONS**

-  Review the test vector under to make sure there are no discrepancies
-  Ensure that there are no peaks in the last 4096 samples of the test vector before Tx EN goes low in TDD mode.

|

ADI_ADRV9025_DPD_LDL_SOLVER_ERROR
---------------------------------

ADI_ADRV9025_DPD_CHOL_SOLVER_ERROR
----------------------------------

**ROOT CAUSE** : Error to convey that the coefficient decomposition hardware is unable to resolve coefficients from auto-correlation / cross-correlation outputs during DPD adaptation

**RECOMMENDED RECOVERY ACTIONS**

-  Ensure that the path delay value is correct. Run path delay calibration again if required.
-  Reduce the degree of the polynomial in the DPD model by reducing the value of 'k'

| 

ADI_ADRV9025_DPD_UNITY_MODEL_UNAVAILABLE_ERROR
----------------------------------------------

**ROOT CAUSE** : LUT numbers 28,29 and 30 are reserved for programming the unity gain model on the ADRV902x DPD actuator. If a DPD model supplied by the user via **adi_adrv9025_DpdModelConfigSet()** API has DPD model entries assigned to LUT numbers 28,29 or 30, this error is flagged.

**RECOMMENDED RECOVERY ACTIONS**

-  Inspect the DPD model and re-assign any DPD model entries assigned to LUT numbers 28, 29 or 30.
-  The DPD Model entry LUT assignment can be found under the encircled column in a DPD model file as shown below.

|image1|

| 

ADI_ADRV9025_DPD_UNKNOWN_RPC_ERROR
----------------------------------

**ROOT CAUSE** : It is very unlikely that the transceiver gets into this state and ARM entered into an unknown error state.  

**RECOMMENDED RECOVERY ACTIONS**

-  Reset the Transceiver which means complete re-initialization of the system.

| 
| |TES GUI#resources:eval:user-guides:adrv9029|main page#none|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/madurdpdmodel.jpg
   :width: 400px
.. |TES GUI#resources:eval:user-guides:adrv9029|main page#none| image:: navigation ADRV9029 DPD USER GUIDE#evaluating_dpd_through_tes_gui
