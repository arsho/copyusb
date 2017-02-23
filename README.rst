Copyusb
--------
Copy connected USB media device to current script directory.
The copy() method will return a list with the path where the USB drive being copied.

DO NOT MISUSE IT FOR STEALING DATA.

The current version can be used only with Python 3. Tested on Windows(10) and Ubuntu(16.04 LTS).

To install (in Ubuntu having both Python2 and Python3 by default)::

    >>> sudo pip3 install copyusb

To install (in Windows with which has only Python 3 installed)::

    >>> sudo pip install copyusb

To use (with caution), simply do::

    >>> import copyusb
    >>> copy_result_list = copyusb.copy()

This will return a list with the destination path where the USB media device data has been copied.
No matter how many USB media device is connected, this program will copy all of them.
