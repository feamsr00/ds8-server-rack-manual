.. _os-events:

5.8 Events (Event Viewer)
=========================
Events is the rack's event log, newest entry first. It is program 6 in the System group; open it with **EVT**. When something misbehaves, start here: most problems name themselves in the log, often with the time they started.

5.8.1 Screen
------------

.. image:: /images/os-events.png
   :alt: Event Viewer showing five entries: settings reset to factory defaults, monitor swung out, setup utility started, monitor pushed back in, setup saved

**Figure 5-5** The log after a factory reset and a visit to the BIOS, newest at the top.

Each entry has a type (Information, Warning or Error), the time it happened and a short description. The header shows the filter in use and which entries are on the screen, such as "1–5 of 5". The log keeps the 40 newest entries and is not saved with the game, so it always starts empty after loading.

Typical entries record the monitor being swung out or pushed back in, the setup utility starting and saving, settings being reset to factory defaults, drives being inserted or removed, a bay going on or offline, a cable being re-patched, a processor error with its line, an overheat and its recovery, the filter asking to be cleaned, an alarm from a rule or library task, and a print job stopped because someone changed the printer by hand. The rack also logs the occasional remark of its own: a greeting when it starts, and a comment every five hours of uptime, such as "All systems nominal. Suspiciously nominal." Every message is listed, with its meaning and what to do about it, in :ref:`C Event messages <app-c>`.

5.8.2 Keys
----------
**Table 5-7** Events keys

+-------------------+------------------------------------------------------+
| Key               | What it does                                         |
+===================+======================================================+
| **UP** / **DN**   | Scroll by one entry                                  |
+-------------------+------------------------------------------------------+
| **PG+** / **PG-** | Scroll by one page                                   |
+-------------------+------------------------------------------------------+
| **F1**            | Clears the log; **CLEV** on the pad and **F3** in    |
|                   | System do the same                                   |
+-------------------+------------------------------------------------------+
| **F2**            | Changes the filter: all events, warnings and errors, |
|                   | or errors only                                       |
+-------------------+------------------------------------------------------+
