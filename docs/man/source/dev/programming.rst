.. _ch-programming:

11 Programming the rack (IC10)
==============================

.. index::
   single: Programming the rack (IC10)

This chapter begins the developer part of the manual. It explains how the rack's twelve processors are arranged, how a program reaches devices and the rack's own memory, which switches restrain it, and how to load, debug and store programs. It assumes you can already write IC10 for an ordinary IC housing; the rack changes where things are, not how the language works. Every logic value and memory address the examples use is listed in :ref:`12 Logic and memory reference <ch-reference>`.

11.1 Processor architecture
---------------------------

.. index::
   single: Processor architecture

To IC10, the rack is an IC housing with twelve sockets instead of one. Each socket takes an ordinary IC10 chip, and each chip runs its own program on its own registers, but all twelve share the same six pins, d0 to d5, and all twelve see the rack itself as ``db``. A program inside the rack therefore reads and writes the rack's memory with ``get db`` and ``put db``, and reads the rack's logic values with ``l db``, just as a program in an ordinary housing would address its own housing.

.. _table-11-1:

.. table:: **Table 11-1** Processors

   +------------+------------------------------+----------------------------+----------------------------+
   | Processors | Sockets                      | Started and stopped with   | Reset with                 |
   +============+==============================+============================+============================+
   | 1–4        | Front, in the processor unit | The **RUN** toggles on the | The **RST** buttons on the |
   |            | under the monitor            | panel                      | panel                      |
   +------------+------------------------------+----------------------------+----------------------------+
   | 5–12       | Rear, in the expansion       | **F1** in the CPU program  | **F2** in the CPU program  |
   |            | chassis                      |                            |                            |
   +------------+------------------------------+----------------------------+----------------------------+

.. _figure-11-1:

.. figure:: /images/expansion-chassis.png
   :alt: The rear expansion chassis labelled IC10 processors 5 to 12, run and error, with eight empty sockets numbered 5 to 12 and two lamps above each
   :width: 100%

   **Figure 11-1** The expansion chassis at the back of the cabinet holds processors 5 to 12. The two lamps above each socket are RUN and ERR.

Each processor runs a number of lines every game tick set by the **CLOCK** knob: 32, 64, 128 or 256 for LO, MED, HI and MAX, starting on HI. **TURBO** doubles that, and the BIOS setting **CPU clock multiplier** scales it again by 0.5, 1 or 2. Speed is not free, though: each running processor draws 4 W for every 64 lines per tick, so 8 W on the default HI clock, and the heat goes into the core along with everything else.

11.2 Pins and I/O ports
-----------------------

.. index::
   single: Pins and I/O ports

The rack has 32 I/O ports, each of which holds the ID of one device on the rack's data network. The six pins do not point at devices directly; they point at ports, through the six pin cables on the patch field, and each pin cable can reach ports 1 to 8. Out of the box, d0 is cabled to port 1 and d5 to port 6.

.. _table-11-2:

.. table:: **Table 11-2** Ways a program reaches a device

   +-----------+-----------------------------------+----------------------------------------+
   | Method    | Instructions                      | Reaches                                |
   +===========+===================================+========================================+
   | Pins      | ``l``, ``s`` and friends on d0–d5 | The device on the I/O port that the    |
   |           |                                   | pin's cable is plugged into            |
   +-----------+-----------------------------------+----------------------------------------+
   | Device ID | ``ld``, ``sd``                    | Any device on the rack's data network. |
   |           |                                   | The IDs on ports 1–8 are in memory     |
   |           |                                   | cells 4128–4135, and those on ports    |
   |           |                                   | 9–32 in cells 4160–4183                |
   +-----------+-----------------------------------+----------------------------------------+
   | Batch     | ``lb``, ``sb``, ``lbn``, ``sbn``  | Every matching device on the rack's    |
   |           |                                   | data network                           |
   +-----------+-----------------------------------+----------------------------------------+

Ports 9 to 32 have no pins at all; they exist so that a program can find device IDs in memory instead of hard-coding them. Assign a device to one of these ports, and the program reads its ID from the matching memory cell and addresses it with ``ld`` and ``sd``.

