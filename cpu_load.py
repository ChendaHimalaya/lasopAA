#!/usr/bin/env python3
"""
python_cpu_stress.py
Continuously performs a CPU-heavy computation to keep utilization high.

Usage:
  python3 python_cpu_stress.py --workers 4 --duration 60

    --workers  <int>   Number of parallel processes (default: 1)
    --duration <int>   How many seconds to run. 0 => run indefinitely (default: 0)
"""
import time
import math
import argparse
import multiprocessing


def cpu_heavy_loop(duration=0):
    """
    Continuously perform a CPU-intensive calculation for 'duration' seconds.
    If duration=0, run indefinitely until interrupted.
    """
    end_time = None
    if duration > 0:
        end_time = time.time() + duration

    while (end_time is None) or (time.time() < end_time):
        # A loop with arbitrary math to keep the CPU busy
        s = 0
        for i in range(5_000_000):
            # Do some random (but CPU-heavy) arithmetic
            s += ((i % 3) ** 2) + (i % 7) - (i % 11)
        # Optionally do something with 's' to avoid Python optimizing it away
        # (Typically not necessary in Python, but it's good practice.)
        _ = math.sqrt(abs(s))


def worker_process(duration):
    """
    Each worker process runs the cpu_heavy_loop.
    """
    print(f"[Worker {multiprocessing.current_process().name}] Starting CPU loop. Duration={duration}s")
    cpu_heavy_loop(duration)
    print(f"[Worker {multiprocessing.current_process().name}] Finished")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel processes")
    parser.add_argument("--duration", type=int, default=0, help="Time in seconds to run (0 => indefinite)")
    args = parser.parse_args()

    # Spawn multiple processes to use multiple CPU cores
    processes = []
    for w in range(args.workers):
        p = multiprocessing.Process(target=worker_process, args=(args.duration,), name=f"W{w+1}")
        p.start()
        processes.append(p)

    # Wait for all processes to finish
    for p in processes:
        p.join()


if __name__ == "__main__":
    main()
