#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""
MIT License
Copyright (c) 2016-2018 Pierre-Yves Lapersonne (Mail: dev@pylapersonne.info)
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
# ✿✿✿✿ ʕ •ᴥ•ʔ/ ︻デ═一

"""
File.......: client3.py
Brief......: The Python client to use soa s to drive the Tapster2 bot
Author.....: Pierre-Yves Lapersonne
Version....: 2.0.1
Since......: 10/01/2018
"""

import argparse
import sys

import glue3
from config3 import *
from commands_parser3 import *

if __name__ == "__main__":

    # Check args if this execution is a "light" execution, i.e. without verbatims
    parser = argparse.ArgumentParser(description='Python client for Tapster2 robot.')
    parser.add_argument('--url', dest='robotserverurl', help="The URL of the robot's server", required=False)
    parser.add_argument('--light', dest='command', help='Run in light mode, i.e. without verbatims nor prompts.', required=False)
    parser.add_argument('--file', dest='commandsfile', help='Load a file at this path containing a list of commands to process seperated by a line break.', required=False)
    parser.add_argument('--version', action='version', help='Displays the version of this program.', version='%(prog)s '+CLIENT_VERSION)
    args = parser.parse_args()

    if args.robotserverurl:
        config3.ROBOT_URL = args.robotserverurl
    else:
        config3.ROBOT_URL = DEFAULT_ROBOT_URL

# In this case we are in light mode

    if args.command:
        if not checkRobotConnection():
            sys.exit()
        command = args.command
        if isRobotCommand(command):
            parseCommand(command)
        elif glue3.isHelpCommand(command):
            glue3.help()
        elif glue3.isConfigCommand(command):
            glue3.config()
        else:
            print ("ERROR: Bad command: '" + command + "'")
        sys.exit()

# In this case we are in commandsfile mode

    if args.commandsfile:
        if not checkRobotConnection():
            sys.exit()
        pathOfFile = args.commandsfile
        if glue3.checkFile(pathOfFile):
            print ("Will process file: '" + pathOfFile + "'")
            glue3.processCommandsFile(pathOfFile)
        else:
            print ("ERROR: File not found: '" + commandsFile + "'")
        sys.exit()

# In that case we are in verbose / interactive mode

    # Welcome guys!
    print ("Version " + CLIENT_VERSION)
    glue3.welcome()

    checkRobotConnection()

    # Some help?
    glue3.help()

    # Deal with commands
    stop = False
    lastCommand = None
    while not stop:
        command = glue3.askForCommand()
        if glue3.isRepeatCommand(command):
            command = lastCommand
        if isRobotCommand(command):
            parseCommand( command )
        elif glue3.isHelpCommand(command):
            glue3.help()
        elif glue3.isConfigCommand(command):
            glue3.config()
        elif glue3.isStopCommand(command):
            stop = True
        else:
            print ("Nope. Bad command: '" + command + "'")
        lastCommand = command
    # Bye!
    print ("Ok, bye!")
