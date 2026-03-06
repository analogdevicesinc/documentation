MIDI Controlled Reverb on Core 1
================================

This second example is a MIDI controlled reverb on Core 1.

The Faust Code for the MIDI Controlled Reverb
---------------------------------------------

Multiple `examples <https://github.com/moforte/sam-faust/tree/master/faust-examples>`__ for the SHARC audio module have been put together and hosted on github. In order to successfully run this example, please clone this repository.

For this particular example workflow, we will be looking at the freeverb example from the git repository.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/freeverb1.gif
   :width: 600px

-  Open the Faust `online editor <https://faust.grame.fr/editor>`__.
-  You can copy the contents into the editor 2 different ways

   -  Name the \*.dsp file freeverbForBrowser.dsp. and copy the contents of freeverbForBrowser.dsp into the online editor.

      -  Drag the freeverbForBrowser.dsp file into the tile bar of the editor

-  Compile and run the Faust program using the |image1| button

Looking at the Block Diagram for the MIDI Controlled Reverb
-----------------------------------------------------------

The block diagram button |image2| can be used to generate a hierarchical block diagram for an algorithm. This block diagram is hierarchical. Here are a few of the hierarchical levels:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module//faust11.png
   :alt: /faust11.png
   :width: 540px
   :height: 160px

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module//faust12.png
   :alt: /faust12.png
   :width: 1000px
   :height: 595px

Creating Files for use with the Baremetal Framework
---------------------------------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/freeverb2.gif
   :width: 600px

-  Click the ``Export/compile to a specific platform`` button


|image3|

-  In the first dropdown box, choose ``sam``
-  In the second dropdown box, choose ``sam-source-midi`` and then ``Export``:

.. note::

   \ **faust2sam** will generate the following three C++ source files, which is the algorithm.

   
   -  ``fast_pow2.h``
   -  ``samFaustDSP.cpp``
   -  ``samFaustDSP.h``
   


-  Click on the QR code that shows to download the files
-  These 3 source files can be copied to the Faust directory in the CCES framework. The framework can then be compiled and downloaded to the SHARC Audio Module.
-  See :doc:`Faust with the CCES Bare Metal Framework </wiki-migration/resources/tools-software/sharc-audio-module/faust>` for more information

Expected Effect
~~~~~~~~~~~~~~~

When you run the project through the debugger, you will be able to control the **reverb** by turning the pressing the **push button** labeled **SW1** until **LED6** lights up and then turning the **POT** labeled **HADC0**.

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#ex-work-volume
   :alt: MIDI Controlled Volume#.|Faust and the SHARC Audio Module#ex-work-saw|MIDI Sawtooth Synth

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/play_button.png
   :width: 50px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/diagram_button.png
   :width: 50px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/export_button.png
   :width: 50px
