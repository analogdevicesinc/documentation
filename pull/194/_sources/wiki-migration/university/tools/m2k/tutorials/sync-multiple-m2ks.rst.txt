=======Using Multiple ADALM2000s Synchronised=======

By forwarding the trigger signal on one module’s TriggerOut(TO) pin, and reading it on another’s TriggerIn(TI) pin, one can obtain more synchronised channels of both analog and digital inputs. This can be achieved either with Scopy, as well as with libm2k. The following example will provide a description on how to make use of two ADALM2000 modules’ trigger features to have their analog and digital inputs synchronised.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/tutorials/2m2k.jpg
   :alt: 2m2k.jpg
   :width: 600px

Hardware Connections
====================

Analog Example
--------------

Both modules will read a test signal on their channel 1, respectively the trigger on channel 2. The trigger will be generated using DIO0 of the first ADALM2000. This is going to be transmitted to the second module by connecting its TriggerIn pin to the first’s TriggerOut Pin. You will have to make the connections shown in the diagram below. The connection between the TO and TI pins, highlighted with red, links the two devices' triggers, thus enabling them to acquire data in a synchronised manner.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/tutorials/2m2k_analog.png
   :alt: 2m2k_analog.png

Digital Example
---------------

Here, the trigger is also going to be generated on the first ADALM2000’s DIO0 pin and then forwarding it to the second’s trigger in. Both of the modules’ DIO1 pins will read the same generated waveform. To do this, connect the modules as shown below. Again, the connection which enables the two modules to acquire data simultaneously is the one between the TO and TI pins, highlighted with red.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/tutorials/2m2k_dig.png
   :alt: 2m2k_dig.png

Using Scopy
===========

In order to achieve this with Scopy, you’ll need to open a second instance of Scopy.

MacOS users: To be able to open multiple instances of Scopy, open a terminal widow and run the following command:

::

   open -n /path/to/application/Scopy.app

.. _analog-example-1:

Analog Example
--------------

Open Scopy and connect the first module. Click the button for the Digital I/O instrument and set DIO 0 to output.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/tutorials/2m2k_dio1.png
   :alt: 2m2k_dio1.png

Then go to the Oscilloscope and open the Trigger settings menu. Set the trigger mode to normal, channel 2 as source and the condition to Rising Edge.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/tutorials/2m2k_trig1.png
   :alt: 2m2k_trig1.png

Then configure the TriggerOut pin to forward the oscilloscope trigger. Click the single button when you’re done and you’ll see that the device is waiting for the trigger signal.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/tutorials/2m2k_trig1fw.png
   :alt: 2m2k_trig1fw.png

Let’s configure the second module now. Open the second instance of Scopy and go to the Oscilloscope instrument. Open the Trigger Settings menu and set the trigger mode to normal. Then disable the internal trigger and enable the digital one. Set the source to External Trigger In and the condition to rising edge. Once again, click the single button when you’re done.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/tutorials/2m2k_trig2.png
   :alt: 2m2k_trig2.png

Go back to the first instance of Scopy. Open the Signal Generator and generate a square waveform of 5 MHz on channel 1. Then, open the Digital I/O instrument and run it. Then set the state of DIO 0 to 1.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/tutorials/2m2k_dio2.png
   :alt: 2m2k_dio2.png

You’ll notice that both Oscilloscope instruments were triggered. In the image below, the superior half shows the analog inputs of the module whose trigger signal is being forwarded, while the inferior depicts the second ADALM2000. With the cursors enabled, a delay of approximately 190 nanoseconds is measured.

|2m2k_ainsync1.png| |2m2k_ainsync2.png|

.. _digital-example-1:

Digital Example
---------------

In the Digital I/O Instrument of the first instance of Scopy, keep the DIO0 pin as output and make sure its state is set to 0. Open the Logic Analyser instrument and enable pins: DIO0, DIO1. Set the trigger condition on DIO0 to rising edge.


|2m2k_digla1.png|

Then, go to the Oscilloscope’s Trigger settings menu. Here, select the Logic Analyser option for the External TriggerOut configuration.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/tutorials/2m2k_digtrig.png
   :alt: 2m2k_digtrig.png

In the second instance of Scopy, open the Logic Analyser instrument, and enable pins: DIO0 and DIO1. Go to the Trigger menu and set the mode to normal, the source to External Trigger In and the condition to rising edge.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/tutorials/2m2k_digtrig2.png
   :alt: 2m2k_digtrig2.png

Go to the Patter Generator of the first instance of Scopy and enable DIO7. Generate a clock signal of 5MHz on this pin. Go back to the Digital I/O instrument where we configured our trigger pin. Run the instrument and set the state of DIO0 to 1. Again, you’ll notice that both instruments have triggered. The figure below shows the instance of Scopy from where the trigger is being forwarded in the superior half, while under it the second one is displayed. |2m2k_digsync1.png|


|2m2k_digsync2.png|

If you’ll zoom in on the plot and enable the cursors in the second instance of Scopy, you’ll be able to measure the delay, as shown below.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/tutorials/2m2k_digsync3.png
   :alt: 2m2k_digsync3.png

Using Libm2k
============

.. _analog-example-2:

Analog Example
--------------

Maintaining the connections made when demonstrating the synchronisation of the analog inputs using Scopy, the same result can be achieved using the example Python libm2k :git-libm2k:`script <bindings/python/examples/analogin_sync_2m2ks.py>`. The script follows the exact steps shown in the Scopy section of this tutorial.

.. _digital-example-2:

Digital Example
---------------

As mentioned in the previous sub-section, keep the connections you made when you did this with Scopy and use the Python libm2k :git-libm2k:`script <bindings/python/examples/digitalin_sync_2m2ks.py>` provided with the library. This script also reproduces the steps shown in the Scopy section of this tutorial.

Adding More
~~~~~~~~~~~

This section offers instructions on how to add more modules to the chain of M2Ks. For example, you can forward the trigger from the second module to a third in the same manner: connect the second M2K’s TriggerOut pin to the third’s TriggerIn pin. If you want to use Scopy, you’ll need to open as many instances as the number of modules you want to use. On the other hand, if you want to use libm2k, you’ll also need to edit the example scripts, to comply with your desired configuration.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/tutorials/3m2k.jpg
   :alt: 3m2k.jpg

.. |2m2k_ainsync1.png| image:: https://wiki.analog.com/_media/university/tools/m2k/tutorials/2m2k_ainsync1.png
.. |2m2k_ainsync2.png| image:: https://wiki.analog.com/_media/university/tools/m2k/tutorials/2m2k_ainsync2.png
.. |2m2k_digla1.png| image:: https://wiki.analog.com/_media/university/tools/m2k/tutorials/2m2k_digla1.png
.. |2m2k_digsync1.png| image:: https://wiki.analog.com/_media/university/tools/m2k/tutorials/2m2k_digsync1.png
.. |2m2k_digsync2.png| image:: https://wiki.analog.com/_media/university/tools/m2k/tutorials/2m2k_digsync2.png
