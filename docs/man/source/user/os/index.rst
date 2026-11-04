.. _ch-os:

5 The DS-8 operating system
===========================

.. index::
   single: DS-8 OS

DS-8 OS is the rack's own small operating system. It runs on the monitor, boots in a few seconds, and offers thirteen programs in four groups. This chapter explains how to start the system, find your way around it and use the keys that work in every program; the programs themselves each have a section of their own, 5.6 to 5.18, on pages linked from :ref:`Table 5-1 <table-5-1>`. The key pad and its layout are shown in :ref:`4 Controls and indicators <ch-controls>`.

5.1 Start-up
------------

.. index::
   single: Start-up

When you switch the rack on, or when it restarts after a power loss, it shows a boot screen first. How long the boot screen stays depends on the BIOS self-test setting: 1.2 s for Quick, 4 s for Normal and 8 s for a full memory test. After that the rack opens its start program, which is System unless you choose another in the BIOS (see :ref:`7 Configuration <ch-configuration>`).

.. _figure-5-1:

.. figure:: /images/os-boot.png
   :alt: The DS-8 Server OS boot screen with a progress bar and the line Copyright (c) Stationeer Data Systems
   :width: 100%

   **Figure 5-1** The boot screen.

If the mod has been updated since the rack last ran, the rack shows an update screen instead and waits for you to install the new OS. Storage, processors and automation keep running in the meantime (see :ref:`8 Maintenance <ch-maintenance>`).

5.2 The start menu
------------------

.. index::
   single: Start menu

Press **HOME** in any program to open the start menu. It lists every program by group, together with the key that opens it, and shows a short status summary beside the list.

.. _figure-5-2:

.. figure:: /images/os-start-menu.png
   :alt: The start menu open over System: SYSTEM, DATA and LOGIC groups on the left with their pad keys, AUTO programs numbered 1 to 5 and a STATUS block on the right
   :width: 100%

   **Figure 5-2** The start menu. Each program shows the key that opens it: a blue pad key for the first eight, and a digit for the five automation programs.

- **UP** and **DN** move the selection, **<** and **>** switch between the two columns, **ENT** opens the selected program and **ESC** closes the menu. Pressing **HOME** a second time opens System.
- The digits 1–5 open the automation programs directly: 1 for Dashboard, 2 for Rules, 3 for Scenes, 4 for Library and 5 for Jobs.
- Under the automation column, the STATUS block shows the core temperature, the power source, how many processors are running, and whether anything is in alarm.

5.3 The programs
----------------

.. index::
   single: Programs

The thirteen programs are grouped by what they deal with. The blue keys on the key pad open the first eight from anywhere; the five automation programs open from the start menu.

.. _table-5-1:

