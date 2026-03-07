:doc:`Click here to return to Thrift User Guide Homepage </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide>`

List of API in Network Properties
=================================

-  :doc:`GetNwPolicy </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/networkproperties>`
-  :doc:`UpdateNetworkPolicy </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/networkproperties>`
-  :doc:`GetLevelStackDbgSettings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/networkproperties>`
-  :doc:`GetDomainStackDbgSettings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/networkproperties>`
-  :doc:`UpdateLevelStackDbgSettings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/networkproperties>`
-  :doc:`UpdateDomainStackDbgSettings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/networkproperties>`

| 
| ====Get Network Policy==== This API used for Getting A2B network policy for the specified A2B channel. It takes elementUid as argument and returns A2B Network policy information.

| **API:**
| AnalogDevices.SigmaStudio.Scripting.A2bNwPolicy GetNwPolicy(string elementUid);

**Arguments:**

-  “elementUid” = UID of the A2B Channel
   A2B Network policy contains below parameters for users to update Network policy from thrift. Rest of the parameters are read only parameters and not to be changed.
-  DsvryMode
-  NDiscoveryStartDelay
-  BOverrideSelfDisc
-  RediscoveryWaitTimeInMilliSecondsResult
-  OLineFaultDbSettings. bEnablePostDiscFaultDiag
-  OLineFaultDbSettings.bAutoDiscoveryOnPDFault
-  OLineFaultDbSettings.CanPerformPartialDiscovery
-  OLineFaultDbSettings.nNumAttemptsCritical
-  OLineFaultDbSettings.RediscoveryInterval

This API returns List of all Network property details for the selected A2B Channel.

| **Result:**
| This API returns List of Network properties details for the selected A2B Channel.

| **Csharp Example:**
| A2bNwPolicy a2BNwPolicy = new A2bNwPolicy();

::

   a2BNwPolicy = client.GetNwPolicy("A2B_0"); 

| **Python Example:**
| A2bnetworkpolicy = A2bNwPolicy()

::

   A2bnetworkpolicy = client.GetNwPolicy("A2B_0")

| 
| ====Update Network Policy==== This API used for Updating A2B network policy for the specified A2B channel. It takes elementUid and NwPolicy as argument and returns SSPResult. It is recommended to read the network policy using GetNwPolicy before updating the policy.

| **API:**
| AnalogDevices.SigmaStudio.Scripting.A2bNwPolicy UpdateNetworkPolicy (string elementUid, list NwPolicy);

| **Arguments:**
| A2B Network policy contains below parameters for users to update Network policy from thrift. Rest of the parameters are read only parameters and not to be changed.

-  “elementUid” = UID of the A2B Channel
-  “NwPolicy” - Following are the list Parameters for NwPolicy

   -  DsvryMode

      -  NDiscoveryStartDelay
      -  BOverrideSelfDisc
      -  RediscoveryWaitTimeInMilliSecondsResult
      -  OLineFaultDbSettings. bEnablePostDiscFaultDiag
      -  OLineFaultDbSettings.bAutoDiscoveryOnPDFault
      -  OLineFaultDbSettings.CanPerformPartialDiscovery
      -  OLineFaultDbSettings.nNumAttemptsCritical
      -  OLineFaultDbSettings.RediscoveryInterval

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateNetworkPolicy action.

-  IsSuccess is set to 'True' if the UpdateNetworkPolicy was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| A2bNwPolicy network = new A2bNwPolicy();

::

   ADI_A2B_LINE_FAULT_SETTINGS Linefault = new ADI_A2B_LINE_FAULT_SETTINGS();
   ADI_A2B_DISCOVERY_MODE discmode = ADI_A2B_DISCOVERY_MODE.A2B_SIMPLE_DISCOVERY; 

   // Setting properties for Linefault
   Linefault.bEnablePostDiscFaultDiag = true;
   Linefault.bAutoDiscoveryOnPDFault = true;
   Linefault.CanPerformPartialDiscovery = false;
   Linefault.nNumAttemptsCritical = 5;
   Linefault.RediscoveryInterval = 100;
   // Assign Linefault to network
   network.oLineFaultDbSettings = Linefault;
   // Setting other properties for network
   network.DsvryMode = discmode;
   network.bOverrideSelfDisc = true;
   network.RediscoveryWaitTimeInMilliSeconds = 25;
   // Update the network policy for device "A2B_0"
   _ssp_result = client.UpdateNetworkPolicy("A2B_0", network);

