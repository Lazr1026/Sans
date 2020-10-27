#!/bin/bash
/usr/bin/python3 /home/pi/Sans/sans.py &> /home/pi/ram/err & #needs heavy modification or replacement to work
pid=$!
sleep 10
kill $pid
