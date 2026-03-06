FMComms5 Configuration Options
==============================

RF Ports
--------

By default the FMComms5 is configured with the Minicircuits `TCM1-63AX+ <http://www.minicircuits.com/pdfs/TCM1-63AX+.pdf>`__ baluns on the Rx1A, Rx2A, Rx1C, Tx1A, Tx2A, and Tx1B channels. This wideband balun allows for tuning across the entire 6GHz range of the AD9361, although performance may be compromised at some frequencies.

Reference Clock
---------------

By default the FMComms5 uses a Rakon 40MHz RXO3225M as the reference clock. This is driven into the :adi:`ADCLK846`, which distributes the clock to the two :adi:`AD9361`\ s, the :adi:`ADF5355`, as well as back to the FMC connector. It is important that the PCB trace lengths to the two AD9361s be equally matched.

This on board reference can be bypassed by placing C301 (0.1uF) and removing R360. In this configuration an external reference clock can be injected into J301 (which is 50Ω terminated). The level of the external reference should be ensured to not exceed the :adi:`ADCLK846` input conditions (1.8 V p-p), and it will still be used to distribute the reference clock to the two AD9361s.

.. important::

   If you change the frequency of the reference clock, you must update the device tree.


External PLL
------------

While the AD9361 contains two identical synthesizers to generate the required LO signals for the RF signal paths: one for the receiver and one for the transmitter, and these PLLs require no external components; for phase sync'ed applications, it is sometimes easier/better to use an external LO for an improvement in phase noise, and overall easier phase synchronization.

Rev B
~~~~~

The FMComms5 comes with the layout provisions to accept the ADF5355. In the interim, an external LO signal can be injected into J302. This LO will be distributed to the two AD9361s by the Inphi 13617. Similar to the reference clock distribution, length matching is very critical for the external LO routes.

When the ADF5355 is available, it can be inserted into the design by soldering down the device, placing C331 and C332 and removing C390. In this configuration the RFOutA port of the ADF5355 port is in circuit, which allows for external LO generation up to 7GHz (divided to 3.5GHz in the AD9361). To generate an LO signal up to 8GHz (4GHz after the divide by 2 in the AD9361), the RFOutB node must be used. To select this net remove C331 and C332, and place C353 and C390.

Rev C
~~~~~

The FMComms5 comes with the :adi:`ADF5355`. This onboard reference normally flows through C331, and C332 (and C390 and R350 are DNI). To use the onboard ADF5355, just pick the right device tree on the SD Card. With the necessary device tree, the :doc:`ADF5355 </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf5355>` can be controlled like any IIO device to change the LO frequency of both transceivers.

To bypass the ADF5355 and use an external LO, hardware modifications are necessary. Rotate C332 by 90 degrees, so it goes on the pad of the C390 and remove C331 placing R350. In this configuration, an external reference clock can be injected into J302. The level of the external reference should be ensured to not exceed the :adi:`HMC744LC3` input conditions, and it will still be used to distribute the reference clock to the two AD9361s.

.. important::

   The hardware modifications (moving the cap, removing the cap, adding the resistor, is difficult since the components are tiny (0402 packages or 1 x 0.5 mm) and should be done by skilled professionals only


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms5-ebz/hardware/img_0246.jpg
   :align: center
   :width: 500px
