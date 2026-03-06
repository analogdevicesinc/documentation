:doc:`Click here to return Exporting A2B System Configuration files </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles-list>`

Loading Network Configuration from .DAT file
============================================

This file stores network configuration as binary file. The order of bytes in the file is same as the format specified for “Storing Networking Configuration in EEPROM”.

adi_a2b_busconfig.dat
---------------------

This file stores network configuration as binary file. The order of bytes in the file is as below

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   |image2|\


.. container:: centeralign

   |image3|\


.. container:: centeralign

   \


   |image4|

.. container:: centeralign

   |image5|\


.. container:: centeralign

   \


   |image6|

Follow the following steps to use this binary file as input to A2B target software.

-  Define path for the binary file - **A2B_CONF_BINARY_BCF_FILE_URL** in a2bapp_defs.h (. \\Target\\examples\\demo\\a2b-xx\\app\\a2bapp_defs.h)
-  Define macro **‘A2B_FEATURE_EEPROM_OR_FILE_PROCESSING’** and **‘A2B_BCF_FROM_FILE_IO’** in feature.h (. \\Target\\examples\\demo\\a2b-xx\\a2bstack-pal\\a2b\\feature.h)
-  Ensure that **ADI_SIGMASTUDIO_BCF** is not defined (in feature.h)

The advantage of binary file is that network configuration doesn’t have compile time dependency with the target software.

Target application can choose file IO operations or memory read operations to access the .dat file when it is stored on Host PC.

.. note::

   The A2b_System_Autoconfig.dat can also be exported using thrift. For more information, you can refer to :doc:`Export of Busconfig Files using thrift </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`.


.. |image1| image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/image1_dat.png
.. |image2| image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/image2_dat.png
.. |image3| image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/image3_dat.png
.. |image4| image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/image4_dat.png
.. |image5| image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/image5_dat.png
.. |image6| image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/image6_dat.png
