.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



| 
| :doc:`ezLINX™ iCoupler® Isolated Interface Development Platform Homepage </wiki-migration/resources/eval/ezlinx>`

ezLINX Hardware Configuration
=============================

| A list of jumper configurations for setting up the various interfaces on the *ez*\ LINX development platform is given below:

+-----------------+--------------------------------------------------------------------+------------------------------------------------+------------------------------------------------+
| Interface       | Configuration                                                      | Jumpers Fitted                                 | Jumpers Open                                   |
+-----------------+--------------------------------------------------------------------+------------------------------------------------+------------------------------------------------+
| RS-485 / RS-422 | Half-Duplex Configuration                                          | JP3, JP4, JP40                                 | Not applicable                                 |
+-----------------+--------------------------------------------------------------------+------------------------------------------------+------------------------------------------------+
|                 | Full-Duplex Configuration                                          | Not applicable                                 | JP3, JP4, JP40                                 |
+-----------------+--------------------------------------------------------------------+------------------------------------------------+------------------------------------------------+
|                 | 120Ω termination                                                   | JP19                                           | Not applicable                                 |
+-----------------+--------------------------------------------------------------------+------------------------------------------------+------------------------------------------------+
| RS - 232        | Loopback Tout1 to Rin1                                             | JP2                                            | Not applicable                                 |
+-----------------+--------------------------------------------------------------------+------------------------------------------------+------------------------------------------------+
| CAN             | Split terminate the bus with 120Ω and a common-mode 47nF capacitor | JP17, JP18                                     | Not applicable                                 |
+-----------------+--------------------------------------------------------------------+------------------------------------------------+------------------------------------------------+
| SPI0            | Master Mode                                                        | JP5, JP7, JP9, JP11, JP13, JP15, JP20, JP36    | JP6, JP8, JP10, JP12, JP14, JP16, JP21, JP37   |
+-----------------+--------------------------------------------------------------------+------------------------------------------------+------------------------------------------------+
|                 | Slave Mode                                                         | JP6, JP8, JP10, JP12, JP14, JP16, JP21, JP37   | JP5, JP7, JP9, JP11, JP13, JP15, JP20, JP36    |
+-----------------+--------------------------------------------------------------------+------------------------------------------------+------------------------------------------------+
| SPI2            | Master Mode                                                        | JP22, JP24, JP26, JP28, JP30, JP32, JP35, JP38 | JP23, JP25, JP27, JP29, JP31, JP33, JP34, JP39 |
+-----------------+--------------------------------------------------------------------+------------------------------------------------+------------------------------------------------+
|                 | Slave Mode                                                         | JP23, JP25, JP27, JP29, JP31, JP33, JP34, JP39 | JP22, JP24, JP26, JP28, JP30, JP32, JP35, JP38 |
+-----------------+--------------------------------------------------------------------+------------------------------------------------+------------------------------------------------+

| 
| For more information on each interface and jumper settings chose from the list below:

-  :doc:`Isolated USB </wiki-migration/resources/eval/ezlinx/isolated-usb>`
-  :doc:`Isolated CAN </wiki-migration/resources/eval/ezlinx/isolated-can>`
-  :doc:`Isolated RS-485/RS-422 </wiki-migration/resources/eval/ezlinx/isolated-rs485-rs422>`
-  :doc:`Isolated RS-232 </wiki-migration/resources/eval/ezlinx/isolated-rs232>`
-  :doc:`Isolated I2C </wiki-migration/resources/eval/ezlinx/isolated-i2c>`
-  :doc:`Isolated SPI </wiki-migration/resources/eval/ezlinx/isolated-spi>`
-  :doc:`Isolated LVDS </wiki-migration/resources/eval/ezlinx/isolated-lvds>`
