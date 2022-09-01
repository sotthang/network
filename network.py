from netmiko import ConnectHandler
# from openpyxl import load_workbook

'''
# account excel open
excel_file = load_workbook('account.xlsx')
excel_sheet = excel_file['Sheet1']

# switch ip
IP_list = open('devices_ip.txt', 'r')
'''

Dell_S_IP_list = ['1.1.1.1']

Dell_N_IP_list = ['2.2.2.1', '2.2.2.2']

Cisco_IP_list = ['3.3.3.1', '3.3.3.2', '3.3.3.3']


# switch connect information
for IP in Dell_S_IP_list:
    switch = {
        'device_type': 'dell_os9',
        'ip': IP,
        'port': '22',
        'username': 'id',
        'password': 'pw',
        'secret': 'secret',
        'verbose': True
    }
    
    
    # switch connect
    net_connect = ConnectHandler(**switch)
    
    
    # switch command
    output = net_connect.send_command('show run')
    
    
    # save file
    hostname =  net_connect.find_prompt()[:-1]
    with open(f'config/{hostname}.txt', 'w') as f:
        f.write(output)


# switch connect information
for IP in Dell_N_IP_list:
    switch = {
        'device_type': 'dell_os6',
        'ip': IP,
        'port': '22',
        'username': 'id',
        'password': 'pw',
        'secret': 'secret',
        'verbose': True
    }

    
    # switch connect
    net_connect = ConnectHandler(**switch)

    
    # switch command
    output = net_connect.send_command('show run')

    
    # save file
    hostname =  net_connect.find_prompt()[:-1]
    with open(f'config/{hostname}.txt', 'w') as f:
        f.write(output)


# switch connect information
for IP in Cisco_IP_list:
    switch = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'port': '22',
        'username': 'id',
        'password': 'pw',
        'secret': 'secret',
        'verbose': True
    }

    
    # switch connect
    net_connect = ConnectHandler(**switch)

    
    # switch command
    output = net_connect.send_command('show run')

    
    # save file
    hostname =  net_connect.find_prompt()[:-1]
    with open(f'config/{hostname}.txt', 'w') as f:
        f.write(output)

        
