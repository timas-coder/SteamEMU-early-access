import tkinter as tk
import urllib.request
import subprocess
from tkinter import ttk

def download_progress(count, block_size, total_size):
    percent = int(count * block_size * 100 / total_size)
    progress_bar["value"] = percent
    root.update_idletasks()

def download_file():
    url = "https://steamdeck-images.steamos.cloud/recovery/steamdeck-recovery-4.img.bz2"
    file_name = "steamdeck-recovery-4.img"
    urllib.request.urlretrieve(url, file_name, reporthook=download_progress)

def run_command1():
    subprocess.run(['qemu-img create -f qcow2 steamos.qcow2 64G'])

def run_command2():
    subprocess.run(['qemu-img create -f qcow2 steamos.qcow2 256G'])

def run_command3():
    subprocess.run(['sudo qemu-system-x86_64 -enable-kvm -smp cores=4 -m 8G \
    -device usb-ehci -device usb-tablet \
    -device intel-hda -device hda-duplex \
    -device VGA,xres=1280,yres=800 \
    -drive if=pflash,format=raw,readonly=on,file=/usr/share/ovmf/OVMF.fd \
    -drive if=virtio,file=steamdeck-recovery-4.img,driver=raw \
    -device nvme,drive=drive0,serial=badbeef \
    -drive if=none,id=drive0,file=steamos.qcow2'])

def run_command4():
    subprocess.run(['echo', 'Right, dont spam issues saying this dosent work, it not implemented yet, like i said, this isnt a error so dont try running it again'])

root = tk.Tk()

progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(pady=10)

download_button = tk.Button(root, text="Download Recovery image", command=download_file)
download_button.pack()

command_button1 = tk.Button(root, text="SteamOS 64G", command=run_command1)
command_button1.pack()

command_button2 = tk.Button(root, text="SteamOS 256G", command=run_command2)
command_button2.pack()

command_button3 = tk.Button(root, text="Run steamOS installation", command=run_command3)
command_button3.pack()

command_button4 = tk.Button(root, text="Run steamOS Main", command=run_command4)
command_button4.pack()

root.mainloop()
