No-OS Build System
==================

::

   make

This is the complete compilation process. It is made up of three rules, that can be used separately: project, update, build

<code> make project </code> - creates the ``build`` directory and the required directory structure

- uses SDK to create a project under the ``build`` directory <code> make update </code> - updates the no-OS sources under the ``build`` directory with files specified in ``src.mk`` <code> make build </code> - performs the build of files under the ``build`` directory using gcc <code> make sdkbuild </code> - performs the build of files under the ``build`` directory using SDK

When modifications are performed, the following three commands trigger the necessary clean actions: <code> make clean </code> - deletes the artifacts generated during build <code> make reset </code> - deletes the ``build`` directory (this results in a fresh setup for starting the complete compilation process) <code> make sdkclean </code> - cleans the artifacts (.o, .elf, .hex, etc.) created by the build command using the SDK

<code> make run </code> - downloads and runs the executable on the target board

<code> make debug </code> - downloads the executable on the target board and opens a command-line ``gdb`` instance to debug it (only on some platforms)

Workflows
---------

.. image:: https://wiki.analog.com/_media/resources/no-os/workflows.drawio_1_.svg
   :align: center

Compilation Using Generic Tools
-------------------------------

.. image:: https://wiki.analog.com/_media/resources/no-os/workflownosdk.drawio_1_.svg
   :align: center

Compilation Using Platform-Specific Tools
-----------------------------------------

.. image:: https://wiki.analog.com/_media/resources/no-os/workflowsdk.drawio_1_.svg
   :align: center
