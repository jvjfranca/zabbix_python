from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://192.168.1.80/zabbix")

zapi.login("josevicente","@sonic123")

group_id = '8'
template_id = '10116'
snmp_port = '161'

with open('clientes.txt', 'r')as clientes:
    c = clientes.readlines()
    for row in c:
        lista = (row.strip('\n')).split(',')
        try:
            host_name = str(lista[0])
            host_ip = str(lista[1])
            zapi.host.create({"host": host_name,
                              "interfaces": [{"type": "2",
                                              "main": "1",
                                              "useip": "1",
                                              "ip": host_ip,
                                              "dns": "",
                                              "port": snmp_port}],
                              "groups": [{"groupid": group_id}],
                              "templates": [{"templateid": template_id}]})
        except:
            print("Não foi possivel adicionar o Host")

hosts = zapi.host.get({"output": ["hostid","name"], "sortfield": "name"})
for host in hosts:
    print(host)