Multiplexer/Demultiplexer Examples
==================================

:doc:`Click here to return to the Tutorials section. </wiki-migration/resources/tools-software/sigmastudio/tutorials>`

Example 1: Crossfade (Data-Controlled)
--------------------------------------

This schematic shows a simple way of smoothly switching (crossfading) from one signal to the other (here 500 Hz and 2kHz). It uses these blocks: DC Input control entry, two Tone (Lookup/Sine), Crossfade (Data-Controlled), and Output.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/multiplexerdemultiplexerexamplespicture1.jpg
   :alt: multiplexerdemultiplexerexamplespicture1.jpg

Example 2: Index-Selectable Mux/DeMux
-------------------------------------

This schematic shows a simple way of multiplexing two sources and then demultiplexing the signals to two outputs. Two Tone (Lookup/Sine) blocks feed an Index-Selectable Multiplexer, with the switching between them controlled by a DC Input. The output goes to an Index-Selectable Demultiplexer, whose behavior is controlled by a second DC Input Entry to feed two Outputs.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/multiplexerdemultiplexerexamplespicture2.jpg
   :alt: multiplexerdemultiplexerexamplespicture2.jpg

Example 3: Mono Switch
----------------------

This schematic uses Mono Switch 1xN and Mono Switch Nx1 flanking a General (2nd-Order) Filter grown by 2. The filter frequency response choice is highpass and the highpassed signal is routed to the output. Tone (Lookup/Sine), Probe, Stimuli and Output blocks complete the signal flow.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/multiplexerdemultiplexerexamplespicture3.jpg
   :alt: multiplexerdemultiplexerexamplespicture3.jpg

Below is the frequency response of the HP filter.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/multiplexerdemultiplexerexamplespicture4.jpg
   :alt: multiplexerdemultiplexerexamplespicture4.jpg

Example 4: Stereo Switch
------------------------

This schematic shows a simple way of multiplexing two sources using two State-Variable filters, Stereo Switch Nx2, Input and Output blocks. The filters' high-pass outputs are selected and routed to the output blocks.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/multiplexerdemultiplexerexamplespicture5.jpg
   :alt: multiplexerdemultiplexerexamplespicture5.jpg

Example 5: State Machine
------------------------

This schematic uses a Counter as the control, a Tone (Lookup/Sine) and a State Machine block, in order to show how the tone passed through to the output is blocked once the count goes beyond the specified range.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/multiplexerdemultiplexerexamplespicture6.jpg
   :alt: multiplexerdemultiplexerexamplespicture6.jpg
