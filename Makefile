SHELL = /bin/bash
.PHONY: transform_data 

all: transform_data

transform_data:
	python3 src/transform_cb.py
