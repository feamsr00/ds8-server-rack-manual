.. _ch-reference:

12 Logic and memory reference
=============================
This chapter is the reference for everything a program or a logic device can see of the rack: its logic values, its memory map, and the codes that appear in both. How to use them in a program is explained in :ref:`11 Programming (IC10) <ch-programming>`.

12.1 Interfaces
---------------
Other devices talk to the rack in two ways. Logic values are read and written with ``l`` and ``s``, or with logic readers and writers, exactly as for any other device. Memory is read and written with ``get`` and ``put``, and erased with ``clr``. The rack's own processors use both interfaces through ``db``; chips in other housings use them through a pin that points at the rack.

12.2 Logic values
-----------------
Table 12-1 lists the logic values the rack adds or redefines. The usual ``On``, ``Power``, ``PrefabHash`` and ``ReferenceId`` work as on any device. The number in the second column is the logic type's number, for use with logic readers.

**Table 12-1** Logic values

+-------------------+-----+-------------+-------------------------------+
| Logic type        | No. | Access      | Meaning                       |
+===================+=====+=============+===============================+
| ``Mode``          | 3   | Read, write | The program on the screen,    |
|                   |     |             | 0–12 (Table 12-3). Writes are |
|                   |     |             | rounded and limited to 0–12   |
+-------------------+-----+-------------+-------------------------------+
| ``Error``         | 4   | Read        | 1 while the rack is switched  |
|                   |     |             | on and overheated             |
+-------------------+-----+-------------+-------------------------------+
| ``Temperature``   | 6   | Read        | Core temperature in kelvin,   |
|                   |     |             | including the **CAL** offset  |
+-------------------+-----+-------------+-------------------------------+
| ``Lock``          | 10  | Read, write | Write protection: 1 on, 0     |
|                   |     |             | off. A write of 0.5 or more   |
|                   |     |             | switches it on                |
+-------------------+-----+-------------+-------------------------------+
| ``Charge``        | 11  | Read        | Energy in the UPS plus the    |
|                   |     |             | fitted battery cell, in       |
|                   |     |             | joules                        |
+-------------------+-----+-------------+-------------------------------+
| ``Setting``       | 12  | Read, write | The memory cell at the        |
|                   |     |             | cursor. Writing stores a      |
|                   |     |             | value there, subject to write |
|                   |     |             | protection                    |
+-------------------+-----+-------------+-------------------------------+
| ``Maximum``       | 23  | Read        | Cells online right now        |
+-------------------+-----+-------------+-------------------------------+
| ``Ratio``         | 24  | Read        | ``Quantity`` divided by       |
|                   |     |             | ``Maximum``; 0 when nothing   |
|                   |     |             | is online                     |
+-------------------+-----+-------------+-------------------------------+
| ``PowerActual``   | 26  | Read        | Draw while running, in watts; |
|                   |     |             | 0 when the rack is not        |
|                   |     |             | running                       |
+-------------------+-----+-------------+-------------------------------+
| ``Quantity``      | 27  | Read        | Cells in use, that is, cells  |
|                   |     |             | that are not zero             |
+-------------------+-----+-------------+-------------------------------+
| ``RequiredPower`` | 33  | Read        | Draw from mains while         |
|                   |     |             | switched on, including UPS    |
|                   |     |             | charging                      |
+-------------------+-----+-------------+-------------------------------+
| ``Idle``          | 37  | Read        | 1 when there is almost no     |
|                   |     |             | read or write traffic         |
+-------------------+-----+-------------+-------------------------------+
| ``ClearMemory``   | 62  | Write       | A write of 0.5 or more        |
|                   |     |             | formats every bank that is    |
|                   |     |             | not write-protected           |
+-------------------+-----+-------------+-------------------------------+
| ``LineNumber``    | 173 | Read, write | The line of the selected      |
|                   |     |             | processor; −1 if its socket   |
|                   |     |             | is empty. Writing sets the    |
|                   |     |             | line                          |
+-------------------+-----+-------------+-------------------------------+
| ``Index``         | 241 | Read, write | The cursor address. Writes    |
|                   |     |             | wrap around the data area, so |
|                   |     |             | they always land on a data    |
|                   |     |             | cell                          |
+-------------------+-----+-------------+-------------------------------+

Writes from outside the rack to ``Mode``, ``Lock``, ``Setting``, ``Index``, ``LineNumber`` and ``ClearMemory`` are refused while the **REM** switch is off or **MAINT** is on, and each refusal adds one to the fault counter. The rack's own processors may always write them. The selected processor is the one chosen with the **PROG** knob or in the CPU program.

