AD5791 ACE Remote Control
=========================

Following section contains the source code for a simple application to calculate the INL and DNL values for a DAC and a guide on how to use it. The Application writes codes to a DAC in the AD5791 family using the :adi:`ACE tool <en/design-center/evaluation-hardware-and-software/ace-software.html>` and reads voltages recorded on an instrument using VISA.

Getting Started
---------------

Hardware
~~~~~~~~

-  :adi:`SDP-B Controller board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/SDP-B.html>` and it's 12V DC adapter
-  :adi:`AD5791 Evaluation Board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD5791.html>` or an equivalent board that has any of the following DACs

   -  AD5790
   -  AD5781
   -  AD5780
   -  AD5760

-  +/-15V Power Supply for the evaluation board.
-  A Digital Multimeter that supports VISA. The `Keysight 3458A Digital Multimeter <https://www.keysight.com/en/pdx-2905513-pn-3458A/digital-multimeter-8-digit?cc=SG&lc=eng>`__ was used when the script was written. For a different instrument, you need to consult it's manufacturer's website/documentation.
-  A USB to GPIB or equivalent connector for interfacing the instrument to your PC.

Software
~~~~~~~~

-  :adi:`ACE software <en/design-center/evaluation-hardware-and-software/ace-software.html>`
-  AD5791 ACE plugin can be downloaded from within ACE
-  A python environment.
-  Python script; Download from `here. <https://wiki.analog.com/_media/resources/tools-software/other-software/ad5791_inl_dnl-master_193b34dd42b.zip>`__

Setting Up
----------

Setting Up the python environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Download and install Python 3.7 from `here <https://www.python.org/downloads/>`__. Make sure that the "Add Python 3.7 to PATH" option is enabled.\


|image1|

-  Open a command prompt/powershell window in the same directory as the extracted files. Then install the required packages by running the following command:``pip install -r requirements.txt``
-  Run the script by using the command:``python Main.py``

Hardware and ACE
~~~~~~~~~~~~~~~~

Refer to the :adi:`Evaluation Board user guide <media/en/technical-documentation/user-guides/EVAL-AD5791SDZ-UG-1152.pdf>` on powering the board up and setting up the ACE plugin. Please make sure that the plugin is functional and the device responds to the plugin interaction before proceeding further.

Setting up communication between ACE and the Python script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Open ACE, then go to Tools -> Settings.\


|image2|

-  Go to IPC Server Tab and ensure that it is enabled. Also ensure that a port is allocated.\

|image3|

-  In the file "ACERemoteController.py", ensure that the port number matches on line 70.\

|image4|

Running the application
-----------------------

-  Make a note of the following constants (lines 52 to 60) in the file **"main.py"** and change accordingly:

   -  Board and chip names, e.g. for AD5760, the change the **board** variable to **"EVAL-AD5760SDZ"** and **chip** to **"AD5760"** without quotes

      -  ACE Installation path
      -  GPIB address of your device
      -  Command to capture data from your multimeter. The script was developed and tested with the `Keysight 3458A Digital Multimeter <https://www.keysight.com/en/pdx-2905513-pn-3458A/digital-multimeter-8-digit?cc=SG&lc=eng>`__. Refer your instrument's manual for the correct command.\

      |image5|

      -  Constants for code range (maximum and minimum), number of codes to jump through and the voltage span according to the reference fed to the DAC.\

      |image6|

-  Run the script by using the command:``python Main.py``
-  After the script finishing capturing data, you should see the results window similar to this:|image7|
-  A spreadsheet will be exported to the home directory that contains all the values captured and plotted.\

|image8|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/other-software/python_installation.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/other-software/go_to_settings.png
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/other-software/ipc_server.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/other-software/line_70.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/other-software/ad5791_code_constants.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/other-software/ad5791_code_range.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/other-software/results.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/other-software/spreadsheet.png
   :width: 600px
