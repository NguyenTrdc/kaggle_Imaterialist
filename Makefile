install_libraries:
	pip install --upgrade pip
	pip install -r https://gist.githubusercontent.com/krokrob/53ab953bbec16c96b9938fcaebf2b199/raw/9035bbf12922840905ef1fbbabc459dc565b79a3/minimal_requirements.txt
	pip install jupyter notebook
	pip install tensorflow
	pip install pandas
	pip install matplotlib
	pip install opencv-python
	pip install selenium

intall_env:
	pyenv virutalenv IMaterialist
	pyenv local IMaterialist

full_install: # to be execute in project's folder
	make install_env
	make install_libraries
