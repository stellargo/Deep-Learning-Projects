=================
HOW TO RUN:
=================

From terminal, run: 

`cd SPEECH\ EMOTION\ PROBLEM/`
`./setup.sh <path/to/test/data>`

(Note: 
1. the python function is inside context subdirectory AND setup.sh will take care of running it on the docker instance.
2. The output will be found after the script finishes executing in the current directory

=================
FILE STRUCTURE:
=================

/context: it has the context for the docker build.

	/context/Dockerfile: it is the dockerfile required to build the docker image.
	/context/opensmile-2.3.0.tar.gz: source code of opensmile.
	/contex/output.py: it is the python script which generates the predictions. It is to be run on docker container.

/context/model: it stores the tensorflow model and info like mean and std of training data.

	/context/model/mean.npy: mean of training data
	/context/model/std.npy: std of training data
	/context/model/model.h5: tensorflow keras model

/setup.sh: this script creates a docker image, creates container of that image, and runs the function /contex/output.py on the container to generate a file 'output.txt' which is then sent back to the host from the container.