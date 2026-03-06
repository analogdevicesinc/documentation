Tutorial: Creating a New C-language MicroPython Module
======================================================

Python modules in MicroPython can be either written in Python or C. Modules written in C would have better performance, but worse portability. It is advised only implement highly platform dependent modules or performance critical modules in C.

A module template
-----------------

Here is a template that can be used as a starting point of writing a new module in C.

.. code:: c

   #include "py/runtime.h

   STATIC mp_obj_t foo_bar(void) {
       bool result = True;
       return mp_obj_new_bool(result);
   }

   MP_DEFINE_CONST_FUN_OBJ_0(mod_foo_bar_obj, foo_bar);

   STATIC const mp_rom_map_elem_t foo_module_globals_table[] = {
       { MP_ROM_QSTR(MP_QSTR___name__), MP_ROM_QSTR(MP_QSTR_foo) },
       { MP_ROM_QSTR(MP_QSTR_bar), MP_ROM_PTR(&mod_foo_bar_obj) },
   };

   STATIC MP_DEFINE_CONST_DICT(foo_module_globals, foo_module_globals_table);

   const mp_obj_module_t mp_module_foo = {
       .base = { &mp_type_module },
       .globals = (mp_obj_dict_t*)&foo_module_globals,
   };

In this template, it declares a module called foo and has one member function called bar. With no arguments, when called, it returns True. If arguments need to be added, all arguments need to have type of mp_obj_t, and the MP_DEFINE_CONST_FUN_OBJ_X macro should be changed to reflect the argument number (for example, use MP_DEFINE_CONST_FUN_OBJ_2 if the function has 2 arguments.)

To link this module into a MicroPython build, one also needs to add the module into the builtin list in mpconfigport.h:

.. code:: c

   #define MICROPY_PORT_BUILTIN_MODULE_WEAK_LINKS \
       { MP_ROM_QSTR(MP_QSTR_foo), MP_ROM_PTR(&mp_module_foo) }, \

And add the file implement the library into Makefile.

--------------

`Building MicroPython with CCES#.|MicroPython Overview#..|Back to main SHARC Audio Module <https://wiki.analog.com/_media/navigation SHARC Audio Module#.building>`__
