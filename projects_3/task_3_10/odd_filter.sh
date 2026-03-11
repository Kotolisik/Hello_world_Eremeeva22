#!/bin/bash

for ((i=1; i<=20; i++)); do
	
    if [ $i -eq 15 ]; then
        echo "число 15!"
        break
    fi
    
    if [ $((i % 2)) -eq 0 ]; then
        continue
    fi
    
    echo "Число: $i"
done
