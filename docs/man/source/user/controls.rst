.. _ch-controls:

4 Controls and indicators
=========================

.. index::
   single: Controls and indicators

Every switch, knob, key and lamp on the front of the cabinet is described in this chapter, area by area from the top down. All 157 controls are real controls that you click, and pointing at any of them shows its name and its current setting. The service bay and the expansion chassis at the back are covered in :ref:`8 Maintenance <ch-maintenance>` and :ref:`11 Programming (IC10) <ch-programming>`.

4.1 Front panel overview
------------------------

.. index::
   single: Front panel overview

.. _figure-4-1:

.. figure:: /images/fig-front-panel.png
   :alt: Patch field on top, screen and keys in the middle, drives and power below
   :width: 100%

   **Figure 4-1** The front panel, top to bottom

Read the panel from the top down. The patch field and the panel switches sit above eye level, the monitor and key pad are in the middle, and the processors, drives, UPS and power switches are nearer the floor. Guarded controls, marked with a red ring in the figure, sit under a flip-up cover so that they cannot be pressed by accident.

.. _figure-4-2:

.. figure:: /images/top-of-cabinet.png
   :alt: The top of a DS-8 rack: alarm beacon at the left, the DATA SERVER DS-8 nameplate, and the patch field below it
   :width: 100%

   **Figure 4-2** The top of the cabinet: the alarm beacon (left), the nameplate, and the patch field with its fourteen cables.

4.2 Operating the controls
--------------------------

.. index::
   single: Operating the controls

The controls follow a few simple rules, and knowing them saves a good deal of puzzled clicking.

- **Knobs and sliders** step up by one position per click. Hold the quantity modifier key while clicking to step back down; on-screen hints call this key SHIFT.
- **The 64-key pad** sits behind a glass cover, which must be open before the keys respond. The F1–F5 soft keys under the monitor are always reachable. You can also hold **Alt** and click the screen itself to use it as a touch screen, and the mouse wheel scrolls.
- **The LOCK key switch** turns only while you hold the rack key in your hand, unless the server's ``KeyRequired`` setting is off. A locked panel ignores every front control except the key cover, the monitor, its lock pin, the **BIOS** button and the key switch itself.
- **Rear controls** respond only while the service hatch is open. The panel lock does not affect them.
- **When the rack is overheated or switched off,** keys do nothing, although switches still move.
- **While the screen saver runs,** the first key you press only wakes the screen.

4.3 Patch field
---------------

.. index::
   single: Patch field

The patch field across the top of the cabinet connects drive bays to memory banks and processor pins to I/O ports. How to use it is explained in :ref:`6 Storage and data handling <ch-storage>`; this table lists its parts.

.. _table-4-1:

.. table:: **Table 4-1** Patch field

   +--------------------+--------------+--------------------+-------------------------+-------------------------+
   | Control            | Type         | Positions          | Default                 | Function                |
   +====================+==============+====================+=========================+=========================+
   | Bank write-protect | Slide switch | Off, on            | Off                     | Protect one memory bank |
   | switches (8)       |              |                    |                         | each against writes     |
   +--------------------+--------------+--------------------+-------------------------+-------------------------+
   | Bay cables (8)     | Patch cable  | Bank ports 0–7, or | Bay *n* on bank *n* − 1 | Decide which drive      |
   |                    |              | pulled             |                         | serves which bank       |
   +--------------------+--------------+--------------------+-------------------------+-------------------------+
   | Pin cables (6)     | Patch cable  | I/O ports 1–8, or  | Pin d\ *n* on port *n*  | Decide which I/O port   |
   |                    |              | pulled             | + 1                     | each processor pin      |
   |                    |              |                    |                         | reaches                 |
   +--------------------+--------------+--------------------+-------------------------+-------------------------+

4.4 Switch strip
----------------

.. index::
   single: Switch strip

The switch strip holds the panel's on/off preferences, two knobs for the screen, the system **RESET** button and the five status lamps.

.. _figure-4-3:

.. figure:: /images/switch-strip.png
   :alt: The switch strip with eight toggles, THEME, SAMPLE and RESET, and below it the control row from LOCK to the three sliders
   :width: 100%

   **Figure 4-3** From the top: the lower patch-field row, the switch strip with the status lamps at the right, and the control row with **FORMAT** under its red guard.

