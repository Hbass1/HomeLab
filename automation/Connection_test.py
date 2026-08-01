from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.0.56',
    'username': 'admin',
    'password': 'cisco',
    'secret': 'cisco',
}

print("Establishing connection to device...")

try:
    connection= ConnectHandler(**cisco_device)

    output = connection.send_command('sh ip int brief')
    print("\n####### Device Output  #######")
    print(output)

    connection.disconnect()
    print("Connection to the device has been closed.")

except Exception as e:
    print(f"An error occurred: {e}")