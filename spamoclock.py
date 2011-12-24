#! /usr/bin/python
# python ncurses library http://docs.python.org/howto/curses.html
import curses

# call up a curses screen or window 
stdscr = curses.initscr()


curses.noecho() # turns of automatic echoing of keys to screen 
curses.cbreak() # makes curses react to keys instantly w/o enter key,cbreak mode
stdscr.keypad(1)# special cursor & nav keys get return values to curses


begin_x = 20 ; begin_y = 7
heigh = 5; width = 40
win = curses.newwin(heigh,width,begin_y,begin_x) #note coord syntax is (y,x)

#content
str_hellow ="hellow"
addstr(str_hellow)
addstr('this is the world')

curses.nocbreak(); stdscr.keypad(0); curses.echo()

curses.endwin()