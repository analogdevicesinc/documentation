ADIsim Operational Simulator API
================================

Overview
--------

| The intent of this page is to document the API so that any client can interface with the ADIsim operational simulator.
| The simulator supports the loading of product model files (PMF) to create product instances in memory. Any number of PMFs can be loaded (even duplicates) into memory concurrently. Upon loading a PMF, the client may set or retrieve information pertinent to that instance, such as setting a property value or querying the interface. The client may run a simulation of a model instance against some input vector. It is contingent upon the client to manage instances and to deallocate them upon completion of a simulation session (intermittent simulation calls of arbitrary length are permitted).

Structure
---------

| Before the API can be documented, it is important to understand precisely what is loaded into memory and how the memory is structured. As stated in the Overview section, any number of PMFs may be loaded concurrently into memory. The client interface accesses instances through a unique identifier called a key.
| Every model instance has at least one mode, but possibly more. A mode is used to encapsulate and describe unique product states of the device. Modes are typically high level (broad), full chip settings rather than the toggling of one particular setting. The client software can query the current mode setting, query other possible modes of operation, and set the desired mode.
| For any given mode, the simulator model receives its behavior through a collection of processing blocks. Each block contains properties which, in turn, have access permissions (read, read/write, or hidden). Only those blocks which have pertinent properties to the software client (that is, read or read/write) are visible. If a block has only hidden properties then that block is hidden, as well. There is also a global block which contains settings for the simulation, such as input frequency or sampling rate.
| See Figure 1 for a graphical representation.
| |image1|

.. container:: centeralign

   \ *Figure 1. ADIsim.dll Structure*\


API
---

| The API section is broken up into two subsections: DLL Interface and the Process Message Schema. The DLL Interface section documents how to interface physically to the ADIsim.dll. The Process Message Schema section documents how to interface logically to a model instance. The simulator was designed this way to preserve generitivity and provide extensibility.

Physical Interface
~~~~~~~~~~~~~~~~~~

.. code:: java

   int ImportPMF(const char* filename);


   | *Description:*
|

.. container:: indent

   Takes the Product Model File (\*.pmf) or ADC (\*.adc) file addressed by filename to create a model instance into memory.


   | *Parameter(s):*
|

.. container:: indent

   \ ``filename`` – string containing the PMF location.


   | *Returns:*
|

.. container:: indent

   \ ``key`` – reference to this model instance used in future functions.


   | ``int Reset(int key);`` *Description:*
|

.. container:: indent

   Resets the simulation conditions for this model instance.


   | *Parameter(s):*
|

.. container:: indent

   \ ``key`` – instance index for PMF returned from ``ImportPMF(…).``\


   | *Returns:*
|

.. container:: indent

   \ ``success`` – execution status of the function call.


   | ``int RunSamples(double* in, double* out, long length, int key);`` *Description:*
|

.. container:: indent

   Runs a multistep simulation on an array of input values for this model instance.


   | *Parameters:*
|

.. container:: indent

   \ ``in`` – pointer to the input value array.


|

.. container:: indent

   If the input data type is real, ``RunSamples(…)`` expects an array of doubles, which captures the following relationship:


   | ^ Value ^ Maps To ^

================ =========================
``in[0]``        real\ :sub:`0`
``in[1]``        real\ :sub:`1`
…                …
``in[length-1]`` real\ :sub:```length-1```
================ =========================

|

|

.. container:: indent

   If the input data type is complex, ``RunSamples(…)`` expects an array of interleaved doubles, which captures the following relationship:


   | ^ Value ^ Maps To ^

================== =========================
``in[0]``          real\ :sub:`0`
``in[1]``          imag\ :sub:`0`
``in[2]``          real\ :sub:`1`
``in[3]``          imag\ :sub:`1`
…                  …
``in[2\*length-2]`` real\ :sub:```length-1```
``in[2\*length-1]`` imag\ :sub:```length-1```
================== =========================

|

|

.. container:: indent

   \ ``out`` – pointer to the output value array. It must be allocated by the client.


|

.. container:: indent

   If the input data type is real, ``RunSamples(…)`` expects space for an array of doubles, which captures the following relationship:


   | ^ Value ^ Maps To ^

