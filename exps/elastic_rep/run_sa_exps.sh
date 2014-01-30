#!/bin/bash

ops=("read" "write")

for op in ${ops[@]}
do
   exp="sa_$op"
   echo "Now starting: $exp"
   ./basho_bench exps/$exp.config
   lastexpto $exp
done
