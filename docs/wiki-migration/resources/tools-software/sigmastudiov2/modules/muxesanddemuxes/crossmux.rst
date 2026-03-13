:doc:`Click here to return to the Multiplexers and Demultiplexers page </wiki-migration/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes>`

Cross Mux
=========

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes/crossmux.png
   :alt: crossmux.png

Description
-----------

The Cross Mux block allows route an input to one of selected output pins. The
output for each input is selected based on the numeric value on the control.

Targets Supported
-----------------

========= ========== ================ ============= ================
Name      ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
========= ========== ================ ============= ================
Cross Mux B          B                NA            B
========= ========== ================ ============= ================

| ===== Pins =====

Input
~~~~~

====== ===== ===============
Name   Type  Description
====== ===== ===============
InputX Audio Input Channel X
====== ===== ===============

Output
~~~~~~

======= ===== ================
Name    Type  Description
======= ===== ================
OutputX Audio Output Channel X
======= ===== ================

Note:

-  X - Channel Index

Configurable Parameters
-----------------------

+----------------+---------------+------------------+------------------------------------------------------------------------+
| GUI Parameter  | Default Value | Range            | Function Description                                                   |
+================+===============+==================+========================================================================+
| Index_ChannelX | 0             | 0 to NumOuputs-1 | Selects the output channel to route the input                          |
+----------------+---------------+------------------+------------------------------------------------------------------------+
| NumInputs      | 1             | 1 to 20          | Number of input channels. Change in this value requires re-compilation |
+----------------+---------------+------------------+------------------------------------------------------------------------+
| NumOuputs      | 1             | 1 to 20          | Number of input channels. Change in this value requires re-compilation |
+----------------+---------------+------------------+------------------------------------------------------------------------+

Note:

-  X - Channel Index

DSP Parameters
--------------

+----------------+-----------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                   | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+===============================================+========================+===============+
| Index_ChannelX | Selects the output channel to route the input | Float                  | NA            |
+----------------+-----------------------------------------------+------------------------+---------------+

Note:

-  X - Channel Index
