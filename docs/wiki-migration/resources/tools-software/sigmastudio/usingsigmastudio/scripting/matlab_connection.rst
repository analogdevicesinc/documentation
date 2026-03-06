:doc:`Click here to return to 'SigmaStudio Scripting' page. </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/scripting>`

Matlab Connection
=================

| This example script designs an FIR filter with Matlab using following Matlab function:
| h = firpm(N, a*2, b);
| N: the filter order
| Example of a length 31 lowpass filter:
| H = firpm(30, [0 .1 .2 .5]*2, [1 1 0 0]);
| Type help firpm in Matlab command line for more information on this function.
| This scrip can take a Schematic as an input argument along with the FIR address and FirOrder. If the arguments are valid the script will run the filter on SHARC target through SigmaStudio. It is expected that the target is booted with an appropriate script. \\
| =====Hardware and Software Requirement===== All infrastructures required to run SigmaStudio.
| Matlab installation with valid license.
| =====Usage===== matlabConnectionTest.exe schematic_name.dspproj fir Address firOrder
| matlabConnectionTest.exe fir1.dspproj 10 30
| =====FAQ===== Q: How do I get the FIR address?
| You may get it from the capture window or use export to get the address.
| Q: How do I build the application?
| Use the code given below to build the application
| ``// #LANGUAGE# C#
   using System;
   using System.Collections.Generic;
   using System.Linq;
   using System.Text;
   using Analog.SigmaStudioServer;
   
   namespace ConsoleApplication1
   {
     class Program
     {
       class mYSsMatlab
       {
         public SigmaStudioServer sserver;
         public MLApp.MLApp matlab;
         public void Message(string s)
         {
           Console.WriteLine(s);
         }
         public bool runFir(string schematicName, int AddrFirCoef, float[] coef, int N)
         {
           int delayms = 10000;
           bool ret = sserver.SET_LOGGING_MODE(true);
           try 
           {
             ret = sserver.SET_LOGGING_MODE(true);
             if (ret != true)
             {
               Message("Couldn't connect to SigmaStudio, please make sure that the SigmaStudio is running");
               return ret;
             } 
           }
           catch (Exception ex)
           {
             Console.WriteLine("Server Connection failed. exception {0}", ex.Message);
             Message("Couldn't connect to SigmaStudio, please make sure that the SigmaStudio is running");
             return ret;
           }
           sserver.CLOSE_PROJECT();
           ret = sserver.OPEN_PROJECT(schematicName);
           if (ret == false)
           {
             Message("schematic load failed " + schematicName);
             return ret;
           }
           ret = sserver.DELAY_SCRIPT(delayms);
           sserver.DOWNLOAD();
           if (ret == false)
           {
             Message("schematic load failed " + schematicName); return ret;
           }
           sserver.PARAMETER_WRITE_ARRAY_FLOAT("IC 1", AddrFirCoef, N, coef);
           sserver.DELAY_SCRIPT(delayms);
           Message("Test case for : " + "matlabTest");
           return ret;
         }
         public float[] designFir(int N) 
         {
           float[] h = new float[N+1];
           System.Array h_r = new double[N+1];
           System.Array h_i = new double[N+1];
           string returnString;
           int i = 0;
           /* Example of a length 31 lowpass filter: h=firpm(30,[0 .1 .2 .5]*2,[1 1 0 0]); */
           System.Array a = new double[4]; a.SetValue(0, 0); a.SetValue(0.1, 1); a.SetValue(0.2, 2); a.SetValue(0.5, 3);
           System.Array b = new double[4]; b.SetValue(1, 0); b.SetValue(1, 1); b.SetValue(0, 2); b.SetValue(0, 3);
           System.Array z = new double[4]; z.SetValue(0, 0); z.SetValue(0, 1); z.SetValue(0, 2); z.SetValue(0, 3);

           matlab.PutFullMatrix("a", "base", a, z);
           matlab.PutFullMatrix("b", "base", b, z);

           StringBuilder matlabCmdFir = new StringBuilder();

           matlabCmdFir.AppendFormat("h = firpm({0}, a*2, b)", N);
           returnString = matlab.Execute(matlabCmdFir.ToString());
           /* returnString = matlab.Execute("h = firpm(30, a*2, b)"); */

           matlab.GetFullMatrix("h", "base", ref h_r, ref h_i);

           foreach(double c in h_r)h[i++] = (float)Convert.ToDecimal(c);
           return h;
         }
         public mYSsMatlab()
         { 
           matlab = new MLApp.MLApp();
           sserver = new SigmaStudioServer();
         }
       }
       class Class1 
       {
         [STAThread]
         static void Main(string[] args)
         {
           int i = 0;
           int orderFir = 30;
           int addressFir = 30;
           if(args.Length != 3)
           {
             Console.WriteLine(" ERROR in arguments. Usage testMatlab schematic.dspproj firOrder");
             return ;
           }
           try 
       { 
         addressFir = Int32.Parse(args[1]);
       }
           catch
       {
         Console.WriteLine("ERROR : wrong fir Address {0} Exiting ", args[1]); return; 
       }
           try 
       { 
         orderFir = Int32.Parse(args[2]); 
       }
           catch 
       { 
         Console.WriteLine("ERROR : wrong filter order {0}", args[1]); orderFir = 30; 
       }

           Console.WriteLine("Testing FIR coef design with matlab and running with SigmaStudio, schematic used = {0} firAddress = {1} fir Order = {2} please wait...", args[0], orderFir, addressFir);

           mYSsMatlab ssMatLabTest = new mYSsMatlab();

           /* design FIR using matlab */
           float[] h = ssMatLabTest.designFir(orderFir);

           /* print the fir coef */
           Console.Write("coef [{0}]= ", h.Length);
           foreach (double c in h) 
           { 
             Console.Write(" {0}", c); i++; 
           } 
           Console.WriteLine("] ");

           /* run FIR on sharc through SigmaStudio */
           ssMatLabTest.runFir(args[0], addressFir, h, 30);
         } 
       } 
     } 
   }``
