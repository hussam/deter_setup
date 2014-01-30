#!/usr/bin/python

import sys,os

hosts = [
         "'10.1.1.3'",
         "'10.1.1.4'",
         "'10.1.1.5'",
         "'10.1.1.6'",
         "'10.1.1.7'",
         "'10.1.1.8'"
        ]

exps = {
   'str' : """{psm, shard, [], {rets, route}, [
               {{0, 50}, {rsm, quorum, [{r,1}, {w,3}], [
                  'rets@10.1.1.3',
                  'rets@10.1.1.4',
                  'rets@10.1.1.5'
                  ]}},
               {{50, 100}, {rsm, quorum, [{r,1}, {w,3}], [
                  'rets@10.1.1.6',
                  'rets@10.1.1.7',
                  'rets@10.1.1.8'
                  ]}}
            ]}""",

   'rts' : """{rsm, quorum, [shuffle, {r,1}, {w,3}], [
               {psm, shard, [], {rets, route}, [
                  {{0,   50}, 'rets@10.1.1.3'},
                  {{50, 100}, 'rets@10.1.1.4'}
                  ]},
               {psm, shard, [], {rets, route}, [
                  {{0,   50}, 'rets@10.1.1.5'},
                  {{50, 100}, 'rets@10.1.1.6'}
                  ]},
               {psm, shard, [], {rets, route}, [
                  {{0,   50}, 'rets@10.1.1.7'},
                  {{50, 100}, 'rets@10.1.1.8'}
                  ]}
            ]}"""
   }

ops = ['rping', 'wping']

template = ""
with open("config.template", "r") as f:
   template = "".join(f.readlines())

for op in ops:
   for exp, spec in exps.iteritems():
      Fname = exp + "_" + op + ".config"
      if os.path.exists(Fname): os.remove(Fname)
      with open(Fname, "w") as f:
            config = template.replace(
               "HOSTS", ",".join(hosts)).replace(
               "SPEC", spec).replace(
               "OP", op)
            f.write(config)
