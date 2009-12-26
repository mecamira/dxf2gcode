# -*- coding: iso-8859-15 -*-
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
'''

Container for global variables accessible to all classes

Michael Haberler  20.12.2009
'''
import os
import sys
import gettext
import locale
import constants




# logger instance, see http://docs.python.org/library/logging.html
# once set, use as logger.error("foo")
logger = None

# GlobalConfig instance
config = None


# PluginLoader, Varspace
plugins =  dict()   # plugin instances keyed by instance name


#-------------------------------------

# determine Platform
platform = ""  
if os.name == "posix" and sys.platform == "darwin":
    platform = "mac"
# TODO - windows test
# TODO - linux test

# Appearance - see NotebookClass
# on macs/linux the notbook buttons need a character headroom 
# to display the label properly
# on windows the come out fine with 0 
if platform is "mac":
    NOTEBOOK_BUTTON_EXTRASPACE = 1
else:
    NOTEBOOK_BUTTON_EXTRASPACE = 0


# Language support
# 
langs = []  # list of supported languages

# figure default language
lc, encoding = locale.getdefaultlocale()

if (lc):
    langs = [lc]    # if there's one, use as default

language = os.environ.get('LANGUAGE', None)
if (language):
    """langage comes back something like en_CA:en_US:en_GB:en
    on linuxy systems, on Win32 it's nothing, so we need to
    split it up into a list"""
    langs += language.split(":")

"""Now add on to the back of the list the translations that we
know that we have, our defaults"""
langs += []

"""Now langs is a list of all of the languages that we are going
to try to use.  First we check the default, then what the system
told us, and finally the 'known' list"""

gettext.bindtextdomain(constants.APPNAME, os.path.realpath(os.path.dirname(sys.argv[0])))
gettext.textdomain(constants.APPNAME)
# Get the language to use
trans = gettext.translation(constants.APPNAME, localedir='languages', languages=langs, fallback = True)
trans.install()