============================= =====================
real\ :sub:`0`                ``out[0]``
real\ :sub:`1`                ``out[1]``
…                             …
real\ :sub:```out_length-1``` ``out[out_length-1]``
============================= =====================

|

|

.. container:: indent

   If the input data type is complex, ``RunSamples(…)`` expects space for an array of interleaved doubles, which captures the following relationship:


   | ^ Value ^ Maps To ^

============================= =======================
real\ :sub:`0`                ``out[0]``
imag\ :sub:`0`                ``out[1]``
real\ :sub:`1`                ``out[2]``
imag\ :sub:`1`                ``out[3]``
…                             …
real\ :sub:```out_length-1``` ``out[2\*out_length-2]``
imag\ :sub:```out_length-1``` ``out[2\*out_length-1]``
============================= =======================

|

|

.. container:: indent

   where:


   |

.. container:: indent

   
   .. container:: indent

      \ ``out_length = ceil(length * (fout / fs)).``\

   


|

.. container:: indent

   
   .. container:: indent

      \ ``fout`` and ``fs`` are retrieved via ``ProcessMessage(…)`` and ``ceil(…)`` returns the next highest inclusive integer.


      |

.. container:: indent

   \ ``length`` – contains the number of simulation iterations to run.


|

.. container:: indent

   \ ``key`` – instance index for PMF returned from ``ImportPMF(…).``\


   | *Returns:*
|

.. container:: indent

   \ ``success`` – execution status of the function call.


   | ``int RunSample(double* in, double* out, int key);`` *Description:*
|

.. container:: indent

   Functionally equivalent to ``RunSamples(in, out, 1, key);``\


   | ``int GetPortCount(int* count, int port_direction, int key);`` *Description:*
|

.. container:: indent

   Gets the number of inputs/outputs for this model instance.


   | *Parameter(s):*
|

.. container:: indent

   \ ``port_direction`` – whether a port is an input or an output {0 : Input, 1: Output}.


|

.. container:: indent

   \ ``key`` – instance index for PMF returned from ``ImportPMF(…).``\


   | *Returns:*
|

.. container:: indent

   \ ``count`` – the port count.


|

.. container:: indent

   \ ``success`` – execution status of the function call.


   | ``int QueryPort(double* f, bool* is_complex, int* domain, char** unit, int port_direction, int port_index, int key);`` *Description:*
|

.. container:: indent

   Gets information about the desired port for this model instance.


   | *Parameter(s):*
|

.. container:: indent

   \ ``port_direction`` – whether a port is an input or an output {0 : Input, 1: Output}.


   |

.. container:: indent

   \ ``port_index`` – the port index.


|

.. container:: indent

   \ ``key`` – instance index for PMF returned from ``ImportPMF(…).``\


   | *Returns:*
|

.. container:: indent

   \ ``f`` – the port frequency.


   |

.. container:: indent

   \ ``is_complex`` – the port complexity.


|

.. container:: indent

   \ ``domain`` – the port domain {0 : Unspecified, 1 : Analog, 2 : Digital}.


   |

.. container:: indent

   \ ``unit`` – the port unit (the string allocation is managed by MOTIF).


|

.. container:: indent

   \ ``success`` – execution status of the function call.


   | ``void Destroy(int key);`` *Description:*
|

.. container:: indent

   Deallocates model instance from memory.


   | *Parameter(s):*
|

.. container:: indent

   \ ``key`` – instance index for PMF returned from ``ImportPMF(…).``\


   | *Returns:*
|

.. container:: indent

   Nothing.


   | ``void DestroyAll();`` *Description:*
|

.. container:: indent

   Deallocates all model instances from memory.


   | *Parameter(s):*
|

.. container:: indent

   None.


   | *Returns:*
|

.. container:: indent

   Nothing.


| ==== Logical Interface ==== The generative design of the simulator requires a generic interface. Besides the above documented physical interface, there is a logical interface which is consistent across all models. The logical interface is further subdivided into two categories: concepts and message passing.

Concepts
^^^^^^^^

| All models support a logical Rate Dependency interface. This means that every model will contain both a ``fin`` and ``fout`` property where:
|

.. container:: indent

   \ ``fin`` – the rate of the incoming data


