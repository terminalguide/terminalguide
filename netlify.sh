#! /bin/bash

set -e
set -x

echo $PATH

go get -v github.com/asciitosvg/asciitosvg/cmd/a2s
export PATH="$PATH:$GOPATH/bin"
which a2s

lektor plugins list
lektor plugins reinstall
lektor build --output-path _site-build
