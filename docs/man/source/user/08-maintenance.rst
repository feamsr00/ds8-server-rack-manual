.. _ch-maintenance:

8 Maintenance
=============
The DS-8 asks for very little: a clean air filter, a battery in reasonable health, and an OS update now and then. Everything needed for that is in the service bay at the back of the cabinet, which this chapter describes along with the procedures that use it. How power, heat and the UPS behave in normal operation is explained in :ref:`3 Installation and commissioning <ch-installation>`; this chapter is about keeping them that way.

8.1 Maintenance schedule
------------------------
The rack does not keep a calendar, so the schedule below is driven by what the rack tells you. The lamps, the service display and the event log will each say when something needs attention, usually well before it becomes urgent.

**Table 8-1** Maintenance schedule

+-------------------------------------+-----------------------------------------+-----+
| Task                                | When                                    | See |
+=====================================+=========================================+=====+
| Check the service display and run a | On every visit to the rack, and after   | 8.3 |
| self test                           | any alarm                               |     |
+-------------------------------------+-----------------------------------------+-----+
| Clean the air filter                | When the **AIR FILTER** lamp turns      | 8.4 |
|                                     | amber, and at the latest when the event |     |
|                                     | log reports a clogged filter. On Auto   |     |
|                                     | in normal air, that is roughly every    |     |
|                                     | 150 hours of running                    |     |
+-------------------------------------+-----------------------------------------+-----+
| Fit a new filter element            | When **FILTER MAX** on the Counters     | 8.4 |
|                                     | page has fallen to 60 %, which takes    |     |
|                                     | about ten cleanings                     |     |
+-------------------------------------+-----------------------------------------+-----+
| Recondition the UPS battery         | When the self test reports a worn       | 8.5 |
|                                     | battery (health below 80 %)             |     |
+-------------------------------------+-----------------------------------------+-----+
| Reset the service counters          | After each full service, so that the    | 8.6 |
|                                     | service hours count from that visit     |     |
+-------------------------------------+-----------------------------------------+-----+
| Install the OS update               | When the update screen appears after    | 8.8 |
|                                     | the mod has been updated                |     |
+-------------------------------------+-----------------------------------------+-----+

8.2 The service bay
-------------------
The service bay sits behind the **SERVICE** hatch at the back of the cabinet. Its controls respond only while the hatch is open, and the panel lock on the front does not affect them, so anyone who can reach the back of the rack can service it.

.. image:: /images/rack-back.png
   :alt: The back of the rack: a nameplate reading DATA SERVER DS-8, 230 V 16 A 900 W max, a barcode label, and the closed service hatch below

**Figure 8-1** The back of the cabinet with the service hatch closed. The nameplate's 900 W is the manufacturer's ambition rather than the rack's appetite; the real draw is given in 3.3.

.. image:: /images/service-bay.png
   :alt: The open service bay with the service display lit: DIP switches, BYPASS and MAINT toggles, PAGE, SAVER and TRIP + knobs, FAN, CUT and CAL sliders, seven buttons, and the AIR FILTER cartridge with its green lamp

**Figure 8-2** Inside the hatch: the service display at the top left, DIP switches 1 to 8 along the top, the toggles and knobs, the three sliders, the row of seven buttons, and the **AIR FILTER** cartridge along the bottom with its condition lamp at the right.

**Table 8-2** Service bay controls

