#!/bin/bash
echo "Starting Arcade"

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

cd "$parent_path"
echo "Starting Attract"
attract & disown

echo "Starting Script"
python3 $parent_path/modules/rfid/main.py &