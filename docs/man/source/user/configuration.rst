.. _ch-configuration:

7 Configuration
===============

.. index::
   single: Configuration

Most of the rack's behaviour is set with the switches on its front panel (see :ref:`4 Controls and indicators <ch-controls>`). This chapter covers the three places where the rest is configured: the setup utility, often called the BIOS, which changes how the rack starts and runs; the DIP switches in the service bay; and the server settings, which apply to every rack in the world. Every default is also collected in :ref:`Appendix B: Factory defaults <app-b>`.

.. _sec-7-1:

7.1 The setup utility (BIOS)
----------------------------

.. index::
   single: Setup utility (BIOS)

The setup utility is reached through the **BIOS** button, a small red button hidden behind the monitor. On a running rack, pressing it restarts the rack straight into setup, with storage and processors offline for as long as setup is open. On a rack that is switched off, pressing it arms setup to open at the next start; pressing it again cancels the request.

.. _figure-7-1:

.. figure:: /images/monitor-swung-out.png
   :alt: The monitor swung out to the left, showing the system board slot full of coloured wiring and the red BIOS button at its bottom right
   :width: 100%

   **Figure 7-1** The monitor swung out. The system board sits in the opening, and the red **BIOS** button is at its bottom right.

.. _figure-7-2:

.. figure:: /images/setup-utility.png
   :alt: DS-8 Setup Utility: the settings list on the left, item help and a hardware monitor on the right
   :width: 100%

   **Figure 7-2** The setup screen. The header names the system board (SB-8) and its firmware; on the right are help for the selected item and a hardware monitor showing the core temperature, fan speed, battery and its health, mains, running hours and memory size.

.. _table-7-1:

.. table:: **Table 7-1** Setup utility keys

   +---------------------------+------------------------------------------+
   | Key                       | What it does                             |
   +===========================+==========================================+
   | **UP** / **DN**           | Select a setting                         |
   +---------------------------+------------------------------------------+
   | **ENT**, **>** or **INC** | Selects the setting's next value         |
   +---------------------------+------------------------------------------+
   | **<** or **DEC**          | Selects the setting's previous value     |
   +---------------------------+------------------------------------------+
   | **F1**                    | Loads the default values                 |
   +---------------------------+------------------------------------------+
   | **F5** or **ESC**         | Saves the settings and restarts the rack |
   +---------------------------+------------------------------------------+

.. index::
   single: Power-on self test (setup utility)
   single: Start program (setup utility)
   single: After power loss (setup utility)
   single: CPU clock multiplier (setup utility)
   single: Battery low warning (setup utility)
   single: Fan idle floor (setup utility)
   single: Clock format (setup utility)
   single: Scratch cells (setup utility)
   single: Boot chime (setup utility)

.. _table-7-2:

.. table:: **Table 7-2** Setup utility settings (defaults in bold)

   +------------------------+-------------------------------------+-----------------------------------------+
   | Setting                | Options                             | Effect                                  |
   +========================+=====================================+=========================================+
   | Power-on self test     | Quick, **Normal**, Full memory test | Length of the boot screen: 1.2, 4 or 8  |
   |                        |                                     | s                                       |
   +------------------------+-------------------------------------+-----------------------------------------+
   | Start program          | **System** … Dashboard              | The program shown after power-up and    |
   |                        |                                     | after **RESET**                         |
   +------------------------+-------------------------------------+-----------------------------------------+
   | After power loss       | **Restart**, Stay off               | With Stay off, the rack waits for       |
   |                        |                                     | **RESET** when mains returns            |
   +------------------------+-------------------------------------+-----------------------------------------+
   | CPU clock multiplier   | x0.5, **x1**, x2                    | Scales the **CLOCK** knob; power and    |
   |                        |                                     | heat scale with it                      |
   +------------------------+-------------------------------------+-----------------------------------------+
   | Idle drive power (ECO) | 20 %, **40 %**, 60 %, 80 %          | What idle drives draw while the **ECO** |
   |                        |                                     | DIP switch is on                        |
   +------------------------+-------------------------------------+-----------------------------------------+
   | Battery low warning    | 15 %, **25 %**, 35 %, 50 %          | The UPS charge that raises the          |
   |                        |                                     | low-battery error                       |
   +------------------------+-------------------------------------+-----------------------------------------+
   | Fan idle floor         | **Off**, Low, Medium                | Keeps the fans above idle on Auto:      |
   |                        |                                     | cooler, at the cost of more power and   |
   |                        |                                     | filter wear                             |
   +------------------------+-------------------------------------+-----------------------------------------+
   | Clock format           | **24 hours**, 12 hours              | How the time is shown                   |
   +------------------------+-------------------------------------+-----------------------------------------+
   | Write protect at boot  | **Off**, On                         | Switches write protection on at every   |
   |                        |                                     | start                                   |
   +------------------------+-------------------------------------+-----------------------------------------+
   | Scratch cells          | **Read / write**, Read only         | Whether programs may write the eight    |
   |                        |                                     | shared cells after the status registers |
   +------------------------+-------------------------------------+-----------------------------------------+
   | Boot chime             | **On**, Off                         | A beep when the system has started      |
   +------------------------+-------------------------------------+-----------------------------------------+

