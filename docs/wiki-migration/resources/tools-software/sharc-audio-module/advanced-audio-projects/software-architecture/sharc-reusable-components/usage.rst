Using SHARC Reusable Components
===============================

*This page will describe the usage of the SHARC Reusable Components repository.For frequent embedded developers, the process for integrating modules from SHARC Reusable Components should appear fairly straightforward. For those who do not frequently do such development (or for those who need a refresher), some steps will be highlighted below.*

--------------

Steps for Using a Reusable Component
------------------------------------

+---+---+---+
| 1. Consult the project's README file                             | This is good practice for any developer incorporating external source code into a project. Every reusable component comes with a "README" file and a "LICENSE" file. The README ideally explains what the module does and where it comes from, what it's expected output and limitations are, and finally, the good stuff – how to configure, integrate, and test it.                                                                                                                                                                                         | |image10|           |
+---+---+---+
| 2. Consult the project's LICENSE file                            | The LICENSE file explains what license the module contains, which in many cases will be a variation of an open-source license (e.g. MIT, Apache, etc). Developers must always look at the license files before incorporating new source into their project to ensure that they are cooperating with their project's licensing guidelines and maintaining legal compliance with all underlying source code used in their project.                                                                                                                              | |image11|           |
+---+---+---+
| 3. Copy the ENTIRE module to your project.                       | Copy the module into your project according to the readme's instructions. This should include ALL of the original files from the module, including any README, LICENSE, or NOTICE files. This ensures that compliance is maintained and module documentation is carried over into your project. As an example, we will copy the "ssd1306" module from oss-services into SC584-EZLITE-Audio-Starter/ARM/src/oss-services.                                                                                                                                      | |image12|           |
+---+---+---+
| 4. Add the relevant module file paths to your project's Makefile | The next step is to adjust your application's Makefile to include the new additions to the project. This will include adding to the Include and Source paths for most projects. The makefile for the SC584-EZLITE-Audio-Starter is in the build/ directory.                                                                                                                                                                                                                                                                                                   | |image13| |image14| |
+---+---+---+
| 5. Test compilation                                              | At this point, it's recommended to test compilation to ensure your build system can detect all relevant source files and compile them accordingly. For the audio starter framework, this is done via running a shell script located in the top directory to connect your environment with the CrossCore Embedded Studio build system. Then you can call the Make program from the build directory. You will need to adjust the "env.sh" script to reflect your current version of CrossCore Embedded Studio. A console log of the relevant commands is shown. | |image15| |image16| |
+---+---+---+
| 6. Test Functionality                                            | At this stage, you can begin using the project from the application level and testing the functionality desired. Rudimentary steps on how to do this should be covered by the project README; otherwise, the initial project's documentation may be used (a link to this may also be present in the README). In the case of the SSD1306, the following configuration was done with the SC584-EZLITE-Audio-Starter framework:                                                                                                                                  | |image17| |image18| |
+---+---+---+

--------------

`SHARC Reusable Components #..|SW Architecture #.contributing|Contributing to SHARC RCs <https://wiki.analog.com/_media/navigation Software Architecture #.>`__

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_readme_license.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_readme_license.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_copy.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_makefile_inc.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_makefile_src.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_compilation_script.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_compilation.png
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_functionality_hw.png
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_functionality_sw.png
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_readme_license.png
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_readme_license.png
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_copy.png
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_makefile_inc.png
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_makefile_src.png
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_compilation_script.png
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_compilation.png
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_functionality_hw.png
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_functionality_sw.png
