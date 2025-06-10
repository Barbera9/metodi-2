import curses
import subprocess
import os


def menu(stdscr):
    #disattiva cursore
    curses.curs_set(0)
    #opzioni
    options =["Prima Parte","Seconda Parte","Seconda Parte Alt","close"]
    current_sel=0

    while True:
        stdscr.clear()

        #roba per evidenziare la selezione
        for idx, option in enumerate(options):
            if idx == current_sel:
                stdscr.addstr(idx, 0, f"> {option}", curses.A_REVERSE)
            else:
                stdscr.addstr(idx, 0, f"> {option}")    
    
        key = stdscr.getch()   
    
        #gestione movimeto selezione
        if key == curses.KEY_UP and current_sel > 0:
            current_sel -= 1

        elif key == curses.KEY_DOWN and current_sel<(len(options)-1):
            current_sel += 1
        elif key in [curses.KEY_ENTER, 10,13]: #invio

            base_path = os.path.dirname(os.path.abspath(__file__))
       
            if current_sel==0:
               script_path= os.path.join(base_path,"PrimaParte.py")
            elif current_sel==1:
                script_path= os.path.join(base_path, "secondaParte.py")
            elif current_sel ==2:
                script_path= os.path.join(base_path, "secondaParte.py")
                value = "Alt"
            elif current_sel ==3:
                break
            if current_sel != 2:
                subprocess.run(["python",script_path])
            else:
                subprocess.run(["python", script_path, value])

        
        stdscr.refresh()

curses.wrapper(menu)
    
