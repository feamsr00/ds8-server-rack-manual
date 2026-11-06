DS-8 Server Rack System Manual
==============================

*Edition 11/2026, for mod version 5.12.7. A community manual maintained by Raven; see* :ref:`About this manual <about>`.

.. image:: /images/icons.png
   :alt: The mod's own icons: the DS-8 Server Rack, a data drive and the rack key
   :width: 55%
   :align: center

The DS-8 Server Rack is a full-height cabinet that stores data, runs up to twelve IC10 programs, and automates a base without a line of code. It holds eight hot-swap data drives with 4,096 memory cells between them by default, twelve processor sockets, a system board and a backup battery, and you operate it from a front panel of 157 controls and a small operating system with thirteen programs.

.. admonition:: WARNING
   :class: danger

   The rack can control airlocks, doors and the air in your rooms, and a mistake in a rule, a library task or a program can open a door to vacuum with someone standing behind it. Read :ref:`2 Safety <ch-safety>` before you let the rack control anything that keeps you alive.

.. rubric:: Find what you need

+-----------------------------------------------------+--------------------------------------------------------+
| I want to                                           | Go to                                                  |
+=====================================================+========================================================+
| Put a rack together and power it up                 | :ref:`3.5 Installing the rack <sec-3-5>`,              |
|                                                     | :ref:`3.6 First power-up <sec-3-6>`                    |
+-----------------------------------------------------+--------------------------------------------------------+
| Find out what a switch, knob or lamp does           | :ref:`4 Controls and indicators <ch-controls>`         |
+-----------------------------------------------------+--------------------------------------------------------+
| Find my way around the screen                       | :ref:`5 DS-8 OS <ch-os>`                               |
+-----------------------------------------------------+--------------------------------------------------------+
| Automate the base without writing code              | :ref:`5.15 Rules <os-rules>`,                          |
|                                                     | :ref:`5.16 Scenes <os-scenes>`,                        |
|                                                     | :ref:`5.17 Library <os-library>`                       |
+-----------------------------------------------------+--------------------------------------------------------+
| Protect or back up my data                          | :ref:`6.5 Write protection <sec-6-5>`,                 |
|                                                     | :ref:`6.6 Backups <sec-6-6>`                           |
+-----------------------------------------------------+--------------------------------------------------------+
| Change a setting                                    | :ref:`7 Configuration <ch-configuration>`              |
+-----------------------------------------------------+--------------------------------------------------------+
| Clean the filter, service the battery or update the | :ref:`8 Maintenance <ch-maintenance>`                  |
| OS                                                  |                                                        |
+-----------------------------------------------------+--------------------------------------------------------+
| Fix something that has gone wrong                   | :ref:`9.4 Troubleshooting <sec-9-4>`                   |
+-----------------------------------------------------+--------------------------------------------------------+
| Find out what an event message means                | :ref:`Appendix C: Event messages <app-c>`              |
+-----------------------------------------------------+--------------------------------------------------------+
| Put a control back to its factory position          | :ref:`Appendix B: Factory defaults <app-b>`            |
+-----------------------------------------------------+--------------------------------------------------------+
| Look up a specification                             | :ref:`Appendix A: Technical data <app-a>`              |
+-----------------------------------------------------+--------------------------------------------------------+
| Write an IC10 program                               | :ref:`11 Programming (IC10) <ch-programming>`,         |
|                                                     | :ref:`11.5 Access from programs <sec-11-5>`            |
+-----------------------------------------------------+--------------------------------------------------------+
| Look up a logic value or memory address             | :ref:`12 Logic and memory reference <ch-reference>`    |
+-----------------------------------------------------+--------------------------------------------------------+
| Run it on a server or alongside other mods          | :ref:`13 Multiplayer, saves and mods <ch-multiplayer>` |
+-----------------------------------------------------+--------------------------------------------------------+

This manual describes the rack as built by mod version 5.12.7. The User Manual, chapters 1 to 10, is for everyone who installs, operates and maintains a rack. The Developer Manual, chapters 11 to 13, is for those who program it, connect other devices to it, or run the server it lives on. The appendices collect the data, defaults and messages you will want to look up rather than read.

.. toctree::
   :caption: User Manual
   :maxdepth: 1

   About this manual <user/about>
   1 Product overview <user/overview>
   2 Safety <user/safety>
   3 Installation and commissioning <user/installation>
   4 Controls and indicators <user/controls>
   5 DS-8 OS <user/os/index>
   6 Storage and data handling <user/storage>
   7 Configuration <user/configuration>
   8 Maintenance <user/maintenance>
   9 Diagnostics and troubleshooting <user/diagnostics>
   10 FAQ <user/faq>

.. toctree::
   :caption: Developer Manual
   :maxdepth: 1

   11 Programming (IC10) <dev/programming>
   12 Logic and memory reference <dev/reference>
   13 Multiplayer, saves and mods <dev/multiplayer>

.. toctree::
   :caption: Appendices
   :maxdepth: 1

   Appendix A: Technical data <appendix/technical-data>
   Appendix B: Factory defaults <appendix/factory-defaults>
   Appendix C: Event messages <appendix/event-messages>
   Appendix D: Credits and revisions <appendix/credits>

.. toctree::
   :caption: Contributing to this manual
   :maxdepth: 1

   Building the Manual <contributing/building>
   Standards & Practices <contributing/standards>
   Workflow <contributing/workflow>

.. toctree::
   :maxdepth: 1

   Index <genindex>

Support
-------

Questions about the mod itself belong on its `Steam Workshop page <https://steamcommunity.com/sharedfiles/filedetails/?id=3819662919>`_, and :ref:`9 Diagnostics and troubleshooting <ch-diagnostics>` says what to include in a report. Corrections to this manual are welcome as `GitHub issues <https://github.com/feamsr00/ds8-server-rack-manual/issues>`_.
