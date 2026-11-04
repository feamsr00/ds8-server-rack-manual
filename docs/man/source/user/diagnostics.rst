.. _ch-diagnostics:

9 Diagnostics and troubleshooting
=================================

.. index::
   single: Diagnostics and troubleshooting

Most problems with the rack name themselves, provided you know where to look. This chapter lists the places the rack reports its condition, explains what each rack state means, and then works through the usual symptoms by subject, from power to saved games. If your question is less "what is wrong" than "why does it do that", :ref:`10 FAQ <ch-faq>` may answer it faster.

9.1 Diagnostic aids
-------------------

.. index::
   single: Diagnostic aids

Start with the tooltip and the event log, in that order. Between them they explain most problems, and the remaining aids in :ref:`Table 9-1 <table-9-1>` fill in the detail.

.. _table-9-1:

.. table:: **Table 9-1** Diagnostic aids

   +------------------+-----------------------------------------+-----------------------------------------+
   | Aid              | Where                                   | What it tells you                       |
   +==================+=========================================+=========================================+
   | Tooltip          | Look at the rack                        | The rack state                          |
   |                  |                                         | (:ref:`Table 9-2 <table-9-2>`), core    |
   |                  |                                         | temperature, power draw and UPS charge; |
   |                  |                                         | drives fitted and cells used; whether   |
   |                  |                                         | write protection is on; chips fitted    |
   |                  |                                         | and running; and whether the air filter |
   |                  |                                         | is pulled                               |
   +------------------+-----------------------------------------+-----------------------------------------+
   | Lamps and beacon | Front panel and top of the cabinet      | What needs attention at a glance; see   |
   |                  |                                         | :ref:`4.12 <sec-4-12>`                  |
   +------------------+-----------------------------------------+-----------------------------------------+
   | Event log        | Events program                          | What happened and when, newest first,   |
   |                  |                                         | with warnings and errors marked. It     |
   |                  |                                         | holds the last 40 entries and is not    |
   |                  |                                         | saved with the game                     |
   +------------------+-----------------------------------------+-----------------------------------------+
   | Self test        | **TEST** in the service bay             | The first fault the rack can find in    |
   |                  |                                         | itself; see :ref:`8.3 <sec-8-3>`        |
   +------------------+-----------------------------------------+-----------------------------------------+
   | Service display  | Service bay                             | Thermal, processor and counter pages;   |
   |                  |                                         | see :ref:`8.3 <sec-8-3>`                |
   +------------------+-----------------------------------------+-----------------------------------------+
   | Fault counter    | System program, service display, status | How many memory accesses and logic      |
   |                  | cell 4111                               | writes the rack has refused since the   |
   |                  |                                         | counters were last reset                |
   +------------------+-----------------------------------------+-----------------------------------------+
   | Code check       | Check tab of the CPU program            | Problems in a processor's program, by   |
   |                  |                                         | line                                    |
   +------------------+-----------------------------------------+-----------------------------------------+
   | Game log         | The game's log file                     | Messages from the mod itself, each      |
   |                  |                                         | starting with ``[ServerRack]``          |
   +------------------+-----------------------------------------+-----------------------------------------+

The event log deserves particular attention, because the rack writes to it whenever something changes state: a drive goes offline, a rule fires, a processor stops, the filter is pulled. Every message and its meaning is listed in :ref:`Appendix C: Event messages <app-c>`, and the Events program is described in :ref:`5.8 Events <os-events>`.

9.2 Rack states
---------------

.. index::
   single: Rack states

The first word of the tooltip is the rack's state. The states are checked in the order of :ref:`Table 9-2 <table-9-2>`, so the tooltip always shows the most fundamental problem first: a rack with no system board will say so, however hot it may also be.

.. _table-9-2:

.. table:: **Table 9-2** Rack states

   +-------------------+----------------------------------------+----------------------------------------+
   | State             | Meaning                                | What to do                             |
   +===================+========================================+========================================+
   | Off               | The rack is switched off at **MAIN     | Switch **MAIN POWER** on               |
   |                   | POWER**                                |                                        |
   +-------------------+----------------------------------------+----------------------------------------+
   | No system board   | The board slot behind the monitor is   | Pull the lock pin, swing the monitor   |
   |                   | empty, so the rack cannot start        | out and fit any motherboard            |
   +-------------------+----------------------------------------+----------------------------------------+
   | Waiting for RESET | The power came back after a cut, and   | Press **RESET**                        |
   |                   | the BIOS setting **After power loss**  |                                        |
   |                   | is Stay off                            |                                        |
   +-------------------+----------------------------------------+----------------------------------------+
   | Setup utility     | The setup utility is open, so storage  | Press **F5** or **ESC** to save and    |
   |                   | and processors are offline             | restart                                |
   +-------------------+----------------------------------------+----------------------------------------+
   | No power          | The rack is switched on, but neither   | Check the power cable and the base's   |
   |                   | mains nor the UPS is supplying it      | supply                                 |
   +-------------------+----------------------------------------+----------------------------------------+
   | Overheated        | The core has passed its trip           | Fix the cooling                        |
   |                   | temperature, so storage is offline and | (:ref:`Table 9-4 <table-9-4>`)         |
   |                   | processors and automation have stopped |                                        |
   +-------------------+----------------------------------------+----------------------------------------+
   | On battery        | Mains has failed and the UPS is        | Restore mains; the UPS lasts about two |
   |                   | carrying the rack                      | minutes at full load                   |
   +-------------------+----------------------------------------+----------------------------------------+
   | Online            | Everything is working                  | Nothing, which is the best kind of     |
   |                   |                                        | maintenance                            |
   +-------------------+----------------------------------------+----------------------------------------+

9.3 The fault counter
---------------------

.. index::
   single: Fault counter

The fault counter goes up by one whenever the rack refuses a request. A read from a bank that no drive serves returns 0 and counts a fault, as does a write that is dropped because of write protection or because nothing serves the bank. Writes to status cells other than the scratch cells, writes from the rack's own processors while **MEM WR** is off, and logic writes from outside the rack while **REM** is off or **MAINT** is on are counted the same way.

A counter that climbs steadily is therefore a program, a rule or another chip asking for something the rack will not give it. Watch the counter on the System program while you halt processors one at a time, and the culprit usually reveals itself. **COUNT** in the service bay or **RSIO** on the key pad resets it.

.. _sec-9-4:

9.4 Troubleshooting
-------------------

.. index::
   single: Troubleshooting

The tables below are grouped by subject. In each, the possible causes are listed roughly from the most to the least likely.

9.4.1 Power and start-up
^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: Power and start-up

.. _table-9-3:

.. table:: **Table 9-3** Power and start-up

   +-----------------------------------------+-----------------------------------------+----------------------------------------+
   | Symptom                                 | Possible cause                          | Remedy                                 |
   +=========================================+=========================================+========================================+
   | The tooltip says No system board        | The board slot is empty                 | Swing the monitor out and fit any      |
   |                                         |                                         | motherboard; see :ref:`7.1 <sec-7-1>`  |
   +-----------------------------------------+-----------------------------------------+----------------------------------------+
   | The tooltip says No power               | No mains, and the UPS is empty or       | Check the power cable and the base's   |
   |                                         | bypassed                                | supply, then let the UPS charge        |
   +-----------------------------------------+-----------------------------------------+----------------------------------------+
   | The tooltip says Waiting for RESET      | **After power loss** is set to Stay off | Press **RESET**, or set **After power  |
   |                                         |                                         | loss** to Restart in the setup utility |
   +-----------------------------------------+-----------------------------------------+----------------------------------------+
   | The tooltip says Setup utility          | Someone pressed the **BIOS** button     | Press **F5** or **ESC**                |
   +-----------------------------------------+-----------------------------------------+----------------------------------------+
   | Processors did not start after power-up | The **AUTO** DIP switch is off          | Press **RST** for each processor, or   |
   |                                         |                                         | switch **AUTO** on                     |
   +-----------------------------------------+-----------------------------------------+----------------------------------------+
   | The monitor shows an update screen      | An OS update is waiting to be installed | Press **ENT** to install it; see       |
   |                                         |                                         | :ref:`8.8 <sec-8-8>`                   |
   +-----------------------------------------+-----------------------------------------+----------------------------------------+
   | The monitor will not swing out          | The lock pin is in                      | Pull the pin above the monitor first   |
   +-----------------------------------------+-----------------------------------------+----------------------------------------+

