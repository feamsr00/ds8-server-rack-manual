.. _ch-installation:

3 Installation and commissioning
================================

.. index::
   single: Installation and commissioning

This chapter takes a rack from a kit on the floor to a running server. It starts with what the rack needs from its surroundings, explains how it is cooled and powered, and finishes with two procedures: installing the rack and switching it on for the first time.

3.1 Requirements
----------------


A working rack needs a little more than most structures, mainly because it refuses to start without a system board and cools itself with whatever air is around it.

.. _table-3-1:

.. table:: **Table 3-1** Requirements

   +----------------------------------+-----------------------------------------------------+
   | Requirement                      | Why it is needed                                    |
   +==================================+=====================================================+
   | A pressurised room               | The fans cool the core with room air; in vacuum the |
   |                                  | rack overheats within minutes                       |
   +----------------------------------+-----------------------------------------------------+
   | A power cable                    | Everything runs on mains, with a small built-in UPS |
   |                                  | as backup                                           |
   +----------------------------------+-----------------------------------------------------+
   | A data cable                     | The rack can only see, read and control devices on  |
   |                                  | its own data network                                |
   +----------------------------------+-----------------------------------------------------+
   | A system board (any motherboard) | The rack will not start without one, and nothing in |
   |                                  | mod version 5.12.7 fits one for you                 |
   +----------------------------------+-----------------------------------------------------+
   | At least one data drive          | Without a drive the rack has no memory to offer     |
   +----------------------------------+-----------------------------------------------------+

A battery cell, IC10 chips and a rack key are optional. The battery extends the UPS runtime, the chips give you programs, and the key lets you lock the front panel.

The Workshop page says that new racks come with a system board fitted, but in version 5.12.7 they arrive without one, so bring a motherboard of your own. Any motherboard will do.

3.2 Ambient conditions and cooling
----------------------------------

.. index::
   single: Ambient conditions and cooling
   single: Cooling
   single: Heat
   single: Vacuum

The rack's core behaves like a small block of metal with a heat capacity of 3,000 J per °C. It warms up with every watt the rack draws, and it sheds heat to the room through its fans. In ordinary base air a rack settles some 20–30 °C above room temperature and stays there contentedly.

The heat the fans carry out depends on the temperature difference, the room's pressure, the fan setting and the state of the air filter:

.. code-block:: text

	heat out (W) = 9 × k × (T_core − T_room)
	k = 0.03 + min(p_room / 101.3 kPa, 1.5) × F_fan × F_filter

- **Fan factor:** On Auto, the factor rises from 1.0 at 35 °C to 2.2 at 70 °C. Low gives 0.6, High 3.2, Manual between 0.3 and 3.4, and the fan test 3.6. With the air filter pulled the fans stop, leaving a factor of 0.35.
- **Filter factor:** This is 0.45 + 0.55 × the filter's condition, so a completely clogged filter roughly halves the cooling.
- **Vacuum:** Below 0.05 kPa only the constant 0.03 is left. A rack drawing 355 W then climbs about 0.12 °C every second and reaches 85 °C in roughly nine minutes, which makes vacuum a poor choice of server room.
- **The room warms too:** 20 % of the heat the fans carry out goes into the room air (server setting ``ExhaustHeatFraction``), as long as the room is above the Armstrong limit and the filter is in.
- **Thermal simulation off:** With the server setting ``ThermalSimulation`` switched off, the core simply stays at 20 °C.

Three temperatures govern what happens as the core warms up. The warning level is set with the **TEMP ALARM** knob, and the trip level sits a fixed margin above it, set with the **TRIP +** knob in the service bay.

.. _table-3-2:

.. table:: **Table 3-2** Temperature thresholds

   +----------+----------------------------------------+-----------------------------------------+
   | Event    | Default                                | What happens                            |
   +==========+========================================+=========================================+
   | Warning  | 70 °C (**TEMP ALARM**, 60–80 °C)       | A warning in the event log, and the     |
   |          |                                        | alarm sounds                            |
   +----------+----------------------------------------+-----------------------------------------+
   | Trip     | Warning + **TRIP +** (default 15) = 85 | Storage goes offline, processors and    |
   |          | °C                                     | automation stop, and the overheat       |
   |          |                                        | screen appears                          |
   +----------+----------------------------------------+-----------------------------------------+
   | Recovery | Warning − 10 = 60 °C                   | With the **ARST** DIP switch on the     |
   |          |                                        | rack comes back by itself; otherwise it |
   |          |                                        | waits for **RESET**                     |
   +----------+----------------------------------------+-----------------------------------------+

.. admonition:: CAUTION
   :class: warning

   Pulling the air filter stops the fans, and the core will start to overheat. Be sure to refit the filter within a few minutes.

.. _sec-3-3:

3.3 Power supply and UPS
------------------------

.. index::
   single: Power supply and UPS
   single: UPS
   single: Power draw

The rack draws a base load whenever it runs, and adds to it for fans, drives, traffic, processors and battery charging. The figures below are the defaults; most can be changed with server settings (see :ref:`7 Configuration <ch-configuration>`).

.. _table-3-3:

