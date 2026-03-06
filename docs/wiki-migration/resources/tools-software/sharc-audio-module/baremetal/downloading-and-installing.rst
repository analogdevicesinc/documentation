Opening the Framework in CCES
=============================

.. image:: https://wiki.analog.com/_media/youtube>GprhlU-IrXQ
   :alt: youtube>GprhlU-IrXQ

After installing the framework, the CCES project will be placed in the following directory: ``C:\Analog Devices\SAM_BareMetal_SDK-Rel2.0.0\framework``.

Rather than opening / editing this project directly, it is recommended to run the :doc:`Bare Metal Example Wizard </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/project-wizard>` for each new example that is planned. This will ensure you always have a clean version of the framework to start with.

Follow the steps below to open the framework in CrossCore Embedded Studio (CCES):

-  From within the CCES IDE click ``File`` -> ``Open Projects from File System``
-  Select the directory where the example wizard created the projects or the location where the framework exists. If using the example wizard this will be in the workspace that was chosen.
-  Ensure that the three ``sam_baremetal_framwork_coreN`` projects are selected and then click ``Finish`` to open them into your workspace.

   -


   |image1|

-  After completing this operation, you should see three folders appear in the Project Explorer. Each project corresponds to each of the three cores on the ADSP-SC589. Core 0 is the ARM core. Cores 1 and 2 are the two SHARC cores. By default, the project is configured to pass audio from the 1/8" audio input jack to the 1/8" audio output jack. Build the project and create a debug profile for the JTAG emulator you’re using (ICE1000 or ICE2000). From here, you’ll be able to download and run the project on the ADSP-SC589.

.. note::

   JP1 on the SHARC Audio Module should be removed (disconnected) when using an emulator to connect to the board


-  For more information on connecting an emulator, see the :adi:`ICE-1000/ICE-2000 Emulator User's Guide <media/en/dsp-documentation/evaluation-kit-manuals/ICE_emu_1000_2000_rev_manual.pdf>`.
-  For more information on setting up the debug profile, see :adi:`Debugging on a Hardware Target with CCES <en/education/education-library/videos/1831703659001.html>`

.. note::

   The default CCES license provided with the SHARC Audio Module SDK is not a full CCES license; it only enables debug sessions for ICE-1000 emulators.


-  There are three LEDs on the SHARC Audio Module board: ``LED10``, ``LED11`` and ``LED12``. Each core toggles an LED once per second if it is running properly.

   -  ``LED10`` - ARM core begins toggling this once the system has been set up
   -  ``LED11`` - SHARC Core 1 begins toggling this LED once it has begun processing audio
   -  ``LED12`` - SHARC Core 2 begins toggling this LED once it has begun processing audio

You can elect to have one or both cores process audio. When using just one core to process audio, ``LED12`` will not strobe.

If the LEDs are strobing rapidly, it has encountered an initialization error. Halt the processor and you’ll find the function that raised the error in the call stack.

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#project-wizard
   :alt: Bare Metal Project Wizard#.|Bare Metal Framework#configuring-cces|Configuring CCES

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/bm-cces-open-framework.gif
   :width: 600px