+----------------+--------------+-------------------------+---------+-------------------------------------------+
| Control        | Type         | Positions               | Default | Function                                  |
+================+==============+=========================+=========+===========================================+
| **BYPASS**     | Toggle       | Off, On                 | Off     | Takes the UPS out of                      |
|                |              |                         |         | circuit: no battery                       |
|                |              |                         |         | backup and no charging                    |
+----------------+--------------+-------------------------+---------+-------------------------------------------+
| **MAINT**      | Toggle       | Off, On                 | Off     | Maintenance mode (see                     |
|                |              |                         |         | 8.7)                                      |
+----------------+--------------+-------------------------+---------+-------------------------------------------+
| **PAGE**       | Knob         | STA, THM, CPU, CNT      | STA     | Selects the page of the                   |
|                |              |                         |         | service display (see                      |
|                |              |                         |         | 8.3)                                      |
+----------------+--------------+-------------------------+---------+-------------------------------------------+
| **SAVER**      | Knob         | 1, 3, 5, 10 min         | 3 min   | Screen saver delay,                       |
|                |              |                         |         | while the **SAVR** DIP                    |
|                |              |                         |         | switch is on                              |
+----------------+--------------+-------------------------+---------+-------------------------------------------+
| **TRIP +**     | Knob         | +5, +10, +15, +20 °C    | +15 °C  | How far above the                         |
|                |              |                         |         | **TEMP ALARM** setting                    |
|                |              |                         |         | the core trips                            |
+----------------+--------------+-------------------------+---------+-------------------------------------------+
| **FAN**        | Slider       | 80, 90, 100, 115, 130 % | 100 %   | Trims the automatic fan                   |
|                |              |                         |         | curve                                     |
+----------------+--------------+-------------------------+---------+-------------------------------------------+
| **CUT**        | Slider       | 0, 10, 20, 30, 40 %     | 0 %     | Battery reserve that                      |
|                |              |                         |         | the UPS keeps back and                    |
|                |              |                         |         | never uses                                |
+----------------+--------------+-------------------------+---------+-------------------------------------------+
| **CAL**        | Slider       | −2 to +2 °C             | 0 °C    | Offset added to the                       |
|                |              |                         |         | core temperature sensor                   |
+----------------+--------------+-------------------------+---------+-------------------------------------------+
| **TEST**       | Button       | –                       | –       | Runs the self test (see                   |
|                |              |                         |         | 8.3)                                      |
+----------------+--------------+-------------------------+---------+-------------------------------------------+
| **FANS**       | Button       | –                       | –       | Runs the fans at full                     |
|                |              |                         |         | speed for 10 s (see                       |
|                |              |                         |         | 8.6)                                      |
+----------------+--------------+-------------------------+---------+-------------------------------------------+
| **BATT**       | Button       | –                       | –       | Reconditions the UPS                      |
|                |              |                         |         | battery (see 8.5)                         |
+----------------+--------------+-------------------------+---------+-------------------------------------------+
| **COUNT**      | Button       | –                       | –       | Resets the service                        |
|                |              |                         |         | hours and the fault                       |
|                |              |                         |         | counter (see 8.6)                         |
+----------------+--------------+-------------------------+---------+-------------------------------------------+
| **CLEAN**      | Button       | –                       | –       | Blows the pulled filter                   |
|                |              |                         |         | clean (see 8.4)                           |
+----------------+--------------+-------------------------+---------+-------------------------------------------+
| **NEW**        | Button       | –                       | –       | Fits a new filter                         |
|                |              |                         |         | element (see 8.4)                         |
+----------------+--------------+-------------------------+---------+-------------------------------------------+
| **RESET**      | Button       | –                       | –       | Factory reset, when                       |
|                |              |                         |         | pressed twice within 4                    |
|                |              |                         |         | s (see 8.9)                               |
+----------------+--------------+-------------------------+---------+-------------------------------------------+
| **AIR FILTER** | Cartridge    | In, Pulled              | In      | Pulling it stops the                      |
|                |              |                         |         | fans                                      |
+----------------+--------------+-------------------------+---------+-------------------------------------------+
| **DIP 1–8**    | DIP switches | Off, On                 | See 7.2 | Behaviour you seldom                      |
|                |              |                         |         | change; described in                      |
|                |              |                         |         | :ref:`7 Configuration <ch-configuration>` |
+----------------+--------------+-------------------------+---------+-------------------------------------------+

The **AIR FILTER** lamp is green while the filter is above 50 %, amber between 25 and 50 %, and red below 25 %; it flashes red while the filter is pulled. Changing any knob, slider or DIP switch in the bay also briefly shows the new setting on the service display, so you can confirm a change without counting detents.

8.3 Service display and self test
---------------------------------
The service display is a small monochrome screen at the top left of the bay. **PAGE** turns it through four pages, and the bottom line of every page is shared: it normally shows the fault count and whether **BUS A** and **BUS B** are on, but a running fan test or battery reconditioning shows its countdown there instead, a pulled filter shows FILTER OUT - CLEAN OR NEW, and any button you press leaves its reply there for a few seconds.

.. image:: /images/service-display.png
   :alt: The service display on page 1 of 4: serial and firmware, filter and battery bars, beep, eco and saver settings, faults and bus state

