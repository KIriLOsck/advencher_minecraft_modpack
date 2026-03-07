import requests
import subprocess
import os

try:
    with open("cache.txt", "r", encoding="utf-8") as file:
        cached_tag = file.read()
except FileNotFoundError:
    cached_tag = "none"

url = "https://api.github.com/repos/Kostya0Sim/HBMCore/releases/latest"
response = requests.get(url).json()
last_tag = response.get("tag_name")

print(last_tag, "/", cached_tag)

if cached_tag != last_tag:
    print(f"Downloading from ' https://github.com/Kostya0Sim/HBMCore/releases/download/{last_tag}/server_mods.tar.gz '...")
    subprocess.run(["rm", "-rf", "server/mods"])
    subprocess.run([
        "curl", "-L", "-o", "last.tar.gz", f"https://github.com/Kostya0Sim/HBMCore/releases/download/{last_tag}/server_mods.tar.gz"
    ])
    subprocess.run(["tar", "-xzvf", "last.tar.gz", "-C", "server/"])
    subprocess.run(["rm", "last.tar.gz"])

    with open("cache.txt", "w", encoding="utf-8") as file:
        file.write(last_tag)

    print("Update succesfully!")
else:
    print("Already up to date!")

print("Checking if server-core exist...")
files = os.listdir("server")
if "minecraft_server.1.12.2.jar" in files:
    print("Done!")
else:
    print("Not exist! Downloading...")
    subprocess.run(["sh", "install.sh"])
    print("Done!")