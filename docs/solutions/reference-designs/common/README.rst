:orphan:

Common Templates
================================================================================

This directory contains reusable reStructuredText (RST) templates for
software tools documentation used across ADI reference designs.

Overview
--------------------------------------------------------------------------------

The common templates provide standardized documentation sections for:

- **IIO Oscilloscope** (``using-iio-osc.rst.jinja``) - ADI IIO
  Oscilloscope application documentation
- **Scopy** (``using-scopy.rst.jinja``) - Scopy software toolbox
  documentation

These templates are designed to be included in project-specific
quickstart guides to maintain consistency across documentation.

----

using-iio-osc.rst.jinja
--------------------------------------------------------------------------------

Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This template provides documentation for the ADI IIO Oscilloscope
application, a cross-platform tool for interfacing with IIO devices. It
supports both Linux and no-OS environments.

Template Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Optional Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 10 60

   * - Variable
     - Type
     - Description
   * - ``has_linux``
     - boolean
     - Show Linux section (default: false)
   * - ``has_no_os``
     - boolean
     - Show no-OS section (default: false)
   * - ``connection_image``
     - path
     - Image showing IIO Oscilloscope connection (Linux only)
   * - ``iio_has_plugin``
     - boolean
     - Enable plugin section
   * - ``iio_plugin_ref``
     - string
     - Reference to IIO plugin documentation (required if
       ``iio_has_plugin`` is true)
   * - ``iio_show_data_capture``
     - boolean
     - Enable data capture section
   * - ``iio_show_time_domain``
     - boolean
     - Show time domain plot (requires ``iio_show_data_capture``)
   * - ``iio_time_domain_image``
     - path
     - Time domain capture image (required if ``iio_show_time_domain``
       is true)
   * - ``iio_show_frequency_domain``
     - boolean
     - Show frequency domain plot (requires ``iio_show_data_capture``)
   * - ``iio_frequency_domain_image``
     - path
     - Frequency domain capture image (required if
       ``iio_show_frequency_domain`` is true)

Usage Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**For Linux only:**

.. code-block:: rst

   .. include-template:: ../../common/using-iio-osc.rst.jinja

      has_linux: true
      connection_image: ../images/ADRV9002_IIO_connection_zed.png
      iio_has_plugin: true
      iio_plugin_ref: adrv9002-plugin
      iio_show_data_capture: true
      iio_show_time_domain: true
      iio_time_domain_image: ../images/ADRV9002_time_domain.png
      iio_show_frequency_domain: true
      iio_frequency_domain_image: ../images/ADRV9002_frequency_domain.png

**For both Linux and no-OS:**

.. code-block:: rst

   .. include-template:: ../../common/using-iio-osc.rst.jinja

      has_linux: true
      has_no_os: true
      connection_image: ../images/ADRV9002_IIO_connection_zed.png
      iio_has_plugin: true
      iio_plugin_ref: adrv9002-plugin
      iio_show_data_capture: true
      iio_show_time_domain: true
      iio_time_domain_image: ../images/ADRV9002_time_domain.png
      iio_show_frequency_domain: true
      iio_frequency_domain_image: ../images/ADRV9002_frequency_domain.png

Template Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The template generates different sections based on ``has_linux`` and
``has_no_os`` variables:

**Common sections (always shown):**

1. **ADI IIO Oscilloscope** - Introduction

**For Linux (if ``has_linux: true``):**

2. **For Linux** section containing:

   - **Remote run on host** - Instructions for connecting from a host PC
     via IP (with optional connection image)
   - **Locally run on the board** - Instructions for running on the FPGA
     with HDMI monitor

**For no-OS (if ``has_no_os: true``):**

3. **For no-OS** section - Instructions for enabling IIOD with make flag

**Optional sections:**

4. **Plugin** (if ``iio_has_plugin: true``) - Device-specific plugin
   information
5. **Data capture** (if ``iio_show_data_capture: true``) - Time domain
   and/or frequency domain plots

----

using-scopy.rst.jinja
--------------------------------------------------------------------------------

Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This template provides documentation for Scopy, ADI's cross-platform
software toolbox for interfacing with ADI devices. It includes
information about device connection methods, plugins, and data
visualization.

