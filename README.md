[![Source code](https://img.shields.io/static/v1?logo=github&label=Git&style=flat-square&color=brightgreen&message=Source%20code)](https://github.com/FullStackWithLawrence/006-scikit-learn-logistic-regression)
[![Documentation](https://img.shields.io/static/v1?&label=Documentation&style=flat-square&color=000000&message=Documentation)](https://github.com/FullStackWithLawrence/006-scikit-learn-logistic-regression)
[![AGPL License](https://img.shields.io/github/license/overhangio/tutor.svg?style=flat-square)](https://www.gnu.org/licenses/agpl-3.0.en.html)
[![hack.d Lawrence McDaniel](https://img.shields.io/badge/hack.d-Lawrence%20McDaniel-orange.svg)](https://lawrencemcdaniel.com)

# Logistic Regression Prediction Model

A simple example of how to setup a Logistic Regression predictive model
using Python with Pandas, MatPlotLib, Seaborn and Scikit Learn.

This is the source code for FullStackWithLawrence Youtube Video -- "????".

## Usage

I'm providing this code sample in both native Python as well as Jupyter Notebook formats. They each service their own purpose. The Jupyter Notebook is more explanatory whereas the native Python is more illustrative of a real-world production implementation.

### Jupyter Notebook

I strongly recommend that you review the Jupyter notebook that is included in this repo. It provides **significantly** more explanation on ways to go about inspecting and analyzing your data set before attempting to create a model. Additionally, I've added a read-only copy of my output in html format which you can use as a guide, to better understand what the output of the Jupyter Notebook is supposed to look like.

Note that freely downloadable [VS Code](https://code.visualstudio.com/) natively renders Jupyter Notebooks from inside the code editor, which is a really convenient feature.

### Command Line

The included Python module scaffolds the implemntation of a model that would ostensibly be used in a production setting. Be aware that accordingly, this module excludes all code for analysis, QC and corrections to the included data set.

```console
foo@bar:~$ git clone https://github.com/FullStackWithLawrence/006-scikit-learn-logistic-regression.git
foo@bar:~$ cd 006-scikit-learn-logistic-regression
foo@bar:~$ pip install -r requirements.txt

# run the  code from the command line
foo@bar:~$ python logistic-regression.py
```

### If You're New to Jupyter Notebooks

There's an easy way to get Jupyter Notebooks working immediately, by downloading an application named [Anaconda Navigator](https://www.anaconda.com/) that is freely available for both Windows and Mac.

![Anaconda](https://github.com/FullStackWithLawrence/006-scikit-learn-logistic-regression/blob/main/doc/anaconda.png)

### If You're New to Python

Note that I created this code sample using Python version 3.10. For best results I'd recommend that you create a [Python Virtual Environment](https://docs.python.org/3/library/venv.html) based on a matching Python 3.10.x engine. This helps to ensure that you run the exact same Python package versions as I've specified in requirements.txt.

If you starting from scratch then you might need to install Python on your computer, and you might also need to install a good installer. Crazy, and very meta, but yes, you might need to do that.

```console
# 1. check if homebrew is installed on your computer
# -------------------------------------
foo@bar:~$ brew --version
Homebrew 4.0.23
Homebrew/homebrew-core (git revision 50877e2f6f7; last commit 2023-02-27)
Homebrew/homebrew-cask (git revision cf17a964ec; last commit 2023-02-28)

# 2. check if you've previously installed a python interpretter using homebrew
# -------------------------------------
foo@bar:~$ brew list

# 3. if you don't see python@3.10 in the output then install it now.
# -------------------------------------
foo@bar:~$ brew install python@3.10

# 4. verify that python3.10 is in your computer's search path
# -------------------------------------
foo@bar:~$ which python3.10
/opt/homebrew/bin/python3.10

# 5. create a Python Virtual Environment using python 3.10 as your interpretter
# -------------------------------------
foo@bar:~$ mkdir fullstackwithlawrence && cd fullstackwithlawrence
foo@bar:~$ python3.10 -m venv venv
foo@bar:~$ source venv/bin/activate

# 6. verify that your Python virtual environment is activated, and
# that it is using Python version 3.10.x
# -------------------------------------
foo@bar:~$ which python
/Users/foo/fullstackwithlawrence/venv/bin/python3.10

foo@bar:~$ python --version
Python 3.10.12

```

## Contributing

Give back to the open source community! If you have good ideas for how to improve this code then by all means, please seize the day and share your improvements by creating a pull request: fork this repo, make your changes, and then open a pull request; most of which can be done directly from Github.

### Local development

This being the low budget one-man-band operation that it is, I'm reliant on the automated coding style enforcement and syntax checking capabilities of [pre-commit](https://pre-commit.com/), [black](https://pypi.org/project/black/) and [flake8](https://flake8.pycqa.org/), so you'll want to install these amazing tools **prior** to attempting a PR as I've also installed automated [Github Actions](https://github.com/features/actions) [CI](https://en.wikipedia.org/wiki/Continuous_integration) tools that will run these tests on all commits.

```console
foo@bar:~$ pip install -r requirements-dev.txt
foo@bar:~$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
foo@bar:~$ 
foo@bar:~$ pre-commit
```

![pre-commit output](https://github.com/FullStackWithLawrence/006-scikit-learn-logistic-regression/blob/main/doc/pre-commit.png)