7.1.1 Changing a setup setting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: Changing a setup setting

**Requirements:** You need access to the front of the rack; the panel lock does not prevent this.

1. Pull the lock pin above the monitor and swing the monitor out.
2. Press the red **BIOS** button at the bottom right of the opening. A running rack restarts into setup.
3. Select the setting with **UP** and **DN**, and change it with **ENT**, **>** or **<**.
4. Press **F5** to save and restart.
5. Push the monitor back in.

**Result:** The rack restarts with the new settings, and the event log records that setup was saved.

.. admonition:: NOTICE
   :class: note

   While setup is open, storage and processors are offline and automation does not run. Anything the rack controls is unattended until you save and restart.

.. _sec-7-2:

7.2 DIP switches
----------------

.. index::
   single: DIP switches

The eight DIP switches sit in the service bay at the back, behind the service hatch, and change behaviour you are unlikely to want to change often. A photo of the service bay is in :ref:`8 Maintenance <ch-maintenance>`.

.. index::
   single: DIP 1 BEEP
   single: DIP 2 ECO
   single: DIP 3 SAVR
   single: DIP 4 AUTO
   single: DIP 5 WDOG
   single: DIP 6 ARST
   single: DIP 7 QBT
   single: DIP 8 PLCK

.. _table-7-3:

.. table:: **Table 7-3** DIP switches

   +------------+---------+----------------------------------------+
   | DIP        | Default | When it is on                          |
   +============+=========+========================================+
   | 1 **BEEP** | On      | The alarm beeper sounds                |
   +------------+---------+----------------------------------------+
   | 2 **ECO**  | Off     | Idle drives draw less power; the BIOS  |
   |            |         | decides how much less                  |
   +------------+---------+----------------------------------------+
   | 3 **SAVR** | On      | The screen saver starts after the      |
   |            |         | **SAVER** delay                        |
   +------------+---------+----------------------------------------+
   | 4 **AUTO** | On      | Processors start at power-up; with it  |
   |            |         | off, they wait for **RST**             |
   +------------+---------+----------------------------------------+
   | 5 **WDOG** | Off     | A processor stopped by an error        |
   |            |         | restarts after 3 s                     |
   +------------+---------+----------------------------------------+
   | 6 **ARST** | On      | The rack restarts by itself after an   |
   |            |         | overheat                               |
   +------------+---------+----------------------------------------+
   | 7 **QBT**  | Off     | Quick boot                             |
   +------------+---------+----------------------------------------+
   | 8 **PLCK** | Off     | The **LOCK** key switch also locks the |
   |            |         | patch cables                           |
   +------------+---------+----------------------------------------+

7.3 Server settings
-------------------

.. index::
   single: Server settings
   single: Drive size

The server settings belong to the mod rather than to any one rack, and they apply to every rack in the world. You change them in StationeersLaunchPad, where they appear as the mod's BepInEx configuration, and the changes take effect while the game runs.

.. index::
   single: DriveCapacity (server setting)
   single: BasePowerW (server setting)
   single: PowerPerDriveW (server setting)
   single: ActivityPowerW (server setting)
   single: UpsCapacityKJ (server setting)
   single: UpsChargeW (server setting)
   single: ExhaustHeatFraction (server setting)
   single: ThermalSimulation (server setting)
   single: WarnTemperatureC (server setting)
   single: ShutdownTemperatureC (server setting)
   single: FilterLifeHoursV2 (server setting)
   single: KeyRequired (server setting)
   single: SharpScreens (server setting)
   single: ScreenGlass (server setting)
   single: LcdCharacter (server setting)
   single: ScreenLight (server setting)

.. _table-7-4:

