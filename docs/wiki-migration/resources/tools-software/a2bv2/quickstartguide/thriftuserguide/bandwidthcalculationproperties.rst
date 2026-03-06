List of API in Bandwidth Calculation Properties
===============================================

-  UpdateBWCalcNwParams
-  GetBWParams
-  Bandwidth Calc Run and Reset

Update BW Calc Network Params
-----------------------------

This API is used for updating Bandwidth calculation setting parameters. It takes elementUid and band width power calculation parameters as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateBWCalcNwParams(string elementUid, AnalogDevices.SigmaStudio.Scripting.BwParams bwparam);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “bwparam” = Bandwidth calculation setting parameters

   -  CableDelayns – Cable Delay (ns/m)

      -  SampleRateHz – Sampling Rate 48KHZ or 44KHZ
      -  CableType – For setting cable type as UTP, XLR, RJ45, MIXED.
      -  ConservativeRespcyc – true for Conservative; false for Optimized.
      -  OptimizedRespCyc – True for Optimized; Flase for Conservative.
      -  bFormulaB – True for select FormulaB
      -  bFormulaA – True for select FormulaA
      -  bAutoCalcCheckbox – True for select AutoCalculatecheck box enable
      -  bManualRespCycleCalc – True for select Manual response cycle calculation.
      -  overAllCableLen – Overall cable length in m.

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateBwCalNwParams action.

-  IsSuccess is set to 'True' if the UpdateBwCalNwParams was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| BwParams Bwparam = new BwParams();

::

   Bwparam = client.GetBWParams("A2B_0");
   Bwparam.cableDelayns = 7.5f;
   Bwparam.SampleRateHz = 48000;
   Bwparam.ConservativeRespcyc = true;
   Bwparam.OptimizedRespCyc = false;
   Bwparam.bFormulaB = false;
   Bwparam.bFormulaA = true;
   Bwparam.bAutoCalcCheckbox = true;
   Bwparam.bManualRespCycleCalc = false;
   Bwparam.CableType = 0;
   Bwparam.overAllCableLen = 8.0f;
   ssp_result = client.UpdateBWCalcNwParams("A2B_0", Bwparam);

| **Python Example:**
| Bwparam = BwParams()

::

   Bwparam = client.GetBWParams("A2B_0")
   Bwparam.cableDelayns = float(7.5)
   Bwparam.SampleRateHz = 48000
   Bwparam.ConservativeRespcyc = True
   Bwparam.OptimizedRespCyc = False
   Bwparam.bFormulaB = False
   Bwparam.bFormulaA = True
   Bwparam.bAutoCalcCheckbox = True
   Bwparam.bManualRespCycleCalc = False
   Bwparam.CableType = 0
   Bwparam.overAllCableLen = float(8.0)
   ssp_result = client.UpdateBWCalcNwParams("A2B_0", Bwparam)

Get Bandwidth Params
--------------------

This API is used for getting Bandwidth calculation setting parameters. It takes elementUid as argument and returns Bandwidth parameters.

| **API:**
| AnalogDevices.SigmaStudio.Scripting.BwParams GetBWParams(string elementUid);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

| **Result:**
| This API returns bandwidth calculation parameters for the selected A2B channel. Bandwidth calculation parameters are listed below.

-  CableDelayns – Cable Delay (ns/m)
-  SampleRateHz – Sampling Rate 48KHZ or 44KHZ
-  CableType – For setting cable type as UTP, XLR, RJ45, MIXED.
-  ConservativeRespcyc – true for Conservative; false for Optimized.

| **Csharp Example:**
| BwParams bwParams = new BwParams();

::

   bwParams = client.GetBWParams("A2B_0");
   bwParams.CableDelayns = 7.5f;
   bwParams.SampleRateHz = 48000;
   bwParams.ConservativeRespcyc = true;
   _sspresult = client.UpdateBWCalcNwParams("A2B_0", bwParams);

| **Python Example:**
| Bwparam = BwParams()

::

   Bwparam = client.GetBWParams("A2B_0")
   Bwparam.cableDelayns = float(7.5)
   Bwparam.SampleRateHz = 48000
   Bwparam.ConservativeRespcyc = True
   ssp_result = client.UpdateBWCalcNwParams("A2B_0", Bwparam)

Bandwidth Calc Run and Reset
----------------------------

This API is used to Run Bandwidth calculation. It takes elementUid and property name and property value as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateBooleanProperty(string elementUid, string propertyName, bool propertyVal);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyName” = Name of the action property. Some of the property name examples are listed below

   -  BwCalcRun – Run the Bandwidth calculation

      -  BwCalcReset – Reset the Bandwidth Calculation

-  “propertyVal” = Setting value (true or false).

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateBoolProperty action.

-  IsSuccess is set to 'True' if the UpdateBoolProperty was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| \_sspresult = client.UpdateBooleanProperty("A2B_0", "BwCalcRun", true);

::

   _sspresult = client.UpdateBooleanProperty("A2B_0", "BwCalcReset", true);

| **Python Example:**
| ssp_result = client.UpdateBooleanProperty("A2B_0", "BwCalcRun", True)

::

   ssp_result = client.UpdateBooleanProperty("A2B_0", "BwCalcReset", True)
