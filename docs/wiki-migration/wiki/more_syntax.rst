DokuWiki Test Page
==================

This page is intended for verifying that upgrades of DokuWiki did not break our existing plugins and customizations. Every change that matters should be sampled on this page.

Remember that you have to edit this page in order to force a cache refresh.

blockquote
----------

<blockquote> Indeed, the purpose of an encyclopedia is to collect knowledge disseminated around the globe; to set forth its general system to the men with whom we live, and transmit it to those who will come after us, so that the work of preceding centuries will not become useless to the centuries to come; and so that our offspring, becoming better instructed, will at the same time become more virtuous and happy, and that we should not die without having rendered a service to the human race. <cite>\ `Denis Diderot <https://en.wikipedia.org/wiki/Denis Diderot>`__\ `Encyclopédie, Vol. 5 (1755), pp. 635–648A <http://quod.lib.umich.edu/cgi/t/text/text-idx?c=did;cc=did;idno=did2222.0000.004;rgn=main;view=text>`__\ </cite> </blockquote>

definitionlist
--------------

`Definitions <https://www.dokuwiki.org/plugin:definitionlist>`__.

You can apply normal wiki syntax to the definition list.

::

   ; **Pizza** : Food : Delicious : Mausi
   ; **''Curry''**
   : Korma
     ; ''kasmiri'' : fruity
     ; //ceylonese// : coconutty
   : Bhoona

folded
------

If you want to make additional information available that is `folded or hidden <https://www.dokuwiki.org/plugin:folded>`__ by default, you have two options

Inline:
~~~~~~~

This is example ~~text \| with some of it only shown when you unfold it~~. And after that the text just continues to flow in the same paragraph.

Block:
~~~~~~

This is example text.

~~~~ Title \|

========== ============= =========================
This table is only shown when you unfold the block
========== ============= =========================


.. note::

   See `some other wiki page <https://wiki.analog.com/some other wiki page>`__


========== ============= =========================
This table is only shown when you unfold the block
========== ============= =========================

~~~~

graphviz
--------

This can create directed and non-directed graph images from a textual description language called “\ `dot <http://www.graphviz.org/doc/info/lang.html>`__\ ” using the Graphviz program. `graphviz <https://www.dokuwiki.org/plugin:graphviz>`__.

<graphviz dot> digraph { 1 -> 2 -> 3 -> 4 -> 5 ->6 -> 1; 1 -> 3 -> 5; 2 -> 4 -> 6; } </graphviz>

::

   <graphviz dot>
   digraph {
    1 -> 2 -> 3 -> 4 -> 5 ->6 -> 1;
    1 -> 3 -> 5;
    2 -> 4 -> 6;
   }
   </graphviz>

include
-------

Allows you to `include <https://www.dokuwiki.org/plugin:include>`__ different wiki pages in the current page. Simply enclose the ID of the page to be included in double curly brackets:

::

   
.. note::

   See `[id] <https://wiki.analog.com/[id]#[section]>`__


+-----------+------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------+
| [id]      | page ID of the page to include; some `#macros <https://wiki.analog.com/>`__ are possible; shortcuts are resolved (``:``, ``.``, ``..``)  | required                            |
+===========+==========================================================================================================================================+=====================================+
| [section] | limits the included page to a specific section and its subsections                                                                       | optional; default is the whole page |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------+
| [flags]   | flags delimited by ``&``, see `#flags <https://wiki.analog.com/>`__                                                                      | optional                            |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------+

+------------------+--------------+-----------------------------------------------------------------+------------------+------------------------------------------------+
| flags            | Default      |                                                                 | Alternative      |                                                |
+==================+==============+=================================================================+==================+================================================+
| ``firstseconly`` | ``fullpage`` | includes the whole page                                         | ``firstseconly`` | includes only the first section of a wiki page |
+------------------+--------------+-----------------------------------------------------------------+------------------+------------------------------------------------+
| ``showfooter``   | ``footer``   | shows a footer below the page with info about the included page | ``nofooter``     | hides the page info footer                     |
+------------------+--------------+-----------------------------------------------------------------+------------------+------------------------------------------------+
| ``showeditbtn``  | ``editbtn``  | shows a button to edit (or create) the included page            | ``noeditbtn``    | hides the edit (or create) button              |
+------------------+--------------+-----------------------------------------------------------------+------------------+------------------------------------------------+
| etc              | etc          | etc                                                             | ``noheader``     | strips the title from the included page        |
+------------------+--------------+-----------------------------------------------------------------+------------------+------------------------------------------------+

