:doc:`Click here to return to 'SigmaStudio Scripting' page. </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/scripting>`

Sample Scripts for IScripted Interface
======================================

This page shows few sample script of how to use the :doc:`Iscripted interface APIs </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/scripting/iscripted>` in SigmaStudio scripting window.

Control Updates
---------------

The script below can be used to update various parameters in the schematic shown.


|image1|

.. code:: csharp

   // #LANGUAGE# C#
   //------------------Linear Gain ----------------
   //set gain of 'Gain1' module to 0.25
   ss.ObjectSetProperties("setControlValue", "Gain1", 0, 0, "Gain", 0.25);
   //set gain of 'Gain1_2' module to 0.15
   ss.ObjectSetProperties("setControlValue", "Gain1_2", 0, 0, "Gain", 0.15);


   //-------------------Delay ----------------------
   // Set current delay to 10 in 'Delay1'
   ss.ObjectSetProperties("setControlValue", "Delay1", 0, 0, "DelayValue", 10);
   // Set current delay to 10 in 'Delay2'
   ss.ObjectSetProperties("setControlValue", "Delay1_2", 0, 0, "DelayValue", 20);
   //------------------ Param EQ ----
   // Update frequency of first filter in 'Param EQ1 to 50
   ss.ObjectSetProperties("setControlValue", "Param EQ1", 0, 0, "Frequency10", 50);
   // Update frequency of second filter in 'Param EQ1 to 100
   ss.ObjectSetProperties("setControlValue", "Param EQ1", 0, 0, "Frequency11", 100);
   // Update frequency of 3rd filter in 'Param EQ1 to 200
   ss.ObjectSetProperties("setControlValue", "Param EQ1", 0, 0, "Frequency12", 200);


   // Update gain of first filter in 'Param EQ1 to 0.15
   ss.ObjectSetProperties("setControlValue", "Param EQ1", 0, 0, "Gain10", 0.15);
   // Update gain of second filter in 'Param EQ1 to 0.25
   ss.ObjectSetProperties("setControlValue", "Param EQ1", 0, 0, "Gain11", 0.25);
   // Update gain of 3rd filter in 'Param EQ1 to 0.75
   ss.ObjectSetProperties("setControlValue", "Param EQ1", 0, 0, "Gain12", 0.75);

   // As controls in pramaEQ is inside an another form, the following APIs to be called to download the changed parameters to the target. 
   object paramEQ1Object = ss.GetCellObject("Param EQ1");
   ss.ObjectGetMethod(paramEQ1Object, "PackDataAllControls").Invoke(paramEQ1Object, new object[]{});

Get Current Growth
------------------

The script below can be used to get current growth of modules in the schematic shown.


|image2|

.. code:: csharp

   // #LANGUAGE# C#
   //------------------ISIB----------------
   //Get Current Growth of 'ISIB1'
   object[] output;
   ss.ObjectGetProperties("getCurrentGrowth", "ISIB1", out output, 0);
   ss.PrintLine(output[0].ToString());
   ss.PrintLine(output[1].ToString());

   //------------------General Filter----------------
   //Get Current Growth of 'Gen Filter1'
   ss.ObjectGetProperties("getCurrentGrowth", "Gen Filter1", out output, 0);
   ss.PrintLine(output[0].ToString());
   ss.PrintLine(output[1].ToString());

   //------------------Input----------------
   //Get Current Growth of 'Input1'
   ss.ObjectGetProperties("getCurrentGrowth", "Input1", out output, 0);
   ss.PrintLine(output[0].ToString());
   ss.PrintLine(output[1].ToString());

   //------------------Output----------------
   //Get Current Growth of 'Output1'
   ss.ObjectGetProperties("getCurrentGrowth", "Output1", out output, 0);
   ss.PrintLine(output[0].ToString());
   ss.PrintLine(output[1].ToString());

ICRegisterWrite And ICRegisterRead
----------------------------------

The script below can be used to write and read the register without 'ICName' as a parameter.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/registerreadandwritewithouticname.png
   :align: center

