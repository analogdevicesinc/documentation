ACE Remote Control
==================

This is a landing page for up-to-date information and examples pertaining to the ACE remote control feature. This feature allows a user to control ACE and evaluation hardware from other languages/applications.

.. tip::

   For documentation on the remote control interface and methods, please look under the Help menu in ACE.


Examples
--------

Python
~~~~~~

In order to use Python with the remote control library, you will need to install the Python.Net package. More details on the package and how to install it can be found here: https://github.com/pythonnet/pythonnet/wiki

Large Data Capture With AD9208
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently 1GB of data can be captured with the ADS8V1 and 2GB of data can be captured with the ADS7V2 using the AsyncRawCaptureToFile transaction. The following example shows how this transaction can be used from a Python script with the AD9208 evaluation platform.

Setup: AD9208 board connected to ADS7V2 or ADS8V1 motherboard. ADC clock = 3GHz, REFCLK = 375 MHz

Python Code:

::


   # Copyright (c) 2019 Analog Devices, Inc.  All Rights Reserved. This software is proprietary to Analog Devices, Inc. and its licensors.

   # These code snippets are provided ‘as is’ with no warranties, guarantees of suitability, or acceptance of any  liability, for their use.

   import clr
   import sys
   import os
   import time

   # Connect to ACE using the remote control client
   sys.path.append(r'C:\Program Files (x86)\Analog Devices\ACE\Client')
   clr.AddReference('AnalogDevices.Csa.Remoting.Clients')
   import AnalogDevices.Csa.Remoting.Clients as adrc
   clientManager = adrc.ClientManager.Create()
   client = clientManager.CreateRequestClient('localhost:2358')

   # Load the AD9208 plug-in
   client.AddHardwarePlugin('AD9208-3000EBZ')

   # Navigate to initialization wizard and set to one converter
   client.set_ContextPath(r'\System\Subsystem_1\AD9208-3000EBZ\AD9208')
   client.NavigateToPath('Root::System.Subsystem_1.AD9208-3000EBZ.AD9208')
   client.SetWizardParameter('initwizard','jtx_m_cfg','0')
   time.sleep(2)
   client.ApplyWizardSettings('initwizard','Apply')

   # Navigate to capture wizard and set the number of samples to 500MSamples (1GB)
   client.NavigateToPath('Root::System.Subsystem_1.AD9208-3000EBZ.AD9208.AD9208 Analysis')
   client.SetWizardParameter('captureWizard','validatedSampleCount',str(2**29))

   # Divert the output of the ADS7V2/ADS8V1 to a file
   client.AsyncRawCaptureToFile(os.path.expanduser('~\Desktop\largeCapture.bin'),'test','false','true')

   # Wait up to 5secs for the capture to complete
   client.WaitOnRawCaptureToFile('5000','test','false',os.path.expanduser('~\Desktop\largeCapture.bin'))

Download Python and Jupyter Notebook versions of this example: `large_capture_example.zip <https://wiki.analog.com/_media/resources/tools-software/ace/large_capture_example.zip>`_

LabVIEW
~~~~~~~

More information on the following example will be added.

`labview_2015_demo.zip <https://wiki.analog.com/_media/resources/tools-software/ace/remote-control/labview_2015_demo.zip>`_
