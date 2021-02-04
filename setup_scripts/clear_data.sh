#!/bin/bash
#removes signal folders to clear training data
#edit to remove the signal classes you have

cd training_data
rm -f signal/* lora/* zwave/* other/*

cd ..

cd testing_data
rm -rf signal/* lora/* zwave/* other/*