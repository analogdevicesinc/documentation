| 
| :doc:`ezLINX™ iCoupler® Isolated Interface Development Environment Homepage </wiki-migration/resources/eval/ezlinx>`
| ====== ezLINX™ Isolated LVDS Implementation======

The Isolated LVDS port is implemented using the :adi:`adum3442` *i*\ Coupler signal isolator, the :adi:`adn4664` dual LVDS receiver, the :adi:`adn4663` dual LVDS transmitter and the :adi:`adum5000` *iso*\ Power Isolated DC to DC converter. The :adi:`adum3442` is connected to SPORT2 of the ADSP-BF548. Figure 1 below shows a circuit diagram of the implementation of Isolated LVDS using the :adi:`adum3442`, :adi:`adn4663`, :adi:`adn4664` and :adi:`adum5000` on the *ez*\ LINX hardware.

.. image:: https://wiki.analog.com/_media/ezlinx/isolatedlvds.png
   :alt: Figure 1. Isolated LVDS Implementation
   :align: center
   :width: 900px

VDD1 of the ADuM3442, and VDD1 of the ADuM5000 are powered by 3.3V. The ADuM5000 will generate an isolated 3.3V and is used to supply power to VDD2 of the\ :adi:`adum3442`, VCC of the :adi:`adn4663` and the :adi:`adn4664`.

A 32 pin header connector is used for easy access to the Isolated LVDS signals.
