#Elijah Berumen

#!/bin/bash

[ $# -eq 0 ] && { echo "Usage: $0 filename"; exit 1;}

grep "[0-9]$" $1 | wc -l
grep ^"[^aeiouAEIOU]" $1 | wc -l
grep -E "^[a-zA-Z]{9}$" $1 | wc -l
grep -E "^[0-9]{3}-[0-9]{3}-[0-9]{4}$" $1 | wc -l
grep -E "303-[0-9]{3}-[0-9]{4}$" $1 | wc -l
grep -E "^[aeiouAEIOU].*[0-9]$" $1 | wc -l
grep "UCDenver.edu$" $1 | wc -l
grep -E "^[n-zN-Z][a-zA-Z]*[.][a-zA-Z]*@.*[.][a-zA-Z]{3}" $1 | wc -l
