Translating Scopy
=================

Current Scopy Translations
--------------------------

To try to make scopy (and electronics in general) accessible to students, we attempt to make it available in local language. This tries to ensure that students aren't struggling with the concepts and a potential language barrier at the same time. If you are interested in making a translation - thanks, we and future students of your language will thank you, it only takes a few hours, and the instructions are below.

Before making a new translation for Scopy, check to ensure there isn't an existing `translation file <https://github.com/scopy?master/resources/translations>`_ for the language or plugin you are thinking about. We try to maintain Arabic, Simplified Chinese, Traditional Chinese, English, French, German, Italian, Japanese, Korean, Romanian, Spanish and Thai.

If you find a mistake in any of the translations, please :git-scopy:`let us know <issues>` (or better, send us a pull request).

Installing Qt Linguist
~~~~~~~~~~~~~~~~~~~~~~

Windows Users: Download Qt Linguist executable from here: `QtLinguist Download <https://download.qt.io/linguist_releases/>`_ and run it.

Linux Users: Open a terminal and run the following commands:

::

        **sudo apt-get update
        sudo apt-get install qttools5-dev-tools**

.. _translating-scopy-1:

Translating Scopy
~~~~~~~~~~~~~~~~~

Windows Users: Search for Qt Linguist and open the application. Linux Users: From a terminal window, run the following commands:

::

       **locate linguist
       ./path/to/file/linguist**

| Download the translation source file from :git-scopy:`here <resources/translations/scopy_en.ts>`.
| Open Qt Linguist and click Open File and open the file you downloaded. Select the target language and country for your translation. That means the language to which you are translating Scopy. Then click OK.
| |translation_target_language.png|
| A list of all text fields in Scopy should appear after opening the file.
| |translation_field.png|
| Enter your translation in the field indicated by the red arrow. To validate the translation and move on to the next unfinished item, click the green tick highlighted in the figure above. Repeat until you reach the end of the list.

Notes
^^^^^

**! Some text lists may contain the following items: “Form”, “TextLabel”. These do not require translating, as they are not visible to the user. No translation or using the original text would be enough.**

\*\* ! If you want to take a break from translating, be sure to save your file by clicking “Save as” in the File tab. \*\*

**! Respect the spacing and terminating characters in the source text fields, to avoid warnings from Qt5-linguist.**

After you have validated all translations, go to the File tab and click “Release as”. Select the destination folder and release your translation. This reusults in a .qm file, with the translations which Scopy can interpret. Now place the .qm file in ./translations and name it <language>.qm if the translation is meant for the core application. Otherwise, if you translated a plugin, name it <plugin_name>\_<language>.qm (this requires the core <language>.qm file to exist).

| 
| |translation_release.png|
| Now, to run Scopy in your desired language, open the application and go to Preferences. Open the language combo box and select your preferred language. All plugin translations for the specified language will be loaded automatically. Close the application and when you reopen it, you’ve got Scopy in your mother tongue!

.. |translation_target_language.png| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/translation_target_language.png
.. |translation_field.png| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/translation_field.png
.. |translation_release.png| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/translation_release.png
