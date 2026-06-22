.. _eval-ad974x fmc ebz quickstart:

Quick start
===============================================================================

The quick start guide provides step-by-step instructions for setting up
the :adi:`EVAL-AD9740`, :adi:`EVAL-AD9742`, :adi:`EVAL-AD9744` or
:adi:`EVAL-AD9748` evaluation board on the supported FPGA development
board. This guide covers SD card preparation, hardware setup, and Linux
IIO client usage.

.. toctree::

   On ZedBoard <zed>
   On SDP-H1 <sdp-h1-ace>

.. _ad974x fmc ebz carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9740`, :adi:`EVAL-AD9742`, :adi:`EVAL-AD9744` or 
:adi:`EVAL-AD9748` connects to the FPGA carrier via an FMC LPC connector. 
VADJ must be set to 3.3 V.

.. list-table::
   :header-rows: 1

   * - FPGA board
     - :adi:`EVAL-AD9740 <EVAL-AD9740>`
     - :adi:`EVAL-AD9742 <EVAL-AD9742>`
     - :adi:`EVAL-AD9744 <EVAL-AD9744>`
     - :adi:`EVAL-AD9748 <EVAL-AD9748>`
   * - `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`_
     - FMC LPC
     - FMC LPC
     - FMC LPC
     - FMC LPC
   * - `SDP-H1 <https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-sdp-h1.html>`_
     - FMC LPC
     - FMC LPC
     - FMC LPC
     - FMC LPC

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - FPGA board
     - HDL
     - Linux software
     - No-OS software
   * - `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`_
     - Yes
     - Yes
     - No
   * - `SDP-H1 <https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-sdp-h1.html>`_
     - No
     - No
     - No

Hardware setup
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9740`, :adi:`EVAL-AD9742`, :adi:`EVAL-AD9744` or
:adi:`EVAL-AD9748` connects to the
`ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/
avnet-board-families/zedboard/>`_ via the FMC LPC connector (P1 on the
evaluation board, FMC on the ZedBoard). Before inserting the evaluation
board, set VADJ to 3.3 V and configure the ZedBoard for SD card boot.

The :adi:`EVAL-AD9740`, :adi:`EVAL-AD9742`, :adi:`EVAL-AD9744` or 
:adi:`EVAL-AD9748` can also be controlled with the :adi:`EVAL-SDP-H1` controller
board and the :adi:`ACE` software, without any FPGA or Linux system.

ZedBoard + EVAL-AD974X
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  .. figure:: ../images/ad9744_zed.jpeg
     :alt: ZedBoard with EVAL-AD9744 inserted into the FMC LPC connector
     :width: 800

     ZedBoard with EVAL-AD974X hardware setup                                                                                                                                                                                                                                                                                                                       

Go to :ref:`the quick start guide <eval-ad974x fmc ebz quickstart zed>`.

SDP-H1 + EVAL-AD974X + ACE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  .. figure:: ../images/ad9744_sdp_h1.jpeg
     :alt: AD9744-FMC-EBZ Evaluation Board with SDP-H1
     :width: 800

     AD9744-FMC-EBZ Evaluation Board with SDP-H1.

Go to :ref:`the quick start guide <eval-ad974x fmc ebz quickstart sdp-h1-ace>`.
