Formatting Syntax
=================

`DokuWiki <https://www.dokuwiki.org/DokuWiki>`_ supports some simple markup language, which tries to make the datafiles to be as readable as possible. This page contains all possible syntax you may use when editing the pages. Simply have a look at the source of this page by pressing the *Edit this page* button at the top or bottom of the page. If you want to try something, just use the :doc:`playground </wiki-migration/playground/playground>` page. The simpler markup is easily accessible via `quickbuttons <https://www.dokuwiki.org/toolbar>`_, too.

Basic Text Formatting
---------------------

DokuWiki supports **bold**, *italic*, *underlined* and ``monospaced`` texts. Of course you can **``combine``** all these.

::

   DokuWiki supports **bold**, //italic//, __underlined__ and ''monospaced'' texts.
   Of course you can **__//''combine''//__** all these.

You can use :sub:`subscript` and :sup:`superscript`, too.

::

   You can use <sub>subscript</sub> and <sup>superscript</sup>, too.

You can mark something as [STRIKEOUT:deleted] as well.

::

   You can mark something as <del>deleted</del> as well.

**Paragraphs** are created from blank lines. If you want to **force a newline** without a paragraph, you can use two backslashes followed by a whitespace or the end of line.

| This is some text with some linebreaks
| Note that the two backslashes are only recognized at the end of a line
| or followed by
| a whitespace \\\\this happens without it.

::

   This is some text with some linebreaks\\ Note that the
   two backslashes are only recognized at the end of a line\\
   or followed by\\ a whitespace \\this happens without it.

You should use forced newlines only if really needed.

Links
-----

DokuWiki supports multiple ways of creating links.

External
~~~~~~~~

External links are recognized automagically: http://www.google.com or simply www.google.com - You can set the link text as well: `This Link points to google <http://www.google.com>`_. Email addresses like this one: andi@splitbrain.org are recognized, too.