.. code:: csharp

   // #LANGUAGE# C#
   // --------------- FIR Filter ---------------
   byte[] _tableValues = new byte[40] {0x00,0x00,0x00,0x02, 0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x02,
                                       0x00,0x00,0x00,0x02, 0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x02,
                                       0x00,0x00,0x00,0x02, 0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x02,
                                       0x00,0x00,0x00,0x03};
   byte[] readValues;    

   // ---------- ICRegisterWrite API ---------                               
   ss.ICRegisterWrite( 40,_tableValues, 0, 112 ,0x001B, 2, 4, 0, 0);

   // ---------- ICRegisterRead API ----------
   ss.ICRegisterRead( 40, out readValues, 0, 112 ,0x001B, 2, 4, 0, 0);

   // ---------- for loop for read values to print ---------- 
   for(int i = 0; i < readValues.Length; i ++)
   {
   // Print the values byte by byte
   ss.PrintLine(readValues[i].ToString()); 
   }                                

.. code:: csharp

   // #LANGUAGE# C#
   // --------------- FIR Filter ---------------
   byte[] _tableValues = new byte[40] {0x00,0x00,0x00,0x02, 0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x02,
                                       0x00,0x00,0x00,0x02, 0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x02,
                                       0x00,0x00,0x00,0x02, 0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x02,
                                       0x00,0x00,0x00,0x03};
   byte[] readValues;    

   // ---------- ICRegisterWrite API ---------                               
   ss.ICRegisterWrite( 40,_tableValues, 1, 0 ,0x0014, 2, 4, 0, 0);

   // ---------- ICRegisterRead API ----------
   ss.ICRegisterRead( 40, out readValues, 1, 0 ,0x0014, 2, 4, 0, 0);

   // ---------- for loop for read values to print ---------- 
   for(int i = 0; i < readValues.Length; i ++)
   {
   // Print the values byte by byte
   ss.PrintLine(readValues[i].ToString()); 
   }                                

Test the NxM Mixer (Linear)
---------------------------

FOllowing script creates a schematic for ADAU1467 with NxM mixer and tests its functionality for a given input/output configuration.

