# Copyright (C) 2022 Dhanuka Warusadura

import sys
import subprocess

def print_help(prog_name):
    print('%s video_file_name' % prog_name)

def arg_parse():
    if len(sys.argv) != 2:
        print_help(sys.argv[0])
        return 1

    subprocess.call(['mplayer', sys.argv[1]])
    return 0

def execute(file_name):
    if file_name is None:
        return 1
    subprocess.call(['mplayer', str(file_name)])
    return 0
