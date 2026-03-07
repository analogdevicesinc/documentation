AD-PS0005-RD User Guide
=======================

| 
| |AD-PS0005-RD Board|

.. container:: center

   *<fc #000000>\ *\ **Figure 1. AD-PS0005-RD Board**\ *\ </fc>*


   | ===== Overview ===== The :adi:`AD-PS0005-RD` reference design delivers a robust power solution for 48V systems, featuring multiple outputs and hot-swap capability for high reliability and flexibility. It incorporates the following key components:

-  :adi:`LTC4286` – A high-power positive hot-swap controller for safe board insertion and removal.
-  :adi:`LTM4660` – A 60V/300W hybrid step-down µModule® bus converter that generates the 12V output.
-  :adi:`LTM4681` – A quad 31.25A µModule regulator with integrated digital power management for precise control and monitoring.
-  :adi:`LTM4655` – A 40V dual 4A step-down or 50W inverting µModule regulator for versatile power conversion

|

| ===== Features =====

-  Designed for 48V power systems that provides higher power density
-  Hot swap capability for servers and data centers
-  Power source conversion from 48V to 12V for existing 12V systems
-  High power and low voltage capability for FPGAs, microcontrollers, etc.

| 

Applications
------------

-  Automatic Test Equipment
-  Data Centers
-  Microcontrollers and FPGAs

|

Block Diagram
-------------

| |Simplified System Block Diagram|

.. container:: center

   *<fc #000000>\ *\ **Figure 2. Simplified System Block Diagram**\ *\ </fc>*


Specifications
--------------

.. container:: center

   
   +-----------------+---------------------------------------+--------------------------------------+
   | Characteristic  | **Condition**                         | **Value**                            |
   +=================+=======================================+======================================+
   | Input Supply    | External                              | 45.6V\ :sub:`DC` to 50.4V\ :sub:`DC` |
   |                 |                                       | 20A                                  |
   +-----------------+---------------------------------------+--------------------------------------+
   | Hot Swap Output | Test Point E7 and E11                 | 45.6V\ :sub:`DC` to 50.4V\ :sub:`DC` |
   +-----------------+---------------------------------------+--------------------------------------+
   | Output Accuracy | Different Load Currents               | VOUT \* ± 1.5%                       |
   +-----------------+---------------------------------------+--------------------------------------+
   | Efficiency      | All Other Outputs Except for 12V      | 80 to 90%                            |
   +-----------------+---------------------------------------+--------------------------------------+
   |                 | 12V Output and Load Current up to 50A | 90%                                  |
   +-----------------+---------------------------------------+--------------------------------------+

   |


.. container:: center

   *<fc #000000>\ *\ **Table 1. Board Performance Summary**\ *\ </fc>*


Components and Connections
--------------------------

|

| |AD-PS0005-RD Inputs and Outputs|

.. container:: center

   *<fc #000000>\ *\ **Figure 3. Inputs and Outputs**\ *\ </fc>*


   | ==== Power Supply Connection ====

-  TP10 (Positive Terminal)/TP12(Negative Terminal) - Banana Jack Connector
-  TP11 (Positive Terminal)/E5(Negative Terminal) - Turret Terminal

.. note::

   Supply power to either TP10/TP12 or TP11/E5.


|

.. warning::

   Observe the correct polarity to prevent damage to the board.


| ==== LED Indicators ====
| |AD-PS0005-RD LED Location|

.. container:: center

   *<fc #000000>\ *\ **Figure 4. LED Location**\ *\ </fc>*


   |

.. container:: center

   
   ============ =========================================================
   **LED Name** **Description**
   DS1          Indicates if there is 12V output
   DS2          Indicates if there is 5V output
   DS3          Indicates if there is -5V output
   DS4          Indicates if there is 48V input
   DS5          Indicates if there is a fault in LTC4286
   DS6          Indicates if the power is good for LTC4286
   DS7          Indicates if there is output from LTC4286
   DS8          Indicates if there is an error from LTC4286
   DS9          Indicates if there is input from DC1613 SCL PMBus
   DS10         Indicates if there is input from DC1613 SDA PMBus
   DS11         Indicates if there is output at LTM4681 channel 1 or OUT1
   DS12         Indicates if there is output at LTM4681 channel 2 or OUT2
   DS13         Indicates if there is output at LTM4681 channel 3 or OUT3
   DS14         Indicates if there is output at LTM4681 channel 4 or OUT4
   ============ =========================================================
   
   |

.. container:: center

   *<fc #000000>\ *\ **Table 2. LED Designation and Description**\ *\ </fc>*


| ==== Switches ==== |AD-PS0005-RD Switch Location|

.. container:: center

   *<fc #000000>\ *\ **Figure 5. Switch Location**\ *\ </fc>*


Hardware switches used to set Device Address:

-  S1 – L TC4286 (Default OFF). 40H for 7-bit and 80H for 8-bit

| 
| ==== Turrets ==== |AD-PS0005-RD Turrets Location|

.. container:: center

   *<fc #000000>\ *\ **Figure 6. Turrets Location**\ *\ </fc>*


   |

