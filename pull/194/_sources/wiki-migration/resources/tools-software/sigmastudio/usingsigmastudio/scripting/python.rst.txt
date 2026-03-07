:doc:`Click here to return to 'SigmaStudio Scripting' page. </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/scripting>`

SigmaStudio Scripting from Python
=================================

There are two ways the :doc:`SigmaStudio server </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/scripting/server>` APIs can be accessed from Python.

Accessing SigmaStudio through win32com
--------------------------------------

To set up the COM ports for SigmaStudio 4.0:

-  Open an elevated command prompt. Change directory to ``C:\Windows\Microsoft .NET\Framework64\v4.0.30139``.
-  Run the following command: ``RegAsm "C:\Program Files\Analog Devices\SigmaStudio 4.0\Analog.SigmaStudioServer.dll" /codebase`` and the command prompt should return "Types registered successfuly".
-  Now switch directory to the 32-bit version at ``C:\Windows\Microsoft .NET\Framework\v4.0.30139``.
-  Run the same command (``RegAsm "C:\Program Files\Analog Devices\SigmaStudio 4.0\Analog.SigmaStudioServer.dll" /codebase``). The command prompt should again return "Types registered successfuly".

| 
|

.. note::

   Launch SigmaStudio before running your client [Python or LabView/Matlab]. Most clients assume the SigmaStudio endpoint is available. The corresponding error in Python is ``There was no endpoint listening at net.pipe//localhost/SigmaServerPipe``\


.. note::

   Use win32com of version 300 to access SigmaStudio Server API's from python


| ``from  win32com.client.dynamic import Dispatch
  ## This program is designed to test SigmaStudio scripting from Python. 
  if __name__ == "__main__":     
      print('Running')
      server = Dispatch('Analog.SigmaStudioServer.SigmaStudioServer')
      # Make a new SigmaStudio project            
      print('Creating Project...')
      server.new_project
      
      # Hardware Configuration
      print('Inserting HW Config Objects...')
      server.insert_object_point('USBi', 200, 100)
      server.insert_object_point('ADAU1467', 400, 100)
      server.insert_object_point('E2Prom', 400, 180)
      server.connect_object('USB Interface', 0, 'IC 1', 0)
      server.connect_object('USB Interface', 1, 'IC 2', 0)
      # Insert some objects
      print('Inserting Schematic Objects...')
      server.insert_object_point('Sine Tone with Phase and Gain', 50, 100)
      server.insert_object_point('Sine Tone with Phase and Gain', 50, 200)
      server.insert_object_point('Output', 170, 100)
      server.insert_object_point('Output', 170, 200)
      # Change object parameters
      print('Changing Parameters...')
      server.set_object_property('setName', 'Tone1', 'sineWave1', 0, 0, 0)
      server.set_object_property('setName', 'Tone2', 'sineWave2', 0, 0, 0)
      server.set_object_property('setControlValue', 'sineWave1', 0, 0, 'Frequency', '300')
      server.set_object_property('setControlValue', 'sineWave2', 0, 0, 'Frequency', '150')
      server.set_object_property('setControlValue', 'sineWave1', 0, 1, 'Gain', '-40')
      server.set_object_property('setControlValue', 'sineWave2', 0, 1, 'Gain', '-40')
      server.set_object_property('setControlValue', 'sineWave2', 0, 1, 'OnOff', 1)
      server.set_object_property('setControlValue', 'sineWave1', 0, 1, 'OnOff', 1)
      server.set_object_property('setControlValue', 'Output1', 0, 0, 'SelectedChannel', '4')
      # Indexing here works based on the SigmaStudio GUI; so the fourth index is now channel 5
      server.set_object_property('setControlValue', 'Output2', 0, 0, 'SelectedChannel', '4')
      
      # # Connect objects
      server.connect_object('sineWave1', 0, 'Output1', 0)
      server.connect_object('sineWave2', 0, 'Output2', 0)
      # # Compile and download the project to the DSP
      server.compile_project    
      # Turn on output 2    
      server.register_write('IC 1', 62021, 2, 48)    
      # Save project with specific name    
      projectFile= 'C:\\test\\Scripting Test'    
      server.saveas_project(projectFile)``

Register Write
~~~~~~~~~~~~~~

The following code shows how to perform a register write of any length. Only the first three lines need be modified.

.. code:: python

   data = [0x12, 0x01, 0x10, 0x90, 0xc1, 0x20, 0x4c, 0x1d]
   address = 0x20
   ic_name = "IC 1"

   ic_name_variant = VARIANT(pythoncom.VT_BSTR, ic_name)
   address_variant = VARIANT(pythoncom.VT_I4, address)
   num_bytes_variant = VARIANT(pythoncom.VT_I4, len(data))
   data_variant = VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_UI1, data)
   server.REGISTER_WRITE_ARRAY(ic_name_variant, address_variant, num_bytes_variant, data_variant)

FIR Filter
~~~~~~~~~~

Example code to interface with FIR Filters is available at :doc:`FIR Filter </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/firfilter>`.

--------------
