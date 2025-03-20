#!/usr/bin/env bash
#

pip install udocker
udocker --allow-root run jfusterm/stress --cpu 100
