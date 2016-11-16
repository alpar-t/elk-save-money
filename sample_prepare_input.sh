#!/bin/bash
if [ -z "$1" ] ; then 
    echo "Usage $0 <<path to xls>>"
fi

tmpfile=$(mktemp  /tmp/$0.XXXXXX.csv)
trap "rm -v -f $tmpfile >&2" 0 2 3 15

check_tool() {
    if which ssconvert 2>&1 > /dev/null ; then
        return 0
    else
        echo "Can not find '$1'. $2"
        return 1
    fi
}

SSCONVERT="ssconvert"

if ! check_tool $SSCONVERT "Please install gnumeric" ; then
   exit 1;
fi;

ssconvert  $1 $tmpfile

grep '^[0-9]\{2\}\/[0-9]\{2\}\/[0-9]\{4\}' $tmpfile > sample.csv 
cp -v $tmpfile orig.csv 
