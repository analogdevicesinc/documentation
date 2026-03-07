Audio Signal Router
===================

:doc:`Click here to return to the Mixers/Splitters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/mixerssplitters>`

--------------

The Audio Signal Routers cell includes 2 different versions.

-  Audio Signal Router
-  Audio Signal Router External Index Selectable

.. _audio-signal-router-1:

Audio Signal Router
-------------------

|image1| Audio Signal router mixes M different inputs to N different outputs with various gains. The number of input and output pins are configurable. |image2|

This module supports multiple mixer configurations. Each mixer configuration has gains for all the inputs and outputs. A separate gain is available for each of input output combination also. All the gains has a corresponding mute control to quickly mute the particular gain. The current Tab selected (Mix #) in the mixer window is downloaded to the target and used for mixing.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/audiosignalrouterform.png
   :align: center

The following equations show the calculation of the output for given sample mixer table.

==================== ===== ===================== =====================
\                          <fc #0000FF>Out0</fc> <fc #0000FF>Out1</fc>
\                          *Og0*                 *Og1*
<fc #008000>In0</fc> *Ig0* G00                   G01
<fc #008000>In1</fc> *Ig1* G10                   G11
==================== ===== ===================== =====================

-  <fc #0000FF>Out0</fc> = *Og0* \* ( G00 \* *Ig0* \* <fc #008000>In0</fc> + G10 \* *Ig1* \* <fc #008000>In1</fc>)
-  <fc #0000FF>Out1</fc> = *Og1* \* ( G01 \* *Ig0* \* <fc #008000>In0</fc> + G11 \* *Ig1* \* <fc #008000>In1</fc>)

If the input/output channels are more than 16, then the mixer window is split for 16 input/output channels to improve GUI performance.


|image3|

Labels for each of the input/output channels can be edited. This updated channel name will pear on the each of the Pin's tooltip as show below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/channel_customization_.jpg
   :align: center

Audio Signal Router External Index Selectable
---------------------------------------------

This functionality of this module is same as audio signal router except that the current mixer (Mix #) is selected through an external input as shown below. The control pin expects the input in (32.0) format for ADAU145x processors and (28.0) format for other Sigma DSPs.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/audiosignalrouterext.png
   :align: center

Audio Signal Router Script support
----------------------------------

User can able to access this module from script.

The following sample code shows how to read parameters from a file using Sigma studio script.

.. code:: csharp

   // #LANGUAGE# C#
   // Get Cell object

   object obj = ss.GetCellObject("Router1");
   System.Collections.ArrayList arr = null;
   System.Reflection.MethodInfo[] memberInfos = ss.ObjectGetMethods(obj);
   /*foreach (System.Reflection.MethodInfo memberInfo in memberInfos) 
   {   
      ss.PrintLine(memberInfo.Name);
   }*/

   //OPEN the SETTINGWINDOW
   System.Reflection.MethodInfo methodInfo = ss.ObjectGetMethod(obj, "settingswindowopen");
   ss.PrintLine(methodInfo.Name);
   methodInfo.Invoke(obj, new object[]{});

   //CHANGE the Table INDEX
   //and set the values
   // chage the tabindex count based on need and will get the tabindex value.which is used here.
   //setTabIndex should be 0 to 3.
   for (int idx =0; idx <= 1; idx++)
   {
   System.Reflection.MethodInfo methodInfo1 = ss.ObjectGetMethod(obj, "setTabIndex");
   ss.PrintLine(methodInfo1.Name);
   methodInfo1.Invoke(obj, new object[]{idx,2});
   ss.ObjectSetProperties("setControlValue", "Router1", 0, 0, "InputGain_0" , 6.0);
   ss.ObjectSetProperties("setControlValue", "Router1", 0, 0, "InputGain_10" , 2);
   ss.ObjectSetProperties("setControlValue", "Router1", 0, 0, "InputGain_12" , 3);
   ss.ObjectSetProperties("setControlValue", "Router1", 0, 0, "OutputGain_10" , 0.3);
   ss.ObjectSetProperties("setControlValue", "Router1", 0, 0, "OutputGain_12" , 0.3);
   ss.ObjectSetProperties("setControlValue", "Router1", 0, 0, "OutputGain_9" , 0.3);
   ss.ObjectSetProperties("setControlValue", "Router1", 0, 0, "CrossGain_0_1" , 0.5);
   ss.ObjectSetProperties("setControlValue", "Router1", 0, 0, "CrossGain_0_0" ,0.6);
   }


   //CLOSE the SETTINGWINDOW
   System.Reflection.MethodInfo methodInfo2 = ss.ObjectGetMethod(obj, "settingswindowclose");
   ss.PrintLine(methodInfo2.Name);
   methodInfo2.Invoke(obj, new object[]{});

   // 

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/audiosignalrouter.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/audiosignalroutergrow.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/audiorouter_morethan16.jpg
