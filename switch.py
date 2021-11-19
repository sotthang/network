from netmiko import ConnectHandler
from openpyxl import load_workbook

'''
excel_file = load_workbook('account.xlsx')
excel_sheet = excel_file['Sheet1']
# account excel open

IP_list = open('devices_ip.txt', 'r')
# switch ip
'''

Dell_S_IP_list = ['1.1.1.1']

Dell_N_IP_list = ['2.2.2.1', '2.2.2.2']

Cisco_IP_list = ['3.3.3.1', '3.3.3.2', '3.3.3.3']

for IP in Dell_S_IP_list:
    switch = {
        'device_type': 'dell_os9',
        'ip': IP.strip(),
        'port': '22',
        'username': 'admin',
        'password': 'password',
        'secret': 'secret',
        'verbose': True
    }
    # switch connect information

    net_connect = ConnectHandler(**switch)
    # switch connect

    output = net_connect.send_command('show run')
    # switch command

    hostname =  net_connect.find_prompt()[:-1]
    with open(f'config/{hostname}.text', 'w') as f:
        f.write(output)
    # save file

for IP in Dell_N_IP_list:
    switch = {
        'device_type': 'dell_os6',
        'ip': IP.strip(),
        'port': '22',
        'username': 'admin',
        'password': 'password',
        'secret': 'secret',
        'verbose': True
    }
    # switch connect information

    net_connect = ConnectHandler(**switch)
    # switch connect

    output = net_connect.send_command('show run')
    # switch command

    hostname =  net_connect.find_prompt()[:-1]
    with open(f'config/{hostname}.text', 'w') as f:
        f.write(output)
    # save file

for IP in Cisco_IP_list:
    switch = {
        'device_type': 'cisco_ios',
        'ip': IP.strip(),
        'port': '22',
        'username': 'admin',
        'password': 'password',
        'secret': 'secret',
        'verbose': True
    }
    # switch connect information

    net_connect = ConnectHandler(**switch)
    # switch connect

    output = net_connect.send_command('show run')
    # switch command

    hostname =  net_connect.find_prompt()[:-1]
    with open(f'config/{hostname}.text', 'w') as f:
        f.write(output)
    # save file
