Configuration Options for AD-FMCOMMS11-EBZ boards
=================================================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is is now part of the FMCOMMS11 HDL project documentation, found at https://analogdevicesinc.github.io/hdl/projects/fmcomms11/index.html\


Several GPO and GPIO pins are brought to the RF card through connector J2, found on the bottom of the PCB. These pins allow configuration of the PA, LNA and SPDT switch found on the PCB. These devices are summarized in a table below.

Several solder link are brought to the RF card to allow optional clock referece for the clock management uni, ADC and DAC. These configuration options are summarized in a table below.

Design Cross Section

+----------+--------------------------------------------+-----------+--------------------------+
| Location | Device Controlled                          | Settings  | Action                   |
+==========+============================================+===========+==========================+
| JP1      | + Differential Clock Reference for ADF4355 | A and COM | Internal Clock Reference |
+----------+--------------------------------------------+-----------+--------------------------+
|          | + Differential Clock Reference for ADF4355 | B and COM | External Clock Reference |
+----------+--------------------------------------------+-----------+--------------------------+
| JP2      | - Differential Clock Reference for ADF4355 | A and COM | Internal Clock Reference |
+----------+--------------------------------------------+-----------+--------------------------+
|          | - Differential Clock Reference for ADF4355 | B and COM | External Clock Reference |
+----------+--------------------------------------------+-----------+--------------------------+
|          |                                            |           |                          |
+----------+--------------------------------------------+-----------+--------------------------+
| JP22     | + Differential Clock Reference for DAC     | A and COM | ADF4355 Clock Reference  |
+----------+--------------------------------------------+-----------+--------------------------+
|          | + Differential Clock Reference for DAC     | B and COM | External Clock Reference |
+----------+--------------------------------------------+-----------+--------------------------+
| JP5      | - Differential Clock Reference for DAC     | A and COM | ADF4355 Clock Reference  |
+----------+--------------------------------------------+-----------+--------------------------+
|          | - Differential Clock Reference for DAC     | B and COM | External Clock Reference |
+----------+--------------------------------------------+-----------+--------------------------+
|          |                                            |           |                          |
+----------+--------------------------------------------+-----------+--------------------------+
| JP3      | + Differential Clock Reference for ADC     | A and COM | External Clock Reference |
+----------+--------------------------------------------+-----------+--------------------------+
|          | + Differential Clock Reference for ADC     | B and COM | HMC361 Clock Reference   |
+----------+--------------------------------------------+-----------+--------------------------+
| JP4      | - Differential Clock Reference for ADC     | A and COM | External Clock Reference |
+----------+--------------------------------------------+-----------+--------------------------+
|          | - Differential Clock Reference for ADC     | B and COM | HMC361 Clock Reference   |
+----------+--------------------------------------------+-----------+--------------------------+

.. image:: https://wiki.analog.com/_media/navigation AD-FMCOMMS11-EBZ#Characteristics and Performance#./
   :alt: Hardware#FCC or CE certification
