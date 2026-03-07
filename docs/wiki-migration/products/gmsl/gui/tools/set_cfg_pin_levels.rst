Set CFG Pin Levels
==================

CFG Pin Overview
----------------

All GMSL devices use configuration/config/CFG to bootstrap the most basic GMSL link configurations. Voltage levels at the CFG pins are latched at power-up, or upon a low-to-high transition of PWDNB.

These levels set initial register values and functional modes that may not be easily programmed through I2C or UART after the IC powers up. The CFG pins select device address, I2C or UART main control channel, GMSL forward data rate, Coax or STP cable, etc.

| The voltage level for each pin is set by an external precision resistor-divider connected between VDDIO and ground, or for some configurations, by a single resistor connected to VDDIO or ground. The voltage level at the CFG pins is latched approximately 1ms after all of the GMSL device's supplies reach the minimum levels required by the Power-on-Reset (POR) circuit.
| ==== CFG Pin Programming ==== There are two digital (I2C configurable :adi:`MAX5419 <en/products/max5419.html>`) potentiometers on board to set the CFG pin levels. The digital potentiometers are connected by default. Voltages on CFG pins can be monitored through CFG0 and CFG1 test points (loop type terminals).

| The CFG pin voltages latch at power-up and are not volatile after power-off due to the digital potentiometers’ EEPROM. Any of the settings can be changed by the software through register writes after power-up.
| ==== Setting the CFG Pin Levels from the GUI ====

.. important::

   To program the serializer, you must have the USB cable connected to the serializer and vice versa for the deserializer. You cannot program the CFG pin settings over the reverse channel.


From the GMSL GUI, navigate to: **Tools** > **Other Config** > **Set CFG Pin Levels**. For this example, we will be programming the :adi:`MAX96717 <en/products/max96717.html>` serializer.
| |image1|
| On the left side of the screen, you will see drop down options for the CFG pin levels. Select the CFG pin levels to match your intended configuration, then click the "**Program Serializer**" button. When you click the button, it will take a few seconds and then the digital potentiometer will be programmed.

.. important::

   After programming the digital potentiometer, you need to cycle power and restart the GUI for the new settings to take effect.


Once this is programmed, you will not have to program the board again unless you need to change to a different configuration.

.. |image1| image:: https://wiki.analog.com/_media/products/gmsl/gui/tools/cfg_setup_main.png
   :width: 800px
