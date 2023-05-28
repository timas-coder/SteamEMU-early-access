# SteamEMU-early-access
This is my new project which focuses on Emulation for the Steam Deck's OS, SteamOS 3.0, maybe even SteamOS 3.5

 T̶h̶i̶s̶ i̶s̶ n̶o̶t̶ r̶e̶a̶d̶y̶ f̶o̶r̶ l̶i̶n̶u̶x̶ y̶e̶t̶ i am making a linux port now, this should be faster as it wont depend on wsl like the windows version. it is windows 11(or above) only.
This based on qemu, python, the recovery image and most importantly , WSL2 (ubuntu)

Windows:

to install it, first open
Turn Windows features on or off
then select Windows subsystem for linux
then restart
then open ps or cmd and type this command
```
wsl --install
```
Linux:

First, install qemu using
```
sudo apt install qemu
```
then clone the repo using
```
git clone https://github.com/timas-coder/SteamEMU-early-access.git
```
