:orphan:

Test Necessary Files Template
===============================================================================

Zynq
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include-template:: necessary_files.rst.jinja

   fpga_family: zynq
   hdl_project_doc: adrv9009

ZynqMP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include-template:: necessary_files.rst.jinja

   fpga_family: zynqmp
   hdl_project_doc: adrv9009

Versal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include-template:: necessary_files.rst.jinja

   fpga_family: versal
   hdl_project_doc: adrv9009

Versal (VCK190)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include-template:: necessary_files.rst.jinja

   fpga_family: versal
   hdl_project_doc: adrv9009
   carrier: vck190

Microblaze
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include-template:: necessary_files.rst.jinja

   fpga_family: microblaze
   hdl_project_doc: adrv9009

Agilex 7 SoC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include-template:: necessary_files.rst.jinja

   fpga_family: agilex7soc
   hdl_project_doc: adrv9009

Stratix 10 SoC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include-template:: necessary_files.rst.jinja

   fpga_family: stratix10
   hdl_project_doc: adrv9009

Arria 10 SoC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include-template:: necessary_files.rst.jinja

   fpga_family: a10soc
   hdl_project_doc: adrv9009

Cyclone 5 SoC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include-template:: necessary_files.rst.jinja

   fpga_family: cyclone5
   hdl_project_doc: cn0540

Zynq (not in Kuiper)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include-template:: necessary_files.rst.jinja

   fpga_family: zynq
   hdl_project_doc: adrv9009
   in_kuiper: false
   hdl_branch: "projects/ad4080_fmc_evb"
   linux_branch: "staging/ad4080_clean_adf4350:"
