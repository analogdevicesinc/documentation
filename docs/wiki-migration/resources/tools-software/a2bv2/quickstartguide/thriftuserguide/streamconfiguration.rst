:doc:`Click here to return to Thrift User Guide Homepage </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide>`

List of API in Stream and Tunnel Configuration
==============================================

-  **Stream Configuration APIs**

   -  :doc:`Add Stream </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/streamconfiguration>`

      -  :doc:`Update Stream </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/streamconfiguration>`
      -  :doc:`Delete Stream </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/streamconfiguration>`
      -  :doc:`Import Stream </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/streamconfiguration>`
      -  :doc:`Export Stream </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/streamconfiguration>`
      -  :doc:`GetStreamInfo </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/streamconfiguration>`

-  **Tunnel Configuration APIs**

   -  :doc:`Add Tunnel </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/streamconfiguration>`

      -  :doc:`Update Tunnel </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/streamconfiguration>`
      -  :doc:`Delete Tunnel </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/streamconfiguration>`
      -  :doc:`GetTunnelInfo </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/streamconfiguration>`

-  **Generic Configuration**

   -  :doc:`Strict Bound </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/streamconfiguration>`

      -  :doc:`Auto Calculate check box </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/streamconfiguration>`
      -  :doc:`Optimize and Default </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/streamconfiguration>`

| 
| ==== Add Stream ==== AddStream API is used for adding the stream configuration. It takes element Uid and stream information as arguments and returns SSPResult.

| **API:**
| SSPResult AddStream(string elementUid, AnalogDevices.SigmaStudio.Scripting.ADI_A2B_STREAM stream);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “stream” = stream definition which contains below parameters

   -  StreamName – Name of the Stream

      -  StreamID – Stream ID
      -  SamplingRate – Sampling rate
      -  NNumCh – No.of Channels
      -  ChannelsToSkip – Channels to Skip
      -  NWidth – Data Width
      -  StreamSourceNodeID – Source Node Id of stream
      -  DestID – List of destination id’s
      -  StreamSource – Source Stream
      -  NNumSlots – No.of slots
      -  DestNode – Destination Node dictionary with name and Id

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of AddStream action.

-  IsSuccess is set to 'True' if the AddStream was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| ADI_A2B_STREAM stream = new ADI_A2B_STREAM();

::

    stream.NNumCh = 2; // No.of Channels
    stream.NWidth = 16;
    stream.DestID = new List<int>();
    stream.DestNode = new Dictionary<string, int>();
    stream.StreamSource = "";
    stream.SamplingRate = 48;
    stream.StreamSourceNodeID = 1;
    stream.StreamName = "Stream_1";
    stream.StreamID = 1; 
    client.AddStream("A2B_0", stream);

| **Python Example:**
| stream.StreamName = "Stream_1"

::

    stream.StreamID = 1
    stream.SamplingRate = 48
    stream.nNumCh = 2
    stream.ChannelsToSkip = 0
    stream.nWidth = 24
    stream.StreamSourceNodeID = 1
    stream.DestID = []
    stream.StreamSource = ""
    stream.nNumSlots = 32
    stream.DestNode = {}
    ssp_result = client.AddStream("A2B_0", stream)

| 
| ====Update Stream==== Update Steam API is used for updating the stream configuration. It takes element Uid, property name and property value as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateStream(string elementUid, string propertyName, AnalogDevices.SigmaStudio.Scripting.NetworkStreamConfig stream)

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyName” = Property Name of updated Steam parameter.

   -  EditStream – For updating existing stream details.

      -  StreamDestChanged – For updating Steam Destination Change
      -  StreamSourceChanged – For updating Stream Source change.

-  “stream” = stream definition which contains below parameters

   -  StreamName – Name of the Stream

      -  StreamID – Stream ID
      -  SamplingRate – Sampling rate
      -  NNumCh – No.of Channels
      -  ChannelsToSkip – Channels to Skip
      -  NWidth – Data Width
      -  StreamSourceNodeID – Source Node Id of stream
      -  DestID – List of destination id’s
      -  StreamSource – Source Stream
      -  NNumSlots – No.of slots
      -  DestNode – Destination Node dictionary with name and Id

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateStream action.

