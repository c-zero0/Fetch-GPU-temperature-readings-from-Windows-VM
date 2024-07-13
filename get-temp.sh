#!/bin/bash

## original version: https://gist.github.com/jpsutton/8734ce209f7874d5e386d2865c1adc8a

GUEST_NAME=win11 # replace with your VM name

job_exited="false"
exec_result=$(virsh -c qemu:///system qemu-agent-command "$GUEST_NAME" '{"execute": "guest-exec", "arguments": { "path": "C:\\Users\\zero-win11\\AppData\\Local\\Programs\\Python\\Python312\\python.exe", "arg": ["C:\\temps.py"], "capture-output": true }}') # change the path to where python is installed on the windows vm
exec_pid=$(echo "$exec_result" | jq ".return.pid")

while [ "$job_exited" == "false" ]; do
    exec_job_data=$(virsh -c qemu:///system qemu-agent-command "$GUEST_NAME" '{"execute": "guest-exec-status", "arguments": { "pid": '" ${exec_pid}}}")
    job_exited=$(echo "$exec_job_data" | jq '.return.exited')

    if [ "$job_exited" == "false" ]; then
        sleep .1s
        continue
    fi

    echo "$exec_job_data" | jq '.return["out-data"]' | tr -d '"' | base64 --decode
    break
done
