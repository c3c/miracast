Analyzing Chromecast & Miracast devices.
========

Tools for analyzing EZCast / Miracast devices, as part of a project paper.

This repository contains 
  - some xcompiled tools (gdb, netcat) that can be used on mipsel devices such as the Measy A2W (trust us, we didn't backdoor them)
  - a backup of the NAND flash as found on the Measy A2W, potentially containing some helpful kernel modules that may assist in the reverse engineering of some of the underlying USB protocols (all am7x am8x based)
  - a tool by Antionio Ospite to extract firmware details for Actions-Micro devices

Key words: Measy A2W, Miracast, Chromecast, Actions-Micro, AM8251, AM8250, forensics, UART, ADFU, BREC

## Abstract

Google’s Chromecast and Miracast dongles are gadgets that allow
people to stream movies and other media content to an HDMI-capable
device. This paper atempts to ﬁnd out what forensically interesting
information is stored on both devices and how this information can be
retrieved.

The Chromecast makes it diﬃcult to obtain the NAND memory by
encrypting the contents with a unique per device key. Attempts to
retrieve this memory failed. However, contents of crash logs show
that information with absolute timestamps is logged on the device. It
suggests that information, including wireless access points and MAC
addresses, is logged.

The Miracast dongle researched during this project, the Measy A2W, runs the EZCast ﬁrmware. EZCast contains multiple software vulner- abilities that may lead to shell access on similar devices. However, the method used to access the memory and ﬂash on the Measy A2W was via the UART interface. A memory dump could then be retrieved over the network using netcat or via UART using hexdump. The memory of the Miracast contained information including partial images, links of visited websites, and MAC addresses of nearby and connected devices.

**[View paper](https://github.com/c3c/miracast/blob/master/deliverables/paper.pdf?raw=true)**
