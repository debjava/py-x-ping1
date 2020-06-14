import ntplib

ntpClient = ntplib.NTPClient()

def isValidNTP(ipAddress):
    checkFlag = False
    try:
        response = ntpClient.request(ipAddress)
        if response:
            checkFlag = True
    except:
        checkFlag = False

    return checkFlag