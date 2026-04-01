:orphan:

Reference Design Documentation Templates
================================================================================

This directory contains reusable reStructuredText (RST) templates for
generating consistent documentation for Analog Devices reference designs.

Overview
--------------------------------------------------------------------------------

The template system uses Jinja2-based RST templates to generate
comprehensive documentation for ADI evaluation boards and reference
designs. This ensures consistency across different projects while allowing
customization through template variables.

Available Templates
--------------------------------------------------------------------------------

1. Prerequisites Template (``prerequisites.rst.jinja``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A reusable template for generating the prerequisites section of
documentation. This template provides a standardized way to document the
hardware and software requirements for any reference design.

Prerequisites Template Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 20 10 70

   * - Variable
     - Type
     - Description
   * - ``prerequisites_ref``
     - string
     - Reference ID for cross-linking (e.g., "adrv9002 prerequisites")
   * - ``chip_name``
     - string or list
     - Name(s) of the chip(s) used in the evaluation board.
       Accepts a single string (e.g., ``ADRV9002``) or a list
       for multiple chips (e.g., ``[AD9162, AD9625]``). Each
       entry is rendered as an ADI product link, separated
       by "/".
   * - ``eval_board``
     - string or list
     - Name(s) of the ADI evaluation board(s). Accepts a single
       string (e.g., ``EVAL-ADRV9002``) or a list for multiple
       boards (e.g., ``[AD-FMCOMMS11-EBZ, AD-FMCOMMS12-EBZ]``).
       Each entry is rendered as an ADI product link, separated
       by "/". The label automatically pluralizes to "boards"
       when multiple entries are provided.
   * - ``carriers_ref``
     - string
     - Reference to the carriers/supported platforms section (e.g.,
       "adrv9002 carriers")
   * - ``has_linux``
     - boolean
     - Whether the project uses Linux. When true, an SD card
       requirement is included in the hardware prerequisites.
   * - ``has_rf_test_equipment``
     - boolean
     - Whether RF test equipment is required
   * - ``additional_hardware``
     - list
     - Additional hardware items to list in the hardware prerequisites
       section
   * - ``additional_software``
     - list
     - Additional software items to list in the software prerequisites
       section

Prerequisites Usage Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: rst

   .. include-template:: ../template/prerequisites.rst.jinja

      prerequisites_ref: adrv9002 prerequisites
      chip_name: ADRV9002
      eval_board: EVAL-ADRV9002
      carriers_ref: adrv9002 carriers
      has_linux: true
      has_rf_test_equipment: true
      additional_hardware:
        - USB-JTAG programmer for FPGA configuration
        - Coaxial cables for RF connections
      additional_software:
        - MATLAB R2023a or later for data analysis
        - Vivado 2024.1 for HDL development

The prerequisites template automatically generates sections for:

- **Hardware prerequisites**: Including the evaluation board, FPGA carrier
  platform, connectivity options, and SD card requirements (if Linux is
  enabled)
- **Software prerequisites**: Including required development tools

2. ZedBoard Quick Start Template (``quickstart/zed.rst.jinja``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A comprehensive template for generating ZedBoard quick start guides for
ADI evaluation boards. It supports both Linux and no-OS software
configurations.

Quick Start Template Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Required Variables
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. list-table::
   :header-rows: 1
   :widths: 25 10 65

   * - Variable
     - Type
     - Description
   * - ``quickstart_ref``
     - string
     - Reference ID for the quick start guide (e.g., "adrv9002-zed")
   * - ``eval_board``
     - string
     - Name of the ADI evaluation board (e.g., "EVAL-ADRV9002")
   * - ``hdl_project_doc``
     - string
     - HDL project documentation path for Sphinx reference (e.g.,
       "adrv9001")
   * - ``prerequisites_ref``
     - string
     - Reference to prerequisites section

Optional Variables
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**General Configuration**

- ``has_linux`` (boolean): Enable Linux software section
- ``has_no_os`` (boolean): Enable no-OS software section
- ``has_lvds_support`` (boolean): Show LVDS support warning for ZedBoard
- ``has_jesd`` (boolean): Show JESD204 status utility section (only if
  design has JESD support)
- ``quickstart_image`` (path): Image showing the complete setup
- ``has_vadj_warning`` (boolean): Show VADJ voltage warning (applies to
  both Linux and no-OS)
- ``has_vadj_led`` (boolean): Show VADJ LED information (applies to both
  Linux and no-OS)
- ``vadj_led_image`` (path): Image of the VADJ LED indicator (applies to
  both Linux and no-OS)

**Linux-Specific Variables**

- ``linux_setup_steps_file`` (path): File with Linux setup steps
- ``boot_log_file`` (path): File containing the boot log output
- ``linux_additional_hardware`` (list): Additional hardware items needed
- ``linux_has_loopback`` (boolean): Show loopback configuration note for
  Linux

**No-OS Specific Variables**

- ``no_os_project_path`` (path): Path to no-OS project in git repo (e.g.,
  "projects/adrv9001")
- ``no_os_project_specific_doc`` (string): no-OS project-specific
  documentation path for Sphinx reference (e.g.,
  "projects/rf-transceiver/adrv9001")
- ``no_os_setup_image`` (path): Image showing no-OS setup
- ``no_os_setup_steps_file`` (path): File with no-OS setup steps
- ``no_os_console_output_file`` (path): File with console output
- ``no_os_additional_hardware`` (list): Additional hardware for no-OS
- ``no_os_has_loopback`` (boolean): Show loopback configuration note for
  no-OS

Quick Start Usage Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: rst

   .. include-template:: ../../template/quickstart/zed.rst.jinja

      quickstart_ref: adrv9002-zed
      eval_board: EVAL-ADRV9002
      has_linux: true
      has_no_os: true
      has_lvds_support: true
      hdl_project_doc: template_project
      prerequisites_ref: adrv9002 prerequisites
      quickstart_image: ../images/adrv9002_zed_quickstart.png
      has_vadj_warning: true
      has_vadj_led: true
      vadj_led_image: ../images/adrv9002_vadj_led.png
      has_jesd: true
      linux_has_loopback: true
      no_os_has_loopback: true

Quick Start Template Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The quickstart template generates the following sections:

1. **Introduction** - Overview with ZedBoard image and ESD warning
2. **LVDS Support** (optional) - Warning about LVDS limitations on
   ZedBoard
3. **Linux Section** (if ``has_linux: true``)

   - Necessary files (BOOT.bin, uImage, devicetree.dtb)
   - Required software and hardware
   - Testing and setup instructions:

     - Creating the setup with optional quickstart image
     - Loopback configuration note (optional)
     - ESD warning
     - VADJ voltage warning and LED information (optional)
     - Setup steps from included file
     - USB-OTG and jumper settings notes

   - Boot messages (collapsible)
   - Useful serial terminal commands (ifconfig, iio_info, poweroff,
     reboot, etc.)
   - JESD204 status utility (optional, if ``has_jesd: true``)

4. **No-OS Section** (if ``has_no_os: true``)

   - Necessary files (system_top.xsa and no-OS project)
   - Required software (Vivado/Vitis, UART terminal)
   - Required hardware
   - Testing and setup instructions:

     - Creating the setup with optional setup image
     - Loopback configuration note (optional)
     - ESD warning
     - VADJ voltage warning and LED information (optional)
     - Setup steps from included file
     - Jumper settings reference

   - Console output (collapsible)

Example Implementations
--------------------------------------------------------------------------------

See these example implementations in the repository:

- ``../adrv9002/quickstart/zed.rst`` - ZedBoard quickstart with Linux
  and no-OS
- ``../adrv9002/prerequisites.rst`` - Prerequisites example

Path Conventions
--------------------------------------------------------------------------------

- Image paths should be relative to the file that includes the template
- Common files (like setup steps) can be included from the same directory
- Use ``../images/`` for images in the project's images folder
- Use ``../files/`` for binary artifacts and downloadable files (e.g.,
  .zip, .pdf, .docx, .bin, .exe)

Project Structure Guidelines
--------------------------------------------------------------------------------

Each reference design project should follow this directory structure:

.. code-block:: text

   project/
   ├── index.rst                 # Main documentation files (RST only)
   ├── prerequisites.rst
   ├── user-guide.rst
   ├── images/                   # Image files only (.png, .jpg, etc.)
   │   ├── project_setup.png
   │   └── ...
   ├── files/                    # Binary artifacts and downloads
   │   ├── firmware.zip
   │   ├── datasheet.pdf
   │   ├── configuration.bin
   │   └── ...
   └── quickstart/
       ├── zed.rst
       └── ...

**Do NOT place binary files directly in the project root:**

❌ **Bad:**

.. code-block:: text

   project/
   ├── index.rst
   ├── My_beautiful.pptx        # Don't do this!
   ├── someZipfile.zip          # Don't do this!
   ├── finalVersion1234.exe     # Don't do this!

✅ **Good:**

.. code-block:: text

   project/
   ├── index.rst
   ├── images/
   │   └── diagrams.png
   └── files/
       ├── presentation.pptx
       ├── archive.zip
       └── installer.exe

This keeps the project directory clean and organized, making it easier to
navigate and maintain.

Variable Naming Conventions
--------------------------------------------------------------------------------

- **General variables** shared by both Linux and no-OS: no prefix (e.g.,
  ``has_vadj_warning``, ``has_vadj_led``, ``vadj_led_image``)
- **Linux-specific variables**: prefix with ``linux_`` (e.g.,
  ``linux_setup_steps_file``, ``linux_additional_hardware``,
  ``linux_has_loopback``)
- **No-OS-specific variables**: prefix with ``no_os_`` (e.g.,
  ``no_os_project_path``, ``no_os_setup_image``, ``no_os_has_loopback``)

Notes
--------------------------------------------------------------------------------

- All boolean variables default to ``false`` if not specified
- Image sections are only rendered if both the flag is ``true`` AND the
  image path is provided
- Both Linux and no-OS sections share VADJ warnings and VADJ LED
  information using the same general variables
- Loopback configuration notes are separate for Linux
  (``linux_has_loopback``) and no-OS (``no_os_has_loopback``)