|

.. container:: indent

   \ ``fout`` – the rate of the outgoing data


| By computing the ratio ``r = fout / fin``, the user can determine the model’s total interpolation or decimation. This should be performed every time a logical property is changed to ensure that the external harness knows how to appropriately allocate memory. The exact mechanism for querying ``fin`` and ``fout`` is specified in the message passing section below.
| Based on the model’s queried interface, there will be some domain associated with both the input and the output. Domains are restricted to either “analog” or “digital”.
| If a model supports the “analog” domain, whether on the input, output, or both, it will always have a property ``dt``.
|

.. container:: indent

   \ ``dt`` – the delta time between sampled analog values


   | If a model supports the “digital” domain, whether on the input, output, or both, it will always have a property ``fclk``.
|

.. container:: indent

   \ ``fclk`` – the frequency of the digital clock


   | If a model supports both “analog” and “digital” (and ADC or a DAC), it will always have a property ``OSR``.
|

.. container:: indent

   \ ``OSR`` – the oversampling ratio from the digital to the analog domain


   | Some models support an additional parameter ``tessitura``, which represents the expected mean frequency of the input data. This parameter is only necessary when a model is unable to infer the input frequency from context. The term is borrowed from music theory, where it refers to the center frequency at which a vocalist is most comfortable.
|

.. container:: indent

   \ ``tessitura`` - the expected mean frequency of the input data


| It is important to check the permission of the above property values for it may be that only one of them is mutable. This is determined when a model is loaded, or when a mode is changed.
| A graphical representation of the logical model interface is shown in Figure 2 below:
| |image2|

.. container:: centeralign

   \ *Figure 2: Logical Model Interface*\


Message Passing
^^^^^^^^^^^^^^^

| A physical API command that enables logical message passing is provided through the following method:
| ``int ProcessMessage(const char* msg, char** response, int key);`` *Description:*
|

.. container:: indent

   Generic interface to inspect/modify model instance properties.


   | *Parameter(s):*
|

.. container:: indent

   \ ``msg`` – message (in XML format) to send to the model instance.


   |

.. container:: indent

   \ ``response`` – Pointer to the internally allocated response message (in XML format).


|

.. container:: indent

   \ ``key`` – instance index for PMF returned from ``ImportPMF(…).``\


   | *Returns:*
|

.. container:: indent

   \ ``success`` – execution status of the function call.


| All sent message content are children of the root element:
| ``<adisim>[command(s)]</adisim>`` All received message content are children of the root element:
| ``<responses>[answers(s)]</responses>`` Sent messages are composed of a series of atomic messages called commands. Commands perform a specific task understood by ADIsim.dll. Each sent message solicits a response that is called an answer.

Modes
^^^^^

.. code:: xml

   <setmode>[mode]</setmode>


   | *Command element(s):*
|

.. container:: indent

   \ ``[mode]`` – name of the mode you want to switch to.


   | *Answer:*
|

.. container:: indent

   \ ``<setmode s=”Success” />`` – if ``[mode]`` is valid.


|

.. container:: indent

   \ ``<setmode s=”Error”>Cannot find mode: [mode]</setmode>`` – if ``[mode]`` is invalid.


   | ``<getmode />`` *Command element(s):*
|

.. container:: indent

   None.


   | *Answer:*
|

.. container:: indent

   \ ``<getmode mdn=”[mode display name]” mn=”[mode name]”/>``\


   |

.. container:: indent

   where:


|

.. container:: indent

   
   .. container:: indent

      \ ``[mode display name]`` – display name of the current mode.

   


|

.. container:: indent

   
   .. container:: indent

      \ ``[mode name]`` – name of the current mode.


      | ``<querymodes />`` *Command element(s):*
|

.. container:: indent

   None.


   | *Answer:*
|

.. container:: indent

   \ ``<querymodes>``\


   |

.. container:: indent

   
   .. container:: indent

      \ ``<mode mdn=”[mode display name1]” mn=”[mode name1]”/>``\

   


|

.. container:: indent

   
   .. container:: indent

      \ ``…``\


      |

.. container:: indent

   
   .. container:: indent

      \ ``<mode mdn=”[mode display nameN]” mn=”[mode nameN]”/>``\

   