.. table:: **Table 3-3** Power draw

   +-------------------------+-----------------------------------+----------------------------------------+
   | Part                    | Draw                              | Notes                                  |
   +=========================+===================================+========================================+
   | Base, while running     | 60 W                              | Server setting ``BasePowerW``          |
   +-------------------------+-----------------------------------+----------------------------------------+
   | Fans                    | Auto 15–40 W, Low 8 W, High 60 W, | Auto rises between 35 and 70 °C; the   |
   |                         | Manual 4–74 W, fan test 75 W      | **FAN** trim in the service bay scales |
   |                         |                                   | it; each BIOS fan-floor step adds 8 W  |
   +-------------------------+-----------------------------------+----------------------------------------+
   | Each drive being served | 35 W                              | ``PowerPerDriveW``. With the **ECO**   |
   |                         |                                   | DIP switch on, idle drives draw only   |
   |                         |                                   | 20–80 % of this (set in the BIOS,      |
   |                         |                                   | default 40 %)                          |
   +-------------------------+-----------------------------------+----------------------------------------+
   | Read/write traffic      | Up to 80 W                        | ``ActivityPowerW``, at full load       |
   +-------------------------+-----------------------------------+----------------------------------------+
   | Each running processor  | 8 W on the **HI** clock           | 4 W per 64 lines a tick, doubled by    |
   |                         |                                   | **TURBO** and scaled by the BIOS       |
   |                         |                                   | multiplier                             |
   +-------------------------+-----------------------------------+----------------------------------------+
   | UPS charging            | 100 W × **CHARGE** setting        | 25, 50, 100, 150 or 200 %, and only    |
   |                         |                                   | while charging                         |
   +-------------------------+-----------------------------------+----------------------------------------+

Drives, processors and traffic only count while storage is online. As a worked example, a rack with eight idle drives and its fans on Auto at 35 °C draws 60 + 15 + 8 × 35 = 355 W. Switch the **ECO** DIP on and the same rack draws 60 + 15 + 8 × 14 = 187 W.

The built-in UPS stores 40 kJ (server setting ``UpsCapacityKJ``; a value of 0 removes the UPS entirely). It takes over the moment mains fails, unless **BYPASS** is on or the battery is being reconditioned, and it keeps the rack running until its charge falls to the reserve set with the **CUT** slider (0–40 %).

- **Runtime** is simply capacity divided by draw: about 110 s at 355 W, or about 210 s at 187 W.
- **A battery cell** in the battery compartment adds its own charge on top of the UPS. The rack charges the cell from mains once the UPS itself is full.
- **Battery health** falls by about 1 % per full discharge, though never below 50 %, and the usable capacity falls with it. Reconditioning restores it (see :ref:`8 Maintenance <ch-maintenance>`).
- **Low battery** raises an error when the charge reaches 25 % on battery. The BIOS can move this threshold anywhere between 15 % and 50 %.
- **When mains returns,** the rack restarts by itself, or waits for **RESET** if the BIOS is set to "Stay off".

.. admonition:: CAUTION
   :class: warning

   The UPS carries a fully loaded rack for only about two minutes. Fit a battery cell if the rack runs anything that cannot stop for longer than that.

3.4 Wiring
----------

.. index::
   single: Wiring

The rack has two connections and one switch that matter for wiring.

- **Power cable:** This feeds the rack through **MAIN POWER**, the rocker at the bottom left of the front panel in its yellow frame. **MAIN POWER** is the rack's ordinary on/off switch.
- **Data cable:** This decides what the rack can see. Its programs, rules, library tasks, print jobs, logger and dashboard reach only devices on this data network, together with any devices the game's network bridges add to it.
- **Drive buses:** **BUS A** (bays 1–4) and **BUS B** (bays 5–8) sit next to **MAIN POWER**. Both start switched on; switching one off takes its four bays offline and saves their power.
- **Lua chips:** With the StationeersLua mod installed, Lua chips run in the rack's sockets alongside IC10 chips.

.. _sec-3-5:

3.5 Installing the rack
-----------------------

.. index::
   single: Installing the rack

**Requirements:** You must have a DS-8 Server Rack kit, at least one data drive, any motherboard, a power cable and a data cable, and a pressurised room with space for a full-height cabinet.

1. Print a **DS-8 Server Rack kit** and a few **data drives** at the Electronics Printer. Print a **rack key** as well if you want to be able to lock the panel.
2. Place and build the kit in the pressurised room.
3. Connect the power cable and the data cable to the rack.
4. Pull the lock pin above the monitor, swing the monitor out, and fit the motherboard in the system board slot behind it. Push the monitor back in when you are done.
5. Slide the data drives into the bays, starting with bay 1.

**Result:** The rack is ready for its first power-up. Out of the box, bay 1 serves memory bank 0, bay 2 serves bank 1, and so on (see :ref:`6 Storage and data handling <ch-storage>`).

.. _sec-3-6:

3.6 First power-up
------------------

.. index::
   single: First power-up

**Requirements:** The rack must be installed as described in :ref:`3.5 <sec-3-5>`, with power on the cable.

1. Flip **MAIN POWER**. The boot screen appears, the rack starts charging its UPS, and after a few seconds it goes online.
2. Open the glass cover over the key pad and press **HOME** to open the start menu. Alternatively, hold **Alt** and click the screen to use it as a touch screen; the mouse wheel scrolls.
3. Press **HELP** in any program to see its keys.

**Result:** The beacon on top of the cabinet shows green, and pointing at the rack shows a tooltip with its state ("Online"), core temperature, power draw, UPS charge, and the drives and cells in use. The screen and its programs are described in :ref:`5 DS-8 OS <ch-os>`, and every control on the panel in :ref:`4 Controls and indicators <ch-controls>`.

3.7 Next steps
--------------


With the rack running, these are the usual next steps.

- Push IC10 chips into the four front sockets (processors 1–4) or the eight rear sockets (processors 5–12). With the **AUTO** DIP switch on, as it is from the factory, they start on their own at power-up (see :ref:`11 Programming (IC10) <ch-programming>`).
- Give the processors their devices by selecting each device in :ref:`5.12 Network <os-network>` and pressing 0–5 for pins d0–d5.
- Fit a battery cell in the battery compartment for a longer UPS runtime.
- Write-protect the banks that hold anything you want to keep, and read :ref:`2 Safety <ch-safety>` before trusting the rack with an airlock.
