DS-8 Server Rack: User and Developer Manual
===========================================
*Edition 11/2026, for mod version 5.12.7.*

.. image:: /images/icons.png
   :alt: The mod's own icons: the DS-8 Server Rack, a data drive and the rack key

The DS-8 Server Rack, a data drive and the rack key, from the mod's own icons.

Introduction
------------
The DS-8 Server Rack is a full-height cabinet that stores data, runs up to twelve IC10 programs, and automates a base without a line of code. It holds eight hot-swap data drives with 4,096 memory cells between them by default, twelve processor sockets, a system board and a backup battery, and you operate it from a front panel of 157 controls and a small operating system with thirteen programs.

This manual describes the rack as built by mod version 5.12.7. The User Manual, chapters 1 to 10, is for everyone who installs, operates and maintains a rack. The Developer Manual, chapters 11 to 13, is for those who program it, connect other devices to it, or run the server it lives on. The appendices collect the data, defaults and messages you will want to look up rather than read.

.. warning::

	**WARNING:** The rack can control airlocks, doors and the air in your rooms, and a mistake in a rule, a library task or a program can open a door to vacuum with someone standing behind it. Read :ref:`2 Safety <security_warning>` before you let the rack control anything that keeps you alive.

License
-------
This is an unofficial manual for the DS-8 Server Rack, a third-party mod by Iwan for the game Stationeers by RocketWerkz. It is not endorsed by the mod's author or by RocketWerkz. The DS-8, Stationeer Data Systems and everything else described here exist only inside the game; any resemblance to real server hardware is entirely deliberate.

The information reflects mod version 5.12.7 and may change with later versions. Where the Workshop page and the mod disagree, this manual follows the mod. No warranty, express or implied, is given for the contents of your banks.

The text of this manual is provided to you under the `MIT License <https://github.com/feamsr00/ds8-server-rack-manual/blob/main/LICENSE>`_, and all usage of it is determined and defined by the terms of this license. Please refer to the file above for the full license text. Screenshots and item icons show the mod and the game, and remain the property of their owners.

*Copyright (c) 2026 feamsr00. Any rights not expressly granted herein are reserved.*

User Manual
-----------
.. toctree::
   :maxdepth: 1
   :glob:

   user/about
   getting-started/*
   user/*

Developer Manual
----------------
.. toctree::
   :maxdepth: 1
   :glob:

   dev/*

.. _support:

Support
=======
The following communication channels are open:

* Questions about the mod itself: https://steamcommunity.com/sharedfiles/filedetails/?id=3819662919
* Corrections to this manual: https://github.com/feamsr00/ds8-server-rack-manual/issues

:ref:`9 Diagnostics and troubleshooting <ch-diagnostics>` says what to include in a report about the mod.

Indices and tables
==================
* :ref:`genindex`
* :ref:`search`
