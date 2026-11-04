.. _app-c:

Appendix C: Event messages
==========================

.. index::
   single: Event messages

This appendix lists every message the rack writes to its event log, grouped by subject, with its level and what it means. The Events program shows the log newest first, each entry with the game-clock time and its level, and **F2** there filters it to warnings or errors only. The log keeps the last 40 entries and is not saved with the game. The Events program is described in :ref:`5.8 Events <os-events>`, and what to do about most warnings and errors in :ref:`9 Diagnostics and troubleshooting <ch-diagnostics>`.

In the tables, words in *italics* stand for what the rack fills in: a number, a name or a value.

.. _table-c-1:

.. table:: **Table C-1** Message levels

   +-------+------------------------------------------------------+
   | Level | Meaning                                              |
   +=======+======================================================+
   | I     | Information: something happened as it should, and is |
   |       | recorded for reference                               |
   +-------+------------------------------------------------------+
   | W     | Warning: something needs attention, or a change was  |
   |       | made that reduces protection                         |
   +-------+------------------------------------------------------+
   | E     | Error: something has stopped working, or an alarm    |
   |       | has been raised                                      |
   +-------+------------------------------------------------------+

C.1 Power and start-up
----------------------

.. _table-c-2:

.. table:: **Table C-2** Power and start-up messages

   +-----------------------------------------+-------+-----------------------------------------+
   | Message                                 | Level | Meaning                                 |
   +=========================================+=======+=========================================+
   | System started                          | I     | The rack has started, after power-up or |
   |                                         |       | a restart                               |
   +-----------------------------------------+-------+-----------------------------------------+
   | System resumed                          | I     | The rack was running when the game was  |
   |                                         |       | saved, and runs again after loading     |
   +-----------------------------------------+-------+-----------------------------------------+
   | System switched off                     | I     | The rack was switched off at **MAIN     |
   |                                         |       | POWER**                                 |
   +-----------------------------------------+-------+-----------------------------------------+
   | Power lost - system halted              | E     | The rack was switched on but lost all   |
   |                                         |       | power: no mains, and the UPS empty or   |
   |                                         |       | bypassed                                |
   +-----------------------------------------+-------+-----------------------------------------+
   | Mains power lost - running on UPS       | W     | Mains has failed and the UPS is         |
   | battery                                 |       | carrying the rack                       |
   +-----------------------------------------+-------+-----------------------------------------+
   | UPS self test - running on battery      | W     | **TEST** on the UPS panel is running    |
   |                                         |       | the rack on battery for 15 s            |
   +-----------------------------------------+-------+-----------------------------------------+
   | Mains power restored                    | I     | Mains is back after running on battery  |
   +-----------------------------------------+-------+-----------------------------------------+
   | UPS battery below *n* %                 | E     | The UPS charge has fallen below the     |
   |                                         |       | BIOS setting **Battery low warning**    |
   +-----------------------------------------+-------+-----------------------------------------+
   | Power lost - staying off until RESET is | W     | **After power loss** is set to Stay     |
   | pressed                                 |       | off; the rack waits for **RESET**       |
   +-----------------------------------------+-------+-----------------------------------------+
   | RESET pressed - restarting after the    | I     | Someone pressed **RESET** on a rack     |
   | power loss                              |       | waiting after a power loss              |
   +-----------------------------------------+-------+-----------------------------------------+
   | System reset (warm start)               | W     | **RESET** was pressed on a running      |
   |                                         |       | rack: all processors restart and the    |
   |                                         |       | start program is shown                  |
   +-----------------------------------------+-------+-----------------------------------------+
   | System board fitted                     | I     | A motherboard was fitted in the board   |
   |                                         |       | slot                                    |
   +-----------------------------------------+-------+-----------------------------------------+
   | System board removed - system halted    | E     | The board was removed; the rack cannot  |
   |                                         |       | run without it                          |
   +-----------------------------------------+-------+-----------------------------------------+

