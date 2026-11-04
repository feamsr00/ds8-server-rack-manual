1 Product overview
==================
The DS-8 Server Rack is a full-height equipment cabinet that stores data, runs up to twelve IC10 programs and automates a base without any code at all. This chapter describes what the rack is made of, how its parts work together, and the jobs people most often give it.

1.1 Description
---------------
The rack combines three things that a Stationeers base normally keeps in separate boxes. It is a data store, holding eight hot-swap data drives that together give 4,096 memory cells by default. It is a processor housing, with twelve IC10 sockets that all share one set of pins and one view of the base. And it is an automation controller, running rules, scenes, ready-made control programs, print queues and a data logger inside the rack itself, with no chip required.

You operate it from a front panel of 157 clickable controls and from DS-8 OS, a small operating system with thirteen programs that runs on the rack's monitor. Everything the rack reads or controls lives on its data network, so the data cable you connect decides what it can see. Think of it as a programmable logic controller with a filing cabinet bolted on and a mild sense of humour: the event log tells the occasional joke.

1.2 How the parts fit together
------------------------------

.. image:: /images/fig-parts.png
   :alt: The cabinet holds power and cooling, the system board and DS-8 OS, storage, processors and automation, and they reach other devices over the data network

**Figure 1-1** The rack's parts and the data network

The drives become memory through the patch field, a row of cables that connects each drive bay to one of eight memory banks (see :ref:`6 Storage and data handling <ch-storage>`). Processors and automation reach the rest of the base through the data network, and IC10 chips in other housings can read and write the rack's memory as if it were their own (see :ref:`11 Programming (IC10) <ch-programming>`). Power and cooling sit underneath it all: the rack draws power continuously, cools itself with room air, and keeps running for about two minutes on its built-in UPS when mains fails.

1.3 Components and ordering data
--------------------------------
The mod adds four items. All of them are printed or built in the usual way; the rack itself is built from its kit like any other kit structure. The prefab hash in the table is the value ``HASH()`` returns in IC10, which is what batch instructions use to address every rack on a network at once.

.. image:: /images/icons.png
   :alt: The mod's own icons: the DS-8 Server Rack, a data drive and the rack key

**Figure 1-2** The rack, a data drive and the rack key, shown with the mod's own item icons.

**Table 1-1** Components

+----------------------+--------------------------+-------------+-------------------------------+
| Item                 | Prefab name              | Prefab hash | Description                   |
+======================+==========================+=============+===============================+
| DS-8 Server Rack kit | ``ItemKitDS8ServerRack`` | 1688145037  | Builds the rack               |
+----------------------+--------------------------+-------------+-------------------------------+
| DS-8 Server Rack     | ``StructureServerRack``  | 1549423555  | The cabinet itself            |
+----------------------+--------------------------+-------------+-------------------------------+
| Data drive           | ``ItemServerDrive``      | -1344622005 | 512 memory cells, eight       |
|                      |                          |             | program slots, an automation  |
|                      |                          |             | backup and a patch-field      |
|                      |                          |             | backup                        |
+----------------------+--------------------------+-------------+-------------------------------+
| Rack key             | ``ItemDS8RackKey``       | -305833913  | Turns the **LOCK** key switch |
|                      |                          |             | when held in hand             |
+----------------------+--------------------------+-------------+-------------------------------+

This manual does not list printing costs; the printer will happily tell you what it wants.

1.4 Slot assignment
-------------------
The rack has 22 slots, and each slot accepts only the item type shown below. Drive bays 1–4 hang on drive bus A and bays 5–8 on bus B, which matters when you switch a bus off to save power.

**Table 1-2** Slots

+-------+------------------------------------+-----------------------------------------+
| Slots | Accepts                            | Location                                |
+=======+====================================+=========================================+
| 1–8   | Data drives                        | Drive bays below the processor unit:    |
|       |                                    | bays 1–4 in the upper row (bus A), bays |
|       |                                    | 5–8 in the lower row (bus B)            |
+-------+------------------------------------+-----------------------------------------+
| 9–12  | IC10 chips (processors 1–4)        | Processor unit on the front, each       |
|       |                                    | socket with its own **RUN** switch and  |
|       |                                    | **RST** button                          |
+-------+------------------------------------+-----------------------------------------+
| 13    | Any motherboard (the system board) | Behind the swing-out monitor            |
+-------+------------------------------------+-----------------------------------------+
| 14–21 | IC10 chips (processors 5–12)       | Expansion chassis behind the rear door  |
+-------+------------------------------------+-----------------------------------------+
| 22    | One battery cell                   | Battery compartment behind the **LOAD** |
|       |                                    | and **BATT** lamps on the UPS panel     |
+-------+------------------------------------+-----------------------------------------+

Where each of these sits on the cabinet is shown in :ref:`4 Controls and indicators <ch-controls>`, and the order in which to fit them is in :ref:`3 Installation and commissioning <ch-installation>`.

1.5 Application examples
------------------------
The rack is general enough to do many jobs. These are the ones it does particularly well, with a pointer to where each is explained.

**Recording a sensor without writing any code.** A logger channel reads one value from one device at a fixed interval and writes it into a memory bank, keeping the latest value and a rolling history that any IC10 chip can read later. See :ref:`5.11 Logger <os-logger>`.

**Sharing data between chips across the base.** Any IC housing on the rack's data network can read and write the rack's memory with ``get`` and ``put``, so one chip can publish a value that another, three rooms away, picks up. See :ref:`11 Programming (IC10) <ch-programming>`.

**Running a base without chips.** Rules react to a reading by setting a device, and scenes store the settings of every device so that one key, or one rule, can put them all back. A "Night" scene recalled when the daylight sensor drops is a typical first project. See :ref:`5.15 Rules <os-rules>` and :ref:`5.16 Scenes <os-scenes>`.

**Cycling an airlock.** The library's advanced airlock program cycles a two-door airlock on a button press, using a vent and a gas sensor you assign to it. See :ref:`5.17 Library <os-library>`.

**Keeping the printers busy.** Print jobs queue items on any printer on the network, so a long shopping list runs while you are elsewhere. See :ref:`5.18 Jobs <os-jobs>`.

**Running many IC10 programs in one place.** Twelve sockets, a debugger with breakpoints, a small on-rack code editor and program storage on the drives make the rack a comfortable home for a base's control code. See :ref:`5.13 CPU <os-cpu>`.
