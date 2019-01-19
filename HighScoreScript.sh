#!/bin/bash
echo "Starting Arcade"

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

cd "$parent_path"
echo "Starting Attract"


echo "Starting Script"
#python3 $parent_path/modules/rfid/main.py

attract & disown
python3 $parent_path/modules/rfid/main.py &