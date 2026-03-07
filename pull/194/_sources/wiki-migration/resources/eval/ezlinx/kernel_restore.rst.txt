| :doc:`ezLINX™ iCoupler® Isolated Interface Development Environment Homepage </wiki-migration/resources/eval/ezlinx>`

Kernel Restore Guide
====================

| Connect UART1 on the ezLINX® board to the PC using a RS-232 cable. Connect the ezLINX® board to the host PC using the supplied USB cable and to the power supply using the supplied AC adapter.

Factory Reset
-------------

-

.. container:: em

   Connected Mode


:

| Launch the PC application, connect to the ezLINX board, then Press the Reset button SW2 for the first time from the ezLINX board, as is shown in the following figure a message is displayed to inform that the factory reset is done by keep pressing the button (SW2) more than 20 seconds.
| |image1|

| After Keep pressing the SW2 button on the ezLINX board for 20 seconds, the Leds are flashing and a sequence of messages will be displayed in order to inform about the remaining time to the factory reset also to inform user that he should not remove the power. Exemples of message which are displayed : The first is to inform that 80 seconds are remained for factory Rest process.
| |image2|

| The second is to inform that 70 seconds are remained.
| |image3|

| The third, as it is shown in the figure below, is to tell that the factory reset is going to last 60 seconds.
| |image4|

| The fourth message is displayed in the following figure to inform that 50 seconds are remained.
| |image5|

| The last one shows 40 remaining seconds.

.. image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelrestoreguide/lastwarningmessage.jpg
   :align: center
   :width: 850px

| The board does not respond.
| |image6|

| The board now is Disconnected, the factory reset is successfully done.
| |image7|

-

.. container:: em

   Disconnected Mode


:

| Without using the PC application, Keep pressing the SW2 button on the ezLINX board for 20 seconds, until the Leds start flashing.
| Wait until these leds will be OFF and the bootup LED changes the status to ON.
| Now the factory reset is successfully done.

Connecting with HyperTerminal
-----------------------------

| Open up the HyperTerminal software:
| |image8|

| Type any name into the box and click "OK"
| |image9|

| In the drop down menu next to "Connect using:" select "COM1" and click "OK". In the following properties menu select the following values using the drop down menus:
| |image10|

| Click "Apply" then "OK".
| ===== Rebooting the Kernel ===== Press SW1 on the ezLINX board, this will start a countdown in the HyperTerminal window. Press the return key, this will stop the countdown:
| |image11|

| Type the following into the field:
| |image12|

| Hit the return key.
| ===== Factory Reset ===== After a brief period of time the PC will recognize that the ezLINX board is connected. Now press SW2 and the ezLINX board will start its factory reset:
| |image13|

After a brief period of time the board will reconnect with the PC. The kernel has been restored to its default settings and the IP address of the board has returned to its default (192.168.1.21).

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelrestoreguide/factoryresetinformationmessage.jpg
   :width: 850px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelrestoreguide/firstwarningmessage.jpg
   :width: 850px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelrestoreguide/secondwarningmessage.jpg
   :width: 850px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelrestoreguide/thirdwarningmessage.jpg
   :width: 850px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelrestoreguide/fourthwarningmessage.jpg
   :width: 850px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelrestoreguide/boardstatus.jpg
   :width: 850px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelrestoreguide/boarddisconnected.jpg
   :width: 850px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelrestoreguide/newhyperterminalconnection.jpg
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelrestoreguide/comselection.jpg
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelrestoreguide/comproperties.jpg
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelrestoreguide/rebootingstep1.jpg
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelrestoreguide/rebootingstep2.jpg
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelrestoreguide/FactoryReset.jpg
   :width: 600px
