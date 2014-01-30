#!/usr/bin/python

import sys,os

sizes = [ 2 ]

ops = ['read', 'write']

template = ""
with open("config.template", "r") as f:
   template = "".join(f.readlines())

for op in ops:
   for s in sizes: 
      Fname = "singleton_" + op + "_" + str(s) + "k.config"
      if os.path.exists(Fname): os.remove(Fname)
      with open(Fname, "w") as f:
         config = template.replace(
            "VALUE_SIZE", str(int(1024 * s))).replace(
            "OP", op)
         f.write(config)
