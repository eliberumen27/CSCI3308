#!/bin/bash

#Elijah Berumen
[ $# -eq 0 ] && { echo "Usage: $0 filename"; exit 1;}
div=3
lines=$(wc -l < $1)
times=$(cut -f 4-6 -d ' ' $1 | sed 's/ /+/g' | bc)
sid=$(sort -k3,3 -k2,2 -k1,1 $1 | cut -f 1 -d ' ')
first=$(sort -k3,3 -k2,2 -k1,1 $1 | cut -f 2 -d ' ')
last=$(sort -k3,3 -k2,2 -k1,1 $1 | cut -f 3 -d ' ')

pTimes=(${times// / })
pSid=(${sid// / })
pFirst=(${first// / })
pLast=(${last// / })

counter=0
while [ $counter -le $lines ]
do
echo $((${pTimes[$counter]} / $div )) [${pSid[$counter]}] ${pLast[$counter]}, ${pFirst[$counter]}
((counter++))
done
