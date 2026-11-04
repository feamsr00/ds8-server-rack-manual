.. _os-cpu:

5.13 CPU (Processor Unit)
=========================
CPU is the control room for the rack's twelve processors. It shows what each one is doing and offers a debugger, a small code editor and a code check, so that most problems can be found and fixed without leaving the rack. It is program 7 in the Logic group; open it with the **CPU** key. Inside the program, the same key selects the next processor, or the previous one with the modifier. Sockets, pins and the switches that change how programs run are described in :ref:`11 Programming (IC10) <ch-programming>`.

5.13.1 Screen
-------------

.. image:: /images/os-cpu.png
   :alt: Processor Unit Overview: processors 1 to 5 running, 6 to 12 empty with their rear-door slot, and a panel showing the clock, I/O, db and pins d0 to d5

**Figure 5-10** The Overview tab with processors 1–5 running and 6–12 empty. Under the list: 128 lines a tick, I/O on, ``db`` writable, and the port behind each pin.

The Overview tab lists every processor with its place (front or rear), its state and mode, the line it is on, its program size and its last error. An empty rear socket shows which slot in the rear door it is. The panel under the list shows the clock speed in lines per tick, whether I/O is on, whether the processors may write to the rack's memory (**MEM WR**), and which port and device each pin d0–d5 reaches.

5.13.2 Tabs and keys
--------------------
The program has four tabs, and **TAB** moves between them.

**Table 5-14** CPU soft keys by tab

+----------+------------------+------------------+--------------------+-------------------+-------------------+
| Tab      | **F1**           | **F2**           | **F3**             | **F4**            | **F5**            |
+==========+==================+==================+====================+===================+===================+
| Overview | Run / halt       | Reset            | Pause and open the | Next processor    | Check the code    |
|          |                  |                  | debugger           |                   |                   |
+----------+------------------+------------------+--------------------+-------------------+-------------------+
| Debugger | Pause / run      | Step one line    | Step over          | Breakpoint at the | Run to the cursor |
|          |                  |                  |                    | cursor (up to 16) |                   |
+----------+------------------+------------------+--------------------+-------------------+-------------------+
| Editor   | Comment the line | Copy the line    | Delete the line    | Undo everything   | Write the program |
|          | out              |                  |                    |                   | to the chip       |
+----------+------------------+------------------+--------------------+-------------------+-------------------+
| Check    | Check again      | Show the line in | Show the line in   | —                 | —                 |
|          |                  | the debugger     | the editor         |                   |                   |
+----------+------------------+------------------+--------------------+-------------------+-------------------+

A few more keys complete the set.

- **Overview:** Use **UP** and **DN** to select a processor, and press **ENT** to open it in the debugger. To save its program to the drive in the selected bay, type a slot number and press **CPY**; to load the program in that slot instead, press **PST** (see :ref:`5.9 Disks <os-disks>`).
- **Debugger:** Use **INC** and **DEC** to pick a register to watch, and the processor stops as soon as that register changes. **CLR** removes all breakpoints.
- **Editor:** Use **UP** and **DN** to pick a line and **<** and **>** to pick a number in it, then change the number by typing digits and pressing **ENT**, or with **INC** and **DEC**.

5.13.3 The code check
---------------------
The code check reads a program and reports, in plain words:

- code that does not compile, unknown instructions, and jumps to labels that do not exist;
- loops without a ``yield``, and programs with no ``yield`` at all, which use the whole clock every tick;
- programs that end without looping, and programs longer than the chip can hold;
- pins the program uses that have no device on them, and values a device cannot read or set.

5.13.4 Processor states
-----------------------
**Table 5-15** Processor states and socket lamps

+-----------------------------+------------------------+
| State                       | Socket lamps           |
+=============================+========================+
| Empty socket                | Dark                   |
+-----------------------------+------------------------+
| Halted                      | **RUN** steady green   |
+-----------------------------+------------------------+
| Running                     | **RUN** flashing green |
+-----------------------------+------------------------+
| Single step (paused)        | **RUN** amber          |
+-----------------------------+------------------------+
| Error (at run time)         | **ERR** flashing red   |
+-----------------------------+------------------------+
| Bad code (does not compile) | **ERR** steady red     |
+-----------------------------+------------------------+

A run-time error stops only the processor that hit it. The error and its line appear on this screen and in the event log, and with the **WDOG** DIP switch on, the processor restarts after 3 s.

5.13.5 Finding a fault with the debugger
----------------------------------------
**Requirements:** The processor must have a chip and a program.

1. On the Overview tab, select the processor and press **F3**. The processor pauses and the debugger opens.
2. Move the cursor to a line of interest and press **F4** to set a breakpoint there.
3. Press **F1** to run until the breakpoint, or **F2** to step one line at a time.
4. If a register is misbehaving, pick it with **INC** or **DEC**, and the processor will stop the moment it changes.

**Result:** The processor stops exactly where the trouble starts. Press **CLR** to remove the breakpoints and **F1** to let it run on.

5.13.6 Making a quick fix in the editor
---------------------------------------
**Requirements:** The fix must be small enough to make by changing numbers or commenting lines out; anything larger is easier on a computer.

1. Select the processor on the Overview tab, then press **TAB** until the Editor tab opens.
2. Select the line with **UP** and **DN**, and the number with **<** and **>**.
3. Type the new value and press **ENT**, or use **F1** to comment the whole line out.
4. Press **F5** to write the program to the chip.

**Result:** The changed program runs on the chip, and the event log notes that it was changed on the rack. If you change your mind before step 4, **F4** undoes everything.
