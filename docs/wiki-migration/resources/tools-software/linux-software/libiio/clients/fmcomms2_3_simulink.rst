ADI vs MathWorks Support
========================

MATLAB and Simulink support is currently provided from ADI and through the
MathWorks. However, implementations and board support will differ between these
sources. Official MathWork support is for:

-  `ADALM-PLUTO <https://www.mathworks.com/hardware-support/adalm-pluto-radio.html>`_
-  `FMComms2/3/4 with Zedboard or ZC706 <https://www.mathworks.com/hardware-support/zynq-sdr.html>`_
-  `ADRV9361-Z7035 (PicoZed) with ADRV1CRR-FMC carrier <https://www.mathworks.com/hardware-support/zynq-sdr.html>`_.

ADI maintains support for all FMComms, ADALM-PLUTO, and ADRV board variants, as
well as devices that support libiio. If your board has official support from
MathWorks we would recommend starting with their implementations linked above.

ADI libiio Support
==================

.. include:: matlab_simulink.rst

Data Streaming Example in MATLAB
================================

In this section, we will show an example of data streaming using MATLAB libiio. Download the example **ad9361_matlab.m** from GitHub and open it in MATLAB:

.. admonition:: Download
   :class: download

   :git-MathWorks_tools:`hil_models/legacy/fmcomms2_3_data_stream/ad9361_matlab.m`

In this example, *input* defines two sine waves (one for I channel, and the other for Q channel) streaming from MATLAB to target, as well as all the attributes of the device configuration channels. *output* is used to capture the streamed data from target, as well as to record all the attributes of the device monitoring channels, which is RSSI in this example.

There are two other parameters of the AD9361 you can set according to your
modeling requirement:

-  Channel size: This is the number of samples buffered at the target before they are sent out together at each time. This number applies to both I and Q channels.
-  Number of data channels: This can be either 2 or 4. If it is 2, it will
   enable one IQ channel. Otherwise, it will enable two IQ channels.

Since we are streaming two sine waves to the target, we will also receive two
sine waves back in MATLAB. This is what you should be able to get in the end:

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/clients/iio_matlabexample.png
   :alt: Block diagram

Besides the two sine waves in the plot, we also see the RSSI indicator for both
channel 1 and channel 2 in the workspace.

Data Streaming Example in Simulink
==================================

Tx and Rx in One Block
----------------------

In this section, we will show an example of data streaming using Simulink libiio block. Download the Simulink model **ad9361_sim.slx** from GitHub and open the model from Simulink:

.. admonition:: Download
   :class: download

   :git-MathWorks_tools:`hil_models/legacy/fmcomms2_3_data_stream/ad9361_sim.slx`

In this model, DATA_IN1 to DATA_IN4 are four pins used to stream two sine waves (one for I channel, and the other for Q channel) from Simulink to target, and DATA_OUT1 to DATA_OUT4 are four pins used to observe the time-domain streamed data from target in a Time Scope, as highlighted below. The other pins all represent certain settings you can find from :doc:`ADI IIO Scope </wiki-migration/resources/tools-software/linux-software/fmcomms2_plugin>`.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/clients/sinkmodel.png
   :alt: Block diagram
   :width: 600

There are two other parameters of the Ad9361 Simulink block you can set
according to your modeling requirement:

-  Channel size: This is the number of samples buffered at the target before they are sent out together at each time. This number applies to both I and Q channels.
-  Number of data channels: This can be either 2 or 4. If it is 2, it will
   enable one IQ channel. Otherwise, it will enable two IQ channels.

Make sure:

-  RX LO Frequency = TX LO Frequency
-  DDS Mode = DAC Buffer Output

Since we are streaming two sine waves to the target, we will also see two sine
waves in the Time Scope. This is what you should be able to observe:

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/clients/iio_example2.png
   :alt: Block diagram
   :width: 800

Besides the two sine waves in the Time Scope, we also see the RSSI indicator for
both channel 1 and channel 2.

Separate Tx and Rx Blocks
-------------------------

In the example above, we use one block for both Tx and Rx settings. You also
have the option to have Tx and Rx in two separate blocks. All you have to do is
to provide two configuration (.cfg) files.

Download the Simulink model **ad9361_sim.slx** from GitHub and open the model from Simulink:

.. admonition:: Download
   :class: download

   :git-MathWorks_tools:`hil_models/legacy/fmcomms2_3_data_stream/ad9361_sim.slx`

In this Simulink model, you will find the Rx block on the top and the Tx block
on the bottom, as shown below:

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/clients/txandrx.png
   :alt: Block diagram
   :width: 600

In this GitHub directory, along with the Simulink model, you will find two cfg
files: ad9361_tx.cfg and ad9361_rx.cfg, which includes the attributes related to
Tx and Rx.

Using these two cfg files and the two blocks provided in the Simulink model, you
can now make an independent Tx model and an independent Rx model.