Template Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Optional Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 35 10 55

   * - Variable
     - Type
     - Description
   * - ``scopy_has_plugin``
     - boolean
     - Enable plugin section
   * - ``scopy_plugin_path``
     - string
     - Path to Scopy plugin documentation (required if
       ``scopy_has_plugin`` is true)
   * - ``scopy_show_data_capture``
     - boolean
     - Enable data capture section
   * - ``scopy_show_time_domain``
     - boolean
     - Show time domain plot (requires ``scopy_show_data_capture``)
   * - ``scopy_time_domain_image``
     - path
     - Time domain capture image (required if ``scopy_show_time_domain``
       is true)
   * - ``scopy_show_frequency_domain``
     - boolean
     - Show frequency domain plot (requires ``scopy_show_data_capture``)
   * - ``scopy_frequency_domain_image``
     - path
     - Frequency domain capture image (required if
       ``scopy_show_frequency_domain`` is true)

Usage Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. include-template:: ../../common/using-scopy.rst.jinja

      scopy_has_plugin: true
      scopy_plugin_path: plugins/adrv9002/adrv9002
      scopy_show_data_capture: true
      scopy_show_time_domain: true
      scopy_time_domain_image: ../images/ADRV9002_scopy_time_domain.png
      scopy_show_frequency_domain: true
      scopy_frequency_domain_image: ../images/ADRV9002_scopy_frequency_domain.png

Template Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The template generates the following sections:

1. **Scopy** - Introduction to Scopy toolbox
2. **Connection Methods** - General instructions on connecting devices:

   - Automatic device scanning in home section
   - Manual connection methods (IP, USB, serial port, URI)
   - Example connection screenshots (hard-coded, not customizable)

3. **Plugin** (optional) - Device-specific plugin information with
   external link
4. **Data capture** (optional) - Time domain and/or frequency domain
   plots

Connection Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The template includes built-in documentation about Scopy connection
methods:

- **Automatic scanning** - Devices appear automatically when scan is ON
- **Manual connection** - Via IP address, USB, serial port, or static/
  dynamic URI
- **Connection images** - Two reference images showing:

  - Device scan interface (``../../images/Scopy_connection1.png``)
  - Connection options interface (``../../images/Scopy_connection2.png``)

These images are hard-coded in the template and not customizable per
project.

----

Path Conventions
--------------------------------------------------------------------------------

- Image paths should be relative to the file that includes the template
- Use ``../images/`` for images in the project's images folder
- Connection images for Scopy use ``../../images/`` to reference common
  images in the reference-designs root

Notes
--------------------------------------------------------------------------------

- All boolean variables default to ``false`` if not specified
- Image sections are only rendered if both the flag is ``true`` AND the
  image path is provided
- Variable naming convention:

  - IIO Oscilloscope variables: prefix with ``iio_`` (e.g.,
    ``iio_has_plugin``, ``iio_show_data_capture``)
  - Scopy variables: prefix with ``scopy_`` (e.g.,
    ``scopy_has_plugin``, ``scopy_show_data_capture``)

Plugin Path Formats
--------------------------------------------------------------------------------

IIO Oscilloscope Plugin Reference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Uses internal Sphinx reference: ``:ref:`{{ iio_plugin_ref }}```
- Example: ``iio_plugin_ref: adrv9002-plugin``

Scopy Plugin Path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Uses external documentation link:
  ``:external+scopy:doc:`here <{{ scopy_plugin_path }}>```
- Path should be relative to Scopy documentation root
- Example: ``scopy_plugin_path: plugins/adrv9002/adrv9002``
- Generates link to:
  https://analogdevicesinc.github.io/scopy/plugins/adrv9002/adrv9002.html

Example Integration
--------------------------------------------------------------------------------

These templates are typically included in quickstart guides. See the
zed.rst template for a complete integration example:

.. code-block:: rst

   .. include-template:: ../../common/using-iio-osc.rst.jinja
      os_type: linux
      connection_image: ../images/ADRV9002_IIO_connection_zed.png
      iio_has_plugin: true
      iio_plugin_ref: adrv9002-plugin

   .. include-template:: ../../common/using-scopy.rst.jinja
      scopy_has_plugin: true
      scopy_plugin_path: plugins/adrv9002/adrv9002

This creates documentation for both IIO Oscilloscope and Scopy in
sequence.
