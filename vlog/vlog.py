GLOBAL_LOG_LEVEL = 0

def vlog(log_level, *args, **kwargs):
  try:
    if GLOBAL_LOG_LEVEL >= log_level:
      print(*args, **kwargs)
  except NameError as e:
    # No global GLOBAL_LOG_LEVEL was set, so do
    # nothing at all
      pass


def main():
  global GLOBAL_LOG_LEVEL

  import os
  import sys
  from docopt import docopt

  doc = """Usage: {0} [options] <log_level> <stuff-to-echo>...

Options:
-h, --help                       This help
-v, --version                    Print version and exit
<log_level>                      This program will only echo if
                                 $GLOBAL_VLOG_LEVEL >= <log_level> 
""".format(sys.argv[0])

  args = docopt(doc, version="2.0.1")

  log_level = args['<log_level>']
  try:
    log_level = int(log_level)
  except ValueError as e:
    print(f"'{log_level}' can't be interpreted as an integer")
    exit(1)

  try:
    GLOBAL_LOG_LEVEL = os.environ["GLOBAL_VLOG_LEVEL"]
  except KeyError as e:
    # No $GLOBAL_VLOG_LEVEL was set, so do
    # nothing at all
    exit(0)

  try:
    GLOBAL_LOG_LEVEL = int(GLOBAL_LOG_LEVEL)
  except ValueError as e:
    print(f"$GLOBAL_VLOG_LEVEL ('{GLOBAL_LOG_LEVEL}') can't be interpreted as"
        " an integer")
    exit(1)

  # Finally, actually do stuff
  vlog(log_level, " ".join(args["<stuff-to-echo>"]))