.. code:: csharp

   // #LANGUAGE# C#
   // Modify the below variables to create test NxM mixer for the particular input output configuration.
   int inputs = 8;
   int outputs = 4; 

   //*********Local Vars*************//
   double GainInc = 0.001;
   double DCInc = 0.1;
   double[] InputDCValues = new double[inputs];
   double[] OutputReadBackValues = new double[outputs];
   object[] DCModuleObjects = new object[inputs];
   object[] RBModuleObjects = new object[outputs];
   double[,] GainValues = new double[inputs, outputs];
   double[] ActualResults = new double[outputs];
   double[] ExpectedResults = new double[outputs];
   HResult rest;
   ss.EnableLoggingMode(true);
   // Create Input Vectors. 
   ss.ProjectNew();
   Object IcObject = ss.ObjectInsert("ADAU1467", 300, 100);
   Object USBiObject = ss.ObjectInsert("USBi", 50, 100);
   rest =ss.ObjectConnect("USB Interface", 0, "IC 1", 0);
   int X = 300; 
   int Y = 100; 

   // Add cell and algorithm 
   object MixerCellObject = ss.ObjectInsert("NxM Mixer (Linear)", X, Y);
   rest = ss.ObjectSetProperties("addAlgorithm", MixerCellObject, "IC 1", "NxM Mixer Slew");
   ss.PrintLine("Mixer Module Added");

   // growth input and output
   rest = ss.ObjectSetProperties("growAlgorithm", MixerCellObject, 0, inputs - 2, 0); // input growth
   rest = ss.ObjectSetProperties("growAlgorithm", MixerCellObject, 0, outputs - 1, 1); // output growth
   ss.PrintLine("Mixer Module Grown");

   // Set gains for test
   int index = 1;
   for (int i = 0; i < inputs; i++)
   {
       for (int j = 0; j < outputs; j++)
       {
           GainValues[i, j] = index++ * GainInc;
           rest = ss.ObjectSetProperties("setControlValue","NxM Linear1", j, i , "Gain" + j +"_" + i, GainValues[i, j]);
       }
   }

   // Add DC for the inputs
   for (int i = 0; i < inputs; i++)
   {
       object DCCellObject = ss.ObjectInsert("DC Input Entry", X - 100, Y + i * 100);  
       rest =ss.ObjectConnect(DCCellObject, 0, MixerCellObject, i);
       //ss.PrintLine("DC Module " + i + " Added");
       DCModuleObjects[i] = DCCellObject;
       InputDCValues[i] = (i + 1) * DCInc; 
       rest = ss.ObjectSetProperties("setControlValue", DCCellObject, 0, 0 , "DC", InputDCValues[i]);
   }

   // Add Readback for the outputs
   for (int i = 0; i < outputs; i++)
   {
       object RBCellObject = ss.ObjectInsert("DSP Readback", X + 100, Y + i * 100);    
       rest =ss.ObjectConnect(MixerCellObject, i, RBCellObject, 0);
       //ss.PrintLine("ReadBack Module " + i + " Added");
       RBModuleObjects[i] = RBCellObject;
   }

   // Download
   ss.ProjectLinkCompileDownload();
   System.Threading.Thread.Sleep(3000);

   ss.PrintLine("*****************************************");
   bool isFailed = false;
   for (int outIndx = 0; outIndx < outputs; outIndx++)
   {
       // Find Address of readback params
       string[] names;
       int[] addresses;
       ss.ICGetParamNamesAndAddresses("IC 1", RBModuleObjects[outIndx], out names, out addresses);
       int RBModuleAddresse = addresses[0];

       // Calculate Expected result and compare with Actual Result.
       ExpectedResults[outIndx] = 0; 
       for (int inIndx = 0; inIndx < inputs; inIndx++)
       {
           ExpectedResults[outIndx] += GainValues[inIndx, outIndx] * InputDCValues[inIndx];
       }
       
       // Read Actual Result
       float valRead;
       ss.ICParameterRead("IC 1", RBModuleAddresse, 8, 24, out valRead);
       ActualResults[outIndx] = valRead;
       double error = System.Math.Abs(ExpectedResults[outIndx] - ActualResults[outIndx]);
       ss.PrintLine(System.String.Format("Out{0}: Expected = {1:0.00000000000000f}  Actual = {2:0.00000000000000f} Error = {3:0.00000000000000f}", outIndx, ExpectedResults[outIndx], ActualResults[outIndx],error ));
       if (error > 0.00001)
       {
           isFailed = true;
       }
   }
   ss.PrintLine("*****************************************");
   if (isFailed)
   {
       ss.PrintLine("Test failed");
   }
   else
   {
       ss.PrintLine("Test Pass");
   }

Control Updates for AutoEQ
--------------------------

The script below can be used to automate Auto EQ module.

.. code:: csharp

   // #LANGUAGE# C#

   ss.ObjectSetProperties("setControlValue", "Auto EQ1", 0, 0, "RespType_0", "Impulse");
   ss.ObjectSetProperties("setControlValue", "Auto EQ1", 0, 0, "RespType_1", "Impulse");
   ss.ObjectSetProperties("setControlValue", "Auto EQ1", 0, 0, "RespType_2", "Impulse");
   ss.ObjectSetProperties("setControlValue", "Auto EQ1", 0, 0, "ResponseFile_0", "C:\\SSExampleSchematics\\S300\\AutoEQ\\Woofer.txt");
   ss.ObjectSetProperties("setControlValue", "Auto EQ1", 0, 0, "ResponseFile_1", "C:\\SSExampleSchematics\\S300\\AutoEQ\\Mid 1.txt");
   ss.ObjectSetProperties("setControlValue", "Auto EQ1", 0, 0, "ResponseFile_2", "C:\\SSExampleSchematics\\S300\\AutoEQ\\Tweeter.txt");

   ss.ObjectSetProperties("setControlValue", "Auto EQ1", 0, 0, "TargetResponseCsv_0", "C:\\SSExampleSchematics\\S300\\AutoEQ\\TargetResponse.csv");

   ss.ObjectSetProperties("setControlValue", "Auto EQ1", 0, 0, "DesignAll", true);

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/script2.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/getcurrentgrowth42.png
