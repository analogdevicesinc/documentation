Release Highlights and Previous Versions
========================================

ACE 1.30.3323.1470 (Update)
---------------------------

**Released:** 10th January 2025

-  **Download** `ACEInstall_1.30.3323.1470.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.30.3323.1470.exe>`_
-  **Download** `ACEInstall_1.30.3323.1470_minimal.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.30.3323.1470_minimal.exe>`_
-  **Download** `ACEInstall_1.30.3323.1470_offline.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.30.3323.1470_offline.exe>`_

Changelog:

-  Enables improved product discovery on hardware attached, for sessions with an active internet connection, when hardware is connected ACE will attempt to identify the board and match it's appropriate plug-in software if available. On successful matches, users will now be prompted to download the plug-in directly in the attached hardware section and require no additional action.
-  Long running hardware tasks will display a loading spinner on the attached hardware tile for IIO boards
-  FFT analysis updated to include spectrum bound analysis options
-  Interactive device view can now be replaced with a static SVG for plug-ins that do not require interactivity on the main view or supply configuration options by alternate means

**Release Notes:** `ACE v3323.1470 Release Notes <https://wiki.analog.com/_media/resources/tools-software/ace/release_notes_-_ace_v1.30.3323_external_.pdf>`_

ACE 1.30.3311.1463 (Update)
---------------------------

**Released:** 24th April 2024

-  **Download** `ACEInstall_1.30.3311.1463.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.30.3311.1463.exe>`_
-  **Download** `ACEInstall_1.30.3311.1463_minimal.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.30.3311.1463_minimal.exe>`_
-  **Download** `ACEInstall_1.30.3311.1463_offline.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.30.3311.1463_offline.exe>`_

Changelog:

-  Fixes display issues for switch blocks in some diagrams
-  Fixes wire routing bug seen in some plug-in diagrams that results in unexpected hidden wires
-  Fixes issues resolving transaction parameters in scripts
-  Fixes an issue where the widget block in new diagrams would always select the default widget even when overridden

**Release Notes:** `ACE v1.30.3311.1463 Release Notes <https://wiki.analog.com/_media/resources/tools-software/ace/release_notes_-_ace_v1.30.3311_external_.pdf>`_

ACE 1.30.3303.1460 (Update)
---------------------------

**Released:** 22nd February 2024

-  **Download** `ACEInstall_1.30.3303.1460.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.30.3303.1460.exe>`_
-  **Download** `ACEInstall_1.30.3303.1460_minimal.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.30.3303.1460_minimal.exe>`_
-  **Download** `ACEInstall_1.30.3303.1460_offline.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.30.3303.1460_offline.exe>`_

- Fixes issues displaying some legacy device views - Fixes deadlock issues in plug-in installation settings when package feed URLs are duplicated - Improves plug-in installation stability with broken broken feeds when more than one plug-in package feed is enabled

ACE 1.30.3290.1451
------------------

**Released:** 1st January 2024

-  **Download** `ACEInstall_1.30.3290.1451.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.30.3290.1451.exe>`_
-  **Download** `ACEInstall_1.30.3290.1451_minimal.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.30.3290.1451_minimal.exe>`_
-  **Download** `ACEInstall_1.30.3290.1451_offline.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.30.3290.1451_offline.exe>`_

**Release Notes:** `ACE v1.30 Release Notes <https://wiki.analog.com/_media/resources/tools-software/ace/release_notes_-_ace_v1.30_external_.pdf>`_

ACE 1.29.3286.1447 (Hotfix)
---------------------------

**Released:** 27th October 2023

-  **Download** `ACEInstall_1.29.3286.1447.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.29.3286.1447.exe>`_
-  **Download** `ACEInstall_1.29.3286.1447_minimal.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.29.3286.1447_minimal.exe>`_
-  **Download** `ACEInstall_1.29.3286.1447_offline.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.29.3286.1447_offline.exe>`_