9.4.2 Temperature, alarm and UPS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: Temperature, alarm and UPS

.. _table-9-4:

.. table:: **Table 9-4** Temperature, alarm and UPS

   +-----------------------------------------+-----------------------------------------+-----------------------------------------+
   | Symptom                                 | Possible cause                          | Remedy                                  |
   +=========================================+=========================================+=========================================+
   | The tooltip says Overheated             | No air, a clogged or pulled filter,     | Fix the cooling. The rack restarts by   |
   |                                         | fans on Low, or a hot room              | itself once the core is 10 °C below the |
   |                                         |                                         | alarm temperature; with the **ARST**    |
   |                                         |                                         | DIP switch off, press **RESET**         |
   +-----------------------------------------+-----------------------------------------+-----------------------------------------+
   | The core runs hot but has not tripped   | Worn filter, **FAN** trim low, or fans  | Clean the filter, set the fans to Auto, |
   |                                         | on Manual                               | or raise the **FAN** trim               |
   +-----------------------------------------+-----------------------------------------+-----------------------------------------+
   | The alarm keeps sounding                | On battery, above the alarm             | **MUTE** silences it until the cause    |
   |                                         | temperature, filter pulled, or an alarm | clears; the Dashboard lists rule and    |
   |                                         | raised by a rule or library task        | task alarms                             |
   +-----------------------------------------+-----------------------------------------+-----------------------------------------+
   | There is no alarm although something is | **MAINT** is on, or the **ALRM** switch | Switch **MAINT** off and **ALRM** on    |
   | wrong                                   | is off                                  |                                         |
   +-----------------------------------------+-----------------------------------------+-----------------------------------------+
   | The beeper is silent but the beacon     | The **BEEP** DIP switch is off          | Switch **BEEP** on                      |
   | flashes                                 |                                         |                                         |
   +-----------------------------------------+-----------------------------------------+-----------------------------------------+
   | The UPS does not take over              | **BYPASS** on, battery reconditioning,  | Switch **BYPASS** off, let the UPS      |
   |                                         | charge down to the **CUT** reserve, or  | charge, and lower **CUT**               |
   |                                         | ``UpsCapacityKJ`` set to 0              |                                         |
   +-----------------------------------------+-----------------------------------------+-----------------------------------------+
   | The UPS runtime has become shorter      | Battery health has fallen with each     | Recondition the battery; see            |
   |                                         | full discharge                          | :ref:`8.5 <sec-8-5>`                    |
   +-----------------------------------------+-----------------------------------------+-----------------------------------------+

9.4.3 Storage and memory
^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: Storage and memory

.. _table-9-5:

.. table:: **Table 9-5** Storage and memory

   +----------------------------------------+-----------------------------------------+----------------------------------------+
   | Symptom                                | Possible cause                          | Remedy                                 |
   +========================================+=========================================+========================================+
   | Reads return 0 and the fault counter   | The bank is not served: its bus is off, | Check **BUS A** and **BUS B**, the bay |
   | climbs                                 | its bay is offline, its patch cable is  | buttons, the patch field and the Disks |
   |                                        | pulled, there is no drive, or the rack  | program                                |
   |                                        | is offline                              |                                        |
   +----------------------------------------+-----------------------------------------+----------------------------------------+
   | Writes are ignored                     | The **WP** toggle, the bank's           | Switch the protection off              |
   |                                        | write-protect switch, or the BIOS       |                                        |
   |                                        | setting **Write protect at boot**       |                                        |
   +----------------------------------------+-----------------------------------------+----------------------------------------+
   | A rack processor cannot write memory   | **MEM WR** is off                       | Switch **MEM WR** on                   |
   +----------------------------------------+-----------------------------------------+----------------------------------------+
   | A write to a status cell is ignored    | Only the scratch cells 4136–4143 can be | Use a scratch cell or a data bank      |
   |                                        | written, only while the rack is         |                                        |
   |                                        | running, and only if the BIOS allows it |                                        |
   +----------------------------------------+-----------------------------------------+----------------------------------------+
   | A program stops with an error on       | The address is below 0 or above 4183    | Check the address arithmetic           |
   | ``get`` or ``put``                     |                                         |                                        |
   +----------------------------------------+-----------------------------------------+----------------------------------------+
   | Several banks are suddenly empty       | A ``clr`` or a write to ``ClearMemory`` | See the notice below                   |
   |                                        | formatted them                          |                                        |
   +----------------------------------------+-----------------------------------------+----------------------------------------+
   | The event log is empty after loading a | The event log is not saved              | Nothing; this is expected              |
   | save                                   |                                         |                                        |
   +----------------------------------------+-----------------------------------------+----------------------------------------+

