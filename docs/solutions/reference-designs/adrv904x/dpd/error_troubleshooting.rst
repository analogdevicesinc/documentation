ADRV904x DPD ERROR TROUBLESHOOTING
==================================

**ADI_ADRV904X_DFE_APP_ERR_CODE_DPD_CHOL_SOLVER_ERROR(0xE001)** **Root Cause**: Invalid cross correlation encountered in DPD **Troubleshooting/Recovery Actions**:

-  Verify that there is no saturation at the Tx DAC output or ORx ADC input. Add power back off if needed.
-  Verify that CFR hard clipper is not engaged using the CfrStatisticsGet( ) API
-  Verify that DPD actuator input/output and ORx power levels seen by DPD is reasonable by reading the DPD statistics through the API DfeDpdCalSpecificStatusGet()
-  Verify that there is no DPD Actuator LUT saturation by reading the LUT saturation mask returned by DfeDpdCalSpecificStatusGet() API
-  Check for any discontinuities in the input signal. The DPD capture data can be obtained through the API DfeDpdCaptureDataFromBufMemGet(). Ensure that DPD tracking calibration is disabled before calling this API.
-  Review Low Phy or source signal to look for any discontiuities.

**ADI_ADRV904X_DFE_APP_ERR_CODE_DPD_MODEL_DESCRIPTOR_ERROR(0xE002)** **ADI_ADRV904X_DFE_APP_ERR_CODE_DPD_MODEL_DDR_DELAY_ERROR (0xE003)** **ADI_ADRV904X_DFE_APP_ERR_CODE_DPD_MODEL_POLY_TYPE_ERROR (0xE004)** **ADI_ADRV904X_DFE_APP_ERR_CODE_DPD_MODEL_DUPLICATE_LUT_ERROR (0xE005)** **Root Cause**: Invalid DPD Model Programmed via DpdModelConfigDpdSet( ) API **Troubleshooting**:

-  Ensure that the DPD Model text file released in the SW pkg is being parsed
   correctly including the linear term, idelay, jdelay etc. All DPD Models
   released in the SW pkg have been verified to program correctly.

**ADI_ADRV904X_DFE_APP_ERR_CODE_DPD_MAX_FRAC_EST_CNT_ERROR (0xE007)** **Root Cause**: DPD sub-sample alignment failure due to insufficient information **Troubleshooting**:

-  Ensure that a path delay seed has been programmed via DpdPathDelaySeed() API
   to guide the path delay tracking cal

**ADI_ADRV904X_DFE_APP_ERR_CODE_DPD_ACT_LUT_ENTRY_SAT_ERROR (0xE008)** **Root Cause**: DPD Actuator LUT entries have saturated. **Troubleshooting**:

-  Verify that there is no saturation at the Tx DAC output or ORx ADC input. Add power back off if needed.
-  Verify that CFR hard clipper is not engaged using the CfrStatisticsGet( ) API
-  Verify that DPD actuator input/output and ORx power levels seen by DPD is reasonable by reading the DPD statistics through the API DfeDpdCalSpecificStatusGet()
-  The PA non-linearity may be too high causing LUT entries to saturate. Adjust
   the PA bias and/or adjust the digital signal levels.

**ADI_ADRV904X_DFE_APP_ERR_CODE_DPD_INCOMPLETE_CAPTURE (0xE023)** **Root Cause**:Capture data contains zeros.

-  If you see this error code occasionally and it goes away, then it is simply indicating that DPD capture data is seeing zeros occasionally.
-  Inspect the signal to ensure that there are no discontinuities (zeros).
-  If operating in TDD mode, ensure that the TxEN signal is correctly aligned
   with the waveform and the TDD State Machine is triggered at the right time.

