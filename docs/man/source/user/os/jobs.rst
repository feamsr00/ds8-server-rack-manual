.. _os-jobs:

5.18 Jobs (Print Jobs)
======================
Jobs keeps the printers busy. It queues items on any fabricator on the rack's data network that the game treats as a printer, so a long shopping list can run while you are somewhere else entirely. It is program 11 in the Automation group; open it with **HOME**, then **5**.

5.18.1 Screen
-------------

.. image:: /images/os-jobs.png
   :alt: Print Jobs with a Printer panel showing none on the network, and an empty job list

**Figure 5-15** A rack with no printer on its network, and therefore not much to do.

The Printer panel at the top shows the selected printer and its state, the item for a new job and the quantity. The job list below shows each job's item, quantity and state.

5.18.2 Keys
-----------
**Table 5-22** Jobs keys

+---------------------------+------------------------------------------------------+
| Key                       | What it does                                         |
+===========================+======================================================+
| **F1**                    | Selects the next printer; with the modifier, the     |
|                           | previous one                                         |
+---------------------------+------------------------------------------------------+
| **UP** / **DN**           | Select a field                                       |
+---------------------------+------------------------------------------------------+
| **<** / **>**             | Select the item; with the modifier, step through     |
|                           | your favourites                                      |
+---------------------------+------------------------------------------------------+
| Digits, **INC** / **DEC** | Set the quantity, from 1 to 999; **INC** and **DEC** |
|                           | step by 1, or by 10 with the modifier                |
+---------------------------+------------------------------------------------------+
| **F2** or **ENT**         | Adds the job                                         |
+---------------------------+------------------------------------------------------+
| **TAB**                   | Selects the next job in the list                     |
+---------------------------+------------------------------------------------------+
| **F3**                    | Marks or unmarks the item as a favourite (up to 40); |
|                           | with the modifier, switches the printer on or off    |
+---------------------------+------------------------------------------------------+
| **F4**                    | Removes the selected job                             |
+---------------------------+------------------------------------------------------+
| **F5**                    | Clears every job on the printer                      |
+---------------------------+------------------------------------------------------+

5.18.3 Queueing a print job
---------------------------
**Requirements:** The printer must be on the rack's data network and have a recipe for the item.

1. Press **F1** until the printer you want is selected.
2. Select the item with **<** and **>**.
3. Type the quantity.
4. Press **ENT** to add the job.

**Result:** The job appears in the list, and the event log records what was queued and where.

5.18.4 How jobs run
-------------------
Jobs go into the printer's own instruction memory, up to 255 items per entry, so the printer works through them by itself. If someone changes the printer's recipe by hand, the rack notices within three checks, stops that job and logs it, on the reasonable assumption that the person at the printer knows what they want.
