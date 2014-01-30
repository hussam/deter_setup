#!/bin/bash

ops=("read" "write")
num_replicas=( 3  5  7 9 11 )

for op in ${ops[@]}
do
   for n in ${num_replicas[@]}
   do
      exp="quorum_$op""_$n"
      echo "Now starting: $exp"
      ./basho_bench exps/$exp.config
      lastexpto $exp
   done
done
