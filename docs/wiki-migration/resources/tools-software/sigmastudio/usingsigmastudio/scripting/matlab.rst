:doc:`Click here to return to 'SigmaStudio Scripting' page. </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/scripting>`

SigmaStudio as a MATLAB® COM server
===================================

To use MATLAB as a SigmaStudio server client, both applications must be installed and running on the same machine.

In this configuration, MATLAB is a COM automation client and SigmaStudio (via SigmaStudioServer) becomes a COM automation server. For COM operation, the SigmaStudioServer must first be registered as a COM object.

Registering SigmaStudioServer as a COM object
---------------------------------------------

Automatic COM object Registration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have installed SigmaStudio in its default directory (C:\\Program Files\\Analog Devices\\SigmaStudio X.xx, where X.xx is the version), and your .NET framework is up to date, you may use the SigmaStudioServer Registration utility. `Right-click here <https://raw.githubusercontent.com/tkrome/SigmaStudio-Server-Registration/master/SigmaServerReg.bat>`__, and click "Save link as...," then run the saved file as an administrator. You will need to enter the version of SigmaStudio ("3.17" for version 3.17, for example), as well as whether you're using 32- or 64-bit MATLAB.

SigmaStudio 3.16 and below
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Ensure that you have RegAsm.exe application available on your machine. It should be present in "C:\\Windows\\Microsoft.NET\\Framework\\v2.0.50727\\". If not installed, download and install the “.NET Framework 2.0 Software Development Kit (SDK)”, available from Microsoft.
-  Open the command prompt (as administrator)

   -  If using 32 bit MATLAB version, change the working directory to "C:\\Windows\\Microsoft.NET\\Framework\\v2.0.50727"
   -  If using 64 bit MATLAB version, change the working directory to "C:\\Windows\\Microsoft.NET\\Framework64\\v2.0.50727"

-  Execute the following command to register the assembly file: RegAsm "C:\\Program Files\\Analog Devices\\SigmaStudio 3.xx\\Analog.SigmaStudioServer.dll" /codebase

| Note: here xx in 3.xx should be the current SigmaStudio version like 3.15.
| You should get a "Type registered successfully" message after the assembly file has been registered.

SigmaStudio 3.17 onwards
~~~~~~~~~~~~~~~~~~~~~~~~

-  Ensure that you have RegAsm.exe application available on your machine. It should be present in "C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319". If not installed, download and install the “.NET Framework 4.7 Software Development Kit (SDK)”, available from Microsoft.
-  Open the command prompt (as administrator)

   -  If using 32 bit MATLAB version, change the working directory to "C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319"
   -  If using 64 bit MATLAB version, change the working directory to "C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319"

-  Execute the following command to register the assembly file: RegAsm "C:\\Program Files\\Analog Devices\\SigmaStudio 3.xx\\Analog.SigmaStudioServer.dll" /codebase

| Note: here xx in 3.xx should be the current SigmaStudio version like 3.15.
| You should get a "Type registered successfully" message after the assembly file has been registered.

Creating a SigmaStudioServer process in MATLAB
----------------------------------------------

.. code:: matlab

   % SigmaSetup.m
   % IMPORTANT: Launch the SigmaStudio application first!

   % Add SigmaStudio installtion directory to path
   path(path, 'C:\Program Files\Analog Devices\SigmaStudio 4.5');

   % Intantiate SigmaStudio server and invoke the interface
   ss = actxserver('Analog.SigmaStudioServer.SigmaStudioServer');
   ss_server = ss.invoke('ISigmaStudioServer');

   % Close the project
   ss_server.CLOSE_PROJECT();

   % Load sample project file
   ss_server.OPEN_PROJECT( "C:\Users\SReddy2\Downloads\Matlab Test\MatLabTest.dspproj");

   % Compile and download program to hardware
   ss_server.COMPILE_PROJECT();

   % Set the Gain Parameter
   ss_server.PARAMETER_WRITE("IC 1",22, 8,24,2.0);

   | 
|

.. note::

   Launch SigmaStudio before running your client [Python or LabView/Matlab].


SigmaStudio as a MATLAB® .NET server
====================================

The documentation for calling .NET Libraries can be found `here <https://www.mathworks.com/help/matlab/using-net-libraries-in-matlab.html>`__. The documentation for calling methods (functions) in .NET libraries can be found `here <https://www.mathworks.com/help/matlab/methods.html>`__.

Set up the communication as follows.

::

   try
     theDir = dir('/Program Files/Analog Devices/**/Analog.SigmaStudioServer.dll');
     if (isempty(theDir))
       fprintf('ERROR: Cannot find Analog.SigmaStudioServer.dll\n');
       return;
     end
   catch
     fprintf('ERROR: Cannot find Analog.SigmaStudioServer.dll\n');
     return;
   end
   theFile = fullfile(theDir(end).folder,'Analog.SigmaStudioServer.dll');
   theAssembly = NET.addAssembly(theFile); % load assembly
   SSclass = Analog.SigmaStudioServer.SigmaStudioServer; % handle to class

Then, you can query the DLL for the implemented methods with

::

   methods SSclass

or, for a very nice table with arguments and return values, use

::

   methodsview(SSclass)
