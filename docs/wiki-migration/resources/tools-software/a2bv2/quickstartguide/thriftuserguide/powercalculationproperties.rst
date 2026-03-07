:doc:`Click here to return to Thrift User Guide Homepage </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide>`

List of API in Power Calculation Properties
===========================================

-  :doc:`GetPwrParams </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/powercalculationproperties>`
-  :doc:`ComputePwr </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/powercalculationproperties>`
-  :doc:`UpdatePwrCalcNwParams </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/powercalculationproperties>`
-  :doc:`Power calculation Run and Reset </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/powercalculationproperties>`

| 
| ====Get power parameters==== This API is used for Retrieve the power parameters. It takes elementUid as argument and returns PowerParamForCalc which is having PowerCalcParams and BStandbyMode.

| **API:**
| AnalogDevices.SigmaStudio.Scripting.PowerParamForCalc GetPwrParams(string elementUid);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

| **Result:**
| This API Returns PowerParamForCalc object which contains list of PowerCalcParams and BStandbyMode.

-  In Success case, it will give List of PowerCalcParams.
-  PowerCalcParams will give result as null in case of failure.
-  PowerCalcParams contains below parameters info

-  Node dependent parameters:

   -  NodeName
   -  Selfpwr
   -  NodeId

-  Resistance related parameters:

   -  InductorDcR
   -  PosBiasPmosSwitchOnR
   -  NegBiasPmosSwitchOnR
   -  ConnectionR
   -  CableR
   -  FCableLength
   -  LoclPwrdApAnR

-  Voltage related parameters:

   -  VDoide1
   -  VDoide3
   -  VReg

-  Non displayed constants:

   -  Vout1
   -  Vout2

-  Current related parameters:

   -  Iiovdd_vout1
   -  Iiovdd_vout2
   -  Ivext1
   -  Ivext2
   -  IvRegPeri

-  Constant Current:

   -  Ivssn
   -  Ipllvdd_Idvdd
   -  Ivnq
   -  ItxVdd
   -  IrxVdd
   -  ItrxIdle

-  Other parameters:

   -  NupDigitalLogic
   -  NupSchottKey
   -  FInRush
   -  ShortCircuitProtectR
   -  TotPhantomR

| **CSharp Example:**

::

   PowerParamForCalc paramForCalc = new PowerParamForCalc();
   paramForCalc = client.GetPwrParams("A2B_0");

| **Python Example:**
| power = PowerCalcParams()

::

   power = client.GetPwrParams("A2B_0")

| 
| ====Compute power parameters==== This API is used for computing the power parameters. It takes elementUid as argument and returns Power Calculation information for the selected A2B channel.

| **API:**
| AnalogDevices.SigmaStudio.Scripting.PwrCalc ComputePwr(string elementUid);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

| **Result:**
| This API Returns Power Calculation object which contains list of PowerCalcOutputs and powercalSummary.

| **Csharp example:**
| PwrCalc pwrCalc = client.ComputePwr("A2B_0");

| **Python example:**
| PwrCalc pwrCalc = client.ComputePwr("A2B_0")

Update Power Calc Network Params
--------------------------------

This API is used for updating Power calculation parameters. It takes elementUid and power calculation parameters as arguments and returns SSPResult.

| **API:**
| SSPResult UpdatePwrCalcNwParams(string elementUid, AnalogDevices.SigmaStudio.Scripting.PowerParamForCalc pwrCalc);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “pwrCalc” = Power Calculation Parameters

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdatePwrCalcNwParams action.

-  IsSuccess is set to 'True' if the UpdatePwrCalcNwParams was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| PowerParamForCalc paramForCalc = new PowerParamForCalc();

::

   paramForCalc = client.GetPwrParams("A2B_0");
   // Updating Peri Supply 1 property for main node
   paramForCalc.PowerCalcSettings[0].Ivext1 = 13.99f; 
   // Updating Peri Supply 2 property for main node
   paramForCalc.PowerCalcSettings[0].Ivext2 = 8.01f; 
   //Updating Peri Supply 1 property for sub node 0
   paramForCalc.PowerCalcSettings[1].Ivext1 = 14.99f; 
   _sspresult =  client.UpdatePwrCalcNwParams("A2B_0", paramForCalc); // Update power params

| **Python Example:**
| pwrcalc = PowerParamForCalc()

::

   pwrcalc = client.GetPwrParams("A2B_0")
   #Updating Peri Supply 1 property for main node
   pwrcalc.PowerCalcSettings[0].Ivext1 = float(12.99)
   #Updating Peri Supply 2 property for main node
   pwrcalc.PowerCalcSettings[0].Ivext2 = float(7.01)
   #Updating Peri Supply 1 property for sub node 0
   pwrcalc.PowerCalcSettings[1].Ivext1 = float(14.99)
   ssp_result = client.UpdatePwrCalcNwParams("A2B_0", pwrcalc)

| 
| ====Power Calc Run and Reset==== This API is used to Run Power calculation. It takes elementUid and property name and property value as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateBooleanProperty(string elementUid, string propertyName, bool propertyVal);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyName” = Name of the action property. Some of the property name examples are listed below

   -  PwrCalcRun – Run the Power calculation

      -  PwrCalcReset – Reset the Power Calculation

-  “propertyVal” = Setting value (true or false).

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateBoolProperty action.

-  IsSuccess is set to 'True' if the UpdateBoolProperty was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| \_sspresult = client.UpdateBooleanProperty("A2B_0", "PwrCalcRun", true);

::

   _sspresult = client.UpdateBooleanProperty("A2B_0", "PwrCalcReset", true);

| **Python Example:**
| ssp_result = client.UpdateBooleanProperty("A2B_0", "PwrCalcRun", True)

::

   ssp_result = client.UpdateBooleanProperty("A2B_0", "PwrCalcReset", True)

.. note::

   Close and reopen the respective window for viewing the updated settings.


.. tip::

   For more information about Power calculation properties, you can refer to the :doc:`A2B Plugin for SigmaStudio+ User Guide </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkanalysisanddebug>`.