.. index::
   single: DISP
   single: LCD
   single: LAMP
   single: ALRM
   single: BEEP
   single: REM
   single: HOLD
   single: THEME
   single: SAMPLE
   single: RESET

.. _table-4-2:

.. table:: **Table 4-2** Switch strip

   +-------------------------+--------+------------------------+---------+-------------------------+
   | Control                 | Type   | Positions              | Default | Function                |
   +=========================+========+========================+=========+=========================+
   | **DISP**                | Toggle | Off, on                | On      | Monitor power           |
   +-------------------------+--------+------------------------+---------+-------------------------+
   | **LCD**                 | Toggle | Off, on                | On      | Status display power    |
   +-------------------------+--------+------------------------+---------+-------------------------+
   | **LAMP**                | Toggle | Off, on                | On      | Panel lamps; off        |
   |                         |        |                        |         | darkens every lamp on   |
   |                         |        |                        |         | the cabinet             |
   +-------------------------+--------+------------------------+---------+-------------------------+
   | **ALRM**                | Toggle | Off, on                | On      | Arms the alarm          |
   +-------------------------+--------+------------------------+---------+-------------------------+
   | **BEEP**                | Toggle | Off, on                | On      | Key click               |
   +-------------------------+--------+------------------------+---------+-------------------------+
   | **REM**                 | Toggle | Off, on                | On      | Allows remote control   |
   |                         |        |                        |         | over the data network   |
   +-------------------------+--------+------------------------+---------+-------------------------+
   | **C/K**                 | Toggle | Off, on                | Off     | Shows temperatures in   |
   |                         |        |                        |         | kelvin instead of       |
   |                         |        |                        |         | Celsius                 |
   +-------------------------+--------+------------------------+---------+-------------------------+
   | **HOLD**                | Toggle | Off, on                | Off     | Pauses every logger     |
   |                         |        |                        |         | channel                 |
   +-------------------------+--------+------------------------+---------+-------------------------+
   | **THEME**               | Knob   | XP, OLV, SLV, CLS, MID | XP      | Colour scheme of the    |
   |                         |        |                        |         | screen                  |
   +-------------------------+--------+------------------------+---------+-------------------------+
   | **SAMPLE**              | Knob   | 1, 2, 5, 10 s          | 2 s     | Sample time of the      |
   |                         |        |                        |         | performance graphs      |
   +-------------------------+--------+------------------------+---------+-------------------------+
   | **RESET**               | Button | —                      | —       | Restarts the system;    |
   |                         |        |                        |         | also restarts a rack    |
   |                         |        |                        |         | that is waiting after a |
   |                         |        |                        |         | power loss or an        |
   |                         |        |                        |         | overheat                |
   +-------------------------+--------+------------------------+---------+-------------------------+
   | **PWR NET ACT TMP ERR** | Lamps  | —                      | —       | Status lamps (see       |
   |                         |        |                        |         | :ref:`4.12 <sec-4-12>`) |
   +-------------------------+--------+------------------------+---------+-------------------------+

4.5 Control row
---------------

.. index::
   single: Control row

The control row carries the controls you are most likely to reach for during normal operation: the panel lock, the fans, the alarm temperature and write protection.

.. index::
   single: LOCK
   single: FAN
   single: DISPLAY
   single: TEMP ALARM
   single: WP
   single: FORMAT
   single: MUTE
   single: LAMP
   single: BRT
   single: VOL
   single: FAN%

.. _table-4-3:

