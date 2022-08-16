#Some notes to considering when installing everything

 - Anaconda3 and Apple M1 are not friends, particularly regarding Tensorflow
 - Miniforge3 is advised to install tensorflow. This may block me from using Spyder.
 - To sort it out, I am doing a clean installation using conda from Miniforge3. It is very important to get rid of my previous Anaconda. This website helped me a lot: https://stackoverflow.com/questions/71523255/conda-using-usr-local-bin-python-instead-of-conda-environment-python
 - Critical to inspect the hidden files in /User/ and delete the references to anaconda3 paths (in my case I just deleted them as they were empty of further info).
 - You know you have done it right when "conda activate" stops working or, when prompting afterwards "which python" there is no dir to Anaconda3.
 - Then, I successfully installed Miniforge3 for the first time following these instructions (https://github.com/apple/tensorflow_macos/issues/153).

This post is also useful but failed to install tensorflow with it https://towardsdatascience.com/setting-up-apples-new-m1-macbooks-for-machine-learning-f9c6d67d2c0f


I got ScikitLearn with this command, directly in the environment with tf:

conda install --channel=conda-forge scikit-learn

