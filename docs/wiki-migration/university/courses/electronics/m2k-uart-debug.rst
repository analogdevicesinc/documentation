Debugging UART with the ADALM2000
=================================

Objective
---------

The objective of this tutorial is to use the Pattern Generator and Logic Analyzer instruments provided by the :adi:`ADALM2000` (M2K) board and the :doc:`Scopy </wiki-migration/university/tools/m2k/scopy>` software toolset to visualize UART (Universal Asynchronous Receiver/Transmitter) transactions between two devices.

The :adi:`EVAL-ADICUP3029` microcontroller board and a typical software project that uses the UART communication module, waits for input data from the user, and then echoes it back through the pins available on the board.

Background
----------

A Universal Asynchronous Receiver/Transmitter (UART) is a computer hardware device for asynchronous serial communication in which the data format and transmission speeds are configurable. Its purpose is to transmit and receive serial data, using only two wires to communicate between devices (TX and RX). In the past, UARTs were separate integrated circuits, such as the industry standard 16550. However, most modern microcontrollers include one or more UART peripheral devices on-chip, requiring only an external physical interface device, such as a line driver / receiver or USB-UART interface device.

The UART transmitter converts parallel data from a controlling device like a microcontroller into serial form, transmits it in serial to the UART receiver, which then converts the serial data back into parallel data for the receiving device. Data flows from the TX pin of the UART transmitter to the RX pin of the UART receiver.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   Figure 1. UART data flow between devices


A UART transmits data asynchronously, which means there is no clock signal to synchronize the output of bits from the transmitting UART to the sampling of bits by the receiving UART. The UART transmit contains start and stop bits to frame the data byte being transferred. These bits define the beginning and end of the data byte so the receiving UART knows when to start (and stop) reading the bits.



|image2|

.. container:: centeralign

   Figure 2. UART data frame


When the UART receiver detects a start bit, it starts to read the incoming bits at a specific frequency, called the baud rate. Baud rate is the rate at which data is transferred, expressed in bits per second (bps). Both UARTs (Rx and Tx) must be configured at almost the same baud rate. This scheme is tolerant of a slight mismatch in baud rate between the transmitting and receiving devices; a typical 8-bit byte can tolerate approximately 10% difference in baud rate between transmitter and receiver before a bit error occurs.

UART data is organized into bytes. Each byte contains 1 start bit, 5 to 9 data bits (depending on the UART), an optional parity bit, and 1 or 2 stop bits.

.. container:: centeralign

   \ |image3|\


.. container:: centeralign

   Figure 3. UART Byte Configuration


The UART data transmission line is normally held at a high voltage level when no transmission is occurring. To start the transfer of data, the the transmission line is pulled from high to low. When the receiving UART detects the high to low voltage transition, it interprets this event as as start bit and begins reading the rest of the bits in the data frame at the selected baud rate.

A parity bit may be included after the data bits. Parity describes the evenness or oddness of a number.

Even parity: for a given set of bits, the occurrences of bits whose value is 1 is counted. If that count is odd, the parity bit value is set to 1. If the count of 1s in a given set of bits is already even, the parity bit value is 0.

Odd parity: for a given set of bits, if the count of bits with a value of 1 is even, the parity bit value is set to 1 . If the count of bits with a value of 1 is odd, the count is already odd so the parity bit value is 0.

The parity bit is simple error detection scheme, and will detect all single-bit errors. Bits can be changed during transmission by mismatched baud rates, noise picked up on long distance data transfers, etc. Like baud rate, both transmitter and receiver must be set to the same parity configuration.

To signal the end of the data byte, the sending UART drives the data transmission line from a low voltage to a high voltage for at least two bit periods.

Hardware Configuration
----------------------

Figure 4. shows the hardware connection between M2K board and EVAL-ADICUP3029.

.. container:: centeralign

   \ |image4|\


.. container:: centeralign

   Figure 4. UART Debug Hardware Setup


The UART pins for the EVAL-ADICUP3029 are available for communication at port **P7**.

**EVAL-ADICUP3029 UART pin configuration:** PORT P7:

-  Pin7 - UART TX
-  Pin8 - UART RX

PORT P4:

-  Pin7 - GND

**M2K UART pin configuration:**

-  DIO0 - TX
-  DIO1 - RX
-  GND - DGND

Connect M2K pins to EVAL-ADICUP3029 as follows:

-  Pin7 - DIO1
-  Pin8 - DIO0

**EVAL-ADICUP3029 UART switch configuration:**

-  Set S2 to the CENTER position.