C.2 Temperature and cooling
---------------------------

.. _table-c-3:

.. table:: **Table C-3** Temperature and cooling messages

   +----------------------------------------+-------+-----------------------------------------+
   | Message                                | Level | Meaning                                 |
   +========================================+=======+=========================================+
   | Core temperature above *n* C           | W     | The core has passed the alarm           |
   |                                        |       | temperature                             |
   +----------------------------------------+-------+-----------------------------------------+
   | Core overheated - storage offline      | E     | The core has passed the trip            |
   |                                        |       | temperature; processors and automation  |
   |                                        |       | have stopped                            |
   +----------------------------------------+-------+-----------------------------------------+
   | Core cooled down - storage back online | I     | The core is 10 °C below the alarm       |
   |                                        |       | temperature again, and the rack has     |
   |                                        |       | recovered                               |
   +----------------------------------------+-------+-----------------------------------------+
   | Air filter clogged - pull and clean it | W     | The filter has fallen below 25 %        |
   | (service hatch)                        |       |                                         |
   +----------------------------------------+-------+-----------------------------------------+
   | Air filter pulled - fans stopped       | W     | The filter cartridge was pulled         |
   +----------------------------------------+-------+-----------------------------------------+
   | Air filter inserted (*n* %) - fans     | I     | The filter is back in, at the condition |
   | running                                |       | shown                                   |
   +----------------------------------------+-------+-----------------------------------------+
   | Air filter cleaned (*n* %)             | I     | **CLEAN** restored the filter to the    |
   |                                        |       | condition shown                         |
   +----------------------------------------+-------+-----------------------------------------+
   | New air filter element fitted          | I     | **NEW** restored the filter to 100 %    |
   +----------------------------------------+-------+-----------------------------------------+
   | A program executed HCF - the core      | E     | A processor ran ``hcf``, which heats    |
   | heated up                              |       | the core by 25 °C                       |
   +----------------------------------------+-------+-----------------------------------------+

C.3 Service bay
---------------

.. _table-c-4:

.. table:: **Table C-4** Service bay messages

   +-----------------------------------------+--------+-----------------------------------------+
   | Message                                 | Level  | Meaning                                 |
   +=========================================+========+=========================================+
   | Service hatch opened                    | I      | The rear controls are now accessible    |
   +-----------------------------------------+--------+-----------------------------------------+
   | Service hatch closed                    | I      | The rear controls no longer respond     |
   +-----------------------------------------+--------+-----------------------------------------+
   | UPS bypassed - no battery backup        | W      | **BYPASS** was switched on              |
   +-----------------------------------------+--------+-----------------------------------------+
   | UPS back in circuit                     | W      | **BYPASS** was switched off             |
   +-----------------------------------------+--------+-----------------------------------------+
   | Maintenance mode on - alarms and remote | W      | **MAINT** was switched on               |
   | control suspended                       |        |                                         |
   +-----------------------------------------+--------+-----------------------------------------+
   | Maintenance mode off                    | W      | **MAINT** was switched off              |
   +-----------------------------------------+--------+-----------------------------------------+
   | Battery reconditioning started - no     | W      | **BATT** was pressed                    |
   | backup for 60 seconds                   |        |                                         |
   +-----------------------------------------+--------+-----------------------------------------+
   | Battery reconditioned - health 100 %    | I      | Reconditioning finished                 |
   +-----------------------------------------+--------+-----------------------------------------+
   | Battery reconditioning aborted - no     | W      | Mains failed during reconditioning      |
   | mains power                             |        |                                         |
   +-----------------------------------------+--------+-----------------------------------------+
   | Self test: *result*                     | I or W | The result of **TEST**; I for a pass, W |
   |                                         |        | otherwise. The results are listed in    |
   |                                         |        | :ref:`Table 8-4 <table-8-4>`            |
   +-----------------------------------------+--------+-----------------------------------------+
   | Service counters reset                  | I      | **COUNT** reset the service hours and   |
   |                                         |        | the fault counter                       |
   +-----------------------------------------+--------+-----------------------------------------+
   | Settings reset to factory defaults      | W      | A factory reset was performed; the log  |
   |                                         |        | was cleared before this entry           |
   +-----------------------------------------+--------+-----------------------------------------+