11.2.1 Assigning a device to a pin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: Assigning a device to a pin

**Requirements:** The device must be on the rack's data network, and the panel must not be locked with the **PLCK** DIP switch on.

1. Open the Network program.
2. Select the device with **UP** and **DN**.
3. Press the digit of the pin, **0** to **5**.

**Result:** The device becomes that pin for every processor in the rack. The rack puts the device on a free port and moves the pin's cable to it, so you do not have to touch the patch field yourself.

To place a device on a port without a pin, press **F3** in the Network program, which steps the selected device through ports 1 to 32. **F4** clears every port. On the patch field itself, clicking a pin cable moves it to the next free port to the right, and holding the modifier while clicking pulls it out. The Network program is described in full in :ref:`5.12 Network <os-network>`.

11.3 Controls that affect programs
----------------------------------

.. index::
   single: Controls that affect programs

Several panel controls and settings change how programs run without changing a line of their code. The controls themselves are described in :ref:`4 Controls and indicators <ch-controls>`; :ref:`Table 11-3 <table-11-3>` lists only what each does to a running program.

.. _table-11-3:

.. table:: **Table 11-3** Controls that affect programs

   +--------------------------+-------------------------+-----------------------------------------+
   | Control                  | Where                   | Effect on programs                      |
   +==========================+=========================+=========================================+
   | **CLOCK**                | Processor unit          | Lines per tick: 32, 64, 128 or 256 (LO, |
   |                          |                         | MED, HI, MAX)                           |
   +--------------------------+-------------------------+-----------------------------------------+
   | **TURBO**                | Processor unit          | Doubles the clock, and the power the    |
   |                          |                         | processors draw                         |
   +--------------------------+-------------------------+-----------------------------------------+
   | **CPU clock multiplier** | Setup utility           | Scales the clock by 0.5, 1 or 2, on top |
   |                          |                         | of **CLOCK** and **TURBO**              |
   +--------------------------+-------------------------+-----------------------------------------+
   | **I/O**                  | Processor unit          | Off: programs keep running but reach no |
   |                          |                         | device at all, by pin, by ID or by      |
   |                          |                         | batch                                   |
   +--------------------------+-------------------------+-----------------------------------------+
   | **MEM WR**               | Processor unit          | Off: the rack's own processors can no   |
   |                          |                         | longer ``put`` into its memory. It does |
   |                          |                         | not stop ``clr``                        |
   +--------------------------+-------------------------+-----------------------------------------+
   | **DEBUG**                | Processor unit          | On: all processors wait, and **STEP**   |
   |                          |                         | advances the selected one by a line, or |
   |                          |                         | ten with the modifier                   |
   +--------------------------+-------------------------+-----------------------------------------+
   | **HALT ALL**             | Processor unit, guarded | Stops all twelve processors             |
   +--------------------------+-------------------------+-----------------------------------------+
   | **PROG**                 | Processor unit          | Selects processor 1–4 as the selected   |
   |                          |                         | processor: the one a computer's IC      |
   |                          |                         | editor reads and writes, **STEP**       |
   |                          |                         | advances and ``LineNumber`` reports.    |
   |                          |                         | The CPU program can select any of the   |
   |                          |                         | twelve                                  |
   +--------------------------+-------------------------+-----------------------------------------+
   | **AUTO**                 | DIP switch 4            | On: programs start at power-up. Off:    |
   |                          |                         | they wait for **RST**                   |
   +--------------------------+-------------------------+-----------------------------------------+
   | **WDOG**                 | DIP switch 5            | On: a processor stopped by a runtime    |
   |                          |                         | error restarts after 3 s                |
   +--------------------------+-------------------------+-----------------------------------------+
   | **REM**                  | Switch strip            | Off: chips outside the rack cannot      |
   |                          |                         | write the rack's logic values; see      |
   |                          |                         | :ref:`11.5 <sec-11-5>`                  |
   +--------------------------+-------------------------+-----------------------------------------+

11.4 Loading and storing programs
---------------------------------

