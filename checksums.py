#!/usr/bin/env python
import zlib
import hashlib
import time
import sys


algorithms = [getattr(hashlib, algo) for algo in hashlib.algorithms_guaranteed]
algorithms.append(zlib.crc32)
algorithms.append(zlib.adler32)


def run(bytes_data, algorithm, iterations=1000):
	[...TO BE COMPLETED ...] 

def iteration(title, sample):
    print(title + ' (%d chars):' % len(sample))
    values = []
    for algorithm in algorithms:
        duration = run(sample, algorithm)
        values.append((duration, algorithm))
        print('%.06fs using %s' % (duration, algorithm.__name__))
    print()
    return values


if __name__ == '__main__':
    sample = ''.join([chr(i) for i in range(32, 123)]).encode()
    print('Python: %s' % sys.version)
    print('Sample: %s' % sample)
    print()

    iteration('Short', sample)
    iteration('Long', sample * 10000)
