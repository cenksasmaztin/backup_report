import paramiko
import time
import os
import argparse
from datetime import datetime
import difflib
import re

# SSH bağlantısı fonksiyonu
def ssh_connect(ip, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
    return client

# Gereksiz veya değişken satırları kaldıran bir filtre fonksiyonu
def filter_config(config):
    filtered_config = []
    for line in config.splitlines():
        if "uptime" in line or "timestamp" in line or re.search(r"wpa\s+key|auth\s+key|session\s+key", line, re.IGNORECASE):
            continue
        filtered_config.append(line.strip())  # Boşlukları kaldırarak satır ekle
    return "\n".join(filtered_config)

# Cihazdan konfigürasyon çekme fonksiyonu (stdout ve stderr birleştirildi)
def get_config(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    time.sleep(5)
    stdout.channel.recv_exit_status()
    output = stdout.read().decode('utf-8') + stderr.read().decode('utf-8')  # stdout ve stderr birleştirildi
    return filter_config(output)  # Filtrelenmiş çıktıyı döndür

# İlk yedekleme işlemi
def initial_backup(ip, username, password, command):
    client = ssh_connect(ip, username, password)
    config = get_config(client, command)
    client.close()
    backup_dir = "backup"
    os.makedirs(backup_dir, exist_ok=True)
    with open(f"{backup_dir}/{ip}_initial_config.txt", "w") as file:
        file.write(config)
    print(f"Initial backup for {ip} completed.")
    return config

# Değişiklikleri izleme fonksiyonu
def monitor_changes(ip, username, password, command):
    client = ssh_connect(ip, username, password)
    initial_config_path = f"backup/{ip}_initial_config.txt"
    
    while True:
        current_config = get_config(client, command)
        with open(initial_config_path, "r") as file:
            initial_config = file.read()
        
        if initial_config != current_config:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            update_dir = "backup"
            os.makedirs(update_dir, exist_ok=True)
            update_path = f"{update_dir}/{ip}_update_{timestamp}.txt"
            
            with open(update_path, "w") as file:
                file.write(current_config)
            
            # Değişikliklerin farkını almak
            diff = difflib.unified_diff(
                initial_config.splitlines(),
                current_config.splitlines(),
                lineterm=""
            )
            diff_output = "\n".join(diff)
            
            # Değişiklik kaydı
            log_path = f"{update_dir}/{ip}_change_log_{timestamp}.txt"
            with open(log_path, "w") as log_file:
                log_file.write(f"Changes detected at {timestamp}\n\n{diff_output}")
            
            print(f"Change detected for {ip} - backup and log saved.")
        
        time.sleep(300)

# Komut satırı argümanları ayarlama
def main():
    parser = argparse.ArgumentParser(description="Network device configuration backup tool")
    parser.add_argument("-i", "--ip", required=True, help="Comma-separated list of device IP addresses")
    parser.add_argument("-u", "--username", required=True, help="SSH username")
    parser.add_argument("-p", "--password", required=True, help="SSH password")
    parser.add_argument("-c", "--command", default="show running-config", help="Command to retrieve configuration")
    
    args = parser.parse_args()
    
    # IP listesini virgülle ayırarak bir diziye çevirme
    ip_addresses = args.ip.split(",")
    
    # Her IP adresi için backup ve değişiklik izleme işlemlerini başlatma
    for ip in ip_addresses:
        initial_backup(ip.strip(), args.username, args.password, args.command)
        monitor_changes(ip.strip(), args.username, args.password, args.command)

if __name__ == "__main__":
    main()
