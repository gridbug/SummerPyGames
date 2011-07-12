#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#       WhateverWeCallTheGame.py
#       
#       Copyright Contributors
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#       
import pygame,threads,menus,levels
from globalvalues import GlobalObjects,Events
pygame.init()
def main():
    menus.init()
    levels.init()
    render=threads.RenderThread()
    render.start()
    eventthread=threads.EventThread()
    eventthread.start()
    def cleanup():
        render.killed.set()
        render.join()
        eventthread.killed.set()
        eventthread.join()
    running = True
    while running:
        with Events.trigger:
            for event in Events.events:
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if not GlobalObjects.escInUse and event.key == pygame.K_ESCAPE:
                        running = False
        with Events.trigger,Events.done:
            Events.trigger.wait()
    cleanup()
    return 0

if __name__ == '__main__':
	main()

