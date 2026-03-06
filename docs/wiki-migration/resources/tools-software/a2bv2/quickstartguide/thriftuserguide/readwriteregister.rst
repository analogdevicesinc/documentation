:doc:`Click here to return to Thrift User Guide Homepage </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide>`

List of API for Register Access for A2B
=======================================

-  :doc:`Register Read </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/readwriteregister>`
-  :doc:`Set Register Value </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/readwriteregister>`

| 
| ====Register Read==== This API used for reading transceiver register value. It takes elementUid and register address list as argument and returns List of Register addresses.

| **API:**
| List<AnalogDevices.SigmaStudio.Scripting.RegAddrValPair> ReadRegValue(string elementUid, List<int> regaddrlist);

| **Arguments:**
| \* “elementUid” = Name of the action property

-  “regaddrlist” = Register Address List object for collecting register info from the the API

| **Result:**
| This API returns List of register addresses for the selected node.

| **Csharp Example:**
| // Reading same address register value for main node

::

   List<int> regAddrList = new List<int>() { 0x0, 0x1 };
   List<RegAddrValPair> regAddrValPairs = new List<RegAddrValPair>();
   regAddrValPairs = client.ReadRegValue("AD243xMain_0", regAddrList);

| **Python Example:**
| #Reading same address register value for main node

::

   RegAddrlist= [0x1,0x2]
   RegAddrVal1 = []
   RegAddrVal1 = client.ReadRegValue("AD243xMain_0",RegAddrlist)

| 
| ====Set Register Value==== This API used for updating register value for main node and sub nodes. We can update Control register, I2S/PDM register, Interrupt and error register, IO register value, Control register, GPIOD register values for main node and sub nodes. It takes elementUid and register info as argument and returns SSPResult.

| **API:**
| SSPResult SetRegValue(string elementUid, AnalogDevices.SigmaStudio.Scripting.RegAddrValPair regvalpair);

| **Arguments:**
| \* “elementUid” = Name of the action property

-  “regvalpair” = Register value pair contains below parameters

   -  Register Address

      -  Register Value

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of SetRegValue action.

-  IsSuccess is set to 'True' if the SetRegValue was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| // Setting register values of register address 0x0C, 0x41 for main node

::

   RegAddrValPair regAddrVal = new RegAddrValPair();
   regAddrVal.RegAddr = 0x0C;
   regAddrVal.RegVal = 0x05;
   _sspresult = client.SetRegValue("AD243xMain_0", regAddrVal);

| **Python Example:**

::

   #Setting register value of address 0xE and 0x0F for main node          
   RegAddrVal1.RegAddr = 0x0E
   RegAddrVal1.RegVal = 0x05
   ssp_result = client.SetRegValue("AD243xMain_0", RegAddrVal1)

.. tip::

   For additional details on Transceiver Register configuration, you may refer the :doc:`A2B Plugin for SigmaStudio+ User Guide </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/schematics-components>`.