::

   DokuWiki supports multiple ways of creating links. External links are recognized
   automagically: http://www.google.com or simply www.google.com - You can set
   link text as well: [[http://www.google.com|This Link points to google]]. Email
   addresses like this one: <andi@splitbrain.org> are recognized, too.

Internal
~~~~~~~~

Internal links are created by using square brackets. You can either just give a `pagename <https://wiki.analog.com/pagename>`_ or use an additional `link text <https://wiki.analog.com/pagename>`_.

::

   Internal links are created by using square brackets. You can either just give
   a [[/pagename|pagename]] or use an additional [[/pagename|link text]].

`Wiki pagenames <https://www.dokuwiki.org/pagename>`_ are converted to lowercase automatically, special characters are not allowed.

You can use `namespaces <https://wiki.analog.com/some/namespaces>`_ by using a colon in the pagename.

::

   You can use [[/some/namespaces|namespaces]] by using a colon in the pagename.

For details about namespaces see `namespaces <https://www.dokuwiki.org/namespaces>`_.

Linking to a specific section is possible, too. Just add the section name behind a hash character as known from HTML. This links to `this Section <https://wiki.analog.com/syntax>`_.

::

   This links to [[/syntax#internal|this Section]].

Notes:

-  Links to `existing pages <https://wiki.analog.com/syntax>`_ are shown in a different style from `nonexisting <https://wiki.analog.com/nonexisting>`_ ones.
-  DokuWiki does not use `CamelCase <https://en.wikipedia.org/wiki/CamelCase>`_ to automatically create links by default, but this behavior can be enabled in the `config <https://www.dokuwiki.org/config>`_ file. Hint: If DokuWiki is a link, then it's enabled.
-  When a section's heading is changed, its bookmark changes, too. So don't rely on section linking too much.

Interwiki
~~~~~~~~~

DokuWiki supports `Interwiki <https://www.dokuwiki.org/Interwiki>`_ links. These are quick links to other Wikis. For example this is a link to Wikipedia's page about Wikis: `Wiki <https://en.wikipedia.org/wiki/Wiki>`_.

::

   DokuWiki supports [[doku>Interwiki]] links. These are quick links to other Wikis.
   For example this is a link to Wikipedia's page about Wikis: [[https://en.wikipedia.org/wiki/Wiki|Wiki]].

The icons are used beside the wiki links to help quickly visually identify the destination site of the link. This saves the reader a mouseover to understand where they are going to go.

-  `Op Amp Applications Handbook <amazon>0750678445>`__ (a link to amazon)
-  `Interwiki <https://www.dokuwiki.org/Interwiki>`_ (a link to Dokuwiki)
-  `strlen <https://secure.php.net/strlen>`_ (php manual)
-  `Analog Devices <https://en.wikipedia.org/wiki/Analog Devices>`_ (wikipedia)

Additionally to the default dokuwiki interwiki links the following are available in this wiki:

Specific to the ADI website
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+------------+------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Tag        | Description                        | Example                                                                                                                 |
+============+====================================+=========================================================================================================================+
| adi        | Link to the Analog Devices website | ``[[:adi:`AD5755|AD5755]]```                                                                            |
+------------+------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| maxim      | Linux to the Maxim website         | ``[[https://www.maximintegrated.com/MAX77840|MAX77840]]``                                                               |
+------------+------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| footprints | Link to ADI's footprints           | ``[[:adi:`media/en/package-pcb-model-library/AD5755|AD5755]]```                                         |
+------------+------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| export     | ADI's export info                  | ``[[:adi:`AD5755|AD5755]]```                                                                            |
+------------+------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ez         | Link to the engineerzone           | ``[[:ez:`fpga|fpga]]```                                                                                 |
+------------+------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| reg        | Link to hardware registeration     | ``[[https://form.analog.com/Form_Pages/FeedBack/ADALM-PLUTO|ADALM-PLUTO]]``                                             |
+------------+------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ADI buy    | shopping cart                      | ``[[:adi:`en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADALM-PLUTO|Buy]]``` |
+------------+------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ibis       | Link to ibis models                | ``[[:adi:`media/en/package-pcb-model-library/ibis-models/LTC2876|LTC2876]]```                           |
+------------+------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| github     | ADI's open repos                   | ``[[https://github.com/libiio?master/CMakeLists.txt|CMakeLists.txt]]``                                                  |
+------------+------------------------------------+-------------------------------------------------------------------------------------------------------------------------+

.. tip::

   Some of the above (like footprint, and IBIS models) need a package suffix to function properly


Distributors
^^^^^^^^^^^^

+-------------+--------------------------------------------------------+----------------------------------------------------------------+
| Tag         | Description                                            | Example                                                        |
+=============+========================================================+================================================================+
| ``arrow``   | Link to Arrow's search                                 | ``[[arrow>ADALM-PLUTO]]``                                      |
+-------------+--------------------------------------------------------+----------------------------------------------------------------+
| ``digikey`` | Link to the digikey search, with a Digikey part number | ``[[https://www.digikey.com/345-1146-ND|345-1146-ND]]``        |
+-------------+--------------------------------------------------------+----------------------------------------------------------------+
| ``mouser``  | Link to Arrow's search                                 | ``[[https://www.mouser.com/584-ADALM-PLUTO|584-ADALM-PLUTO]]`` |
+-------------+--------------------------------------------------------+----------------------------------------------------------------+

.. tip::

   The above links to search, if you give an unambiguous, exact part number, it will take you to the product page, if it is not specific, it will drop you in search.


Others
^^^^^^

+---------------+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| oreilly       | Link to the O'Reilly book catalog | ``[[oreilly>9780596005900]]``                                                                                          | `Linux Devices Driver <oreilly>9780596005900>`__                                                                     |
+---------------+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| git.linux.org | Link to linux kernel tree         | ``[[https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/soc/codecs/adau1373.c|adau1373.c]]`` | `adau1373.c <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/soc/codecs/adau1373.c>`_ |
+---------------+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| xilinx        | Xilinx Website                    | ``[[https://www.xilinx.com/kc705|kc705]]``                                                                             | `kc705 <https://www.xilinx.com/kc705>`_                                                                             |
+---------------+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| mw            | MathWorks Website                 | ``[[https://www.mathworks.com/hardware-support/adalm-pluto-radio.html|PlutoSDR]]``                                     | `PlutoSDR <https://www.mathworks.com/hardware-support/adalm-pluto-radio.html>`_                                     |
+---------------+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+

Windows Shares
~~~~~~~~~~~~~~

Windows shares like `this <https://wiki.analog.com/\\server\share>`_ are recognized, too. Please note that these only make sense in a homogeneous user group like a corporate `Intranet <https://en.wikipedia.org/wiki/Intranet>`_.

::

   Windows Shares like [[/\\server\share|this]] are recognized, too.

Notes:

-  For security reasons direct browsing of windows shares only works in Microsoft Internet Explorer per default (and only in the "local zone").
-  For Mozilla and Firefox it can be enabled through different workaround mentioned in the `Mozilla Knowledge Base <http://kb.mozillazine.org/Links_to_local_pages_don't_work>`_.

Image Links
~~~~~~~~~~~

You can also use an image to link to another internal or external page by combining the syntax for links and `images <https://wiki.analog.com/>`_ (see below) like this:

::

   [[http://www.php.net|{{wiki:dokuwiki-128.png}}]]


   |dokuwiki-128.png|

Please note: The image formatting is the only formatting syntax accepted in link names.

The whole `image <https://wiki.analog.com/>`_ and `link <https://wiki.analog.com/>`_ syntax is supported (including image resizing, internal and external images and URLs and interwiki links).

Footnotes
---------

You can add footnotes  [1]_ by using double parentheses.

::

   You can add footnotes ((This is a footnote)) by using double parentheses.

Sectioning
----------


Headline Level 3
~~~~~~~~~~~~~~~~

Headline Level 4
^^^^^^^^^^^^^^^^

Headline Level 5
""""""""""""""""

::

   ==== Headline Level 3 ====
   === Headline Level 4 ===
   == Headline Level 5 ==

By using four or more dashes, you can make a horizontal line:

--------------

Images and Other Files
----------------------

You can include external and internal `images <https://www.dokuwiki.org/images>`_ with curly brackets. Optionally you can specify the size of them.

Real size:


|image1|

Resize to given width:


|image2|

Resize to given width and height [2]_:


|image3|

Resized external image:


|http://de3.php.net/images/php.gif|

::

   Real size:                        {{wiki:dokuwiki-128.png}}
   Resize to given width:            {{wiki:dokuwiki-128.png?50}}
   Resize to given width and height: {{wiki:dokuwiki-128.png?200x50}}
   Resized external image:           {{http://de3.php.net/images/php.gif?200x50}}

By using left or right whitespaces you can choose the alignment.

.. image:: https://wiki.analog.com/_media/wiki/dokuwiki-128.png
   :alt: dokuwiki-128.png
   :align: right

.. image:: https://wiki.analog.com/_media/wiki/dokuwiki-128.png
   :alt: dokuwiki-128.png
   :align: left

.. image:: https://wiki.analog.com/_media/wiki/dokuwiki-128.png
   :alt: dokuwiki-128.png
   :align: center

::

   {{ wiki:dokuwiki-128.png}}
   {{wiki:dokuwiki-128.png }}
   {{ wiki:dokuwiki-128.png }}

Of course, you can add a title (displayed as a tooltip by most browsers), too.

.. image:: https://wiki.analog.com/_media/wiki/dokuwiki-128.png
   :alt: This is the caption
   :align: center

::

   {{ wiki:dokuwiki-128.png |This is the caption}}

If you specify a filename (external or internal) that is not an image (``gif, jpeg, png``), then it will be displayed as a link instead.

For linking an image to another page see `#image_links <https://wiki.analog.com/>`_ above.

Lists
-----

Dokuwiki supports ordered and unordered lists. To create a list item, indent your text by two spaces and use a ``*`` for unordered lists or a ``-`` for ordered ones.

-  This is a list
-  The second item

   -  You may have different levels

-  Another item

-  The same list but ordered
-  Another item

   -  Just use indention for deeper levels

-  That's it

::

     * This is a list
     * The second item
       * You may have different levels
     * Another item

     * The same list but ordered
     * Another item
       * Just use indention for deeper levels
     * That's it

Also take a look at the `FAQ on list items <https://www.dokuwiki.org/faq:lists>`_.

Text Conversions
----------------

DokuWiki can convert certain pre-defined characters or strings into images or other text or HTML.

The text to image conversion is mainly done for smileys. And the text to HTML conversion is used for typography replacements, but can be configured to use other HTML as well.

Text to Image Conversions
~~~~~~~~~~~~~~~~~~~~~~~~~

DokuWiki converts commonly used `emoticon <https://en.wikipedia.org/wiki/emoticon>`_\ s to their graphical equivalents. Those `Smileys <https://www.dokuwiki.org/Smileys>`_ and other images can be configured and extended. Here is an overview of Smileys included in DokuWiki:

-  8-) %% 8-) %%
-  8-O %% 8-O %%
-  :-( %% :-( %%
-  :-) %% :-) %%
-  =) %% =) %%
-  :-/ %% :-/ %%
-  :-\\ %% :-\\ %%
-  :-? %% :-? %%
-  :-D %% :-D %%
-  :-P %% :-P %%
-  :-O %% :-O %%
-  :-X %% :-X %%
-  :-\| %% :-\| %%
-  ;-) %% ;-) %%
-  ^\_^ %% ^\_^ %%
-  :?: %% :?: %%
-  :!: %% :!: %%
-  LOL %% LOL %%
-  FIXME %% FIXME %%
-  DELETEME %% DELETEME %%

Text to HTML Conversions
~~~~~~~~~~~~~~~~~~~~~~~~

Typography: `dokuwiki <https://wiki.analog.com/dokuwiki>`_ can convert simple text characters to their typographically correct entities. Here is an example of recognized characters.

-> <- <-> => <= <=> >> << -- --- 640x480 (c) (tm) (r) "He thought 'It's a man's world'..."

::

   -> <- <-> => <= <=> >> << -- --- 640x480 (c) (tm) (r)
   "He thought 'It's a man's world'..."

The same can be done to produce any kind of HTML, it just needs to be added to the `pattern file <https://www.dokuwiki.org/entities>`_.

There are three exceptions which do not come from that pattern file: multiplication entity (640x480), 'single' and "double quotes". They can be turned off through a `config option <https://www.dokuwiki.org/config:typography>`_.

Quoting
-------

Some times you want to mark some text to show it's a reply or comment. You can use the following syntax:

::

   I think we should do it

   > No we shouldn't

   >> Well, I say we should

   > Really?

   >> Yes!

   >>> Then lets do it!

I think we should do it

   No we shouldn't

..

      Well, I say we should

   Really?

..

      Yes!

         Then lets do it!

Tables
------

DokuWiki supports a simple syntax to create tables.

=========== =================================== ===========
Heading 1   Heading 2                           Heading 3
=========== =================================== ===========
Row 1 Col 1 Row 1 Col 2                         Row 1 Col 3
Row 2 Col 1 some colspan (note the double pipe) 
Row 3 Col 1 Row 3 Col 2                         Row 3 Col 3
=========== =================================== ===========

Table rows have to start and end with a ``|`` for normal rows or a ``^`` for headers.

::

   ^ Heading 1      ^ Heading 2       ^ Heading 3          ^
   | Row 1 Col 1    | Row 1 Col 2     | Row 1 Col 3        |
   | Row 2 Col 1    | some colspan (note the double pipe) ||
   | Row 3 Col 1    | Row 3 Col 2     | Row 3 Col 3        |

To connect cells horizontally, just make the next cell completely empty as shown above. Be sure to have always the same amount of cell separators!

Vertical tableheaders are possible, too.

========= ==================== ===========
\         Heading 1            Heading 2
Heading 3 Row 1 Col 2          Row 1 Col 3
Heading 4 no colspan this time 
Heading 5 Row 2 Col 2          Row 2 Col 3
========= ==================== ===========

As you can see, it's the cell separator before a cell which decides about the formatting:

::

   |              ^ Heading 1            ^ Heading 2          ^
   ^ Heading 3    | Row 1 Col 2

   | Row 1 Col 3        |

   ^ Heading 4    | no colspan this time

   |                    |

   ^ Heading 5    | Row 2 Col 2

   | Row 2 Col 3        |

You can have rowspans (vertically connected cells) by adding ``:::`` into the cells below the one to which they should connect.

=========== ========================== ===========
Heading 1   Heading 2                  Heading 3
=========== ========================== ===========
Row 1 Col 1 this cell spans vertically Row 1 Col 3
Row 2 Col 1 :::                        Row 2 Col 3
Row 3 Col 1 :::                        Row 2 Col 3
=========== ========================== ===========

Apart from the rowspan syntax those cells should not contain anything else.

::

   ^ Heading 1      ^ Heading 2                  ^ Heading 3          ^
   | Row 1 Col 1    | this cell spans vertically | Row 1 Col 3        |
   | Row 2 Col 1    |                            | Row 2 Col 3        |
   | Row 3 Col 1    |                            | Row 2 Col 3        |

You can align the table contents, too. Just add at least two whitespaces at the opposite end of your text: Add two spaces on the left to align right, two spaces on the right to align left and two spaces at least at both ends for centered text.

==================== ============ ============
Table with alignment              
==================== ============ ============
right                center       left
left                 right        center
xxxxxxxxxxxx         xxxxxxxxxxxx xxxxxxxxxxxx
==================== ============ ============

This is how it looks in the source:

::

   ^           Table with alignment           ^^^
   |         right|    center    |left          |
   |left          |         right|    center    |
   | xxxxxxxxxxxx | xxxxxxxxxxxx | xxxxxxxxxxxx |

Note: Vertical alignment is not supported.

No Formatting
-------------

If you need to display text exactly like it is typed (without any formatting), enclose the area either with ``<nowiki>`` tags or even simpler, with double percent signs ``%%``.

This is some text which contains addresses like this: http://www.splitbrain.org and \**formatting*\*, but nothing is done with it. The same is true for //\__this\_\_ text// with a smiley ;-).

::

   <nowiki>
   This is some text which contains addresses like this: http://www.splitbrain.org and **formatting**, but nothing is done with it.
   </nowiki>
   The same is true for %%//__this__ text// with a smiley ;-)%%.

Code Blocks
-----------

You can include code blocks into your documents by either indenting them by at least two spaces (like used for the previous examples) or by using the tags ``<code>`` or ``<file>``.

::

   This is text is indented by two spaces.

::

   This is preformatted code all spaces are preserved: like              <-this

::

   This is pretty much the same, but you could use it to show that you quoted a file.

Those blocks were created by this source:

::

     This is text is indented by two spaces.

::

     This is preformatted code all spaces are preserved: like              <-this

::

   <file>
   This is pretty much the same, but you could use it to show that you quoted a file.
   </file>

Syntax Highlighting
~~~~~~~~~~~~~~~~~~~

:doc:`dokuwiki </wiki-migration/wiki/dokuwiki>` can highlight sourcecode, which makes it easier to read. It uses the `GeSHi <https://github.com/GeSHi/geshi-1.0>`_ Generic Syntax Highlighter -- so any language supported by GeSHi is supported. The syntax is the same like in the code and file blocks in the previous section, but this time the name of the used language is inserted inside the tag. Eg. ``<code java>`` or ``<file java>``.

.. code:: java

   /**
     * The HelloWorldApp class implements an application that
     * simply displays "Hello World!" to the standard output.
    */
   class HelloWorldApp {
       public static void main(String[] args) {
           System.out.println("Hello World!"); //Display the string.
       }
   }

The following language strings are currently recognized: *abap, actionscript-french, actionscript, actionscript3, ada, apache, applescript, asm, asp, autoit, avisynth, bash, basic4gl, bf, bibtex, blitzbasic, bnf, boo, c, c_mac, caddcl, cadlisp, cfdg, cfm, cil, cmake, cobol, cpp, cpp-qt, csharp, css, d, dcs, delphi, diff, div, dos, dot, eiffel, email, erlang, fo, fortran, freebasic, genero, glsl, gml, gnuplot, groovy, gettext, haskell, hq9plus, html, idl, ini, inno, intercal, io, java5, java, javascript, kixtart, klonec, klonecpp, latex, lisp, locobasic, lolcode, lotusformulas, lotusscript, lscript, lsl2, lua, m68k, make, matlab, mirc, modula3, mpasm, mxml, mysql, nsis, oberon2, objc, ocaml-brief, ocaml, oobas, oracle8, oracle11, pascal, perl, per, php-brief, php, pic16, pixelbender, plsql, povray, powershell, progress, prolog, properties, providex, python, qbasic, rails, rebol, reg, robots, ruby, sas, scala, scheme, scilab, sdlbasic, smalltalk, smarty, sql, tcl, teraterm, text, thinbasic, tsql, typoscript, vbnet, vb, verilog, vhdl, vim, visualfoxpro, visualprolog, whitespace, winbatch, whois, xml, xorg_conf, xpp, z80*

Downloadable Code Blocks
~~~~~~~~~~~~~~~~~~~~~~~~

When you use the ``<code>`` or ``<file>`` syntax as above, you might want to make the shown code available for download as well. You can to this by specifying a file name after language code like this:

::

   <file php myexample.php>
   <?php echo "hello world!"; ?>
   </file>

.. code:: php

   <?php echo "hello world!"; ?>

If you don't want any highlighting but want a downloadable file, specify a dash (``-``) as the language code: ``<code - myfile.foo>``.

Embedding HTML and PHP
----------------------

**Please Note**: HTML and PHP embedding is disabled, and will not be turned on on this wiki. (compare to other dokuwiki installations).

RSS/ATOM Feed Aggregation
-------------------------

`dokuwiki <https://wiki.analog.com/dokuwiki>`_ can integrate data from external XML feeds. For parsing the XML feeds, `SimplePie <http://simplepie.org/>`_ is used. All formats understood by SimplePie can be used in DokuWiki as well. You can influence the rendering by multiple additional space separated parameters:

+-------------+-----------------------------------------------------------------------------------------------------------------------+
| Parameter   | Description                                                                                                           |
+=============+=======================================================================================================================+
| any number  | will be used as maximum number items to show, defaults to 8                                                           |
+-------------+-----------------------------------------------------------------------------------------------------------------------+
| reverse     | display the last items in the feed first                                                                              |
+-------------+-----------------------------------------------------------------------------------------------------------------------+
| author      | show item authors names                                                                                               |
+-------------+-----------------------------------------------------------------------------------------------------------------------+
| date        | show item dates                                                                                                       |
+-------------+-----------------------------------------------------------------------------------------------------------------------+
| description | show the item description. If `HTML <https://www.dokuwiki.org/config:htmlok>`_ is disabled all tags will be stripped  |
+-------------+-----------------------------------------------------------------------------------------------------------------------+
| *n*\ [dhm]  | refresh period, where d=days, h=hours, m=minutes. (e.g. 12h = 12 hours).                                              |
+-------------+-----------------------------------------------------------------------------------------------------------------------+

The refresh period defaults to 4 hours. Any value below 10 minutes will be treated as 10 minutes. :doc:`dokuwiki </wiki-migration/wiki/dokuwiki>` will generally try to supply a cached version of a page, obviously this is inappropriate when the page contains dynamic external content. The parameter tells :doc:`dokuwiki </wiki-migration/wiki/dokuwiki>` to re-render the page if it is more than *refresh period* since the page was last rendered.

**Example:**

::

   [[https://wiki.analog.com/_media/rss>http///slashdot.org/index.rss 5 author date 1h|index.rss 5 author date 1h]]

`index.rss 5 author date 1h <https://wiki.analog.com/_media/rss>http///slashdot.org/index.rss 5 author date 1h>`__

Control Macros
--------------

Some syntax influences how DokuWiki renders a page without creating any output it self. The following control macros are availble:

+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Macro       | Description                                                                                                                                                                                 |
+=============+=============================================================================================================================================================================================+
+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Syntax Plugins
--------------

DokuWiki's syntax can be extended by `Plugins <https://www.dokuwiki.org/plugins>`_. How the installed plugins are used is described on their appropriate description pages. The following syntax plugins are available in this particular DokuWiki installation:

~~\ INFO:syntaxplugins\ ~~

.. [1]
   This is a footnote

.. [2]
   when the aspect ratio of the given width and height doesn't match that of the image, it will be cropped to the new ratio before resizing

.. |dokuwiki-128.png| image:: https://wiki.analog.com/_media/wiki/dokuwiki-128.png
   :target: http://www.php.net
.. |image1| image:: https://wiki.analog.com/_media/wiki/dokuwiki-128.png
.. |image2| image:: https://wiki.analog.com/_media/wiki/dokuwiki-128.png
   :width: 50px
.. |image3| image:: https://wiki.analog.com/_media/wiki/dokuwiki-128.png
   :width: 200px
   :height: 50px
.. |http://de3.php.net/images/php.gif| image:: http://de3.php.net/images/php.gif
   :width: 200px
   :height: 50px
