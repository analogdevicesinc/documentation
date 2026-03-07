FTC 2025: JESD204 Deep Dive
===========================

The JESD204 Deep Dive session will have two instructor lead demos. Repeating the demos is optional, but if you wish to follow along, please have the following completed before the session:

-  Setup python with the necessary dependencies
-  Download the pyadi-jif repo including examples

Install Python 3.9 Virtual Environment
--------------------------------------

First open a PowerShell terminal (or terminal in macOS or Linux).

Next, install the `uv <https://docs.astral.sh/uv/getting-started/installation/#standalone-installer>`_ tool which will be used to download python itself:

::

   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.9.8/install.ps1 | iex"

.. image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/stage1.png
   :align: center
   :width: 900px

Once installed use the uv command to download python 3.9, create a virtual environment and activate it

::

   uv venv venv --python 3.9
   venv\Scripts\activate

.. image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/stage2.png
   :align: center
   :width: 900px

Install pyadi-jif with optional dependencies

::

   uv pip install "pyadi-jif[cplex,tools,draw]"

.. image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/stage3.png
   :align: center
   :width: 900px

Download the pyadi-jif Repo Examples
------------------------------------

Download the pyadi-jif repo which will contain examples of using JIF: :git-pyadi-jif:`archive/refs/heads/main.zip`
