FIR Filter
==========

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| -----------------------------------------------------------------------------------------------------

Overview
========

|firpic1.png| The FIR (finite impulse response) block lets you implement any FIR filter desired.

-  Drag the block into the workspace.
-  Click Table.
-  Enter the coefficients as calculated by your chosen software (see below). (Max is 800.)

| Frequency response can be shaped by specifying the appropriate filter coefficients, as shown here:
| |firpic2.png|
| You can use this popup window to input as many more coefficients as you desire, resulting in your own custom FIR filter. (Remember, the more numbers the closer to an ideal IIR filter, but at the cost of memory.)

CAD programs are available which simplify the design of lowpass, highpass, bandpass, or bandstop FIR filters. A popular one was developed by Parks and McClellan and uses the Remez exchange algorithm. The design begins by specifying such parameters as passband ripple, stopband [attenuation] ripple, and the transition region. One such CAD program is QED1000 from Momentum Data Systems; a free version is downloadable from www.mds.com.

| The frequency response of the filter coefficients in the RMS Table editor figure shown above is pictured below:
| |firpic3.png|
| To add input / output sets, right-click and Add Algorithm, IC1, FIR. After the default algorithm is established, this block can have algorithms added to it. (If you're using more than one DSP board, you will need to add the initial default algorithm for the desired board.) Right-click the block and select Add Algorithm > IC N > Pink Noise Filter. This adds another set of input/output pins for connection.

For background detail and theory, see `FIR Filter Algorithm <https://wiki.analog.com/resources/tools-software/sigmastudio/algorithminformation/firfilter>`_.

Scripting the FIR Filter from Python
====================================

First, establish a connection between Python and SigmaStudio as described on the page :doc:`SigmaStudio Scripting from Python </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/scripting/python>`.

After a connection between Python and SigmaStudio has been established, the FIR Filter can be updated with new coefficients using the following code.

Here, fir_filter_coeffs is a list containing the coefficients and 'FIR1' is the name of the FIR block in SigmaStudio.

.. code:: python

   fir_filter_coeffs = [0.1, 0.8, 0, 0.3, 0, 1, 0.7]
   v_obj = VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, fir_filter_coeffs)
   server.SET_OBJECT_PROPERTY('setControlValue', 'FIR1', 0, 0, 'Number_of_Coeffs', len(fir_filter_coeffs))
   # Update the coefficients in SigmaStudio; this reverts the schematic back to design mode...
   server.SET_OBJECT_PROPERTY('setControlValue', 'FIR1', 0, 0, 'Coefficients', v_obj)
   # so recompile the project.
   server.COMPILE_PROJECT

The FIR Filter coefficients can also be read by Python:

.. code:: python

   def print_object_property(block_name, param_name, grow_idx, repeat_idx):
       arg1 = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_BSTR, 'getControlValue')
       arg2 = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_BSTR, block_name)
       arg3 = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_ARRAY | pythoncom.VT_VARIANT, [])
       arg4 = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, grow_idx)
       arg5 = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, repeat_idx)
       arg6 = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_BSTR, param_name)

       server.GET_OBJECT_PROPERTY(arg1, arg2, arg3, arg4, arg5, arg6)

       print(block_name + ': ' + param_name + ' has value ' + str(arg4.value[0]))
       
   print_object_property('FIR1', 'Coefficients', 0, 0)

Controlling the FIR Filter from a Microcontroller
=================================================

The following assumes you have a working microcontroller platform, with SigmaDSP interface code based on :doc:`Interfacing SigmaDSP Processors with a Microcontroller </wiki-migration/resources/tools-software/sigmastudio/tutorials/microcontroller>`.

Reading FIR Coefficients from the SigmaDSP
------------------------------------------

.. code:: cpp

   // NOTE: This code will not work for very large filters that span multiple data memories or memory pages.
   void print_FIR_coeffs(int fir_start_addr, int fir_filter_length) {
       // Initialize a double array to hold the coefficients.
       double fir_coeffs[fir_filter_length] = {};

       for (int i = 0; i < fir_filter_length; i++) {
           // DSP memory holds FIR coefficients in reverse order so fill the fir_coeffs array from last to first.
           fir_coeffs[fir_filter_length - i - 1] = SIGMA_READ_REGISTER_FLOAT(fir_start_addr + i);
       }
       
       // At this point you can do anything you like with fir_coeffs. We will simply print them out.
       Serial.println("FIR Coefficients:");
       for (int i = 0; i < fir_filter_length; i++) {
           Serial.println(fir_coeffs[i], 4);
       }
   }

Writing FIR Coefficients to the SigmaDSP
----------------------------------------

.. code:: cpp

   // NOTE: This code will not work for very large filters that span multiple data memories or memory pages.
   void write_FIR_coeffs(int fir_start_addr, int fir_filter_length, double* coefficients) {
       for (int i = 0; i < fir_filter_length; i++) {
           // DSP memory holds FIR coefficients in reverse order, so increment address while decrementing coefficient index.
           SIGMA_WRITE_REGISTER_FLOAT(fir_start_addr + i, coefficients[fir_filter_length - i - 1]);
       }
   }

Example Usage
-------------

If you have an FIR algorithm added to your SigmaStudio project, the exported source code will include variable information in the \*PARAMS.h\* file. Using these variables for addressing allows your code to automatically keep track of any changes in the filter address as your SigmaStudio project grows in complexity.

.. code:: cpp

   // Print the coefficients contained in the default program
   print_FIR_coeffs(MOD_FIR1_ALG0_FIRSIGMA300ALG1FIRCOEFF0_ADDR, MOD_FIR1_COUNT);
   // Create an array of new coefficients
   double new_coefficients[MOD_FIR1_COUNT] = {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0};
   // Write the new FIR coefficients to the DSP
   write_FIR_coeffs(MOD_FIR1_ALG0_FIRSIGMA300ALG1FIRCOEFF0_ADDR, MOD_FIR1_COUNT, new_coefficients);
   // Read back the coefficients; they should now be identical to new_coefficients
   print_FIR_coeffs(MOD_FIR1_ALG0_FIRSIGMA300ALG1FIRCOEFF0_ADDR, MOD_FIR1_COUNT);

.. |firpic1.png| image:: https://wiki.analog.com/_media/firpic1.png
.. |firpic2.png| image:: https://wiki.analog.com/_media/firpic2.png
.. |firpic3.png| image:: https://wiki.analog.com/_media/firpic3.png
