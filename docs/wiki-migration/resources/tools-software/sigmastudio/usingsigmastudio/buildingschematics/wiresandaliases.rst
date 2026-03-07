Wires and Aliases
=================

| :doc:`Click here to return to the Building Schematics page </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics>`
| SigmaStudio schematic design are built from blocks which are connected together with "wires". Wires define the systems's signal flow.

| **To create a schematic wire:** Move the mouse cursor over a block's :doc:`pin </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/schematicblocks>` so the wire icon,\ |icon.png| ,is displayed. Next, Left-click on a block pin, and while holding the mouse button, drag the cursor to another blocks's corresponding pin. Input pins can only connect to Output pins and Output pins can only connect to Input pins.
| |wirespic1.png|

**Selecting:**

| To select a wire, click on it with the left mouse button. Selected wires are indicated by green squares (points) as shown below.
| |wirespic2.png|
| **Position:**

| To change the position of a wire, place the mouse cursor over a point. Next, **Left-click** on the wire point, and while holding the mouse button, drag the cursor to reposition the wire.
| |wirespic3.png|
| **Menu:**

| Right-click on a wire to bring up the wire menu. This menu includes following commands:
| |wirespic4.png|

**Wire colors:**

| Wires are colored according to their associated DSP processor. The input and output pins of the wire must be associated with the same DSP or you will not be able to create a wire between the pins. Projects with more than one processor IC will have distinct colors for each IC.
| |wirespic5.png|

--------------

**Alias:**

To organize your project visually, it often helps to create an alias to provide a clear connective reference (a "jump") in the signal flow in the schematic. An **Alias** consists of a pair of alias input and alias output blocks. Using alias blocks can reduce the visual clutter in the schematic window created by long wire connections.

| To create an alias, **Right-Click** on a block's output pin (blue pin) and select **Alias** from the menu.
| |wirespic6.png|

| When you click **Alias**, two blocks appear, input and output. The alias input is automatically connected to source block's output pin. Next, create a wire from the alias output block (Alias 2 in the example below) to the signal destination.
| |wirespic7.png|
|

.. hint::

   Note: Using an alias is functionally equivalent to connecting two pins with a wire. The signal flow in the example below is identical to the alias example above.


.. image:: https://wiki.analog.com/_media/wirespic8.png
   :alt: wirespic8.png
   :align: center

.. |icon.png| image:: https://wiki.analog.com/_media/icon.png
.. |wirespic1.png| image:: https://wiki.analog.com/_media/wirespic1.png
.. |wirespic2.png| image:: https://wiki.analog.com/_media/wirespic2.png
.. |wirespic3.png| image:: https://wiki.analog.com/_media/wirespic3.png
.. |wirespic4.png| image:: https://wiki.analog.com/_media/wirespic4.png
.. |wirespic5.png| image:: https://wiki.analog.com/_media/wirespic5.png
.. |wirespic6.png| image:: https://wiki.analog.com/_media/wirespic6.png
.. |wirespic7.png| image:: https://wiki.analog.com/_media/wirespic7.png
