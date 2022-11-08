#!/usr/bin/env python3

"""

Author: J.Thomas

Purpose: Moving files around using shutil and os from the standard library

"""

def main()

    import shutil
    import os

    os.chdir("/home/student/mycode")

    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    shutil.copytree("5g_research/", "5g_research_backup/")


if __name__ == "__main__":
        main()

