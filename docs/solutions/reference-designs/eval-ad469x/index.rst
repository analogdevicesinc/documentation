.. _eval-ad469x:

EVAL-AD469x
===============================================================================

Overview
-------------------------------------------------------------------------------

Features:

- feature 1
- feature 2

Applications:

- application 1
- application 2

.. toctree::
   :hidden:

   user-guide
   ltspice-guide
   ltspice-transient-sims
   linux-driver
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board:

   #. :ref:`Prerequisites <eval-ad469x-prerequisites>` - what you need to get
      started
   #. :ref:`Quick start guide <eval-ad469x-quickstart>`:

      #. Using the :ref:`ZedBoard <eval-ad469x-quickstart-zedboard>`

   #. Configure an SD Card with
      :doc:`ADI Kuiper Linux </linux/kuiper/index>`

#. Design with the AD469x

   - :ref:`eval-ad469x-block-diagram`

   - :ref:`eval-ad469x-user-guide`

   - :ref:`eval-ad469x-ltspice-guide`

     - :ref:`eval-ad469x-ltspice-transient-sims`

   - Resources for designing a custom AD469x-based platform software

     #. For Linux software:

        #. About the device driver:

           - :ref:`eval-ad469x-linux-driver`

        #. About the device tree:

           - :dokuwiki:`Customizing the device tree on the target <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

     #. :external+hdl:ref:`HDL reference design <ad469x_evb>` which you must
        use in your FPGA.

#. :ref:`Help and Support <help-and-support>`

.. _eval-ad469x-block-diagram:

Block diagram
-------------------------------------------------------------------------------

ADI articles
-------------------------------------------------------------------------------

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Technical support for the evaluation board hardware and software can be obtained
by posting a question to ADI's
:ez:`EngineerZone <data_converters/precision_adcs>` technical support community
for precision ADCs.
