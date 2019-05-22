#!/bin/bash
for file in valid/*
do
  echo $file
  ../229/life/showgen "${file}"
  echo "-------------------------------------------------------"
done