C.4 Front panel
---------------

.. _table-c-5:

.. table:: **Table C-5** Front panel messages

   +----------------------------------------+-------+-----------------------------------------+
   | Message                                | Level | Meaning                                 |
   +========================================+=======+=========================================+
   | Monitor swung out - equipment bay open | I     | The monitor was swung out, exposing the |
   |                                        |       | board slot and **BIOS** button          |
   +----------------------------------------+-------+-----------------------------------------+
   | Monitor pushed back in                 | I     | The monitor was closed again            |
   +----------------------------------------+-------+-----------------------------------------+
   | Front panel locked                     | I     | The **LOCK** key switch was turned to   |
   |                                        |       | locked                                  |
   +----------------------------------------+-------+-----------------------------------------+
   | Front panel unlocked                   | I     | The **LOCK** key switch was turned to   |
   |                                        |       | unlocked                                |
   +----------------------------------------+-------+-----------------------------------------+
   | Write protection switched on           | W     | **WP** was switched on                  |
   +----------------------------------------+-------+-----------------------------------------+
   | Write protection switched off          | W     | **WP** was switched off                 |
   +----------------------------------------+-------+-----------------------------------------+
   | Alarm armed                            | W     | **ALRM** was switched on                |
   +----------------------------------------+-------+-----------------------------------------+
   | Alarm switched off                     | W     | **ALRM** was switched off; the rack     |
   |                                        |       | will not raise its alarm                |
   +----------------------------------------+-------+-----------------------------------------+
   | Remote control over the data network   | I     | **REM** was switched on                 |
   | allowed                                |       |                                         |
   +----------------------------------------+-------+-----------------------------------------+
   | Remote control over the data network   | I     | **REM** was switched off                |
   | blocked                                |       |                                         |
   +----------------------------------------+-------+-----------------------------------------+
   | Data logger on hold                    | I     | **HOLD** was switched on; logger        |
   |                                        |       | channels pause                          |
   +----------------------------------------+-------+-----------------------------------------+
   | Data logger released                   | I     | **HOLD** was switched off               |
   +----------------------------------------+-------+-----------------------------------------+
   | Drive bus A (bays 1-4) switched on     | I     | **BUS A** was switched on               |
   +----------------------------------------+-------+-----------------------------------------+
   | Drive bus A (bays 1-4) switched off    | W     | **BUS A** was switched off; bays 1 to 4 |
   |                                        |       | are not served                          |
   +----------------------------------------+-------+-----------------------------------------+
   | Drive bus B (bays 5-8) switched on     | I     | **BUS B** was switched on               |
   +----------------------------------------+-------+-----------------------------------------+
   | Drive bus B (bays 5-8) switched off    | W     | **BUS B** was switched off; bays 5 to 8 |
   |                                        |       | are not served                          |
   +----------------------------------------+-------+-----------------------------------------+

C.5 Storage
-----------

.. _table-c-6:

.. table:: **Table C-6** Storage messages

   +----------------------------------------+-------+---------------------------------------+
   | Message                                | Level | Meaning                               |
   +========================================+=======+=======================================+
   | Drive #\ *serial* inserted in bay *n*  | I     | A drive was put into a bay            |
   +----------------------------------------+-------+---------------------------------------+
   | Drive removed from bay *n*             | W     | A drive was taken out; any bank it    |
   |                                        |       | served now reads 0                    |
   +----------------------------------------+-------+---------------------------------------+
   | Bay *n* switched online                | I     | The bay was switched online, with its |
   |                                        |       | button or in the Disks program        |
   +----------------------------------------+-------+---------------------------------------+
   | Bay *n* switched offline               | I     | The bay was switched offline          |
   +----------------------------------------+-------+---------------------------------------+
   | Bank *n* write protected               | I     | The bank's write-protect switch was   |
   |                                        |       | switched on                           |
   +----------------------------------------+-------+---------------------------------------+
   | Bank *n* writable again                | I     | The bank's write-protect switch was   |
   |                                        |       | switched off                          |
   +----------------------------------------+-------+---------------------------------------+
   | Bay *n* patched to bank *n*            | I     | A patch cable now connects the bay to |
   |                                        |       | the bank                              |
   +----------------------------------------+-------+---------------------------------------+
   | Patch cable of bay *n* pulled          | I     | The bay's patch cable was pulled; its |
   |                                        |       | bank is not served                    |
   +----------------------------------------+-------+---------------------------------------+
   | Disk in bay *n* formatted              | W     | The drive was erased                  |
   +----------------------------------------+-------+---------------------------------------+
   | Disk in bay *n* copied to bay *n* (*n* | I     | A whole drive was copied to another   |
   | programs)                              |       |                                       |
   +----------------------------------------+-------+---------------------------------------+
   | Drive #\ *serial*: program slot *n*    | W     | A stored program was deleted from the |
   | cleared                                |       | drive                                 |
   +----------------------------------------+-------+---------------------------------------+
   | Patch field saved to drive *serial*    | I     | Pin patches, I/O ports and logger     |
   |                                        |       | devices were saved to the drive       |
   +----------------------------------------+-------+---------------------------------------+
   | Patch field loaded from drive *serial* | I     | They were loaded again                |
   +----------------------------------------+-------+---------------------------------------+
   | Automation saved to drive #\ *serial*  | I     | Rules, scenes and library tasks were  |
   |                                        |       | saved to the drive                    |
   +----------------------------------------+-------+---------------------------------------+
   | Automation loaded from drive #\        | I     | They were loaded again                |
   | *serial*                               |       |                                       |
   +----------------------------------------+-------+---------------------------------------+
   | Logger channel *n* started             | I     | The channel began recording           |
   +----------------------------------------+-------+---------------------------------------+
   | Logger channel *n* stopped             | I     | The channel stopped recording         |
   +----------------------------------------+-------+---------------------------------------+

C.6 Processors
--------------

.. _table-c-7:

.. table:: **Table C-7** Processor messages

   +---------------------------------------+-------+-----------------------------------------+
   | Message                               | Level | Meaning                                 |
   +=======================================+=======+=========================================+
   | Processor *n*: chip inserted          | I     | A chip was put into the socket          |
   +---------------------------------------+-------+-----------------------------------------+
   | Processor *n* running                 | I     | The processor was started               |
   +---------------------------------------+-------+-----------------------------------------+
   | Processor *n* halted                  | I     | The processor was stopped               |
   +---------------------------------------+-------+-----------------------------------------+
   | All processors halted                 | W     | **HALT ALL** was pressed                |
   +---------------------------------------+-------+-----------------------------------------+
   | Processor *n*: *error* line *n*       | E     | A runtime error stopped the processor;  |
   |                                       |       | the error type and line are given       |
   +---------------------------------------+-------+-----------------------------------------+
   | Processor *n*: Compile: *error* line  | E     | The program does not compile            |
   | *n*                                   |       |                                         |
   +---------------------------------------+-------+-----------------------------------------+
   | Processor *n*: restarted by the       | W     | **WDOG** restarted the processor 3 s    |
   | watchdog                              |       | after an error                          |
   +---------------------------------------+-------+-----------------------------------------+
   | Processor *n* paused: *reason*        | I     | The debugger paused the processor, for  |
   |                                       |       | example at a breakpoint                 |
   +---------------------------------------+-------+-----------------------------------------+
   | Processor *n*: program changed on the | I     | The Editor tab of the CPU program wrote |
   | rack (*n* lines)                      |       | a change to the chip                    |
   +---------------------------------------+-------+-----------------------------------------+
   | Processor *n*: "*title*" loaded from  | I     | A stored program was loaded into the    |
   | drive #\ *serial* slot *n*            |       | chip                                    |
   +---------------------------------------+-------+-----------------------------------------+
   | Processor *n*: program saved to drive | I     | The chip's program was stored on a      |
   | #\ *serial* slot *n*                  |       | drive                                   |
   +---------------------------------------+-------+-----------------------------------------+
   | Pin d\ *n* patched to I/O port *n*    | I     | The pin's cable now connects to that    |
   |                                       |       | port                                    |
   +---------------------------------------+-------+-----------------------------------------+
   | Patch cable of pin d\ *n* pulled      | I     | The pin's cable was pulled; the pin     |
   |                                       |       | reaches no device                       |
   +---------------------------------------+-------+-----------------------------------------+
   | Processors may write to the drives    | I     | **MEM WR** was switched on              |
   +---------------------------------------+-------+-----------------------------------------+
   | Processors may only read the drives   | I     | **MEM WR** was switched off             |
   +---------------------------------------+-------+-----------------------------------------+
   | Processor I/O enabled                 | I     | **I/O** was switched on                 |
   +---------------------------------------+-------+-----------------------------------------+
   | Processor I/O disabled - programs     | W     | **I/O** was switched off                |
   | cannot reach devices                  |       |                                         |
   +---------------------------------------+-------+-----------------------------------------+

C.7 Automation
--------------

.. _table-c-8:

.. table:: **Table C-8** Automation messages

   +-----------------------------------------+-------+----------------------------------------+
   | Message                                 | Level | Meaning                                |
   +=========================================+=======+========================================+
   | Rule *n*: IF *device* *value* *compare* | E     | A rule whose action is Raise alarm has |
   | *limit*                                 |       | become active. Rules with the compare  |
   |                                         |       | type always read ALWAYS *device*       |
   |                                         |       | *value* instead                        |
   +-----------------------------------------+-------+----------------------------------------+
   | Scene "*name*" recalled (*n* settings)  | I     | A scene was applied to the devices     |
   +-----------------------------------------+-------+----------------------------------------+
   | Scene "*name*" stored (*n* settings of  | I     | A scene was stored                     |
   | *n* devices)                            |       |                                        |
   +-----------------------------------------+-------+----------------------------------------+
   | *Library program* started               | I     | A library task was started             |
   +-----------------------------------------+-------+----------------------------------------+
   | *Library program* stopped               | I     | A library task was stopped             |
   +-----------------------------------------+-------+----------------------------------------+
   | Airlock cycling out                     | I     | The advanced airlock began a cycle     |
   |                                         |       | towards the outside                    |
   +-----------------------------------------+-------+----------------------------------------+
   | Airlock cycling in                      | I     | The advanced airlock began a cycle     |
   |                                         |       | towards the inside                     |
   +-----------------------------------------+-------+----------------------------------------+
   | Airlock gave up after *n* s at *n* kPa  | W     | The airlock reached its time limit and |
   |                                         |       | opened the far door anyway; see the    |
   |                                         |       | WARNING in :ref:`2.2.1 <sec-2-2-1>`    |
   +-----------------------------------------+-------+----------------------------------------+
   | Room alarm: pressure low (*sensor*)     | E     | The room alarm task found the pressure |
   |                                         |       | below its minimum. The same message    |
   |                                         |       | ends in pressure high, oxygen low or   |
   |                                         |       | too hot for the other limits           |
   +-----------------------------------------+-------+----------------------------------------+
   | Leak alarm: *sensor* lost *n* kPa       | E     | The leak alarm task saw the pressure   |
   |                                         |       | drop faster than its limit             |
   +-----------------------------------------+-------+----------------------------------------+
   | Tank guard: *tank* at *n* kPa,          | W     | The tank guard task opened the relief  |
   | releasing                               |       |                                        |
   +-----------------------------------------+-------+----------------------------------------+
   | Job: *n* x *item* on *printer*          | I     | A print job was queued                 |
   +-----------------------------------------+-------+----------------------------------------+
   | Job stopped: *item* on *printer*,       | W     | Someone changed the printer's recipe,  |
   | recipe changed by hand                  |       | so the rack stopped the job            |
   +-----------------------------------------+-------+----------------------------------------+

