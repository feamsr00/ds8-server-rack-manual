.. _os-system:

5.6 System (DS-8 Server Manager)
================================
System is the rack's front page: a single screen that answers the question "is this server all right?" It is program 0 in the System group, and it is the program the rack opens after power-up unless the BIOS says otherwise. Open it with **SYS**, or by pressing **HOME** twice.

5.6.1 Screen
------------

.. image:: /images/os-system.png
   :alt: DS-8 Server Manager: Server, Health and Storage panels on a rack running on mains with five processors and no drives

**Figure 5-3** A rack online on mains, drawing 116 W, with five processors running and all eight bays empty.

**Table 5-3** System screen

+------------+------------------------------------------------------+
| Panel      | What it shows                                        |
+============+======================================================+
| Server     | The state (Online, No power or Overheated), the up   |
|            | time, the power source (mains or UPS battery),       |
|            | whether the power and data cables are connected,     |
|            | write protection, and whether the front panel is     |
|            | locked                                               |
+------------+------------------------------------------------------+
| Health     | The fan mode, core temperature, power draw, I/O load |
|            | and UPS charge. The fan reads STOPPED in red while   |
|            | the air filter is pulled                             |
+------------+------------------------------------------------------+
| Processors | "no chips", how many of the fitted chips are         |
|            | running, or how many are in error                    |
+------------+------------------------------------------------------+
| Storage    | The drives online and inserted, the cells in use out |
|            | of the cells online, and one tile per bay showing    |
|            | the bank it serves, "no cable" or "empty"            |
+------------+------------------------------------------------------+

5.6.2 Keys
----------
**Table 5-4** System keys

+----------+-----------------------------------------------------+
| Key      | What it does                                        |
+==========+=====================================================+
| **F1**   | About: shows the OS version and the size of the     |
|          | address space                                       |
+----------+-----------------------------------------------------+
| **F2**   | Resets the read, write and fault counters; **RSIO** |
|          | on the pad does the same                            |
+----------+-----------------------------------------------------+
| **F3**   | Clears the event log; **CLEV** on the pad does the  |
|          | same                                                |
+----------+-----------------------------------------------------+
| **HOME** | Opens the start menu                                |
+----------+-----------------------------------------------------+

The history behind these numbers is in :ref:`5.7 Perf <os-perf>` and :ref:`5.8 Events <os-events>`.
