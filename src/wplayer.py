#!/usr/bin/env python3
# Copyright (C) 2022 Dhanuka Warusadura

import sys
import engine
import ui

def main():
    if len(sys.argv) > 1:
        engine.arg_parse()
    else:
        ui.init()

if __name__ == '__main__':
    main()