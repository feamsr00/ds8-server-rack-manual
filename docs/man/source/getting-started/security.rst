.. _security_warning:

2 An Admonishment Regarding Safety
==================================
The rack keeps a base's memory and, before long, a fair share of its life support. Most of what can go wrong with it is quiet: a format nobody meant, a door that opens at the wrong moment, a cabinet slowly cooking itself in vacuum. This chapter gathers those risks in one place. The same notices appear again throughout the manual, right beside the steps they concern, so you will meet them where they matter as well as here.

2.1 Safety notices in this manual
---------------------------------
Every notice in this manual opens with a signal word that tells you how bad things get if you ignore it. The notice then names the hazard, explains what happens, and says how to avoid it.

**Table 2-1** Signal words

+-------------+-----------------------------------------------------+
| Signal word | What ignoring it can do                             |
+=============+=====================================================+
| **WARNING** | Injure or kill your character, for example by       |
|             | opening an airlock to vacuum                        |
+-------------+-----------------------------------------------------+
| **CAUTION** | Damage, overheat or shut down equipment, along with |
|             | whatever that equipment was keeping alive           |
+-------------+-----------------------------------------------------+
| **NOTICE**  | Lose data, programs or settings                     |
+-------------+-----------------------------------------------------+

A notice looks like this:

.. note::

	**NOTICE:** Example notice. The first sentence names the hazard and the consequence; the rest says what to do about it.

2.2 Operational risks
---------------------

2.2.1 Airlocks that give up
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::

	**WARNING:** When the library's advanced airlock reaches its time limit, it opens the far door anyway, at whatever pressure the airlock has reached, and only then logs a warning. Set the limit generously, make sure the vent can actually reach its target pressure, and test the cycle with nobody standing inside.

The time limit exists so that a stuck airlock does not trap anyone forever, which is a fair trade until the vent is too small for the room. The airlock program and its settings are described in :ref:`5.17 Library <os-library>`.

2.2.2 Data loss
^^^^^^^^^^^^^^^

.. note::

	**NOTICE:** A single ``clr`` from a program that points a pin at the rack, or a write of 1 to the ``ClearMemory`` logic value, formats every bank that is not write-protected, all at once. Switch on write protection for the banks you care about, and keep ``clr`` out of any program that addresses the rack.

The guarded **FORMAT** button and the Disks program's format and copy functions always ask before they act, but they still do exactly what they say: a copy overwrites every cell, program and backup on the target drive. Pulling a drive from a running rack is safe for the data, which simply leaves with the drive, but any bank that drive served answers 0 from then on. Write protection and backups are covered in :ref:`6 Storage and data handling <ch-storage>`.

2.2.3 Changing the drive size
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

	**NOTICE:** Changing the server setting ``DriveCapacity`` moves every memory address at once, because it changes both the bank size and where the status cells begin. Drives already in use keep their old size. Decide on the drive size before you build the first rack, and leave it alone afterwards.

2.2.4 Overheating
^^^^^^^^^^^^^^^^^

.. attention::

	**CAUTION:** The rack cools itself with room air. In vacuum, a rack drawing 355 W reaches its trip temperature in about nine minutes; with its air filter pulled the fans stop altogether, and a clogged filter roughly halves the cooling. When the core trips, storage goes offline and every processor and automation task stops. Install the rack in a pressurised room, keep the filter clean, and refit a pulled filter within a few minutes.

If the rack runs anything important, such as an airlock or a room's climate, an overheat is an outage of that system too. Cooling is explained in :ref:`3 Installation and commissioning <ch-installation>`.

2.2.5 Power loss
^^^^^^^^^^^^^^^^

.. attention::

	**CAUTION:** The built-in UPS carries a fully loaded rack for only about two minutes. With **BYPASS** on, or while the battery is being reconditioned, there is no backup at all, and a rack set to "Stay off" after a power loss waits for someone to press **RESET**. Fit a battery cell if the rack runs anything that cannot stop for more than two minutes.

2.2.6 Automation that reaches everything
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

	**CAUTION:** Rules set to "Set all alike", scene recalls and IC10 batch instructions act on every matching device on the rack's data network, including devices in rooms you may not be thinking about. Check what a scene holds before you recall it, and test new rules on a quiet afternoon.

2.2.7 Remote control
^^^^^^^^^^^^^^^^^^^^

.. note::

	**NOTICE:** While the **REM** switch is on and **MAINT** is off, any chip outside the rack can write the rack's ``Mode``, ``Lock``, ``Setting``, ``Index``, ``LineNumber`` and ``ClearMemory`` logic values. Between them, these change the screen, switch write protection off, move the cursor and write the cell under it, set the selected processor's line, and format every unprotected bank. **REM** does not guard the memory itself, however: ``put``, ``putd`` and ``clr`` from any chip that can address the rack work whatever the switch says, and only write protection stops them. Switch **REM** off unless something outside the rack genuinely needs to control it, and write-protect the banks you care about.

The logic values involved are listed in :ref:`12 Logic and memory reference <ch-reference>`.

2.2.8 Maintenance mode
^^^^^^^^^^^^^^^^^^^^^^

.. attention::

	**CAUTION:** **MAINT** in the service bay suppresses every alarm and blocks remote control. That is exactly what you want while servicing the rack, and exactly what you do not want a week later when it is overheating in silence. Switch it off when you close the hatch.

2.2.9 Factory reset
^^^^^^^^^^^^^^^^^^^

.. note::

	**NOTICE:** Pressing **RESET** in the service bay twice within four seconds returns every setting to its factory default. Drives, programs and automation are kept, but your switch positions, BIOS settings and patching are not. Note down anything you changed before you press it.

2.2.10 The mod installed twice
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

	**NOTICE:** Two copies of the mod, for example one from the Workshop and one in the local mods folder, stop saves from loading. The mod detects this, switches the second copy off and writes a warning to the game log, but you should still remove one copy. See :ref:`13 Multiplayer, saves and mods <ch-multiplayer>`.

2.3 Mitigation
--------------
The rack has no access control beyond a key switch and a couple of toggles, so most of its safety is in how you set it up. These recommendations hold for every installation.

**Universal recommendations**

- Write-protect the banks you care about, and back up the automation and the patch field to a drive after every significant change.
- Keep **REM** off unless something outside the rack needs to control it, and keep ``clr`` out of any program that points a pin at the rack.
- Keep the rack in a pressurised room with a clean filter and its fans on Auto.
- Fit a battery cell if the rack runs anything you cannot afford to lose for more than two minutes.
- Read the event log after anything unexpected; it usually names the cause, and occasionally offers a joke for your trouble.
- Test airlocks, rules and scenes with nobody standing where the consequences would land.

Maintenance procedures are in :ref:`8 Maintenance <ch-maintenance>`, and the settings that change the rack's behaviour are in :ref:`7 Configuration <ch-configuration>`.

**Keep your banks protected and your filter clean.**
