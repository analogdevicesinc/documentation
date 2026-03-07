:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio>`

SigmaStudio+ Scripting
======================

As a startup guide, this page simply introduces to the Scripting functionality supported by SigmaStudio+ Application. This uses Apache Thrift and RPC protocol in order to connect to the server application(SS+). An example (i.e., CSharp client/Python) is also given along with the package to make the user understand basic actions that are available for Scripting. Refer to :doc:`Remote Execute </wiki-migration/resources/tools-software/sigmastudiov2/tutorials/remoteexecute>` for detailed example for client application.


| Available actions for SigmaStudio+ scripting:

-  :doc:`CreateNewProject </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/createnewproject>`
-  :doc:`SaveProject </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/saveproject>`
-  :doc:`OpenExistingProject </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/openproject>`
-  :doc:`AddShape </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/addshape>`
-  :doc:`RemoveShape </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/removeshape>`
-  :doc:`AddConnection </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/addconnection>`
-  :doc:`RemoveConnection </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/removeconnection>`
-  :doc:`MoveShape </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/moveshape>`
-  :doc:`RotateShape </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/rotateshape>`
-  :doc:`ResizeShape </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/resizeshape>`
-  :doc:`Link </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/link>`
-  :doc:`LinkCompileConnect </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/linkcompileconnect>`
-  :doc:`LinkCompileDownload </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/linkcompiledownload>`
-  :doc:`UpdateProperties </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/updateproperties>`
-  :doc:`GetAllPlugins </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/getallplugins>`
-  :doc:`GetAvailableCanvas </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/getavailablecanvaselements>`
-  :doc:`GetCanvasElements </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/getelementsinsidecanvas>`
-  :doc:`GetProperties </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/getproperties>`
-  :doc:`Export </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/export>`
-  :doc:`Import </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/import>`
-  :doc:`GetPluginProperties </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/getpluginproperties>`
-  :doc:`UpdateBooleanProperty </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/updatebooleanproperty>`
-  :doc:`UpdateNumericProperty </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/updatenumericproperty>`
-  :doc:`UpdateStringProperty </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/updatestringproperty>`
-  :doc:`UpdateListProperty </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/updatelistproperty>`
-  :doc:`ExportPreset </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/exportpreset>`
-  :doc:`ImportPreset </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/importpreset>`
-  :doc:`Execute </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/execute>`
-  :doc:`Read </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/read>`
-  :doc:`LoadShape </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/loadshape>`
-  :doc:`SaveShape </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/saveshape>`
-  :doc:`GetCaptureViewEntries </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/getcapture>`
-  :doc:`ClearCaptureViewEntries </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/clearcapture>`
-  :doc:`UpdateLabel </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/updatelabel>`
-  :doc:`MigrateTarget </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/migratetarget>`
-  :doc:`NewSequence </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/newsequence>`
-  :doc:`OpenSequenceFile </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/opensequencefile>`
-  :doc:`SaveSequence </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/savesequence>`
-  :doc:`AddSequenceMode </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/addsequencemode>`
-  :doc:`DeleteSequenceMode </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/deletesequencemode>`
-  :doc:`AddSequenceEntry </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/addsequenceentry>`
-  :doc:`DeleteSequenceEntry </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/deletesequenceentry>`
-  :doc:`DownloadSequence </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/downloadsequence>`
-  :doc:`SetSequenceMode </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/setsequencemode>`
-  :doc:`CloseProject </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/closeproject>`
-  :doc:`GetPinCollections </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting/getpincollections>`

|

| ==== Scripting.Thrift==== We support Apache Thrift up to version 20.0, ensuring compatibility with the latest features and improvements.

This file is given out for the user to generate files in a specific language with the help of commands as given in the Apache Thrift startup guide.

| https://thrift.apache.org/tutorial/.
