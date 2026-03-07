LTspice User Guide - AD469x Model
=================================

Overview
--------

AD469x is a family of 16-Bit, Easy Drive Mux SAR ADCs. The LTspice component library includes the AD469x family to enable hardware-free prototyping of multichannel precision measurement signal chains using the AD469x. This user guide provides an overview of the AD469x LTspice model features and functionality, plus links to other detailed user guides for setting up the models for different types of simulations (transient, noise analysis, etc.).

Models Supported
~~~~~~~~~~~~~~~~

There are four generics in the AD469X family, ranging from 8 - 16 Channels, and 500 kSPS to 1 MSPS. Please note that the LTspice models for the 16-channel generics (AD4695 and AD4696) only include 8 analog input channels.

======= ================= =========== ================
Generic Channels (Device) Sample Rate Channels (Model)
======= ================= =========== ================
AD4695  16                500k        8
AD4696  16                1M          8
AD4697  8                 500k        8
AD4698  8                 1M          8
======= ================= =========== ================

Model Revision History
~~~~~~~~~~~~~~~~~~~~~~

-  Original model releases – 06/22/2022

Features & Capabilities
~~~~~~~~~~~~~~~~~~~~~~~

The AD469x LTspice models cover the following features:

Transient Simulations
^^^^^^^^^^^^^^^^^^^^^

:doc:`Transient simulation </wiki-migration/resources/quick-start/ad469x-ltspice-user-guide/transient-sims>` using the AD469x LTspice model assess the settling accuracy and performance of the analog front-end (AFE) in response to the charge kickback of the AD469x analog input pins. The models emulate the following relevant behaviors of actual AD469x devices:

-  Magnitude of the transient glitches on the Easy Drive ADC inputs
-  Timing of the transient glitches relative to each CNV rising edge
-  Acquisition time of ADC relative to the desired sampling rate
-  Behaviors of input transients of each channel for a given channel sequencer configuration

Symbol and Pin Functions
------------------------

This section provides step-by-step instructions on how to access the AD469x family symbol in LTspice.

-  Open a New Schematic in LTspice:

To begin, open LTspice and create a new schematic by selecting the appropriate option from the file menu.

-  Access the Components Library:

Locate the components library in LTspice taskbar. Click on the symbol library icon twice to open the window.

-  Navigating the Component Library:

Once the component library window pops up, you will see a variety of categories and subcategories. Look for the ADC list and click on it to access the available ADC models in the LTspice directory. Within the ADC list, locate and select the AD4696 model to proceed with your design.

.. image:: https://wiki.analog.com/_media/resources/quick-start/symbol_ad469x.gif
   :align: center

Symbol
~~~~~~

The symbol for the model is shown in Fig. 1.

.. image:: https://wiki.analog.com/_media/resources/quick-start/ad469x-symbol.png
   :alt: LTspice Symbol for AD469x family
   :align: center
   :width: 200px

Pin Functions
~~~~~~~~~~~~~

The following table lists the names and brief descriptions of the pins on the AD469x LTspice models. The functionality of each pin varies slightly depending on the type of simulation. Detailed descriptions for each pin are included in their respective simulation overview guide.

+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pin               | Function                                                                                                                                                                                                             |
+===================+======================================================================================================================================================================================================================+
| IN0 - IN7         | 8 analog input channels for conversion.                                                                                                                                                                              |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SLCT0 - SLCT2     | Bit select input for channel selection. Only valid for SEQ_EN = 0.                                                                                                                                                   |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CH_OUT0 - CH_OUT2 | Channel indicator. The CH_OUT[2:0] pins represent a 3-bit value that corresponds to the most-recently sampled channel. When CH_OUTx is 0V, it represents logic LOW and when CH_OUTx is 1V, it represents logic HIGH. |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| COMM              | Common channel input emulates the COM pin on AD469x.                                                                                                                                                                 |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| REF               | Reference voltage input determines the full-scale range and LSB size of the VSAMPLE output. VREF = REF - REFGND                                                                                                      |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AVDD / LDO_IN     | Connect AVDD to 5V.                                                                                                                                                                                                  |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CNV               | Convert start signal. Used in transient sims to initiate the conversion of selected channels.                                                                                                                        |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RESET             | Reset signal (active high RESET). Must be pulsed high at the start of transient simulation to model active switches.                                                                                                 |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| REFGND            | Reference Ground. REF is referenced to REFGND.                                                                                                                                                                       |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VSAMPLE           | Sampled output voltage.                                                                                                                                                                                              |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Parameters
----------

The AD469x LTspice models include a set of parameters for configuring various aspects of the models. The parameters are accessed by right clicking on the parameters statements on the symbol.

.. image:: https://wiki.analog.com/_media/resources/quick-start/param-u1.png
   :align: center
   :width: 400px

.. image:: https://wiki.analog.com/_media/resources/quick-start/param-u2.png
   :align: center
   :width: 400px

The following table lists the names and brief descriptions of the parameters available in the AD469x LTspice models. Detailed descriptions for each parameter are included in their respective simulation overview guide.

+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
|                |                                                                                                                                                                                                                                                        | Default Value |
+================+========================================================================================================================================================================================================================================================+===============+
| OSR            | Oversampling Ratio. In transient simulations, OSR determines how many times the same channel is sampled before switching to the following one (only for SEQ_EN!=0). In noise simulations, OSR determines the input referred noise of the AD469x model. | 1             |
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| SEQ_EN         | Sequencer Enable. Determines the active channels to be used in the simulation.                                                                                                                                                                         | 0             |
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| CNV_FREQ_NOISE | Conversion Frequency value for noise analysis. This parameter must be set to 0, except for noise analysis.                                                                                                                                             | 0             |
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| CNV_CH_NOISE   | Channel to be selected for AC/Noise analysis.                                                                                                                                                                                                          | 0             |
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| COM_OPT        | Common input enable. Enable the function for the COMM input. The conversion will take the voltage value at COMM as reference instead of REFGND. It can be used for pseudo-differential conversions.                                                    | 0             |
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+

Limitations / Disclaimer
------------------------

The model has not undergone validation for the remaining simulation types, including.

-  DC sweeps
-  AC analysis
-  DC transfer function
-  DC operating point analyses

--------------

Sample Schematics
=================

Transient Simulation
--------------------

A detailed explanation on sample transient schematic and downloadable files are available here: :doc:`Transient Simulations with AD469x LTspice Model </wiki-migration/resources/quick-start/ad469x-ltspice-user-guide/transient-sims>`
