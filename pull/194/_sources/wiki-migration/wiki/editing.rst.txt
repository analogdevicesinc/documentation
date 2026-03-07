Page Editing
============

Developing Documentation is a combination of editing existing pages that others have created, and/or creating new pages.

Wiki pages are written in a simple, plain-text `syntax <https://wiki.analog.com/syntax>`_ with a few `extensions <https://wiki.analog.com/more_syntax>`_, that allows structuring the page and pleasant formatting while retaining high readability of the page source. When you edit a page and save your changes, the previous content will **not** be lost. Instead it will be saved as an old revision of the page in the `attic <https://www.dokuwiki.org/attic>`_ and can still be viewed or even restored.

Before you edit your first "real" page in the wiki, you should try out the possibilities in the :doc:`playground </wiki-migration/playground/playground>`. The playground is provided so that users can test things and play around to their heart's content. The playground is wiped out on a daily basis, so feel free to try out things there, and don't worry about making any permanent damage.

Editing Existing Pages
----------------------

To edit a page in the wiki, simply log in (you must be logged in, with a valid myAnalog account to edit wiki pages), and either :

-  edit the **entire page** at once, by clicking the button labeled "Edit this page" shown on the top of the page.
-  edit **a section**, by clicking the button labeled "Edit" underneath each section. By mousing over this edit button will highlight the section to be editted. Editing sections is sometimes easier, since it is just less text to deal with.

Clicking on either button will switch to `editing <https://wiki.analog.com/syntax>`_ mode for this page, and you can change the wiki source of this page in an embedded editor. Before saving changes (by clicking on the *Save* button), examine your changes, by looking at a *Preview* or see a difference, by clicking on the *Changes* button.

Creating new pages
------------------

There are two ways to create new pages. Both require that you are logged into the wiki and have special access (ie, normally that means you are an Analog Devices employee).

-  go to the page that you want to create (by typing in the exact path), and clicking on the "Create this page" link at the top of the page
-  create a link by editing an existing page, to something that doesn't exist, and then clicking on that link, and then clicking on the "Create this page" link at the top of the page.

The Creation/Editing Process
============================

Just like paper documentation, the wiki is able to differentiate between revisions of a document that are *Under Development* (which is private, typically for a unreleased product), *Draft*, and those that are *Approved*.

Public pages will always have a banner at the top of each page, with information about the Approval/Draft status. The banner is color-coded with an icon: A Green check mark for the latest approved version, and an orange exclamation point for all others.

The development process is something like:

<graphviz dot> digraph { subgraph cluster_0 {

::

         style=filled;
         color=lightgrey;
         node [style=filled,color=white];
         "Create new page" -> "Under Development" -> Edit -> "Under Development";
         label = "Under Development";
     }

::

     subgraph cluster_1 {
         node [style=filled];
         "Edit " -> Draft -> "Edit ";
         label = "Draft";
         color=blue
     }

"Under Development" -> Approve -> Published -> "Edit "; "Draft" -> Approve; } </graphviz>

Under Development
-----------------

When a page is initially created on the Wiki, it will only be visible to Analog Devices employees until it is approved. A message at the top of the page with the "draft" notice will note that the content can only be seen internally. A page can sit in this state forever, and be edited as many times as the creation team would like.

Once a page has been approved (by an ADI employee), it will be public and visible to both internal and external audiences. This allows documentation to be created over days/weeks before it becomes "public".

Once content is public, any edits made to it will also be public.

Drafts
------

Anyone logged into the wiki, can edit a page, and their version will be saved as a draft. You do not need to be an Analog Devices employee to edit a page. If you see a problem - please fix it.

Anyone not logged into the site will see the latest approved revision by default (unless there isn't one). All users can still view any revision of a page if they specifically request it -- whether or not it is approved.

Approvals
---------

Any Analog Devices Employee can *Approve* a page. You do so by clicking the "Approve document" link on the page header. Multiple people can approve the same page.

Troubleshooting
===============

In some cases, the editing of a page is impossible. This can be mainly for these reasons :

-  Some pages may be `locked <https://www.dokuwiki.org/locking>`_. This normally happens when someone else is editing the page.
-  You may have not enough rights to edit the page. In that case, you will have no edit button, but will instead show a button labeled "Show pagesource". To be able to edit the page, you might need to `login <http://my.analog.com>`_ first.

See also
--------

Read the following pages for further information:

-  `The edit window <https://www.dokuwiki.org/edit window>`_
-  `Formatting syntax <https://wiki.analog.com/syntax>`_ and `basic extensions we use <https://wiki.analog.com/more_syntax>`_
-  `Good style <https://www.dokuwiki.org/tips:good style>`_
-  `The edit summary <https://www.dokuwiki.org/summary>`_
-  `Old page revisions <https://www.dokuwiki.org/attic>`_
-  `Creating a new page <https://www.dokuwiki.org/page#create a page>`_