.. table:: **Table 4-3** Control row

   +----------------+----------------+-------------------------+----------+-------------------------+
   | Control        | Type           | Positions               | Default  | Function                |
   +================+================+=========================+==========+=========================+
   | **LOCK**       | Key switch     | Unlocked, locked        | Unlocked | Locks the front panel;  |
   |                |                |                         |          | turns only with the     |
   |                |                |                         |          | rack key in hand        |
   +----------------+----------------+-------------------------+----------+-------------------------+
   | **FAN**        | Knob           | AUT, LO, HI, MAN        | AUT      | Fan mode                |
   +----------------+----------------+-------------------------+----------+-------------------------+
   | **DISPLAY**    | Knob           | AUT, PWR, STO, NET, CLK | AUT      | Page shown on the       |
   |                |                |                         |          | status display; AUT     |
   |                |                |                         |          | rotates through them    |
   +----------------+----------------+-------------------------+----------+-------------------------+
   | **TEMP ALARM** | Knob           | 60, 65, 70, 75, 80 °C   | 70 °C    | Alarm temperature; the  |
   |                |                |                         |          | trip point sits **TRIP  |
   |                |                |                         |          | +** above it            |
   +----------------+----------------+-------------------------+----------+-------------------------+
   | **WP**         | Toggle         | Off, on                 | Off      | Write protection for    |
   |                |                |                         |          | every bank              |
   +----------------+----------------+-------------------------+----------+-------------------------+
   | **FORMAT**     | Guarded button | —                       | —        | Formats the drive       |
   |                |                |                         |          | selected in Disks or,   |
   |                |                |                         |          | from any other program, |
   |                |                |                         |          | the drive serving the   |
   |                |                |                         |          | cursor's bank; always   |
   |                |                |                         |          | asks first              |
   +----------------+----------------+-------------------------+----------+-------------------------+
   | **MUTE**       | Button         | —                       | —        | Silences the alarm      |
   |                |                |                         |          | until its cause clears  |
   +----------------+----------------+-------------------------+----------+-------------------------+
   | **LAMP**       | Button         | —                       | —        | Lamp test: lights every |
   |                |                |                         |          | lamp at once            |
   +----------------+----------------+-------------------------+----------+-------------------------+
   | **BRT**        | Slider         | 5 positions             | 4th      | Screen brightness       |
   +----------------+----------------+-------------------------+----------+-------------------------+
   | **VOL**        | Slider         | 5 positions             | 4th      | Beeper volume           |
   +----------------+----------------+-------------------------+----------+-------------------------+
   | **FAN%**       | Slider         | 11 positions            | Middle   | Fan speed while **FAN** |
   |                |                |                         |          | is on MAN, from 4 W to  |
   |                |                |                         |          | 74 W                    |
   +----------------+----------------+-------------------------+----------+-------------------------+

Note that the **LAMP** toggle on the switch strip and the **LAMP** button on the control row are two different controls: the toggle switches the panel lamps on and off, while the button only tests them.

4.6 Monitor and key pad
-----------------------

.. index::
   single: Monitor and key pad

The monitor shows DS-8 OS, and the key pad to its right drives it. The monitor also doubles as a door: pull the lock pin above it and it swings out to reveal the system board and the **BIOS** button.

.. _figure-4-4:

.. figure:: /images/monitor-keypad.png
   :alt: The monitor with its lock pin and F1 to F5, the empty status display, and the key pad with its glass cover swung open
   :width: 100%

   **Figure 4-4** The monitor with its soft keys, and the key pad with its glass cover open.

.. index::
   single: BIOS

.. _table-4-4:

.. table:: **Table 4-4** Monitor and key pad

   +---------------+--------------------+--------------+---------+--------------------------------------------+
   | Control       | Type               | Positions    | Default | Function                                   |
   +===============+====================+==============+=========+============================================+
   | Monitor       | Swing-out door     | Closed, open | Closed  | Opens to reach the                         |
   |               |                    |              |         | system board and the                       |
   |               |                    |              |         | **BIOS** button; the                       |
   |               |                    |              |         | lock pin must be pulled                    |
   |               |                    |              |         | first                                      |
   +---------------+--------------------+--------------+---------+--------------------------------------------+
   | Lock pin      | Pin                | In, pulled   | In      | Holds the monitor shut                     |
   +---------------+--------------------+--------------+---------+--------------------------------------------+
   | **F1**–**F5** | Soft keys          | —            | —       | Perform the functions                      |
   |               |                    |              |         | labelled on the screen                     |
   |               |                    |              |         | above them                                 |
   +---------------+--------------------+--------------+---------+--------------------------------------------+
   | Key cover     | Glass lid          | Closed, open | Closed  | Must be open for the                       |
   |               |                    |              |         | key pad to respond                         |
   +---------------+--------------------+--------------+---------+--------------------------------------------+
   | Key pad       | 64 keys            | —            | —       | Layout in                                  |
   |               |                    |              |         | :ref:`Table 4-5 <table-4-5>`               |
   +---------------+--------------------+--------------+---------+--------------------------------------------+
   | **BIOS**      | Button, behind the | —            | —       | Starts the setup                           |
   |               | monitor            |              |         | utility (see                               |
   |               |                    |              |         | :ref:`7 Configuration <ch-configuration>`) |
   +---------------+--------------------+--------------+---------+--------------------------------------------+

