import logging
import platform
import subprocess

logger = logging.getLogger(__name__)

PING_CMD = "ping -{} 1 {}"
WINDOWS_OS = "n"
OTHER_OS = "c"
WINDOWS = "windows"

def isPingOk(hostOrIP):
    try:
        option = WINDOWS_OS if platform.system().lower() == WINDOWS else OTHER_OS
        logger.debug("Ping option value: %s", option)
        output = subprocess.check_output(PING_CMD.format(option, hostOrIP), shell=True)
    except Exception as e:
        logger.error("Exception while executing ping for Host or IP %s: %s", hostOrIP, e)
        return False

    return True