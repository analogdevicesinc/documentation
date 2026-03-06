MIDI Virtual Analog Synth (Core1) /Effects (Core 2)
===================================================

For this final example the full virtual analog synth is run on Core1 and the effects chain is run on Core 2.

.. important::

   Part of this example will run on core 2 so be sure to set the following #define in ``audio_system_config.h`` or select that Faust will run on both cores 1 and 2 when using the :doc:`bare metal project wizard </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/project-wizard>`.

   
   .. code:: c
   
      #define USE_FAUST_ALGORITHM_CORE2 TRUE
   


The Faust Code
--------------

Virtual Analog Synth (Core 1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multiple `examples <https://github.com/moforte/sam-faust/tree/master/faust-examples>`__ for the SHARC audio module have been put together and hosted on github. In order to successfully run this example, please clone this repository.

For this particular example workflow, we will be looking at the virtualAnalog example from the git repository.


|image1|

-  Open the Faust `online editor <https://faust.grame.fr/editor>`__.
-  You can copy the contents into the editor 2 different ways

   -  Name the \*.dsp file virtualAnalogForBrowser.dsp. and copy the contents of virtualAnalogForBrowser.dsp into the online editor.

      -  Drag the virtualAnalogForBrowser.dsp file into the tile bar of the editor

-  Compile and run the Faust program using the |image2| button

.. note::

   Note this may take about a minute to compile and run


Effects Chain (Core 2)
~~~~~~~~~~~~~~~~~~~~~~

Multiple `examples <https://github.com/moforte/sam-faust/tree/master/faust-examples>`__ for the SHARC audio module have been put together and hosted on github. In order to successfully run this example, please clone this repository.

For this particular example workflow, we will be looking at the virtualAnalog example from the git repository.


|image3|

-  Open the Faust `online editor <https://faust.grame.fr/editor>`__.
-  You can copy the contents into the editor 2 different ways

   -  Name the \*.dsp file virtualAnalogWithEffectsForBrowser.dsp. and copy the contents of virtualAnalogWithEffectsForBrowser.dsp into the online editor.

      -  Drag the virtualAnalogWithEffectsForBrowser.dsp file into the tile bar of the editor

-  Compile and run the Faust program using the |image4| button

.. note::

   Note this may take about a minute to compile and run


Looking at the Block Diagram
----------------------------

Virtual Analog Synth
~~~~~~~~~~~~~~~~~~~~

The block diagram button |image5| can be used to generate a hierarchical block diagram for an algorithm. This block diagram is hierarchical. Here are a few of the hierarchical levels:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust//faust19.png
   :alt: /faust19.png
   :width: 576px
   :height: 189px

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust//faust20.png
   :alt: /faust20.png
   :width: 312px
   :height: 166px

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust//faust21.png
   :alt: /faust21.png
   :width: 576px
   :height: 112px

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust//faust22.png
   :alt: /faust22.png
   :width: 572px
   :height: 173px

Effects Chain
~~~~~~~~~~~~~

The block diagram button |image6| can be used to generate a hierarchical block diagram for an algorithm. This block diagram is hierarchical. Here are a few of the hierarchical levels:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust//faust26.png
   :alt: /faust26.png
   :width: 574px
   :height: 124px

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust//faust27.png
   :alt: /faust27.png
   :width: 574px
   :height: 208px

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust//faust28.png
   :alt: /faust28.png
   :width: 576px
   :height: 206px

Creating Files for use with the Baremetal Framework
---------------------------------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/effects2.gif
   :width: 600px

-  Click the ``Export/compile to a specific platform`` button


|image7|

-  In the first dropdown box, choose ``sam``
-  In the second dropdown box, choose ``sam-source-poly-1``\ (core 1) or ``sam-source-midi``\ (core 2) and then Export:

.. note::

   \ **faust2sam** will generate the following three C++ source files, which is the algorithm.

   
   -  ``fast_pow2.h``
   -  ``samFaustDSP.cpp``
   -  ``samFaustDSP.h``
   


-  Click on the QR code that shows to download the files
-  These 3 source files can be copied to the Faust directory in the CCES framework. The framework can then be compiled and downloaded to the SHARC Audio Module.

.. important::

   The files created from the **Virtual Analog Synth** project should be placed in the faust folder for **Core1** and the ones from the **Effects Chain** should be placed in the faust folder for **Core2**\


-  See :doc:`Faust with the CCES Bare Metal Framework </wiki-migration/resources/tools-software/sharc-audio-module/faust>` for more information

MIDI Assignments for the Virtual Analog Algorithm
-------------------------------------------------

+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| **Function**                | **MIDI CC** | **Module**          | **Type** | **Notes**                                       |
+=============================+=============+=====================+==========+=================================================+
| Tune                        | 47          | 1 - Controllers     | knob     | Master tuning                                   |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| Glide                       | 5           | 1 - Controllers     | knob     | Portamento time                                 |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| Modulation Mix              | 48          | 1 - Controllers     | knob     | Modulation mix between OSC3 and Noise           |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
|                             |             |                     |          |                                                 |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| Oscillator Modulation       | 22          | 2 - Oscillator Bank | switch   | Enable modulation control of OSC frequencies    |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| OSC 1 Range                 | 23          | 2 - Oscillator Bank | knob     | OSC 1 range                                     |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| OSC 1 Detune                | 24          | 2 - Oscillator Bank | knob     | OSC 1 detuning                                  |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| OSC 1 Waveform              | 25          | 2 - Oscillator Bank | knob     | OSC 1 waveform shape                            |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| OSC 2 Range                 | 28          | 2 - Oscillator Bank | knob     | OSC 2 range                                     |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| OSC 2 Detune                | 29          | 2 - Oscillator Bank | knob     | OSC 2 detuning                                  |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| OSC 2 Waveform              | 30          | 2 - Oscillator Bank | knob     | OSC 2 waveform shape                            |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| OSC 3 Range                 | 33          | 2 - Oscillator Bank | knob     | OSC 3 range                                     |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| OSC 3 Detune                | 34          | 2 - Oscillator Bank | knob     | OSC 3 detuning                                  |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| OSC 3 Waveform              | 35          | 2 - Oscillator Bank | knob     | OSC 3 waveform shape                            |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| OSC 3 Control               | 9           | 2 - Oscillator Bank | switch   | OSC 3 as a control signal or as an audio source |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
|                             |             |                     |          |                                                 |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| OSC 1 Amp                   | 26          | 3 - Mixer           | knob     | OSC 1 gain                                      |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| Osc1 mixer switch           | 12          | 3 - Mixer           | switch   | OSC 1 enable                                    |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| OSC 2 Amp                   | 31          | 3 - Mixer           | knob     | OSC 2 gain                                      |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| Osc2 mixer switch           | 14          | 3 - Mixer           | switch   | OSC 2 enable                                    |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| OSC3 Amp                    | 36          | 3 - Mixer           | knob     | OSC 3 gain                                      |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| OSC3 mixer switch           | 17          | 3 - Mixer           | switch   | OSC 3 enable                                    |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| External Input amp          | 27          | 3 - Mixer           | knob     | Extrenal input gain                             |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| External Input mixer switch | 13          | 3 - Mixer           | switch   | External input enable                           |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| Noise Amp                   | 32          | 3 - Mixer           | knob     | Noise gain                                      |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| Noise mixer switch          | 15          | 3 - Mixer           | switch   | Noise Enable                                    |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+
| White/pink toggle           | 16          | 3 - Mixer           | switch   | Noise pink/white                                |
+-----------------------------+-------------+---------------------+----------+-------------------------------------------------+

+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
| Filter Modulation Enable | 19         | 4 - Filter              | switch | Enable modulation control of the filter cutoff frequency |
+==========================+============+=========================+========+==========================================================+
| Keyboard Range           | 38         | 4 - Filter              | knob   | Add keyboard control of the filter cutoff frequency      |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
| Cutoff Frequency         | 74         | 4 - Filter              | knob   | Filter cutoff frequency                                  |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
| Emphasis                 | 37         | 4 - Filter              | knob   | Filter Resonance (Q)                                     |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
| Amount of Contour        | 39         | 4 - Filter              | knob   | Amount of envelope generator                             |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
| Attack Time              | 40         | 4 - Filter              | knob   | VCF envelope generator attack time                       |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
| Decay Time               | 41         | 4 - Filter              | knob   | VCF envelope generator decay time                        |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
| Sustain Level            | 42         | 4 - Filter              | knob   | VCF envelope generator sustain level                     |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
|                          |            |                         |        |                                                          |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
| Attack Time              | 43         | 5 - Loudness Contour    | knob   | VCA envelope generator attack time                       |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
| Decay Time               | 44         | 5 - Loudness Contour    | knob   | VCA envelope generator decay time                        |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
| Sustain Level            | 45         | 5 - Loudness Contour    | knob   | VCA envelope generator sustain level                     |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
|                          |            |                         |        |                                                          |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
| Decay                    | 20         | 6 - Keyboard            | switch | Enables using the decay stage as a release stage         |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
| Glide                    | 65         | 6 - Keyboard            | switch | Enable portamento                                        |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
| Pitch Wheel              | pitchWheel | 6 - Keyboard            | knob   | Pitch Wheel                                              |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
| Mod Wheel                | 1          | 6 - Keyboard            | knob   | Modulation Wheel control                                 |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
| Sustain                  | 64         | midi sustain foot pedal | switch | Note sustain, preempts the VCF/VCA release stage         |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
|                          |            |                         |        |                                                          |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+
| Master Volume            | 7          | 5 - Output              | knob   | Master volume                                            |
+--------------------------+------------+-------------------------+--------+----------------------------------------------------------+

MIDI Assignments for the Effects Chain Algorithm
------------------------------------------------

================ =========== ========== ========
**Function**     **MIDI CC** **Module** **Type**
================ =========== ========== ========
                                         
Invert           49          Flanger    knob
Enable           102         Flanger    switch
Delay            50          Flanger    knob
Rate             51          Flanger    knob
Depth            52          Flanger    knob
Feedback         53          Flanger    knob
Wave Shape       54          Flanger    knob
                                         
Delay            55          Chorus     knob
Enable           103         Chorus     switch
Rate             56          Chorus     knob
Depth            57          Chorus     knob
Deviation        58          Chorus     knob
                                         
enable           105         Echo       switch
Delay Portamento 60          Echo       knob
Delay            61          Echo       knob
Warp             62          Echo       knob
Feedback         2           Echo       knob
Amp              75          Echo       knob
Feedback sm?     76          Echo       knob
                                         
Damp             3           Reverb     knob
Enable           104         Reverb     switch
Room Size        4           Reverb     knob
Wet Dry          79          Reverb     knob
================ =========== ========== ========

The Virtual Analog/Effects Chain TouchOSC UI
--------------------------------------------

TouchOSC is a mobile app that can be used to create arbitrary GUIs that send MIDI values. TouchOSC is available for both iOS and Android. A TouchOSC configuration is provided for the Virtual Analog and Effects chain algorithms (virtualAnalog.touchOSC)

The Virtual Analog Page:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust//faust29.png
   :alt: /faust29.png
   :width: 574px
   :height: 430px

The Effects Chain Page:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust//faust30.png
   :alt: /faust30.png
   :width: 574px
   :height: 430px

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#ex-work-saw
   :alt: MIDI Sawtooth Synth#.|Faust and the SHARC Audio Module#..|Back to main SHARC Audio Module

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/virtualanalog1.gif
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/play_button.png
   :width: 50px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/effects1.gif
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/play_button.png
   :width: 50px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/diagram_button.png
   :width: 50px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/diagram_button.png
   :width: 50px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/export_button.png
   :width: 50px
