.. _ch-storage:

6 Storage and data handling
===========================

.. index::
   single: Storage and data handling

The rack's memory lives on its data drives, but programs never see drives directly. They see eight memory banks, and the patch field decides which drive serves which bank. This chapter explains how that works, when a bank answers and when it does not, and how to protect and back up what you store. The programs that work on storage are :ref:`5.9 Disks <os-disks>`, :ref:`5.10 Editor <os-editor>` and :ref:`5.11 Logger <os-logger>`.

6.1 Memory organisation
-----------------------

.. index::
   single: Memory organisation
   single: Banks
   single: Memory

With the default 512-cell drives, the rack's memory is eight banks of 512 cells: 4,096 numbers at addresses 0–4095. Bank *n* covers addresses *n* × 512 to *n* × 512 + 511, so bank 0 holds 0–511 and bank 7 holds 3584–4095. Each bank is served by whichever drive its patch cable connects to. Immediately after the data come 88 status cells, at addresses 4096–4183, which report on the rack itself; they are listed in :ref:`12 Logic and memory reference <ch-reference>`.

.. admonition:: NOTICE
   :class: note

   The server setting ``DriveCapacity`` changes the size of every bank, and with it every address above bank 0, including where the status cells begin. Drives already in use keep their old size. Choose the drive size before you build the first rack, and leave it alone afterwards.

.. _sec-6-2:

6.2 When a bank answers
-----------------------

.. index::
   single: When a bank answers

A bank reads and writes only while all five of these conditions hold:

1. The system is running: it has power and a system board, and is neither overheated nor in setup.
2. The bay's bus is on: **BUS A** for bays 1–4, **BUS B** for bays 5–8.
3. The bay itself is online, as set by its power button or by **F1** in Disks.
4. A patch cable connects the bay to the bank.
5. A drive sits in the bay.

If any of them fails, a read from the bank returns 0, a write is quietly dropped, and the rack's fault counter goes up by one. Writes also need write protection to be off (see :ref:`6.5 <sec-6-5>`). When a program keeps reading zeros, this list is the first place to look.

6.3 Data drives
---------------

.. index::
   single: Data drives

.. _table-6-1:

.. table:: **Table 6-1** Data drives

   +----------------+------------------------------------------------------+
   | Property       | Details                                              |
   +================+======================================================+
   | Capacity       | 512 cells, fixed when the drive is first used. The   |
   |                | server setting ``DriveCapacity`` (64–4096) changes   |
   |                | it for new drives                                    |
   +----------------+------------------------------------------------------+
   | Programs       | Eight program slots, separate from the cells. A      |
   |                | slot's title is the first comment line of its        |
   |                | program                                              |
   +----------------+------------------------------------------------------+
   | Backups        | One automation backup (rules, scenes and library     |
   |                | tasks) and one patch-field backup                    |
   +----------------+------------------------------------------------------+
   | Hot swap       | A drive can be pulled from a running rack. Its data  |
   |                | goes with it, into a locker, through a save or into  |
   |                | another rack, and the event log notes each insertion |
   |                | and removal                                          |
   +----------------+------------------------------------------------------+
   | Identification | Pointing at a drive shows its serial number (#00000, |
   |                | derived from its reference ID), the cells in use,    |
   |                | its programs and its backups                         |
   +----------------+------------------------------------------------------+

The rack counts a cell as in use when it is not zero, which is worth remembering when a drive full of zeros reports itself as empty.

6.4 The patch field
-------------------

.. index::
   single: Patch field

The patch field across the top of the cabinet decides which drive serves which bank, and which I/O port each processor pin reaches. It has two rows of sockets and fourteen cables.

.. _figure-6-1:

.. figure:: /images/patch-field.png
   :alt: The patch field: eight write-protect switches over bank ports 0 to 7 on the left, processor I/O ports 1 to 8 on the right, and coloured cables running down to bay sockets 1 to 8 and pin sockets d0 to d5
   :width: 100%

   **Figure 6-1** The patch field as it comes from the factory: bay 1 on bank 0 through bay 8 on bank 7 (left), and pins d0–d5 on I/O ports 1–6 (right). Ports 7 and 8 start without a pin. The lit lamps over ports 4 and 5 show devices there.