**Figure 8-3** The service display on page 1, Status.

**Table 8-3** Service display pages

+------+--------------+-----------------------------------------+
| Page | Title        | Shows                                   |
+======+==============+=========================================+
| 1    | DS-8 SERVICE | Serial number, firmware, and NORMAL or  |
|      |              | MAINT; the filter condition (or OUT);   |
|      |              | the UPS charge, marked BYP while        |
|      |              | bypassed or RCN while reconditioning;   |
|      |              | and the **BEEP**, **ECO** and **SAVR**  |
|      |              | DIP settings                            |
+------+--------------+-----------------------------------------+
| 2    | THERMAL      | Core temperature and the **CAL**        |
|      |              | offset; the alarm and trip              |
|      |              | temperatures; fan speed, marked TEST    |
|      |              | during a fan test; and the filter       |
|      |              | condition                               |
+------+--------------+-----------------------------------------+
| 3    | PROCESSORS   | The state of all twelve processors      |
|      |              | (----, HALT, RUN, ERR, CODE or STEP);   |
|      |              | the clock rate and whether **DEBUG** is |
|      |              | on; and the **AUTO** and **WDOG** DIP   |
|      |              | settings                                |
+------+--------------+-----------------------------------------+
| 4    | COUNTERS     | Running hours and service hours; reads, |
|      |              | writes and faults; battery health; and  |
|      |              | **FILTER MAX**, the most a cleaning can |
|      |              | restore                                 |
+------+--------------+-----------------------------------------+

The self test checks the rack in a fixed order and reports the first problem it finds, so a rack with two faults will need two tests to reveal both. It takes 4 s, shows its result on the service display for 15 s, and records it in the event log as information if it passed and as a warning otherwise.

**Table 8-4** Self test results, in the order they are checked

+----------------------------+-----------------------------------------------------+
| Result                     | Meaning                                             |
+============================+=====================================================+
| FAIL: CORE OVERHEATED      | The rack has tripped and is waiting to cool down    |
+----------------------------+-----------------------------------------------------+
| FAIL: AIR FILTER REMOVED   | The filter is pulled, so the fans are stopped       |
+----------------------------+-----------------------------------------------------+
| FAIL: AIR FILTER CLOGGED   | The filter is below 25 %                            |
+----------------------------+-----------------------------------------------------+
| FAIL: PROCESSOR *n* ERROR  | Processor *n* has stopped with a runtime or compile |
|                            | error                                               |
+----------------------------+-----------------------------------------------------+
| WARN: CORE TEMPERATURE     | The core is at or above the alarm temperature       |
+----------------------------+-----------------------------------------------------+
| WARN: BATTERY WORN *nn*\ % | Battery health is below 80 %                        |
+----------------------------+-----------------------------------------------------+
| WARN: BATTERY LOW          | The UPS charge is below 25 %                        |
+----------------------------+-----------------------------------------------------+
| WARN: UPS BYPASSED         | **BYPASS** is on                                    |
+----------------------------+-----------------------------------------------------+
| WARN: NO MAINS CABLE       | No power cable is connected to the rack             |
+----------------------------+-----------------------------------------------------+
| PASS *n* DRIVES ALL OK     | Nothing to report; *n* is the number of drives      |
|                            | fitted                                              |
+----------------------------+-----------------------------------------------------+

8.3.1 Running a self test
^^^^^^^^^^^^^^^^^^^^^^^^^
**Requirements:** The rack should be switched on, and the service hatch must be open.

1. Set **PAGE** to STA if you want to watch the summary while the test runs.
2. Press **TEST**. The display shows SELF TEST RUNNING for 4 s.
3. Read the result on the bottom line, and act on it using Table 8-4.
4. If the result was a FAIL or WARN, fix the cause and test again until the rack passes.

**Result:** The service display shows PASS with the number of drives fitted, and the event log records the result.

8.4 Air filter
--------------
The filter wears only while the rack is running with the filter in. A new filter lasts 200 hours of real time with the fans on Auto in normal air, which you can change with the server setting ``FilterLifeHoursV2``. Everything that makes the fans work harder, or the air dirtier, shortens that time.

**Table 8-5** Filter wear relative to Auto fans in normal air

