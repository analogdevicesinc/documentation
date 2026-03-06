Adding High Quality ASRC
========================

Overview
--------

This article gives a brief overview of how to integrate the Asynchronous Sample Rate Converter library for the SHARC processor.

.. note::

   For more details on the *asrc* command refer to the :doc:`Audio Commands </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/audio-commands>` page.


.. warning::

   This guide assumes user already has access to ASRC library for SHARC ADSP-215xx. Access can be requested from *processor.tools.support@analog.com*.


Details
-------

+-----------------------------------------------------------------------------------------------------------------------+-----------------------------+
| **Step**                                                                                                              | **Example**                 |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------+
| 1. Copy *adi_asrc_pp.h* from *AsynchSampleRateConverter-SH-ADSP215xx-Rel3.0.0/include* to *./SHARC1/include*.         |                             |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------+
| 2. Copy *libadi_asrc_pp_215xx.dlb* from *AsynchSampleRateConverter-SH-ADSP215xx-Rel3.0.0/lib-CCES* to *./SHARC1/lib*. |                             |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------+
| 3. Uncomment the following lines from *./build/makefile*.                                                             | |hq-asrc-makefile-diff.jpg| |
| -                                                                                                                     |                             |
| ARM Section:                                                                                                          |                             |
| *ARM_CFLAGS += -DADI_SHARC_ASRC*                                                                                      |                             |
| SHARC1 section:                                                                                                       |                             |
| - *SHARC1_CFLAGS += -DADI_SHARC_ASRC*                                                                                 |                             |
| - //SHARC1_STATIC_LIBS = ../SHARC1/lib/libadi_asrc_pp_215xx.dlb //                                                    |                             |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------+

.. |hq-asrc-makefile-diff.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/hq-asrc-makefile-diff.jpg
   :width: 400px
