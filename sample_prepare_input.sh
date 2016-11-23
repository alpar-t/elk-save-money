#!/bin/bash 

set -e

if [ -z "$1" ] ; then 
    echo "Usage $0 <<path to xls>>"
    exit 1
fi

tmpfile=$(mktemp  /tmp/$0.XXXXXX.csv)
trap "rm -f $tmpfile >&2" 0 2 3 15

check_tool() {
    if which $1 > /dev/null 2>&1; then
        return 0
    else
        echo "Can not find '$1'. $2"
        return 1
    fi
}

SSCONVERT="ssconvert"
NCAT="ncat"

if ! check_tool $SSCONVERT "Please install gnumeric" ; then
   exit 1;
fi;
if ! check_tool $NCAT "Please install gnumeric" ; then
   exit 1;
fi;

# Convert from input XLS
ssconvert "$1" $tmpfile

# Parse header information
OWNER=`grep '^"Nume client:' $tmpfile | cut -d, -f2 | sed -e 's/"//g'`
ACCOUNT_NO=`grep '^"Cod IBAN:' $tmpfile | cut -d, -f2 | sed -e 's/"//g'`
CURRENCY=`grep '^"Cod IBAN:' $tmpfile | cut -d, -f6 | sed -e 's/"//g'`


# 
# 1. Filter out anything that does not start with a date ( the header )
# 2. Append the information parsed from the header to each entry
# 3. Push the result to logstash
grep '^[0-9]\{2\}\/[0-9]\{2\}\/[0-9]\{4\}' $tmpfile \
    | sed "s/\$/,$OWNER,$ACCOUNT_NO,$CURRENCY/" \
    | $NCAT localhost 6006

