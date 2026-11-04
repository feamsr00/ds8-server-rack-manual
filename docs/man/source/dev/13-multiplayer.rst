.. _ch-multiplayer:

13 Multiplayer, saves and mods
==============================
This chapter is for whoever runs the server or keeps the saves: how the rack behaves in multiplayer, what a saved game keeps, the names the mod uses in save files and logs, how it protects itself against common installation mistakes, and how it gets on with other mods.

13.1 Multiplayer
----------------
Every player needs the mod. The host runs all of the rack's logic: storage, processors, automation and the heat model. Clients receive what the screen and the panel show, and send their clicks and key presses back to the host, so a rack behaves the same whoever is standing in front of it. Install the host's version of the mod on every client, so that both ends agree on what the rack is.

13.2 Saved games
----------------
The rack and its drives are saved with the world. Almost everything you can set is kept; the two exceptions are the event log and the performance graphs, which start empty after every load.

**Table 13-1** What a save keeps

+------------+------------------------------------------------------+
| Saved with | Contents                                             |
+============+======================================================+
| Each rack  | Every switch and knob position, the patch cables,    |
|            | the I/O ports, the scratch cells, the BIOS settings, |
|            | the logger channels, rules, scenes and library       |
|            | tasks, the counters, the core temperature, the UPS   |
|            | charge, filter condition and battery health, the OS  |
|            | version, and the debugger's breakpoints              |
+------------+------------------------------------------------------+
| Each drive | All of its cells, its eight program slots, the       |
|            | automation backup and the patch-field backup         |
+------------+------------------------------------------------------+
| Not saved  | The event log and the performance graphs             |
+------------+------------------------------------------------------+

Because the drive carries its own cells, programs and backups, a drive moved to another rack, or carried to another base, takes all of that with it. How to use this for backups is explained in :ref:`6 Storage and data handling <ch-storage>`.

**Table 13-2** Names in save files

+---------------------------+------------------------------+
| XML name                  | Used for                     |
+===========================+==============================+
| ``DS8ServerRackSaveData`` | Racks                        |
+---------------------------+------------------------------+
| ``ServerDriveSaveData``   | Data drives                  |
+---------------------------+------------------------------+
| ``ServerRackSaveData``    | Racks saved before mod 5.5.1 |
+---------------------------+------------------------------+

Racks saved before mod 5.5.1 still load, unless another installed mod also uses the old name ``ServerRackSaveData``; in that case the game cannot tell the two apart, and one of them has to go.

13.3 Safety nets in the mod
---------------------------
The mod guards against the installation mistakes that most often break a save. None of them needs anything from you except reading the game log when something does not load.

- **Installed twice.** If the mod is installed twice, for example once from the Workshop and once in the local mods folder, the second copy switches itself off and writes a warning to the game log, because two copies would stop saves from loading. Remove one of them anyway.
- **A save that will not load.** When a save fails to load because an XML name is used twice, the mod writes to the game log which name it is and which mod uses it. Save-recovery mods that recreate missing types are a known cause.
- **Updates.** The mod asks the Steam client whether its Workshop item has a newer version, and shows a notice on the rack's screen if it does. No other network access is known.

Every message the mod writes to the game log starts with ``[ServerRack]``, which makes it easy to find among everything else the game has to say.

The safety notices are collected in :ref:`2 Safety <security_warning>`.

13.4 Other mods
---------------
The rack is an ordinary device to the game, so most mods that work with devices work with it. Three are known to work together with it.

**Table 13-3** Compatible mods

+----------------+----------------------------------------------------+
| Mod            | Works with the rack as follows                     |
+================+====================================================+
| SDS FieldPad   | The tablet can mirror a rack's screen and click it |
|                | remotely                                           |
+----------------+----------------------------------------------------+
| StationeersLua | Lua chips run in the rack's sockets alongside IC10 |
|                | chips                                              |
+----------------+----------------------------------------------------+
| Data Centre    | The mod's Workshop page says the two work side by  |
|                | side                                               |
+----------------+----------------------------------------------------+

13.5 Update rates
-----------------
The rack does its work on fixed intervals, which matters when you reason about how quickly it reacts. A rule, for example, can never act faster than the half-second automation cycle, however short its delay.

**Table 13-4** Update rates

+----------------------------------------------------+--------------------------------------+
| What                                               | How often                            |
+====================================================+======================================+
| Rack state: power, heat, UPS, panel                | Four times a second                  |
+----------------------------------------------------+--------------------------------------+
| Automation: rules, scenes, library tasks and print | Every half second                    |
| jobs                                               |                                      |
+----------------------------------------------------+--------------------------------------+
| Rescan of the data network                         | Once a second                        |
+----------------------------------------------------+--------------------------------------+
| Processors                                         | Every game tick, like any IC housing |
+----------------------------------------------------+--------------------------------------+

If something in a multiplayer game or a save does not behave as described here, the symptoms and remedies are in :ref:`9 Diagnostics and troubleshooting <ch-diagnostics>`.