-  IsSuccess is set to 'True' if the UpdateStream was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **CSharp Example**
| ADI_A2B_STREAM stream = new ADI_A2B_STREAM();

::

   stream.NNumCh = 4;
   stream.NWidth = 24;
   stream.DestID = new List<int>();
   stream.DestNode = new Dictionary<string, int>();
   stream.StreamSource = "";
   stream.SamplingRate = 48;
   stream.StreamSourceNodeID = 1;
   stream.StreamName = "From main to sub 0 & 1";
   NetworkStreamConfig streamConfig = new NetworkStreamConfig();
   streamConfig.Stream = stream;
   streamConfig.Position = 0;
   client.UpdateStream("A2B_0", "EditStream", streamConfig);
   // For Stream Destination
   streamConfig.DestID = new List<int>();
   streamConfig.Position = 0;
   streamConfig.DestID.Add(-1); // For Stream destination Main Node
   streamConfig.DestID.Add(1);
   client.UpdateStream("A2B_0", "StreamDestChanged", streamConfig);
   // For updating Stream Source 
   streamConfig.Position = 2;
   streamConfig.Stream.StreamSourceNodeID = -1; // For Stream Source Main Node
   _result = client.UpdateStream("A2B_0", "StreamSourceChanged", streamConfig);

| **Python Example:**
| stream.StreamName = "Stream_1"

::

   stream.StreamID = 1
   stream.SamplingRate = 48
   stream.nNumCh = 2
   stream.ChannelsToSkip = 0
   stream.nWidth = 24
   stream.StreamSourceNodeID = -1
   stream.DestID = []
   stream.StreamSource = ""
   stream.nNumSlots = 32
   stream.DestNode = {}
   networkconfig.Position = 0
   networkconfig.Stream = stream
   networkconfig.DestID = []
   networkconfig.DestID.append(-1)
   networkconfig.DestID.append(1)
   ssp_result = client.UpdateStream("A2B_0", "StreamDestChanged", networkconfig)

.. note::

   
   -  UpdateStream operation will affect based on streamConfig.Position value.
   -  Stream Destination or Source for Main node value is -1.
   
   |


| ====Delete Stream==== This API is used for deleting the stream. It takes element Uid, property name and stream index as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateNumericProperty(string elementUid, string propertyName, double propertyVal);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyVal” = Stream Index which is going to Delete (Index will start from 0 and considered based on the UI display order)
-  “propertyName” = Name of the action property

   -  RemoveStream – For deleting the stream.

      -  MoveUp – For moving the Stream up in the UI list
      -  MoveDown -For moving the Stream down in the UI list

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of DeleteStream action.

-  IsSuccess is set to 'True' if the DeleteStream was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| client.UpdateNumericProperty("A2B_0", "RemoveStream", 0);

| **Python Example:**
| ssp_result = client.UpdateNumericProperty("A2B_0", "RemoveStream", 0)
| ====Import Stream==== This API is used for importing the stream configuration from the given xml file path. It takes element Uid, property name and XML file path as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateStringProperty(string elementUid, string propertyName, string propertyVal);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyName” = Name of the action property

   -  ImportStream – For importing the stream configuration.

-  “propertyVal” = Stream configuration xml file full path from which we are going to import stream configuration.

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of ImportStream action.

-  IsSuccess is set to 'True' if the ImportStream was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| client.UpdateStringProperty("A2B_0", "ImportStream", @"C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Rel1.3.0\\Schematics\\Thrift\\adi_a2b_stream_config.xml");

