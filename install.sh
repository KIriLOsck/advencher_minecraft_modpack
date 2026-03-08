curl https://maven.minecraftforge.net/net/minecraftforge/forge/1.20.1-47.4.16/forge-1.20.1-47.4.16-installer.jar --output server/installer.jar
cd server && java -jar installer.jar --installServer
rm installer.jar