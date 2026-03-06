AD-FMCOMMS2-EBZ Hardware
========================

| 

Schematics, PCB Layout, Bill of Materials
-----------------------------------------

.. admonition:: Download
   :class: download

   
   .. note::

      This is the latest and greatest Rev "E" of this board. Note that the Baluns on the Rev C board (T101-T104) are Johanson Technology's `2450BL15B050E <https://www.johansontechnology.com/datasheets/2450BL15B050/2450BL15B050.pdf>`__ 2.45 GHz Balun. This balun is rated for a operating frequency of 2400~2500 MHz. If you want to evaluate the part outside of this frequency range, an :doc:`alternative balun </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/configuration_options>` should be installed. The test results were taken using the Johanson Technology's 2450BL15B050E balun.

         

   
   :adi:`AD-FMCOMMS2-EBZ Design & Integration Files <media/en/reference-design-documentation/design-integration-files/ad-fmcomms2-ebz-designsupport.zip>`
   
   -  Schematic
   -  PCB Layout
   -  Bill of Materials
   
      -  The Epson crystal used on this board, has the generic part number "TSX-3225 40.0000MHZ" - however, the generic part number does not have the specifications needed to meet the AD9361 datasheet specs. ADI has worked with Epson to provide a tighter tolerance part, which can be ordered as the "OUTD-2B-0166" or "X1E000021036701" (either part number will work, depending on which system your Epson contact/distributor has) which meets the requirements that the AD9361 demands.
   
   -  Allegro Project (Get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`__; you need 16.5 or higher).
   


I/O Voltage
-----------

The AD-FMComms2 (AD9361) assumes a VDD_INTERFACE voltage between 1.71V and 2.625V (1.8 to 2.5 +/- 5%), so on your FPGA carrier board, you should ensure that V\ :sub:`ADJ` is between these levels. Setting things to 3.3V will damage the part.

Picture and Main components
---------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/fmcomms2_locations.png
   :width: 600px

Outline
-------

For those that don't want to load up the Allegro viewer, here is a basic outline/component placements of the board. While this board does meet parts of the VITA-57.1 (FMC) specifications, there are many things it violates, and is **not** designed to be a form/fit/function board.

-  The FMC cutout for the bezel is missing (so we could space the SMA connectors out as far as possible, and achieve maximum isolation between the channels.
-   The mounting holes near the end of the board with the connectors is also in the wrong place (so it didn't effect the RF path between the connectors and the AD9361.
-  The FMC height specification on the top side of the board is violated to put some 90 degree SMA connectors.

|fmcomms2c_bottom_layout.png| |fmcomms2c_top_layout.png|

Size
----

The size of the board (not including the SMA connectors, which project beyond the edge of the board) is 73.3mm x 69mm. This is under the FMC specifications of 84mm x 69mm). The mounting holes are not compliant with the FMC standard, and are shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/fmcomms2c_dimensions.png
   :width: 500px

Layers
------

The AD-FMCOMMS2-EBZ is a 10 layer board.

Design Cross Section

+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
| Subclass Name | Type       | Material | Thickness (MIL) | Conductivity (mho/cm) | Dielectric Constant | Loss Tangent | Shield | Width (MIL) |
+===============+============+==========+=================+=======================+=====================+==============+========+=============+
|               | SURFACE    | AIR      |                 | 0                     | 1                   | 0            |        |             |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
| TOP           | CONDUCTOR  | COPPER   | 2.025           | 595900                | 1                   | 0            |        | 8.00        |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
|               | DIELECTRIC | FR-4     | 8               | 0                     | 3.38                | 0.035        |        |             |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
| L2_GND        | PLANE      | COPPER   | 1.35            | 595900                | 1                   | 0.035        | Y      |             |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
|               | DIELECTRIC | BT_EPOXY | 3               | 0                     | 4.10                | 0.02         |        |             |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
| L3_PWR        | PLANE      | COPPER   | 1.35            | 595900                | 1                   | 0.035        | Y      |             |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
|               | DIELECTRIC | FR-4     | 3               | 0                     | 4.10                | 0.035        |        |             |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
| L4_GND        | PLANE      | COPPER   | 1.35            | 595900                | 1                   | 0.035        | Y      |             |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
|               | DIELECTRIC | BT_EPOXY | 4.60            | 0                     | 4.10                | 0.02         |        |             |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
| L5_SIG        | CONDUCTOR  | COPPER   | 1.35            | 595900                | 1                   | 0.035        |        | 3.80        |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
|               | DIELECTRIC | FR-4     | 8               | 0                     | 4.10                | 0.035        |        |             |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
| L6_SIG        | CONDUCTOR  | COPPER   | 1.35            | 595900                | 1                   | 0.035        |        | 3.80        |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
|               | DIELECTRIC | BT_EPOXY | 4.60            | 0                     | 4.10                | 0.02         |        |             |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
| L7_GND        | PLANE      | COPPER   | 1.35            | 595900                | 1                   | 0.035        | Y      |             |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
|               | DIELECTRIC | FR-4     | 3               | 0                     | 4.10                | 0.035        |        |             |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
| L8_PWR        | PLANE      | COPPER   | 1.35            | 595900                | 1                   | 0.035        | Y      |             |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
|               | DIELECTRIC | BT_EPOXY | 3               | 0                     | 4.10                | 0.02         |        |             |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
| L9_GND        | PLANE      | COPPER   | 1.35            | 595900                | 1                   | 0.035        | Y      |             |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
|               | DIELECTRIC | FR-4     | 8               | 0                     | 3.38                | 0.035        |        |             |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
| BOTTOM        | CONDUCTOR  | COPPER   | 2.025           | 595900                | 1                   | 0            |        | 8.00        |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+
|               | SURFACE    | AIR      |                 | 0                     | 1                   | 0            |        |             |
+---------------+------------+----------+-----------------+-----------------------+---------------------+--------------+--------+-------------+

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/fmcomms2c_layers.png
   :width: 600px

.. |fmcomms2c_bottom_layout.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/fmcomms2c_bottom_layout.png
   :width: 400px
.. |fmcomms2c_top_layout.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/fmcomms2c_top_layout.png
   :width: 435px
