import requests
import subprocess
import os

REPO = "KIriLOsck/advencher_minecraft_modpack"

try:
    with open("modpack.cache", "r", encoding="utf-8") as file:
        cached_tag = file.read()
except FileNotFoundError:
    cached_tag = "none"

url = f"https://api.github.com/repos/{REPO}/releases/latest"
response = requests.get(url).json()
last_tag = response.get("tag_name")

print(last_tag, "/", cached_tag)

if cached_tag != last_tag:
    print(f"Downloading from ' https://github.com/{REPO}/releases/download/{last_tag}/server_mods.tar.gz '...")

    subprocess.run(["rm", "-rf", "server/mods"])
    subprocess.run(["rm", "-rf", "server/config"])
    subprocess.run(["rm", "-rf", "server/scripts"])

    subprocess.run([
        "curl", "-L", "-o", "last.tar.gz", f"https://github.com/{REPO}/releases/download/{last_tag}/server_mods.tar.xz"
    ])
    subprocess.run(["tar", "-xJvf", "last.tar.xz", "-C", "server/", "--strip-components=1"])
    subprocess.run(["rm", "last.tar.gz"])

    with open("modpack.cache", "w", encoding="utf-8") as file:
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