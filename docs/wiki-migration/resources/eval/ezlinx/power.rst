| 
| :doc:`ezLINX™ iCoupler® Isolated Interface Development Environment Homepage </wiki-migration/resources/eval/ezlinx>`
| ====== ezLINX™ Power Supply Implementation ======

Power Input
===========

An AC/DC desktop power supply is used to supply 7.5V input to the barrel connector J1 on the *ez*\ LINX hardware. This supply connects through a protection circuit as shown in Figure 1 below to the UNREG_IN node of the circuit.

.. image:: https://wiki.analog.com/_media/ezlinx/powerinput.png
   :alt: Figure 1.
   :align: center
   :width: 500px

3.3V Power Supply
=================

The ADP1864 Constant Frequency Current-Mode Step-Down DC-to-DC Controller is used with an external P-Channel Mosfet to generate the regulated 3.3V Power Supply for the *ez*\ LINX hardware. The circuit implementation of the 3.3V power supply is shown in below in Figure 2.

.. image:: https://wiki.analog.com/_media/ezlinx/3-3vsupply.png
   :alt: Figure 2.
   :align: center
   :width: 500px

1.2V, 2.5V and 5V Power Supplies
================================

A P-Channel mosfet is used to regulate the 3.3V input to 1.2V, See Figure 3 below.

.. image:: https://wiki.analog.com/_media/ezlinx/1-2vsupply.png
   :alt: Figure 3.
   :align: center
   :width: 500px

The :adi:`ADP1706 <en/power-management/linear-regulators/adp1706/products/product.html>` Linear regulator is used to regulate the 3.3V input to 2.5V, See Figure 4 below.

.. image:: https://wiki.analog.com/_media/ezlinx/2-5vsupply.png
   :alt: Figure 4.
   :align: center
   :width: 500px

The :adi:`ADP3335 <en/power-management/linear-regulators/adp3335/products/product.html?ref=ASC-PR-283>` low dropout regulator is used to regulate the UNREG_IN input to 5V, See Figure 5 below.

.. image:: https://wiki.analog.com/_media/ezlinx/power-5v.jpg
   :alt: Figure 5.
   :align: center
   :width: 500px