.. container:: center

   
   ======== =========== ========
   Pin Name Description Pin Type
   ======== =========== ========
   TP11     48V Input   Turret
   E5       GND         Turret
   E7       LTC4286 OUT Turret
   E11      GND         Turret
   TP41     -5V OUT     Turret
   E3       5V OUT      Turret
   E4       GND         Turret
   E1       12V OUT     Turret
   E2       GND         Turret
   TP25     0.85V OUT   Turret
   TP29     GND         Turret
   TP27     1V OUT      Turret
   TP28     1.2V OUT    Turret
   TP26     1.8V OUT    Turret
   ======== =========== ========
   
   |

.. container:: center

   *<fc #000000>\ *\ **Table 3. Turrets Designation and Description**\ *\ </fc>*


| ==== Jumpers ==== |AD-PS0005-RD Jumpers Locations|

.. container:: center

   *<fc #000000>\ *\ **Figure 7. Jumpers Location**\ *\ </fc>*


   |

.. container:: center

   
   =========== ============ ===============
   Jumper Name Description  Default Setting
   =========== ============ ===============
   J1          LTM4660 RUN  1-2
   J2          LTM4669 MODE 1-2
   J3          LTM4655 RUN  1-2
   P1          LTM4655 SSFM 1-2
   P2          LTM4655 RUN  1-2
   P4          LTC4286 EN   1-2
   P5          LTM4681 RUN0 1-2
   P6          LTM4681 RUN1 1-2
   P7          LTM4681 RUNP 1-2
   J4          LTM4681 RUN2 1-2
   J5          LTM4681 RUN3 1-2
   J6          LTM4681 WP01 2-3
   J7          LTM4681 WP23 2-3
   =========== ============ ===============
   
   |

.. container:: center

   *<fc #000000>\ *\ **Table 4. Jumpers Designation and Description**\ *\ </fc>*


| ===== Board Evaluation =====

Equipment Needed
~~~~~~~~~~~~~~~~

-  48V 20A Power Supply
-  Digital Multimeter

Hardware Setup
^^^^^^^^^^^^^^

-  Confirm the jumper settings.
-  Set the DC Power supply to 48V.
-  Connect the positive terminal to TP10 for banana jack or TP11 for test grabber or hook clips.
-  Connect the negative terminal to TP12 for banana jack or E5 for test grabber or hook clips.
-  Turn on the DC Power supply. You will notice DS4 (Green LED) will light up.
-  Output measurements can be done using the Pin Turrets as reference.

| |Sample Setup for Voltage Measurement|

.. container:: center

   *<fc #000000>\ *\ **Figure 8. Sample Setup for Voltage Measurement**\ *\ </fc>*


| ==== Test Measurement ====

-  Configure the digital multimeter for DC voltage measurement.
-  Refer to Figure 3 for the location of the test points and Table 5 for the expected results.
-  Using the digital multimeter, measure the DC voltage across each listed combination of test points.
-  Observe proper polarity. Connect the (+) lead to A and the (-) lead to B.

.. container:: center

   
   +----------------+-----------+-----------+------------------------+-------------------------+
   | **Test Point** | **A (+)** | **B (-)** | **Minimum Reading(V)** | **Maximum Reading (V)** |
   +================+===========+===========+========================+=========================+
   | 1              | TP11      | GND       | 45.6                   | 50.4                    |
   +----------------+-----------+-----------+------------------------+-------------------------+
   | 2              | E7        | E11       | 45.6                   | 50.4                    |
   +----------------+-----------+-----------+------------------------+-------------------------+
   | 3              | TP41      | GND       | -5.08                  | -4.92                   |
   +----------------+-----------+-----------+------------------------+-------------------------+
   | 4              | E3        | GND       | 4.92                   | 5.08                    |
   +----------------+-----------+-----------+------------------------+-------------------------+
   | 5              | TP25      | GND       | 0.788                  | 0.812                   |
   +----------------+-----------+-----------+------------------------+-------------------------+
   | 6              | TP27      | GND       | 0.985                  | 1.015                   |
   +----------------+-----------+-----------+------------------------+-------------------------+
   | 7              | TP28      | GND       | 1.182                  | 1.218                   |
   +----------------+-----------+-----------+------------------------+-------------------------+
   | 8              | TP26      | GND       | 1.773                  | 1.827                   |
   +----------------+-----------+-----------+------------------------+-------------------------+
   | 9              | E1        | GND       | 11.808                 | 12.192                  |
   +----------------+-----------+-----------+------------------------+-------------------------+
   
   |


.. container:: center

   *<fc #000000>\ *\ **Table 5. Expected Voltage Measurements**\ *\ </fc>*


| |Sample Setup for Efficiency Test|

.. container:: center

   *<fc #000000>\ *\ **Figure 9. Sample Setup for Efficiency Test**\ *\ </fc>*


Efficiency
^^^^^^^^^^

| 
| |Efficiency vs. Load Current|