**ADI_ADRV904X_DFE_APP_ERR_CODE_DPD_FEATURE_COMPUTE_HOG (0xE006)** **ADI_ADRV904X_DFE_APP_ERR_CODE_DPD_STATUS_GET_INSUFFICIENT_MEMORY (0xE00B)** **ADI_ADRV904X_DFE_APP_ERR_CODE_INVALID_CONFIG_SIZE (0xE00C)** **ADI_ADRV904X_DFE_APP_ERR_CODE_INVALID_CONFIG_OFFSET (0xE00D)** **ADI_ADRV904X_DFE_APP_ERR_CODE_DPD_CTRL_GET_INSUFFICIENT_MEMORY (0xE00E)** **ADI_ADRV904X_DFE_APP_ERR_CODE_DPD_FUNC_NOT_SUPPORTED (0xE00F)** **ADI_ADRV904X_DFE_APP_ERR_CODE_DPD_CTRL_INVALID_PARAM (0xE010)** **ADI_ADRV904X_DFE_APP_ERR_CODE_CAL_FRAMEWORK_TASK_DOES_NOT_EXIST (0xE011)** **ADI_ADRV904X_DFE_APP_ERR_CODE_CAL_FRAMEWORK_STATUS_FUNC_NOT_SUPPORTED (0xE012)** **ADI_ADRV904X_DFE_APP_ERR_CODE_CAL_FRAMEWORK_INVALID_CONFIG_STATE (0xE013)** **ADI_ADRV904X_DFE_APP_ERR_CODE_CAL_FRAMEWORK_SET_CONFIG_FUNC_NOT_SUPPORTED (0xE014)** **ADI_ADRV904X_DFE_APP_ERR_CODE_CAL_FRAMEWORK_GET_CONFIG_FUNC_NOT_SUPPORTED (0xE015)** **ADI_ADRV904X_DFE_APP_ERR_CODE_CAL_FRAMEWORK_HAL_INVALID_CHANNEL (0xE016)** **ADI_ADRV904X_DFE_APP_ERR_CODE_CAL_FRAMEWORK_INVALID_CONFIG_OFFSET (0xE017)** **ADI_ADRV904X_DFE_APP_ERR_CODE_CAL_FRAMEWORK_TASK_CREATE_ERROR(0xE018)** **ADI_ADRV904X_DFE_APP_ERR_CODE_CAL_FRAMEWORK_EVENT_CREATE_ERROR(0xE019)** **ADI_ADRV904X_DFE_APP_ERR_CODE_CAL_FRAMEWORK_TIMER_CREATE_ERROR (0xE01A)** **ADI_ADRV904X_DFE_APP_ERR_CODE_CAL_FRAMEWORK_TRACKING_CAL_SUSPEND_TIMEOUT (0xE01B)** **ADI_ADRV904X_DFE_APP_ERR_CODE_DPD_EVENT_TIMEOUT_ERROR (0xE01C)** **ADI_ADRV904X_DFE_APP_ERR_CODE_DPD_PWR_METER_DPD_RATE_OVERFLOW (0xE01D)** **ADI_ADRV904X_DFE_APP_ERR_CODE_DPD_PWR_METER_CONFIG_FAIL (0xE01E)** **ADI_ADRV904X_DFE_APP_ERR_CODE_DPD_LUT_COPY_FAILED (0xE01F)** **ADI_ADRV904X_DFE_APP_ERR_CODE_CAPTURE_SEQ_MUTEX_REQ_FAILED (0xE020)** **ADI_ADRV904X_DFE_APP_ERR_CODE_CAPTURE_SEQ_PERIOD_REQ_INVALID (0xE021)** **ADI_ADRV904X_DFE_APP_ERR_CODE_CAPTURE_SEQ_CAPTURE_DONE_FAILED (0xE022)** **ADI_ADRV904X_DFE_APP_ERR_CODE_EVENT_RX_HANDLE_INIT_FAILED (0xE025)** **ADI_ADRV904X_DFE_APP_ERR_CODE_EVENT_THREAD_CREATION_FAILED (0xE026)** **ADI_ADRV904X_DFE_APP_ERR_CODE_DPD_CAPTURE_REQUEST_FAILED (0xE027)** **ADI_ADRV904X_DFE_APP_ERR_CODE_EVENT_HANDLE_GET_FAILED (0xE028)**

**Root Cause**: Insufficient resources for DPD computation **Troubleshooting**:

-  Grab a memory dump and contact ADI if you encounter this error.
-  These errors may require a full system reset
