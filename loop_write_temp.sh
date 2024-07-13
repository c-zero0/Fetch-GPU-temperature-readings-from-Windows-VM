#!/bin/bash

if [[ "$EUID" -ne 0 ]]; then
  if [[ "$1" != "--no-sudo" ]]; then
    echo "If you can run virsh commands without root, usage is ./loop_write_temp.sh --no-sudo, otherwise run this script as root"
    exit
  fi
fi

while true
do
    ./write-temp.py
    sleep 1s
done