.. _table-4-5:

.. table:: **Table 4-5** Key pad layout

   +-------+------+------+------+-----+------+------+------+------+
   |       | 1    | 2    | 3    | 4   | 5    | 6    | 7    | 8    |
   +=======+======+======+======+=====+======+======+======+======+
   | Row 1 | HOME | <<   | >>   | SYS | DSK  | EDT  | PRF  | NET  |
   +-------+------+------+------+-----+------+------+------+------+
   | Row 2 | LOG  | EVT  | HELP | ESC | TAB  | PG+  | PG-  | CLR  |
   +-------+------+------+------+-----+------+------+------+------+
   | Row 3 | BM1  | BM2  | BM3  | BM4 | REC1 | REC2 | REC3 | REC4 |
   +-------+------+------+------+-----+------+------+------+------+
   | Row 4 | 7    | 8    | 9    | DEL | CPY  | UP   | PST  | INC  |
   +-------+------+------+------+-----+------+------+------+------+
   | Row 5 | 4    | 5    | 6    | +/- | <    | DN   | >    | DEC  |
   +-------+------+------+------+-----+------+------+------+------+
   | Row 6 | 1    | 2    | 3    | .   | GOTO | FIND | ZERO | FILL |
   +-------+------+------+------+-----+------+------+------+------+
   | Row 7 | 0    | 00   | EXP  | ENT | BAY- | BAY+ | BNK- | BNK+ |
   +-------+------+------+------+-----+------+------+------+------+
   | Row 8 | BAY  | CPYD | OPEN | FMT | CPU  | RSIO | CLEV | SLP  |
   +-------+------+------+------+-----+------+------+------+------+

The keys are colour-coded. The blue keys jump straight to a program, the red ones are **ESC** and the logger's **REC1**–**REC4**, **ENT** is green, and the digits are grey. What each key does is explained in :ref:`5 DS-8 OS <ch-os>`.

4.7 Processor unit
------------------

.. index::
   single: Processor unit

The processor unit holds the sockets for processors 1–4 and the switches that govern how all twelve processors run.

.. _figure-4-5:

.. figure:: /images/processor-unit.png
   :alt: The processor unit with four sockets, RUN toggles and RST buttons, the PROG and CLOCK knobs, STEP, guarded HALT ALL and four toggles, above the eight drive bays
   :width: 100%

   **Figure 4-5** The processor unit above the drive bays. The tooltip shows what pointing at the rack tells you: its state, temperature, draw, UPS charge, and the drives and cells in use.

.. index::
   single: RUN
   single: RST
   single: PROG
   single: CLOCK
   single: STEP
   single: HALT ALL
   single: DEBUG
   single: MEM WR
   single: TURBO

.. _table-4-6:

.. table:: **Table 4-6** Processor unit

   +--------------+----------------+------------------+---------+-------------------------+
   | Control      | Type           | Positions        | Default | Function                |
   +==============+================+==================+=========+=========================+
   | **RUN** 1–4  | Toggle         | Halt, run        | Run     | Runs or halts           |
   |              |                |                  |         | processors 1–4          |
   +--------------+----------------+------------------+---------+-------------------------+
   | **RST** 1–4  | Button         | —                | —       | Resets processors 1–4   |
   +--------------+----------------+------------------+---------+-------------------------+
   | **PROG**     | Knob           | 1–4              | 1       | Selects the front       |
   |              |                |                  |         | processor that a        |
   |              |                |                  |         | computer's IC editor on |
   |              |                |                  |         | the network reads and   |
   |              |                |                  |         | writes, and that        |
   |              |                |                  |         | ``LineNumber`` reports  |
   +--------------+----------------+------------------+---------+-------------------------+
   | **CLOCK**    | Knob           | LO, MED, HI, MAX | HI      | 32, 64, 128 or 256      |
   |              |                |                  |         | lines per game tick for |
   |              |                |                  |         | every processor         |
   +--------------+----------------+------------------+---------+-------------------------+
   | **STEP**     | Button         | —                | —       | With **DEBUG** on,      |
   |              |                |                  |         | advances every          |
   |              |                |                  |         | processor by one line,  |
   |              |                |                  |         | or ten with the         |
   |              |                |                  |         | modifier                |
   +--------------+----------------+------------------+---------+-------------------------+
   | **HALT ALL** | Guarded button | —                | —       | Halts all twelve        |
   |              |                |                  |         | processors              |
   +--------------+----------------+------------------+---------+-------------------------+
   | **DEBUG**    | Toggle         | Off, on          | Off     | Single-step mode:       |
   |              |                |                  |         | processors advance only |
   |              |                |                  |         | with **STEP**           |
   +--------------+----------------+------------------+---------+-------------------------+
   | **MEM WR**   | Toggle         | Off, on          | On      | Lets the rack's own     |
   |              |                |                  |         | processors write to its |
   |              |                |                  |         | drives                  |
   +--------------+----------------+------------------+---------+-------------------------+
   | **TURBO**    | Toggle         | Off, on          | Off     | Doubles the clock, and  |
   |              |                |                  |         | the processor power     |
   |              |                |                  |         | with it                 |
   +--------------+----------------+------------------+---------+-------------------------+
   | **I/O**      | Toggle         | Off, on          | On      | Lets programs reach     |
   |              |                |                  |         | devices                 |
   +--------------+----------------+------------------+---------+-------------------------+

