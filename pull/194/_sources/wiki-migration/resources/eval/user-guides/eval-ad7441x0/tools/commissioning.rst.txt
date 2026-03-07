Commissioning made easy with AD74412R/13R
=========================================

Introduction
------------

| 
| During the installation stage of a process or building control system, sensors and actuators need to be connected to their respective control/monitor channels. This can be a complex and error prone exercise. This is especially true when sensors and actuators are located large distances from control modules, or in difficult to access areas.
| The Analog Devices Software Configurable I/O product family has 2 quad-channel Software Configurable I/O parts for building and process control applications, the AD74412R and the AD74413R. Each channel can be configured for voltage output, current output, voltage input, current input, RTD measurement and digital input. This document outlines how the variety of configuration options and on-board diagnostics can be used to confirm the sensors and actuators connected to each channel at the commissioning stage.
| By using the flexibility of the AD74412R/13R, a variety of configuration options and on-board diagnostics can be combined with knowledge of the electrical properties of the components being installed to determine which channel corresponds to each of the components, and then configure the AD74412R/13R to correctly match them, thus dramatically simplifying the installation process.

Case Study: Load Identification in a Temperate Control Process
--------------------------------------------------------------

| 
| An example scenario of a Temperature Control Process is used to demonstrate load confirmation capability. This is a common process in production lines where precise temperature control of water or other liquid is required. In the example, shown in Figure 1, a water mixing tank has a constant input flow of cold water, along with an adjustable input flow of hot water from a boiler, which is controlled with a ball valve to regulate water temperature. A temperature probe is placed in the tank to monitor the water temperature. An emergency stop button is also placed near the tank to shut off input flow in case of an emergency. All components are connected to the control module for the process, which uses a quad channel Software Configurable IO, AD7441xR.

.. image:: https://wiki.analog.com/_media/Temp Control Process.png
   :alt: Temp Control Process.png
   :align: center

| 
| Figure 1: Temperature Control Process Diagram

Understanding the Instrument Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 
| To begin, the characteristics of the sensors and actuators required for this process should be determined. Once the characteristics are understood, the instruments can be differentiated.
| \* A typical Control Valve for this process requires two channels, one to sense the position state of the valve using a voltage input channel, and one to control the actuator of the valve using a current output channel

-  The temperature probe uses a Pt100 RTD, which is measured using a resistance measurement channel. A Pt100 has a resistance of 100-138Ω for 0°C to 100 °C temperature range.
-  The Emergency Stop Button is a generic latching push-to-break button which is monitored with a digital input channel. The emergency stop button will electrically present as an open-circuit or short-circuit, which can be detected with on-board diagnostics of the AD74412R/AD74413R.

| 

Determining how the Channels are Configured
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|

| Now that the characteristics of the sensors & actuators are understood, the next step is to determine which channel is connected to which instrument. This example starts with the Control Valve as it uses 2 channels which have a “cause and effect” relationship that can be used for confirmation. The valve is controlled by a current in 4mA – 20mA range. The position sensor returns a voltage corresponding to the position of the valve.
| A current is sourced (using current output mode) on a single channel while monitoring the voltage (using voltage input mode) on the other 3 channels for a correlating input signal. This is repeated for subsequent channels until a correlating input signal is observed.
| Figure 2 shows the response on all 4 channels when sourcing a current on Channel C. No response is noted on Channels A & B, a voltage response is captured on Channels C & D. The Channel C measurement is the voltage response from the actuator (based on the fixed current applied). A correlating voltage input is also observed on Channel D, confirming Channel C as the actuator control channel and Channel D as the position sensor channel. Confirmation of these channels is achieved in a maximum of 4 attempts.

.. image:: https://wiki.analog.com/_media/load_confirmation_of_control_valve.png
   :alt: load_confirmation_of_control_valve.png
   :align: center

| 
| Figure 2: Determining channels used for Control Valve
| To confirm which channel is connected to the RTD, the remaining channels (A & B) are configured in resistance measurement mode and results are scanned for the expected resistance value. In this case, a Pt100 is expected to be in the range of 100Ω-138Ω for 0-100 °C water temperature range. Figure 3 shows that Channel B measures a resistance of 127Ω, indicating that the RTD is connected to Channel B.

.. image:: https://wiki.analog.com/_media/load_confirmation_of_rtd.png
   :alt: load_confirmation_of_rtd.png
   :align: center

| 
| Figure 2: Determining channel used for RTD

By a process of elimination, Channel A is identified as the emergency stop button. The on-board diagnostics can be used to confirm this:

-  If the emergency button is pushed, the switch appears as an open circuit. An open-circuit alert will have been observed while determining control valve channels using Current Output mode. The alert condition is asserted in the ALERT_STATUS register of the AD74412R/AD74413R.
-  If the emergency button is not pushed, the switch appears as a short circuit. Configure the channel in voltage output mode and check for short-circuit error alert.

| 
| This is an example of confirmation, not determination. Prior knowledge of the sensors/actuators connected to the channels is required in order to infer the relationships between the sensors and the expected electrical indicators. Sensor sensitivity should also be considered when devising a confirmation routine to ensure that large currents are not sourced to sensitive components.

| 

Conclusion
----------

| By using simple electrical properties of the connected instruments and the on-board configuration and diagnostic tools of the AD74412R/AD74413R products, connections on I/O channels are quickly confirmed, without the need for manual intervention.
| This process highlights the flexibility and value of the AD7441xR Software Configurable I/O parts and can dramatically reduce the installation time and avoid mis-wire problems seen during installation, saving significant time and expense.

:doc:`Back to AD74412R/AD74413R Table of Contents </wiki-migration/resources/eval/user-guides/ad7441x>`
