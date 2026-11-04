.. _os-disks:

5.9 Disks (Disk Management)
===========================
Disks manages the eight drive bays, the drives in them, and the eight program slots on each drive. It is program 1 in the Data group; open it with **DSK**. How bays become memory banks is explained in :ref:`6 Storage and data handling <ch-storage>`.

5.9.1 Screen
------------

.. image:: /images/os-disks.png
   :alt: Disk Management listing bays 1 to 8, all empty, and a Selected disk panel saying bay 1 is empty

**Figure 5-6** All eight bays empty. The Selected disk panel always says what to do next.

The list has one row per bay, showing the drive's serial number, the bank it serves, its address range, the cells in use with a usage bar, and its status: Healthy, Offline, No cable or Stopped, or an empty bay. Below the list, the Selected disk panel shows the selected drive's serial number, its size, the cells used and free, and the bank port it is patched to.

5.9.2 Keys
----------
Use **UP** and **DN**, or **BAY-** and **BAY+**, to select a bay.

**Table 5-8** Disks keys

+-------------------+-----------------------------------+-----------------------------------------+
| Key               | Pad equivalent                    | What it does                            |
+===================+===================================+=========================================+
| **F1**            | **BAY**                           | Switches the bay online or offline      |
+-------------------+-----------------------------------+-----------------------------------------+
| **F2**            | **FMT**, or the **FORMAT** button | Formats the selected drive, after       |
|                   |                                   | asking first; only its cells are erased |
+-------------------+-----------------------------------+-----------------------------------------+
| **F3**            | **CPYD**                          | Copies everything on the drive to       |
|                   |                                   | another bay, overwriting the cells,     |
|                   |                                   | programs and backups there              |
+-------------------+-----------------------------------+-----------------------------------------+
| **F4**            | **OPEN**                          | Opens the bay's bank in Editor          |
+-------------------+-----------------------------------+-----------------------------------------+
| **F5** or **ENT** | —                                 | Opens the drive's program slots         |
+-------------------+-----------------------------------+-----------------------------------------+

5.9.3 Program slots
-------------------
Each drive holds eight IC10 programs, stored separately from its memory cells. The slot window lists each slot's program title (taken from the program's first comment line), its length, the processor it was saved from and the processor running it now.

**Table 5-9** Program slot keys

+-------------------+----------------------------------------------------+
| Key               | What it does                                       |
+===================+====================================================+
| **UP** / **DN**   | Select a slot                                      |
+-------------------+----------------------------------------------------+
| **<** / **>**     | Select the target processor                        |
+-------------------+----------------------------------------------------+
| **F1** or **PST** | Loads the slot's program into the target processor |
+-------------------+----------------------------------------------------+
| **F2** or **CPY** | Saves the target processor's program into the slot |
+-------------------+----------------------------------------------------+
| **F3**            | Clears the slot                                    |
+-------------------+----------------------------------------------------+
| **F4**            | Opens the bank in Editor                           |
+-------------------+----------------------------------------------------+
| **F5**            | Copies the whole drive to another bay              |
+-------------------+----------------------------------------------------+

The processor side of the same job is in :ref:`5.13 CPU <os-cpu>`, where you type a slot number and press **CPY** to save or **PST** to load.

5.9.4 Formatting a drive
------------------------

.. note::

	**NOTICE:** Formatting erases every memory cell on the drive. The drive's programs and backups are not touched. Check that you have selected the right bay before you confirm.

**Requirements:** The drive must be in a bay, and its bank must not be write-protected.

1. Select the bay with **UP** and **DN**.
2. Press **F2**.
3. Confirm when the rack asks.

**Result:** Every cell on the drive reads 0, and the event log records the format.

5.9.5 Copying a drive
---------------------

.. note::

	**NOTICE:** Copying overwrites everything on the target drive: its cells, its eight programs and both of its backups.

**Requirements:** There must be a drive in both the source and the target bay.

1. Select the source bay with **UP** and **DN**.
2. Press **F3**.
3. Choose the target bay and confirm when the rack asks.

**Result:** The target drive becomes an exact copy of the source, and the event log records how many programs went with it.

5.9.6 Loading a program into a processor
----------------------------------------
**Requirements:** The program must already be saved in one of the drive's slots, and the target processor's socket must hold a chip.

1. Select the bay with **UP** and **DN**, then press **F5** to open its program slots.
2. Select the slot with **UP** and **DN**.
3. Select the target processor with **<** and **>**.
4. Press **F1** and confirm when the rack asks.

**Result:** The program is written to the processor's chip, and the event log names the program, the drive and the slot it came from.
