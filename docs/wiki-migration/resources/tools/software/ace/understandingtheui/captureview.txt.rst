Navigation
==========

You can return to the ACE Application User Guide Homepage here: :doc:`Application User Guide </wiki-migration/resources/tools-software/ace/applicationuserguide>`

-  :doc:`(Previous) Memory Map View </wiki-migration/resources/tools/software/ace/understandingtheui/memorymapview.txt>`
-  :doc:`(Next) Tool Views </wiki-migration/resources/tools/software/ace/understandingtheui/toolviews>`

Capture View
------------

The Capture View allows you to gather samples from the component, perform the required analysis, plot the analyzed data, and view the analyzed results.

|Analysis.png| Figure 16: Data Analysis View

Analysis Display Types
~~~~~~~~~~~~~~~~~~~~~~

The menu bar on the left-hand side of the screen allows you to change the type of analysis results and plots that are shown. A blue border will appear around the currently selected view.

The collapse button on capture and results wizards allows you to collapse each of the wizards in turn. The graph expands to fill the available space.

The expand button will reduce the size of the graph and open the selected wizard section.

Capture Wizard
~~~~~~~~~~~~~~

The capture wizard, allows you to easily configure the component device parameters that affect how data is captured from the component.

The run once button executes a single capture from the chip which is then analyzed and plotted on the graph.

The run continuous button gathers, analyzes and plots samples from the component until the stop button is pressed.

The expand/collapse button allows you to open and close the wizard section. Once closed a data capture can be executed using the run once and run continuous icon buttons.


|Capture Wizard|

Results Wizard
~~~~~~~~~~~~~~

The results wizard gives key results based on the acquired data. It also allows you to change which channels are plotted on the graph and their corresponding results.

The previous and next buttons allow you to pull up and display other results to easily compare the performance from one execution to the next.

The export to file button allows you to export the currently displayed dataset.

The expand/collapse button allows you to open and close the wizard section. Once closed the current data can still be exported using the file export icon button.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/understandingtheui/ResultsWizard.png
   :alt: Results Wizard

Graph Manipulation
~~~~~~~~~~~~~~~~~~

ACE offers a variety of zooming and panning controls to allow you to change the view of the graph.

Zooming
~~~~~~~

Zooming can be accomplished in four different ways: using the zoom buttons in the top of the plot, using the zoom end-point selectors at the bottom of the plot, performing a drag rectangle, and using the mouse scroll-wheel.

  

Zoom Buttons
~~~~~~~~~~~~

|ZoomToFit.png| Zoom To Fit – A single zoom to a best-fit scenario. May be used as a ‘home’ zoom position after other exploratory zooms are used to return to a known, all-inclusive view.

  

Zoom End-Point Selectors
~~~~~~~~~~~~~~~~~~~~~~~~

Moving either of the zoom end-point selectors will zoom horizontally in or out with the zoom amount weighted on the side of the control, e.g., moving the left selector to the right causes the left portion of the plot to zoom in while the right side of the plot remains anchored. Moving the right end-point selector to the left zooms in the right side of the plot while the left side stays anchored. By moving either or both selectors, the zoom may be conditioned to go in or out, over a broad or very narrow range. The residual shaded portion of the horizontal zoom bar that remains may be used to implement panning, as noted below. This is called the horizontal zoom range.

Mouse Drag Rectangle
~~~~~~~~~~~~~~~~~~~~

A precise zoom in both the x and y direction can be accomplished by clicking on the plot, dragging out a colored rectangle, and releasing the mouse click. It does not matter where you begin the operation as long as you are within the plot, nor where you finish, i.e. the drag is omnidirectional.

Mouse Scroll-Wheel
~~~~~~~~~~~~~~~~~~

Moving the mouse scroll-wheel changes both the vertical and horizontal zoom simultaneously about the x/y coordinate of the mouse cursor. When you point at a specific point on the plot and then scroll forward with the scroll-wheel, the horizontal and vertical scroll are activated. If you move to another point and zoom, the zoom is based upon the new point. If the action at the new point is a reverse zoom, then the reverse zoom action is based upon the new point. The result of zooming and reverse zooming from different points may leave the total zoom in an un-expected zoom location and amount. Simply hitting the Zoom Fit button will return you to a known location and amount.

Panning
~~~~~~~

Once some level of zooming has taken place, horizontal panning may be used within the limits of the zoom window. Any of the above zoom methods will result in the horizontal zoom range being less than the original zoom amount for the plot, thereby allowing room to pan. To pan, or move left or right without zooming, simply click with the mouse cursor on the light-gray horizontal zoom range = that is between the two zoom end-point selectors, and= drag left or right. At this time, vertical panning is= not available.

Capture Size Limitations and Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The data analysis is limited to 4M samples. This is the maximum number of samples that can be captured using the graphical user interface.

Capturing samples meeting the sample requirement, the maximum amount of data that can be captured is limited by the amount of ava= ilable memory on the PC. Memory usage can be reduced by directing ACE to store cap= ture data in temporary files.

Figure 23 shows the settings for controlling how captured data is stored. The “Max Capture Cache Bytes” field is the maximum amount of capture data, in hexadecimal bytes, that ACE will store to memory. If the capture data excee= ds this number it will be stored in a temporary file. Set this field to 0 to always store data in a temporary file.

The temporary file location is configurable in the “Temp File Location” field. Windows environment variables are allowed in the path name.

The maximum file size can be set as a hexadecimal number of bytes in the “Max File Byte Size” field. The data will be broken down into files that do not exceed the specified limit.

.. image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/CaptureSettings.PNG
   :alt: Capture data storage settings

.. |Analysis.png| image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/Analysis.png
.. |Capture Wizard| image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/CaptureWizard.png
.. |ZoomToFit.png| image:: https://wiki.analog.com/_media/resources/tools-software/ace/understandingtheui/ZoomToFit.png