.. container:: center

   *<fc #000000>\ *\ **Figure 10. Efficiency vs. Load Current**\ *\ </fc>*


|

.. note::

   :adi:`LTM4681` and :adi:`LTM4655` efficiency results are referenced to VIN 12V to be comparable with their datasheet specifications.


| ==== Output Regulation ====
| |Output Regulation vs Load Current|

.. container:: center

   *<fc #000000>\ *\ **Figure 11. Output Regulation vs. Load Current**\ *\ </fc>*


| ===== Software Setup =====
| The Status, Faults, Voltage, Current, Power, etc. of both the :adi:`LTC4286` and :adi:`LTM4681` can be monitored using :adi:`LTpowerPlay` and :adi:`DC1613A`.

| :adi:`LTpowerPlay` is a windows-based development environment supporting Analog Devices' Digital Power Systems Management (PSM) products.
| === Requirements ===

-  :adi:`LTpowerPlay`
-  :adi:`DC1613A`

| 
| Connect the :adi:`DC1613A` as shown below:
| |DC1613A Connection|

.. container:: center

   *<fc #000000>\ *\ **Figure 12. DC1613A Connection Location**\ *\ </fc>*


   | ==== Software Installation ==== 1. Download and install :adi:`LTpowerPlay`.

2. Request an LTpowerPlay License. When LTpowerPlay launches the first time, it will prompt you to request a license.

-  Click '**Request a License Key...**'
-  Enter the required information.
-  Click **'Send License Request'**

   -  **Note:** Ensure your email spam filter allows messages from **licenseserver@ltpowerplay.com**

3. Install your LTpowerPlay License File.

-  You will receive an email containing your license file and installation instructions.
-  Follow the steps in the email to complete the license installation.

|

| ==== Software Operation ==== 1. Double click on LTpowerPlay icon and follow the onscreen instructions.
| |LTpowerPlay Startup Screen|

.. container:: center

   *<fc #000000>\ *\ **Figure 13. LTpowerPlay Startup Screen**\ *\ </fc>*


2. Once you clicked on **Detect Chips**, it will open the main screen. The devices should be enumerated in the left pane.
| |LTpowerPlay Main Screen|

.. container:: center

   *<fc #000000>\ *\ **Figure 14. LTpowerPlay Main Screen**\ *\ </fc>*


| 
| ===== Resources =====

-  :adi:`LTC4286 Product Page <LTC4286>`
-  :adi:`LTM4660 Product Page <LTM4660>`
-  :adi:`LTM4681 Product Page <LTM4681>`
-  :adi:`LTM4655 Product Page <LTM4655>`

| 
| ===== Design & Integration Files =====

.. admonition:: Download
   :class: download

   `AD-PS0005-RD Design & Integration Files <https://wiki.analog.com/_media/resources/eval/ad-ps0005-rd/ad-ps0005-rd-designsupport.zip>`_

   
   -  Schematic
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   
   |


Help and Support
----------------

.. container:: center round

   Analog Devices will provide **limited** online support for anyone using the reference design with Analog Devices components via the :ez:`EngineerZone Support Community <reference-designs>` forum.


.. |AD-PS0005-RD Board| image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/ad-ps0005-rd_top-angle-evaluation-board.png
   :width: 600px
.. |Simplified System Block Diagram| image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/ad_ps0005_rd_block_diagram.png
.. |AD-PS0005-RD Inputs and Outputs| image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/ad_ps0005_rd_in_out.png
   :width: 600px
.. |AD-PS0005-RD LED Location| image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/ad_ps0005_rd_led.png
   :width: 400px
.. |AD-PS0005-RD Switch Location| image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/ad_ps0005_rd_switches.png
   :width: 600px
.. |AD-PS0005-RD Turrets Location| image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/ad_ps0005_rd_turrets.png
   :width: 600px
.. |AD-PS0005-RD Jumpers Locations| image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/ad_ps0005_rd_jumper.png
   :width: 600px
.. |Sample Setup for Voltage Measurement| image:: https://wiki.analog.com/_media/onunloaddisablefetch/ad_ps0005_rd_setup_voltage.png
   :width: 600px
.. |Sample Setup for Efficiency Test| image:: https://wiki.analog.com/_media/onunloaddisablefetch/ad_ps0005_rd_setup.png
   :width: 600px
.. |Efficiency vs. Load Current| image:: https://wiki.analog.com/_media/maxbatchsizeinbytes/ad_ps0005_rd_efficiency.png
.. |Output Regulation vs Load Current| image:: https://wiki.analog.com/_media/maxbatchsizeinbytes/ad_ps0005_rd_output_regulation.png
.. |DC1613A Connection| image:: https://wiki.analog.com/_media/onunloaddisablefetch/dc1613a_connection.png
   :width: 600px
.. |LTpowerPlay Startup Screen| image:: https://wiki.analog.com/_media/onunloaddisablefetch/ltpowerpay_startup.png
   :width: 600px
.. |LTpowerPlay Main Screen| image:: https://wiki.analog.com/_media/onunloaddisablefetch/ltpowerpay.png
   :width: 600px
