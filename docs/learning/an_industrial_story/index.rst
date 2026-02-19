Enabling Flexible Data Acquisition Across Mixed Vendor Compute Platforms
================================================================================

ADI DataX™ unifies application portability across heterogeneous
compute environments, enabling reusable workflows for data acquisition and
processing. Developers can scale complexity as needed, from rapid prototyping to
advanced system refinement. The solution highlights modularity, consistency, and
efficiency in building multi‑vendor data pipelines. This approach significantly 
reduces integration overhead and accelerates product development.

Resources
--------------------------------------------------------------------------------
- Zeprhy: :git-zephyr:`ZEPHYR_PROJECT_NAME <ZEPHYR_PROJECT_NAME:>`
- NO-OS: :git-noos:`NO_OS_PROJECT_NAME <NO_OS_PROJECT_NAME:>`
- Linux: :git-linux:`LINUX_PROJECT_NAME <LINUX_PROJECT_NAME:>`
- Hardware: 
  
  - :adi:`AD-APARD32690-SL Rev. E <ad-apard32690-sl>`
  - :adi:`AD-APARDPFW-SL <ad-apardpfw-sl>`
  - :adi:`EVAL-ADIN1110 <eval-adin1110>`
  - :adi:`EVAL-CN0391-ARDZ <cn0391>`
  - :adi:`AD-RPI-T1LPSE-SL <ad-rpi-t1lpse-sl>`

Block diagram
--------------------------------------------------------------------------------

.. figure:: demo_block_diagram.svg
   :align: center


Demo description
--------------------------------------------------------------------------------
This demo illustrates the flexibility of ADI DataX™ in enabling data acquisition
across mixed vendor compute platforms. The system integrates ADI's data 
acquisition hardware with a variety of compute platforms, including Zephyr RTOS 
and NO-OS. The demo showcases the seamless connectivity and data flow between 
the hardware and software components, demonstrating how developers can easily 
build and deploy data acquisition workflows across different environments. By 
leveraging ADI DataX™, developers can focus on application development without 
worrying about the complexities of integration, enabling faster time-to-market 
for their products.

In this demo setup, the Raspberry Pi, running :adi:`Kuiper 2 <kuiper>`, serves
as the central interogation unit, communicating with the ADI hardware components
to acquire data using the  :adi:`AD-RPI-T1LPSE-SL <ad-rpi-t1lpse-sl>` via T1L
connections.

The :adi:`AD-RPI-T1LPSE-SL <ad-rpi-t1lpse-sl>` powers the :adi:`AD-APARDPFW-SL <ad-apardpfw-sl>`
which powers the :adi:`AD-APARD32690-SL <ad-apard32690-sl>` and forwards power 
to the :adi:`EVAL-ADIN1110 <eval-adin1110>`.

To demonstrate the flexibility of DataX™, the :adi:`AD-APARD32690-SL <ad-apard32690-sl>`
runs Zephyr RTOS, while the :adi:`EVAL-ADIN1110 <eval-adin1110>` runs NO-OS. 
Both of the boards have an :adi:`EVAL-CN0391-ARDZ <cn0391>` connected to them, 
which is used to read the temperature using 4 thermocouples each.
The system can be interchaned, by simply compiling the Zephyr application for the 
:adi:`EVAL-ADIN1110 <eval-adin1110>` and the NO-OS application for the
:adi:`AD-APARD32690-SL <ad-apard32690-sl>`, demonstrating the ease of using
DataX™ in enabling data acquisition across mixed vendor compute platforms.


Required Hardware
--------------------------------------------------------------------------------

.. csv-table::
    :file: hardware_table.csv

.. TODO::
    - Build steps for both systems
    - Setup instructions for the Raspberry
    - Scopy results