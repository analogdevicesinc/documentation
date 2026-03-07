Controlling ADALM-Phaser with MATLAB
====================================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/rfm_300.png
   :align: center
   :width: 800px

The article will discuss operating the ADALM-Phaser (Phaser) platform with MATLAB through use of the RF and Microwave Toolbox from Analog Devices (RFuW Toolbox). The RFuW Toolbox provides interface system objects for control of Phaser including examples and documentation in one convenient package.

Required Components
===================

-  First make sure you have ADALM-Phaser running with ADALM-Pluto attached. This process is covered in the article :doc:`EVAL-CN0566-RPIZ Overview </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0566/overview_setup>`.
-  Next from MATLAB install the `RF and Microwave Toolbox detailed on github <https://analogdevicesinc.github.io/RFMicrowaveToolbox/main/install/>`_
-  Finally from MATLAB install `Transceiver Toolbox <https://analogdevicesinc.github.io/TransceiverToolbox/master/install/>`_ which will control Pluto.

Verify Connectivity
===================

With Phaser connected to your local network or directly to your host machine with MATLAB installed, create an instance of the adi.Phaser class from the command prompt with the IP address of the Raspberry Pi.

.. code:: matlab

   bf = adi.Phaser;
   bf.uri = 'ip:phaser';
   bf()

This will connect and configure Phaser with a default set of parameters. If you receive a connectivity error verify the Raspberry Pi is powered up and you can at least ping the device. If you are having issues reach out to our support forums on EngineerZone.

Next verify connectivity to Pluto with a similar method. Create and instance of the adi.AD9361.Rx class and run the operator method as so:

.. code:: matlab

   sdr = adi.AD9361.Rx
   sdr.uri = 'ip:pluto';
   data = sdr();

Like the Phaser system object this operation should not generate any errors. The *data* vector should contain non-zero data.

Running an Example
==================

Now that we can communicate with the boards, we can run a basic example. With RFuW Toolbox installed a number of examples are provided with it and place on path. First make sure that the HB100 included with the Phaser kit is place in-front of Phaser itself and turned on. Next, open the basic RX only example by running the following on the MATLAB prompt:

::

   edit phaser_simple.m

This will launch the script containing the basic RX example. May any modifications to the URIs if necessary to reflect your system:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/capture.png
   :align: center
   :width: 600px

Once updated run the script by pressing play:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/capture2.png
   :align: center
   :width: 600px

This will produce a plot like the one below:
