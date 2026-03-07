Faust Integration with the SHARC Audio Module
=============================================

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/logo_faust_complet_bleu.png
   :align: left
   :width: 300px

Overview
--------

`Faust (Functional Audio Stream) <http://faust.grame.fr/>`_ is an `open-source <https://github.com/grame-cncm/faust>`_, functional programming language, specifically designed for real-time audio signal processing and synthesis. Faust generates C++, as well as other target languages, for signal processing applications.

The Faust library provides a rich set of audio DSP objects that can be used in creating DSP algorithms. Using Faust, it is possible to quickly create large algorithms that take advantage of the computing power available on the :doc:`SHARC Audio Module </wiki-migration/resources/tools-software/sharc-audio-module>` platform.

Not only can Faust generate efficient inner loops in C++, it also:

-  Can generate test GUIs for prototyping algorithms
-  Can generate easy-to-read hierarchical block diagrams directly from the Faust source, which graphically illustrate signal flow and processing.
-  Provide a runtime system that supports MIDI for both voice allocation and parameter control.

Useful Faust References
-----------------------

This document will **not** go into detail about the Faust language. There are a number of good references and tutorials for Faust. Here are some useful references for learning more about Faust.

-  `The main Faust website <http://faust.grame.fr>`_
-  `Faust Documentation <http://faust.grame.fr/Documentation/>`_
-  `Dr. Julius O. Smith III’s site about Faust <https://ccrma.stanford.edu/~jos/spf/>`_
-  `Romain Michon's Faust tutorials <https://ccrma.stanford.edu/~rmichon/faustTutorials/>`_
-  `Romain’s online Faust course <https://ccrma.stanford.edu/~rmichon/faustWorkshops/course2015/>`_
-  `FAUST (programming_language) <https://en.wikipedia.org/wiki/FAUST_(programming_language)>`_ on Wikipedia

The Faust Compiler
------------------

The new `Faust Online Editor <https://fausteditor.grame.fr/>`_ can be used to edit, compile, and run Faust code from any modern Web Browser with `WebAssembly <http://www.webassembly.org>`_ support. All prototyping is done in a web browser and the browser can export C++ code targeted for the SHARC Audio Module platform.

|

.. tip::

   \ **Recommended Browsers**

   | \* *Chrome* (Recommended)
   
   -  *Firefox* (Note: MIDI is not currently supported)
   


faust2sam
---------

Faust programs may be targeted for many different platforms via what is known as "an architecture". Internally the script `faust2sam <https://github.com/grame-cncm/faust/blob/master-dev/tools/faust2appls/faust2sam>`_ calls the Faust compiler using an architecture that is specific to the :adi:`SHARC Audio Module <sharcaudiomodule>` platform. When an algorithm is compiled using **faust2sam**, three C++ source code files are generated for the SHARC Audio Module platform. These files may then be inserted into the baremetal framework :adi:`Cross Core Embedded Studio <cces>` (CCES) workspace to be compiled into an algorithm that runs on the SHARC Audio Module platform.

.. tip::

   **Note:** While it's possible to install and run faust2sam locally on your Linux or macOS machine we generally recommend the use of the `Faust Online Editor <http://faust.grame.fr/editor-page>`_ since it runs in your web browser and is available on all platforms including Microsoft Windows.


Hardware Setup for Faust
------------------------

In order to have a successful experience using Faust, certain hardware will be needed.

Hardware Needed
~~~~~~~~~~~~~~~

-  :adi:`ICE-1000 <ice1000>` or :adi:`ICE-2000 <ice2000>`
-  :doc:`SHARC Audio Module Platform </wiki-migration/resources/tools-software/sharc-audio-module>` and accompanying power supply
-  :doc:`Audio Project Fin </wiki-migration/resources/tools-software/sharc-audio-module/hardware/audioproj-fin>`
-  `3.5mm stereo cable <https://www.monoprice.com/product?p_id=644>`_ or equivalent
-  Powered speakers
-  Device capable of sending MIDI signals such as a MIDI keyboard controller
-  MIDI cable
-  (optional for iOS connections) Device for connecting an iOS device to the MIDI jacks. 2 devices that have been tested are the `Yamaha MD-BT01 bluetooth MIDI adapter <https://usa.yamaha.com/products/music_production/accessories/md-bt01/index.html>`_ and the `iRig Pro I/O Audio/MIDI interface <https://www.ikmultimedia.com/products/irigproio/?pkey=irig-pro-io>`_

