.. _os-library:

5.17 Library (Program Library)
==============================

.. index::
   single: Library (Program Library)

The Library holds sixteen finished control programs that you fill in with devices and numbers, rather than writing yourself. Up to twelve tasks built from them can run at once. It is program 10 in the Automation group; open it with **HOME**, then **4**. The mod's author marks it as beta, so treat it with the usual respect for anything wearing that label.

5.17.1 Screen
-------------


.. _figure-5-14:

.. figure:: /images/os-library.png
   :alt: Program Library catalogue with Advanced airlock selected and a panel listing what to build for it
   :width: 100%

   **Figure 5-14** The catalogue. Selecting a program shows what to build for it; for the airlock, that is two doors, an active vent, a gas sensor and two logic buttons, all on the rack's data network.

The screen has two views: the catalogue of programs, and the list of your running tasks. In the catalogue, the panel below the list explains what to build for the selected program.

5.17.2 Keys
-----------


.. _table-5-20:

.. table:: **Table 5-20** Library keys

   +----------------------------------+-----------------------------------------------------+
   | Key                              | What it does                                        |
   +==================================+=====================================================+
   | **TAB** or **F5**                | Switches between the catalogue and your tasks       |
   +----------------------------------+-----------------------------------------------------+
   | **UP** / **DN**                  | Select a program or task                            |
   +----------------------------------+-----------------------------------------------------+
   | **F1** or **ENT**                | Installs the program as a task, or starts and stops |
   |                                  | the task                                            |
   +----------------------------------+-----------------------------------------------------+
   | **F2**                           | Triggers the task: cycles an airlock task, and on   |
   |                                  | other tasks finds devices like **F3**               |
   +----------------------------------+-----------------------------------------------------+
   | **F3**                           | Finds devices for the task's empty roles            |
   +----------------------------------+-----------------------------------------------------+
   | **F4**                           | Removes the task                                    |
   +----------------------------------+-----------------------------------------------------+
   | **<** / **>**, **INC** / **DEC** | Select and change a field                           |
   +----------------------------------+-----------------------------------------------------+

Find devices fills each empty role with the first matching device on the network, by name. A task that still lacks a required device shows "Missing:" followed by the role.

5.17.3 The sixteen programs
---------------------------

.. index::
   single: Sixteen programs

.. index::
   single: Advanced airlock (library program)
   single: Room climate (library program)
   single: Greenhouse lights (library program)
   single: Solar tracking (library program)
   single: Tank filler (library program)
   single: Power manager (library program)
   single: Room alarm (library program)
   single: Air conditioner (library program)
   single: Backup generator (library program)
   single: Air scrubber (library program)
   single: Presence lights (library program)
   single: Automatic door (library program)
   single: Night lights (library program)
   single: Leak alarm (library program)
   single: Interval timer (library program)
   single: Tank guard (library program)

.. _table-5-21:

