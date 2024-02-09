import os
import psutil

SERVER_PORT = 8080

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

COMMONS = os.path.join(DIR_PATH, 'Commons')

LOGS = os.path.join(COMMONS, 'logs')

OS_TYPE = os.name

disk_usage = ''

if OS_TYPE == 'posix':
    disk_usage = psutil.disk_usage('/')
else:
    disk_usage = psutil.disk_usage('C:\\')

FREE_SPACE = disk_usage.free
