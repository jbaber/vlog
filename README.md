Provide `vlog(log_level, *args, **kwargs)` function
which simply does `print(*args, **kwargs)` iff `log_level >= GLOBAL_LOG_LEVEL`.

Also provides a command line wrapper so you can call

    vlog log_level "Some words"

to get appropriate echoing on the command line if $log_level >= $GLOBAL_VLOG_LEVEL

After

    pip3 install .

`vlog --help` will show the flags to the executable script `vlog`.
