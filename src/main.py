# Copyright (C) 2022 Dhanuka Warusadura

import sys
import wplayer
import ui

def main():
    if len(sys.argv) > 1:
        wplayer.arg_parse()
    else:
        ui.init()

if __name__ == '__main__':
    main()
