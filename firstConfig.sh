#!/bin/bash

git clone https://github.com/VundleVim/Vundle.vim.git "$PWD/../.vim/bundle/Vundle.vim"

for dir in .[^.]*; do
	sudo rm -r $PWD/../$dir
	ln -s "$PWD/$dir" "$PWD/../$dir"
  done


