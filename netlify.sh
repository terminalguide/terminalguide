#! /bin/bash

set -e

lektor plugins list
lektor plugins reinstall
lektor build --output-path _site-build
