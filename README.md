# cnn-kerberossdr

Forked from commit 75ff7d33c84cd156745c42d98b472c71ba49059b of randaller/cnn-rtlsdr

## Send files to the pi
scp -r /Users/marcellabenner/Desktop/signalCode/cnn-kerberossdr/requirements.txt ubuntu@192.168.1.254:/home/ubuntu/test

## Commands to run each Docker image:

### prepare:
sudo docker run -it --privileged -v /dev/bus/usb:/dev/bus/usb 
-v /path/to/training_data/[signal_type1]:/home/classifier/cnn-kerberossdr/training_data/[signal_type1] 
-v /path/to/training_data/[signal_type2]:/home/classifier/cnn-kerberossdr/training_data/[signal_type2] 
-v /path/to/training_data/other:/home/classifier/cnn-kerberossdr/training_data/other 
-v /path/to/testing_data/[signal_type1]:/home/classifier/cnn-kerberossdr/testing_data/[signal_type1] 
-v /path/to/testing_data/[signal_type2]:/home/classifier/cnn-kerberossdr/testing_data/[signal_type2] 
-v /path/to/testing_data/other:/home/classifier/cnn-kerberossdr/testing_data/other [ImageID]

sudo docker run -it --privileged -v /dev/bus/usb:/dev/bus/usb 
-v /home/pi/cnn-kerberossdr/training_data/lora:/home/classifier/cnn-kerberossdr/training_data/lora 
-v /home/pi/cnn-kerberossdr/training_data/sigfox:/home/classifier/cnn-kerberossdr/training_data/sigfox 
-v /home/pi/cnn-kerberossdr/training_data/zwave:/home/classifier/cnn-kerberossdr/training_data/zwave 
-v /home/pi/cnn-kerberossdr/training_data/other:/home/classifier/cnn-kerberossdr/training_data/other 
-v /home/pi/cnn-kerberossdr/testing_data/lora:/home/classifier/cnn-kerberossdr/testing_data/lora 
-v /home/pi/cnn-kerberossdr/testing_data/sigfox:/home/classifier/cnn-kerberossdr/testing_data/sigfox 
-v /home/pi/cnn-kerberossdr/testing_data/zwave:/home/classifier/cnn-kerberossdr/testing_data/zwave 
-v /home/pi/cnn-kerberossdr/testing_data/other:/home/classifier/cnn-kerberossdr/testing_data/other [ImageID]

### train:
sudo docker run -it --privileged -v /dev/bus/usb:/dev/bus/usb 
-v /path/to/training_data/[signal_type1]:/home/classifier/cnn-kerberossdr/training_data/[signal_type1] 
-v /path/to/training_data/[signal_type2]:/home/classifier/cnn-kerberossdr/training_data/[signal_type2] 
-v /path/to/training_data/other:/home/classifier/cnn-kerberossdr/training_data/other 
-v /path/to/testing_data/[signal_type1]:/home/classifier/cnn-kerberossdr/testing_data/[signal_type1] 
-v /path/to/testing_data/[signal_type2]:/home/classifier/cnn-kerberossdr/testing_data/[signal_type2] 
-v /path/to/testing_data/other:/home/classifier/cnn-kerberossdr/testing_data/other 
-v /path/to/model:/home/classifier/cnn-kerberossdr/model [ImageID]

### predict:
sudo docker run -it --privileged -v /dev/bus/usb:/dev/bus/usb 
-v /path/to/training_data/[signal_type1]:/home/classifier/cnn-kerberossdr/training_data/[signal_type1] 
-v /path/to/training_data/[signal_type2]:/home/classifier/cnn-kerberossdr/training_data/[signal_type2] 
-v /path/to/training_data/other:/home/classifier/cnn-kerberossdr/training_data/other 
-v /path/to/testing_data/[signal_type1]:/home/classifier/cnn-kerberossdr/testing_data/[signal_type1]  
-v /path/to/testing_data/[signal_type2]:/home/classifier/cnn-kerberossdr/testing_data/[signal_type2]  
-v /path/to/testing_data/other:/home/classifier/cnn-kerberossdr/testing_data/other 
-v /path/to/model:/home/classifier/cnn-kerberossdr/model [ImageID]


## Pushing & Pulling from GitHub and Docker

### GitHub
#### Pulling
git pull

#### Pushing
git add [*, file name] 

git commit -m '[comment]'

git push

#### Clearing Cache
Useful if git is not recognizing file changes
git rm --cached path/to/repo
git reset path/to/repo

### Docker
#### Pulling

#### Pushing
docker login

docker images

docker tag [imageID] [user]/[repo_name]:[tag]

docker push [user]/[repo_name]

#### Clearing Cache
docker build --no-cache .

### Pachyderm

#### Add Data
pachctl put file -r signals@master -f testing_data

#### Create Repo
pachctl create repo signals

#### List Repos
pachctl list repo
