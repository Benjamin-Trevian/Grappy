#/bin/bash

rm -r build & rm -r dist
python3 setup.py bdist_wheel sdist
twine upload dist/*
