-module(d).
-compile(export_all).

-define(MATCH_SPEC, [{'_', [], [{return_trace}]}]).

start() ->
   dbg:tracer(),
   dbg:p(all, c).

trace(ModuleName) ->
   start(),
   dbg:tpl(ModuleName, ?MATCH_SPEC).

trace(ModuleName, Function) ->
   start(),
   dbg:tpl(ModuleName, Function, ?MATCH_SPEC).

stop() ->
   dbg:stop_clear().