- **Upper row, left:** bank ports 0–7, each with its write-protect switch above it.
- **Upper row, right:** processor I/O ports 1–8.
- **Lower row, left:** one cable from each drive bay, 1–8.
- **Lower row, right:** one cable from each processor pin, d0–d5.

Moving a cable follows a simple rule. Clicking it moves it to the next free port to its right; when no port to the right is free, the cable comes out. Clicking a cable that is out plugs it into the first free port from the left. Holding the modifier while clicking pulls a cable straight out. A bay without a cable serves no bank, and a pin without a cable reaches no device.

Swapping two bays' cables swaps which bank each drive answers on, without moving any data at all. Pin cables are usually easier to manage from :ref:`5.12 Network <os-network>`, where selecting a device and pressing 0–5 plugs everything in for you. With the **PLCK** DIP switch on, the **LOCK** key switch locks the cables as well as the panel.

6.4.1 Swapping two bays
^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: Swapping two bays

This example swaps bays 1 and 2, so that the drive in bay 2 serves bank 0 and the drive in bay 1 serves bank 1.

**Requirements:** The panel must be unlocked, or the **PLCK** DIP switch must be off.

1. Hold the modifier and click bay 1's cable to pull it.
2. Hold the modifier and click bay 2's cable to pull it.
3. Click bay 2's cable. It goes into the first free port, bank 0.
4. Click bay 1's cable. It goes into the next free port, bank 1.

**Result:** The banks have swapped drives, and the event log records each move.

.. _sec-6-5:

6.5 Write protection
--------------------

.. index::
   single: Write protection

Write protection works at three levels, and a write succeeds only when none of them objects.

- **The WP toggle** on the control row protects every bank at once. It is also the ``Lock`` logic value.
- **The bank switches** on the patch field protect one bank each.
- **The BIOS setting "Write protect at boot"** switches protection on every time the rack starts (see :ref:`7 Configuration <ch-configuration>`).

Separately, the **MEM WR** switch decides whether the rack's own processors may write to its drives at all. It does not affect chips in other housings, which are held back only by write protection.

.. admonition:: NOTICE
   :class: note

   A single ``clr`` from a program that points a pin at the rack, a ``clrd`` with the rack's ID, or a write of 1 to ``ClearMemory``, formats every bank that is not write-protected, all at once. Protect the banks you care about. See also :ref:`2 Safety <ch-safety>`.

.. _sec-6-6:

6.6 Backups
-----------

.. index::
   single: Backups

Besides its cells and programs, each drive can hold two backups.

.. _table-6-2:

.. table:: **Table 6-2** Backups on a drive

   +-------------+----------------------------------------+----------------------------------------+
   | Backup      | What it holds                          | Made from                              |
   +=============+========================================+========================================+
   | Automation  | Every rule, scene and library task     | **F5** in :ref:`5.15 Rules <os-rules>` |
   +-------------+----------------------------------------+----------------------------------------+
   | Patch field | The pin patches, the I/O ports and the | **F5** in                              |
   |             | logger devices                         | :ref:`5.12 Network <os-network>`       |
   +-------------+----------------------------------------+----------------------------------------+

To copy a whole drive, programs and backups included, use **F3** in Disks.

6.6.1 Backing up the automation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: Backing up the automation

**Requirements:** A drive must be in the selected bay (use **BAY-** and **BAY+** to choose).

1. Open Rules.
2. Press **F5**.

**Result:** All rules, scenes and library tasks are saved to the drive, and the event log names the drive's serial number. To load them back, select the bay holding the drive, open Rules, and press **F5** while holding the modifier.

6.6.2 Backing up the patch field
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: Backing up the patch field

**Requirements:** A drive must be in the selected bay.

1. Open Network.
2. Press **F5**.

**Result:** The pin patches, I/O ports and logger devices are saved to the drive. Holding the modifier while pressing **F5** loads them back, keeping only the devices that are still on the network.
