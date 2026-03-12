Using Keil IDE with EV-COG-AD3029WZ
===================================

<note > **There are no seperate toolchain,On-Board Peripheral Drivers & Software for EV-COG-AD3029WZ, the toolchain,On-Board Peripheral Drivers & Software for EV-COG-AD3029LZ works with EV-COG-AD3029WZ.The user needs to change only the pin muxing based on the application.For help regarding pinmapping refer to the Hardware Details section.** 

This will be a paragraph talk about why you might want to use Keil with the EV-COG-AD3029LZ.

How to use EV-COG-AD3029WZ with Keil
------------------------------------

In order to use EV-COG-AD3029WZ board with Keil, you will need to replicate the following steps.

-  Install mBed windows serial driver from

   -  https://developer.mbed.org/handbook/Windows-serial-configuration

-  Open any example-workspace and project from the ADuCM3029 BSP(board support package). I used the SysTick example in the below images
-  In the Keil toolbar select **Project** → **Options** → **Debug**, and select the “CMSIS DAP” option

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/tools/keildebug.png
   :align: center
   :width: 500px

-  Under the CMSIS DAP Settings, select the SW option

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/tools/keilcmsisdap.png
   :align: center
   :width: 500px

-  Push Crtl+F5 or in the Keil toolbar select **Debug** → **Start/Stop Debug Session**
-  That’s it – You are ready to go.

*End of Document*

:doc:`Back </wiki-migration/resources/eval/user-guides/ev-cog-ad3029wz>`
