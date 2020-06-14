from multiprocessing import Pool

from net_util.ping import pingutil

NO_OF_PROCESS = 20


def getAllPingDetailsList(ips):
    pool = Pool(processes=NO_OF_PROCESS)
    result = pool.map_async(getIPPingStatus, ips)
    pool.close()
    dataList = result.get()
    return dataList;


def getIPPingStatus(ip):
    flag = pingutil.isPingOk(ip);
    responseDict = {ip: flag}
    return responseDict;
