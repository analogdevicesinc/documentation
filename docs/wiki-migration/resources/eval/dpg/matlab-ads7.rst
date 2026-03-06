Using MATLAB with ADS7 Series Pattern Generators
================================================

This page provides information on using MATLAB with the ADS7 series of pattern generators for high speed DAC evaluation.

For information on using MATLAB with DPG3, see :doc:`Using MATLAB With the DPG </wiki-migration/resources/eval/dpg/matlab>`.

Code Samples
------------

General Requirements
~~~~~~~~~~~~~~~~~~~~

::

   *High Speed DAC evaluation board (see [[/resources/eval/dpg/eval-ad9162|AD9161/AD9162/AD9163/AD9164 Evaluation Boards]])
   *ADS7-V1/-V2 pattern generator (see [[/resources/eval/dpg/ads7|ADS7-V1/-V2 for High-Speed DAC Evaluation]])
   *DPGDownloader software for controlling the pattern generator (see [[/resources/eval/dpg/dacsoftwaresuite|High-Speed DAC Software Suite]])
   *ACE software for configuring the eval board (see [[/resources/tools-software/ace|Analysis | Control | Evaluation (ACE) Software]])
   *Recent version of MATLAB (e.g. R2014b)

This table contains a list of downloadable MATLAB sample scripts for various high speed DAC evaluation boards. The script source code is wrapped up in a zip file. Once downloaded, the zip file should be extracted to a folder of your choice.

+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+--------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| Eval Board                                                     | Download                                                                                                                                                                                          | Last Update | DPG Device                                                   | SW Requirements                                                                                |
+================================================================+===================================================================================================================================================================================================+=============+==============================================================+================================================================================================+
| :doc:`AD9162 </wiki-migration/resources/eval/dpg/eval-ad9162>` | `Single Tone Gen for AD9162 <https://wiki.analog.com/_media/resources/eval/dpg/ad9162_matlab_06062018.zip>`__ (`Read Me <https://wiki.analog.com/_media/resources/eval/dpg/ad9162_readme.pdf>`__) | 6/6/2018    | :doc:`ADS7-V1/-V2 </wiki-migration/resources/eval/dpg/ads7>` | :doc:`DPGDownloader </wiki-migration/resources/eval/dpg/dacsoftwaresuite>`, :adi:`ace`         |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+--------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| :doc:`AD9172 </wiki-migration/resources/eval/dpg/eval-ad9172>` | `Single Tone Gen for AD9172 <https://wiki.analog.com/_media/resources/eval/dpg/ad9172_matlab_06132018.zip>`__ (`Read Me <https://wiki.analog.com/_media/resources/eval/dpg/ad9172_readme.pdf>`__) | 6/13/2018   | :doc:`ADS8-V1 </wiki-migration/resources/eval/dpg/ads7>`     | :doc:`DPGDownloader </wiki-migration/resources/eval/dpg/dacsoftwaresuite>`, :adi:`ace`         |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+--------------------------------------------------------------+------------------------------------------------------------------------------------------------+