**Release Notes:** A hotfix release to address an incompatibility with nuget project structure for installed plug-in packages developed for v1.29 of ACE.

ACE 1.29.3268.1439
------------------

**Released:** 5th October 2023

-  **Download** `ACEInstall_1.29.3268.1439.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.29.3268.1439.exe>`_
-  **Download** `ACEInstall_1.29.3268.1439_minimal.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.29.3268.1439_minimal.exe>`_
-  **Download** `ACEInstall_1.29.3268.1439_offline.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.29.3268.1439_offline.exe>`_

**Release Notes:** `ACE v1.29 Release Notes <https://wiki.analog.com/_media/resources/tools-software/ace/release_notes_-_ace_v1.29_external_.pdf>`_

Major Updates - Complete overhaul of how IIO components are supported in ACE, reflected in changes to the installer options. Command line communication tool no longer included. IIO hardware support now delivered through the ACE plug-in architecture.

Minor Updates - Further updates in-app to support alternate plug-in installation feeds. In the event a package feed is offline user can add a custom source as outlined in this article - :doc:`Alternative Plug-in Package Sources </wiki-migration/resources/tools-software/ace/alternativepackagesources>`

ACE 1.28.3258.1431
------------------

**Released:** 22nd August 2023

-  **Download** `ACEInstall_1.28.3258.1431.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.28.3258.1431.exe>`_
-  **Download** `ACEInstall_1.28.3258.1431_minimal.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.28.3258.1431_minimal.exe>`_
-  **Download** `ACEInstall_1.28.3258.1431_offline.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.28.3258.1431_offline.exe>`_

**Release Notes:** Minor Updates - Plug-in sources settings modified to support addition of alternate plug-in package feeds to install/update plug-ins through the in-app plug-in manager tool. In the event a package feed is offline user can add a custom source as outlined in this article - :doc:`Alternative Plug-in Package Sources </wiki-migration/resources/tools-software/ace/alternativepackagesources>`

ACE 1.28.3252.1429
------------------

**Released:** 2nd May 2023

**Download** `ACEInstall_1.28.3252.1429.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.28.3252.1429.exe>`_

**Release Notes:** `ACE v1.28 Release Notes <https://wiki.analog.com/_media/resources/tools-software/ace/release_notes_-_ace_v1.28_external_.pdf>`_

ACE 1.27.3250.1427
------------------

**Released:** 13th February 2023

**Download** `ACEInstall_1.27.3250.1427.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.27.3250.1427.exe>`_

**Release Notes:** `ACE v1.27 Release Notes <https://wiki.analog.com/_media/resources/tools-software/ace/release_notes_-_ace_v1.27_external_.pdf>`_

ACE 1.26.3240.1417
------------------

**Released:** 21st June 2022

**Download** `ACEInstall_1.26.3240.1417.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.26.3240.1417.exe>`_

**Release Notes:** `ACE v1.26 Release Notes <https://wiki.analog.com/_media/resources/tools-software/ace/release_notes_-_ace_v1.26_external_.pdf>`_

ACE 1.25.3217.1403 (hotfix)
---------------------------

**Released:** 23rd May 2022

**Download** `ACEInstall_1.25.3233.1412.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.25.3233.1412.exe>`_

**Release Notes:** `ACE v1.25 Hotfix Release Notes <https://wiki.analog.com/_media/resources/tools-software/ace/release_notes_-_ace_v1.25_external_.pdf>`_

ACE 1.25.3217.1403
------------------

**Released:** 4th March 2022

**Download** `ACEInstall_1.25.3217.1403.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.25.3217.1403.exe>`_

**Release Notes:** `ACE v1.25 Release Notes <https://wiki.analog.com/_media/resources/tools-software/ace/release_notes_-_ace_v1.25_external_.pdf>`_

ACE 1.24.3095.1398
------------------

**Released:** 11th November 2021

**Download** `ACEInstall_1.24.3095.1398.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.24.3095.1398.exe>`_

