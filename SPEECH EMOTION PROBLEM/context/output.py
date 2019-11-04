# Imports
import os
import tqdm
import shutil
import numpy as np

from tensorflow.keras.models import load_model

EMOTIONS = {
	0: "disgust", 
	1: "happy", 
	2: "sad", 
	3: "fear", 
	4: "neutral",
}

test_path = "./test"
test_path_opensmile = test_path+"_opensmile"

if os.path.isdir(test_path_opensmile):
	shutil.rmtree(test_path_opensmile)


# Generate OpenSmile features for the data.
os.makedirs(test_path_opensmile)

for root, subdirs, files in os.walk(test_path):
	for wav_file in files:
		if wav_file.startswith(".") or not wav_file.endswith(".wav"):
			continue

		osmile_cmd = "./opensmile-2.3.0/SMILExtract -C ./opensmile-2.3.0/config/emo_large.conf"
		osmile_cmd += " -I "+os.path.join(root, wav_file)
		osmile_cmd += " -O "+test_path_opensmile+"/"+wav_file[:-3] +'arff'

		os.system(osmile_cmd) # Exectute opensmile command


# Build test set from the generated opensmile features.
X_test = []
X_test_names = []


for root, subdirs, files in os.walk(test_path_opensmile):
	for file_name in files:
		if file_name.startswith(".") or not file_name.endswith(".arff"):
			continue

		f = open(os.path.join(root, file_name))
		lines = f.readlines()
		params = lines[6560].split(',')[1:-1]
		params = [float(i) for i in params]
		params = np.array(params)
		f.close()
		X_test.append(params)

		X_test_names.append(file_name[:-5])
    
X_test = np.array(X_test)

# Zero center and normalize by subracting and dividing by the mean and std respectively of the training data
train_mean = np.load("mean.npy")
train_std = np.load("std.npy")

X_test -= train_mean
X_test = np.divide(X_test, train_std, out=np.zeros_like(X_test), where=train_std!=0)

# Load tf keras model
model = load_model("model.h5")

# Make predictinos
y_test = np.argmax(model.predict(X_test), axis=1)

# Save predictions
f = open("output.txt", "w")
f.write("File name, prediction\n\n")

for i in range(len(X_test)):
	f.write(X_test_names[i]+","+EMOTIONS[y_test[i]]+"\n")

f.close()





