import paramiko
import time

# VPS details
HOST = "49.50.113.25"
USERNAME = "root"
PASSWORD = "UWbXTV*8y!w3N3y"

# Command to run on the VPS
COMMAND = "your_command_here"  # Ganti dengan command yang mau dijalankan di VPS

def connect_and_run():
    try:
        # Initialize SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(HOST, username=USERNAME, password=PASSWORD)

        print(f"Connected to {HOST}")
        while True:
            stdin, stdout, stderr = ssh.exec_command(COMMAND)
            print(stdout.read().decode())
            print(stderr.read().decode())

            # Wait 15 minutes before re-running the command
            time.sleep(900)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        ssh.close()
        print("Connection closed.")

if __name__ == "__main__":
    connect_and_run()
