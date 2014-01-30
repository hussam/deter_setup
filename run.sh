#!/bin/bash

if [ $# -eq 0 ]
then
   echo "Specify experiment folder(s)"
   exit -1
fi

dir=$@
resdir=results/"$(basename $dir)-$(date +"%y_%m_%d-%H:%M:%S")"
mkdir -p $resdir

for expfile in `ls $dir/*.config`
do
   echo "Now starting: $expfile"
   basho_bench $expfile

   exp=$(basename "$expfile")
   exp="${exp%.*}"
   mv `readlink tests/current` $resdir/$exp
done

rm -r tests    # basho_bench dumps a tests dir in local dir