+----------------------------+----------------+
| Condition                  | Wear           |
+============================+================+
| Fans on Low                | 0.6 ×          |
+----------------------------+----------------+
| Fans on High               | 1.8 ×          |
+----------------------------+----------------+
| Fan test running           | 2 ×            |
+----------------------------+----------------+
| Dusty or polluted air      | Up to 6 ×      |
+----------------------------+----------------+
| Pressure above 1 atm       | Up to 1.5 ×    |
+----------------------------+----------------+
| Clean, breathable base air | 0.25 ×         |
+----------------------------+----------------+
| Thin air                   | Down to 0.1 ×  |
+----------------------------+----------------+
| Below 1 kPa                | No wear at all |
+----------------------------+----------------+

The BIOS setting **Fan idle floor** keeps the fans above idle and so adds to the wear as well. When the filter falls below 25 %, the event log asks you to pull it and clean it, and from then on it cools the core noticeably less well; a fully clogged filter roughly halves the cooling.

8.4.1 Cleaning or replacing the air filter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Requirements:** The service hatch must be open. The rack should be running, so that the filter condition is shown.

.. attention::

	**CAUTION:** Pulling the filter stops the fans, and the core will start to overheat. Be sure to refit the filter within a few minutes. In vacuum or in a hot room, do the job as quickly as you can, or switch the rack off first.

1. Note the filter condition on the service display, or the colour of the **AIR FILTER** lamp.
2. Pull the **AIR FILTER** cartridge. The fans stop, the lamp flashes red and the alarm sounds.
3. Press **CLEAN** to blow the filter clean, or **NEW** to fit a fresh element. Cleaning the filter restores it to its maximum, which drops 4 % with each cleaning (however, never below 60 %). Selecting **NEW** restores filter capacity to 100 %.
4. Push the filter back in. The fans start again, and the service display shows FILTER IN with the new condition.

**Result:** The **AIR FILTER** lamp is green, the alarm stops, and the event log records the cleaning or the new element.

Both **CLEAN** and **NEW** refuse to work while the filter is still in the rack and say PULL THE FILTER FIRST, which is the rack's way of reminding you that it is not a dishwasher.

8.5 UPS battery
---------------
The UPS battery loses about 1 % of its health with each full discharge, but never falls below 50 %, and the usable capacity of the UPS falls along with it. A rack that rides out power cuts regularly will therefore slowly lose runtime. Reconditioning brings the health back to 100 %; it takes 60 s, needs mains power, and leaves the rack without any backup for that minute. How the UPS behaves during a power cut is explained in 3.3.

8.5.1 Reconditioning the UPS battery
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Requirements:** Mains power must be present, **BYPASS** must be off, and the service hatch must be open. Choose a moment when a short power cut would not matter.

.. attention::

	**CAUTION:** For the 60 s that reconditioning takes, the UPS cannot take over. If mains fails during that minute, the rack goes down at once, along with anything it controls, and the reconditioning is aborted. Do not recondition while the base's power supply is unreliable.

1. Check battery health on the Counters page of the service display (**PAGE** to CNT).
2. Press **BATT**. The service display shows RECONDITION 60 S  NO BACKUP, then counts down on its bottom line.
3. Wait for the countdown to finish. Do not switch off the rack or mains in the meantime.

**Result:** The service display shows BATTERY HEALTH 100%, and the event log records the reconditioning. If mains was lost during the minute, the display shows RECONDITION ABORTED instead; restore power and start again.

If **BATT** answers UPS IS BYPASSED or NEEDS MAINS POWER, it has not started, and the reason is as stated.

8.6 Fan test and service counters
---------------------------------
**FANS** runs the fans at full speed for 10 s, which draws 75 W and is useful to confirm that the fans work after fitting a filter, or to take a few degrees off a warm core in a hurry. It needs the rack to be running and the filter to be in; otherwise it answers NO POWER or FILTER OUT - FANS LOCKED.

**COUNT** resets the service hours and the fault counter to zero, and records that in the event log. The running hours, the read and write counters and the battery health are not affected. Pressing it at the end of every service turns the service hours into a simple "time since last service" meter.