| **Python Example:**
| ssp_result = client.UpdateStringProperty(("A2B_0", "ImportStream", " C:/Analog Devices/ADI_A2B-SSPlus_Software-Rel1.3.0/Schematics/Thrift/adi_a2b_stream_config.xml")

|

.. note::

   Ensure XML file validations specified in the API arguments are addressed prior to calling this API.


| ====Export Stream==== This API is used for exporting the stream configuration into the given xml file path location. It takes element Uid, property name and XML file path as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateStringProperty(string elementUid, string propertyName, string propertyVal);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyName” = Name of the action property

   -  ExportStream– For exporting the stream configuration.

-  “propertyVal” = Stream configuration xml file full path to where we are going to export stream configuration.

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of ExportStream action.

-  IsSuccess is set to 'True' if the ExportStream was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| client.UpdateStringProperty("A2B_0", "ExportStream", @"C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Rel1.3.0\\Schematics\\Thrift\\adi_a2b_stream_config.xml");

| **Python Example:**
| ssp_result = client.UpdateStringProperty(("A2B_0", "ExportStream", " C:/Analog Devices/ADI_A2B-SSPlus_Software-Rel1.3.0/Schematics/Thrift/adi_a2b_stream_config.xml")

|

.. note::

   Ensure XML file validations specified in the API arguments are addressed prior to calling this API.


| ====GetStreamInfo==== This API used for Getting All Stream details. It takes elementUid as argument and returns List of Stream data.

| **API:**
| List<AnalogDevices.SigmaStudio.Scripting.ADI_A2B_STREAM> GetStreamInfo(string elementUid);

| **Arguments:**
| \* “elementUid” = Name of the action property

| **Result:**
| This API returns List of all Stream details for the selected A2B Channel.

| **Csharp Example:**
| List<ADI_A2B_STREAM> aDI_A2B_STREAMs = new List<ADI_A2B_STREAM>();

::

   aDI_A2B_STREAMs = client.GetStreamInfo("A2B_0");

| **Python Example:**
| stream = ADI_A2B_STREAM()

::

   stream = client.GetStreamInfo("A2B_0")

|

.. tip::

   For additional details on stream configuration, you may refer the :doc:`A2B Plugin for SigmaStudio+ User Guide </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/drawinga2bschematics>`.


| ====Add Tunnel==== Add Tunnel API is used for adding new tunnel into the tunnel configuration. It takes element Uid and tunnel object as arguments and returns SSPResult.

| **API:**
| SSPResult AddTunnel(string elementUid, AnalogDevices.SigmaStudio.Scripting.ADI_A2B_TUNNEL_STREAM tunnel);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “tunnel” = tunnel stream information which we are going to add.

   -  Tunnel Name – Name of the Stream

      -  Tunnel ID – Tunnel ID
      -  No.of Down slots – Number of down slots
      -  No.of Up slots – Number of up slots
      -  Member Node ID – To be empty

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of AddTunnel action.

-  IsSuccess is set to 'True' if the AddTunnel was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| ADI_A2B_TUNNEL_STREAM tunnel = new ADI_A2B_TUNNEL_STREAM();

::

    tunnel.TunnelName = "Tunnel0_1";
    tunnel.TunnelID = 1;
    tunnel.NumDwnSlots = 2;
    tunnel.NumUpSlots = 2;
    NetworkStreamConfig tunnelConfig = new NetworkStreamConfig();
    tunnelConfig.Tunnels = tunnel;
    tunnel.MemberNodeID = new List<int>(); 
    tunnel.TunnelID = 0;
    tunnel.MemberNodeID.Add(-1); // For Main Node
    tunnel.MemberNodeID.Add(0); // For Sub0 
   _result = client.AddTunnel("A2B_0", tunnel); // Add Tunnel

| **Python Example:**
| tunnel = ADI_A2B_TUNNEL_STREAM()

::

   tunnel.tunnelName = "Tunnel_1";
   tunnel.tunnelID = 1
   tunnel.numDwnSlots = 2
   tunnel.numUpSlots = 2
   tunnel.memberNodeID = []
   tunnel.memberNodeID.append(-1)
   tunnel.memberNodeID.append(0)
   tunnelconfig.Tunnels = tunnel
   tunnel.upOffset = 0
   tunnel.dwnOffset = 0
   tunnel.schedule = 1
   ssp_result = client.AddTunnel("A2B_0", tunnel)

|

.. note::

   Member Node Id for Main node value is -1.


| ====Update Tunnel==== This API is used for updating the tunnel in the tunnel configuration. It takes element Uid, property name and property value as arguments and returns SSPResult.
| **API:**
| SSPResult UpdateStream(string elementUid, string propertyName, AnalogDevices.SigmaStudio.Scripting.NetworkStreamConfig stream)

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyName” = Property Name of updated Steam parameter.

   -  EditStream – For updating existing stream details.

      -  TunnelParticipantChanged– For updating Tunnel Participants Change

-  “stream” = stream definition which contains below parameters

   -  StreamSource – Source stream

      -   nNumSlots – No. of Slots
      -  StreamName – Stream Name
      -  StreamID – Stream ID
      -  SamplingRate – Sampling Rate in Khz
      -  nNumCh – No. of channels
      -  StreamSourceNodeID – Source Stream Node ID
      -  DestID – Destination Node ID

-  “Tunnel” = Tunnel definition which contains below parameters

   -  numDwnSlots – No. of DownSlots

      -  numUpSlots – No. of Upslots
      -  memberNodeID – Tunnel Participants Member Node ID
      -  memberNode – Tunnel Participants Member Nodes
      -  tunnelColor – Tunnel Color
      -  upOffset – Upoffset value
      -  dwnOffset – Downoffset Value
      -  schedule - Schedule
      -  tunnelName – Tunnel Name
      -  tunnelID – Tunnel ID

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateTunnel action.

-  IsSuccess is set to 'True' if the UpdateTunnel was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| ADI_A2B_STREAM stream = new ADI_A2B_STREAM();

::

   ADI_A2B_TUNNEL_STREAM tunnel = new ADI_A2B_TUNNEL_STREAM();
   NetworkStreamConfig tunnelconfig = new NetworkStreamConfig();
   // Setting properties for the stream object
   stream.StreamSource = "";
   stream.nNumSlots = 2;
   stream.StreamName = "";
   stream.StreamID = 0;
   stream.SamplingRate = 48;
   stream.nNumCh = 24;
   stream.StreamSourceNodeID = 1;
   stream.DestID = new List<int>(); 
   // Setting properties for the tunnel object
   tunnel.numDwnSlots = 2;
   tunnel.numUpSlots = 2;
   tunnel.memberNodeID = new List<int>();
   tunnel.memberNodeID.Add(0);
   tunnel.memberNodeID.Add(1);  
   tunnel.memberNode = new Dictionary<int, int>(); 
   tunnel.tunnelColor = "Transparent"; 
   tunnel.upOffset = 0;
   tunnel.dwnOffset = 0;
   tunnel.schedule = false;
   tunnel.tunnelName = "Tunnel0_0";
   tunnel.tunnelID = 0;
   // Assigning tunnel to tunnelconfig
   tunnelconfig.Tunnels = tunnel; 
   tunnelconfig.Stream = stream;
   tunnelconfig.Position = 0;
   tunnelconfig.DestID = new List<int>(); 
   // Updating the Tunnel configuration for device "A2B_0"
   _sspresult = client.UpdateStream("A2B_0", "TunnelParticipantChanged", tunnelconfig);

| **Python Example:**
| stream = ADI_A2B_STREAM()

::

   tunnel = ADI_A2B_TUNNEL_STREAM()
   tunnelconfig = NetworkStreamConfig()
   stream.StreamSource = ""
   stream.nNumSlots = 2
   stream.StreamName = ""
   stream.StreamID = 0
   stream.SamplingRate = 48
   stream.nNumCh = 24
   stream.StreamSourceNodeID = 1
   stream.DestID = []
   tunnel.numDwnSlots = 2
   tunnel.numUpSlots = 2
   tunnel.memberNodeID = []
   tunnel.memberNodeID.append(0)
   tunnel.memberNodeID.append(1)
   tunnel.memberNode = {}
   tunnel.tunnelColor = "Transparant"
   tunnel.upOffset = 0
   tunnel.dwnOffset = 0
   tunnel.schedule = False
   tunnel.tunnelName = "Tunnel0_0"
   tunnel.tunnelID = 0
   tunnelconfig.Tunnels = tunnel
   tunnelconfig.Stream = stream
   tunnelconfig.Position = 0
   tunnelconfig.DestID = []
   ssp_result = client.UpdateStream("A2B_0", "TunnelParticipantChanged", tunnelconfig)

| 
| ====Delete Tunnel==== This API is used for deleting theTunnel. It takes element Uid, property name and stream index as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateNumericProperty(string elementUid, string propertyName, double propertyVal);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyVal” = Tunnel Index which is going to Delete (Index will start from 0 and considered based on the UI display order)
-  “propertyName” = Name of the action property

   -  DeleteTunnel– For deleting the stream.

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of DeleteTunnel action.

-  IsSuccess is set to 'True' if the DeleteTunnel was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| \_sspresult = client.UpdateNumericProperty("A2B_0", "DeleteTunnel", 0);

| **Python Example:**
| ssp_result = client.UpdateNumericProperty("A2B_0", "DeleteTunnel", 0)
| ====GetTunnelInfo==== This API used for Getting All Stream details. It takes elementUid as argument and returns List of Stream data.

| **API:**
| List<AnalogDevices.SigmaStudio.Scripting. ADI_A2B_TUNNEL_STREAM> GetTunnelInfo(string elementUid);

| **Arguments:**
| \* “elementUid” = Name of the action property

| **Result:**
| This API returns List of all Tunnel details for the selected A2B Channel.

| **Csharp Example:**
| ADI_A2B_TUNNEL_STREAM Tunnel = new ADI_A2B_TUNNEL_STREAM();

::

   Tunnel = client.GetTunnelInfo("A2B_0");

| **Python Example:**
| Tunnel = ADI_A2B_TUNNEL_STREAM()

::

   Tunnel = client.GetTunnelInfo(“A2B_0”)

| 
| ====StrictBound==== This API is used for enabling/disabling StrictBound option. It takes element Uid and property name and property value as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateBooleanProperty(string elementUid, string propertyName, bool propertyVal);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyName” = Name of the action property. Some of the property name examples are listed below

   -  StrictBound– For enabling/disabling StrictBound

-  “PropertyValue” = “True” or “False”

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateBoolProperty action.

-  IsSuccess is set to 'True' if the UpdateBoolProperty was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| \_sspresult = client.UpdateBooleanProperty("A2B_0", "StrictBound", true);

| **Python Example:**
| ssp_result = client.UpdateBooleanProperty("A2B_0", "StrictBound", True)
| ====Auto Calculate check box==== This API is used for enabling/disabling Auto Calculate check box option. It takes element Uid and property name and property value as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateBooleanProperty(string elementUid, string propertyName, bool propertyVal);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyName” = Name of the action property. Some of the property name examples are listed below

   -  AutoCalculateChk– For enabling/disabling Auto Calculate check box

-  “PropertyValue” = “True” or “False”

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateBoolProperty action.

-  IsSuccess is set to 'True' if the UpdateBoolProperty was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| \_sspresult = client.UpdateBooleanProperty("A2B_0", "AutoCalculateChk", false);

| **Python Example:**
| ssp_result = client.UpdateBooleanProperty("A2B_0", "AutoCalculateChk", False)
| ====Optimize and Default==== This API is used for enabling/disabling Optimize and Default option. It takes element Uid and property name and property value as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateNumericProperty(string elementUid, string propertyName, double propertyVal);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyName” = Name of the action property. Some of the property name examples are listed below

   -  ButtonOptimize – For enabling/disabling Optimize option

      -  ButtonDefault – For enabling/disabling Default option

-  “PropertyValue” = Value of the property which we are going to update.

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateNumericProperty action.

-  IsSuccess is set to 'True' if the UpdateNumericProperty was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| \_sspresult = client.UpdateNumericProperty("A2B_0", "ButtonOptimize", 1);

::

   _sspresult = client.UpdateNumericProperty("A2B_0", "ButtonDefault", 1);

| **Python Example:**
| ssp_result = client.UpdateNumericProperty("A2B_0", "ButtonOptimize", 1)

::

   ssp_result = client.UpdateNumericProperty("A2B_0", "ButtonDefault", 1)

.. note::

   After executing the necessary APIs, proceed with the Link Operation to view the settings in the graphical user interface (GUI).


.. tip::

   For additional details on Tunnel configuration, you may refer the :doc:`A2B Plugin for SigmaStudio+ User Guide </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/drawinga2bschematics>`.

