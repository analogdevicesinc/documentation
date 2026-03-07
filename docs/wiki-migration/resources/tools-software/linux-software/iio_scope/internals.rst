IIO Oscilliscope Internals
==========================

Making your own plugin for the IIO Oscilloscope.

libiio connect your C code to the IIO device (backed by the IIO device driver), but it does not automatically connect your code to a GTK widget.

That is the responsibility of :git-iio-oscilloscope:`iio_widget.c` and :git-iio-oscilloscope:`iio_widget.h <iio_widget.c>`, which are exclusively part of the IIO oscilloscope project.

Those functions are called in the :git-iio-oscilloscope:`plugin file <plugins/fmcomms2.c#L1590>`, normally in the ``init`` function. Calling these functions (with the right parameters) ensures that libiio will connect with the GTK widget.

The init function is called during the plugin load via the :git-iio-oscilloscope:`osc_plugin struct <plugins/fmcomms2.c#L2059>`.

OSC Plugins are dynamically loaded (DL) libraries (.so or .dll). During OSC start-up each file under the plugin folder is accessed using the dlopen() API. Using dlsym(lib, "plugin") the symbol to the osc_plugin structure is obtained. So each and every plugin is probed, weather or not the init() function is called depends on the return value of the identify() function call which takes place prior in time. Identify() is typically used to check the presence of a number of IIO devices required to a specific plugin to operate.

If you have any more detailed questions about how to write your own plugins for your own IIO devices, please ask on ADI's :ez:`EngineerZone <community/linux-device-drivers/linux-software-drivers>`.
