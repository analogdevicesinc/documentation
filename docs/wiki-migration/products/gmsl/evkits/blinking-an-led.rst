Blinking an LED
===============

With the EV kit connected to your computer, we can do a simple configuration to make use of the onboard LED.

All of the EV kits have an LED used to indicate link lock, or that the two GMSL PHYs are locked to each other. The LED is tied to the LOCK pin which is one function of the pin, so we can configure it as a GPIO and toggle the LED with some register writes.

Finding the MFP Number
----------------------

Every IC has LOCK indication on the multi-function pin (MFP). On the MAX96717, it is located on MFP3.

.. image:: https://wiki.analog.com/_media/products/gmsl/evkits/max96717_mfp3.png
   :align: center
   :width: 600px

MFP3 is also GPIO3, ADC0, ERRB, and VTG3 but for this exercise, we are only concerned with GPIO3.

Cross-Referencing the EV Kit
----------------------------

Now that we've identified the correct pin to program, we can refer to the schematic to see how this is connected. In the EV kit datasheet, we can see MFP3 is connected to two LEDs used to indicate ERRB or LOCK.

.. image:: https://wiki.analog.com/_media/products/gmsl/evkits/mfp3_schem.png
   :align: center
   :width: 600px

Then referring to the EV kit, we can see the two LEDs referenced.

.. image:: https://wiki.analog.com/_media/products/gmsl/evkits/evk_leds.png
   :align: center
   :width: 600px

Using the GMSL GUI to Toggle the MFP
------------------------------------

With the LED's physical location identified and the GPIO number identified, we can utilize the GMSL GUI to toggle the pin.

Using the search register feature, enter ``GPIO3`` into the search box and the GUI will search for and navigate to the register for GPIO3.

.. image:: https://wiki.analog.com/_media/products/gmsl/evkits/gpio3_gui.png
   :align: center
   :width: 600px

The register to be programmed is ``0x2C7``. Referring to the register description field, we want to configure the device as follows:

-  ``GPIO_OUT_DIS`` = 0: Enable the output driver
-  ``GPIO_TX_EN`` = 0: Disable GMSL2 GPIO transmission
-  ``GPIO_RX_EN`` = 0: Disable GMSL2 GPIO reception

With these settings, the hex value to write to this register is ``0x80``.

.. image:: https://wiki.analog.com/_media/products/gmsl/evkits/gpio3_gui_cfg.png
   :align: center
   :width: 600px

After writing this value, the LOCK LED will turn off and the ERRB LED will turn on. This is because we also set ``GPIO_OUT`` = 0. The ``GPIO_OUT`` bit is used to drive the GPIO pin output value when ``GPIO_RX_EN`` = 0.

`blinking.mp4 <https://wiki.analog.com/_media/products/gmsl/evkits/blinking.mp4>`__

If you set ``GPIO_OUT`` = 1, then the pin will be driven high, the green LOCK LED will turn on, and the red ERRB LED will be turned off. If you read the register again, you will also see that ``GPIO_IN`` is set indicating that the pin value is 1. The ``GPIO_IN`` bit will always reflect the pin value during operation.
