I/Q Correction
==============

As shown in the previous section, in an FMComms system, the complex modulation/demodulation scheme is used. In theory, the two baseband signals (in-phase and quadrature) should be orthogonal to each other with the same amplitude. However, due to the different channel environments and component properties  [1]_ , there is usually offset on the phase and the amplitude, which sets the context of I/Q correction.

Why I/Q Correction
------------------

The I/Q imbalance is commonly seen in any RF front-end that exploits analog quadrature down-mixing. With an imbalanced I/Q, there will be several problems.

In contrast to an ideal down-converter that performs simple frequency shifting, a down-converter with I/Q imbalance not only down-converts the desired signal, but also introduces its image interference. Such image interference, if left uncorrected, presents an error floor which limits the demodulation performance. Moreover, although the I/Q imbalance introduced by the LO may be assumed constant over the signal bandwidth, the mismatches in the subsequent baseband I/Q amplifiers and filters tend to vary with frequencies. Such frequency dependent I/Q imbalance is particularly severe in a wideband direct-conversion receiver and the corresponding estimation and compensation process becomes more challenging.  [2]_

In order to overcome these problems and to realize a successful communication, it is necessary to implement the I/Q correction in the FMComms system.

Math of I/Q Correction
----------------------

We will use the algorithm introduced in S.W. Ellingson's paper Correcting I-Q Imbalance in Direct Conversion Receivers  [3]_ to conduct the I/Q correction.

Given a single tone that converts the signal from RF to baseband, ideally, the two baseband signals (in-phase and quadrature) should be orthogonal to each other with the same amplitude. Without loss of generality, we normalize the magnitude and the phase, then the two signals can be expressed as:

:math:`I(t)=cos(\omega t)` and

:math:`Q(t)=sin(\omega t)` ,

where :math:`\omega` is the baseband frequency of the tone.

However, due to the different channel environments and component properties, there is usually DC bias, as well as the offset on the phase and the amplitude, which makes the two signals as following:

:math:`I prime(t)=\alpha cos(\omega t)+beta_I` and

:math:`Q prime(t)=sin(\omega t+\psi)+beta_Q` ,

where :math:`beta_I` and :math:`beta_Q` are DC biases on two channels, :math:`\alpha` stands for the amplitude offset, and :math:`\psi` stands for the phase offset.

Since the DC biases can be easily found out by calculating the mean value of the signals, the main challenge is to correct the following two signals:

:math:`I prime prime(t)=\alpha cos(\omega t)` ,

:math:`Q prime prime(t)=sin(\omega t + \psi)` ,

and recover them back to :math:`I(t)` and :math:`Q(t)` . Using Trigonometric Identities, these two equations can be rewritten in the matrix format:

:math:`[matrix21{I prime prime(t)} {Q prime prime(t)}] =[matrix22alpha 0 {sin(\psi)} {cos(\psi)}] [matrix21{I(t)} {Q(t)}]` .

Then according to the linear algebra, :math:`I(t)` and :math:`Q(t)` can be obtained by doing a matrix inverse:

:math:`[matrix21{I(t)} {Q(t)}] =[matrix22alpha^{-1} 0 {-\alpha^{-1}tan(\psi)} {sec(\psi)}] [matrix21{I prime prime(t)} {Q prime prime(t)}]` .

.. note::

   :math:`[matrix21{I(t)} {Q(t)}] =[matrix22A 0 C D] [matrix21{I prime prime(t)} {Q prime prime(t)}]=[matrix22A 0 C D] [matrix21{I prime(t)-beta_I} {Q prime(t)-beta_Q}]` ,

   
   where :math:`I prime(t)` and :math:`Q prime(t)` are observed signals, and :math:`A, C, D` are correction matrix parameters.


Please refer to the S.W. Ellingson's paper [4]_ for the detailed procedures of finding out the correction matrix parameters.

Implementation
--------------

Based on the theory introduced in the previous section, the implementation of I/Q correction is conducted in two steps, namely the correction matrix calculation and the matrix multiplication. Specifically, in the first step, we use some software, such as MATLAB or Simulink, to calculate the parameters of the correction matrix. Then in the second step, we use hardware to implement the matrix multiplication and obtain the corrected I and Q.

