import os
import psutil

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

RECEIVED_FILES = os.path.join(DIR_PATH, 'received_files')

RESOURCES_PATH = os.path.join(DIR_PATH,'Resources')

APP_LOG = os.path.join(RESOURCES_PATH, 'app.log')

CLIENT_LOG = os.path.join(DIR_PATH,'Client','client.log')

OS_TYPE = os.name

disk_usage = ''

if OS_TYPE == 'posix':
    disk_usage = psutil.disk_usage('/')
else:
    disk_usage = psutil.disk_usage('C:\\')

FREE_SPACE = disk_usage.free