Example:

::

   .. include:: ../start.rst

provides the first section of the start page .. include:: ../start.rst

interwiki links
---------------

| `analog devices <adi>>`__
| `blackfin.uclinux.org <bf>>`__
| `digikey <https://www.digikey.com/ADDS-BF537-STAMP>`__
| `O'Reilly <oreilly>>`__
| `docs.blackfin.uclinux.org <docs>>`__

There are some *special* internal links which have icons associated with them:

-  `Software/Tools <driver>>`__
-  `Linux drivers <linux>>`__

math
----

::

   <m size>...mathematical formulae...</m>

size (optional) the base glyph size in pixels - default value: 12.

alignment can be controlled in the same way as DokuWiki images, one space to the left to right align, one to the right to left align, one on each side to centre.

-   :math:`S(f)(t)=a_{0}+sumn=1+inftya_{n} cos(n \omega t)+b_{n} sin(n \omega t)`
-  <m 8>delim{lbrace}{matrix{3}{1}\ |3x-5y+z=0} {sqrt{2}x-7y+8z=0} {x-8y+9z=0|}{ }</m>
-  <m 16>delim{\|}\ |1/N} sum{n=1}{N}{gamma(u_n)} - 1/{2 pi} int{0}{2 pi}{gamma(t) dt|\ {\|} <= epsilon/3</m>

syntax can be found in the `math <https://wiki.analog.com/math>`__ page.

note
----

Notes have changed recently -- please use the new format. With the new format, comes new options! You can control the corners (square [default] or round), if it has an icon or not, and the width. See the examples below.

.. note::

   
   ::
   
   .. note::

            text which you want in the box

   


.. tip::

   
   ::
   
   .. tip::

      text which you want in the box

   


.. important::

   
   ::
   
   .. important::

      text which you want in the box

   


.. warning::

   
   ::
   
   .. warning::

      text which you want in the box

   


.. hint::

   
   ::
   
   .. hint::

      text which you want in the box

   


.. admonition:: Download
   :class: download

   
   ::
   
   .. admonition:: Download
      :class: download

            * list of files to download

   


.. note::

   
   ::
   
   .. note::

            * list of things todo, or that are in progress

   


**Safety Notes:**

.. danger::

   **danger** - normal text is white.

   
   ::
   
   .. danger::

            //**DANGER**// - normal text is white.

   


.. warning::

   **warning** - normal text is black.

   
   ::
   
   .. warning::

            //**warning**// - normal text is black.

   


.. caution::

   **caution** - normal text is black.

   
   ::
   
   .. caution::

            //**caution**// - normal text is black.

   


.. container:: round notice

   **notice** - normal text is white

   
   ::
   
   .. container:: round notice

            //**notice**// - normal text is white

   


.. container:: round safety

   **safety** - normal text is white

   
   ::
   
   .. container:: round safety

            //**safety**// - normal text is white

   


You can use notes and boxes also inside text with paragraphs like this (the key thing to notice is the case of the ``WRAP`` or ``wrap`` keyword):

.. note::

   
   .. note::

      info

   


, text between

.. hint::

   help


, text between

.. warning::

   alert


, text between

.. important::

   important


, text between

.. tip::

   tip


, text between

.. admonition:: Download
   :class: download

   download


, text between

.. note::

   todo


and

.. container:: round box

   round box


and

.. danger::

   danger


,

.. warning::

   warning


,

.. caution::

   caution


,

.. container:: notice

   notice


,

.. container:: safety

   safety


.

::

.. note::

   info


,

.. hint::

   help


, ...

source
------

``source`` is used to grap source code from the svn or git repositories. Since you may want to grab different parts of the file, it accepts lots of different options, but the main flavour is:

::

   <source path:part language repository>

where part can be, numeric, two regular expressions (no spaces - it's a bug I haven't cared about - complain if it is a big deal to you), or function names.

::

    /1-3/         : captures from lines 1 to 3
    /foo/-/bar/   : captures from the first occurrence of "foo",
                     to the next occurrence of "bar"
    /foo/2-/bar/  : captures from the 2nd occurrence of "foo,
                     to the next occurrence of "bar"
    /foo/12-3/^$/ : captures from the 12th occurrence of "foo",
                     to the 3rd next blanks line
    /foo/-EOF     : captures from the first occurrence of "foo",
                     to the end of file
    foo{}         : functions
    foo[]         : arrays
    foo()         : scopes

If your regular expressions are a little rusty - check out a short `reference <http://www.regular-expressions.info/reference.html>`__

path can also have globs in it - it help pick the latest version in a branch. for example, this uses latest busybox version in trunk (sometimes there is more than one)

::

   <source master/cf_lib/edk/pcores/axi_adc_2c_v1_00_a/regmap.txt:/REGISTER/-/0x02/ txt fpgahdl_xilinx> 

<source master/cf_lib/edk/pcores/axi_adc_2c_v1_00_a/regmap.txt:/REGISTER/-/0x02/ txt fpgahdl_xilinx>

For example:

::

   <source trunk/README:0-5 text linux-kernel>

<source trunk/README:0-5 text linux-kernel>

::

   <source trunk/arch/blackfin/mm/isram-driver.c:IADDR2DTEST() c linux-kernel>

<source trunk/arch/blackfin/mm/isram-driver.c:IADDR2DTEST() c linux-kernel>

xterm
-----

::

   $ this is a shell prompt

xterms within ``

<WRAP box>`` tags, to give things different colours/titles:

.. container:: box bgred

   
   .. warning::

      root user on the host, or development computer

   
   ::
   
      test:~ #> **whoami**
      root
      test:~ #>
   


.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      Linux:~ $> **whoami**
      username
      Linux:~ $>
   


wrap
----

Examples for the Wrap Plugin
============================

Basic syntax
------------

An uppercase **<WRAP>** (or alternatively **<block>** or **<div>**) creates a **``div``** and should be used for **"big"** containers, **surrounding** paragraphs, lists, tables, etc.

::

.. container:: classes width :language

      "big" content


or
   <block classes width :language>
   "big" content
   </block>

   or
   <div classes width :language>
   "big" content
   </div>

A lowercase **<wrap>** (or alternatively **<inline>** or **<span>**) creates a **``span``** and should be used for **"small"** containers, **inside** paragraphs, lists, tables, etc.

::

.. container:: classes width :language

   "small" content


or
   <inline classes width :language>"small" content</inline>

   or
   <span classes width :language>"small" content</span>

:!: Please note, some things **won't work with lowercase spans**:

-  **alignments** (including alignments generated by changing the text direction)
-  **multi-columns**
-  and **widths**

if the according wrap isn't floated as well.

Classes and Styles
------------------

Columns and Floats
~~~~~~~~~~~~~~~~~~

You can have columns easily by adding the class ``column`` and a width, e.g.

::

.. container:: column

   ...content...


.. container:: column

   **Emulated Big Headline**

   
   You can emulate a big headline with italic, bold and underlined text, e.g.
   
   ::
   
      //**__Emulated Big Headline__**//
   
   **Emulated Small Headline**
   
   A smaller headline uses no underlining, e.g.
   
   ::
   
      //**Emulated Small Headline**//
   
   If you need text that is bold and italic, simply use it the other way around:
   
   ::
   
      **//No Headline//**
   


.. container:: column

   **Different Floating Options**

   
   Normally you would only need the class ``column``, but for more sophisticated uses (not only for columns, but for any other classes, like `#boxes_and_notes <https://wiki.analog.com/>`__ as well) you can have several kinds of "floats":
   
   -  **``column``** is the same as ``left`` in LTR languages and the same as ``right`` in RTL languages
   -  **``left``** will let you float your wrap on the left
   -  **``right``** will let the wrap float right
   -  **``center``** will position the wrap in the horizontal center of the page
   


.. container:: column

   **Widths**

   
   You can set any valid widths (but only on divs): ``%, px, em, ex, pt, pc, cm, mm, in``, but most of the time you'd only want either
   
   +--------+-----------+-----------------------------------------------------------------------------------------------------------------+
   | type   | e.g.      | note                                                                                                            |
   +========+===========+=================================================================================================================+
   | ``%``  | ``30%``   | makes sense in a liquid layout                                                                                  |
   +--------+-----------+-----------------------------------------------------------------------------------------------------------------+
   | ``px`` | ``420px`` | makes sense if your layout has a fixed pixel width or if your container contains images with a certain width    |
   +--------+-----------+-----------------------------------------------------------------------------------------------------------------+
   | ``em`` | ``20em``  | makes sense if you like your wrap container to grow and shrink with the font size or if your layout is em-based |
   +--------+-----------+-----------------------------------------------------------------------------------------------------------------+
   
   A **table** inside a column or box will always be **100% wide**. This makes positioning and sizing tables possible.
   


.. container:: em

   After using any of the float classes, you might come across something like this, where the following text protrudes into the space where only the floating containers should be ...



... to prevent that, you should simply add

::


after your last column.

You **can** use the same options with spans (as each element that floats is automatically a block level element), but it probably doesn't make too much sense. :!: Widths on spans normally do not work (by design), but can make sense, when it is floating.

:!: Attention: Widths can cause problems and will often look different and break in some browsers. If you're not a web developer, you might not understand any problems regarding the `box model <https://en.wikipedia.org/wiki/Internet_Explorer_box_model_bug>`__. Just try to test your columns in all major browsers and make your widths smaller than you initially think they should be.

All of those options will also work in the `#boxes_and_notes <https://wiki.analog.com/>`__ wraps (see below).

Multi-columns
^^^^^^^^^^^^^

.. container:: col3

   For modern browsers (Firefox, Chrome and Safari) you can use multi-columns. Just use **``col2``** for 2 columns, **``col3``** for 3 columns, **``col4``** for 4 columns and **``col5``** for 5 columns.

   
   :!: Note: Multi-columns don't make sense for spans.


Alignments
~~~~~~~~~~

You can use these different text alignments:

-  ``leftalign``
-  ``rightalign``
-  ``centeralign``
-  ``justify``

.. container:: centeralign

   Center aligned text ...


.. container:: rightalign

   ... and right aligned.


::

.. container:: centeralign

      Center aligned text ...


.. container:: rightalign

      ... and right aligned.


:!: You cannot add alignments to spans.

Boxes and Notes
~~~~~~~~~~~~~~~

.. container:: round box 570px center

   **round box 570px center**

   
   -  ``box`` creates a box around the container and uses the colours from the template's ``style.ini`` as default colours (``__background_alt__`` and ``__text__``)
   -  any of the classes ``info``, ``tip``, ``important``, ``alert``, ``help``, ``download``, ``todo`` will add a special note container with a corresponding icon
   -  the classes ``danger``, ``warning``, ``caution``, ``notice``, ``safety`` use safety colours (and no icons)
   -  ``round`` can be added to anything with a background colour or a border and will only work in modern browsers (no Internet Explorer)
   


.. note::

   **Info**

   
   ::
   
   


.. tip::

   **Tip**

   
   ::
   
   


.. important::

   **Important**

   
   ::
   
   


.. warning::

   **Alert**

   
   ::
   
   


.. hint::

   **Help**

   
   ::
   
   


.. admonition:: Download
   :class: download

   **Download**

   
   ::
   
   


.. note::

   **Todo**

   
   ::
   
   



**Safety Notes:**

.. danger::

   **Danger**

   
   ::
   
   


.. warning::

   **Warning**

   
   ::
   
   


.. caution::

   **Caution**

   
   ::
   
   


.. container:: round notice left

   **Notice**

   
   ::
   
   


.. container:: round safety left

   **Safety**

   
   ::
   
   



You can use notes and boxes also inside text with spans like this:

.. note::

   info


,

.. hint::

   help


,

.. warning::

   alert


,

.. important::

   important


,

.. tip::

   tip


,

.. admonition:: Download
   :class: download

   download


,

.. note::

   todo


and

.. container:: round box

   round box


and

.. danger::

   danger


,

.. warning::

   warning


,

.. caution::

   caution


,

.. container:: notice

   notice


,

.. container:: safety

   safety


.

::

.. note::

   info


,

.. hint::

   help


, ...

Marks
~~~~~

You can mark text as

.. container:: hi

   highlighted


,

.. container:: lo

   less significant


and

.. container:: em

   especially emphasised


.

::

   You can mark text as

.. container:: hi

   highlighted


,

.. container:: lo

   less significant


and

.. container:: em

   especially emphasised


.

:!: This might look ugly in some templates and should be adjusted accordingly.

Miscellaneous
~~~~~~~~~~~~~

Indent
^^^^^^

.. container:: indent

   This text will appear indented.


::

.. container:: indent

   This text will appear indented.


Outdent
^^^^^^^

.. container:: outdent

   This text will appear "outdented".


::

.. container:: outdent

   This text will appear "outdented".


Prewrap
^^^^^^^

.. container:: prewrap 250px

   
   ::
   
      Inside this code block the words will wrap to a new line although they are all in one line.
   


::

.. container:: prewrap 250px

   
   ::
   
        Inside this code block the words will wrap to a new line although they are all in one line.
   
   ::
   


Spoiler
^^^^^^^

Here follows a spoiler:

.. container:: spoiler

   Darth Vader is Luke's father.


::

   Here follows a spoiler:

.. container:: spoiler

   Darth Vader is Luke's father.


Just select the text in the spoiler box to be able to read its content.

Hide
^^^^

The following text is hidden:

.. container:: hide

   John, please revise that sentence.


::

   The following text is hidden:

.. container:: hide

   John, please revise that sentence.


:!: Warning: The text will still appear in the source code, in non-modern browsers and is searchable. Do not hide any security risky secrets with it!

Pagebreak
^^^^^^^^^

The following will add a pagebreak:


::

   The following will add a pagebreak:


This has no effect on the browser screen. A `pagebreak <http://reference.sitepoint.com/css/page-break-after>`__ will force a new page in printouts.

Nopagebreak
^^^^^^^^^^^

The following will try to avoid a pagebreak:

.. container:: nopagebreak

   much content, belonging together (like a long table)


::

   The following will try to avoid a pagebreak:

.. container:: nopagebreak

   much content, belonging together (like a long table)


This also has no effect on the browser screen. It will try to `avoid a page break <http://reference.sitepoint.com/css/page-break-inside>`__ in printouts.

Noprint
^^^^^^^

.. container:: noprint

   This text appears on the screen, but not in print.


::

.. container:: noprint

   This text appears on the screen, but not in print.


Onlyprint
^^^^^^^^^

.. container:: onlyprint

   This text does not appear on the screen, but only in print.


::

.. container:: onlyprint

   This text does not appear on the screen, but only in print.


Typography
~~~~~~~~~~

I advise against using the following typography classes. It's better to create semantic classes that reflect their meaning instead.

-  font family: ``sansserif``, ``serif``, ``monospace``
-  font size: ``bigger``, ``muchbigger``, ``smaller``
-  font colour: ``fgred``, ``fggreen``, ``fgblue``, ``fgcyan``, ``fgviolet``, ``fgyellow``, ``fggrey``, ``fgwhite``, ``fgblack``
-  background colour: ``bgred``, ``bggreen``, ``bgblue``, ``bgcyan``, ``bgviolet``, ``bgyellow``, ``bggrey``, ``bgwhite``, ``bgblack``

Combining and Nesting
~~~~~~~~~~~~~~~~~~~~~

You can combine and nest all classes and types of boxes, e.g.

.. container:: box bggreen fgblack 350px right :en

   **Outer green box floats right**

   
   .. container:: 165px left

      Inner nested box floats left and is partly

         
         .. container:: em hi

            \ *em*\ phasized and *hi*\ ghlighted with nested

                     
                     .. container:: bigger

                        \ *bigger* text

                     
            inside

         
      .

   
   Text inside outer right box, but beneath inner left box.
   
   
   .. tip::

      Round tip box underneath, after a ``clear``.

   


::

.. container:: box bggreen fgblack 350px right :en

      //**__Outer green box floats right__**//
   
   .. container:: 165px left

            Inner nested box floats left and is partly
         
         .. container:: em hi

            __em__phasized and __hi__ghlighted with nested

                     
                     .. container:: bigger

                        __bigger__ text

                     
            inside

         
         .

   
   Text inside outer right box, but beneath inner left box.
   
   
   .. tip::

            Round tip box underneath, after a ''clear''.

   


Language and Text Direction
---------------------------

You can change the language and the reading direction of a wrap container by simply adding a colon followed by the language code, like this:

::

.. container:: :he

      זוהי עברית. ((
   
   .. container:: :en

      This means "This is Hebrew.", at least according to [[http://translate.google.com/|Google Translate]].

   
   ))


.. container:: :he

   זוהי עברית.  [1]_


The text direction (``rtl``, right to left or ``ltr``, left to right) will get inserted automatically and is solely dependent on the language. The list of currently supported languages is taken from: http://meta.wikimedia.org/wiki/Template:List_of_language_names_ordered_by_code (If you specify a language not listed there, it simply won't do anything.)

Analog TV
---------

<code> |analogTV>983688886001|\ </code>

To find this magic number, search on ``www.analog.com`` for the video that you want to include in the wiki. In this case, when I search for ``Automotive Safety Systems and Radar`` (words from the title), search provides : ``http://www.analog.com/en/education/education-library/videos/983688886001.html``. Just use the number, without the ``.html`` at the end of the url.

If you goto the :adi:`videos section <en/education/education-library/videos.html>`, it is a little more difficult. Just click on the ``get code`` button, near the bottom of the players. This will bring up something that says ``embed code``. In the ``<object id=...`` string, there will be a portion which is the ``videoId=983688886001``. Just use this number.

Any video on ``www.analog.com`` will work this way.

.. image:: https://wiki.analog.com/_media/analogTV>983688886001
   :alt: analogTV>983688886001

YouTube
-------

Works the same/similar way:

<code> |youtube>LCf-\_iREESQ|\ </code>

find the video you want to watch, and then use it's "tag" in the url to encode it.

.. image:: https://wiki.analog.com/_media/youtube>LCf-_iREESQ
   :alt: youtube>LCf-\_iREESQ

.. [1]

.. container:: :en

   This means "This is Hebrew.", at least according to `Google Translate <http://translate.google.com/>`__.


.. |3x-5y+z=0} {sqrt{2}x-7y+8z=0} {x-8y+9z=0| image:: https://wiki.analog.com/_media/3x-5y+z=0} {sqrt{2}x-7y+8z=0} {x-8y+9z=0
.. |1/N} sum{n=1}{N}{gamma(u_n)} - 1/{2 pi} int{0}{2 pi}{gamma(t) dt| image:: https://wiki.analog.com/_media/1/N} sum{n=1}{N}{gamma(u_n)} - 1/{2 pi} int{0}{2 pi}{gamma(t) dt
.. |analogTV>983688886001| image:: https://wiki.analog.com/_media/analogTV>983688886001
.. |youtube>LCf-\_iREESQ| image:: https://wiki.analog.com/_media/youtube>LCf-_iREESQ
