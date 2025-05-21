#kenobi/scheduler.py

import time
import schedule
import subprocess
import sys


def run_kenobi():
    print("🚀 Running Kenobi pipeline...")
    subprocess.run([sys.executable,"-m", "kenobi.core.kenobi"])


#Schedule to run once every day at 9am
schedule.every().day.at("09:00").do(run_kenobi)

if __name__=="__main__":
    print("📅 Scheduler started. Waiting for scheduled time...")
    while True:
        schedule.run_pending()
        time.sleep(60)