.. note::

	**NOTICE:** A write of 1 to ``ClearMemory`` formats every bank that is not write-protected, at once. Only write protection prevents it once **REM** is on.

12.3 Memory map
---------------
With the default 512-cell drives, addresses 0 to 4095 hold data and the 88 cells from 4096 to 4183 report the rack's status. The status cells are read-only, apart from the eight scratch cells that programs may share.

.. image:: /images/fig-memory-map.png
   :alt: Data fills addresses 0 to 4095; 88 status cells follow from 4096

**Figure 12-1** The memory map with the default 512-cell drives: eight data banks, then seven groups of status cells

**Table 12-2** Memory map with the default drive size

+-----------+--------+-------------------------------+-----------------------------+
| Address   | Offset | Contents                      | Unit or values              |
+===========+========+===============================+=============================+
| 0–4095    | —      | Data banks 0–7, 512 cells     | Any number                  |
|           |        | each                          |                             |
+-----------+--------+-------------------------------+-----------------------------+
| 4096      | 0      | Core temperature              | °C                          |
+-----------+--------+-------------------------------+-----------------------------+
| 4097      | 1      | Power draw                    | W                           |
+-----------+--------+-------------------------------+-----------------------------+
| 4098      | 2      | UPS charge                    | 0–1                         |
+-----------+--------+-------------------------------+-----------------------------+
| 4099      | 3      | On battery                    | 1 while on battery          |
+-----------+--------+-------------------------------+-----------------------------+
| 4100      | 4      | Air filter condition          | 0–1                         |
+-----------+--------+-------------------------------+-----------------------------+
| 4101      | 5      | Fan mode                      | 0 Auto, 1 Low, 2 High, 3    |
|           |        |                               | Manual                      |
+-----------+--------+-------------------------------+-----------------------------+
| 4102      | 6      | I/O activity                  | 0–1                         |
+-----------+--------+-------------------------------+-----------------------------+
| 4103      | 7      | Uptime                        | s                           |
+-----------+--------+-------------------------------+-----------------------------+
| 4104      | 8      | Time of day                   | Minutes                     |
+-----------+--------+-------------------------------+-----------------------------+
| 4105      | 9      | Alarm active                  | 1 while the alarm is active |
+-----------+--------+-------------------------------+-----------------------------+
| 4106      | 10     | Drives being served           | Count                       |
+-----------+--------+-------------------------------+-----------------------------+
| 4107      | 11     | Cells in use                  | Count                       |
+-----------+--------+-------------------------------+-----------------------------+
| 4108      | 12     | Cells online                  | Count                       |
+-----------+--------+-------------------------------+-----------------------------+
| 4109      | 13     | Reads since the last reset    | Count                       |
+-----------+--------+-------------------------------+-----------------------------+
| 4110      | 14     | Writes since the last reset   | Count                       |
+-----------+--------+-------------------------------+-----------------------------+
| 4111      | 15     | Faults since the last reset   | Count                       |
+-----------+--------+-------------------------------+-----------------------------+
| 4112–4115 | 16–19  | Line number of processors 1–4 | −1 when there is no chip    |
+-----------+--------+-------------------------------+-----------------------------+
| 4116–4119 | 20–23  | State of processors 1–4       | Table 12-4                  |
+-----------+--------+-------------------------------+-----------------------------+
| 4120      | 24     | Running hours                 | h                           |
+-----------+--------+-------------------------------+-----------------------------+
| 4121      | 25     | Alarm temperature             | °C                          |
+-----------+--------+-------------------------------+-----------------------------+
| 4122      | 26     | Service hatch open            | 1 while open                |
+-----------+--------+-------------------------------+-----------------------------+
| 4123      | 27     | Write protection              | 1 while on                  |
+-----------+--------+-------------------------------+-----------------------------+
| 4124      | 28     | UPS battery health            | 0–1                         |
+-----------+--------+-------------------------------+-----------------------------+
| 4125      | 29     | Mains present                 | 1 while present             |
+-----------+--------+-------------------------------+-----------------------------+
| 4126      | 30     | Maintenance mode              | 1 while **MAINT** is on     |
+-----------+--------+-------------------------------+-----------------------------+
| 4127      | 31     | Caller                        | The number of the rack      |
|           |        |                               | processor reading the cell, |
|           |        |                               | 1–12; 0 from outside        |
+-----------+--------+-------------------------------+-----------------------------+
| 4128–4135 | 32–39  | Device IDs on I/O ports 1–8   | Reference ID, 0 when empty  |
+-----------+--------+-------------------------------+-----------------------------+
| 4136–4143 | 40–47  | Scratch cells                 | Any number; writable        |
+-----------+--------+-------------------------------+-----------------------------+
| 4144–4151 | 48–55  | Line number of processors     | −1 when there is no chip    |
|           |        | 5–12                          |                             |
+-----------+--------+-------------------------------+-----------------------------+
| 4152–4159 | 56–63  | State of processors 5–12      | Table 12-4                  |
+-----------+--------+-------------------------------+-----------------------------+
| 4160–4183 | 64–87  | Device IDs on I/O ports 9–32  | Reference ID, 0 when empty  |
+-----------+--------+-------------------------------+-----------------------------+

