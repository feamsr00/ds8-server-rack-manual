.. _os-editor:

5.10 Editor (Memory Editor)
===========================
Editor is a window onto the rack's memory, for reading and writing single cells by hand. It is program 2 in the Data group. Open it with **EDT**; the **GOTO**, **FIND** and **FILL** keys and the bookmark keys **BM1**–**BM4** also open it, already doing their job.

5.10.1 Screen
-------------

.. image:: /images/os-editor.png
   :alt: Memory Editor at address 0000 in bank 0, served by an empty bay 1, with four columns of ten cells

**Figure 5-7** The cursor at address 0000. The header says that bank 0 is served by bay 1, which is empty, so every cell reads 0.

The Address and Value boxes at the top show the cursor's address and the value in that cell. Below them, four columns of ten show the 40 cells around the cursor, and **TAB** moves between the columns. The header names the bank and what serves it: the bay and the drive's serial number, "no cable", or an empty bay. READ ONLY appears while the bank is write-protected (see :ref:`6 Storage and data handling <ch-storage>`).

5.10.2 Keys
-----------
**Table 5-10** Editor keys

+-------------------------------+--------------------------------------------------+
| Key                           | What it does                                     |
+===============================+==================================================+
| Digits, then **ENT**          | Write the number into the cell under the cursor, |
|                               | then move the cursor on                          |
+-------------------------------+--------------------------------------------------+
| Arrow keys, **PG+** / **PG-** | Move the cursor                                  |
+-------------------------------+--------------------------------------------------+
| **F1** (**GOTO**)             | Goes to an address                               |
+-------------------------------+--------------------------------------------------+
| **F2** (**FIND**)             | Finds a value                                    |
+-------------------------------+--------------------------------------------------+
| **F3** (**ZERO**)             | Zeroes the cell under the cursor                 |
+-------------------------------+--------------------------------------------------+
| **F4** (**FILL**)             | Fills a range of cells with one value            |
+-------------------------------+--------------------------------------------------+
| **F5**                        | Moves to the next bank                           |
+-------------------------------+--------------------------------------------------+
| **BNK-** / **BNK+**           | Move back or forward by one bank                 |
+-------------------------------+--------------------------------------------------+
| **CPY** / **PST**             | Copy and paste a value                           |
+-------------------------------+--------------------------------------------------+
| **INC** / **DEC**             | Add or subtract 1, or 10 with the modifier       |
+-------------------------------+--------------------------------------------------+
| **BM1**–**BM4**               | Jump to a bookmark; hold the modifier to set the |
|                               | bookmark to the cursor instead                   |
+-------------------------------+--------------------------------------------------+

5.10.3 Writing a value to a cell
--------------------------------
**Requirements:** The bank must be served by a drive, and neither the **WP** toggle nor the bank's own switch may be protecting it.

1. Press **F1**, type the address and press **ENT** to move the cursor there.
2. Type the value.
3. Press **ENT**.

**Result:** The value is written, and the cursor moves on to the next cell so that you can keep typing.

5.10.4 Using the editor from IC10
---------------------------------
The editor's cursor is also the rack's ``Index`` logic value, and the cell under it is ``Setting``. A chip elsewhere on the network can therefore move the cursor and read or write that cell without touching memory instructions at all:

.. code-block:: text

	s rack Index 100      # cursor to cell 100
	l r0 rack Setting     # read cell 100
	s rack Setting 42     # write 42 there

Writes from outside the rack need the **REM** switch on and **MAINT** off. Everything else about memory is in :ref:`12 Logic and memory reference <ch-reference>`.
