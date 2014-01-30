-module(test).
-compile(export_all).

-include("deps/libdist/include/libdist.hrl").

start_slaves(NumSlaves) ->
   Hosts = [ list_to_atom("10.1.1." ++ integer_to_list(2 + I)) || I <- lists:seq(1, NumSlaves) ],
   [ N || {ok, N} <- [slave:start(H, n,
            "-pa /usr/er/libdist/ebin /usr/er/rets/ebin") || H <- Hosts] ].



