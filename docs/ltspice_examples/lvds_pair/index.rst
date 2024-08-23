LTspice Example: LVDS pair
===============================================================================

Quick and dirty example of what a documented LTspice example on GitHub might look like. The folder for this exact page is at:

`Source and LTspice simulation for this page <https://github.com/mthoren-adi/documentation/tree/main/docs/ltspice_examples/lvds_pair>`__

Pages are "atomic" and can be moved around.

(Forgive the table of contents and sidebar navigation, mthoren-adi is still figuring that out.)



Objective:
----------

To simulate the behavior of a perfect LVDS transmitter driving the input capacitance of an FPGA.

Download the LTspice simulation here:

:download:`LVDS_FPGA_signal_integrity.asc <LVDS_FPGA_signal_integrity.asc>`

Here is how to number figures: :numref:`fig-lvds_screenshot` is a screenshot of the LTspice simulation (you can screenshot waveforms, etc. too, of course):


.. _fig-lvds_screenshot:

.. figure:: lvds_pair_ltspice_screenshot.png
   :align: center
   :width: 600

   Screenshot of LVDS simulation


Here is an example of embedding a video. Who better to describe the subtleties of signal Integrity than this expert?

.. video:: https://www.youtube.com/watch?v=dQw4w9WgXcQ



If there is a complaint or edit needed to an LTspice simulation or the document itself, it's a pull request like any other. Anyone inside ADI or outside can start a PR, but the admin's approval is needed to merge. Here is a case where a professor found an error in the LTspice simulation from this Active Learning exercise (the 50-ohm output impedance of the ADALM2000 was not included):

:dokuwiki:`Activity: Transient Response of an RL Circuit - ADALM2000 <university/courses/electronics/rl_transient_response>`

Here is the pull request:

`Pull Request <https://github.com/analogdevicesinc/education_tools/pull/49/>`_

And the details of the files changed:

`Pull Request Files Changed <https://github.com/analogdevicesinc/education_tools/pull/49/files>`_

How cool would it be to have a visual diffing tool for this? There is a company that does this sort of thing for PCB design files. We could do one for LTspice.


Generic warning banner example:

Warning
-------------------------------------------------------------------------------

.. esd-warning::


.. toctree::

   ltspice_examples/index