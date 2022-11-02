#!/bin/bash

# To use this plugin:
# 1. Install xbar (https://github.com/matryer/xbar).
# 2. Download the MacOS executable from the latest release of Claranet4 (https://github.com/bede/claranet4)
# 3. Change the path at the bottom of this file to point to wherever your executable is stored.
# 4. Open xbar, and open your plugins folder. Put this file inside it.
# 5. Open System Preferences -> Security and Privacy and grant xbar permissions for Bluetooth, Automation and Developer Tools

# <xbar.title>Aranet4 CO2 reading</xbar.title>
# <xbar.version>0.1.0</xbar.version>
# <xbar.author>Bede Constantinides</xbar.author>
# <xbar.author.github>bede</xbar.author.github>
# <xbar.desc>Example of how to include items that cycle in the top, and items that only appear in the dropdown.</xbar.desc>
# <xbar.abouturl>https://github.com/bede/claranet4</xbar.abouturl>

echo "$(/Users/bede/Git/claranet4/dist/claranet4-MacOS read --field co2)""ppm"
