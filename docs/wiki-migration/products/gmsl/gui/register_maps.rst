GMSL GUI Register Maps
======================

| One of the more commonly used features of the GMSL GUI is the ability to read and write to all of the registers without the need of processor.
| |image1|
| Everything regarding the serializer tab will be the same on the deserializer tab, just a difference in registers.

--------------

.. container:: group

   
   .. container:: half column

      This section contains all of the registers in numerical order and grouped by function.

   
   .. container:: half column


   
   |image2|

--------------

|

.. container:: group

   
   .. container:: half column

      This section contains handful of features for manipulating the register values.

         | Starting at the top-left and working clockwise, the "Hex Value (0x)" box is used for writing to or reading from a register. Placing a hex value in there and then clicking the "**Write Register**" button will put that value in the register. Clicking the "**Read Register**" button will place the current value of the register in this box.
         | The box to the right of this is the "Hex Reset Value (0x)" which indicates the default value of the register after reset.
         | Beneath all the buttons are the individual bits of the register. The check box next to each bit indicates if the bit is set or cleared. When you clear or set a bit, the value in the "Hex Value (0x)" box will change accordingly which is convenient when converting back and forth between hexadecimal and binary.
      | Lastly, is the "Read Selected Registers" dropdown. This dropdown has multiple options to read some or all of the registers to a \*.txt or \*.csv file. This is very helpful when debugging and sharing register settings.

   
   .. container:: half column


   
   |image3|

--------------

.. container:: group

   
   .. container:: half column

      This section contains all of the register bit-field descriptions. It also breaks out the sub-groups of bits for easier interpretation and bitwise manipulation.

   
   .. container:: half column


   
   |image4|

--------------

.. container:: group

   
   .. container:: half column

      This section logs all the communication to the specific device tab that you are on. So only communication to the serializer (in this case) would be seen in this log window.

   
   .. container:: half column


   
   |image5|

.. |image1| image:: https://wiki.analog.com/_media/products/gmsl/gui/screenshot_2024-02-26_131603.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/products/gmsl/gui/registers.png
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/products/gmsl/gui/bits.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/products/gmsl/gui/descriptions.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/products/gmsl/gui/log.png
   :width: 300px
