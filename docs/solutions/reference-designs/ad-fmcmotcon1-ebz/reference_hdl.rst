HDL Reference Designs
=====================

.. warning::

   Analog Devices uses six designations to inform our customers where a
   semiconductor product is in its
   :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`.
   From emerging innovations to products which have been in production for
   twenty years, we understand that insight into life cycle status is important.
   Device life cycles are tracked on their individual product pages on
   `analog.com <https://www.analog.com/>`_, and should always be consulted
   before making any design decisions.

   This particular article/document/design has been retired or deprecated,
   which means it is no longer maintained or actively updated, even though the
   devices themselves may be Recommended for New Designs or in
   Production. This page is here for historical/reference purposes only.

Two HDL reference designs are provided targeting different use cases and system
complexity levels:

-  :doc:`Xilinx ISE HDL Project + Chipscope Interface </solutions/reference-designs/ad-fmcmotcon1-ebz/reference_hdl/ise>`

   -  Control and monitoring through Chipscope

      -  Only manual control
      -  Monitoring of system important parameters
      -  Simple to synthetize / understand / utilize

-  :doc:`HDL Project for Linux </solutions/reference-designs/ad-fmcmotcon1-ebz/reference_hdl/linux>`

   -  Complex HDL blocks with AXI Lite and AXI streaming interfaces

      -  Infrastructure for Linux support
      -  Integration of automatically generated HDL code for Simulink designed motor controller
      -  EDK and Vivado projects