.. table:: **Table 5-1** Programs

   +-----+--------------------------------------+------------+---------------------+-------------------------+
   | No. | Program                              | Group      | Open with           | What it is for          |
   +=====+======================================+============+=====================+=========================+
   | 0   | :ref:`5.6 System <os-system>`        | System     | **SYS**             | An overview of the      |
   |     |                                      |            |                     | whole server            |
   +-----+--------------------------------------+------------+---------------------+-------------------------+
   | 3   | :ref:`5.7 Perf <os-perf>`            | System     | **PRF**             | Temperature, power and  |
   |     |                                      |            |                     | I/O graphs              |
   +-----+--------------------------------------+------------+---------------------+-------------------------+
   | 6   | :ref:`5.8 Events <os-events>`        | System     | **EVT**             | The event log, newest   |
   |     |                                      |            |                     | first                   |
   +-----+--------------------------------------+------------+---------------------+-------------------------+
   | 1   | :ref:`5.9 Disks <os-disks>`          | Data       | **DSK**             | The eight bays, their   |
   |     |                                      |            |                     | drives and their        |
   |     |                                      |            |                     | program slots           |
   +-----+--------------------------------------+------------+---------------------+-------------------------+
   | 2   | :ref:`5.10 Editor <os-editor>`       | Data       | **EDT**, **GOTO**,  | Reading and writing     |
   |     |                                      |            | **FIND**, **FILL**, | memory cells            |
   |     |                                      |            | **BM1**–**BM4**     |                         |
   +-----+--------------------------------------+------------+---------------------+-------------------------+
   | 5   | :ref:`5.11 Logger <os-logger>`       | Data       | **LOG**             | Recording a device      |
   |     |                                      |            |                     | value into a bank       |
   +-----+--------------------------------------+------------+---------------------+-------------------------+
   | 4   | :ref:`5.12 Network <os-network>`     | Logic      | **NET**             | Devices on the data     |
   |     |                                      |            |                     | network, pins and I/O   |
   |     |                                      |            |                     | ports                   |
   +-----+--------------------------------------+------------+---------------------+-------------------------+
   | 7   | :ref:`5.13 CPU <os-cpu>`             | Logic      | **CPU**             | The twelve processors:  |
   |     |                                      |            |                     | overview, debugger,     |
   |     |                                      |            |                     | editor and code check   |
   +-----+--------------------------------------+------------+---------------------+-------------------------+
   | 12  | :ref:`5.14 Dashboard <os-dashboard>` | Automation | **HOME**, then 1    | Every device at a       |
   |     |                                      |            |                     | glance, and anything in |
   |     |                                      |            |                     | alarm                   |
   +-----+--------------------------------------+------------+---------------------+-------------------------+
   | 8   | :ref:`5.15 Rules <os-rules>`         | Automation | **HOME**, then 2    | IF a value THEN set a   |
   |     |                                      |            |                     | device                  |
   +-----+--------------------------------------+------------+---------------------+-------------------------+
   | 9   | :ref:`5.16 Scenes <os-scenes>`       | Automation | **HOME**, then 3    | Stored settings of      |
   |     |                                      |            |                     | every device            |
   +-----+--------------------------------------+------------+---------------------+-------------------------+
   | 10  | :ref:`5.17 Library <os-library>`     | Automation | **HOME**, then 4    | Sixteen ready-made      |
   |     |                                      |            |                     | control programs (beta) |
   +-----+--------------------------------------+------------+---------------------+-------------------------+
   | 11  | :ref:`5.18 Jobs <os-jobs>`           | Automation | **HOME**, then 5    | Print queues for        |
   |     |                                      |            |                     | printers on the network |
   +-----+--------------------------------------+------------+---------------------+-------------------------+

The **<<** and **>>** keys step through the programs in the order of this table. The program number is reported by the rack as its ``Mode`` logic value, and writing ``Mode`` from IC10 switches the screen to that program (see :ref:`12 Logic and memory reference <ch-reference>`).

The automation programs only set things up; the work itself runs in the background. Rules, scenes, library tasks and print jobs are processed inside the rack every half second while it is online, whichever program is on the screen. They need no chips and no drives, but they stop when the rack overheats, loses power or enters setup, and they reach only devices on the rack's data network. After a power-up, or when mains returns, the rack waits 3 s, re-applies every rule once, and checks them all again 8 s later. A start-up scene, if one is set, is recalled 3 s after the start.

5.4 Reading a program screen
----------------------------

.. index::
   single: Reading a program screen

Every program window shares the same frame, which makes a new program easy to find your way around. The pictures on each program's page show it in place.

- **Title bar:** This shows the program's name, its group, and its place within the group, such as DATA 2/3.
- **Hint line:** Along the bottom, this lists the main keys for the screen. At its right edge are three counters: CPU (processors running out of chips fitted), NET (devices on the data network) and DRV (drives online out of drives inserted).
- **Soft key labels:** These show what **F1**–**F5** do in this program. A blank label means the key is unused here.
- **Taskbar:** Along the very bottom are **Home**, the programs of the current group (click one to switch to it), the core temperature and the clock.
- **SHIFT:** Where an on-screen hint says SHIFT, it means the quantity modifier key that this manual simply calls the modifier.

