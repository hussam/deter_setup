#!/usr/bin/python

import sys,os

hosts = [
         "'10.1.1.3'",
         "'10.1.1.4'",
         "'10.1.1.5'",
         "'10.1.1.6'",
         "'10.1.1.7'"
        ]

specs = {
   'chain'        : """{rsm, chain, [], [
                           'rets@10.1.1.3',
                           REM_REPLICAS
                        ]}""",

   'quorum'       : """{rsm, quorum, [shuffle], [
                           'rets@10.1.1.3',
                           REM_REPLICAS
                        ]}""",

   'fullquorum'   : """{rsm, quorum, [shuffle, {r,1}, {w, N}], [
                           'rets@10.1.1.3',
                           REM_REPLICAS
                        ]}""",

   'hybrid'       : """{rsm, chain, [], [
                           'rets@10.1.1.3',
                           {rsm, quorum, [shuffle, {r,1}, {w, M}], [
                              REM_REPLICAS
                           ]}
                        ]}"""
   }

ops = ['read', 'write']

num_replicas = [3, 4, 5]


template = ""
with open("config.template", "r") as f:
   template = "".join(f.readlines())

for n in num_replicas:
   for op in ops:
      for exp, spec in specs.iteritems():
         m = n-1
         rem_replicas = ",".join(map(lambda h: "'rets@" + h[1:], hosts[1:n]))

         Fname = exp + "_" + op + "_" + str(n) + ".config"
         if os.path.exists(Fname): os.remove(Fname)
         with open(Fname, "w") as f:
            config = template.replace(
               "HOSTS", ",".join(hosts[0:n])).replace(
               "SPEC", spec.replace(
                     "REM_REPLICAS", rem_replicas).replace(
                     "N", str(n)).replace(
                     "M", str(m))
                  ).replace(
               "OP", op)
            f.write(config)
