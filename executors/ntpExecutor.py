import json
import logging
from timeit import default_timer as timer

from net_util.ntp import multithreadedntp

logger = logging.getLogger(__name__)

NTP_CMD = "ntp"

def executeByMultiThreading(parsedargs):
    start = timer()
    argsDict = parsedargs.__dict__
    argList = argsDict.get(NTP_CMD)
    ipString = argList[0];
    ips = ipString.split(',')
    logger.debug('All IPs: {}'.format(ips))
    resultList = multithreadedntp.getAllNTPStatusList(ips)
    jsonStr = json.dumps(resultList);
    end = timer()
    result = end - start
    logger.debug("Total Time Taken: %f %s", result, " seconds")
    return jsonStr
