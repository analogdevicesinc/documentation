Multichannel analog interface hardware for the ADALM1000
========================================================

The two analog input channels of the ADALM1000 provide a high input impedance and wide dynamic range which is very helpful for many of the measurements that students would be making around their laboratory activities. However, there are only the two analog inputs. Often, there are many more than two signals in the circuit or system under investigation that you would like to monitor. Or there could be a number of low bandwidth sensors, such as ambient temperature or light levels around a room, that need to be measured or monitored over long duration times when gathering experimental data. As a solution to this need, the following multi-channel analog multiplexer is proposed.

A first incarnation of this very simple design uses one CD4052 dual 4:1 analog multiplexer (or the equivalent 74HC4052/74HCT4052 ) to switch one or both analog input channels, see the schematic in figure 1. In addition the PDIP versions of the MAX4618 and MAX4582 are pin compatible with the industry-standard 74HC4052.

The 4:1 mux added to the two input channels allows the board to measure up to 8 signal channels. More information and CAD design files for this and the other ADALM1000 accessory boards can be found :doc:`on this Wiki page </wiki-migration/university/tools/adalm1000/accessory-boards-index>`.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/analog-mux-bw-sch.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 1, Analog Mux Circuit Schematic


.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/m1k-analog-mux-4052-top.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2, Analog Mux Circuit PCB Top artwork


.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/analog-mux-2.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 3, Analog Mux Circuit configured for use in ALICE


For ease of use 6/8 pins of the ANALOG connector pass through to the second 1X8 pin analog connector (ANALOG2). The 8 analog inputs of the mux fill out the other 8 pin MUXIN connector. The X and Y outputs of the mux can be connected to input only AIN/BIN pins through solder jumpers.

Digital outputs PIO 0 and 1 are used to address the four Mux channels. Digital output PIO 2 drives the INH inhibit input of the Mux which turns off all the switches.

The multiplexer is powered from the fixed + 5V supply on the ALM1000 analog connector which will limit the allowed range of analog input voltages to be within the same 0 to + 5V supported by the analog inputs. The 6/8 analog connector pins of the ALM1000 including the +5 volt and +2.5 volt power supplies are included in the female connector on the right and can be used to power sensor electronics, up to the current limits of the ALM1000 power supplies.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-poly-phase-fig7.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 5, ALICE Analog Mux controls


There are many use cases that can benefit from more than two scope inputs. Below in figures 6 and 7 are examples showing the Mux being used to view multiple outputs of a poly-phase filter.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/accesory-mux.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6, M1k Mux accessory board attached to poly phase filter and an M1k


Another use case is the artificial lumped LC transmission line :git-education_tools:`experiment board <experiment-boards>` shown in figure 7.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lc-atl-fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, M1k plus Mux accessory board connected to lumped LC transmission line.


The simplest way to use the 74HC4052 is just on a small bit of proto-board with male jumper wires attached as show in figure 8.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/74hc4052-bb-mux.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8, Simply attach 74HC4052 on proto-board and jumper wires


There are other analog multiplexer configurations in the generic CD4XXX series of CMOS ICs. The CD4051 is a single 8:1 mux and the CD4067 is a single 16:1 mux. The old Motorola MC14529B analog selector can be a configured as a dual 4-channel or single 8-channel device depending on how the input controls are used. By using 3 or all 4 of the digital PIO bits and two of these single multiplexers either 16 or even 32 signal channels could be measured. This `16:1 mux breakout board <https://www.sparkfun.com/products/9056>`__ available from SparkFun is based on the CD74HC4067 and works well with the ALM1000. Another `8 Channel Multiplexer Breakout <https://www.sparkfun.com/products/13906>`__ based the 74HC4051 is also available. Either works well with the ADALM1000. Also available from SparkFun, the `MIKROE Analog MUX Click <https://www.sparkfun.com/products/18931>`__ board uses the 74HC4067 16:1 mux. The MIKROE analog mux board comes with spring action terminal blocks for the 16 analog inputs which makes for easy connections.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/mikroe-analog_mux_click_2_.png
   :align: center
   :width: 200px