.. index::
   single: Loading and storing programs

A chip carries its program with it, as in any housing. The rack adds two conveniences: a computer on the data network can edit the chip of the selected processor, and every drive has eight slots in which programs can be stored and loaded again.

11.4.1 Editing a program with a computer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: Editing a program with a computer

**Requirements:** A computer with an IC editor must be on the rack's data network, and the processor must have a chip.

1. Select the processor: turn the **PROG** knob for processors 1 to 4, or pick any processor in the CPU program with **UP** and **DN**.
2. Open the IC editor on the computer. It now reads the program of that processor.
3. Edit the program, and write it back from the computer as you would to any housing.
4. Press **RST** for that processor (or **F2** in the CPU program) to make sure it starts again from the first line.

**Result:** The processor runs the new program. If it does not compile, the processor shows CODE, and the Check tab of the CPU program names the line.

For a quick fix without a computer, use the Editor tab of the CPU program, which can change numbers in a line, comment lines out, copy and delete them, and write the result to the chip.

11.4.2 Storing and loading programs on a drive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: Storing and loading programs on a drive

**Requirements:** A drive must be in the selected bay and a chip in the processor's socket. For storing, the rack's write protection (**WP**) must be off.

1. Open the CPU program and select the processor with **UP** and **DN**.
2. Select the drive with **BAY-** and **BAY+**.
3. Type the slot number, 1 to 8. Without a number, slot 1 is used.
4. Press **CPY** to store the processor's program in that slot, or **PST** to load the program from the slot into the processor, and confirm the question that follows.

**Result:** The program is stored on the drive, labelled with the processor and the time, or loaded into the processor's chip, which then starts again from its first line. Programs on a drive travel with the drive, which makes a drive a convenient way to carry a library of programs from rack to rack.

The CPU program, its debugger and its code check are described in :ref:`5.13 CPU <os-cpu>`.

.. _sec-11-5:

11.5 Access from programs
-------------------------

.. index::
   single: Access from programs

A program reaches the rack in two ways: through its memory, with ``get``, ``put`` and ``clr``, and through its logic values, with ``l`` and ``s``. The same instructions work from the rack's own processors, through ``db``, and from chips in other housings, through a pin that points at the rack. What differs is what restrains them.

.. _table-11-4:

.. table:: **Table 11-4** What restrains access to the rack

   +----------------------------------------+-----------------------------------------+----------------------------------------+
   | Operation                              | From the rack's own processors          | From chips in other housings           |
   +========================================+=========================================+========================================+
   | ``get`` from a data bank               | The bank must be served                 | The bank must be served                |
   +----------------------------------------+-----------------------------------------+----------------------------------------+
   | ``put`` into a data bank               | **MEM WR** must be on; the bank must be | The bank must be served and not        |
   |                                        | served and not write-protected          | write-protected                        |
   +----------------------------------------+-----------------------------------------+----------------------------------------+
   | ``put`` into a scratch cell            | The rack must be running, and the BIOS  | The rack must be running, and the BIOS |
   |                                        | must allow it                           | must allow it                          |
   +----------------------------------------+-----------------------------------------+----------------------------------------+
   | ``clr`` on the rack                    | Only write protection stops it          | Only write protection stops it         |
   +----------------------------------------+-----------------------------------------+----------------------------------------+
   | ``s`` to ``Mode``, ``Lock``,           | Always allowed                          | **REM** must be on and **MAINT** off   |
   | ``Setting``, ``Index``, ``LineNumber`` |                                         |                                        |
   | or ``ClearMemory``                     |                                         |                                        |
   +----------------------------------------+-----------------------------------------+----------------------------------------+
   | ``l`` of any logic value               | Always allowed                          | Always allowed                         |
   +----------------------------------------+-----------------------------------------+----------------------------------------+

Every refused write, and every read from a bank that nothing serves, adds one to the fault counter; a refused read returns 0. Addresses below 0 or above 4183 stop the program with an error.

