#!/bin/bash

# This script records the time it takes to install in-silico-framework.
# It is meant to be used as a cron task to gather execution statistics of soma login node.
# Author:  Omar Valerio (omar.valerio@gmail.com)
# Date:    Apr 24th, 2022

usage() {
    cat << EOF
Usage: ./time-installer.sh -f <host-timings.txt>

    -h                          Display help
    -f <host-timings.txt>       The file where the results of timing measurements are appended.
EOF
}

# Reading command line options supported by the time-installer script
while getopts "f:h" opt; do
    case "${opt}" in
        f)
            output_timings=${OPTARG}
            ;;
        h)
            usage
            exit 0
            ;;
    esac
done
shift $((OPTIND-1))

if [ -z "${output_timings}" ] || ! [[ -f ${output_timings} ]] ; then
    echo "ERROR: The file to record the timings is missing or cannot be open."
    usage
    exit 1
fi

# Remove any existing isf installation
if [[ -d $HOME/conda-py2 ]]; then
    rm -rf $HOME/conda-py2
fi

# Remove any previously downloaded files (offline-installer)
# NOTE: the in-silico-framework and pandas-msgpack require authentication therefore not removed.
if [[ -f Anaconda2-4.2.0-Linux-x86_64.sh ]]; then
    rm Anaconda2-4.2.0-Linux-x86_64.sh
fi

if [[ -d conda_packages ]]; then
    rm -rf conda_packages
fi

if [[ -d pip_packages ]]; then
    rm -rf pip_packages
fi

# The time the installer takes to execute is found using the SECONDS builtin variable
# REF: https://www.xmodulo.com/measure-elapsed-time-bash.html
start_date=$(date +'%d/%m/%Y %H:%M:%S %Z')
start_time=$SECONDS

./isf-install.sh -d -t py2
#sleep 5s

stop_time=$SECONDS
elapsed_time=$(( stop_time - start_time ))

# Append file with start time and elapsed execution time values
echo "${start_date}, ${elapsed_time}" >> ${output_timings}