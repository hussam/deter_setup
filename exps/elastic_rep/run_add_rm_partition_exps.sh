#!/bin/bash

ops=("add" "rm")

for op in ${ops[@]}
do
   exp="$op""_partitions"
   echo "Now starting: $exp"
   ./basho_bench exps/$exp.config
   lastexpto $exp
done
