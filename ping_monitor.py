import subprocess

host = input("Enter the host to ping: ")
result = subprocess.run(['ping', "-n", "1", host], capture_output=True, text=True)

if result.returncode == 0:
    print("ONLINE")
else:
    print("OFFLINE")
    
print(result.stdout)
print(type(result.stdout))
print(result.returncode)