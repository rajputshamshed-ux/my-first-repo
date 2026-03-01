#!/bin/bash
for i in {0..99}; do
    if [ $i -lt 99 ]; then
        printf "%02d, " $i
    else
        printf "%02d\n" $i
    fi
done
