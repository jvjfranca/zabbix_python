# Script Name	: zabbix_groups.py
# Author		: Jose Vicente Jonas Franca
# Created		: 10 Jun 2016
# Description   : Create Users Groups in Zabbix reading a txt file using the Zabbix API

# import zabbix_api
from zabbix_api import ZabbixAPI

# set the zabbix server
zapi = ZabbixAPI(server="http://192.168.1.80/zabbix")

# login into zabbix server using username and password
zapi.login("user","password")

# read the lines from grupos.txt then create the User Group with the name in the line
with open('grupos.txt', 'r')as clientes: # open the file as clientes
    c = clientes.readlines() # read the lines from the file
    for row in c: # for each row in c
        lista = (row.strip('\n')).split(',') # strip the new lines and split the comma
        try:
            group_name = str(lista[0]) # get the group name
            zapi.usergroup.create({"name": group_name}) # create the user group name
            print("[+] User Group {} successfully created".format(group_name))
        except:
            print("[-] It was not possible to create the User Group")
