:doc:`Link to parent page </wiki-migration/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end>`

Power Architecture Overview
===========================

The power solution for the 2-24GHz Front End provides regulation for the four major functional blocks in the system: the transmit chain, the receive chain, the LO chains, and the :adi:`AD9081` or :adi:`AD9082` MxFE with clocking solution.

| The power for the transmit chain (shown below) features two switching regulators. One is the ultra-small :adi:`MAXM17632`, which delivers 1A at high efficiency from up to 36Vin in a tiny 3x3mm uSLICTM package. The other is the :adi:`ADP5600`, which integrates a low ripple interleaved inverting charge pump with a high performance LDO to easily produce clean negative voltages. The sensitive signal chain power domains are regulated by low noise, high performance linear regulators.
| |image1|

| 
| The power for the receive chain (shown below) follows a similar design philosophy as the transmit. It uses the same :adi:`MAXM17632` power module and highly integrated :adi:`ADP5600` to minimize the solution space. The sensitive power domains of the signal chain are regulated by low noise linear regulators.
| |image2|
| The power for the LO chains (shown below) utilize two :adi:`MAXM17632` power modules and the :adi:`ADP5600`. These are accompanied by low noise linear regulators for the sensitive signal chain power domains.
| |image3|
| The power solution for the MxFE and its clock (shown below) features Silent Switcher® technology. These high efficiency regulators, :adi:`LTM8051`, :adi:`LT8625S` and :adi:`LT8627S`, feature low EMI and output noise. Some power domains of the MxFE chip can be driven directly from a Silent Switcher® output, while the more sensitive ICs such as the :adi:`ADF4377` clock chip are further regulated by LDOs like the :adi:`LT3045`. The :adi:`LT3045` LDO features industry leading performance with 77dB PSRR at 1MHz.
| |image4|

| 
|

.. admonition:: Download
   :class: download

   To request the complete LTPowerPlanner design files for 2-24Ghz MxFE Front End, please send a request to `here <https://support.analog.com/en-US/technical-support/create-case-techsupport/>`_ and include the following info:


   | \* Name
   
   -  Job Title
   -  Company Name
   -  Company Location
   -  Application/Use Case
   
   |

   |


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/tx_power_tree.jpg
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/rx_power_tree.jpg
   :width: 800px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/LO_Power_Tree.jpg
   :width: 800px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/mxfe_clk_power_tree.jpg
   :width: 800px