12.3.1 Rules of memory access
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The status cells read 0 while the rack is not running.
- Only the scratch cells can be written, and only while the rack is running and the BIOS setting **Scratch cells** is Read / write. A write to any other status cell is refused and counts as a fault.
- A read from a bank that no drive serves returns 0 and counts as a fault. A write to it, or to a protected bank, is dropped and counts as a fault.
- Addresses below 0 or above the last status cell stop the program with an error.
- ``clr`` on the rack formats every bank that is not write-protected, exactly like ``ClearMemory``.
- Chips in other housings can always ``put`` into the rack, subject to write protection. **MEM WR** restrains only the rack's own processors, and does not stop ``clr``.

12.4 Addresses with another drive size
--------------------------------------
The server setting ``DriveCapacity`` sets the number of cells per drive, and with it the whole map. Bank *n* covers addresses *n* × ``DriveCapacity`` to (*n* + 1) × ``DriveCapacity`` − 1, and each status cell sits at 8 × ``DriveCapacity`` plus the offset given in Table 12-2. With 1,024-cell drives, for example, the data area is 0 to 8191, the core temperature is at 8192, and the first scratch cell at 8232.

A program cannot read the drive size from the rack, so keep it in a ``define`` at the top of the program and derive every address from it. A change of drive size then means changing one line rather than hunting for every 4096 in the code. The setting itself is described in :ref:`7 Configuration <ch-configuration>`.

12.5 Program numbers
--------------------
``Mode`` reports and selects the program on the screen by number. The numbers do not follow the start menu, which groups the programs by purpose, so look them up rather than counting down the menu.

**Table 12-3** Program numbers

+-----+---------+-----+-----------+
| No. | Program | No. | Program   |
+=====+=========+=====+===========+
| 0   | System  | 7   | CPU       |
+-----+---------+-----+-----------+
| 1   | Disks   | 8   | Rules     |
+-----+---------+-----+-----------+
| 2   | Editor  | 9   | Scenes    |
+-----+---------+-----+-----------+
| 3   | Perf    | 10  | Library   |
+-----+---------+-----+-----------+
| 4   | Network | 11  | Jobs      |
+-----+---------+-----+-----------+
| 5   | Logger  | 12  | Dashboard |
+-----+---------+-----+-----------+
| 6   | Events  |     |           |
+-----+---------+-----+-----------+

The programs themselves are described in :ref:`5 DS-8 OS <ch-os>`.

12.6 Processor states
---------------------
The state cells for processors 1 to 4 (4116–4119) and 5 to 12 (4152–4159) hold one of six codes. The same states appear on the service display and in the CPU program under the short names given.

**Table 12-4** Processor states

+------+---------------+------------+------------------------------+
| Code | State         | Short name | Meaning                      |
+======+===============+============+==============================+
| 0    | No chip       | ``----``   | The socket is empty          |
+------+---------------+------------+------------------------------+
| 1    | Halted        | HALT       | Stopped by its **RUN**       |
|      |               |            | switch, **HALT ALL**, or     |
|      |               |            | **F1** in the CPU program    |
+------+---------------+------------+------------------------------+
| 2    | Running       | RUN        | Running normally             |
+------+---------------+------------+------------------------------+
| 3    | Error         | ERR        | Stopped by a runtime error   |
+------+---------------+------------+------------------------------+
| 4    | Compile error | CODE       | The program does not compile |
+------+---------------+------------+------------------------------+
| 5    | Single step   | STEP       | Paused in the debugger, or   |
|      |               |            | waiting for **STEP** while   |
|      |               |            | **DEBUG** is on              |
+------+---------------+------------+------------------------------+
