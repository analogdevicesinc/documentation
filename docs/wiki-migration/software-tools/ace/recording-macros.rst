Recording a macro and generating scripts
========================================

ACE has a feature called Macro Tools to record configuration and device interaction steps by putting them into a file called a Macro. Once a Macro is generated using the Macro Tools feature, it can then be called again thereby repeating the steps performed in one go. Following steps explain how to generate a macro.

-  Open ACE, then go to Tools -> Macro Tools.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/macrotools.png
   :align: center
   :width: 400px

-  Hit the 'record macro commands' button, the left hand side icon on the below image

.. image:: https://wiki.analog.com/_media/software-tools/ace/ace-record_icon.png
   :align: center
   :width: 400px

-  Start performing device interaction such as changing parameters, inputting values to registers on the memorymap, capturing data etc. The 'Commands' windows will fill up as the GUI is navigated and interacted with.
-  Once all parameters to be entered are recorded, hit the 'stop recording macro commands' button. Same location as above.

Once a macro file has been recorded, it can then be stored into a macro file and played again to repeat the previously performed steps.

Additionally, ACE has a built in feature to then generate scripts that perform the recorded actions in a supported language of choice.

-  Click on the Generate icon at the right to open the script generator window.

.. image:: https://wiki.analog.com/_media/software-tools/ace/ace-generate_icon.png
   :align: center
   :width: 400px

-  Select the desired language among C#, MATLAB or Python

|image1| his code can then be imported into an IDE for execution. Using this code as the base, add additional features like instrument control so as to have an automated set of measurements.

The Remote API DLL
==================

Apart from supported languages, the remote API can also be used by IDEs that support DLLs like LabVIEW. The DLL is located in the ACE installation directory within the subfolder "Clients".

.. |image1| image:: https://wiki.analog.com/_media/software-tools/ace/ace-generated-code-editor.png
   :width: 400px
