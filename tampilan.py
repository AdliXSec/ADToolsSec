import os
import platform



if platform.system() == 'Windows':
    hapus = 'cls'
else:
    hapus = 'clear'

def tampilan():
    os.system(hapus)
    os.system("color a")
    print(" =======================================================================")
    print(" #                                                                     #")                                                                    
    print(" #             _____    _______          _        _____                #")
    print(" #       /\   |  __ \  |__   __|        | |      / ____|               #")
    print(" #      /  \  | |  | |    | | ___   ___ | |___  | (___   ___  ___      #")
    print(" #     / /\ \ | |  | |    | |/ _ \ / _ \| / __|  \___ \ / _ \/ __|     #")
    print(" #    / ____ \| |__| |    | | (_) | (_) | \__ \  ____) |  __/ (__      #")
    print(" #   /_/    \_\_____/     |_|\___/ \___/|_|___/ |_____/ \___|\___|     #")
    print(" #   -------------------------------------------------------------     #")
    print(" #    Author : AdliXSec                                       v2.0     #")
    print(" #    Team   : Dark Clown Security                                     #")
    print(" #                                                                     #")
    print(" #                                                                     #")
    print(" #    Info:                            Note:                           #")
    print(" #    - Only Windows 10                - Don't Copy This Code          #")
    print(" #    - Use Python3 Not Python2        - Don't Recode This Tools       #")
    print(" #                                                                     #")
    print(" #                             Indonesian                              #")
    print(" =======================================================================")
    
def infouser():
    print("\n")
    print(" ========================= Information User ============================")
    print(" #                                                                     #")  
    print(" #   OS                    : ",platform.system())
    print(" #   Processor             : ",platform.processor())
    print(" #   Machine               : ",platform.machine())
    print(" #   System's network name : ",platform.node())
    print(" #   Platform Information  : ",platform.platform())
    print(" #                                                                     #")
    print(" =======================================================================")
