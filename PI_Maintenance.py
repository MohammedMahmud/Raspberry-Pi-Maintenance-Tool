import os
from datetime import datetime
import argparse
import subprocess

now = datetime.now()
current_time = now.strftime('%I:%M')


def call_update_and_upgrade_all():
    # Free some space's
    os.system("sudo apt-get clean")
    # update!!
    os.system("sudo apt-get update")
    # upgrade
    subprocess.check_output("sudo apt-get dist-upgrade", shell=True)

    os.system('sudo apt-get autoremove')
    return "Done"


def future_time_task_now(future_time):
    while True:
        if str(current_time) == future_time:
            return call_update_and_upgrade_all()
        else:
            print("Its Not Time Yet")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--ChangeTime", help="This time Maintenance will be begin EX: "+current_time, type=str)
    parser.add_argument("-n", "--Now", help="This will check NOW... Immediately", action="store_true")
    args = parser.parse_args()

    if args.ChangeTime:
        res = future_time_task_now(args.ChangeTime)
        print(res)
    elif args.Now:
        call_update_and_upgrade_all()


if __name__ == '__main__':
    try:
        print(main())
    except SystemExit as e:
        print(e)

