#!/bin/bash

ops=("read" "write")
num_replicas=( 2 3 4 5 6 )

for op in ${ops[@]}
do
   for n in ${num_replicas[@]}
   do
      exp="er_$op""_$n"
      echo "Now starting: $exp"
      ./basho_bench exps/$exp.config
      lastexpto "chain_$op""_$n"
   done
done
