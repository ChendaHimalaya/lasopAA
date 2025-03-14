#!/usr/bin/env bash
#
# run_cpu_stress.sh
# A simple wrapper to run the python_cpu_stress.py script.

# Default values (you can override them via arguments)
WORKERS=2
DURATION=5000

# If you want to pass custom arguments, you could parse them here.
# Example usage:
#   ./run_cpu_stress.sh 4 60

if [[ -n "$1" ]]; then
  WORKERS=$1
fi

if [[ -n "$2" ]]; then
  DURATION=$2
fi

echo "Running cpu_load.py with $WORKERS workers for $DURATION seconds."

# Adjust path if necessary.
python cpu_load.py --workers "$WORKERS" --duration "$DURATION"
