#!/bin/bash

if [ $# -eq 0 ]
then
   echo "Specify experiment folder(s)"
   exit -1
fi

dir=$@
resdir="$(basename $dir)-$(date +"%y_%m_%d-%H:%M")"
mkdir $resdir

for expfile in `ls $dir/*.config`
do
   echo "Now starting: $expfile"
   basho_bench $expfile

   exp=$(basename "$expfile")
   exp="${exp%.*}"
   mv `readlink /usr/er/basho_bench/tests/current` $resdir
done