5.5 Keys that work everywhere
-----------------------------

.. index::
   single: Keys that work everywhere

A number of keys behave the same way in every program. Learning them once pays off thirteen times.

- **Numbers:** The digits, **.**, **+/-**, **EXP**, **DEL** and **CLR** build a number in the entry line. **ENT** confirms it and **ESC** cancels it.
- **Moving:** **UP**, **DN**, **<**, **>**, **PG+** and **PG-** move the selection or cursor, and **TAB** moves to the next field or tab.
- **Copy and paste:** **CPY** and **PST** copy and paste a value.
- **INC and DEC:** In System, Disks, Editor, Perf, Network, Logger and Events, these change the memory cell at the editor cursor by 1, or by 10 with the modifier. In CPU and the automation programs they change the selected field instead.
- **HELP:** This shows the current program's key list until you close it.

Several pad keys act directly, whichever program happens to be on the screen.

.. index::
   single: BAY-
   single: BAY+
   single: BAY
   single: FMT
   single: CPYD
   single: OPEN
   single: BNK-
   single: BNK+
   single: GOTO
   single: FIND
   single: FILL
   single: ZERO
   single: BM1
   single: BM4
   single: REC1
   single: REC4
   single: RSIO
   single: CLEV
   single: SLP

.. _table-5-2:

.. table:: **Table 5-2** Pad keys that act from any program

   +------------------------------+-----------------------------------------------------+
   | Keys                         | What they do                                        |
   +==============================+=====================================================+
   | **BAY-** / **BAY+**          | Select the previous or next bay                     |
   +------------------------------+-----------------------------------------------------+
   | **BAY**                      | Switches the selected bay online or offline         |
   +------------------------------+-----------------------------------------------------+
   | **FMT**                      | Formats the drive in the selected bay, after asking |
   |                              | first                                               |
   +------------------------------+-----------------------------------------------------+
   | **CPYD**                     | Copies the selected bay's drive to another bay      |
   +------------------------------+-----------------------------------------------------+
   | **OPEN**                     | Opens the selected bay's bank in Editor             |
   +------------------------------+-----------------------------------------------------+
   | **BNK-** / **BNK+**          | Move the editor cursor back or forward by one bank  |
   +------------------------------+-----------------------------------------------------+
   | **GOTO**, **FIND**, **FILL** | Open Editor on that function                        |
   +------------------------------+-----------------------------------------------------+
   | **ZERO**                     | Zeroes the cell at the editor cursor                |
   +------------------------------+-----------------------------------------------------+
   | **BM1**–**BM4**              | Jump to a bookmarked address in Editor; hold the    |
   |                              | modifier to store the cursor in that bookmark       |
   |                              | instead                                             |
   +------------------------------+-----------------------------------------------------+
   | **REC1**–**REC4**            | Start or stop logger channels 1–4                   |
   +------------------------------+-----------------------------------------------------+
   | **RSIO**                     | Resets the read, write and fault counters           |
   +------------------------------+-----------------------------------------------------+
   | **CLEV**                     | Clears the event log                                |
   +------------------------------+-----------------------------------------------------+
   | **SLP**                      | Starts the screen saver                             |
   +------------------------------+-----------------------------------------------------+

The guarded **FORMAT** button on the control row behaves a little differently from **FMT**. In Disks it formats the selected drive, and from any other program it formats the drive that serves the bank under the editor cursor. Either way, it always asks before erasing anything.

.. toctree::
   :hidden:

   5.6 System <system>
   5.7 Perf <perf>
   5.8 Events <events>
   5.9 Disks <disks>
   5.10 Editor <editor>
   5.11 Logger <logger>
   5.12 Network <network>
   5.13 CPU <cpu>
   5.14 Dashboard <dashboard>
   5.15 Rules <rules>
   5.16 Scenes <scenes>
   5.17 Library <library>
   5.18 Jobs <jobs>
