Bare Metal Project Wizard
=========================

The SHARC Audio Module Bare Metal Project wizard allows you to create a new project configuration for your SHARC Audio Module.

.. image:: https://wiki.analog.com/_media/youtube>GprhlU-IrXQ
   :alt: youtube>GprhlU-IrXQ

To begin, open the wizard by selecting **File → New → SHARC Audio Module Bare Metal Project** from the pull-down menu. The **General Project Information** page will appear. This is where a name is given to the new project. Then click Next.

.. important::

   If the Bare Metal Framework Wizard does not currently show in CCES under **File → New → SHARC Audio Module Bare Metal Project** does not show, try clicking **File → New → Other** and it should show under the C/C++ tab. This is normally a result of installing a new version of CCES after the Bare Metal Framework has been installed.


General Project Information Page
--------------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/bm_wizard_start.gif
   :width: 600px

Now the **Expansion Fin Selection** page will appear. Here is where you can select any expansion Fins connected to your SHARC Audio Module through the expansion interface on the bottom of the board. Then click Next.

Expansion Fin Selection Page
----------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/expansion_fin_selection.png
   :width: 600px

Next the **A2B Module Selection** page will appear. Select the A2B module that you have connected to your SHARC Audio Module through the A2B bus. Once the A2B module is selected, 1 A2B configuration should be chosen so that audio can be transmitted and received properly over the A2B bus. Then click Next.

.. tip::

   If multiple A2B modules are connected users should review :doc:`Using pre-configured topology files in the baremetal framework </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/preconfigured-a2b-topology>` since the wizard is only meant for simple A2B configurations.


A2B Module Selection Page
-------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/a2b_module_selection.png
   :width: 600px

If an Audio Project Fin is present, the **Faust Support** window will appear. If using Faust within this particular example select whether Faust will be running on 1 or both SHARC cores.

Faust Support Page
------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust_support.png
   :width: 600px

The **Audio Parameters** page will appear allowing the configuring of certain audio parameters. Here the audio block size and sample rate can be selected as well as if audio processing with use both SHARC cores, and then click Finish.

Audio Parameters Page
---------------------

-  **Audio block size** - A smaller audio block size will reduce the audio latency through the framework but it also slightly decreases the processing efficiency. A larger block size, on the other hand increases the audio latency while also increasing processing efficiency. Generally, a block size of 16 or 32 is a good compromise.
-  **Audio sample rate** - The audio sample rate is number of audio samples present in a second of audio. As sample rate increases so too does the maximum frequency we can capture (Nyquests theorem). However, higher sample rates also reduce the number of processor cycles available to process each sample. Generally, a sample rate of 44.1kHz or 48kHz is a good compromise.
-  **Use both cores to process audio** - The framework can use either one core or both cores to process audio. When using both cores, audio is first processed on core 1 and then it is passed to core 2. Using both cores effectively doubles the amount of processing power available. However, it also increases the audio latency. There's a good discussion on the wiki about the different latencies in single core and dual core mode.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/audio_parameters.png
   :width: 600px

The new project will be created for all 3 cores of the ADSP-SC589 processor within CrossCore Embedded Studio.

--------------

`Bare Metal Framework#.|Bare Metal Framework#downloading-and-installing|Opening the Framework in CCES <https://wiki.analog.com/_media/navigation SHARC Audio Module#.>`_
