Using the Xilinx ILA in HDL Projects
====================================

This is a guide describing how the ILA helpers can be used to quickly integrate an ILA into your HDL project. Further we will also describe how XVC can be setup to access debug cores remotely without a JTAG connection.

.. tip::

   The contents of this article were developed based on this application note by Xilinx: https://support.xilinx.com/s/article/974879?language=en_US\


ILA Setup
---------

For any ILA setup using the provided helper scripts you will first have to include ``adi_xilinx_ila.tcl`` into your ``system_bd.tcl``:

::

   source $ad_hdl_dir/projects/common/xilinx/adi_xilinx_ila.tcl

Keep in mind to add the dependency to your Makefile:

::

   M_DEPS += ../../common/xilinx/adi_xilinx_ila.tcl

Configuring the debug core
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   Keep in mind that one debug core only supports capturing from a single clock domain. This means that you will need to create a separate debug cores for each domain, which are identified by their clock.


You can allocate a System ILA core from xilinx using the ``ad_ila_setup`` and ``ad_ila_setup_intf`` commands. To capture signals directly use the former variant of the command, for an ILA which can attach to interfaces directly the latter.

Assuming we want to capture the signals in the domain ``sys_cpu_clk`` with a sample depth of 2048 and advanced capturing features enabled:

::

   ad_ila_setup sys_cpu_clk 2048

The full range of options for ad_ila_setup commands is described here:

::

   ## Instantiate an ILA core that can be used to monitor interfaces
   #
   # \param[clk] - The clock domain to which the interfaces are aligned
   # \param[resetn] - The clock domains inverted reset signal
   # \param[depth] - The ILA depth in samples, must be in 2**k, for k in [10, 17]
   # \param[input_pipe_stages] - Input pipeline stages of the ILA core
   # \param[advanced_trigger] - Enable advanced trigger options in the ILA
   # \param[capture_control] - Enable capture control logic in the ILA
   # \param[comparator_count] - Comparator count
   #
   proc ad_ila_setup_intf {clk                       \
                           resetn                    \
                          {depth 1024}               \
                          {input_pipe_stages 1}      \
                          {advanced_trigger {TRUE}}  \
                          {capture_control {TRUE}}   \
                          {comparator_count {0}}     \
                          } {...}

   ## Instantiate an ILA core that can be used to monitor non-interface signals
   #
   # \param[clk] - The clock domain to which the interfaces are aligned
   # \param[depth] - The ILA depth in samples, must be in 2**k, for k in [10, 17]
   # \param[input_pipe_stages] - Input pipeline stages of the ILA core
   # \param[advanced_trigger] - Enable advanced trigger options in the ILA
   # \param[capture_control] - Enable capture control logic in the ILA
   # \param[comparator_count] - Comparator count
   #
   proc ad_ila_setup {clk                       \
                     {depth 1024}               \
                     {input_pipe_stages 1}      \
                     {advanced_trigger {TRUE}}  \
                     {capture_control {TRUE}}   \
                     {comparator_count {0}}     \
                     } {...}

As you can see both are quite similar, except that with interface ILAs an inverted reset signal is required.

.. important::

   Advanced capture controls are enabled by default. Should you try to use these on a device with increased utilization constraints this this might be an issue.


Connecting signals to the core
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once a debug core is setup for the clock domain of your target signals, you can simply call ``ad_ila_connect`` or ``ad_ila_connect_intf`` to connect them to the ILA:

::

   ad_ila_connect sys_cpu_clk sys_ps8/emio_gpio_t

The full command syntax:

::

   ## Connect signal to signal ILA core
   #
   # \param[clk] - The clock domain to which the interfaces are aligned
   # \param[target] - The target pin/port
   #
   proc ad_ila_connect {clk target} {...}

   ## Connect *any* interface to previously instantiated intf ILA core
   #
   # \param[clk] - The clock domain to which the interfaces are aligned
   # \param[target] - The target interface pin/port
   #
   proc ad_ila_connect_intf {clk target} {...}

Xilinx Virtual Cable
--------------------

To make the debugging process more accessible XVC can be used to access the internal JTAG bus from the PS / Userspace.

HDL Project Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

This is facilitated by two debug bridges which work in tandem:

-  The first debug bridge acts as an AXI-BSCAN bridge
-  The second connects the BSCAN signal to the internal debug bridge

The required IP cores can be configured using the ``ad_ila_setup_xvc`` command:

