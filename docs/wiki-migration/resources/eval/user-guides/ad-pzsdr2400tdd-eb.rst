AD-PZSDR2400TDD-EB User Guide
=============================

The :adi:`AD-PZSDR2400TDD-EB` is affectionately dubbed the first 'RF personality card'. It plugs into the ADRV1CRR-FMC :adi:`ADRV1CRR-FMC.html <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADRV1CRR-FMC.html>` carrier card. 35mm U.FL coaxial cables connect the card to the ADRV9361-Z7035 :adi:`ADRV9361-Z7035.html#eb-overview <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADRV9361-Z7035.html#eb-overview>` providing access to the transmit and receive inputs of the :adi:`AD9361`. Information on the card, how to use it, the design package that surrounds it, and the software which can make it work, can be found here.

The purpose of the :adi:`AD-PZSDR2400TDD-EB` is to provide the user with a tunable path to condition the transmit or receive signals of the :adi:`AD9361`. Selection of TX or RX path is achieved by the 200MHz to 2.7GHz SPDT switch :adi:`HMC546LP2` controlled by the FPGA and accompanying software. The transmit path consists of a 2.4GHz filter, half watt driver amplifier :adi:`ADL5324` and 2 watt power amplifier :adi:`HMC921`. The receive path consists of the same 2.4GHz filter as well as a low loss LNA :adi:`HMC669`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pzsdr2400tdd-ebz/pcb_top.jpg
   :align: center
   :width: 600px

Table of Contents
-----------------

People who follow the flow that is outlined, have a much better experience with things. However, like many things, documentation is never as complete as it should be. If you have any questions, feel free to :doc:`ask </wiki-migration/resources/eval/user-guides/ad-pzsdr2400tdd-eb/help_and_support>`.

-  :doc:`Introduction </wiki-migration/resources/eval/user-guides/ad-pzsdr2400tdd-eb/introduction>`
-  :doc:`Hardware </wiki-migration/resources/eval/user-guides/ad-pzsdr2400tdd-eb/hardware>`: This provides a brief description of the board by itself, and is a good reference for those who want to understand a little more about the board. If you just want to use the board, you can skip this section, and come back to it when you want to incorporate the AD9361 into your product.

   -  :doc:`Hardware </wiki-migration/resources/eval/user-guides/ad-pzsdr2400tdd-eb/hardware>` (including :doc:`schematics </wiki-migration/resources/eval/user-guides/ad-pzsdr2400tdd-eb/hardware>`)

      -  :doc:`Functional Overview & Specifications </wiki-migration/resources/eval/user-guides/ad-pzsdr2400tdd-eb/hardware/functional_overview>`
      -  :doc:`Configuration options </wiki-migration/resources/eval/user-guides/ad-pzsdr2400tdd-eb/hardware/configuration_options>`
      -  :doc:`Characteristics and Performance </wiki-migration/resources/eval/user-guides/ad-pzsdr2400tdd-eb/hardware/characteristics_and_performance>`
      -  :doc:`Layout Considerations </wiki-migration/resources/eval/user-guides/ad-pzsdr2400tdd-eb/hardware/layout_considerations>`
      -  :doc:`FCC or CE certification </wiki-migration/resources/eval/user-guides/ad-pzsdr2400tdd-eb/hardware/fcc_or_ce_certification>`

   -  :doc:`Software </wiki-migration/resources/eval/user-guides/ad-pzsdr2400tdd-eb/software>`

-  :doc:`Help and Support </wiki-migration/resources/eval/user-guides/ad-pzsdr2400tdd-eb/help_and_support>`

.. image:: https://wiki.analog.com/_media/analogTV>4840956066001
   :alt: analogTV>4840956066001
   :align: center

Warning
-------

.. esd-warning::

