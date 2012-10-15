################################################################################
#      This file is part of OpenELEC - http://www.openelec.tv
#      Copyright (C) 2009-2012 Stephan Raue (stephan@openelec.tv)
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with OpenELEC.tv; see the file COPYING.  If not, write to
#  the Free Software Foundation, 51 Franklin Street, Suite 500, Boston, MA 02110, USA.
#  http://www.gnu.org/copyleft/gpl.html
################################################################################

import os
import sys
import xbmcaddon
import time
import subprocess
import logging

__scriptname__ = "Google Chrome Browser"
__author__     = "OpenELEC"
__url__        = "http://www.openelec.tv"
__settings__   = xbmcaddon.Addon(id='web.browser.google.chrome')
cwd = __settings__.getAddonInfo('path')

logfile = xbmc.translatePath( os.path.join(cwd, 'google.chrome.log') )
logging.basicConfig(filename=logfile,level=logging.DEBUG)

# During installation get the file from
# http://dl.google.com/linux/chrome/deb/dists/stable/Release
# http://dl.google.com/linux/chrome/deb/dists/stable/main/binary-i386/Packages
# http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_22.0.1229.94-r161065_i386.deb

# During installation execute the following comand to get the icon
# ln -s opt/google/chrome/product_logo_128.png icon.png

# During installation, make sure
# ref.: https://groups.google.com/a/chromium.org/forum/?fromgroups=#!topic/chromium-dev/nKMlqRSqvrE
# chown root:root opt/google/chrome/chrome
# chown root:root opt/google/chrome/chrome-sandbox
# chmod 4755 opt/google/chrome/chrome-sandbox


def startGoogleChrome():
    
    try:
        # Determine the location of the google-chrome wrapper
        wrappercmd = xbmc.translatePath( os.path.join(cwd, 'google-chrome') )
        
        # Determine the location for the user data, since the application is run as root
        userdatadir = xbmc.translatePath( os.path.join(cwd, 'DATADIR') )

        args = [wrappercmd, '--user-data-dir', userdatadir]

        subprocess.Popen(args)
    except e: 
        logging.error(e.strerror)

    while (not xbmc.abortRequested):
      time.sleep(0.250)

# Call the main function
startGoogleChrome()
