FxLMS Filter
============

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| -----------------------------------------------------------------------------------------------------

|fxlms.png| FxLMS(Filtered Least mean squared)filter is an adaptive filter which is used for system identification.The filter would produce an output such that the error signal fed to input of the Filter is reduced gradually.The error signal would be the difference between the desired response and the output of the FxLMS filter.

**Inputs to the module:**

1. Reference input

2. Error Input

3. Filtered Reference Input

4. Adapt On/Off

**Output of the module:**

1. Adaptive output (Anti-noise in the case of Active noise cancellation)

**Parameters to the module:**

1. Number of Taps - Length of the adaptive Filter

2. alpha - Step size for adaptation ( also called as mu)

3. Leakage - Leakage factor is used as forgetting factor

FxLMS filter can be used for Active noise cancellation.The Reference input will be the reference to the noise to be cancelled.The error(residual signal) input is the acoustic addition of anti-noise and the noise signal near to the error microphone.The Filtered Reference is the reference signal filtered through the secondary path.Where the secondary path is the transfer function of the path after the FxLMS filter output back to FxLMS error input.

| 
| |fxlms_anc.png|
| The output of the filter is

y(n) = W'X

where,

::

        W is the coefficient vector
        X is the Input reference vector
        

The coefficient update equation is W := (1- alpha \* Leakage)\* W + alpha \* error(n) \* XFilterd/ energy

where,

::

        W is the coefficient vector
        XFilterd is the Filtered input reference vector
        alpha is the stepsixe parameter
        Leakage is the leakage factor
        error(n) is the current error sample
        energy is the norm square of the filtered reference vector

| 
| |anc.png|

.. |fxlms.png| image:: https://wiki.analog.com/_media/fxlms.png
.. |fxlms_anc.png| image:: https://wiki.analog.com/_media/fxlms_anc.png
.. |anc.png| image:: https://wiki.analog.com/_media/anc.png
