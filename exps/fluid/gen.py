#!/usr/bin/python

import sys,os

protocols = ["chain", "primary_backup"]

exps = {
#   'wping' : [0.125],
#   'write' : [0.5, 1, 1.5, 2, 2.5, 4, 8, 16]
   'write' : [1,2,4,8]
   }

template = ""
with open("config.template", "r") as f:
   template = "".join(f.readlines())

for p in protocols:
   for op,sizes in exps.iteritems():
      for s in sizes:
         Fname = p + "_" + op + "_" + str(s) + "k.config"
         if os.path.exists(Fname): os.remove(Fname)
         with open(Fname, "w") as f:
            exp = template.replace(
               "PROTOCOL", p).replace(
               "OP", op).replace(
               "VALUE_SIZE", str(int(1024 * s)))
            f.write(exp)
