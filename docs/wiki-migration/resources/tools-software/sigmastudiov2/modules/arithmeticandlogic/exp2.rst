:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Exp 2
=====

| 
| ===== Description ===== This module computes the 2 Power of the incoming data.
| ===== Targets Supported =====

==== ========= ========= ========== ==========
Name ADAU-145x ADAU-146x ADSP-214xx ADSP-SC5xx
==== ========= ========= ========== ==========
Exp2 Yes       Yes       Yes        Yes
==== ========= ========= ========== ==========

| 
| ===== Pins =====

Input
-----

===== ============= ==========================================
Name  Type          Description
===== ============= ==========================================
Input Audio/Control Input data whose 2 Power is to be computed
===== ============= ==========================================

Output
------

+---------+---------+-------------------------------------------------------------+
| Name    | Type    | Description                                                 |
+=========+=========+=============================================================+
| Output0 | Control | Pow2(input)                                                 |
+---------+---------+-------------------------------------------------------------+
| Output1 | Control | Flag set when the output of the module Overflows/Underflows |
+---------+---------+-------------------------------------------------------------+

Configurable Parameters
~~~~~~~~~~~~~~~~~~~~~~~

No configurable parameters

DSP Parameters
~~~~~~~~~~~~~~

2 Power x is equivalent to e^(x ln 2). Taylor series expansion of e^x is used to compute the value of 2 Power x.
