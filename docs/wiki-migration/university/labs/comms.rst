Communications Based Lab Activity Material
==========================================

The laboratory activities provided on this wiki are considered open source and available for free use in non-commercial educational and academic settings. **The only requirement is that they continue to retain the attribution to Analog Devices Inc.** Supplying them on the ADI wiki allows registered users to contribute to the materials posted here improving the content and keeping them up to date.

Laboratory guides provided on GitHub are available for modification as well, which can be done through the provided **LaTeX** source. As with the wiki **the requirement is that they continue to retain the attribution to the original authors and you abide by the co-located licenses.**

Lab Preparation
---------------

Circuit Simulation
~~~~~~~~~~~~~~~~~~

| Basic information and material on :doc:`circuit simulation </wiki-migration/university/courses/electronics/circuitsimulationnotes>`, including tool links and usage information.
| Most of the labs are populated with :adi:`LTspice <en/design-center/design-tools-and-calculators/ltspice-simulator.html>` resource files which contain the schematics of the circuits discussed at a specific topic. A file containing the ADALM2000 connections for the schematics can be found here: :git-education_tools:`m2k/ltspice/m2k_conn_ltspice`.

+----------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Course         | ADALM1000 (M1K)                                                                                           | ADALM2000 (M2K)                                                                                                      | ADALM-PLUTO (PlutoSDR)                                                                                                                        |
+================+===========================================================================================================+======================================================================================================================+===============================================================================================================================================+
| Communications | `schematic files <https://wiki.analog.com/_media/university/courses/electronics/electronics-lab-i.zip>`_  | :git-education_tools:`schematic files <m2k/adisimpe/electronics-lab-i>`                                              | `transceiver simulation <https://www.mathworks.com/matlabcentral/fileexchange/46626-rf-blockset-models-for-analog-devices-rf-transceivers>`_  |
+----------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

Lab Hardware and Software
~~~~~~~~~~~~~~~~~~~~~~~~~

These labs can be performed using the :doc:`ADALM2000 </wiki-migration/university/tools/m2k>` (M2K) Active Learning Module , or the :doc:`ADALM1000 </wiki-migration/university/tools/m1k>` (M1K) entry level design instrumentation.

For labs using the :doc:`ADALM-PLUTO </wiki-migration/university/tools/pluto>` (PlutoSDR), a MATLAB license will be required with the Communications Toolbox. If you do not have MATLAB, you can get a temporary trial from `this link <https://www.mathworks.com//campaigns/products/trials.html?prodcode=CM>`_ and then install the `support package <https://www.mathworks.com//hardware-support/adalm-pluto-radio.html>`_ for PlutoSDR.

+-------------+--------------------------------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|             | ADALM1000 (M1K)                                                                | ADALM2000 (M2K)                                           | ADALM-PLUTO (PlutoSDR)                                                                            |
+=============+================================================================================+===========================================================+===================================================================================================+
| PC Software | :doc:`ALICE </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>` | :doc:`Scopy </wiki-migration/university/tools/m2k/scopy>` | `Matlab(Trial) <https://www.mathworks.com//campaigns/products/trials.html?prodcode=CM>`_          |
|             |                                                                                |                                                           | `PlutoSDR Support Package <https://www.mathworks.com//hardware-support/adalm-pluto-radio.html>`_  |
+-------------+--------------------------------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------+

Some of the labs are written to be performed using just the components provided in the Analog Parts Kit, :doc:`ADALP2000 </wiki-migration/university/tools/adalp2000/parts-index>`, supplied through ADI and our authorized distribution channels, however additional devices are provided.

General Lab materials
~~~~~~~~~~~~~~~~~~~~~

M1K and M2K based material:

-  Background Lab Notes: :doc:`Solder-less Breadboards </wiki-migration/university/courses/electronics/electronics-lab-breadboards>`
-  Background Lab Activity: :doc:`Solder-less Breadboard Parasitic Capacitance </wiki-migration/university/courses/electronics/electronics-lab-breadboard-coupling>`
-  Background Lab Notes: :doc:`Resistors </wiki-migration/university/courses/electronics/electronics-lab-resistors>` (including color code)
-  Background Lab Notes: :doc:`Capacitors </wiki-migration/university/courses/electronics/electronics-lab-capacitors>` (including color code)
-  Review Activity: :doc:`Real voltage sources </wiki-migration/university/courses/electronics/electronics-lab-0>`

PlutoSDR based material:

-  Textbook (PDF): :adi:`Software-Defined Radio For Engineers <sdrforengineers>`
-  `Textbook MATLAB code <https://github.com/sdrforengineers/code>`_
-  `Lab MATLAB code <https://github.com/sdrforengineers/LabGuides/tree/master/textbook/matlab>`_

.. include:: main_list.rst

General Expected Background
===========================

The communications labs and topics are split into two main categories: analog communications and digital communications. The analog communications sections require a basic background in certain analysis, as well as some introduction to continuous-time signal analysis. The digital communications topics are targeted at those with a solid background in digital signal processing and the fundamentals of modulation/demodulation. A basic understanding of probability tools is useful as well. Labs are performed in MATLAB, therefore knowledge of writing MATLAB code is essential.

Related reference manuals are recommended:

-  `Software Receiver Design: Build your Own Digital Communication System in Five Easy Steps <https://www.amazon.com/Software-Receiver-Design-Digital-Communication/dp/0521189446>`_
-  `Digital Communications: A Discrete-Time Approach <https://www.amazon.com/Digital-Communications-Discrete-Time-Michael-Rice/dp/0130304972>`_
-  `Linear Systems and Signals <https://www.amazon.com/Linear-Systems-Signals-2nd-Lathi/dp/0195158334>`_

**Return to Communications Course Material** :doc:`Table of Contents </wiki-migration/university/courses/comms>`