Hardware Connections
~~~~~~~~~~~~~~~~~~~~

-  Attach the Audio Project Fin to the expansion interface of the SHARC Audio Module Platform (``P4/P5``)
-  Connect the 3.5mm jack from the powered speakers to ``LINE OUT`` of the SHARC Audio Module
-  Connect the 3.5mm jack coming from the audio source to ``LINE IN`` of the SHARC Audio Module
-  Connect the end of the MIDI cable to ``MIDI IN`` of the Audio Project Fin
-  Connect the cable of the ICE-1000 or ICE-2000 to the ``DEBUG`` header on the SHARC Audio Module
-  Connect the end of the power supply to ``P3`` of the SHARC Audio Module

Faust with the CCES Bare Metal Framework
----------------------------------------

The :adi:`SHARC Audio Module <sharcaudiomodule>` :doc:`Bare Metal framework </wiki-migration/resources/tools-software/sharc-audio-module/baremetal>` is a light-weight C / C++ framework designed for efficient audio signal processing using the :adi:`ADSP-SC589 <sc58x>` processor on the :doc:`SHARC Audio Module main board </wiki-migration/resources/tools-software/sharc-audio-module/hardware/main-board>`. Users can easily run their Faust algorithms using the bare metal framework.

Adding Faust files to the Baremetal Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Faust algorithms can be added to this framework in the ``faust`` directory.

The CCES Baremetal Framework has a subproject directory for each processor core:

-  ``<PROJECT_NAME>_Core1``
-  ``<PROJECT_NAME>_Core2``

For each project directory there is a directory where the three source files created from the Faust online editor should be placed.

-  ``<PROJECT_NAME>_Core1/src/faust``
-  ``<PROJECT_NAME>_Core2/src/faust``

.. note::

   Each core can be running a different Faust algorithm.


Typical Faust Bare Metal Configuration Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bare Metal Project Wizard Setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is easy to get up and running with a new project in CrossCore Embedded Studio using the :doc:`bare metal project wizard </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/project-wizard>`.

The following options should be selected when using the wizard:

-  Give the project a meaningful name, click Next.
-  Choose the Audio Project Fin on the Expansion Fin Selection page because it is used in all tutorials, click Next.
-  Click Next on the A2B Module Selection page without making any changes.
-  On the Faust Support page choose which cores will be running Faust, click Finish.

**No other options need to be changed.**

Configuration File Setup
^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

   This section is only needed if the :doc:`bare metal project wizard </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/project-wizard>` is not used or to update the configuration file if there was a mistake when using the wizard.


In addition there is a header file that is common across all cores called ``audio_system_config.h``. In this file the following pre-processor macros should be set. The example below indicates that a Faust algorithm will only be running on Core1 and that Core2 will be simply passing audio to the codec.

.. code:: c

   #define SAM_AUDIOPROJ_FIN_BOARD_PRESENT TRUE

   #define FAUST_INSTALLED TRUE

   #define USE_FAUST_ALGORITHM_CORE1 TRUE

   #define USE_FAUST_ALGORITHM_CORE2 FALSE

Compiling and Running the Algorithm in CCES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This document will **not** go into extensive detail on how to use CCES. Please go through the :doc:`CCES Getting Started Guide </wiki-migration/resources/tools-software/crosscore/cces/getting-started>` if looking for more detailed information on using CCES. However here are some brief notes on how to work with this algorithm.

-  Copy the Faust C++ source files to the ``faust`` directory for the core that the algorithm will run on.
-  Set the ``audio_system_config.h`` preprocessor macros as described.
-  Open the workspace with CCES.
-  Use ``File> Import> General> Existing Projects into Workspace`` to import the projects for each core into the workspace.
-  Compile with ``Project> Build Project`` **(This may take a few minutes)**
-  Connect the host computer to the SHARC Audio Module with an ICE-1000 or ICE-2000 emulator.
-  Make hardware connections as described in :doc:`Hardware Connections </wiki-migration/resources/tools-software/sharc-audio-module/faust>`
-  Create a Debug Configuration per the CCES instructions.
-  Run the compiled algorithm on the SHARC Audio Module with ``Run> Debug``
-  Send MIDI signals depending on the algorithm created

