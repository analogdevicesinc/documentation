MIDI Controlled Volume on Core 1
================================

A first example to demonstrate the workflow is a simple MIDI controlled stereo volume control that runs on Core 1.

The Faust Code for the MIDI Controlled Volume
---------------------------------------------

Here is the Faust code for the MIDI controlled stereo volume. Note that the metadata string “[midi:ctrl 2]” is used to map MIDI continuous controller 2 (CC-2) to control the gain slider.

<WRAP clear/>

.. code:: c

   //---------------------------------------------------------
   // Volume control in dB with MIDI control (CC-1, modWheel)
   //---------------------------------------------------------

   import("stdfaust.lib");

   gain        =  vslider("Volume[midi:ctrl 2] [tooltip CC-1]", 0, -70, +4, 0.1) : ba.db2linear : si.smoo;

   process     = _,_: *(gain), *(gain);

Building a Test GUI for the MIDI Controlled Volume
--------------------------------------------------

-  Open the Faust `online editor <https://faust.grame.fr/editor>`_.
-  Name the \*.dsp file volume.dsp.
-  Copy the algorithm above into the online editor.
-  Compile and run the Faust program using the |image1| button

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/volume1.gif
   :width: 600px

Looking at the Block Diagram for the MIDI Controlled Volume
-----------------------------------------------------------

The block diagram button |image2| can be used to generate a hierarchical block diagram for an algorithm.

.. note::

   You may need to allow pop-ups in your browser to view the block diagram


This block diagram is hierarchical. Here are a few of the hierarchical levels:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module//faust8.png
   :alt: /faust8.png
   :width: 312px
   :height: 254px

Creating Files for use with the Baremetal Framework
---------------------------------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/volume2.gif
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

When you run the project through the debugger, you will be able to control the volume by turning the POT labeled ``HADC0``.

--------------

`Hardware Reference#.|Faust and the SHARC Audio Module#ex-work-reverb|MIDI Controlled Referb <https://wiki.analog.com/_media/navigation SHARC Audio Module#..hardware>`_

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/play_button.png
   :width: 50px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/diagram_button.png
   :width: 50px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/export_button.png
   :width: 50px
