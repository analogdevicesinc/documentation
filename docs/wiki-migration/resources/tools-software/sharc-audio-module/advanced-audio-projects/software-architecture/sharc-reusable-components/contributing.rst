Contributing to SHARC Reusable Components
=========================================

*This page will walk through the process of contributing to the SHARC Reusable Components repository.*

Overview
--------

The following procedure is for developers to follow if they desire to contribute to the SHARC Reusable Components repository. Before beginning the below steps, developers should read the design philosophy surrounding the repository. It is reprinted here for convenience:

-  Modularity

   -  Ideally each module is self-contained and interoperability between modules is easy to develop.

-  Reusability

   -  Each module can be ported to new hardware (or even a new HAL) with minimal need for additional configuration.

-  Ease-of-Development

   -  A developer (customer or internal) should have to spend minimal time to prototype and test with each new module they roll in. Each module contains a readme.md or .txt which fully explains the entire integration process to roll it into a new framework (or for new hardware).
   -  Items are added based on how each module enables a customer use case, and how critical that use case is. A developer (customer or internal) should have to spend minimal time to prototype and test with each new module they roll in.

-  Ease-of-Licensing

   -  A "LICENSE" file is contained in every module which fully describes its licensing conditions. All open-source and proprietary components are labelled, and care is taken during development to try and use open-source-licensed libraries where possible.

What follows will be the recommended steps to contribute to the SHARC Reusable Components using software support for an SSD1306 I2C Display peripheral as an example.

Steps for Contribution
----------------------

--------------

1. Identify the "best" software support to use for the new Reusable Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Depending on the component being added, either an absence or an abundance of software support may already be available and properly licensed on the internet. Peruse GitHub or other external sites to see if some open-source drivers already exist under a non-restrictive license. In the case of an SSD1306 display example, the following library might be chosen for its simple API and open licensing: :git-https::`afiskon/stm32-ssd1306 </github.com/afiskon/stm32-ssd1306>`.

2. Identify the license of the underlying component and verify it is as nonrestrictive as possible
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For maximal reuse, a reusable component should contain minimal licensing restrictions. GitHub does a decent job showing the restrictions of each project license. Ensure a library's LICENSE.md file permits redistribution & alteration before attempting to integrate with the Reusable Components repository.


|image1|

3. Plan Integration Steps
~~~~~~~~~~~~~~~~~~~~~~~~~

Before integrating a Reusable Component, plan out the steps of integration to ensure code quality and reliability. It's useful to begin by cloning an Audio Starter framework for a particular board and doing some initial development tied to a particular hardware board (e.g. SC584). Use this stage to plan out the development steps to uncover and eliminate as many bugs as possible in advance so that someone does not have to do this unexpectedly later.

The development flow for the ssd1306 driver component might look something like this:

-  Clone SC584 Audio Starter and create a "feature/ssd1306" branch
-  Copy the ssd1306 library into the ARM/src/oss-services folder of the project
-  Add the new files to the project Makefile in the "build" directory
-  "Functional Testing" using SC584-EZLITE with display hardware
-  "Smoke Testing" all other basic shell commands to verify no unforeseen integration issues in other areas

4. Design and test the new "Reusable Component"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Small tweaks to the underlying library will likely be needed to make it a Reusable Component, but try to leave the code as untouched as possible unless major bug fixes are needed for integration (for example the addition of thread-safe techniques). **If adjustments are needed, make sure the license allows for this, otherwise we may not be able to release adjusted code**. Make sure the code is not tied to any particular hardware once the implementation is complete (this is to ensure code is modular and reusable). 

Once necessary tweaks have been made and the Reusable Component is complete, re-run the Functional and Smoke testing steps above.

5. Document your Reusable Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/license_readme.png

The documentation style preference for Reusable Components is "GitHub-style", meaning:

-  A **"LICENSE.md"** file contains the component's licensing information and includes copyright information. In many cases, this will be part of any underlying libraries you used in development and can be copied over as long as the same licensing details apply. Again, please pay attention to ensure the licensing restrictions are as open as possible. 
-  A markdown file called **"README.md"** is located at the top directory of the component to house most of the information about your project. The README should indicate...

   -  Date of the most recent update
   -  A brief description of the intended use of the component
   -  Any and all project dependencies

      -  For example, SSD1306 component requires the TWI driver

   -  Hardware configuration used to test the component
   -  Instructions for integrating the component into an Audio Starter Framework
   -  Any useful/required code snippets for using the component

The readme will be rendered by GitHub when you navigate to the component's top directory. If you are unfamiliar with creating markdown files, there is a helpful guide here: `Markdown Syntax Guide <https://www.markdownguide.org/basic-syntax>`__. Images can also be added by including them in an "img" directory within your project and referencing them via markdown syntax. 

6. Create a pull request
~~~~~~~~~~~~~~~~~~~~~~~~

Please create a fork from the :git-https::`sharc-reusable-components </github.com//analogdevicesinc/sharc-reusable-components/tree/1.2.0-Github>` repository and branch from the latest branch. Ensure your branch has a useful name like "feature/ssd1306-display". Then use the pull request to document what was done, what software was used, testing, and any bugs to report. Most importantly, if anything is unclear – ask for feedback. Once a pull request is made, be sure to stay active and respond to feedback and requested edits until the pull request has been merged. 

Once this step is complete, congratulations and thank you for contributing to SHARC Reusable Components!

--------------

`Using SHARC RCs #..|Software Architecture #.|SHARC Reusable Components <https://wiki.analog.com/_media/navigation SHARC Reusable Components #.usage>`__

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/software-architecture/sharc-reusable-components/rc_license_mit.png