::

   ## Instantiate Xilinx Virtual Cable debug bridge
   #  This procedure will instantiate the two debug bridges that make
   #  up the XVC logic, and hook them up to the main CPU interconnect
   #
   #  \param[cpu_addr] - The address to assign on the AXI bus
   #
   proc ad_ila_setup_xvc {cpu_addr} {...}

A complete debug configuration example covering both interfaces and a plain signal on the ``sys_cpu_clk``:

::

   ad_ila_setup_xvc 0x44A00000

   ad_ila_setup_intf sys_cpu_clk sys_cpu_resetn 2048
   ad_ila_connect_intf sys_cpu_clk axi_cpu_interconnect/S00_AXI
   ad_ila_connect_intf sys_cpu_clk axi_cpu_interconnect/M00_AXI
   ad_ila_connect_intf sys_cpu_clk axi_cpu_interconnect/M01_AXI
   ad_ila_connect_intf sys_cpu_clk sys_ps8/GPIO_0
   ad_ila_connect_intf sys_cpu_clk sys_ps8/SPI_0
   ad_ila_connect_intf sys_cpu_clk sys_ps8/SPI_1

   ad_ila_setup sys_cpu_clk 2048
   ad_ila_connect sys_cpu_clk sys_ps8/emio_gpio_t

Software Configuration
~~~~~~~~~~~~~~~~~~~~~~

This section covers the required software changes.

Linux Kernel Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

The UIO drivers need to be enabled. For this you can update the ``arch/arm64/configs/adi_zynqmp_defconfig``:

::

   CONFIG_UIO_PDRV_GENIRQ=y
   CONFIG_UIO_DMEM_GENIRQ=y

.. tip::

   Note: These are set to be compiled into a module (``m``) by default.


Depending on your target setup ``CPU_IDLE`` must also be disabled, which can be achieved either through the kernel config ``CONFIG_CPU_IDLE=n`` or the kernel command line. With the default Kuiper Linux image CPU idle is already disabled through the command line, thus there are no changes necessary in that regard.

The UIO drivers need to be configured with a kernel command line argument to be available for binding in the device tree using the following argument:

::

   uio_pdrv_genirq.of_id=generic-uio

Finally the debug bridge on the AXI bus should be configured as a UIO device in the device tree:

::

   / {
           fpga_axi: fpga-axi@0 {
                   interrupt-parent = <&gic>;
                   compatible = "simple-bus";
                   #address-cells = <0x1>;
                   #size-cells = <0x1>;
                   ranges = <0 0 0 0xffffffff>;

                   debug_uio: xvc@84a00000 {
                           compatible = "generic-uio";
                           reg = <0x84a00000 0x10000>;
                   };
           };
   };

Userspace Software
^^^^^^^^^^^^^^^^^^

Once you've installed the modified HDL and Kernel, the xvcserver binary need to be configured and installed.

The xvcserver source code is available from Xilinx (https://support.xilinx.com/s/article/974879?language=en_US - see ``XVC_attachments.zip``) or directly from `GitHub <https://gist.githubusercontent.com/Yamakaja/c4bfe4a6235379c0d32939461768509e/raw/e26c993dbacfc98a2f757c1a0a439bb647e57424/xvcserver.c>`__.

Once you've downloaded ``xvcserver.c`` onto the device, you can proceed by configuring the source file to open the correct uio device. You might have to check the kernel logs or sysfs to see which device corresponds to the device tree entry. When using the source file from GitHub, replace the ``UIO_DEVICE`` on line 27 according to your findings: https://gist.github.com/Yamakaja/c4bfe4a6235379c0d32939461768509e#file-xvcserver-c-L27

Finally you may compile and run the xvcserver on the Zynq device:

::

   $ gcc -o xvcserver -march=native xvcserver.c
   $ ./xvcserver

This opens op a TCP server on port 2542 which you can connect to over ethernet.

Debugging with XVC
------------------

Finally to connect to the ``xvcserver`` open the Vivado Hardware Manager:

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/xilinx_ila/xilinx_hardware_manager_0.png

Open the ``Open new Hardware Target`` wizard:

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/xilinx_ila/xilinx_hardware_manager_1.png

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/xilinx_ila/xilinx_hardware_manager_2.png

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/xilinx_ila/xilinx_hardware_manager_3.png

<Insert missing pictures>

Before you can get started with the debugging process you will have to load debug information which was generated during implementation into the debugger. The required ``.ltx`` file can be found at ``*.runs/impl_1/system_top.ltx``.

At this point you can begin using the ILA just like with a direct connection.
