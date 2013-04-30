#!/bin/bash
for file in malformed/*
do
  echo $file
  ../229/life/showgen "${file}"
  echo "-------------------------------------------------------"
done
