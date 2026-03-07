ADIS16228 EVALUATION ON A PERSONAL COMPUTER
===========================================

.. note::

   UPDATE NOTICE: This Wiki Guide covers the use of evaluation tools (ADIS16228/PCBZ and EVAL-ADISZ) that are no longer available for purchase, but it remains online to support those who already have these tools. For all new :adi:`adis16228` users, please go to the :adi:`ADIS16228's product page <adis16228>`, then click on :adi:`Evaluation Kits <en/products/mems/accelerometers-special-purpose/adis16228.html#product-evaluationkit>` and then click on the **See All** tab to review a listing of the most current :adi:`adis16228` evaluation tools. Thank you!


The :doc:`Vibration Evaluation Program </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram>` enables PC-based evaluation of the :adi:`ADIS16228CMLZ <ADIS16228>`, using the following hardware: :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>` breakout board and :adi:`EVAL-ADIS` evaluation system. Please the following picture for an example of how to use these two devices together for this purpose.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16228-pc-evaluation-setup-picture-02.png
   :width: 300px

PART NUMBERS TO ORDER
=====================

:adi:`Click here to start the online ordering process <en/mems-sensors/mems-accelerometers/adis16228/products/product.html#product-samples>` for the following two parts, or contact your ADI distributor to place the order.

:adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`

:adi:`EVAL-ADISZ <EVAL-ADIS>`

SOFTWARE TO DOWNLOAD
====================

.. include:: vibrationevaluationprogram.rst

PC SYSTEM REQUIREMENTS
======================

.. include:: vibrationevaluationprogram.rst

ADIS16228/PCBZ CONTENTS & SETUP
===============================

The :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>` kit comes with the following materials: (1) ADIS16228CMLZ, (1) interface PCB and (10) M2x0.4x6mm machine screws.

Installing the :adi:`ADIS16228CMLZ <ADIS16228>` onto the interface PCB requires two simple steps:

**Step #1**

Insert the :adi:`ADIS16228CMLZ's <ADIS16228>` flex connector into the mating connector on the interface board, then close the clasp to secure the connection. For more details on this process, please :ez:`click here to see a video demonstration <docs/DOC-2672>`

**Step #2**

Secure the `ADIS16228CMLZ <ad>ADIS16228>`__ to the interface board, using the M2x0.4x6mm machine screws.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16228_pcb_asy_step2_01.jpg
   :width: 200px

EVAL-ADISZ SETUP
================

Use the following two steps to configure the :adi:`EVAL-ADISZ <EVAL-ADIS>` for use with the :adi:`ADIS16228/PCBZ <ADIS16228>`:

**Step #1**

Connect J1 on the :adi:`EVAL-ADISZ <EVAL-ADIS>` to J1 on the :adi:`ADIS16228/PCBZ <ADIS16228>`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16228_pcb_eval-adis-j1-01.jpg
   :width: 300px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16228-pc-evaluation-setup-picture-02.png
   :width: 300px

NOTE: The ribbon cable in this example is not included with the :adi:`EVAL-ADIS` or :adi:`ADIS16228/PCBZ <ADIS16228>`. For more information on where to acquire these types of cables, :ez:`Click here <docs/DOC-2523>` for more information.

**Step #2**

Set JP1 to +3.3V

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-jp1-setting-02.jpg
   :width: 300px

USB DRIVER INSTALLATION
=======================

.. include:: vibrationevaluationprogram.rst

VIBRATION EVALUATION PROGRAM OVERVIEW
=====================================

This section provides a basic description of the functions in the Vibration Evaluation Software package. For a list of `ADIS16228-specific tutorials <https://wiki.analog.com/>`_ that provided detailed, step-by-step instructions for the most common :adi:`ADIS16228` evaluation functions, please `click here <https://wiki.analog.com/>`_.

LAUNCH SOFTWARE
===============

.. include:: vibrationevaluationprogram.rst

KEY PROGRAM FEATURES
====================

The follow sections provide a basic description of each function inside of the Vibration Evaluation Program.

`Click here to access a list of ADIS16228 Tutorials with the Vibration Evaluation Program <https://wiki.analog.com/[/resources/eval/user-guides/inertial-mems/imu/adis16228-pc-eval>`_

.. include:: vibrationevaluationprogram.rst

ADIS16228 VIDEO INSTRUCTIONS
============================

Click on the following links to view quick demonstrations of many :adi:`ADIS16228` functions in the **Vibration Evaluation Program.**

**NOTES**

1) May need to adjust volume up, on the first few on this list.

2) **Internet Explorer** users may need to disable **Protected Mode** to access these videos. Starting at the **Menu Bar**, located in the **Menu Bar**, use the following click path to access the checkbox for enabling and disabling this function: **Tools**>\ **Internet Options**>\ **Security.** Remember to click on **Apply**, then click on **OK** to make sure that these changes take effect, before you try to access these videos.

ADIS16228 VIDEO TUTORIAL LIST
-----------------------------

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VIDEO TITLE/LINK                                                                                                                                                  | SUMMARY                                                                                                                                                                  |
+===================================================================================================================================================================+==========================================================================================================================================================================+
| :ez:`Writing to Registers <servlet/JiveServlet/download/10784-1-22506/ADIS16228_Vid_Tut_RegisterAccess_03.mp4>`                                                   | Register read and write examples, using **Register Access** menu.                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ez:`Manual FFT Mode Demonstration <servlet/JiveServlet/download/10785-1-22507/ADIS16228_Vid_Tut_ManualFFT_03.mp4>`                                               | Manual FFT mode example that uses the **Main Window** drop-down selector and illustrates the resulting register (**REC_CTRL1**) changes in the **Register Access** menu. |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ez:`Automatic FFT Mode Demonstration <servlet/JiveServlet/download/10786-1-22508/ADIS16228_Vid_Tut_AutomaticFFT_03.mp4>`                                         |                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ez:`Sample Rate Control Demonstration <servlet/JiveServlet/download/10787-1-22515/ADIS16228_Vid_Tut_SampleRate_05.mp4>`                                          |                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ez:`Automated Offset Correction Demonstration <servlet/JiveServlet/download/10831-1-22677/ADIS16228_Vid_Tut_AuotmaticBiasCorrection_01.mp4>`                     |                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ez:`Manual FFT/Multi-Record Demonstration <servlet/JiveServlet/download/10811-1-22567/ADIS16228_Vid_Tut_MultiRecord_01.mp4>`                                     |                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ez:`Automatic FFT/Multi-Record Demonstration <servlet/JiveServlet/download/10812-2-22568/ADIS16228_Vid_Tut_MultiRecord_02.mp4>`                                  |                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ez:`Alarm Demonstration <servlet/JiveServlet/download/10832-2-22678/ADIS16228_Vid_Tut_AlarmDemo_01.mp4>`                                                         |                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ez:`Data Capture Demonstration & FFT Header Explanation <servlet/JiveServlet/download/10833-1-22679/ADIS16228_Vid_Tut_DataCapture_01.mp4>`                       |                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