.. container:: centeralign

   MIKROE Analog MUX Click


The SparkFun analog mux boards do not come with header connectors so they would need to be added. The pins on the connector do not line up with the M1k connectors so male to male jumpers would be needed as shown in the figure 9.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/sparkfun-mux.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9, CD4067 mux break out board attached to poly phase filter and an M1k


In figure 10 we have a modified version of the protoboard/breadboard adapter which now includes the multiplexer and two of the input resistor divider networks.

.. image:: https://wiki.analog.com/_media/university/tools/m1k_breadboard_mux_layout.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 10 Breadboard adapter with analog MUX and input attenuators


Another functionally similar option is the :adi:`dual 4:1 ADG609 <media/en/technical-documentation/data-sheets/ADG608_609.pdf>` and single ADG608 8:1 multiplexers, which have a different pin-out than the generic CD4051/52 multiplexers. Through-hole and surface mount ADG609 based boards similar to the one in figure 3 are also included in the zip file.

While the generic CD4052 is lower cost than the ADG609, there are two main advantages of using the ADG609 over the CD4052. The ADG609 on resistance maximum spec is 30 ohms, where the CD4052 on resistance maximum spec is 240 ohms and the 74HC4052 on resistance maximum spec is 120 ohms. This higher resistance could cause errors and distortions in the measurements under certain conditions.

The TTL compatible digital input minimum logic high voltage spec for the ADG609 is 2.45 V where the CD4052 and 74HC4052 minimum logic high voltage spec is 3.15V which is just slightly lower than the 3.3V typical logic high output voltage generated by the ALM1000. The actual logic threshold for the CD4052 is probably closer to VDD/2 ( 2.5V ) at room temperature and seems to work ( given this will probably be used at room temperature ) but there could be little margin in certain cases. The TTL compatible 74HCT4052 has a 1.6 volt typical logic high threshold which is perfect for the 3.3 V CMOS outputs of the ALM1000.

This analog multiplexer data acquisition add-on board is a perfect candidate for writing a custom program using the ALM1000 Python interface software package (`pysmu <https://github.com/signalspec/libsmu>`__). A basic example Python program (eight-channel-mux.py) is written with a minimal display but provides all the ALM1000 pysmu specific code to pole the dual 4:1 MUX inputs through the two analog input channels A and B. The display window as shown in figure 11 displays the 8 raw voltage values. The program can of course be further customized by the user to display the input signals in the appropriate scale factor with any gain and offset calibration for the sensor(s) being used. A copy of the Python program is included in the zip file.

.. image:: https://wiki.analog.com/_media/university/tools/m1k-analog-mux_f5.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 11 Basic 8 input MUX data display


The :doc:`ALICE (Software used for ADALM1000) </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>` has an optional mode which turns the ALM1000 into a four ( five counting Channel A ) input scope. The program uses a technique common in analog CRT oscilloscopes ( with a single electron beam ) where multiple input channels were switched in on alternating sweeps of the beam. This trick requires periodic signals and that each sweep be "triggered" or synced from the same input signal. In our case this will be channel A which is not multiplexed. This could be either the function generator output of channel A or a signal input to channel A in Hi-Z mode. As an example note the screen shot in figure 12.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/analog-mux-window.png
   :align: center
   :width: 720px

.. container:: centeralign

   Figure 12, Four channel Mux display of ALICE desktop


One important feature of the program is that a sync or sweep start pulse is output on the PIO 3 digital output pin just before each analog sweep starts. Using this "reset" pulse would be necessary whenever this program is used to observe a circuit that contains "state" such as to reset a digital counter to the same starting condition for each sweep.

`Design file archive: <https://wiki.analog.com/_media/university/tools/m1k-analog-mux.zip>`__
