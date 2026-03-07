Filters
=======

| :doc:`Click here to return to the Toolbox page </wiki-migration/resources/tools-software/sigmastudio/toolbox>`
| -----------------------------------------------------------------------------------------------------------

.. hint::

   Note: Most of these filters allow either double- or single-precision computation. Double-precision should be used unless the DSP is running out of resources. Single-precision should not be used for signal content below 1/10 the sampling frequency (5kHz for a typical 48kSPS system), or for high-Q filters.


The Filters library of the Toolbox lets you access numerous filter / EQ blocks for shaping the frequency content of your signal. The following blocks are available:

FIR Filters
-----------

-  :doc:`FIR Filter </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/firfilter>`
-  :doc:`General FIR filter </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/generalfirfilter>`
-  :doc:`FIR Filter Pool </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/firfilterpool>`
-  :doc:`NLMS Adaptive Filter </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/nlmsfilter>`
-  :doc:`Modified-Fx LMS </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/mfxlms>`
-  :doc:`FxLMS Filter </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/filterednlmsfilter>`

Second Order Filters
--------------------

-  :doc:`Parametric EQ </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/parametriceq>`
-  :doc:`Crossover </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/crossover>`

-  :doc:`General (2nd Order) </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/general2ndorder>`; This page contains coefficient formulas for most second-order filters in SigmaStudio.
-  :doc:`General (2nd Order)/Slew </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/generaleq2ndorderslew>`
-  :doc:`General (2nd Order)/Slew Ext </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/generaleq2ndorderslewext>` (Slew Rate Control from Pin)
-  :doc:`General (2nd Order)/Lookup </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/general2ndorderlookup>` (Pin selects from a table of similar second-order filters)
-  :doc:`General (2nd Order)/Index Selectable </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/general2ndorderindexselectable>` (Pin selects from a table of arbitrary second-order filters)
-  :doc:`General 2nd Order w var Param/Lookup/Slew </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/general2ndorderwvarparamlookupslew>`

-  :doc:`Blend EQ </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/generaleqblend>`
-  :doc:`Blend EQ Ext </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/generaleqblendext>`
-  :doc:`Single Blend EQ </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/singleblendeq>`
-  :doc:`Single Blend EQ Ext </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/singleblendeqext>`
-  :doc:`RMS Blend EQ </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/rmsblendeq>`
-  :doc:`Text-In (linked) </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/textinlinked>`
-  :doc:`Text-In (unlinked) </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/textinunlinked>`
-  :doc:`Text-in Eq Slew </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/textineqslewunlinked>`
-  :doc:`Text-in Eq Slew Ext </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/textineqslewext>`
-  :doc:`Biquad 3channel 1cascade </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/biquad3ch1cascade>`
-  :doc:`Biquad 8channel 4cascade </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/biquad8ch4cascades>`
-  :doc:`Biquad 8channel 5cascade </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/biquad8ch5cascades>`
-  :doc:`IdxSelectable Indp. Multiple Band Filter </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/idxselectableindpmultiplebandfilter>`
-  :doc:`Medium Size EQ </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/mediumsizeeq>`
-  :doc:`Medium-Size Eq Slew </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/mediumsizeeqslew>`
-  :doc:`Medium-Size Eq Slew Ext </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/mediumsizeeqslewext>`

First Order Filters
-------------------

-  :doc:`General (1st Order) </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/general1storder>`
-  :doc:`First Order w var Param/Lookup/Slew </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/firstorderwvarparamlookupslew>`

Miscellaneous
-------------

-  :doc:`DC Blocking </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/dcblocking>`
-  :doc:`De-Emphasis </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/deemphasis>`
-  :doc:`Pinking </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/pinking>`
-  :doc:`State Variable </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/statevariable>`
-  :doc:`State Variable (Q input) </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/statevariableqinput>`
-  :doc:`State Variable (Q/F input) </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/statevariableqfinput>`
-  :doc:`Non Bare Filter </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/nonbarefilter>`
-  :doc:`Tracking Filter </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/trackingfilter>`

The topic pages in this book contain specific information about the individual blocks. Be sure to take a look at the :doc:`Filter Examples </wiki-migration/resources/tools-software/sigmastudio/tutorials/filterexamples>` page to see sample schematics using some filter blocks.

To view the response of a filter's settings, drag a filter block into the workspace attach a :doc:`Simulation Stimulus </wiki-migration/resources/tools-software/sigmastudio/toolbox/systemschematicdesign/simulationstimuli>` block to the input and a :doc:`Simulation Probe </wiki-migration/resources/tools-software/sigmastudio/toolbox/systemschematicdesign/simulationprobe>` to the filter's output. Now Click the Probe button Stimulus button. Take a look at the :doc:`Filter Examples </wiki-migration/resources/tools-software/sigmastudio/tutorials/filterexamples>`.
