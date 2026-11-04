.. _ch-api:

Using the API
=============

.. index::
   single: Using the API

To use the rack from a program, some requirements must be followed. This page is the short version: every logic value and memory address is listed in :ref:`12 Logic and memory reference <ch-reference>`, and how to program the rack is explained in :ref:`11 Programming (IC10) <ch-programming>`.

DS-8 Requirements
-----------------

- A chip in another housing needs a pin that points at the rack. A processor inside the rack uses ``db`` instead.
- Logic writes from outside the rack need the **REM** switch on and **MAINT** off.
- Memory writes from the rack's own processors need **MEM WR** on.
- A memory bank answers only while a drive serves it, and takes writes only while it is not write-protected.

Getting Data
------------

With the rack on pin d0 of a chip elsewhere:

.. code-block:: text

	alias rack d0
	get r0 rack 4096      # core temperature in C
	get r1 rack 4098      # UPS charge 0-1
	l r2 rack Error       # 1 = overheated

Putting Data
------------

.. code-block:: text

	alias rack d0
	put rack 100 r0       # keep a copy in cell 100
	s rack Index 100      # cursor to cell 100
	s rack Setting 42     # write 42 there

.. admonition:: NOTICE
   :class: note

   A single ``clr`` on the rack formats every bank that is not write-protected, all at once. Keep it out of any program that addresses the rack.

Other mods
----------

Other mods that work with the rack are listed in :ref:`13 Multiplayer, saves and mods <ch-multiplayer>`.
