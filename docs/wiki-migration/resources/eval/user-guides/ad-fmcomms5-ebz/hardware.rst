AD-FMCOMMS5-EBZ Hardware
========================

| 
| ===== Schematic, PCB Layout, Bill of Materials =====

Rev. C
------

.. admonition:: Download
   :class: download

   :adi:`AD-FMCOMMS5-EBZ Design & Integration Files <media/en/reference-design-documentation/design-integration-files/ad-fmcomms5-ebz-designsupport.zip>`

   
   -  Schematic
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project (get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`_; you need 17.2 or higher)
   


Rev. B
------

.. admonition:: Download
   :class: download

   
   -  `Rev B Schematic <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms5-ebz/fmcomms5_schematic.pdf>`_
   -  `Rev B BOM <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms5-ebz/fmcomms5-bom.xls>`_
   -  `Rev B Build Files <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms5-ebz/fmcomms5_build.zip>`_
   -  `Rev B Allegro Board File <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms5-ebz/fmcomms5_revb.7z>`_ (This file is `compressed <http://www.7-zip.org/7z.html>`_). Get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`_ (You need 16.5 or higher).
   
   .. important::

      **ERRATA**:

         
         The FMCOMMS5, REV B has a bug in it, that doesn't allow the ADF5355 to function properly. (Pin 5, AVDD is a floating node). It's a simple fix - short pin 5 (AVDD) with pin 4 (CE) to make a connection to VDD_EXT_LO_3P3.


         
         |AD-FMCOMMS5-EBZ Rev B ADF5355 rework|

I/O Voltage
~~~~~~~~~~~

The :adi:`AD-FMCOMMS5-EBZ` (AD9361) assumes a VDD_INTERFACE voltage between 1.71V and 2.625V (1.8 to 2.5 +/- 5%), so on your FPGA carrier board, you should ensure that V\ :sub:`ADJ` is between these levels. Setting things to 3.3V will damage the part.

Phase Synchronization
~~~~~~~~~~~~~~~~~~~~~

Traces between baluns and SMAs are not phase-matched on REV-A and REV-B which can cause phase misalignment with the libad9361-iio ad9361_fmcomms5_phase_sync solution. This is corrected on REV-C. Therefore, phase alignment performance can vary over frequency. The RF switches on REV-A/B are also not designed to work above 900 MHz. Higher frequency switches are available on REV-C.

Below are some preliminary results using Release 2018-R1 with equal length but unmatched cables

Rev B
^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms5-ebz/fm5_phase_performance_rev_b.svg
   :alt: Rev B
   :align: center

Rev C
^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms5-ebz/fm5_phase_performance_rev_c.svg
   :alt: Rev C
   :align: center

.. |AD-FMCOMMS5-EBZ Rev B ADF5355 rework| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms5-ebz/fmcomms5_rework.png
   :width: 200px
