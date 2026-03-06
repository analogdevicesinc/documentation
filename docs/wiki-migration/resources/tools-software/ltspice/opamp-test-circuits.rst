LTspice Example Test Circuits for Op Amp Parameters
===================================================

Download and unzip `opampltspicetestcircuits.zip <https://wiki.analog.com/_media/resources/tools-software/ltspice/opampltspicetestcircuits.zip>`__ to open and simulate test circuits in LTspice.

DC Simulation Parameters
========================

Vos, Ib, and Iq
---------------

**Vos (input offset voltage)** is the small differential voltage that needs to by applied at the inputs of an op amp to force the output to 0V. In an ideal op amp, Vos is 0V – but a real op amp will have a non zero value for Vos. See :adi:`MT-037 <media/en/training-seminars/tutorials/MT-037.pdf>` for more details.

**Ib (input bias current)** is the current that flows into the input terminals of an op amp. In an ideal op amp, Ib+ and Ib- are zero – but a real op amp will have a non-zero value for Ib+ and Ib-. See :adi:`MT-038 <media/en/training-seminars/tutorials/MT-038.pdf>` for more details.

**Iq (quiescent current)** is the current internally consumed by the op amp (with no load).

**Vos Ib Iq.asc** is provided to test these three parameters of an op amp model in LTspice.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ltspice/vos_ib_iq_screenshot.png

AC Simulation Parameters
========================

Aol and GBW
-----------

**Aol (open-loop voltage gain)** is the gain factor of a voltage feedback op amp at DC. In an ideal op amp, Aol is ∞ - but a real op amp will have a finite value for Aol. Even though Aol is a parameter related to DC performance, we use an AC simulation to measure this value. See :adi:`MT-033 <media/en/training-seminars/tutorials/MT-033.pdf>` and :adi:`MT-044 <media/en/training-seminars/tutorials/MT-044.pdf>` for more details.

**GBW (gain-bandwidth product)** describes the gain of a voltage feedback op amp at higher frequencies. The GBW is the product of a frequency and the gain of the op amp at that frequency. See :adi:`MT-033 <media/en/training-seminars/tutorials/MT-033.pdf>` and :adi:`MT-045 <media/en/training-seminars/tutorials/MT-045.pdf>` for more details.

**Aol and GBW.asc** is provided to test these two parameters of an op amp model in LTspice.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ltspice/aol_and_gbp_screenshot.png

Zo and Zout
-----------

**Zo (open-loop output impedance)** is the impedance at the output of the op amp. In an ideal op amp, Zo is 0Ohms – but a real op amp will have a finite (and often complex) value for Zo. Zo is am important parameter for understanding transient response and stability. See `Stability 101 Whiteboard Series <https://www.youtube.com/playlist?list=PLiwaj4qabLWwAenk99ONF2_JUjopeAXo4>`__ for more information.

**Zout (closed-loop output impedance)** is the impedance measured at the output of an op amp in a closed loop configuration. The Zout measurement includes Zo, GBW, and the feedback network (Beta) of the circuit.

**Zo and Zout.asc** is provided to test these two parameters of an op amp model in LTspice.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ltspice/zo_and_zout.png

Ccm and Cdiff
-------------

**Ccm (common-mode input capacitance)** is the capacitance between each of the input pins of an op amp and ground.

**Cdiff (differential input capacitance)** is the capacitance between the two inputs of an op amp.

**Ccm and Cdiff.asc** is provided to test these two parameters of an op amp model in LTspice.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ltspice/ccm_and_cdiff_screenshot.png
