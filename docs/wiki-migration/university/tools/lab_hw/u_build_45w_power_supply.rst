45W Benchtop Power Supply Project
=================================

Overview
--------

| You can never have too many power supplies. Well, that's a bit of an exaggeration - if you have so many power supplies that they displace so much oxygen in your lab that you can't breathe, you have too many. But you get the idea. Even though power supplies seem simple at first glance, they vary widely in their capabilities and intended applications. A well-equipped lab bench will have several commercial power supplies with several adjustable outputs, ideally with "lots of" current capability AND adjustable current limit. And while most of the time it does not make sense to try to make your own test equipment - like oscilloscopes, spectrum analyzers, network analyzers, etc., power supplies are an exception.
| In this tutorial, we will build a highly capable 45W power supply with an output voltage range of 1 to 16V, adjustable current limit from 0 to 3 amps. The topology is an LDO (linear) output stage with a buck preregulator, limiting the maximum power dissipation to about 7W.

|image1|

.. container:: centeralign

   Figure 1. Finished Supply with Heat Sink and USB-C power input


Materials
---------

-  TRIMMER 5K OHM 0.5W PC PIN TOP `Bourns 3386F-1-502TLF <https://www.bourns.com/docs/Product-Datasheets/3386.pdf>`_
-  TRIMMER 50K OHM 0.5W PC PIN TOP `Bourns3386F-1-503TLF <https://www.bourns.com/docs/Product-Datasheets/3386.pdf>`_
-  DIODE SCHOTTKY 35V 7.5A TO220AC `Vishay VS-MBR735-M3 <https://www.vishay.com/docs/96268/vs-mbr735-m3.pdf>`_
-  CAP ALUM 470UF 20% 35V RADIAL `Würth 860020575014 <https://www.we-online.com/katalog/datasheet/860020575014.pdf>`_
-  FIXED IND 10UH 5.1A 22 MOHM TH `Würth 7447471100 <https://www.we-online.com/katalog/datasheet/7447471100.pdf>`_
-  CONN BANANA JACK SOLDER `Keystone 575-4 <https://www.keyelco.com/userAssets/file/M65p111.pdf>`_
-  TRANS PNP 40V 0.2A TO92-3 `onsemi 2N3906BU <https://www.onsemi.com/pdf/datasheet/pzt3906-d.pdf>`_
-  DIODE GEN PURP 100V 200MA DO35 `onsemi 1N4148TR <https://www.onsemi.com/download/data-sheet/pdf/1n914-d.pdf>`_

Theory of Operation
-------------------

| :git-education_tools:`u_build_45w_power_supply LTspice simulation <experiment-boards/u_build_45w_ps/ltspice>`

Construction
------------

| :git-education_tools:`u_build_45w_power_supply Eagle PCB files <experiment-boards/u_build_45w_ps>`

Testing
-------

Conclusion
----------

.. |image1| image:: https://wiki.analog.com/_media/university/tools/lab_hw/u_build_45w_power_supply/u_build_45w_power_supply_top.jpg
   :width: 500px
