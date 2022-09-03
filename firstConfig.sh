#!/bin/bash

for dir in .[^.]*; do
	sudo rm -r ~/$dir
	ln -s '$PWD/$(dir)' '$PWD/../$(dir)'
  done


