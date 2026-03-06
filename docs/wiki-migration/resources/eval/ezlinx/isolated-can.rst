| .. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.


| :doc:`ezLINX™ iCoupler® Isolated Interface Development Environment Homepage </wiki-migration/resources/eval/ezlinx>`

ezLINX™ Isolated CAN Implementation
===================================

The Isolated CAN port on the *ez*\ LINX Development Environment is implemented using the :adi:`ADM3053` Signal and Power Isolated CAN transceiver. The :adi:`ADM3053` connects to CAN0 of the ADSP-BF548 and is capable of functioning at data rates of up to 1Mbit/s. Figure 1 below is a circuit diagram of the implementation of the :adi:`ADM3053` on the *ez*\ LINX hardware.

.. image:: https://wiki.analog.com/_media/ezlinx/isolatedcan.png
   :alt: Figure 1.
   :align: center
   :width: 700px

The CAN Node can be configured using jumpers JP17 and JP18. When both jumpers JP17 and JP18 are fitted, the CAN node is split terminated with 120Ω and a common mode capacitor of 47nF. If termination is not required, remove JP17 and JP18. A list of jumper configurations for all the interfaces on *ez*\ LINX can be found :doc:`here </wiki-migration/resources/eval/ezlinx/config>`.

The 5V supply is connected to VCC (pin 8) to power the *iso*\ Power isolated Power supply of the :adi:`ADM3053`. This generates an isolated 5V on the Visoout pin (pin 12) of the ADM3053 and needs to is connected to the Visoin pin(pin 19). The 3.3V supply is connected to the VIO pin (pin 6) to power the *i*\ Coupler signal isolation, which needs to be compatible with the 3.3V logic of the Blackfin ADSP-BF548. The RS pin (pin 18) is connected through a 0Ω resistor to CAN_ISO_GND in order to de-activate slew rate limiting.

A four pin screw terminal connector, J8, is used for easy access to the CANH (Pin 1), CANL (Pin 3) and CAN_ISO_GND(Pin 2 and 4) connections. Application note :adi:`AN-1123 <static/imported-files/application_notes/AN-1123.pdf>` provides more information on implementing CAN Nodes.
