.. _cn0549 eval:

CN0549
======

Condition-Based Monitoring Development Platform

.. figure:: images/cn0549_angle.jpg
   :align: center
   :alt: CN0549
   :width: 600px

Overview
--------

The CN0549 is a high-fidelity vibration acquisition platform designed to accelerate the development of 
custom condition-based monitoring and predictive maintenance solutions from prototype to production. 
It provides a complete system for capturing high-quality vibration data from industrial assets.

The design features combination of the following components:

   - CN0540: 24-Bit Data Acquisition System for IEPE Sensors
   - CN0532: IEPE-Compatible Interface for Wideband MEMS Accelerometer Sensors

Software Ecosystem:

   The CN0549 features an open-source, reusable software stack that enables:

   - Real-time processing capabilities
   - Integration with popular data analysis tools (MATLAB, Python)
   - Algorithm development for CbM applications
   - Support for various processing options (microcontrollers, FPGAs)

Features
--------

   - Wide bandwidth MEMS accelerometer sensor data is output in the popular IEPE format
   - Easy mounting to machines (like pumps, fans, and motors) while maintaining sensor signal integrity
   - The DAQ solution provides a high fidelity, IEPE analog input bandwidth from DC to 54 kHz
   - Embedded FPGA Software captures and stores the raw data for local embedded or networked processing
   - IIO Oscilloscope application allows users to quickly visualize the data for evaluation purposes.

Applications
------------

   - Develop and validate CbM algorithms
   - Collect and analyze vibration data from industrial equipment
   - Create predictive maintenance solutions
   - Prototype custom monitoring systems

.. tip::
   
   Navigate through the following sections to learn more about the CN0549, including detailed setup information, 
   software examples, and how to get started with your own condition-based monitoring projects.

   .. toctree::
      :titlesonly:
      :glob:

      cn0549
      matlab_example
      python_example
      pelican_kit

Recommendations
---------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

Warning
-------

.. esd-warning::

Help and support
----------------

Please go to :ref:`Help and Support <help-and-support>` page.
