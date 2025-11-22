#!/bin/bash

# To use this plugin:
# 1. Install xbar (https://github.com/matryer/xbar)
# 2. Download the MacOS executable from the latest release of Claranet4 (https://github.com/bede/claranet4)
# 3. Change the path on line 17 below to point to wherever your execuable is stored
# 4. Open xbar, and open your plugins folder. Put this file inside it.
# 5. Open System Preferences -> Security and Privacy and grant xbar permissions for Bluetooth, Automation and Developer Tools

# <xbar.title>Aranet4 CO2 reading</xbar.title>
# <xbar.version>0.1.0</xbar.version>
# <xbar.author>Bede Constantinides</xbar.author>
# <xbar.author.github>bede</xbar.author.github>
# <xbar.desc>Example of how to include items that cycle in the top, and items that only appear in the dropdown.</xbar.desc>
# <xbar.abouturl>https://github.com/bede/claranet4</xbar.abouturl>

# echo "$(claranet4 read --field co2)""ppm CO\u2082"
echo "$(claranet4 read --field co2 390F544C-F0FF-F8BE-3A3A-BB1219AA2145)""ppm CO\u2082"
# echo "$(/Users/bede/Research/git/claranet4/dist/claranet4 read --field co2 390F544C-F0FF-F8BE-3A3A-BB1219AA2145)""ppm CO\u2082"
# echo "$(/Users/bede/Research/git/claranet4/dist/claranet4 read --field temperature 390F544C-F0FF-F8BE-3A3A-BB1219AA2145)""\u00b0"
