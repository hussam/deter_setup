#!/bin/bash

exp="fail"
echo "Now starting: $exp"
./basho_bench exps/$exp.config
lastexpto $exp
