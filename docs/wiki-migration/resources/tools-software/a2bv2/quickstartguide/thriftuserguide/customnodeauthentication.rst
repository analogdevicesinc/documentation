:doc:`Click here to return to Thrift User Guide Homepage </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide>`

Custom Node Authentication
==========================

This API is used for the enabling or disabling the Custom Node Authentication along with settings for Sub nodes in A2B network. It takes element Uid and customAuthentication info as arguments and returns SSPResult.

| **API:**
| SSPResult EnableCustomAuth(string elementUid, AnalogDevices.SigmaStudio.Scripting.ADI_A2B_CUSTOM_ID customAuth);

| **Arguments:**
| \* “elementUid” = UID of the A2B Sub Node

-  “customAuth” = Custom Authentication configuration contains below parameters as shown below

   -  BEnableNodeId – For enabling/disabling Custom Node Identifier of specified Sub node

      -  BReadFromMem – For enabling/disabling reading from I2C device
      -  BReadFromGpio – For enabling/disabling reading from GPIO Pins
      -  BReadFromMailbox - For enabling/disabling reading from Mailbox
      -  AGpioVal – For enabling GPIO pins when reading from GPIO pins
      -  NMemAddr – Memory address when reading from I2C device
      -  NMemDevAddrWidth – Device memory address width when reading from I2C device
      -  NMemDevAddr – Device address when reading from I2C device
      -  NodeId – Node Ids
      -  NRetryCnt – No.of retry count
      -  NMaxTimeOut – Maximum timeout when reading from Mailbox

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of EnableCustomAuth action.

-  IsSuccess is set to 'True' if the EnableCustomAuth was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **CSharp Example:**
| ADI_A2B_CUSTOM_ID oCustomAuth = new ADI_A2B_CUSTOM_ID();

::

   oCustomAuth.BEnableNodeId = true; 
   oCustomAuth.BReadFromGpio = true;
   oCustomAuth.BReadFromMailbox = true;
   oCustomAuth.AGpioVal = new byte[8] { 1, 1, 1, 1, 1, 1, 1, 1 };
   oCustomAuth.NMemAddr = 0x50;
   oCustomAuth.BReadFromMem = true;
   oCustomAuth.NMemDevAddrWidth = 2;
   oCustomAuth.NMemDevAddr = 0x50;
   oCustomAuth.NodeId = new byte[5] { 49, 50, 51, 52, 53 };
   oCustomAuth.NRetryCnt = 100;
   oCustomAuth.NMaxTimeOut = 100;
   _result = client.EnableCustomAuth("AD243xSubNode_1", oCustomAuth);

| **Python Example:**
| CustomNodeAuth = ADI_A2B_CUSTOM_ID()

::

   CustomNodeAuth.bEnableNodeId = True
   CustomNodeAuth.bReadFromMem = True
   CustomNodeAuth.NodeId = bytearray([49, 50, 51, 52, 53])
   CustomNodeAuth.nMemDevAddr = 0x50
   CustomNodeAuth.nMemDevAddrWidth = 2
   CustomNodeAuth.nMemAddr = 0x50
   CustomNodeAuth.bReadFromGpio = True
   CustomNodeAuth.aGpioVal = bytearray([1, 1, 1, 1, 1, 1, 1, 1])
   CustomNodeAuth.bReadFromMailbox = True
   CustomNodeAuth.nMaxTimeOut = 100
   CustomNodeAuth.nRetryCnt = 100
   ssp_result = client.EnableCustomAuth("AD243xSubNode_0",CustomNodeAuth)

.. tip::

   For more information about Custom node ID configuration, you can refer to the :doc:`A2B Plugin for SigmaStudio+ User Guide </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/drawinga2bschematics>`.

