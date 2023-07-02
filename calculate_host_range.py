def calculate_host_range(ip_address, subnet_mask):
    ip_parts = ip_address.split('.')
    mask_parts = subnet_mask.split('.')

    # Convert IP address and subnet mask to binary
    ip_binary = ''.join(format(int(part), '08b') for part in ip_parts)
    mask_binary = ''.join(format(int(part), '08b') for part in mask_parts)

    # Calculate the network address by applying the bitwise AND operation
    network_binary = ''.join(str(int(ip_binary[i]) & int(mask_binary[i])) for i in range(len(ip_binary)))

    # Calculate the maximum number of hosts based on the subnet mask
    host_bits = mask_binary.count('0')
    max_hosts = 2 ** host_bits - 2  # Subtract 2 for the network and broadcast addresses

    # Calculate the first and last host addresses in the range
    first_host_binary = network_binary[:-1] + '1'  # Increment the host portion by 1
    last_host_binary = network_binary[:-1] + '1' * host_bits  # Set all host bits to 1

    # Convert the first and last host addresses back to decimal
    first_host_parts = [str(int(first_host_binary[i:i+8], 2)) for i in range(0, len(first_host_binary), 8)]
    last_host_parts = [str(int(last_host_binary[i:i+8], 2)) for i in range(0, len(last_host_binary), 8)]

    first_host = '.'.join(first_host_parts)
    last_host = '.'.join(last_host_parts)

    return (first_host, last_host)

# Example usage
ip_address = '192.168.1.100'
subnet_mask = '255.255.255.0'
first_host, last_host = calculate_host_range(ip_address, subnet_mask)
print("First host:", first_host)
print("Last host:", last_host)
