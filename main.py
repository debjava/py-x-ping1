import argparse
import logging
import multiprocessing
import os

from executors import PingExecutor, ntpExecutor

# For File Logging

log_filename = "logs/app.log"
log_format = "%(asctime)s %(levelname)-8s %(name)-20s  %(message)s"
os.makedirs(os.path.dirname(log_filename), exist_ok=True)
logger = logging.getLogger()

# For File Logging

handler = logging.FileHandler(log_filename, "a")
formatter = logging.Formatter(log_format)
formatter.datefmt = "%Y-%m-%d %H:%M:%S"
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# For Console Logging - uncomment below to see the changes in the console

# consoleHandler = logging.StreamHandler()
# consoleHandler.setFormatter(formatter)
# logger.addHandler(consoleHandler)

argParser = argparse.ArgumentParser()


def define_arguments():
    argParser.add_argument('-p', '--ping', nargs="+", help="Ping IP Addresses.")
    argParser.add_argument('-r', '--reach', nargs="+", help="Reach IP Addresses.")
    argParser.add_argument('-t', '--telnet', nargs="+", help="Telnet command")
    argParser.add_argument('-n', '--ntp', nargs="+", help="NTP command")


def run_command():
    define_arguments()
    parsedargs = argParser.parse_args()

    if parsedargs.ping:
        logger.debug("It is ping validation")
        str = PingExecutor.executeByMultiThreading(parsedargs)
        logger.debug("Response in json format:%s", str)
        print(str)
    elif parsedargs.reach:
        logger.debug("It is IP reachability check")
        str = PingExecutor.executeByMultiprocessing(parsedargs)
        logger.debug("Response in json format:%s", str)
        print(str)
    elif parsedargs.ntp:
        logger.debug("It is IP NTP check")
        str = ntpExecutor.executeByMultiThreading(parsedargs)
        logger.debug("Response in json format:%s", str)
        print(str)
    elif parsedargs.telnet:
        logger.debug("It is Telnet")
        commandName = "telnet"


if __name__ == '__main__':
    multiprocessing.freeze_support()
    run_command()