MIDI in Faust
-------------

Mapping MIDI messages to Faust Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Faust has a number of meta data conventions for mapping MIDI messages into Faust control. Below is the simple MIDI controlled sawtooth synth, which illustrates how this control mapping is done. In the example below nentry() is a numerical entry object that can be mapped to receive specific MIDI values. A number of metadata values are reserved to have specific mapping functions.

-  ``freq`` – If a MIDI noteOn event is received it’s MIDI keyNumber is mapped to a frequency.
-  ``bend`` – if a MIDI pitchBend message is received it is mapped to a bend value.
-  ``gain`` – if a MIDI noteOn message is received it’s velocity value is mapped to a gain value which ranges from [0 .. 1.0]
-  ``gate`` – if MIDI noteOn/noteOff messages are received they are mapped to a gate value (0/1)
-  ``[midi:ctrl 1]`` – A Faust control (slider, etc.) can be mapped to listen to a MIDI continuous controller.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module//faust3.png
   :alt: /faust3.png
   :width: 576px
   :height: 289px

MIDI Conventions for Audio Project Fin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The pots and push buttons on the Audio Project Fin can be used to control key algorithm parameters. The pots and push button switches are mapped to default continuous controllers.

Pot Mapping
^^^^^^^^^^^

========= ========
Pot       CC
========= ========
``HADC0`` ``CC-2``
``HADC1`` ``CC-3``
``HADC2`` ``CC-4``
========= ========

Push Button Switch Mapping
^^^^^^^^^^^^^^^^^^^^^^^^^^

======= ==========
PB      CC
======= ==========
``SW1`` ``CC-102``
``SW2`` ``CC-103``
``SW3`` ``CC-104``
``SW4`` ``CC-105``
======= ==========

The algorithm examples that are provided use these conventions. For example, the effects algorithm is “echo : flange : chorus : reverb”. For this algorithm each of the four push buttons turns on a different effects unit. The first pot is the echo feedback, the second pot is the reverb room size and the third pot is the reverb damping.

Typical Workflow
----------------

The typical workflow using faust to design algorithms for the SHARC Audio Module is:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module//faust4.png
   :alt: /faust4.png
   :width: 1000px
   :height: 503px

-  Open the Faust `online editor <https://faust.grame.fr/editor>`_.
-  Name the ``*.dsp`` file appropriately for the algorithm being created.
-  Create the algorithm in Faust. MIDI control can be attached to the algorithm in the Faust code using the MIDI metadata mechanism discussed in :doc:`MIDI in Faust </wiki-migration/resources/tools-software/sharc-audio-module/faust>`.
-  Compile and run the Faust program using the |image1| button

.. important::

   Compiling within CCES can take a while so it is recommended to iterate through changes using the Faust editor until comfortable with the algorithm


-  Once the developer is satisfied with the algorithm **faust2sam** (run in the background) can be used to generate a set of C++ files for the algorithm that are intended to be used with a CCES framework.
-  Click the ``Export/compile to a specific platform`` button

|image2|

-  In the second dropdown box, choose ``sam`` and then ``Export``
-  Click on the QR code that shows to download the files
-  These 3 source files can be copied to the ``faust`` directory in the CCES framework. The framework can then be compiled and downloaded to the SHARC Audio Module.

Here is a block diagram of how the code for the virtual analog synthesizer demo and the effects chain is organized.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module//faust5.png
   :alt: /faust5.png
   :width: 976px
   :height: 625px

Example Workflows
-----------------

-  :doc:`MIDI Controlled Volume (Core 1) </wiki-migration/resources/tools-software/sharc-audio-module/faust/ex-work-volume>`
-  :doc:`MIDI Controlled Reverb (Core 1) </wiki-migration/resources/tools-software/sharc-audio-module/faust/ex-work-reverb>`
-  :doc:`MIDI Sawtooth Synth (Core 1) </wiki-migration/resources/tools-software/sharc-audio-module/faust/ex-work-saw>`
-  :doc:`MIDI Virtual Analog Synth (Core1) / Effects (Core 2) </wiki-migration/resources/tools-software/sharc-audio-module/faust/ex-work-virtual-analog>`

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#hardware
   :alt: Hardware Reference#.|SHARC Audio Module#.micropython|MicroPython Overview

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/play_button.png
   :width: 50px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/faust/export_button.png
   :width: 50px