.. table:: **Table 7-4** Server settings

   +-----------+--------------------------+---------+------------+-------------------------+
   | Section   | Setting                  | Default | Range      | Effect                  |
   +===========+==========================+=========+============+=========================+
   | 1 Storage | ``DriveCapacity``        | 512     | 64–4096    | Cells per drive; the    |
   |           |                          |         |            | address space is 8      |
   |           |                          |         |            | times this. Set it      |
   |           |                          |         |            | before the first rack   |
   |           |                          |         |            | is built                |
   +-----------+--------------------------+---------+------------+-------------------------+
   | 2 Power   | ``BasePowerW``           | 60      | 0–5000     | Draw of a running rack, |
   |           |                          |         |            | not counting the fans   |
   +-----------+--------------------------+---------+------------+-------------------------+
   | 2 Power   | ``PowerPerDriveW``       | 35      | 0–5000     | Extra draw for each     |
   |           |                          |         |            | drive being served      |
   +-----------+--------------------------+---------+------------+-------------------------+
   | 2 Power   | ``ActivityPowerW``       | 80      | 0–5000     | Extra draw at full      |
   |           |                          |         |            | read/write load         |
   +-----------+--------------------------+---------+------------+-------------------------+
   | 2 Power   | ``UpsCapacityKJ``        | 40      | 0–100000   | Energy of the built-in  |
   |           |                          |         |            | UPS in kJ; 0 removes    |
   |           |                          |         |            | the UPS                 |
   +-----------+--------------------------+---------+------------+-------------------------+
   | 2 Power   | ``UpsChargeW``           | 100     | 1–5000     | Charging draw, scaled   |
   |           |                          |         |            | by the **CHARGE**       |
   |           |                          |         |            | slider                  |
   +-----------+--------------------------+---------+------------+-------------------------+
   | 3 Heat    | ``ExhaustHeatFraction``  | 0.2     | 0–1        | Share of the fans'      |
   |           |                          |         |            | exhaust heat that warms |
   |           |                          |         |            | the room                |
   +-----------+--------------------------+---------+------------+-------------------------+
   | 3 Heat    | ``ThermalSimulation``    | On      | On, off    | Off keeps the core at   |
   |           |                          |         |            | 20 °C, so it never      |
   |           |                          |         |            | trips                   |
   +-----------+--------------------------+---------+------------+-------------------------+
   | 3 Heat    | ``WarnTemperatureC``     | 70      | 30–200     | Alarm temperature until |
   |           |                          |         |            | someone turns the       |
   |           |                          |         |            | **TEMP ALARM** knob     |
   |           |                          |         |            | (60–80)                 |
   +-----------+--------------------------+---------+------------+-------------------------+
   | 3 Heat    | ``ShutdownTemperatureC`` | 85      | 40–300     | Sets where the **TRIP   |
   |           |                          |         |            | +** knob starts:        |
   |           |                          |         |            | whichever of +5, +10,   |
   |           |                          |         |            | +15 or +20 °C above the |
   |           |                          |         |            | alarm is nearest        |
   +-----------+--------------------------+---------+------------+-------------------------+
   | 3 Heat    | ``FilterLifeHoursV2``    | 200     | 0.1–100000 | Real-time hours until a |
   |           |                          |         |            | new filter clogs, on    |
   |           |                          |         |            | Auto in normal air      |
   +-----------+--------------------------+---------+------------+-------------------------+
   | 4 Panel   | ``KeyRequired``          | On      | On, off    | Off lets anyone turn    |
   |           |                          |         |            | the **LOCK** switch     |
   |           |                          |         |            | without the rack key    |
   +-----------+--------------------------+---------+------------+-------------------------+
   | 5 Display | ``SharpScreens``         | On      | On, off    | Keeps displays sharp up |
   |           |                          |         |            | close, without flicker  |
   |           |                          |         |            | at an angle             |
   +-----------+--------------------------+---------+------------+-------------------------+
   | 5 Display | ``ScreenGlass``          | On      | On, off    | A faint glass in front  |
   |           |                          |         |            | of the displays, with   |
   |           |                          |         |            | dust, scratches and     |
   |           |                          |         |            | reflections             |
   +-----------+--------------------------+---------+------------+-------------------------+
   | 5 Display | ``LcdCharacter``         | On      | On, off    | An old-LCD look, with   |
   |           |                          |         |            | viewing-angle shifts    |
   |           |                          |         |            | and edge bleed          |
   +-----------+--------------------------+---------+------------+-------------------------+
   | 5 Display | ``ScreenLight``          | On      | On, off    | The monitor casts a     |
   |           |                          |         |            | soft light in the       |
   |           |                          |         |            | colour of its picture   |
   +-----------+--------------------------+---------+------------+-------------------------+

.. admonition:: NOTICE
   :class: note

   Changing ``DriveCapacity`` moves every memory address at once, because it changes both the bank size and where the status cells begin, while drives already in use keep their old size. Decide on it before the first rack is built.

The effect of the power and heat settings is explained in :ref:`3 Installation and commissioning <ch-installation>`, and the game-log and save names the mod uses are listed in :ref:`13 Multiplayer, saves and mods <ch-multiplayer>`.