.. table:: **Table 5-21** Library programs

   +-------------------+-------------------------------+-------------------------------+-------------------------------+
   | Program           | What it does                  | Devices (optional ones in     | Settings (defaults)           |
   |                   |                               | brackets)                     |                               |
   +===================+===============================+===============================+===============================+
   | Advanced airlock  | Cycles a two-door airlock on  | Inner door, outer door,       | Fill to 100 kPa, empty below  |
   |                   | a button press; **F2** on the | active vent, gas sensor,      | 1 kPa, give up after 60 s     |
   |                   | rack cycles it too            | (button inside), (button      |                               |
   |                   |                               | outside)                      |                               |
   +-------------------+-------------------------------+-------------------------------+-------------------------------+
   | Room climate      | Holds a room's temperature    | Gas sensor, (wall heater),    | 21 °C, band 2 °C, 90–110 kPa  |
   |                   | and pressure                  | (wall cooler), (active vent   |                               |
   |                   |                               | on an air line)               |                               |
   +-------------------+-------------------------------+-------------------------------+-------------------------------+
   | Greenhouse lights | Day and night cycle for grow  | All grow lights of one kind,  | 8 min light, 4 min dark, only |
   |                   | lights                        | (daylight sensor)             | without sun: no               |
   +-------------------+-------------------------------+-------------------------------+-------------------------------+
   | Solar tracking    | Turns every panel of one kind | Daylight sensor, all solar    | Vertical mode 0, offset 0°,   |
   |                   | to the sun                    | panels of one kind            | every 2 s                     |
   +-------------------+-------------------------------+-------------------------------+-------------------------------+
   | Tank filler       | Fills a tank between two      | Tank or pipe analyser, pump   | Start below 2,000 kPa, stop   |
   |                   | pressures                     | or active vent                | above 5,000 kPa               |
   +-------------------+-------------------------------+-------------------------------+-------------------------------+
   | Power manager     | Sheds up to four loads as     | Battery, loads 1–4 (each one  | Off below 10/20/30/40 %,      |
   |                   | batteries run low             | device or all of a kind)      | margin 10 %                   |
   +-------------------+-------------------------------+-------------------------------+-------------------------------+
   | Room alarm        | Warns when a room's air goes  | Gas sensor, (warning lights), | 80–130 kPa, oxygen at least   |
   |                   | bad                           | (speaker or klaxon)           | 16 %, at most 45 °C           |
   +-------------------+-------------------------------+-------------------------------+-------------------------------+
   | Air conditioner   | Switches an air conditioner   | Gas sensor, air conditioner   | Target 21 °C, minimum 18,     |
   |                   | between two temperatures      |                               | maximum 24, done within 0.5   |
   |                   |                               |                               | °C                            |
   +-------------------+-------------------------------+-------------------------------+-------------------------------+
   | Backup generator  | Starts generators when        | Battery, all generators of    | Start below 20 %, stop above  |
   |                   | batteries run low             | one kind                      | 90 %                          |
   +-------------------+-------------------------------+-------------------------------+-------------------------------+
   | Air scrubber      | Runs filtration when CO2 or   | Gas sensor, all filtration    | CO2 at most 1 kPa, pollutant  |
   |                   | pollutants rise               | units of one kind             | at most 0.05 kPa, stop at 50  |
   |                   |                               |                               | %                             |
   +-------------------+-------------------------------+-------------------------------+-------------------------------+
   | Presence lights   | Keeps lights on while someone | Occupancy sensor, all lights  | Off after 30 s                |
   |                   | is in the room                | of one kind                   |                               |
   +-------------------+-------------------------------+-------------------------------+-------------------------------+
   | Automatic door    | Opens a door while someone is | Occupancy sensor, doors of    | Close after 3 s, lock when    |
   |                   | near                          | one kind                      | closed: no                    |
   +-------------------+-------------------------------+-------------------------------+-------------------------------+
   | Night lights      | Switches lights on when the   | Daylight sensor, all lights   | Delay 10 s                    |
   |                   | sun is gone                   | of one kind                   |                               |
   +-------------------+-------------------------------+-------------------------------+-------------------------------+
   | Leak alarm        | Warns when a room loses       | Gas sensor, (warning lights), | Drop of 5 kPa within 60 s     |
   |                   | pressure fast                 | (speaker or klaxon)           |                               |
   +-------------------+-------------------------------+-------------------------------+-------------------------------+
   | Interval timer    | Switches a device on and off  | Any device with an On switch, | On 5 min, off 10 min          |
   |                   | on a timer                    | or all of a kind              |                               |
   +-------------------+-------------------------------+-------------------------------+-------------------------------+
   | Tank guard        | Opens a relief before a tank  | Tank or pipe analyser, valve, | Open above 50,000 kPa, close  |
   |                   | bursts                        | pump or vent                  | below 40,000 kPa              |
   +-------------------+-------------------------------+-------------------------------+-------------------------------+

The room-alarm and leak-alarm tasks report on :ref:`5.14 Dashboard <os-dashboard>` while active.

.. admonition:: WARNING
   :class: danger

   When the advanced airlock reaches its time limit, it opens the far door anyway, at whatever pressure the airlock has reached, and only then logs a warning. Set the limit generously, make sure the vent can actually reach its target pressure, and test the cycle with nobody standing inside. See also :ref:`2 Safety <ch-safety>`.

5.17.4 Setting up a task
------------------------

.. index::
   single: Setting up a task

**Requirements:** The devices the program needs must be built and on the rack's data network, and fewer than twelve tasks may be installed.

1. In the catalogue, select the program and read the panel below the list to see what it needs.
2. Press **F1** to install it as a task.
3. Press **F3** to fill the device roles automatically, or select each role with **<** and **>** and pick its device with **INC** and **DEC**.
4. Adjust the settings in the same way, typing numbers and pressing **ENT** where needed.
5. Press **F1** to start the task.

**Result:** The task runs every half second while the rack is online, and the event log records that it started.