8.7 Maintenance mode
--------------------
**MAINT** is meant for the time you spend working on the rack. While it is on, the alarm stays silent, and writes from outside the rack to its ``Mode``, ``Lock``, ``Setting``, ``Index``, ``LineNumber`` and ``ClearMemory`` logic values are refused, so nothing on the network can switch the screen or the write protection while you work. Storage, processors and automation keep running as normal. The **MAINT** lamp and the amber lamp of the beacon flash for as long as maintenance mode is on, and the service display shows MAINT on its first page.

.. attention::

	**CAUTION:** Maintenance mode suppresses every alarm, including the overheat alarm. Switch **MAINT** off before you close the service hatch, or the rack will overheat in silence the next time something goes wrong.

8.8 OS updates
--------------
When the mod is updated, every rack still running an older DS-8 OS shows an update screen in place of its programs. Until the update is installed, the keys drive only the installer, but storage, processors and automation keep running, so there is no hurry. The installer, unlike some, will wait patiently for as long as you like.

8.8.1 Installing an OS update
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Requirements:** The rack must be running, must not be overheated, and must have a system board fitted.

1. Read the update screen, which lists what the new version changes.
2. Press **ENT** to install on this rack, or **F2** to install on every rack in the world at once.
3. Wait a few seconds while the progress bar fills and the rack restarts.

**Result:** The rack runs the new DS-8 OS, a window lists what was installed, and the event log records the new version and the one it replaced. Drives, programs and rules are kept.

8.9 Factory reset
-----------------
A factory reset returns the rack's settings to the state it left the factory in. It is the right tool when a rack has been configured into a corner and nobody remembers how; it is the wrong tool for anything else.

**Table 8-6** What a factory reset changes

+---------------------------------------------------+-----------------------------------------------------+
| Reset to default or cleared                       | Kept                                                |
+===================================================+=====================================================+
| Every switch, knob, slider and DIP switch, except | Drives and their contents, including programs on    |
| the filter and the hatch                          | drives                                              |
+---------------------------------------------------+-----------------------------------------------------+
| All BIOS settings                                 | The chips in the processor sockets                  |
+---------------------------------------------------+-----------------------------------------------------+
| All 32 I/O ports, so every pin loses its device   | Patch cables and pin cables, where they are         |
+---------------------------------------------------+-----------------------------------------------------+
| Bank write protection, the **WP** toggle,         | Rules, scenes and library tasks                     |
| **BYPASS**, and **BUS A** and **BUS B** (back on) |                                                     |
+---------------------------------------------------+-----------------------------------------------------+
| Logger channels, memory bookmarks and the scratch | Filter condition, battery health and the UPS charge |
| cells                                             |                                                     |
+---------------------------------------------------+-----------------------------------------------------+
| The read, write and fault counters, and the event | The OS version and the running hours                |
| log                                               |                                                     |
+---------------------------------------------------+-----------------------------------------------------+

Defaults for everything in the left-hand column are listed in :ref:`B Factory defaults <app-b>`.

8.9.1 Performing a factory reset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Requirements:** The service hatch must be open. Note down any settings, I/O port assignments and logger channels you want to set up again afterwards.

.. note::

	**NOTICE:** A factory reset switches off write protection on every bank, empties every I/O port and clears the event log. Programs that rely on their pins will find no devices until the ports are assigned again, and the banks are unprotected until you protect them again.

1. Press **RESET** in the service bay. The service display shows RESET: PRESS AGAIN.
2. Press **RESET** again within 4 s.

**Result:** The service display shows FACTORY DEFAULTS LOADED, and the event log, otherwise empty, holds a single warning that the settings were reset. Assign the I/O ports again in the Network program (:ref:`5.12 Network <os-network>`), and protect the banks you care about.

The second press is the rack asking whether you are sure, without the indignity of a dialog box. If four seconds pass, it assumes you were not.

8.10 After maintenance
----------------------
Before you close the hatch, make sure the filter is in, **MAINT** and **BYPASS** are off, and a final self test passes; then press **COUNT** if this was a full service. Every message mentioned in this chapter is listed with its meaning in :ref:`C Event messages <app-c>`, and the Events program that shows them is described in :ref:`5.8 Events <os-events>`. If something still does not behave, continue with :ref:`9 Diagnostics and troubleshooting <ch-diagnostics>`; the safety notices for servicing are collected in :ref:`2 Safety <security_warning>`.
