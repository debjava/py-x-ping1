from concurrent.futures.thread import ThreadPoolExecutor

from net_util.ping import pingutil

PING_COMMAND = 'ping'
PING_COUNT = '1'
NO_OF_POOL = 300


def getAllPingStatusList(ips):
    """Function to get the result using python multi threading"""
    executor = ThreadPoolExecutor(NO_OF_POOL)
    results = executor.map(getPingResponse, ips)
    datalist = list(results)
    return datalist;


def getPingResponse(ip):
    flag = pingutil.isPingOk(ip)
    responseDict = {ip: flag}
    return responseDict;