| **Python Example:**
| network = A2bNwPolicy()

::

   Linefault = ADI_A2B_LINE_FAULT_SETTINGS()
   discmode = ADI_A2B_DISCOVERY_MODE()
   Linefault.bEnablePostDiscFaultDiag = True
   Linefault.bAutoDiscoveryOnPDFault = True
   Linefault.CanPerformPartialDiscovery = False
   Linefault.nNumAttemptsCritical = 5
   Linefault.RediscoveryInterval = 100
   network.oLineFaultDbSettings = Linefault
   network.DsvryMode = discmode.A2B_SIMPLE_DISCOVERY
   network.nDiscoveryStartDelay = 25
   network.bOverrideSelfDisc = True
   network.RediscoveryWaitTimeInMilliSeconds = 25
   ssp_result = client.UpdateNetworkPolicy("A2B_0", network)

| 
| ====Get Level Stack Debug Info==== This API used for getting information of Stack Level Debug information for the specified A2B channel. It takes elementUid as argument and returns SSPResult.

| **API:**
| AnalogDevices.SigmaStudio.Scripting.LevelListSent GetLevelStackDbgSettings (string elementUid)

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

| **Result:**
| This API returns List of Level stack debug details for the selected A2B Channel.

| **Csharp Example:**
| LevelListSent level = new LevelListSent();

::

   level = client.GetLevelStackDbgSettings("A2B_0");

| **Python Example:**
| level = LevelListSent()

::

   level = client.GetLevelStackDbgSettings("A2B_0")

| 
| ====Get Domain Stack Debug Info==== This API used for getting information of Stack Domain Debug information for the specified A2B channel. It takes elementUid as argument and returns SSPResult.

| **API:**
| AnalogDevices.SigmaStudio.Scripting.DomainListSent GetDomainStackDbgSettings (string elementUid)

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

| **Result:**
| This API returns List of Domain stack debug details for the selected A2B Channel.

| **Csharp Example:**
| DomainListSent domain = new DomainListSent();

::

   domain = client.GetDomainStackDbgSettings("A2B_0");

| **Python Example:**
| domain = DomainListSent()

::

   domain = client.GetDomainStackDbgSettings("A2B_0")

| 
| ====Update Stack Level Debug Settings==== This API used for updating the Trace level Debug settings for the specified A2B channel. It takes elementUid and LevelListSent as argument and returns SSPResult.

| **API:**
| SSPResult UpdateLevelStackDbgSettings (string elementUid, List LevelListSent);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “LevelListSent” – List of Trace Level

   -  LevelListSentChecked

      -  LevelListSentNum

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateLevelStackDbgSettings action.

-  IsSuccess is set to 'True' if the UpdateLevelStackDbgSettings was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| LevelListSent levelstack = new LevelListSent();

::

   levelstack.LevelListSentChecked = true;
   levelstack.LevelListSentNum = 2;
   _sspresult = client.UpdateLevelStackDbgSettings("A2B_0", levelstack);

| **Python Example:**
| levelstack = LevelListSent()

::

   levelstack.LevelListSentChecked = True
   levelstack.LevelListSentNum = 2
   ssp_result = client.UpdateLevelStackDbgSettings("A2B_0", levelstack)

| 
| ====Update Stack Domain Debug Settings==== This API used for updating the Trace Domain Debug settings for the specified A2B channel. It takes elementUid and DomainListSent as argument and returns SSPResult.

| **API:**
| SSPResult UpdateDomainStackDbgSettings (string elementUid, List DomainListSent);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “DomainListSent” – List of Trace Level

   -  DomainListSentChecked

      -  DomainListSentNum

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateDomainStackDbgSettings action.

-  IsSuccess is set to 'True' if the UpdateDomainStackDbgSettings was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| DomainListSent domainstack = new DomainListSent();

::

   domainstack.DomainListSentChecked = true;
   domainstack.DomainListSentNum = 6;
   _sspresult = client.UpdateDomainStackDbgSettings("A2B_0", domainstack);

| **Python Example:**
| domainstack = DomainListSent()

::

   domainstack.DomainListSentChecked = True
   domainstack.DomainListSentNum = 6
   ssp_result = client.UpdateDomainStackDbgSettings("A2B_0", domainstack)

.. note::

   After executing the necessary APIs, proceed with the Link Operation to view the settings in the graphical user interface (GUI).


.. tip::

   For additional details on Network properties, you may refer the :doc:`A2B Plugin for SigmaStudio+ Quick start Guide </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-a>`.

