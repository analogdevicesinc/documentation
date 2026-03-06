:doc:`Click here to return to Thrift User Guide Homepage </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide>`

List of API in BERT Properties
==============================

-  :doc:`BERT PRBS Test </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/bertproperties>`
-  :doc:`BERT Audio Test </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/bertproperties>`

| 
| ====BERT PRBS Test==== This API is used to Run PRBS Test. It takes elementUid and property name and property value as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateBooleanProperty(string elementUid, string propertyName, bool propertyVal);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyName” = Name of the action property. Some of the property name examples are listed below

   -  BertCalcLinkStatus – To check Link status

      -  BertCalcRdoPseudoRandom– To check to calculate BERT for PRBS
      -  BertCalcEnablePrbsNodetoNodeChecking - To Enable PRBS
      -  BertCalcEnableAutoReset – For Auto Reset
      -  BertCalcEnableShowErrorDiff – To Enable show Error Difference Checkbox
      -  BertCalcStart – To start BERT Calculation
      -  BertCalcRun – To run BERT Calculation
      -  BertCalcReset – To Reset BERT Calculation

-  “propertyVal” = Setting value (true or false).

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateBoolProperty action.

-  IsSuccess is set to 'True' if the UpdateBoolProperty was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| \_sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcLinkStatus", true);

::

   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcRdoPseudoRandom", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcRdoAudio", false);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcEnablePrbsNodetoNodeChecking", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableDCRCERR", false);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableICRCERR", false);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableDDERR", false);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableDPERR", false);
   _sspresult = client.UpdateNumericProperty("A2B_0", "BertCalcAutoResetInterval", 5.0f);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableAutoReset", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableShowErrorDiff", false);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcAutoGenerateBusErrors", true);
   _sspresult = client.UpdateNumericProperty("A2B_0", "BertCalcTriggerTimeInterval", 2);
   _sspresult = client.UpdateNumericProperty("A2B_0", "BertCalcGenErrSelNode", 0);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcGenDCRCERR", false);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcGenICRCERR", false);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcGenDDERR", false);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcGenDPERR", false);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcGenerateError", false);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcStart", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcRun", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcReset", true);

| **Python Example:**
| ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcLinkStatus", "True")

::

   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcRdoPseudoRandom", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcRdoAudio", "False")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcEnablePrbsNodetoNodeChecking", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableDCRCERR", "False")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableICRCERR", "False")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableDDERR", "False")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableDPERR", "False")
   ssp_result = client.UpdateNumericProperty("A2B_0", "BertCalcAutoResetInterval", float(5.0))
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableAutoReset", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableShowErrorDiff", "False")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcAutoGenerateBusErrors", "True")
   ssp_result = client.UpdateNumericProperty("A2B_0", "BertCalcTriggerTimeInterval", 2)
   ssp_result = client.UpdateNumericProperty("A2B_0", "BertCalcGenErrSelNode", 0)
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcGenDCRCERR", "False")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcGenICRCERR", "False")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcGenDDERR", "False")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcGenDPERR", "False")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcGenerateError", "False")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcStart", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcRun", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcReset", "True")

| 
| ====BERT Audio Test==== This API is used to Run PRBS Test. It takes elementUid and property name and property value as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateBooleanProperty(string elementUid, string propertyName, bool propertyVal);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyName” = Name of the action property. Some of the property name examples are listed below

   -  BertCalcLinkStatus – To check Link status

      -  BertCalcRdoAudio – To check to calculate BERT for Audio errors
      -  BertCalcEnableDCRCERR - To Enable check for Data frame CRC Error
      -  BertCalcEnableICRCERR – To Enable check for interrupt frame CRC Error
      -  BertCalcEnableDDERR – To Enable check for Data Decode Error
      -  BertCalcGenDPERR - To Enable check for Data Parity Error
      -  BertCalcAutoGenerateBusErrors – To Enable to Auto Generate the Errors.
      -  BertCalcGenErrSelNode – Generate Error in Specified node
      -  BertCalcGenDCRCERR – To Generate Data frame CRC Error
      -  BertCalcGenICRCERR – To Generate interrupt frame CRC Error
      -  BertCalcGenDDERR – To Generate Data Decode Error
      -  BertCalcGenDPERR – To Generate Data Parity Error
      -  BertCalcGenerateError – To Generate Error
      -  BertCalcStart – To start BERT Calculation
      -  BertCalcRun – To run BERT Calculation
      -  BertCalcReset – To Reset BERT Calculation

-  “propertyVal” = Setting value (true or false)

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateBoolProperty action.

-  IsSuccess is set to 'True' if the UpdateBoolProperty was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| \_sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcLinkStatus", true);

::

   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcRdoPseudoRandom", false);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcRdoAudio", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcEnablePrbsNodetoNodeChecking", false);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableDCRCERR", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableICRCERR", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableDDERR", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableDPERR", true);
   _sspresult = client.UpdateNumericProperty("A2B_0", "BertCalcAutoResetInterval", 5.0f);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableAutoReset", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableShowErrorDiff", false);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcAutoGenerateBusErrors", true);
   _sspresult = client.UpdateNumericProperty("A2B_0", "BertCalcTriggerTimeInterval", 2);
   _sspresult = client.UpdateNumericProperty("A2B_0", "BertCalcGenErrSelNode", 0);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcGenDCRCERR", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcGenICRCERR", false);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcGenDDERR", false);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcGenDPERR", false);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcGenerateError", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcStart", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcRun", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "BertCalcReset", true);

| **Python Example:**
| ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcLinkStatus", "True")

::

   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcRdoPseudoRandom", "False")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcRdoAudio", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcEnablePrbsNodetoNodeChecking", "False")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableDCRCERR", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableICRCERR", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableDDERR", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableDPERR", "True")
   ssp_result = client.UpdateNumericProperty("A2B_0", "BertCalcAutoResetInterval", float(5.0)) 
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableAutoReset", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcEnableShowErrorDiff", "False")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcAutoGenerateBusErrors", "True")
   ssp_result = client.UpdateNumericProperty("A2B_0", "BertCalcTriggerTimeInterval", 2)
   ssp_result = client.UpdateNumericProperty("A2B_0", "BertCalcGenErrSelNode", 0)
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcGenDCRCERR", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcGenICRCERR", "False")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcGenDDERR", "False")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcGenDPERR", "False")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcGenerateError", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcStart", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcRun", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "BertCalcReset", "True")

.. tip::

   For more information about BERT, you can refer to the :doc:`A2B Plugin for SigmaStudio+ User Guide </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkanalysisanddebug>`.

