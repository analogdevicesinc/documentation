ADALM-UARTJTAG hardware
=======================

Analog Devices provides a small adapter board `(ADALM-UARTJTAG) <https://wiki.analog.com/../uartjtag>`_ to be used for JTAG and UART, in order to make that easier for programming and debugging. You are encouraged to use this on your designs for the same reason we do - the standard JTAG connector is huge, and there are times where good old fashion console UART is valuable for doing debug. The 1.8V supply on the connector above is the I/O voltage, and can be used anywhere between 1.8V and 3.3V.

In the box, you should have received the UARTJTAG board, ribbon cable, jumper, and `Samtec FTSH-105-01-L-D 10 <https://www.samtec.com/products/ftsh>`_ position dual row 0.05" through hole pin connector.

.. image:: https://wiki.analog.com/_media/university/tools/jtaguart/adalm-uartjtag.png
   :align: center
   :width: 400px

The PCB includes a jumper, which forces the Zynq to HALT on JTAG. This is great for halting, and not allowing anything to run, but does does pull down a chip select for SPI flash, and will not allow the SPI flash to be found by the on chip bootloader, or by U-Boot. (If you are loading a U-Boot over JTAG).

The pin connector is likely inserted into the ribbon cable:

|3| |4|

but can be removed, and either soldered to the PCB, or left in the ribbon cable, so you don't loose it.

.. image:: https://wiki.analog.com/_media/university/tools/jtaguart/uartjtagcable.png
   :alt: 2
   :width: 300px

If you do want more, they can be obtained from `Samtec <https://www.samtec.com/products/ftsh-105-01-l-d>`_, `Digikey <https://www.digikey.com/SAM10499-ND>`_ or `Arrow <https://www.arrow.com/en/products/ftsh-105-01-l-d/samtec>`_.

Downloads
=========

.. admonition:: Download
   :class: download

   
   -  `Rev A Schematics <https://wiki.analog.com/_media/university/tools/jtaguart/adalm-jtaguart.pdf>`_
   -  `Rev A Gerbers <https://wiki.analog.com/_media/university/tools/jtaguart/adalm-jtaguart_fab.zip>`_ (This file is `compressed <http://www.7-zip.org/7z.html>`_)
   -  `Rev A Bill of materials <https://wiki.analog.com/_media/university/tools/jtaguart/adalm-jtaguart.xlsx>`_
   -  `Rev A Allegro Board File <https://wiki.analog.com/_media/university/tools/jtaguart/adalm-jtaguart_brd.zip>`_ (This file is `compressed <http://www.7-zip.org/7z.html>`_). Get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`_ to view.
   


.. admonition:: Download
   :class: download

   
   -  {{\|Rev B Schematics}}
   -  {{\|Rev B Gerbers}} (This file is `compressed <http://www.7-zip.org/7z.html>`_)
   -  {{\|Rev B Bill of materials}}
   -  {{\|Rev B Allegro Board File}} (This file is `compressed <http://www.7-zip.org/7z.html>`_). Get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`_ to view.
   


.. |3| image:: https://wiki.analog.com/_media/university/tools/jtaguart/uartjtagcablepluspins2.png
   :width: 300px
.. |4| image:: https://wiki.analog.com/_media/university/tools/jtaguart/uartjtagcablepluspins.png
   :width: 200px
