SDP to FMC Interposer
=====================

Preface
-------

The SDP to FMC Interposer board is an adaptor that allows Xilinx FPGA Eval boards to connect to all daughter boards on the SDP Platform. SDP daughter boards are a wide range of component evaluation boards and Circuits from the Lab (TM) reference circuits. The SDP-I-FMC interposer provides the capabilities to prototype a Xilinx FPGA with an ADI data converter, mixed signal or RF system quickly and easily.

Links
-----

| SDP-I-FMC Schematic:
| `sdp-i-fmc_rev1.pdf <https://wiki.analog.com/_media/resources/eval/sdp/sdp-i-fmc_rev1.pdf>`_

Product Overview
----------------

| |image1|
| Fig 1 : SDP-I-FMC Intposer Board

The SDP to FMC Interposer routes signals from the FMC connector to the SDP daughter board. There is no additional logic on the board. There is a Low Pin Count (LPC) FMC connector on board. The SDP-I-FMC can only be used with FPGA evaluation boards that have 3.3VIO logic.

The complete setup is shown below:

-  KC705 Eval Board
-  SDP-I-FMC Interposer board
-  SDP daughter board

| |image2|
| Fig 2: Prototype system setup.

Sample Projects/Code
--------------------

Example Projects for the KC705 and a range of the SDP daughter boards, which show the basic connectivity between the KC705 and the ADI eval boards, are available on the link below :doc:`Xilinx Reference Designs </wiki-migration/resources/alliances/xilinx>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp_i_fmc.jpg
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/sdp/dscn0060_edited.jpg
   :width: 300px
