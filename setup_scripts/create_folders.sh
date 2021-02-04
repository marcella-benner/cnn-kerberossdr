#!/bin/bash
#creates necessary folders to collect training data
#edit to create the signal classes you are interested in
cd testing_data
mkdir sigfox lora zwave other #designate the classes needed

cd ..

cd training_data
mkdir sigfox lora zwave other
