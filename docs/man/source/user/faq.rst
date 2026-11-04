.. _ch-faq:

10 Frequently asked questions
=============================
These are the questions that come up once the rack is running and the first surprises have worn off. Each answer is short and points to the chapter with the full story. For a specific fault, start with :ref:`9 Diagnostics and troubleshooting <ch-diagnostics>` instead.

10.1 General
------------

Do I need drives or chips to use the rack?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
No. Rules, scenes, library tasks, print jobs and the Dashboard run inside the rack and need neither drives nor IC10 chips. Drives are needed only for the rack's memory and for backups, and chips only if you want to write your own programs.

Does every player need the mod?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Yes. The host runs all of the rack's logic, and each client draws the screen and panel from what the host sends and sends its clicks back, which only works if both ends have the mod. Use the same version everywhere.

Does the mod connect to the internet?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Only to ask the Steam client whether its Workshop item has a newer version, so that it can show a notice on the rack's screen. No other network access is known.

How is the rack different from an ordinary IC housing?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It is an IC housing with twelve sockets instead of one, a memory of 4,096 cells spread over eight drives, 32 I/O ports for device IDs, and an operating system with thirteen programs on top. All twelve processors share the same six pins, d0 to d5.

10.2 Power and cooling
----------------------

Why does my rack overheat in vacuum?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The fans cool the core with room air, and in vacuum there is none to speak of. A rack drawing 355 W in vacuum reaches its trip temperature in about nine minutes, so install it in a pressurised room. The full heat model is in chapter 3.

How long will the UPS keep the rack running?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
About 110 s at 355 W, or about 210 s at 187 W with the **ECO** DIP switch on. A battery cell in the battery slot adds its own charge on top, which is the simplest way to buy more time.

How do I make the rack draw less power?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Switch the **ECO** DIP switch on so that idle drives draw less, switch off the drive bus of any drives you do not need, keep the fans on Auto, and turn **CLOCK** down if your programs do not need the speed. Eight idle drives draw 280 W on their own, so the buses are the biggest lever.

Does the rack warm the room?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Yes, a little: 20 % of the heat the fans carry out goes into the room air, which you can change with the server setting ``ExhaustHeatFraction``. A busy rack in a small sealed room will notice its own exhaust eventually.

10.3 Storage
------------

What happens if I pull a drive from a running rack?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The data is safe, because it lives on the drive and simply leaves with it. Any bank the drive served answers 0 from then on, and the fault counter starts to climb if something keeps reading it.

Can I have bigger drives?
^^^^^^^^^^^^^^^^^^^^^^^^^
Yes, with the server setting ``DriveCapacity``, from 64 to 4,096 cells per drive. Change it before you build the first rack, because changing it later moves every memory address at once.

How do I back up my work?
^^^^^^^^^^^^^^^^^^^^^^^^^
The Disks program copies a whole drive to another bay. The Network program saves the patch field, I/O ports and logger devices to a drive with **F5**, and the Rules program saves all rules, scenes and library tasks to a drive with **F5**. Hold the modifier with **F5** to load them again.

10.4 Programming
----------------

Can chips in other housings use the rack's memory?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Yes. With the rack on one of its pins, any chip can ``get`` from it and ``put`` into it. **MEM WR** restrains only the rack's own processors, and **REM** guards only the rack's logic values, so only write protection stops another chip from writing.

Why does this manual keep warning about ``clr``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Because a single ``clr`` on the rack formats every bank that is not write-protected, all at once, and neither **REM** nor **MEM WR** prevents it. It is one short instruction with a very long reach, and it deserves the same respect as the guarded **FORMAT** button.

Can each processor have its own devices on d0 to d5?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
No. All twelve processors share the same six pins. For more devices, assign them to I/O ports 9 to 32 in the Network program and address them by ID, reading the IDs from memory cells 4160 to 4183.

How do two rack processors talk to each other?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Through the eight scratch cells at addresses 4136 to 4143, which any processor can write while the rack is running, unless the BIOS has made them read-only. A data bank works too, but the scratch cells are not lost if a drive is pulled.

Can I edit a program without a computer?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Yes, within reason: the Editor tab of the CPU program can change numbers, comment lines out, copy and delete lines, and write the result to the chip. For anything longer than a quick fix, a computer's IC editor is the better tool; the **PROG** knob chooses which of processors 1 to 4 it reaches.

What does ``hcf`` do in the rack?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It heats the core by 25 °C and logs an error. Halting and catching fire is, for once, almost literally what happens.

Programming the rack is covered in :ref:`11 Programming (IC10) <ch-programming>`, and every logic value and memory address in :ref:`12 Logic and memory reference <ch-reference>`.

10.5 Odds and ends
------------------

Why does the event log occasionally make jokes?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
On about one start in three, the rack greets you with a line of its own, and every five running hours it adds another. They are logged as information, cost nothing, and can be ignored; the full set is in :ref:`C Event messages <app-c>`.

Is the 900 W on the nameplate at the back true?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Only as a statement of ambition. A rack with eight idle drives draws about 355 W, and the real figures are in chapter 3.

Can I stop other players from changing my rack?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Partly. The **LOCK** key switch, turned with the rack key, locks the front panel, and the **PLCK** DIP switch makes it lock the patch cables too. The service bay at the back stays open to anyone, and so does the rack's memory to any chip that can reach it, so protect the banks that matter.

Does the rack work with other mods?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The SDS FieldPad tablet can mirror a rack's screen and click it remotely, StationeersLua chips run in the rack's sockets alongside IC10 chips, and the Data Centre mod's Workshop page says the two work side by side. Details are in :ref:`13 Multiplayer, saves and mods <ch-multiplayer>`.
