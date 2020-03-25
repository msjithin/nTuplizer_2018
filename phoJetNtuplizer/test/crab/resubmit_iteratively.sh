#!/bin/sh

#sleep 50 #inseconds

for (( i=0; i<5; i++)); do
  for jobDir in `ls crab_data2018_13Mar2020`; do
  crab resubmit -d crab_data2018_13Mar2020/${jobDir}
  done

  for jobDir in `ls crab_MC2018_Autumn18_monoHiggs_12Mar`; do
  crab resubmit -d crab_MC2018_Autumn18_monoHiggs_12Mar/${jobDir}
  done

echo "Sleep for 1hr"
sleep 3600
done
exit 0;
