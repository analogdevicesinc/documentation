CheckSum
========

| 
| :doc:`Click here to return to the Basic DSP section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| This module can be used for detecting and transmission error happened while writing the PM, DM0, DM1 data packs from the uC to the SigmaDSP.
| |image1|
| SigmaStudio computes 'Expected' checksum value and displays in the schematic. The SigmaDSP initialization routine computes the actual checksum and stores in the target before the audio processing starts. By clicking the 'read' button, the actual values can be read from the target and displayed in the module. If the circle color is red the computation is still in progress. The green color indicates the computation is completed.

The checksum is calculated for each pack as follows,

::

   initialize the sum to zero
   FOR each word in the pack
       Read each word in the pack      
       Set sum equal to the addition of the each word
   END FOR
   Assign the negative sum to checksum result

| Note:- For DM0 memory checksum is calculated by excluding the stack memory.

Usage
-----

Using SigmaStudio GUI
~~~~~~~~~~~~~~~~~~~~~

-  Drag and drop the module in the schematic.
-  Link Compile Download.
-  Press Read button.
-  If the Circle in the modules is red, press the read until the Circle is green. (If the circle is red, the calculation is not completed)
-  Compare the Expected and the actual value. Both should match for all the 3 memory (DM0, DM1, PM)

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/checksumexample42.png
   :align: center

Using uC
~~~~~~~~

After writing all the download data as per the ADAU145x/ADAU146x download sequence, follow the steps below to verify the DM0, DM1 and PM packs.

-  Calculate the expected checksum for DM0, DM1, PM packs as follows,

.. code:: c

     byte spidata[datalength]; // pack data
     int64 sum = 0;
     int32 checksumresult;
     for(int i = 0; i < datalength/4; i++)
     {
        int data = 0;
        data  =  spidata[4 * i + 3];
        data  = data | (spidata[4 * i + 2] << 8);
        data  = data | (spidata[4 * i + 1] << 16);
        data  = data | (spidata[4 * i] << 24);
        
        sum += data;    
     }  
     checksumresult = -sum;
     

-  Please find the addresses of 'PMCheckSum', 'DM0CheckSum', 'DM1CheckSum' and 'CheckSumCalculationDone' framework variables in the export PARAM.h

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/checksum2.jpg
   :align: center

-  Wait for the 'CheckSumCalculationDone' to become 0x01000000.
-  Read 'PMCheckSum', 'DM0CheckSum' and 'DM1CheckSum'. These values should match the calculated checksums in uC.
-  If the 'CheckSumCalculationDone' is not becoming 0x01000000, the PM pack is not transmitted properly/ the SigmaDSP core is not running.

Supported IC's
--------------

| 1. ADAU145x
| 2. ADAU146x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/checksum.png
