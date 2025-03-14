#!/usr/bin/env bash
#
# run_cpu_stress.sh
# A simple wrapper to run the python_cpu_stress.py script.

# Default values (you can override them via arguments)
WORKERS=2
DURATION=50000

echo "Running cpu_load.py with $WORKERS workers for $DURATION seconds."

# Adjust path if necessary.
python cpu_load.py --workers "$WORKERS" --duration "$DURATION"