.. admonition:: NOTICE
   :class: note

   A single ``clr`` from any program that points a pin at the rack, or a write of 1 to ``ClearMemory``, formats every bank that is not write-protected, all at once. Neither **REM** nor **MEM WR** prevents a ``clr``; only write protection does. Switch on write protection for the banks you care about.

How banks, drives and protection fit together is explained in :ref:`6 Storage and data handling <ch-storage>`.

9.4.4 Processors and programs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: Processors and programs

.. _table-9-6:

.. table:: **Table 9-6** Processors and programs

   +------------------------------------+---------------------------------------+-----------------------------------------+
   | Symptom                            | Possible cause                        | Remedy                                  |
   +====================================+=======================================+=========================================+
   | A processor does not run           | **RUN** off, **HALT ALL** pressed,    | Switch **RUN** on and **DEBUG** off,    |
   |                                    | **DEBUG** on, paused in the debugger, | press **RST**, and check the CPU        |
   |                                    | or **AUTO** off after a power-up      | program                                 |
   +------------------------------------+---------------------------------------+-----------------------------------------+
   | A processor shows CODE or Bad code | The program does not compile          | The Check tab of the CPU program names  |
   |                                    |                                       | the line                                |
   +------------------------------------+---------------------------------------+-----------------------------------------+
   | A processor shows ERR              | A runtime error stopped it            | The CPU program and the event log name  |
   |                                    |                                       | the line. With the **WDOG** DIP switch  |
   |                                    |                                       | on, it restarts after 3 s               |
   +------------------------------------+---------------------------------------+-----------------------------------------+
   | A program cannot reach a device    | The **I/O** switch is off, the pin is | Switch **I/O** on, and patch the pin in |
   |                                    | not patched, or the device is not on  | the Network program: select the device  |
   |                                    | the rack's data network               | and press 0–5                           |
   +------------------------------------+---------------------------------------+-----------------------------------------+
   | Every pin has lost its device      | A factory reset emptied the I/O ports | Assign the devices again in the Network |
   |                                    |                                       | program                                 |
   +------------------------------------+---------------------------------------+-----------------------------------------+
   | Programs run slowly                | **CLOCK** on LO or MED, or the BIOS   | Turn **CLOCK** up, or switch **TURBO**  |
   |                                    | multiplier at x0.5                    | on                                      |
   +------------------------------------+---------------------------------------+-----------------------------------------+

The CPU program and its debugger are described in :ref:`5.13 CPU <os-cpu>`, and the Network program in :ref:`5.12 Network <os-network>`.

9.4.5 Controls and panel
^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: Controls and panel

.. _table-9-7:

.. table:: **Table 9-7** Controls and panel

   +---------------------------------------+---------------------------------------+-----------------------------------------+
   | Symptom                               | Possible cause                        | Remedy                                  |
   +=======================================+=======================================+=========================================+
   | The keys do nothing                   | The glass cover is shut, the panel is | Open the cover, unlock the panel, press |
   |                                       | locked, the screen saver is on, the   | a key to wake the screen, close the     |
   |                                       | rack is overheated, a help window is  | help window, or press **ENT** to        |
   |                                       | open, or the OS update screen is      | install the update                      |
   |                                       | showing                               |                                         |
   +---------------------------------------+---------------------------------------+-----------------------------------------+
   | The **LOCK** switch will not turn     | The rack key is not in your hand      | Hold the key, or switch the server      |
   |                                       |                                       | setting ``KeyRequired`` off             |
   +---------------------------------------+---------------------------------------+-----------------------------------------+
   | The patch cables will not move        | The **PLCK** DIP switch is on and the | Unlock the panel                        |
   |                                       | panel is locked                       |                                         |
   +---------------------------------------+---------------------------------------+-----------------------------------------+
   | The rear controls do not respond      | The service hatch is closed           | Open the hatch                          |
   +---------------------------------------+---------------------------------------+-----------------------------------------+
   | Logic writes from outside are ignored | **REM** is off, or **MAINT** is on    | Switch **REM** on and **MAINT** off     |
   +---------------------------------------+---------------------------------------+-----------------------------------------+
   | **CLEAN** or **NEW** says PULL THE    | The filter is still in the rack       | Pull the filter first; see              |
   | FILTER FIRST                          |                                       | :ref:`8.4 <sec-8-4>`                    |
   +---------------------------------------+---------------------------------------+-----------------------------------------+

