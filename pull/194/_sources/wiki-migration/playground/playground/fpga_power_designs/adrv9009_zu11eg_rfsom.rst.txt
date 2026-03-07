====== ==================================
Type   |image1| Application Board
====== ==================================
Status <fc #00ff00>✔</fc> Fully Validated
====== ==================================

|image2| The :adi:`ADRV9009-ZU11EG` is a highly integrated RF System-On-Module(RF-SOM) based on the Analog Devices ADRV9009 and `Xilinx Zynq UltraScale+ MPSoC <https://www.xilinx.com//products/silicon-devices/soc/zynq-ultrascale-mpsoc.html>`_. For more information on the RF-SOM, please see the :doc:`ADRV9009-ZU11EG Documentation </wiki-migration/resources/eval/user-guides/adrv9009-zu11eg>`.

The power tree consists of... Power rails are sequenced by the :adi:`ADM1266` sequencer/supervisor.

Power Tree
==========

|image3| |image4|

Support Files
=============

LTpowerCAD

`ADM1266 ADI Power Studio Project <https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009-zu11eg/adrv9009-zu11eg_adm1266_v0.1.ssp.zip>`_

ADI Parts Used
==============

+----------------------+---------------------------------------------------------------+--------------------------------------------------------------------+
| Rail/Function        | Part Number                                                   | Description                                                        |
+======================+===============================================================+====================================================================+
| Sequencer/Supervisor | :adi:`ADM1266 <en/products/adm1266.html>`                     | Cascadable Super Sequencer with Margin Control and Fault Recording |
+----------------------+---------------------------------------------------------------+--------------------------------------------------------------------+

.. |image1| image:: https://wiki.analog.com/_media/playground/playground/fpga_power_designs/app.png
   :width: 32px
.. |image2| image:: https://wiki.analog.com/_media/playground/playground/fpga_power_designs/adrv9009-zu11egbottom-web.png
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/playground/playground/fpga_power_designs/adrv9009-zu11eg-1.png
   :width: 0px
   :height: 200px
.. |image4| image:: https://wiki.analog.com/_media/playground/playground/fpga_power_designs/adrv9009-zu11eg-2.png
   :width: 0px
   :height: 200px
