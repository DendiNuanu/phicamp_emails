import paramiko
import os

def deploy():
    host = "146.190.90.47"
    port = 22
    username = "root"
    password = "Fujimori6Riho"
    
    local_file = r"c:\phicamp-wifi\phicamp_app.py"
    remote_path = "/var/www/phicamp_emails/phicamp_app.py"
    
    print(f"Connecting to {host}...")
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
        
        print(f"Uploading {local_file} to {remote_path}...")
        sftp = ssh.open_sftp()
        sftp.put(local_file, remote_path)
        sftp.close()
        
        print("File uploaded successfully.")
        
        print("Attempting to restart the application...")
        
        stdin, stdout, stderr = ssh.exec_command("systemctl list-units --type=service | grep phicamp")
        service_info = stdout.read().decode().strip()
        
        if service_info:
            service_name = service_info.split()[0]
            print(f"Detected service: {service_name}. Restarting...")
            ssh.exec_command(f"systemctl restart {service_name}")
        else:
            print("No systemd service detected. Searching for uvicorn processes...")
            ssh.exec_command("pkill -f 'uvicorn phicamp_app:app'")
            print("Starting application from venv...")
            start_cmd = "cd /var/www/phicamp_emails && ./venv/bin/uvicorn phicamp_app:app --host 0.0.0.0 --port 8000 > /dev/null 2>&1 &"
            ssh.exec_command(start_cmd)
        
        print("Deployment completed!")
        ssh.close()
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    deploy()