**Release Notes:** `ACE v1.24 Release Notes <https://wiki.analog.com/_media/resources/tools-software/ace/release_notes_-_ace_v1.24.pdf>`_

ACE 1.23.3085.1388 (hotfix)
---------------------------

**Released:** 13th August 2021

**Download** `ACEInstall_1.23.3085.1388.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.23.3085.1388.exe>`_

**Notes:**

-  Fixed typo in Memory Map "Side Effects" column
-  Fixed issue causing scripted transactions (e.g. macros) to fail with unset parameters

ACE 1.23.3077.1383
------------------

**Released:** 3rd August 2021

**Download** `ACEInstall_1.23.3077.1383.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.23.3077.1383.exe>`_

**Notes:**

-  Updated to .NET Framework 4.8
-  Unbundled "Core" ACE plug-ins, these may now receive updates outside of hotfixes or ACE releases
-  Added results to default Inverse FFT analysis
-  Added navigation pane to diagrams in ACE to support pan/zoom on larger diagrams
-  Increased supported data capture size and software limits removed
-  Added visual indicator to download button when application update is in progress
-  Removed asterisk prefix to notify users of Volatile/Side effect registers/bitfields

   -  Added a Boolean column to reflect the same information more easily

-  Fixed session saving bug resolved for unsupported XML characters in path
-  Fixed NCO block frequency property validation errors displayed on block
-  Fixed issue where waveform captures even when manually disabled
-  Fixed object retention issues when closing an active analysis node
-  Fixed issue getting page count for page groups under certain conditions
-  Fixed issue where capture status event was not raised when user stops capture
-  Fixed issue with BigInteger type not supported by engineering notation converters
-  Fixed issue where scripted macro properties were not re-evaluated

ACE 1.22.3072.1379 (hotfix)
---------------------------

**Released:** 7th July 2021

**Download** `ACEInstall_1.22.3072.1379.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.22.3072.1379.exe>`_

**Notes:**

-  Fix for limited precision in Vector Generator frequency inputs.
-  Fix for fixed point (integer) frequency input controls affecting Transceivers

ACE 1.22.3063.1372
------------------

**Released:** 6th May 2021

**Download** `ACEInstall_1.22.3063.1372.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.22.3063.1372.exe>`_

**Notes:**

-  Improved Register "hex" export option to include context/target chip
-  Import and replay "hex" or "acehex" Register Sequence/Macro files
-  FFT Grid aligned to sample frequency, log scale option
-  Improved wizard performance on expand/collapse
-  Fix for Analysis view keeping CPU busy
-  Fix for Averaging FFT for certain configurations
-  Fixes/Improvements for number formatting an unit scale
-  Onboard ADC support for SDP-K1
-  Open Scripts serialized as part of session
-  Improved IIO robustness

ACE 1.21.3008.1356 (hotfix)
---------------------------

**Released:** 2nd April 2021

**Download:** `ACEInstall_1.21.3008.1356.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.21.3008.1356.exe>`_

**Notes:**

-  Updated EvalClient for Transceivers

ACE 1.21.2994.1347 (hotfix)
---------------------------

**Released:** 8th Feburary 2021

**Download:** `ACEInstall_1.21.2994.1347.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.21.2994.1347.exe>`_

**Notes:**

-  Memory Map compatibility improvements

ACE 1.21
--------

**Released:** 25th January 2021

**Download:** `ACEInstall_1.21.2985.1344.exe <https://swdownloads.analog.com/ACE/ACEInstall_1.21.2985.1344.exe>`_

**Notes:**

-  Python 3.8 with NumPy & PythonNet bundled.
-  Enhancements to Analysis Graphs, new measurement cursors and annotations.
-  New Inverse FFT Analysis.
-  Improved IIO Support and reliability.
-  Updated Telerik, SciChart, Nlog Libraries for latest performance improvements and fixes.
-  Various bugfixes and general improvements.
