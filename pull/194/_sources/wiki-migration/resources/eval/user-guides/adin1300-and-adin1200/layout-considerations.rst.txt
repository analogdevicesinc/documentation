ADIN1300 and ADIN1200 Layout Considerations
===========================================

The ADIN1300 and ADIN1200 need specific layout guidelines and hardware considerations for designing a physical layer device. This user guide will cover details on the ADIN1300 and ADIN1200 layout recommendations. The sections within this user guide provide a high-level overview, and the document must be used in conjunction with the ADIN1200/1200 datasheets and additional apps notes found through the ADIN1200 and ADIN1300 product pages.

Layout Considerations
---------------------

This section is an overview of the key areas of interest during placement and layout of the PHY and corresponding support components. Take care when routing high speed interface signals to maximize signal performance and ensure optimum EMC performance, with a view to ensure critical signal traces are kept as short as possible to minimize noise coupling.

PHY Package Layout
~~~~~~~~~~~~~~~~~~

The LFCSP has an exposed pad underneath the package that must be soldered to the PCB ground for mechanical and thermal reasons. For thermal impedance performance and to maximize heat removal, use of a 4 × 4 array of thermal vias beneath the exposed ground pad is recommended.

There are also two bus bars on either side of the exposed pad, these bus bars are connected to internal voltage rails and are not intended or required to be soldered to the board. The PCB land pattern must incorporate the exposed ground paddle with vias and two keep out areas around the bus bars in the footprint. No PCB traces or vias can be used in either of the keep out areas. The EVAL-ADIN1300FMCZ uses an array of 4 × 4 vias on a 0.75 mm grid arrangement, as shown below. The via pad diameter dimension is 0.02 in. (0.5015 mm) and the finished drill hole diameter is 0.01 in. (0.2489 mm).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/adin1300_exposed_paddle_and_keepout.png
   :align: center

Component Placement
~~~~~~~~~~~~~~~~~~~

Prioritization of the critical traces and components helps simplify the routing exercise. Place and orient the critical traces and components first to ensure an effective layout with minimal turns, vias, and crossing traces. For an Ethernet PHY layout, the important components are the crystal and load capacitors, the transformer on the MDI lines, and all bypass capacitors local to the device. Prioritize these components and the routing to them. Keep the PHY chip at least 1 in. away from the edge of the board. The following sections provide more detail for each of the areas.

MDI Lines
~~~~~~~~~

The MDI interface runs from the ADIN1300 PHY to the transformer, and from there to the RJ45 connector. Traces running from the MDI_x_x pins of the ADIN1300 to the magnetics must be on the same side of the board, kept as short as possible (ideally less than 1 inch in length), but more importantly they should be length matched, for the MDI traces, the intra differential pairs these should be length matched within 20 mils for 1G operation and within 50 mils for 100M or 10M operation. The inter differential pairs are not as critical and should be length matched as close as possible, but within 1000 mils. The individual trace impedance of these tracks kept below 50 Ω, with differential impedance of 100 Ω for each pair. The same recommendations apply for traces running from the magnetics to the RJ45 connector. Keep impedances constant throughout because any discontinuities may affect signal integrity.

Each pair must be routed together, trace widths kept the same throughout, trace lengths kept equal where possible, and avoid any right angles on these traces (use curves in traces or 45° angles). Avoid stubs on all signal traces. Where possible, route traces on the same layer. By taking these guidelines into account the difference in latency between each pair is minimized and this will also help in avoiding an increase in common mode noise.

Route traces over a continuous reference plane with no interruptions to reduce inductance.

Where possible, ensure a solid return path underneath all signal traces. Avoid routing signal traces across plane splits.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/adin1300_stubs_and_plane_crossing_graphic.png
   :align: center

MAC Interface Pins
~~~~~~~~~~~~~~~~~~

All signals within TX group should be length matched, similarly for all signals within RX group. Where possible route these interface pins on the same side as component pins. Keep trace lengths as short as possible. Route traces with an impedance of 50 Ω to ground.

The ADIN1300 has the capability to program the drive current of the RGMII pins to help improve signal integrity and minimize ringing. Alternatively, series termination resistors can be placed in all RGMII output pins if further tuning is required.

Crystal Oscillator
~~~~~~~~~~~~~~~~~~

To ensure minimum current consumption and to minimize stray capacitances, make connections between the crystal, capacitors, and ground as close to the ADIN1300 as possible and preferably on the same side as the ADIN1300 device. Caps should be tuned to adjust for pin capacitance and trace capacitance.

Power and Ground Planes
~~~~~~~~~~~~~~~~~~~~~~~

From a PCB layout point of view, it is important to place the decoupling capacitors as close as possible to the power and GND pins to minimize the inductance.

Magnetics Module Grounding
~~~~~~~~~~~~~~~~~~~~~~~~~~

A split ground plane under the transformer minimizes noise coupling across the transformer and between adjacent coils within. Ensure a physical separation of the ground planes underneath the transformer. Make the width of this separation at least 100 mil.

Transformer Layout
~~~~~~~~~~~~~~~~~~

No metal layers can be directly underneath the transformer to minimize any noise coupling across the transformer.

RJ45 Module Grounding
~~~~~~~~~~~~~~~~~~~~~

For optimal EMC performance, it is recommended to use a metal shielded RJ45 connector with the shield connected to chassis ground. There must be an isolation gap between the chassis ground and the PHY IC ground with consistent isolation across all layers.

Placement of TVS
~~~~~~~~~~~~~~~~

It is recommended to place the TVS diode close to the ADIN1300 device to ensure minimal track inductance between the external protection and internal protection within the device.

Thermal Considerations
~~~~~~~~~~~~~~~~~~~~~~

The ADIN1300 is packaged in an LFCSP package. This package is designed with an exposed paddle which must be soldered to the PCB for mechanical and thermal reasons. The exposed paddle acts to conduct heat away from the package and into the PCB. By incorporating an array of thermal vias in the PCB thermal paddle, heat is dissipated more effectively into the inner metal layers of the PCB. When designing the PCB layout for optimum thermal performance, use a 4 mm × 4 mm array of vias under the paddle. This LFCSP device includes two exposed power bars adjacent to the exposed pad at the top and bottom. These bars are connected to internal power rails and the area around them is a keep out zone. Keep these areas clear of traces or vias.
