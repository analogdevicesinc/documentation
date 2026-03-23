EVAL-CN0363-PMDZ User Guide
===========================

.. image:: images/colorimeter_photo.png
   :width: 600

The :adi:`EVAL-CN0363-PMDZ <CN0363>` is a dual channel colorimeter featuring a modulated light source transmitter, programmable gain transimpedance amplifiers on each channel, and a very low noise, 24-bit sigma delta ADC. The output of the ADC connects via a standard PMOD connector to a FPGA. The FPGA takes the sampled data from the ADC and implements a synchronous detection algorithm. By using modulated light and digital synchronous detection, rather than a constant (dc) source, the system strongly rejects any noise sources at frequencies other than the modulation frequency, providing excellent accuracy.

The dual channel circuit measures the ratio of light absorbed by the liquids in
the sample and reference containers at three different wavelengths. This forms
the basis of many chemical analysis and environmental monitoring instruments
used to measure concentrations and characterize materials through absorption
spectroscopy.

.. tip::

   Further details of the circuit can be found in the circuit note :adi:`CN0363`\

Table of Contents
-----------------

People who follow the flow that is outlined, have a much better experience with things. However, like many things, documentation is never as complete as it should be. If you have any questions, feel free to :doc:`ask </solutions/reference-designs/cn0363/help_and_support>`.

-  :doc:`Introduction </solutions/reference-designs/cn0363/introduction>`
-  :doc:`Hardware </solutions/reference-designs/cn0363/hardware>`
-  Quick Start Guide

   -  :doc:`Hardware setup </solutions/reference-designs/cn0363/prerequisites>`
   -  :doc:`Linux on ZED </solutions/reference-designs/cn0363/quickstart/zynq>`

      -  `Configure a pre-existing SD-Card <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_
      -  `Update the old card you received with your hardware <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_

-  :doc:`Linux Software Support </solutions/reference-designs/cn0363/software/linux/applications>`

   -  `EVAL-CN0363-PMDZ Colorimeter Application <https://wiki.analog.com/resources/tools-software/linux-software/colorimeter>`_
   -  :doc:`Linux device drivers used for the EVAL-CN0363-PMDZ </solutions/reference-designs/cn0363/software/linux/drivers>`
   -  `IIO Scope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_

-  :doc:`HDL Reference Design </solutions/reference-designs/cn0363/reference_hdl>` which you must use in your FPGA.
-  :doc:`Help and Support </solutions/reference-designs/cn0363/help_and_support>`

Warning
-------

.. esd-warning::

"=====Registration=====

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/EVAL-CN0363-PMDZ?&v=RevA>`_ to receive all these great benefits and more!

"


.. toctree::
   :hidden:

   hardware
   help_and_support
   introduction
   prerequisites
   quickstart/zynq
   reference_hdl
   software/linux/applications
   software/linux/drivers
