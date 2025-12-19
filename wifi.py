import subprocess

def get_wifi_password():
    try:
        # Get the name of the currently connected Wi-Fi
        current_wifi = subprocess.check_output(
            "netsh wlan show interfaces", shell=True, encoding='utf-8'
        )
        for line in current_wifi.split('\n'):
            if "SSID" in line and "BSSID" not in line:
                ssid = line.split(":")[1].strip()
                break
        
        # Retrieve the Wi-Fi password using the SSID
        wifi_details = subprocess.check_output(
            f'netsh wlan show profile "{ssid}" key=clear', shell=True, encoding='utf-8'
        )
        for line in wifi_details.split('\n'):
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                return f"The password for Wi-Fi '{ssid}' is: {password}"
        
        return f"The Wi-Fi '{ssid}' does not have a password or could not retrieve it."
    except Exception as e:
        return f"An error occurred: {e}"

print(get_wifi_password())
