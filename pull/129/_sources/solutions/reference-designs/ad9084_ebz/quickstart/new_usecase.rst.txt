.. _ad9084_ebz quickstart new_usecase:

Running a new JESD mode on hardware
===================================

In order to change the JESD mode or sampling rate of the AD9084-FMCA-EBZ,
you will need to follow the steps below:

#. Generate a new profile using the :ref:`AD9084 (Apollo) Profile Generator <ad9084 profile-generator>`

#. Build the HDL design for your carrier using the same JESD204 parameters as the ones in the profile:

#. Build the Linux image making sure to include the newly generated AD9084 profile

#. Update the clocks and the profile name in the device tree

#. Build the device tree
