#!/usr/bin/env bash
set -u

export TZ=Asia/Seoul

while true; do
  hour=$((10#$(date +%H)))
  minute=$((10#$(date +%M)))
  second=$((10#$(date +%S)))

  if (( (hour >= 15 || hour < 1) && minute % 10 == 0 && second < 10 )); then
    printf '[*] Connecting at %s\n' "$(date +'%Y-%m-%d %H:%M:%S %Z')"
    nc dju-ctf.com 9014 | tee timegate_out.txt
    exit 0
  fi

  sleep 0.2
done

