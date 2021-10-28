#!/bin/bash

set -e
set -x

source /root/.cargo/env

echo "Starting in 10s..."
sleep 5

while true
do
  sleep 5
  python3 -u Client.py -U ianagbip1oti -P password -S http://web:8080/ -T 1 --syzygy /syzygy || true
  echo "Restarting in 5s..."
done

