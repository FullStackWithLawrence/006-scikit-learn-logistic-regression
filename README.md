[![Source code](https://img.shields.io/static/v1?logo=github&label=Git&style=flat-square&color=brightgreen&message=Source%20code)](https://github.com/FullStackWithLawrence/006-scikit-learn-logistic-regression)
[![Documentation](https://img.shields.io/static/v1?&label=Documentation&style=flat-square&color=000000&message=Documentation)](https://github.com/FullStackWithLawrence/006-scikit-learn-logistic-regression)
[![AGPL License](https://img.shields.io/github/license/overhangio/tutor.svg?style=flat-square)](https://www.gnu.org/licenses/agpl-3.0.en.html)
[![hack.d Lawrence McDaniel](https://img.shields.io/badge/hack.d-Lawrence%20McDaniel-orange.svg)](https://lawrencemcdaniel.com)

# Logistic Regression Prediction Model

A simple example of how to setup a Logistic Regression predictive model
using Python with Pandas, MatPlotLib, Seaborn and Scikit Learn.

This is the source code for FullStackWithLawrence Youtube Video -- "????".

## Jupyter Notebook Usage

I strongly recommend that you review the Jupyter notebook that is included in this repo. It includes a fully documented Jupyter notebook that provides **significantly** more explanation on ways to go about inspecting and analyzing your data set before attempting to create
a model.

Additionally, I've added a read-only copy of my output in html format which you can use as a guide, to better understand what the output of the Jupyter Notebook is supposed to look like.

## Command Line Usage

The included Python module scaffolds the implemntation of a model that would ostensibly be used in a production setting. Be aware that accordingly, this module excludes all code for analysis, QC and corrections to the included data set.

```console
foo@bar:~$ git clone https://github.com/FullStackWithLawrence/006-scikit-learn-logistic-regression.git
foo@bar:~$ cd 006-scikit-learn-logistic-regression
foo@bar:~$ pip install -r requirements.txt

# run the  code from the command line
foo@bar:~$ python logistic-regression.py
```

## Prerequisites, If You're New to Python

Note that I created this code sample using Python version 3.10. For best results I'd recommend that you create a [Python Virtual Environment](https://docs.python.org/3/library/venv.html) based on a matching Python 3.10.x engine. This helps to ensure that you run the exact same Python package versions as I've specified in requirements.txt.

If you starting from scratch then you might need to install Python on your computer, and you might also need to install a good installer. Crazy, and very meta, but yes, you might need to do that.

```console
# check if homebrew is installed on your computer
foo@bar:~$ brew --version
Homebrew 4.0.23
Homebrew/homebrew-core (git revision 50877e2f6f7; last commit 2023-02-27)
Homebrew/homebrew-cask (git revision cf17a964ec; last commit 2023-02-28)

# 1. check if you've previously installed a python interpretter using homebrew
foo@bar:~$ brew list

# 2. if you don't see python@3.10 in the output then install it now.
foo@bar:~$ brew install python@3.10

# 3. verify that python3.10 is in your computer's search path
foo@bar:~$ which python3.10
/opt/homebrew/bin/python3.10

# 4. create a Python Virtual Environment using python 3.10 as your interpretter
foo@bar:~$ mkdir fullstackwithlawrence && cd fullstackwithlawrence
foo@bar:~$ python3.10 -m venv venv
foo@bar:~$ source venv/bin/activate

# 5. verify that your Python virtual environment is activated, and
# that it is using Python version 3.10.x
foo@bar:~$ which python
/Users/foo/fullstackwithlawrence/venv/bin/python3.10

foo@bar:~$ python --version
Python 3.10.12

```
