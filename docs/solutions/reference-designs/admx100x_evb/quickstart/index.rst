.. _admx100x-evb quickstart:

Quick Start
===========

The quick start guides provide step-by-step instructions for the initial setup
of the :adi:`EVAL-ADMX100X-FMCZ` evaluation board with the :adi:`ADMX1001` or
:adi:`ADMX1002` modules.

Before proceeding, make sure you have completed the :ref:`admx100x prerequisites`.

.. toctree::
   :hidden:

   On ZedBoard <zed>
   On SDP-H1 <sdp-h1>

.. _admx100x-evb quickstart carriers:

Supported Controller Boards
---------------------------

.. list-table::
   :header-rows: 1

   * - Controller Board
     - ADMX1001
     - ADMX1002
   * - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes (via FMC LPC)
     - Yes (via FMC LPC)
   * - :adi:`SDP-H1 <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/sdp-h1.html>`
     - Yes (via FMC)
     - Yes (via FMC)
   * - :adi:`SDP-S <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-sdp-cs1z.html>`
       :adi:`SDP-B <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-sdp-cb1z.html>`
       :adi:`SDP-I-PMOD <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/sdp-i-pmod.html>`
     - No
     - Yes (via PMOD)

.. _admx100x-evb quickstart sdp-s:

Quick Start with SDP-S or SDP-B (ADMX1002 Only)
-----------------------------------------------

#. Verify the jumper and switch settings match Table 2 in the :ref:`admx100x-evb user-guide`.
#. Connect the **ADMX1002** module to the module connector (**P5**).
#. Configure the **SDP-I-PMOD** interposer before connecting:

   - Set **JP1** to the **SPI** position.
   - Remove **JP2**.

#. Connect the **SDP-I-PMOD** interposer to the PMOD header (**P2**) on the
   EVAL-ADMX100X-FMCZ board using the 6-pin PMOD cable. Connect the male end to
   the top row (pins 1–6) of the PMOD connector, aligning pin 1 of the cable
   with pin 1 of the connector. Connect the female end to the bottom row of
   **P2**.
#. Connect the **SDP-S** or **SDP-B** controller to the SDP-I-PMOD interposer.
#. Connect the SDP controller USB cable to the host PC.
#. Apply power to the SDP-S or SDP-B using the 6 V power adapter. Wait 10
   seconds for the controller to initialize.
#. Apply power to the EVAL-ADMX100X-FMCZ board using the 12 V wall adapter.
#. Set **S1** to **Loopback Off**.
#. Launch the **ADMX100X GUI** on the host PC.

.. note::

   The SDP-S and SDP-B with SDP-I-PMOD do not support the ADMX1001 acquisition
   channel. Use the SDP-H1 for full ADMX1001 functionality.