|

.. container:: indent

   \ ``</querymodes>``\


   |

.. container:: indent

   where:


|

.. container:: indent

   
   .. container:: indent

      \ ``[mode display name#]`` – display name of this mode.

   


|

.. container:: indent

   
   .. container:: indent

      \ ``[mode name#]`` – name of this mode.

   


| === Properties ===

.. code:: xml

   <setprop bn=”[block name]” pn=”[property name]”>[value]</setprop>


   | *Command element(s):*
|

.. container:: indent

   \ ``[block name]`` – name of the block to be indexed.


   |

.. container:: indent

   \ ``[property name]`` – name of the property to set.


|

.. container:: indent

   \ ``[value]`` – value to assign to the property.


   | *Answer:*
|

.. container:: indent

   \ ``<setprop s=”Success” />`` - if ``[block name]`` is found, ``[property name]`` is found.


   |

.. container:: indent

   \ ``<setprop s=”Error”>Could not find block: [block name]</setprop>`` - if ``[block name]`` is not found.


|

.. container:: indent

   \ ``<setprop s=”Error”>Could not find property: [property name]</setprop>`` - if ``[property name]`` is not found.


| <wrap>Note: ``ProcessMessage(…)`` does not perform data validation through ``<setprop…>``.</wrap>

| ``<getprop bn=”[block name]” pn=”[property name]”/>`` *Command element(s):*
|

.. container:: indent

   \ ``[block name]`` – name of the block to be indexed.


|

.. container:: indent

   \ ``[property name]`` – name of the property to get.


   | *Answer:*
|

.. container:: indent

   \ ``<getprop pdn=”[property display name]” l=”[limits]” p=”[permissions]” t=”[type]” u="[unit]" tt="[tooltip]">[value]</getprop>``\


   |

.. container:: indent

   if ``[block name]`` is found and ``[property name]`` is found:


|

.. container:: indent

   
   .. container:: indent

      \ ``[property display name]`` – display name of this property.


      |

.. container:: indent

   
   .. container:: indent

      \ ``[property name]`` – name of this property.

   


|

.. container:: indent

   
   .. container:: indent

      \ ``[limits]`` – limits of valid values associated with this property.


      |

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *{elem0,elem1,…,elemM}* – set of valid values.

         

   


|

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *[m,n]* – closed interval specifying a range of valid values.


            |

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *[m,n)* – half-open interval specifying a range of valid values.

         

   


|

.. container:: indent

   
   .. container:: indent

      \ ``[permissions]`` – permission associated with this property.


      |

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *rw* – read/write.

         

   


|

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *r* - read only.


            |

.. container:: indent

   
   .. container:: indent

      \ ``[type]`` – type associated with this property.

   


|

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *int* – integer.


            |

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *double* – double.

         

   


|

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *int\** - integer array.


            |

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *double\** - double array.

         

   


|

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *string* – string.


            |

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *bool* – Boolean *{false, true}*.

         

   


|

.. container:: indent

   
   .. container:: indent

      \ ``[unit]`` – unit associated with this property. Will be SI, descriptive (*e.g. "Codes", "dB", etc.*), or possibly blank.


      |

.. container:: indent

   
   .. container:: indent

      \ ``[tooltip]`` – tooltip associated with this property.

   


|

.. container:: indent

   
   .. container:: indent

      \ ``[value]`` – value of this property.


      |

.. container:: indent

   else:


|

.. container:: indent

   \ ``<getprop s=”Error”>Could not find block: [block name]</getprop>`` - if ``[block name]`` is not found.


|

.. container:: indent

   \ ``<getprop s=”Error”>Could not find property: [property name]</getprop>`` - if ``[property name]`` is not found.


   | ``<queryprops />`` *Command element(s):*
|

.. container:: indent

   None.


   | *Answer:*
|

.. container:: indent

   \ ``<queryprops>``\


   |

.. container:: indent

   
   .. container:: indent

      \ ``<prop bdn=”[block display name1]” bn=”[block name1]” pdn=”[property display name1]” pn=”[property name1]” l=”[limits1]” p=”[permissions1]” t=”[type1]” u="[unit1]" tt="[tooltip1]">[value1]</prop>``\

   


|

.. container:: indent

   
   .. container:: indent

      \ ``…``\


      |

.. container:: indent

   
   .. container:: indent

      \ ``<prop bdn=”[block display nameN]” bn=”[block nameN]” pdn=”[property display nameN]” pn=”[property nameN]” l=”[limitsN]” p=”[permissionsN]” t=”[typeN]” u="[unitN]" tt="[tooltipN]">[valueN]</prop>``\

   


|

.. container:: indent

   \ ``</queryprops>``\


   |

.. container:: indent

   where:


|

.. container:: indent

   
   .. container:: indent

      \ ``[block display name#]`` – display name of this block.


      |

.. container:: indent

   
   .. container:: indent

      \ ``[block name#]`` – name of this block.

   


|

.. container:: indent

   
   .. container:: indent

      \ ``[property display name#]`` – display name of this property.


      |

.. container:: indent

   
   .. container:: indent

      \ ``[property name#]`` – name of this property.

   


|

.. container:: indent

   
   .. container:: indent

      \ ``[limits#]`` – limits of valid values associated with this property.


      |

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *{elem0,elem1,…,elemM}* – a set of valid values.

         

   


|

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *[m,n]* – closed interval specifying a range of valid values.


            |

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *[m,n)* – half-open interval specifying a range of valid values.

         

   


|

.. container:: indent

   
   .. container:: indent

      \ ``[permissions#]`` – permission associated with this property.


      |

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *rw* – read/write.

         

   


|

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *r* - read only.


            |

.. container:: indent

   
   .. container:: indent

      \ ``[type#]`` – type associated with this property.

   


|

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *int* – integer.


            |

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *double* – double.

         

   


|

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *int\** - integer array.


            |

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *double\** - double array.

         

   


|

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *string* – string.


            |

.. container:: indent

   
   .. container:: indent

         
         .. container:: indent

            \ *bool* – Boolean *{false,true}*.

         

   


|

.. container:: indent

   
   .. container:: indent

      \ ``[unit#]`` – unit associated with this property. Will be SI, descriptive (*e.g. "Codes", "dB", etc.*), or possibly blank.


      |

.. container:: indent

   
   .. container:: indent

      \ ``[tooltip#]`` – tooltip associated with this property.

   


|

.. container:: indent

   
   .. container:: indent

      \ ``[value#]`` – value of this property.

   


| === Other ===

.. code:: xml

   <queryinterface />


   | *Command element(s):*
|

.. container:: indent

   None.


   | *Answer:*
|

.. container:: indent

   \ ``<queryinterface><in domain=”[input domain]” fin=”[input frequency]” is_complex=”[is input complex]” unit=”[input unit]”/><out domain=”[output domain]” fout=”[output frequency]” is_complex=”[is output complex]” unit=”[output unit]”/></queryinterface>``\


   |

.. container:: indent

   where:


|

.. container:: indent

   
   .. container:: indent

      \ ``[input (output) domain]`` – *{analog, digital}* indicating the analog or digital nature of the input (output).


      |

.. container:: indent

   
   .. container:: indent

      \ ``[input (output) frequency]`` – indicating the reciprocal of the time step between input (output) data points.

   


|

.. container:: indent

   
   .. container:: indent

      \ ``[is input (output) complex]`` – *{false, true}* indicating whether input (output) data are complex or real numbers.

   


|

.. container:: indent

   
   .. container:: indent

      \ ``[input (output) unit]`` – indicating the units associated with the input (output) data.


      | ``<queryversion />`` *Command element(s):*
|

.. container:: indent

   None.


   | *Answer:*
|

.. container:: indent

   \ ``<queryversion dllversion=”[dll version]” pmfversion=”[pmf version]”/>``\


   |

.. container:: indent

   where:


|

.. container:: indent

   
   .. container:: indent

      \ ``[dll version]`` – version of the ADIsim.dll.

   


|

.. container:: indent

   
   .. container:: indent

      \ ``[pmf version]`` – version of the Product Model file (model).

   


.. |image1| image:: https://wiki.analog.com/_media/resources/technical-guides/structure2.png
.. |image2| image:: https://wiki.analog.com/_media/resources/technical-guides/logical_model_concept.png
