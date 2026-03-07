Help and Support
================

Do you need help or have general support questions? This page will help you resolve these.

This page has a quickstart troubleshooting approach that goes over some very general questions and common pitfalls, but if you have a specific issue which requires more information or detail please contact us through EngineerZone or Email. (links can be found further down on the page where to direct specific questions)

What to do When Things Go Wrong
-------------------------------

There are many things that can go wrong with an ecosystem this complex, but if you are having issues getting the board or software working, here are a few simple things you can try before contacting Analog Devices.

-  Check the Power on ADICUP3029

   -  Do you have the USB cable plugged in? What about the DC power jack? Is switch (S5) in the "Wall/USB" position?
   -  If you are using batteries, is the switch (S5) in the "BATT" position

      -  Try replacing your batteries, and see if the board powers up

-  Check the Power on EVAL-AD5940xxxx

   -  Ensure the EVAL-AD5940xxx is connected to Arduino UNO connectors on ADICUP3029
   -  Ensure JP1 and JP2 supply jumpers are in position A to power the board from the ADICUP3029.

-  Program the ADuCM3029

   -  Sometimes a flashed program doesn't run properly or can make it difficult to run the debugger.
   -  The first thing to try in this case, is to :doc:`drag and drop </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/adicup3029_hw_drivers>` a known good .HEX or .BIN program into flash.(something with quick visible indicators works best)
   -  If drag and drop is not working, it may be necessary to erase the flash. To do so:

      -  Download and install the CrossCore Serial Flash Programmer from here: :adi:`crosscore-serial-flash-programmer.html#dsp-overview <en/design-center/processors-and-dsp/evaluation-and-development-software/crosscore-serial-flash-programmer.html#dsp-overview>`.
      -  Make sure that the USB is selected on the three way UART switch (S2).
      -  Power cycle the ADICUP3029 board while holding down the boot switch (S3)
      -  Select the mbed serial COM port in the CrossCore Serial Flash Programmer, and erase the flash.
      -  Then try :doc:`dragging and dropping </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/adicup3029_hw_drivers>` a .HEX or .BIN file into flash

   -  If the mass erase didn't work, and you are trying to drag and drop a large .BIN file on EVAL-ADICUP3029 Rev B hardware, it's possible that the mbed interface file needs to be updated to support your application.

      -  Please visit the :doc:`Maintenance Drive details </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/adicup3029_hw_drivers>` page in order to put the board in update mode.
      -  Once you are in "maintenance mode" you should drag and drop the latest interface file onto your maintenance drive. That file can be downloaded at the bottom of :doc:`Maintenance Drive Page </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/adicup3029_hw_drivers>`.

-  Not receiving/transmitting data to the UART

   -  Make sure that the UART switch (S2) is positioned in the correct destination to transmit/receive UART data.

-  I'm trying to program/debug, but I'm getting errors.

   -  Check the drives attached to your computer, do you see a mass storage device called **DAPLINK** or **Maintenance**? If you see the Maintenance drive and your USB is plugged in, then likely the ADuCM3029 isn't being powered, which means the power switch (S5) is likely in the "BATT" position. Flip it "WALL/USB" and unplug/reconnect your USB cable to your computer, and try to programming again.

This is just a brief self-help guide to troubleshooting common issues. If you have other questions that need answering please direct those requests to the locations outlined below.

Hardware, Software, and Documentation Questions
-----------------------------------------------

If you have any questions regarding the ADICUP3029 base board or are experiencing any problems using the **AD5940 SDK** or issues following any of the **documentation** feel free to ask us a question.

-  :ez:`ADuCM3029 support community <community/analog-microcontrollers/aducm302x>` for questions about:

   -  ADICUP3029 hardware
   -  ADuCM3029 silicon
   -  ADICUP3029 documentation

-  :ez:`AD5940 Support Community <data_converters/precision_adcs/w/documents/14012/ad5940-faqs>` for questions about:

   -  AD5940 silicon
   -  AD5940 documentation
   -  AD5940 evaluation boards

When asking a question please take the time to give a detailed description of your problem. If you are experiencing a problem please state the steps you have executed, the result you expected you would get and the result you actually got. By doing so you enable us to provide you precise and detailed answers in a timely manner.

.. tip::

   Before asking questions please take the time to check if somebody else already asked the same question. You might just find your question already answered.


// End of Document //
