IIO Oscilloscope Profile Guidelines
===================================

About
-----

| Profiles are `INI <https://en.wikipedia.org/wiki/INI_file>`_ files that can configure the IIO-Oscilloscope software or manipulate its behavior.

Using Profiles
--------------

There are several situations where profiles can be used.

The state of a IIO-Oscilloscope session can be saved to a profile. In a similar way the state of the session can be restored by loading the saved profile or other profiles with different configurations.

A special use of profiles is the ability to use them as a set of instructions in order to run/close the software, start/stop the data acquisition, test if certain software properties are within a specified range of values, log properties and their values to files, capture screenshots or display custom popup message.

Profile Structure
-----------------

Properties that profiles contain are grouped into sections. Each section is designated to one different part of IIO-Oscilloscope. The following sections are recognized by the profile parser of the software:

-  **[IIO Oscilloscope]** - Describes the configuration of the main window and global properties of the software.
-  **[IIO Oscilloscope - Capture Window<N>]** - Describes the configuration of one plot window of the software. <N> is an unsigned integer value that specifies the index of the plot window that the configuration applies to.
-  **[<Plugin Name>]** - Describes the configuration of a software plugin. <Plugin Name> is a string that matches the name of the plugin displayed on the main window.

A section of a profile can be split which allows a section to be placed in more than one place inside a file.

Sections can be skipped out of a profile without making the profile invalid. But as a result the software profile parser will use the default values for all properties that are related to that section.

Profile Keywords
================

Run/Stop/Capture
----------------

Cycle
~~~~~

The *cycle* instruction runs (cycles) the software for a given number of microseconds.

::

   cycle=[microseconds]

| **Where:**
| [microseconds] - Number of microseconds. Type: unsigned int.
| **Applies in section:** [IIO Oscilloscope - Capture Window<N>]

Quit
~~~~

The *quit* instruction signals the software to terminate its execution.

::

   quit=1

**Applies in section:** [IIO Oscilloscope - Capture Window<N>]

Capture
~~~~~~~

The *capture* instruction signals the software to start capturing data or to stop the process.

::

   capture=[state]

| **Where:**
| [state] - State of the capture process. It can be 0 or 1.
| **Applies in section:** [IIO Oscilloscope - Capture Window<N>]

Loops
-----

Profile instructions that repeat themselves can be rewritten in a more compact way using loops. There are two types of available loops:

-  **SEQ** - Loops through a sequence of numbers.
-  **FOR** - Loops through a given list of values.

SEQ
~~~

The sequence of numbers the *SEQ* loop iterates through, starts from [first] and reaches [last] with a step of [increment].

::

   <SEQ> [var] [first] [increment] []
   </SEQ>

| **Where:**
| [var] - The name of the loop variable. Type: string. Longer names that 127 characters will be truncated.
| [first] - Type: long long.
| [increment] - Type: long long.
| [last] - Type: long long.
| **Applies in section:** All sections.

FOR
~~~

The *FOR* loop iterates through the values specified within the curly brackets. All values must be separated by the space character.

::

   <FOR> [var] in {[space-separated values]}
   </FOR>

| **Where:**
| [var] - The name of the loop variable. Type: string. Longer names that 127 characters will be truncated.
| [space-separated values] - strings without the space character.
| **Applies in section:** All sections.

| Loops can be nested. Any combination is possible and the nesting level is not limited.
| Usage example:

::

   <FOR> y in {1960 1995 2000}
   year=<y>
   <SEQ> d 1 7 28
   day=<d>
   </SEQ>
   </FOR>

Testing
-------

Testing Enable
~~~~~~~~~~~~~~

The *test* instruction tells the software profile parser to treat the profile as a test profile.

::

   test=1

**Applies in section:** [IIO Oscilloscope]

Property Testing
~~~~~~~~~~~~~~~~

The instructions below will test if markers and iio attributes values are within a given interval. A test failure will stop the parsing of the profile and a popup with an error message will be displayed.

::

   test.marker.[m]=[min] [max]

::

   test.[device].[attribute].[type]=[min] [max]

| **Where:**
| [m] - The index of the marker.
| [device] - The name of the iio device.
| [attribute] - The name of the iio attribute of the iio device.
| [type] - Any of the following: int, double.
| [min] - Type: double.
| [max] - Type: double.

Popup Messages
~~~~~~~~~~~~~~

The *test.message* instruction will display a popup window with the message specified in the instruction.

::

   test.message=[message to display]

| **Where:**
| [message] - Any string message. **Applies in section:** [IIO Oscilloscope - Capture Window<N>]

Logging
-------

- nothing yet

Taking Screenshots
------------------

Save as a .png file
~~~~~~~~~~~~~~~~~~~

The *save_png* instruction signals the software to terminate its execution.

::

   save_png=[filename].png

| **Where:**
| [filename] - The name of the file the image should be saved.
| **Applies in section:** [IIO Oscilloscope - Capture Window<N>]
