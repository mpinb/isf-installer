#!/bin/bash

# This script records the time it takes to offline install in-silico-framework (Python3).
# It is meant to be used as a cron task to gather execution statistics of soma login node.
# Author:  Omar Valerio (omar.valerio@gmail.com)
# Date:    Apr 29th, 2022

usage() {
    cat << EOF
Usage: ./time-install-isf3.sh -f <host-timings.txt>

    -h                          Display help
    -d                          Download in-silico-framework dependencies.

    -f <host-timings.txt>       The file where the results of timing measurements are appended.
EOF
}

# Reading command line options supported by the time-installer script
while getopts "f:dh" opt; do
    case "${opt}" in
        f)
            output_timings=${OPTARG}
            ;;
        d)
            download_packages="true"
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

# Remove any existing isf py3 installation
if [[ -d $HOME/conda-py3 ]]; then
    rm -rf $HOME/conda-py3
fi

# The time the installer takes to execute is found using the SECONDS builtin variable
# REF: https://www.xmodulo.com/measure-elapsed-time-bash.html
start_date=$(date +'%d/%m/%Y %H:%M:%S %Z')
start_time=$SECONDS

# If online install desired then use 
if [ ${download_packages} == "true" ]; then
    ./isf-install.sh -d -t py3
else
    ./isf-install.sh -t py3
fi

stop_time=$SECONDS
elapsed_time=$(( stop_time - start_time ))

# Append file with start time and elapsed execution time values
echo "${start_date}, ${elapsed_time}" >> ${output_timings}