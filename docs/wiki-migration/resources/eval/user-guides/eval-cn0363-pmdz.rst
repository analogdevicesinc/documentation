EVAL-CN0363-PMDZ User Guide
===========================

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/colorimeter_photo.png
   :width: 600px

The :adi:`EVAL-CN0363-PMDZ <CN0363>` is a dual channel colorimeter featuring a modulated light source transmitter, programmable gain transimpedance amplifiers on each channel, and a very low noise, 24-bit sigma delta ADC. The output of the ADC connects via a standard PMOD connector to a FPGA. The FPGA takes the sampled data from the ADC and implements a synchronous detection algorithm. By using modulated light and digital synchronous detection, rather than a constant (dc) source, the system strongly rejects any noise sources at frequencies other than the modulation frequency, providing excellent accuracy.

The dual channel circuit measures the ratio of light absorbed by the liquids in the sample and reference containers at three different wavelengths. This forms the basis of many chemical analysis and environmental monitoring instruments used to measure concentrations and characterize materials through absorption spectroscopy.

.. tip::

   Further details of the circuit can be found in the circuit note :adi:`CN0363`\


Table of Contents
-----------------

People who follow the flow that is outlined, have a much better experience with things. However, like many things, documentation is never as complete as it should be. If you have any questions, feel free to :doc:`ask </wiki-migration/resources/eval/user-guides/eval-cn0363-pmdz/help_and_support>`.

-  :doc:`Introduction </wiki-migration/resources/eval/user-guides/eval-cn0363-pmdz/introduction>`
-  :doc:`Hardware </wiki-migration/resources/eval/user-guides/eval-cn0363-pmdz/hardware>`
-  Quick Start Guide

   -  :doc:`Hardware setup </wiki-migration/resources/eval/user-guides/eval-cn0363-pmdz/prerequisites>`
   -  :doc:`Linux on ZED </wiki-migration/resources/eval/user-guides/eval-cn0363-pmdz/quickstart/zynq>`

      -  :doc:`Configure a pre-existing SD-Card </wiki-migration/resources/tools-software/linux-software/zynq_images>`
      -  :doc:`Update the old card you received with your hardware </wiki-migration/resources/tools-software/linux-software/zynq_images>`

-  :doc:`Linux Software Support </wiki-migration/resources/eval/user-guides/eval-cn0363-pmdz/software/linux/applications>`

   -  :doc:`EVAL-CN0363-PMDZ Colorimeter Application </wiki-migration/resources/tools-software/linux-software/colorimeter>`
   -  :doc:`Linux device drivers used for the EVAL-CN0363-PMDZ </wiki-migration/resources/eval/user-guides/eval-cn0363-pmdz/software/linux/drivers>`
   -  :doc:`IIO Scope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

-  :doc:`HDL Reference Design </wiki-migration/resources/eval/user-guides/eval-cn0363-pmdz/reference_hdl>` which you must use in your FPGA.
-  :doc:`Help and Support </wiki-migration/resources/eval/user-guides/eval-cn0363-pmdz/help_and_support>`

Warning
-------


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#esd_warning>`_


"=====Registration=====

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/EVAL-CN0363-PMDZ?&v=RevA>`_ to receive all these great benefits and more!


"
