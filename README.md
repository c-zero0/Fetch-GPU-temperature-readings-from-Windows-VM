Description:

    This guide helps fetch the hotspot and memory junction temperatures of a gpu passed-through to a Windows VM (in this case an AMD gpu) into 2 .txt files compatible with CoolerControl, so these sensors could be added as custom ones and seen by the host while the VM is on.

    This is done by running a python script on the VM which gets the temperatures ("to_be_copied_to_windows_vm/temps.py") via virsh and qemu-agent from the host ("write-temp.py" writes the temperatures to "/tmp/gpu_hotspot_temperature.txt" and "/tmp/gpu_memory_junction_temperature.txt" gathered from "/tmp/temps.txt", which is the redirected output of "get-temp.sh"). "loop_write_temp" just runs this indefinitely.

Requirements:

    Python3 - host & guest
    jq - host
    WMI py module - guest (pip install WMI)

Guide:

    1. Add this to your guest libvirt xml:

        <channel type="unix">
        <target type="virtio" name="org.qemu.guest_agent.0"/>
        <address type="virtio-serial" controller="0" bus="0" port="1"/>
        </channel>

    2. Copy to_be_copied_to_windows_vm/temps.py to guest in C:\
    3. Install Qemu Guest Agent (virtio-win iso with drivers at "https://github.com/virtio-win/virtio-win-pkg-scripts/blob/master/README.md" - guest agent is in the guest-agent folder)
    4. Download & run Open Hardware Monitor ("https://openhardwaremonitor.org/downloads/")
    5. Edit the scripts as needed for the sensors you need (for reference, here was used a 5700xt and were fetched the core hotspot and memory junction temperatures).
    6. cd to the folder where the scripts were downloaded, edit the 'GUEST_NAME' variable from "get-temp.sh" with the name of your VM & run loop_write_temp.sh as root (if you can run virsh commands without root, run ./loop_write_temp.sh --no-sudo)
    7. Now create the custom sensors in CoolerControl for the Hotspot and Memory Junction located at "/tmp/gpu_hotspot_temperature.txt" and "/tmp/gpu_memory_junction_temperature.txt"

Many thanks to the guy who wrote https://gist.github.com/jpsutton/8734ce209f7874d5e386d2865c1adc8a and chatgpt
