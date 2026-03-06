:doc:`Click here to return to 'SigmaStudio Scripting' page. </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/scripting>`

Creating and Running SigmaStudio Scripts
========================================

| 
| SigmaStudio scripts allow project files to be created and manipulated using textual commands. The scripting interface is defined in the C# language and supports scripts written in either C# or Visual Basic languages. No previous knowledge of C# is required to write simple SigmaStudio scripts.
| SigmaStudio scripts can be created in any text editor or within SigmaStudio using the “Script Editor” tool. The Script Editor provides IntelliPrompt display of the script interfaces and syntax highlighting functionality. Script files can be saved as text files (\*.txt) or SigmaStudio Script files (\*.sss). Scripts are loaded and run, pause, and stop from the Script Editor window. Pause, Resume and Stop supports by adding the "ALLOW_PAUSE_STOP() " API in Script.
| =====Opening the Script Editor===== In SigmaStudio, click on ToolsScript in main menu to start the Script Editor shown in Figure 2.
| To create a new script file, open the Script Editor window and click File  New (or CTRL + N). This creates a new script file and automatically inserts ``“// #LANGUAGE# C#”`` on the first line. This identifies the script language as C# (c-sharp) the default SigmaStudio scripting language. Visual Basic scripts are also supported. The language identifier is optional for C# scripts but is required for Visual Basic scripts.
| C# (c-sharp) script language identifier — #LANGUAGE# C#
| Visual Basic script language identifier — #LANGUAGE# VB
| |image1|
| Figure 2: Script Editor
| =====Writing a Script===== To access the IScripted interface list, type “sigmastudio” (or optionally “ss”) followed by a period in the Script Editor window. This will display the IntelliPrompt window listing all available IScripted methods. (“sigmastudio” and “ss” are public references to the SigmaStudio IScripted interface, see the following usage example).
| An example script is given below:
| ``// #LANGUAGE# C# 
  sigmastudio.ProjectNew(); 
  sigmastudio.ObjectInsert( "USBi" ); 
  sigmastudio.ObjectInsert( "ADSP-214xx" ); 
  sigmastudio.ObjectConnect( "USB Interface", 0, "IC 1", 0 ); 
  sigmastudio.ObjectInsert( "Audio Input" ); 
  sigmastudio.ObjectInsert( "Output" ); 
  sigmastudio.ObjectInsert( "Output" ); 
  sigmastudio.ObjectConnect( "Audio Input1", 0, "Output1", 0 ); 
  sigmastudio.ObjectConnect( "Audio Input1", 1, "Output2", 0 ); 
  sigmastudio.ProjectLinkCompileDownload(); 
  sigmastudio.ProjectSaveAs( @"C:\SStudioProjects\SampleScript.dspproj" ); 
  sigmastudio.ProjectClose();``
| This example creates a new project, inserts an ADSP-214xx processor and a USB communication channel, and connects them with a wire. Next, it inserts an input object and 2 output objects, connecting the 2 input pins to the output object pins. The project is then linked, compiled, downloaded, saved to disk and closed.
| =====Running a Script===== To run a SigmaStudio Script, in the Script Editor Window, click on main menu Tools > RunScript or press “F5”, see Figure 3. |image2| Figure 3: Running Script
| If there are any errors in the script code, a dialog detailing the errors is displayed and “Script Failure” is shown in the status bar. If the script successfully compiles and runs, “Success” is shown in the Script Editor status bar. |image3| Figure 4: Script Error
| =====Pause and Resume a Script===== To pause a SigmaStudio Script, in the Script Editor Window, click on main menu Tools > Pause, see Figure 5. |image4|
| if the script successfully paused, "Paused" is shown in the Script Editor status bar. Figure 5: Pause Script
| To Resume a SigmaStudio Script, in the Script Editor Window, click on main menu Tools > Resume, see Figure 6. |image5| Figure 6: Resume Script
| =====Stop a Script===== To stop a SigmaStudio Script, in the Script Editor Window, click on main menu Tools > Stop, see Figure 7. |image6|
| if the script successfully stops, a dialog detailing the script execution halted is displayed and “Script Aborted” is shown in the status bar. |image7|
| |image8|
| =====Object Names===== To reference Schematic objects contained in hierarchy boards, the complete object name must be used. The “complete name” consists of the object’s name preceded by the names of all parent Hierarchy boards separated by periods (‘.’).
| For example, in Figure 5 “Filter2” is contained in a Hierarchy board named “Board1”. The complete name of this object is “Board1.Filter2”.

| |image9| Figure 5: Script Object Name Usage
| The following script would remove the Filter2 object:
| ``sigmastudio.ObjectRemove( "Board1.Filter2" );``
| In the next example (Figure 6), Board2 is contained within Board1, so the full name of object in Board2 includes both board names, “Board1.Board2.Gen 1st Order1”.

| |image10| Figure 6: Script Object Name for Board
| =====Advanced Script Support===== Scripts are not limited to the IScripted interface functions. Scripts can take advantage of the C# language and some elements of the .NET framework. A sample script to add object to a Schematic, modify its attributes and interconnect them is given below.
| ``// #LANGUAGE# C# 
  ss.ProjectOpen( @"C:\SStudioProjects\SampleScript.dspproj"); 
  ss.ObjectDisconnect( "Audio Input1", 0, "Output1", 0 ); 
  ss.ObjectDisconnect( "Audio Input1", 1, "Output2", 0 ); 

  try 
  { 
      int nNumFilters = 4;
      for (int i = 0; i < nNumFilters; ++i)
      {
          object oFilter = ss.ObjectInsert( "General (2nd order)" ); 
          if (null != oFilter) 
          { 
              string strNewName = "Filter_" + (i + 1); 
              ss.ObjectSetProperties( "setName", oFilter, strNewName ); 
              ss.ObjectSetProperties( "addAlgorithm", strNewName, "IC 1", "2 Channel - Single Precision" ); 
          } 
          else 
          { 
              throw new Exception( "ln 11" ); 
          } 
      } 
      HResult hr = HResult.S_OK; 
      for (int ixPin = 0; ixPin < 2; ++ixPin)
      { 
          if (HResult.S_OK != sigmastudio.ObjectConnect( "Audio Input1",ixPin, "Filter_1", ixPin )) 
              throw new Exception( "ln 28" ); 
          if (HResult.S_OK != sigmastudio.ObjectConnect( "Filter_1", ixPin, "Filter_2", ixPin )) 
              throw new Exception( "ln 31" ); 
          if (HResult.S_OK != sigmastudio.ObjectConnect( "Filter_2", ixPin, "Filter_3", ixPin )) 
              throw new Exception( "ln 34" ); 
          if (HResult.S_OK != sigmastudio.ObjectConnect( "Filter_3", ixPin, "Filter_4", ixPin )) 
              throw new Exception( "ln 37" ); 
      } 
      if (HResult.S_OK != sigmastudio.ObjectConnect( "Filter_4", 0, "Output1", 0 )) 
          throw new Exception( "ln 42" ); 
      if (HResult.S_OK != sigmastudio.ObjectConnect( "Filter_4", 1, "Output2", 0 )) 
          throw new Exception( "ln 45" ); 
  } 
  catch(Exception e) 
  { 
      System.Windows.Forms.MessageBox.Show( "FAILURE: " + e.ToString() );
  }``

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/4.1.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/4.3_1.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/4.3_2.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/pausescript.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/scriptresume.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/stopscript.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/scriptstopdialog.png
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/scriptaborted.png
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/4.4_1.jpg
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/4.4_2.jpg
