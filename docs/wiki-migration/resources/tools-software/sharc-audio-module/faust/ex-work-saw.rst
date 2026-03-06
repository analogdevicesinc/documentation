MIDI Sawtooth Synth on Core 1
=============================

This third example is a MIDI controlled sawtooth synth on Core 1.

The Faust Code for the MIDI Controlled Sawtooth Synth
-----------------------------------------------------

Here is the Faust code for the MIDI controlled sawtooth synth. Notice the use of the metadata elements:

-  ``freq`` – If a MIDI noteOn event is received it’s MIDI keyNumber is mapped to a frequency.
-  ``bend`` – if a MIDI pitchBend message is received it is mapped to a bend value.
-  ``gain`` – if a MIDI noteOn message is received it’s velocity value is mapped to a gain value which ranges from [0 .. 1.0]
-  ``gate`` – if MIDI noteOn/noteOff messages are received they are mapped to a gate value (0/1)
-  ``[midi:ctrl 1]`` – A Faust control (slider, etc) can be mapped to listen to a MIDI continuous controller.

.. code:: c

   import("stdfaust.lib");


   normMIDI(mv)  = mv/127.0; 
   vol  = normMIDI(hslider("Ctrl Value IN (Ctrl 1) [midi:ctrl 1]", 60, 0, 127, 1)) ;


   f = nentry("freq",200,40,2000,0.01);
   bend = nentry("bend",1,0,10,0.01) : si.polySmooth(t,0.999,1);
   g = nentry("gain",1,0,1,0.01);
   t = button("gate");
   freq = f*bend;
   envelope = t*g*vol : si.smoo;

   process = os.sawtooth(freq)*envelope <: _,_;

Building a Test GUI for the MIDI Controlled Sawtooth Synth
----------------------------------------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/sawtooth1.gif
   :width: 600px

-  Open the Faust `online editor <https://faust.grame.fr/editor>`__.
-  Name the \*.dsp file sawtooth_synth.dsp.
-  Copy the algorithm into the online editor.
-  Compile and run the Faust program using the |image1| button

Looking at the Block Diagram for the MIDI Controlled Sawtooth
-------------------------------------------------------------

The block diagram button |image2| can be used to generate a hierarchical block diagram for an algorithm. This block diagram is hierarchical. Here are a few of the hierarchical levels:

|/faust15.png|\ |/faust16.png|

Creating Files for use with the Baremetal Framework
---------------------------------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/sawtooth2.gif
   :width: 600px

-  Click the ``Export/compile to a specific platform`` button


|image3|

-  In the first dropdown box, choose ``sam``
-  In the second dropdown box, choose ``sam-source-poly-4`` and then ``Export``

.. note::

   \ **faust2sam** will generate the following three C++ source files, which is the algorithm.

   
   -  ``fast_pow2.h``
   -  ``samFaustDSP.cpp``
   -  ``samFaustDSP.h``
   


-  Click on the QR code that shows to download the files
-  These 3 source files can be copied to the Faust directory in the CCES framework. The framework can then be compiled and downloaded to the SHARC Audio Module.
-  See :doc:`Faust with the CCES Bare Metal Framework </wiki-migration/resources/tools-software/sharc-audio-module/faust>` for more information

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#ex-work-reverb
   :alt: MIDI Controlled Reverb#.|Faust and the SHARC Audio Module#ex-work-virtual-analog|MIDI Virtual Analog Synth

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/play_button.png
   :width: 50px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/diagram_button.png
   :width: 50px
.. |/faust15.png| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module//faust15.png
   :width: 576px
   :height: 220px
.. |/faust16.png| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module//faust16.png
   :width: 574px
   :height: 273px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/export_button.png
   :width: 50px
