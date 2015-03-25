import sys

chars = '|/-\\'

for i in xrange(1, 1000):
  for c in chars:
    sys.stdout.write(c)
    sys.stdout.write('\b')
    sys.stdout.flush()
