{rptree, rets, [ {min_no_slots, 1000} ],
   {psm, shard, [], {rets, route}, [
      {{0, 50}, {rsm, quorum, [shuffle, {r,1}, {w,3}], [
                   'n@10.1.1.3',
                   'n@10.1.1.4',
                   'n@10.1.1.5'
                      ]}},
      {{50, 100}, {rsm, quorum, [shuffle, {r,1}, {w,3}], [
                     'n@10.1.1.6',
                     'n@10.1.1.7',
                     'n@10.1.1.8'
                        ]}}
      ]}
}.
