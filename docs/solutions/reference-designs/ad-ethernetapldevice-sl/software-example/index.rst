.. _ethernet-apl-software-example:

Software Examples
=================

Overview
--------

The AD-EthernetAPLDevice-SL board supports two main categories of software
examples, available through public repositories. Both example sets are
designed to be compiled using Code Fusion Studio (CFS) for optimal
compatibility and ease of use.

Prerequisites
-------------

Code Fusion Studio Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before working with any examples, you'll need to install Code Fusion Studio:

* **Download Instructions**: :adi:`Code Fusion Studio Download
  <en/resources/evaluation-hardware-and-software/embedded-development-software/codefusion-studio.html>`

* **User Guide**: `CFS Documentation
  <https://developer.analog.com/docs/codefusion-studio/2.0.0/user-guide/>`_

Security Considerations
~~~~~~~~~~~~~~~~~~~~~~~

While the examples don't require TESA access, the board is fully compatible
with additional security mechanisms. For enhanced security features:

* **Security Resources**: `CFS Security Guide
  <https://developer.analog.com/docs/codefusion-studio/latest/user-guide/resources/security-resources/>`_

MSDK Examples
-------------

The MSDK examples demonstrate peripheral usage through the Maxim HAL
interface. These examples are automatically installed with Code Fusion
Studio.

Loading MSDK Examples
~~~~~~~~~~~~~~~~~~~~~

1. Open Visual Studio Code.
2. Click **Browse MSDK examples**.

    .. figure:: browse-msdk.png

3. Navigate to the **MAX32690** folder.
4. Select your desired example folder.

5. Click **SELECT EXAMPLE**.

     .. figure:: select-example.png

6. Choose your import destination folder.

    .. figure:: destination-folder.png

7. Edit the makefile:

   * Set ``SBT = 0`` to enable binary signature process
   * Save the file

   .. figure:: makefile-config.png

8. Click the **Build** button to compile.

    .. figure:: build.png

----

no-OS Examples
--------------

The no-OS examples are specifically designed for the AD-EthernetAPLDevice-SL
board and utilize the no-OS HAL for direct hardware access.

Loading no-OS Examples
~~~~~~~~~~~~~~~~~~~~~~

1. Follow the :external+no-OS:doc:`build guide <build_guide>`.

2. Switch to the appropriate branch using Git Bash:

   .. code-block:: bash

      git switch release/hockey_puck

3. Refer to the repository's readme file for specific Code Fusion Studio
   loading instructions

.. note::
   Set ``SBT = 0`` in the makefile to disable firmware digital signature
   verification.


