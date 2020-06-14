from concurrent.futures.thread import ThreadPoolExecutor

from net_util.ntp import ntputil

NO_OF_POOL = 300

def getAllNTPStatusList(ips):
    """Function to get the result using python multi threading"""
    executor = ThreadPoolExecutor(NO_OF_POOL)
    results = executor.map(getNTPResponse, ips)
    datalist = list(results)
    return datalist;

def getNTPResponse(ip):
    flag = ntputil.isValidNTP(ip)
    responseDict = {ip: flag}
    return responseDict;