C.8 Setup utility and OS
------------------------

.. _table-c-9:

.. table:: **Table C-9** Setup utility and OS messages

   +-------------------------------------+-------+--------------------------------------+
   | Message                             | Level | Meaning                              |
   +=====================================+=======+======================================+
   | Setup utility started - storage and | W     | The **BIOS** button was pressed on a |
   | processors offline                  |       | running rack                         |
   +-------------------------------------+-------+--------------------------------------+
   | Setup utility will open at the next | I     | The **BIOS** button was pressed on a |
   | start                               |       | stopped rack                         |
   +-------------------------------------+-------+--------------------------------------+
   | Setup utility request cancelled     | I     | It was pressed again, cancelling the |
   |                                     |       | request                              |
   +-------------------------------------+-------+--------------------------------------+
   | Setup saved - system restarted      | I     | **F5** or **ESC** saved the settings |
   +-------------------------------------+-------+--------------------------------------+
   | OS update 5.12.7 started            | I     | The installer has begun              |
   +-------------------------------------+-------+--------------------------------------+
   | DS-8 OS *version* installed (was    | I     | The update is installed              |
   | *version*)                          |       |                                      |
   +-------------------------------------+-------+--------------------------------------+

C.9 The rack's own remarks
--------------------------

On about one start in three, and after every five running hours, the rack adds a remark of its own at level I. These need no action, though the last one is worth heeding.

.. _table-c-10:

.. table:: **Table C-10** Remarks

   +------------------+-----------------------------------------------------+
   | When             | Message                                             |
   +==================+=====================================================+
   | At a start       | Good morning. Coffee is not a supported peripheral. |
   +------------------+-----------------------------------------------------+
   | At a start       | Back online. Did anyone miss me?                    |
   +------------------+-----------------------------------------------------+
   | At a start       | Systems up. Please keep hands, feet and wrenches    |
   |                  | inside the station.                                 |
   +------------------+-----------------------------------------------------+
   | At a start       | Boot complete. The cable mess behind the monitor is |
   |                  | still there. It always will be.                     |
   +------------------+-----------------------------------------------------+
   | Every five hours | Another five hours without incident. Somebody write |
   |                  | that down.                                          |
   +------------------+-----------------------------------------------------+
   | Every five hours | Uptime milestone reached. No applause necessary.    |
   |                  | Some would be nice.                                 |
   +------------------+-----------------------------------------------------+
   | Every five hours | Still running. The drives send their regards.       |
   +------------------+-----------------------------------------------------+
   | Every five hours | Five more hours. The fans would like to point out   |
   |                  | they never get a day off.                           |
   +------------------+-----------------------------------------------------+
   | Every five hours | All systems nominal. Suspiciously nominal.          |
   +------------------+-----------------------------------------------------+
   | Every five hours | Self check complete: everything works, nobody said  |
   |                  | thank you.                                          |
   +------------------+-----------------------------------------------------+
   | Every five hours | Memory intact, core cool, operator presumably       |
   |                  | asleep.                                             |
   +------------------+-----------------------------------------------------+
   | Every five hours | Reminder: the air filter is not a decoration.       |
   +------------------+-----------------------------------------------------+
