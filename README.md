# zyxel-flash-dump
Dump the contents of Zyxel switch flash.

This was originally written to dump the contents of a filesystem on a Zyxel GS1900-24HPv2.  It loops over the specified memory range for JFFS2_CFG and saves the output to a file.

# address ranges

``` RTL838x# flshow
=============== FLASH Partition Layout ===============
Index  Name       Size       Address
------------------------------------------------------
 0     LOADER     0x40000    0xb4000000-0xb403ffff
 1     BDINFO     0x10000    0xb4040000-0xb404ffff
 2     SYSINFO    0x10000    0xb4050000-0xb405ffff
 3     JFFS2_CFG  0x100000   0xb4060000-0xb415ffff
 4     JFFS2_LOG  0x100000   0xb4160000-0xb425ffff
 5     RUNTIME1   0x6d0000   0xb4260000-0xb492ffff
 6     RUNTIME2   0x6d0000   0xb4930000-0xb4ffffff
======================================================
```

The default configuration for the minicom.exp script will dump 0xb4060000 - 0xb415ffff.

