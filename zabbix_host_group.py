from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://192.168.1.80/zabbix")

zapi.login("josevicente","@sonic123")

with open('host_groups.txt', 'r')as clientes:
    c = clientes.readlines()
    for row in c:
        lista = (row.strip('\n')).split(',')
        try:
            group_name = str(lista[0])
            zapi.hostgroup.create({"name": group_name})
        except:
            print("Não foi possivel adicionar o Grupo")