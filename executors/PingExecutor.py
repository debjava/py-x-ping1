import json
import logging
from timeit import default_timer as timer
from net_util.ping import multithreadingping, multiprocessingping

logger = logging.getLogger(__name__)

PING_CMD = "ping"
REACH_CMD = "reach"

def executeByMultiThreading(parsedargs):
    start = timer()
    argsDict = parsedargs.__dict__
    argList = argsDict.get(PING_CMD)
    ipString = argList[0];
    ips = ipString.split(',')
    logger.debug('All IPs: {}'.format(ips))
    resultList = multithreadingping.getAllPingStatusList(ips)
    jsonStr = json.dumps(resultList);
    end = timer()
    result = end - start
    logger.debug("Total Time Taken: %f %s", result, " seconds")
    return jsonStr

def executeByMultiprocessing(parsedargs):
    start = timer()
    argsDict = parsedargs.__dict__
    argList = argsDict.get(REACH_CMD)
    ipString = argList[0];
    ips = ipString.split(',')
    logging.info('All IPs: {}'.format(ips))
    resultList = multiprocessingping.getAllPingDetailsList(ips)
    jsonStr = json.dumps(resultList);
    end = timer()
    result = end - start
    logger.debug("Total Time Taken: %f %s", result, " seconds")
    return jsonStr
