#!/bin/sh

exist=`ps aux | grep 'python3 main.py' | grep -v grep | wc -l`
if [ "$exist" != "1" ]; then
    cd /data/openai && python3 main.py
    echo "run chatserver"
fi