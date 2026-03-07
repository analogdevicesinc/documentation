Layout Considerations for AD-PZSDR2400TDD-EB boards
===================================================

The :adi:`ADL5324` has several passive components surrounding the IC which directly influence the tuning frequency of the device. The location of these capacitors is critical to the accurate determination of the tuning frequency.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pzsdr2400tdd-ebz/tuning_component_placement.png
   :align: center
   :width: 800px

The component spacing for tuning capacitors C1 and C2 is detailed in the ][adi>ADL5324]] datasheet over a variety of frequencies. A table from the datasheet, detailing this information, is listed below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pzsdr2400tdd-ebz/tuning_component_table.png
   :align: center
   :width: 800px

Placement of the AC coupling capacitors, power supply bypassing capacitors and DC bias inductor should follow the recommendation of the datasheet, but are slightly less critical than the tuning capacitors.

.. image:: https://wiki.analog.com/_media/navigation AD-PZSDR2400TDD-EBZ#Characteristics and Performance#./
   :alt: Hardware#FCC or CE Certification
