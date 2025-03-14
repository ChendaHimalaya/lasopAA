#!/usr/bin/env bash
#
# cpu_stress.sh
# Continuously runs a CPU-heavy calculation for X seconds, then exits.

if [ -z "$1" ]; then
  echo "Usage: $0 <DURATION_IN_SECONDS>"
  exit 1
fi

DURATION=$1
PRECISION=300000
END_TIME=$(( $(date +%s) + DURATION ))

echo "Running CPU stress for $DURATION seconds..."

while [ $(date +%s) -lt $END_TIME ]; do
  echo "scale=$PRECISION; sqrt(2)" | bc >/dev/null
done

echo "Done"
