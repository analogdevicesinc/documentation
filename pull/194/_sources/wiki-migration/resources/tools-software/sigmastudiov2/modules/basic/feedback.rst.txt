:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Feedback
========

| 
| |feedbacknew1.png|

Description
-----------

| The feedback algorithm generates a delay in the signal path and reroutes signal to an input occurring earlier in the path. Note that this block must be used if feedback is required in your design.
| In sample schematic it generates one sample delay in the signal path and reroutes the signal to an input occurring earlier in the path.
| In block schematic it generates delay equal to one blocksize in the signal path and reroutes the signal to an input occurring earlier in the path.

Targets Supported
-----------------

======== ========== ================ ============= ================
Name     ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
======== ========== ================ ============= ================
Feedback B/S        B/S              S             B
======== ========== ================ ============= ================

Pins
----

Input
~~~~~

====== ===== ===============
Name   Type  Description
====== ===== ===============
Input0 Audio Input Channel 0
====== ===== ===============

Output
~~~~~~

======= ===== ================
Name    Type  Description
======= ===== ================
Output0 Audio Output channel 0
======= ===== ================

| 
| ===== Configurable Parameters ===== No configurable parameters
| ===== DSP Parameters ===== No DSP Parameters

.. |feedbacknew1.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/feedbacknew1.png
