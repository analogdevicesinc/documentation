PulSAR ADC PMODs HDL User Guide
===============================

.. warning::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/projects/pulsar_adc/index.html\


Overview
--------

These low power ADCs offer very high performance from 14-bits up to 18-bits with throughputs ranging from 100ksps to 1.3MSPS. The boards are designed to demonstrate the ADC's performance and to provide an easy digital interface for a variety of system applications. A full description of these products are available in their respective data sheets and should be consulted when utilizing the boards. To purchase hardware, please visit our :adi:`website. <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/PulsarPMODs.html>`

Applications
~~~~~~~~~~~~

-  Battery-powered equipment
-  Data acquisition
-  Instrumentation
-  Medical instruments
-  Process controls

Supported Devices
-----------------

-  :adi:`AD7942`
-  :adi:`AD7946`
-  :adi:`AD7988-1`
-  :adi:`AD7685`
-  :adi:`AD7687`
-  :adi:`AD7691`
-  :adi:`AD7686`
-  :adi:`AD7688`
-  :adi:`AD7693`
-  :adi:`AD7988-5`
-  :adi:`AD7980`
-  :adi:`AD7983`
-  :adi:`AD7690`
-  :adi:`AD7982`
-  :adi:`AD7984`

Evaluation Boards
-----------------

-  :adi:`EVAL-AD7942-PMDZ`
-  :adi:`EVAL-AD7946-PMDZ`
-  :adi:`EVAL-AD7988-1-PMDZ`
-  :adi:`EVAL-AD7685-PMDZ`
-  :adi:`EVAL-AD7687-PMDZ`
-  :adi:`EVAL-AD7691-PMDZ`
-  :adi:`EVAL-AD7686-PMDZ`
-  :adi:`EVAL-AD7688-PMDZ`
-  :adi:`EVAL-AD7693-PMDZ`
-  :adi:`EVAL-AD7988-5-PMDZ`
-  :adi:`EVAL-AD7980-PMDZ`
-  :adi:`EVAL-AD7983-PMDZ`
-  :adi:`EVAL-AD7690-PMDZ`
-  :adi:`EVAL-AD7982-PMDZ`
-  :adi:`EVAL-AD7984-PMDZ`

HDL Design Description
----------------------

In the :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>` can be found an in-depth presentation and instructions about the HDL design in general.

The reference design uses the standard `SPI Engine Framework <:doc:`/wiki-migration/resources/fpga/peripherals/spi_engine`>`_ with an integrated pwm generator, which will provide the required conversion rate for the ADC.

HDL Block Diagram
~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/pulsar_adc_pmod_hdl.svg
   :alt: pulsar_adc_pmod_hdl.svg
   :width: 800px

Steps for building the HDL design:

-  Confirm that you have the right tools (the reference design requires Vivado 2021.1)
-  Clone the HDL GitHub repository (the project is located at :git-hdl:`projects/pulsar_adc_pmdz`)
-  Set up the required sampling rate (see caption **Design Configuration**)
-  Build the project (see :doc:`/wiki-migration/resources/fpga/docs/build`)

Design Configuration
~~~~~~~~~~~~~~~~~~~~

The reference design uses a clock generator for the divison of the spi clock and a pwm generator for the conversion signal. The required parameters can be set in :git-hdl:`projects/pulsar_adc_pmdz/common/pulsar_adc_pmdz_bd`.tcl file using the following values, where the PULSE_0_PERIOD is computed as Tcyc_min/Tspi_clk:

.. admonition:: Download
   :class: download

   
   =================================================== ==============
   Part                                                PULSE_0_PERIOD
   =================================================== ==============
   :adi:`AD7942 <eval-ad7942>`     640
   :adi:`AD7946 <eval-ad7946>`     320
   :adi:`AD7988-1 <eval-ad7988-1>` 1600
   :adi:`AD7685 <eval-ad7685>`     640
   :adi:`AD7687 <eval-ad7687>`     640
   :adi:`AD7691 <eval-ad7691>`     640
   :adi:`AD7686 <eval-ad7686>`     320
   :adi:`AD7688 <eval-ad7688>`     320
   :adi:`AD7693 <eval-ad7693>`     320
   :adi:`AD7988-5 <eval-ad7988-5>` 320
   :adi:`AD7980 <eval-ad7980>`     160
   :adi:`AD7983 <eval-ad7983>`     120
   :adi:`AD7690 <eval-ad7690>`     250
   :adi:`AD7982 <eval-ad7982>`     160
   :adi:`AD7984 <eval-ad7984>`     120
   =================================================== ==============
   


**HW Platform(s):**

-  `Cora Z7S <https://digilent.com/reference/programmable-logic/cora-z7/start>`_

HDL Downloads
-------------

.. admonition:: Download
   :class: download

   
   -


   
   |Pulsar ADC PMODs HDL Project.|

.. |Pulsar ADC PMODs HDL Project.| image:: https://wiki.analog.com/_media/:git-hdl:`projects/pulsar_adc_pmdz`
