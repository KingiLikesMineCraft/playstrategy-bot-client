import pytest
import shutil
import os


def pytest_sessionfinish(session, exitstatus):
    shutil.copyfile("correct_playstrategy.py", "playstrategy.py")
    os.remove("correct_playstrategy.py")
    if os.path.exists("TEMP"):
        shutil.rmtree("TEMP")
    if os.path.exists("logs"):
        shutil.rmtree("logs")