The front panel and every switch on it are described in :ref:`4 Controls and indicators <ch-controls>`, and the service bay in :ref:`8 Maintenance <ch-maintenance>`.

9.4.6 Automation
^^^^^^^^^^^^^^^^


.. _table-9-8:

.. table:: **Table 9-8** Automation

   +-----------------------------------+-----------------------------------------+-----------------------------------------+
   | Symptom                           | Possible cause                          | Remedy                                  |
   +===================================+=========================================+=========================================+
   | A rule never acts                 | Rules act on a change, only after their | Check the delay, and the live reading   |
   |                                   | delay, and only while the rack is       | shown on the Rules screen               |
   |                                   | online                                  |                                         |
   +-----------------------------------+-----------------------------------------+-----------------------------------------+
   | A rule acts once and then stops   | It is waiting for the value to fall     | Narrow the band, or use the compare     |
   |                                   | back through its band before it can     | type always                             |
   |                                   | fire again                              |                                         |
   +-----------------------------------+-----------------------------------------+-----------------------------------------+
   | A library task shows Missing:     | A required role has no device           | Press **F2** to find devices, or assign |
   |                                   |                                         | one by hand                             |
   +-----------------------------------+-----------------------------------------+-----------------------------------------+
   | A print job has vanished          | Someone changed the printer's recipe by | Add the job again; the event log names  |
   |                                   | hand                                    | it                                      |
   +-----------------------------------+-----------------------------------------+-----------------------------------------+
   | A scene recall changed devices in | Scenes act on every device on the       | Check what a scene holds before you     |
   | another room                      | rack's data network                     | recall it                               |
   +-----------------------------------+-----------------------------------------+-----------------------------------------+

9.4.7 Saves and other mods
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: Saves and other mods

.. _table-9-9:

.. table:: **Table 9-9** Saves and other mods

   +-----------------------------------------+-----------------------------------------+---------------------------------------+
   | Symptom                                 | Possible cause                          | Remedy                                |
   +=========================================+=========================================+=======================================+
   | A save will not load after installing   | The mod is installed twice, or a        | Remove one copy, and look for the     |
   | the mod                                 | save-recovery mod clashes on an XML     | ``[ServerRack]`` message in the game  |
   |                                         | name                                    | log                                   |
   +-----------------------------------------+-----------------------------------------+---------------------------------------+
   | A save from before mod 5.5.1 loses its  | Another installed mod also uses the old | Remove or update the other mod        |
   | racks                                   | name ``ServerRackSaveData``             |                                       |
   +-----------------------------------------+-----------------------------------------+---------------------------------------+
   | A client sees the screen but cannot use | The client is missing the mod, or runs  | Install the host's version of the mod |
   | it                                      | a different version of it               | on every client                       |
   +-----------------------------------------+-----------------------------------------+---------------------------------------+

Multiplayer and save behaviour are described in :ref:`13 Multiplayer, saves and mods <ch-multiplayer>`.

9.5 Reporting a problem
-----------------------

.. index::
   single: Reporting a problem

If a problem survives this chapter, it may well be a fault in the mod rather than in your base. When you report it to the mod author, include the mod version (the System program's About window shows it), the last few entries of the event log, and every line of the game log that starts with ``[ServerRack]``. A description of what you expected to happen, and what happened instead, is worth more than any screenshot of a blank screen.
