import os
import platform



if platform.system() == 'Windows':
    hapus = 'cls'
else:
    hapus = 'clear'


def error():
    os.system(hapus)
    print(" ==================================================================")
    print(" #                                                                #")
    print(" #        ______   _____    _____     ____    _____      __       #")
    print(" #       |  ____| |  __ \  |  __ \   / __ \  |  __ \   _/ /       #")
    print(" #       | |__    | |__) | | |__) | | |  | | | |__) | (_) |       #")
    print(" #       |  __|   |  _  /  |  _  /  | |  | | |  _  /    | |       #")
    print(" #       | |____  | | \ \  | | \ \  | |__| | | \ \ \   _| |       #")
    print(" #       |______| |_|  \_\ |_|  \_\  \____/  |_|  \_\ (_) |       #")
    print(" #                                                      \_\       #")
    print(" #       ---------------------------------------------------      #")
    print(" #                                                                #")
    print(" #            Sorry, this tool is currently under repair,         #")
    print(" #                 sorry for disturbing your time                 #")
    print(" #                                                                #")
    print(" ==================================================================")
    