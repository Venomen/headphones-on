#!/usr/bin/env bash
#
#  Copyright (c) 2020 - Dawid Deręgowski @ deregowski.net

# import main options

source <(grep json_dump config.ini)
source <(grep status_dump config.ini)
source <(grep check_ip config.ini)
source <(grep work_ip config.ini)
source <(grep run_python config.ini)

# start all
echo -e "\xf0\x9f\x8e\xa7 headphones-on | checking your head ;-). CTRL+C to stop. \xf0\x9f\x8e\xa7"

  while True; do
    if [[ $(curl -s "$check_ip") == "$work_ip" ]]; then
      system_profiler -json SPBluetoothDataType 1> "$json_dump" 2>/dev/null
      python3 $run_python
    else
      echo "Ups, you are not in work..."
    fi
    sleep 5;
  done ;
