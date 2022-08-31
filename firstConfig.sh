#!/bin/bash

for dir in .[^.]*; do
	 ln -sf $dir ~/dotfiles/$dir 
  done