How these switches affect a running program is explained in :ref:`11 Programming (IC10) <ch-programming>`.

4.8 Drive bays
--------------

.. index::
   single: Drive bays

Each of the eight drive bays has a power button that takes it online or offline, and a lamp that shows whether its drive is being served. A bay only serves memory when its bus is on, it is online, a drive is fitted and its patch cable is plugged in (see :ref:`6 Storage and data handling <ch-storage>`).

.. _table-4-7:

.. table:: **Table 4-7** Drive bays

   +-----------------+--------+-----------------+---------+-----------------------------+
   | Control         | Type   | Positions       | Default | Function                    |
   +=================+========+=================+=========+=============================+
   | Bay buttons 1–8 | Button | Online, offline | Online  | Take a bay online or        |
   |                 |        |                 |         | offline; F1 in              |
   |                 |        |                 |         | :ref:`5.9 Disks <os-disks>` |
   |                 |        |                 |         | does the same               |
   +-----------------+--------+-----------------+---------+-----------------------------+
   | Bay lamps 1–8   | Lamp   | —               | —       | Show whether the bay is     |
   |                 |        |                 |         | served (see                 |
   |                 |        |                 |         | :ref:`4.12 <sec-4-12>`)     |
   +-----------------+--------+-----------------+---------+-----------------------------+

4.9 UPS panel
-------------

.. index::
   single: UPS panel

The UPS panel shows how much power the rack draws and how much it has in reserve. It also hides the battery compartment, behind the panel that carries the **LOAD** and **BATT** lamps.

.. _figure-4-6:

.. figure:: /images/ups-panel.png
   :alt: The UPS panel with the CHARGE slider, LOAD and METER gauges, SELECT knob and TEST button, the LOAD and BATT lamp rows, and below it MAIN POWER, BUS A, BUS B and the PDU outlets
   :width: 100%

   **Figure 4-6** The UPS panel (top) and the bottom row, with **MAIN POWER** in its yellow frame, the PDU lamp, **BUS A**, **BUS B** and the five PDU outlets.

.. index::
   single: CHARGE
   single: LOAD
   single: METER
   single: SELECT
   single: TEST
   single: BATT

.. _table-4-8:

.. table:: **Table 4-8** UPS panel

   +-----------------------+--------------+-------------------------+---------+-------------------------+
   | Control               | Type         | Positions               | Default | Function                |
   +=======================+==============+=========================+=========+=========================+
   | **CHARGE**            | Slider       | 25, 50, 100, 150, 200 % | 100 %   | UPS charging power, as  |
   |                       |              |                         |         | a share of 100 W        |
   +-----------------------+--------------+-------------------------+---------+-------------------------+
   | **LOAD**              | Gauge        | —                       | —       | Power draw, against the |
   |                       |              |                         |         | rack's maximum          |
   +-----------------------+--------------+-------------------------+---------+-------------------------+
   | **METER**             | Gauge        | —                       | —       | Shows the value picked  |
   |                       |              |                         |         | with **SELECT**         |
   +-----------------------+--------------+-------------------------+---------+-------------------------+
   | **SELECT**            | Knob         | TMP, UPS, FLT, I/O      | TMP     | Core temperature, UPS   |
   |                       |              |                         |         | charge, filter          |
   |                       |              |                         |         | condition or I/O load   |
   |                       |              |                         |         | on **METER**            |
   +-----------------------+--------------+-------------------------+---------+-------------------------+
   | **TEST**              | Button       | —                       | —       | Runs the rack on        |
   |                       |              |                         |         | battery for 15 s        |
   +-----------------------+--------------+-------------------------+---------+-------------------------+
   | **LOAD** and **BATT** | 5 lamps each | —                       | —       | Draw and UPS charge in  |
   | lamps                 |              |                         |         | fifths (see             |
   |                       |              |                         |         | :ref:`4.12 <sec-4-12>`) |
   +-----------------------+--------------+-------------------------+---------+-------------------------+
   | Battery compartment   | Slot 22      | —                       | Empty   | Takes one battery cell, |
   |                       |              |                         |         | which adds to the UPS   |
   +-----------------------+--------------+-------------------------+---------+-------------------------+

