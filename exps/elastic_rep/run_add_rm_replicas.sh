#!/bin/bash

ops=("add" "rm")

for op in ${ops[@]}
do
   exp="$op""_replicas"
   echo "Now starting: $exp"
   ./basho_bench exps/$exp.config
   lastexpto $exp
done