(S2 selects which device to connect the ADuCM3029's UART to - USB-UART interface, Arduino headers, or WiFi module connector.)

Software Configuration
----------------------

There are several options for which software to use for this demonstration; the main requirement is that it implement some sort of command-line interface that echoes characters back as they are typed. The CLI example project for the EVAL-ADICUP3029 can be used:

:git-EVAL-ADICUP3029:`CLI example for ADICUP3029 <projects/ADuCM3029_demo_cli>`

Scopy Pattern Generator Configuration
-------------------------------------

First, set up the Pattern Generator to transmit test data to EVAL-ADICUP3029.

The EVAL-ADICUP3029 software application has the UART configured as follows:

-  Baud rate: 115200
-  Stop bits: 1
-  Parity: none

For transmission, we will use only one digital channel as Tx. Open the Pattern Generator instrument, select DIO0 channel and press "Group with Selected" button. This will display the decoded pattern for our application based on the data that we want to send.

On the left side of the user interface, a settings menu is available. Configure the UART settings to match the software application that we want to debug.

An example for the Pattern Generator setup is presented in Figure 5.

.. container:: centeralign

   \ |image5|\


.. container:: centeralign

   Figure 5. UART Pattern Generator Setup


**Pattern Generator settings:**

-  Pattern: UART
-  Baud: 115200
-  Stop bits: 1
-  Parity: None
-  Data to send: 'A' (ASCII code)

Scopy Logic Analyzer Configuration
----------------------------------

Several UART configuration parameters need to be determined in order to properly configure Scopy. For the EVAL-ADICUP3029 project, they are as follows:

-  Baud rate: 115200
-  Data bits: 8
-  Parity: none (Check polarity: no)
-  Stop bits: 1
-  Bit order: LSB first
-  Data format: ASCII

An overview of the user interface is shown in Figure 6.


|image6|

.. container:: centeralign

   Figure 6. UART Logic Analyzer User Interface


Open the Logic Analyzer instrument, select DIO0-DIO1 lines and press the "Group with selected" button.

Select the channel group formed and apply the UART decoder. While the group is selected, open settings menu by pressing the |image7| button on the top right side of the user interface. A settings panel will appear for the UART decoder, allowing the signal-channel configuration and parameters setup. Apply the parameters listed above to the group.

.. container:: centeralign


|image8|

.. container:: centeralign

   Figure 7. UART Group Settings


The Logic Analyzer must be set up to “catch” the UART byte transfer on the Logic Analyzer plot. Since the UART transfer starts with a start bit, (transmit line is pulled from high to low), we can use this event to trigger the capture.

.. container:: centeralign

   \ |image9|\


.. container:: centeralign

   Figure 8. Trigger Settings


UART Example
------------

This example verifies the receive/transmit operations of the software application developed for EVAL-ADICUP3029. The data will be transmitted from the Pattern Generator, and visualized on Logic Analyzer, by connecting ADALM2000 to the UART pins of the EVAL-ADICUP3029 board (see Hardware Configuration step).

Set the Time Base of the Logic Analyzer instrument to 30us and the Trigger Position at 90us and run a Single sweep.

.. container:: centeralign

   \ |image10|\


.. container:: centeralign

   Figure 9. General Settings


The Logic Analyzer will wait for the falling edge of the Rx signal to be triggered (corresponding to the start bit).

Run a single sweep on the Pattern Generator to send the first UART byte.

The result captured by the Logic Analyzer is presented in Figure 10.

.. container:: centeralign

   \ |image11|\


.. container:: centeralign

   Figure 10. UART sequence plot


Analyzing the plot, the byte (ASCII code) corresponding to character "A" is sent from the Pattern Generator and received at the EVAL-ADICUP3029 Rx pin. After the byte is received, on TX pin the byte is sent back and captured by the Logic Analyzer.

The decoders available in Scopy allow visualization of the data bytes in ASCII format, including the Start Bit (denoted with "S" on the plot) and the Stop bit (denoted with "T" on the plot).

Now, let's try sending multiple characters and see what happens with our application.

In the Pattern Generator instrument, under the "Data to Send" label, set the data bytes to "ADI".

.. container:: centeralign

   \ |image12|\


.. container:: centeralign

   Figure 11. Pattern Generator - Data to send


On the Logic Analyzer, adjust the Time Base and Trigger Position accordingly to be able to see all of the transactions. (i.e. Time Base: 100us and Trigger Position: 300us)

Run Single sweep in The Logic Analyzer and then in the Pattern Generator.

The result captured by the Logic Analyzer is shown in Figure 12.

.. container:: centeralign

   \ |image13|\


.. container:: centeralign

   Figure 11. Pattern Generator - Data to send


The EVAL-ADICUP3029 example program echoes received data bytes as they come in. As expected all the data bytes were received by the EVAL-ADICUP3029 board and sent back on Tx pin.

Conclusion
----------

In addition to UART, the application includes a set of decoders covering a large number of communication protocols such as I2C, I2S, SPI, JTAG, and others, making ADALM2000 a powerful tool for analyzing and debugging digital signals.

Further Reading:
~~~~~~~~~~~~~~~~

-  :adi:`Implementing UART Using the ADuCM3027/ADuCM3029 Serial Ports <media/en/technical-documentation/application-notes/an-1435.pdf>`
-  :adi:`Implementing UART Using ADuCM302x Serial Ports <media/en/technical-documentation/application-notes/EE-391.pdf>`
-  :doc:`EVAL-ADPAQ3029 - UART(Arduino) demo </wiki-migration/resources/eval/user-guides/eval-adpaq3029/resources/app_uart>`
-  :doc:`EVAL-ADICUP3029 User Guide </wiki-migration/resources/eval/user-guides/eval-adicup3029>`
-  :doc:`ADALM2000 Overview </wiki-migration/university/tools/m2k>`
-  :doc:`Scopy </wiki-migration/university/tools/m2k/scopy>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/uart_flow.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/uart_frame.png
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/uart_sequence.png
   :width: 700px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/hw_uart_m2k.jpg
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/pg_uart_setup.png
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/uart_la_setup.png
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/grp_set_butt.png
.. |image8| image:: https://wiki.analog.com/_media/university/courses/electronics/uart_grp_settings.png
.. |image9| image:: https://wiki.analog.com/_media/university/courses/electronics/uart_trigger_grp.png
.. |image10| image:: https://wiki.analog.com/_media/university/courses/electronics/la_settings_uart.png
.. |image11| image:: https://wiki.analog.com/_media/university/courses/electronics/uart_la_plot.png
.. |image12| image:: https://wiki.analog.com/_media/university/courses/electronics/uart_data_to_send.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/university/courses/electronics/uart_la_plot2.png
