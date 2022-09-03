#!/bin/bash

for dir in .[^.]*; do
	sudo rm -r $PWD/../$dir
	ln -s "$PWD/$dir" "$PWD/../$dir"
  done


