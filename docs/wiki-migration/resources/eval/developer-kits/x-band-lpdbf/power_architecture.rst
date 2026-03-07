Power Architecture
==================

The power tree for this design is broken down into two parts: The on-tile chip power circuitries and the HMC8108 biasing/supply power circuitry. The reason this is done is to draw special attention to the intricacy of the power optimization for the HMC8108.

The power tree for the main circuit highlights a few power components. The :adi:`LTM8063` is a 40V/2A silent switcher uModule regulator that is used to power the ADF5356, MAX5351, LTC6953 and AD9106. Two :adi:`LTM8074` 40V/1.25A silent switcher uModule regulator chips are used to power the 1P0 and 1P8 rails of the AD9083 on the Rx side. A :adi:`LTM8020` 36V/200mA uModule regulator is used to power the ADF5356 and an :adi:`ADP5600` to power the LTC6269. The ADP5600 integrates a low ripple interleaved inverting charge pump with a high performance LDO to easily produce clean negative voltages to the AD8613 and LTC6269. Below is the power tree for the main circuit excluding the HMC8108 biasing/supply circuitry.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_mainpowertree.png
   :width: 600px

**Figure 1: Main Circuit Power Tree**

The power tree for the biasing circuit utilizes a couple of the same silent switching regulator power modules as the main circuit (:adi:`LTM8063` and :adi:`ADP5600`). The drain biasing supply comes from the LTM8063, whereas the gate biasing supplies come from the ADP5600. A detailed breakdown of the HMC8108 biasing and supply circuitry is located in `receiver_front_end_overview\_&_theory_of_operation <https://wiki.analog.com/resources/eval/developer-kits/x-band-lpdbf/receiver_front_end_overview_&_theory_of_operation>`_. Below is the power tree for the biasing/supply circuits.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_biasingcircuitpowertree.png
   :width: 600px

**Figure 2: HMC8108 Biasing/Supply Circuit Power Tree**

The total power per receive channel comes out to about 718mW. The per-part power draw numbers are outlined in the power trees above. Additionally, the table below shows the power numbers per chip family on the board.

+-----------------+-------------------------------------------+-----------------------+-------------------------+
| **Part Number** | **Description**                           | **Quantity on Board** | **Estimated Power (W)** |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| AD9083          | 16 Channel ADC                            | 1                     | 0.989                   |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| LTC6953         | Low-Jitter Clock Distributor              | 1                     | 2.475                   |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| ADF5356         | Microwave Synthesizer with Integrated VCO | 1                     | 0.8124                  |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| LTC6421-20      | Dual-Pack Differential Amplifier          | 8                     | 1.92                    |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| HMC564LC4       | Low Noise Amplifier                       | 1                     | 0.153                   |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| AD8613          | Low Noise CMOS Rail-to-Rail Op Amp        | 1                     | 0.0000684               |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| MAX5351         | 13 Bit Voltage Output DAC                 | 1                     | 0.000842                |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| HMC8108         | Down Mixer                                | 16                    | 4.8                     |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| LT6017          | Precision Op-Amp Quad Pack                | 16                    | 0.016632                |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| AD9106          | 4 Channel DAC/DDS                         | 1                     | 0.315249                |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| HMC516LC5       | Low Noise Amplifier                       | 1                     | 0.195                   |
+-----------------+-------------------------------------------+-----------------------+-------------------------+

**Table 1: Consumption numbers of powered parts on Marlin tile**
