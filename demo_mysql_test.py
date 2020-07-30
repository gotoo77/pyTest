# import mysql.connector
import configparser

import mysql

from src.SQLManager import SQLManager
from utils.my_print import cerr

cfg = configparser.ConfigParser()
cfg.read_file(open('config/connexions.ini'))

server1 = cfg.get('DATABASE', 'server1', raw=False)
port1 = cfg.get('DATABASE', 'port1', raw=False)
DB1 = cfg.get('DATABASE', 'DB1', raw=False)
user1 = cfg.get('DATABASE', 'user1', raw=False)
pwd1 = cfg.get('DATABASE', 'pwd1', raw=False)

print("server1=" + server1)
print("port1=" + port1)
print("DB1=" + DB1)
print("user1=" + user1)
print("pwd1=" + pwd1)

sql = SQLManager(server1, port1, user1, pwd1, DB1)
# try:
sql.connect()
# except mysql.connector.errors.ProgrammingError:
#     err("Oops! mysql error")

# sql.show_databases()
sql.select_DTsa("3")

