from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://192.168.1.80/zabbix")

zapi.login("user","password")

with open('users.txt', 'r')as clientes:
    c = clientes.readlines()
    for row in c:
        lista = (row.strip('\n')).split(',')
        try:
            user_name = str(lista[0])
            user_mail = str(lista[1])
            zapi.user.create({"alias": user_name,
                              "passwd":"@Trocar123",
                              "usrgrps":[{
                                  "usrgrpid": "14"
                              }],
                              "user_medias": [
                                  {
                                      "mediatypeid": "1",
                                      "sendto": user_mail,
                                      "active": 0,
                                      "severity": 63,
                                      "period": "1-7,00:00-24:00"
                                  }
                              ]})
        except:
            print("Não foi possivel adicionar o Usuario")