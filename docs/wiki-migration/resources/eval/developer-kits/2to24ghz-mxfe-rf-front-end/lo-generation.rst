:doc:`Link to parent page </wiki-migration/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end>`

LO Generation Options
=====================

| The 2-24GHz RF Front End has two different sets of LO specifications and requirements- one for the fixed LO sources and a second for the wideband, tunable LOs. Additionally, LO performance requirements vary widely across the instrumentation, communications, and aerospace & defense application space, so while a one-size-fits-all solution for the LO generation circuitry may not be practical, Analog Devices offers numerous, flexible options for wideband frequency synthesizers.
| =====Fixed LO Source=====
| The 18GHz, fixed LO source can be supplied by any integrated PLL/VCO such as the :adi:`ADF4371`, or a discrete LO implementation using ADI PLLs and quad-band VCOs for applications requiring lower phase noise. The frequency synthesizer circuit detailed in CN0568 (shown below), provides one possible solution for a discrete LO implementation using the :adi:`ADF41513` PLL and :adi:`HMC8362` quad-band VCO.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/cn0568synthesizerdiagram.png
   :align: center
   :width: 600px

More information on the CN0568 frequency synthesizer can be found here: :adi:`cn0568.html#rd-overview <en/design-center/reference-designs/circuits-from-the-lab/cn0568.html#rd-overview>`

This circuit was adapted to provide a cleaner output tone (reduced spurs) and a higher output power with the following block diagram:


|image1|

For this design, we selected a discrete LO implementation using the ADF41513 and the HMC8362 to achieve lower phase noise and power consumption. The following plot shows the simulated phase noise performance in ADI SimPLL:


|image2|

The following table summarizes the data in the plot above:


|image3|

The full simulation file created in ADI SimPLL can be requested with the instructions provided at the bottom of this page.

| 
| =====Tunable LO Source===== The tunable LO synthesizer has a more complex set of requirements, many of which directly impact the system-level functionality of the signal chain, such as tuning speed and frequency coverage. The wideband frequency synthesizer circuit shown in the figure below uses the :adi:`ADF4371` integrated PLL/VCO, which is one potential option for the tunable LO source, enabling low phase-noise tuning across the RF signal chain’s full operating range. The tunable filtering on the :adi:`ADF4371` outputs is optional and dependent on the LO spurious requirements of the end system. The SPDT switch selects between the two :adi:`ADF4371` outputs and the :adi:`HMC383` driver amp ensure sufficient LO drive level at the mixer for optimal performance.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/tunable_lo_block_diagram.png

The following plot shows the simulated phase noise performance of the tunable LO circuit for the 11.5-16 GHz output of the :adi:`ADF4371` in ADI SimPLL:


|image4|

The following table summarizes the data in the plot above:


|image5|

The following plot shows the simulated phase noise performance of the tunable LO circuit for the 16-28 GHz output of the :adi:`ADF4371` in ADI SimPLL:


|image6|

The following table summarizes the data in the plot above:


|image7|

Simulation files have been created for these circuits in ADI SimPLL. Two files can be provided by following the instructions at the bottom of this page, one for each output of the :adi:`ADF4371`.

|

.. admonition:: Download
   :class: download

   To request the SimPLL files that simulation the performance of these circuits, please send a request `here <https://support.analog.com/en-US/technical-support/create-case-techsupport/>`__ and include the following info:


   | \* Name
   
   -  Job Title
   -  Company Name
   -  Company Location
   -  Application/Use Case
   
   |

   |


| 

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/fixed_lo_block_diagram.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/18g.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/18g_table.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/11.5g.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/11.5g_table.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/22.6g.png
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/22.6g_table.png
