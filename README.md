# cnn-kerberossdr

Forked from commit 75ff7d33c84cd156745c42d98b472c71ba49059b of randaller/cnn-rtlsdr

## Commands to run each Docker images:

### prepare:
sudo docker run -it --privileged -v /dev/bus/usb:/dev/bus/usb 
-v /path/to/training_data/wfm:/home/classifier/cnn-kerberossdr/training_data/[signal_type1] 
-v /path/to/training_data/gsm:/home/classifier/cnn-kerberossdr/training_data/[signal_type2] 
-v /path/to/training_data/other:/home/classifier/cnn-kerberossdr/training_data/other 
-v /path/to/testing_data/wfm:/home/classifier/cnn-kerberossdr/testing_data/[signal_type1] 
-v /path/to/testing_data/gsm:/home/classifier/cnn-kerberossdr/testing_data/[signal_type2] 
-v /path/to/testing_data/other:/home/classifier/cnn-kerberossdr/testing_data/other 
[ImageID]

### train:
sudo docker run -it --privileged -v /dev/bus/usb:/dev/bus/usb 
-v /path/to/training_data/wfm:/home/classifier/cnn-kerberossdr/training_data/[signal_type1] 
-v /path/to/training_data/gsm:/home/classifier/cnn-kerberossdr/training_data/[signal_type2] 
-v /path/to/training_data/other:/home/classifier/cnn-kerberossdr/training_data/other 
-v /path/to/testing_data/wfm:/home/classifier/cnn-kerberossdr/testing_data/[signal_type1] 
-v /path/to/testing_data/gsm:/home/classifier/cnn-kerberossdr/testing_data/[signal_type1] 
-v /path/to/testing_data/other:/home/classifier/cnn-kerberossdr/testing_data/other 
-v /path/to/model:/home/classifier/cnn-kerberossdr/model [ImageID]

### predict:
sudo docker run -it --privileged -v /dev/bus/usb:/dev/bus/usb 
-v /path/to/training_data/wfm:/home/classifier/cnn-kerberossdr/training_data/wfm 
-v /path/to/training_data/gsm:/home/classifier/cnn-kerberossdr/training_data/gsm 
-v /path/to/training_data/other:/home/classifier/cnn-kerberossdr/training_data/other 
-v /path/to/testing_data/wfm:/home/classifier/cnn-kerberossdr/testing_data/wfm 
-v /path/to/testing_data/gsm:/home/classifier/cnn-kerberossdr/testing_data/gsm 
-v /path/to/testing_data/other:/home/classifier/cnn-kerberossdr/testing_data/other 
-v /path/to/model:/home/classifier/cnn-kerberossdr/model [ImageID]