Simulink Model
~~~~~~~~~~~~~~

A Simulink model is created to calculate the parameters of the correction matrix. The top level of the model is shown in the figure below:

.. image:: https://wiki.analog.com/_media/model_top.jpg
   :alt: Model diagram
   :width: 600px

In this model, the amplitude, phase and DC offset of the I and Q signals are specified by the users. These two signals are :math:`I prime(t)` and :math:`Q prime(t)` in the previous section, which serve as the input to the IQcorrect subsystem. In real-world application, these two inputs can be captured data from users' systems. For example, the output data from ADC on the receiver side. The output of the IQcorrect subsystem are the parameters of the correction matrix (A, C, D). The structure of this subsystem is shown below:

.. image:: https://wiki.analog.com/_media/subsystem.jpg
   :alt: Subsystem diagram
   :width: 900px

Basically, this subsystem executes Step 2 through Step 7 of the algorithm in S.W. Ellingson's paper. In order to facilitate the real-world application, this model supports fixed point data type and sample-based processing. It is noted that all the averaging operations are implemented by FIR filter.

.. admonition:: Download
   :class: download

   You can download the Simulink model from below:

   
   -  `iqcorrection.zip <https://wiki.analog.com/_media/iqcorrection.zip>`_
   
   Pay attention to the output data type of each block. It should be defined according to the range of the data value of your system. Otherwise, you will not get the correct result.


.. note::

   In order to run this model, your MATLAB license needs to include the following components:

   
   -  MATLAB
   -  Simulink
   -  Communications System Toolbox
   -  DSP System Toolbox
   -  Fixed-Point Designer
   
   If you want to generate HDL code from this model, the following component is also required:
   
   -  HDL Coder
   


HDL
~~~

The HDL is implemented for matrix multiplication on FPGA. It takes the correction matrix parameters as input, and multiplies them with the observed I and Q signals to get the corrected signals.

Results
-------

In this section, the time-domain and scatter plots of I and Q signals from the Simulink model are shown before and after I/Q correction. Comparing the figures, it is easy to find the impact of I/Q correction.

Without I/Q Correction
~~~~~~~~~~~~~~~~~~~~~~

Before the I/Q correction, it is obvious that the amplitude of the I and Q signals is very different, and their phase difference is not 90 degrees. The scatter plot shows an ellipse, which also reflects the imbalance of I and Q.

|Block diagram| |scatter1.png|

With I/Q Correction
~~~~~~~~~~~~~~~~~~~

After the I/Q correction, the amplitude of the I and Q signals is identical, and they are orthogonal to each other. Therefore, the scatter plot shows a perfect circle centering in the origin.

|image1| |scatter2.png|

.. hint::

   
   -  Questions? :ez:`Ask Help & Support <community/fpga>`.
   


.. [1]
   This imbalance mainly attributes to the mismatched components in the in-phase (I) and the quadrature (Q) branches. Examples include but not limited to an imperfectly balanced local oscillator (LO) and/or baseband low pass filters (LPF) with mismatched frequency responses.

.. [2]
   Guanbin Xing, Manyuan Shen, and Hui Liu. Frequency Offset and I/Q Imbalance Compensation for Direct-Conversion Receivers. IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, VOL. 4, NO. 2, MARCH 2005.

.. [3]
   `S.W. Ellingson's paper <https://www.faculty.ece.vt.edu/swe/argus/iqbal.pdf>`_

.. [4]
   `S.W. Ellingson's paper <https://www.faculty.ece.vt.edu/swe/argus/iqbal.pdf>`_

.. |Block diagram| image:: https://wiki.analog.com/_media/before.png
   :width: 800px
.. |scatter1.png| image:: https://wiki.analog.com/_media/scatter1.png
.. |image1| image:: https://wiki.analog.com/_media/after.png
   :width: 800px
.. |scatter2.png| image:: https://wiki.analog.com/_media/scatter2.png