.. admonition:: NOTICE
   :class: note

   A ``clr`` on the rack formats every bank that is not write-protected, all at once, and neither **MEM WR** nor **REM** prevents it. Keep ``clr`` out of every program that addresses the rack, including programs in other housings with a pin on the rack, and write-protect the banks you care about.

11.6 Errors and debugging
-------------------------

.. index::
   single: Errors and debugging

A runtime error stops only the processor it happens on. The processor shows ERR, its ERR lamp lights, and the error and its line appear in the CPU program and in the event log. With the **WDOG** DIP switch on, the processor restarts after 3 s, which keeps an occasional error from becoming an outage, and also keeps a persistent one from ever being noticed. A program that does not compile shows CODE instead, and does not start at all.

The Check tab of the CPU program reads each program and reports, in plain words, code that does not compile, unknown instructions, jumps to labels that do not exist, loops without a ``yield``, programs with no ``yield`` at all, programs that end without looping, programs longer than the chip holds, pins the program uses that have no device, and values a device cannot read or set. It is worth running before you blame the hardware.

The debugger, also in the CPU program, can pause a processor, step it a line at a time, step over, set up to 16 breakpoints, run to the cursor, and stop when a watched register changes. With **DEBUG** on, all processors in the rack wait, and **STEP** advances the selected one.

The ``hcf`` instruction heats the core by 25 °C and logs an error. The rack takes the instruction's name more literally than most housings, so keep it out of production code.

11.7 Examples
-------------


The examples below use the default 512-cell drives. With another ``DriveCapacity``, the bank size and every status address move; see :ref:`12 Logic and memory reference <ch-reference>`.

**Example 11-1** Reading the rack from an ordinary IC housing, with the rack on d0

.. code-block:: text

	alias rack d0
	get r0 rack 4096      # core temperature in C
	get r1 rack 4098      # UPS charge 0-1
	put rack 100 r0       # keep a copy in cell 100
	l r2 rack Error       # 1 = overheated

**Example 11-2** Logging a sensor into bank 1 from a processor inside the rack, with the sensor on d0 (**MEM WR** must be on)

.. code-block:: text

	# Bank 1 temperature log
	alias sensor d0
	define BASE 512
	move r1 0
	loop:
	l r0 sensor Temperature
	add r2 BASE r1
	put db r2 r0
	add r1 r1 1
	mod r1 r1 512
	sleep 10
	j loop

**Example 11-3** Passing a flag between two rack processors through a scratch cell

.. code-block:: text

	put db 4136 1         # processor A raises the flag
	get r0 db 4136        # processor B reads it

**Example 11-4** Using a device on an I/O port above 8, which has no pin, by its ID

.. code-block:: text

	get r0 db 4160        # device ID on I/O port 9
	ld r1 r0 Pressure     # read it by ID

**Example 11-5** Letting one program find out which processor it is running on

.. code-block:: text

	get r0 db 4127        # 1-12 inside the rack, 0 from outside
	sub r0 r0 1
	mul r1 r0 512         # processors 1-8: start of bank n-1

Example 11-5 lets you load the same program into up to eight processors and have each work on its own bank, which is tidier than keeping eight copies that differ by one number. Processors 9 to 12 would land in the status cells, so give them other work.

11.8 Programming guidelines
---------------------------

.. index::
   single: Programming guidelines

A few habits make rack programs easier to live with, and the rack easier to live with too.

- Give every loop a ``yield`` or a ``sleep``. A program without one uses its whole clock every tick, which costs power and heat and achieves nothing that a ``yield`` would not.
- Protect the banks you care about, and keep ``clr`` out of anything that addresses the rack.
- Use the scratch cells for flags and handshakes between processors, and the data banks for data.
- Assign devices to I/O ports and read their IDs from memory, rather than hard-coding IDs that change when a device is rebuilt.
- Store finished programs on a drive, so that a lost chip is an inconvenience rather than a rewrite.
- Leave **WDOG** off while developing, so that errors stay visible, and switch it on once a program is trusted.

How banks, drives and write protection work is explained in :ref:`6 Storage and data handling <ch-storage>`, and the BIOS settings mentioned here in :ref:`7 Configuration <ch-configuration>`.
