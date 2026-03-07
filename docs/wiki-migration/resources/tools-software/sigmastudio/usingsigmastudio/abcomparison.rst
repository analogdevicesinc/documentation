Allow Real-Time A/B Testing Between Projects
============================================

| :doc:`Click here to return to the Using Sigma Studio page </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio>`
| Suppose you are viewing your design A and listening to its audio flow, and you wonder how your design B (also open) sounds in comparison.

| Press the real-time A/B-testing icon and when you switch between the 2 projects, SigmaStudio automatically downloads the design B or design A program to the DSP without needing to recompile.
| |abcomparisonpic1.png|
| In other words, clicking the icon lets you switch among any number of open compiled projects without having to recompile each. (The function is very useful: without it, you must recompile a project every time you bring it to the front even if you haven't made any changes to the schematic.)

You can also select "Allow Realtime AB Testing" from the pull down menu:


|image1|

To switch between open projects, press **Ctrl+Tab** or select a project name from the main **Window** menu. Another method is to simply tile the project windows so that you can click on the project windows to select the project. There is a short delay while the new project is being downloaded but it does not have to be recompiled so it is much faster.

To set this up:

1) You select the AB Comparison icon to activate the function.

2) Click on "Link/Compile/Download"

3) Select The second project and click on "Link/Compile/Download". Now, when you switch projects it will automatically download the program for the project that is in focus (on the top of the stack of windows )

Note: the project presets are still active so you can still use them from within a project to audition different settings for the current project.

Project 1 in this screenshot is the active project running:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/screenhunter_337_dec._09_11.41.jpg
   :width: 200px

Clicking on the window for project 2 will load the second project into the DSP and run it. So now Project 2 is active.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/screenhunter_336_dec._09_11.40.jpg
   :width: 200px

.. |abcomparisonpic1.png| image:: https://wiki.analog.com/_media/abcomparisonpic1.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/screenhunter_331_dec._09_11.35.jpg
   :width: 200px