4.10 Bottom row
---------------

.. index::
   single: Bottom row

The bottom row holds the main switch and the two drive buses.

.. index::
   single: MAIN POWER
   single: BUS A
   single: BUS B

.. _table-4-9:

.. table:: **Table 4-9** Bottom row

   +-----------------+------------------+-----------+---------+-------------------------+
   | Control         | Type             | Positions | Default | Function                |
   +=================+==================+===========+=========+=========================+
   | **MAIN POWER**  | Rocker with lamp | Off, on   | —       | The rack's on/off       |
   |                 |                  |           |         | switch                  |
   +-----------------+------------------+-----------+---------+-------------------------+
   | PDU lamp        | Lamp             | —         | —       | Shows the power state   |
   |                 |                  |           |         | (see                    |
   |                 |                  |           |         | :ref:`4.12 <sec-4-12>`) |
   +-----------------+------------------+-----------+---------+-------------------------+
   | **BUS A**       | Toggle           | Off, on   | On      | Drive bus for bays 1–4  |
   +-----------------+------------------+-----------+---------+-------------------------+
   | **BUS B**       | Toggle           | Off, on   | On      | Drive bus for bays 5–8  |
   +-----------------+------------------+-----------+---------+-------------------------+
   | PDU outlets 1–5 | Sockets          | —         | —       | None; they are          |
   |                 |                  |           |         | decoration, and very    |
   |                 |                  |           |         | good at it              |
   +-----------------+------------------+-----------+---------+-------------------------+

4.11 Displays
-------------

.. index::
   single: Displays

Besides the monitor, the rack has a small status display above the key pad and two gauges on the UPS panel.

.. _figure-4-7:

.. figure:: /images/status-display.png
   :alt: The green status display: DS-8, the clock and uptime; core temperature, draw and fan mode; UPS bar and filter condition
   :width: 73%

   **Figure 4-7** The status display, here showing the UPS and filter on its third line.

The status display's first two lines always show the clock and the uptime, then the core temperature, the power draw and the fan mode. The third line shows the page selected with the **DISPLAY** knob, such as the drives online, the processors running, the I/O traffic, or the UPS charge and filter condition. On AUT the display rotates through its pages by itself. The **LCD** toggle on the switch strip switches it off.

The **LOAD** gauge on the UPS panel always shows the power draw. The **METER** gauge next to it shows whatever the **SELECT** knob picks: core temperature, UPS charge, filter condition or I/O load.

.. _sec-4-12:

4.12 Status indicators
----------------------

.. index::
   single: Status indicators

The cabinet is generous with lamps, and between them they tell you most of what the rack is doing without opening a single program. The **LAMP** button on the control row tests them all at once.

.. index::
   single: PWR
   single: NET
   single: ACT
   single: TMP
   single: ERR
   single: LOCK
   single: WP
   single: BATT
   single: LOAD
   single: MAIN POWER
   single: BUS A
   single: BUS B

.. _table-4-10:

.. table:: **Table 4-10** Lamps

   +-------------------------+--------------------------------------+-----------------------------------------+
   | Lamp                    | Where                                | Meaning                                 |
   +=========================+======================================+=========================================+
   | Beacon, red (flashing)  | Top left                             | Overheated, alarm sounding, a processor |
   |                         |                                      | in error, or no system board            |
   +-------------------------+--------------------------------------+-----------------------------------------+
   | Beacon, amber           | Top left                             | Needs attention: switched on but not    |
   |                         |                                      | running, on battery, at or above the    |
   |                         |                                      | alarm temperature, **BYPASS** on,       |
   |                         |                                      | filter pulled or below 25 %, or battery |
   |                         |                                      | reconditioning. Flashes in maintenance  |
   |                         |                                      | mode                                    |
   +-------------------------+--------------------------------------+-----------------------------------------+
   | Beacon, green           | Top left                             | Running and online, with nothing red    |
   +-------------------------+--------------------------------------+-----------------------------------------+
   | **PWR**                 | Switch strip, right                  | Green on mains; flashing amber on       |
   |                         |                                      | battery                                 |
   +-------------------------+--------------------------------------+-----------------------------------------+
   | **NET**                 | Switch strip, right                  | Green with a data cable connected       |
   +-------------------------+--------------------------------------+-----------------------------------------+
   | **ACT**                 | Switch strip, right                  | Blue flicker on memory traffic          |
   +-------------------------+--------------------------------------+-----------------------------------------+
   | **TMP**                 | Switch strip, right                  | Amber at or above the alarm             |
   |                         |                                      | temperature; flashing red when          |
   |                         |                                      | overheated                              |
   +-------------------------+--------------------------------------+-----------------------------------------+
   | **ERR**                 | Switch strip, right                  | Red when overheated or for 1.5 s after  |
   |                         |                                      | a failed memory access; flashing with   |
   |                         |                                      | no system board                         |
   +-------------------------+--------------------------------------+-----------------------------------------+
   | **LOCK**, **WP**, alarm | Control row, beside **LOCK**, **WP** | Red when locked; amber with write       |
   |                         | and **MUTE**                         | protection on; red while the alarm is   |
   |                         |                                      | active (steady once muted)              |
   +-------------------------+--------------------------------------+-----------------------------------------+
   | Bank ports 0–7          | Patch field, upper row               | Green when served by a drive; amber     |
   |                         |                                      | when cabled but the bay is not serving  |
   +-------------------------+--------------------------------------+-----------------------------------------+
   | I/O ports 1–8           | Patch field, upper row               | Green with both a pin cable and a       |
   |                         |                                      | device ID; amber with only one of the   |
   |                         |                                      | two; red with **I/O** off; blue flicker |
   |                         |                                      | while processors run                    |
   +-------------------------+--------------------------------------+-----------------------------------------+
   | Bay lamps               | Each drive bay                       | Green when served; blue while being     |
   |                         |                                      | read or written; amber with a drive     |
   |                         |                                      | fitted but its cable pulled; red with   |
   |                         |                                      | storage offline                         |
   +-------------------------+--------------------------------------+-----------------------------------------+
   | **BATT** row            | UPS panel                            | UPS charge in fifths: green, amber on   |
   |                         |                                      | battery or with **BYPASS** on, red      |
   |                         |                                      | below 25 %                              |
   +-------------------------+--------------------------------------+-----------------------------------------+
   | **LOAD** row            | UPS panel                            | Power draw in fifths of the graph       |
   |                         |                                      | scale: three green, then amber, then    |
   |                         |                                      | red                                     |
   +-------------------------+--------------------------------------+-----------------------------------------+
   | **MAIN POWER**, PDU     | Bottom row                           | Green on mains, amber on battery, dark  |
   |                         |                                      | when switched off                       |
   +-------------------------+--------------------------------------+-----------------------------------------+
   | **BUS A**, **BUS B**    | Bottom row                           | Green when on, red when off             |
   +-------------------------+--------------------------------------+-----------------------------------------+

The lamps on the processor sockets are described in :ref:`11 Programming (IC10) <ch-programming>`, and the service bay's lamps in :ref:`8 Maintenance <ch-maintenance>`.

4.13 The alarm
--------------

.. index::
   single: Alarm

The alarm uses the beacon, the beeper and an entry in the event log. It sounds while the **ALRM** switch is on and the rack is overheated, running on battery, above its alarm temperature or missing its air filter, or while a rule or library task raises an alarm.

**MUTE** silences the alarm until its cause clears, after which it arms itself again. The **BEEP** DIP switch in the service bay turns the beeper off altogether, and **MAINT** suppresses the alarm entirely while you work (see :ref:`8 Maintenance <ch-maintenance>`). When the alarm will not stop, :ref:`9 Diagnostics and troubleshooting <ch-diagnostics>` explains how to find out why.
