Copyusb
--------
Copy connected USB media device to current script directory.
The copy() method will return a list with the path where the USB drive being copied.

DO NOT MISUSE IT FOR STEALING DATA.

N.B.: Currently it only works in Linux machine. 

Tested on Ubuntu 16.04 LTS. The current version can be used only with Python 3.

To install::

    >>> sudo pip3 install copyusb

To use (with caution), simply do::

    >>> import copyusb
    >>> copy_result_list = copyusb.copy()


