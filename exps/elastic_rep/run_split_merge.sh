#!/bin/bash

ops=("split" "merge")

for op in ${ops[@]}
do
   exp=$op
   echo "Now starting: $exp"
   ./basho_bench exps/$exp.config
   lastexpto $exp
done
