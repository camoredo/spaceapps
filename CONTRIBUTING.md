# Contributing to Scripts in Bottles

First off, thanks for taking the time to contribute!

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owner of this repository before making a change.

## Table of Contents
  - [Setting Up the Project Locally](#setting-up-the-project-locally)
  - [Submitting a Pull Request](#submitting-a-pull-request)

## Setting Up the Project Locally

To install the project you need to have `python3`, `pip3`, and `virtualenv`.

1. [Fork](https://help.github.com/articles/fork-a-repo/) the project and then clone your fork:

```sh
$ git clone https://github.com/<your-username>/spaceapps.git
$ cd spaceapps
```

2. Your environment needs to be running `python3` version >= 3.9.0, `pip3` version >= 20.2.4, and `virtualenv` version >= 20.2.1.

3. From the root of the project, run `virtualenv -p python3 venv` to create a virtual environment IF you have not created a virtual environment before.

4. From the root of the project, run `source venv/bin/activate` to active the virtual environment.

3. From the root of the project, run `pip install -r requirements.txt` to install all dependencies.

4. From the root of the project, run `python main.py` to run the script. 

> Tip: Keep your `master` branch pointing at the original repository and make
> pull requests from branches on your fork. To do this, run:
>
> ```sh
> $ git remote add upstream https://github.com/camoredo/spaceapps.git
> $ git fetch upstream
> $ git branch --set-upstream-to=upstream/master master
> ```
>
> This will add the original repository as a "remote" called "upstream", then
> fetch the git information from that remote, and then set your local `master`
> branch to use the upstream master branch whenever you run `git pull`. Then you
> can make all of your pull request branches based on this `master` branch.
> Whenever you want to update your version of `master`, do a regular `git pull`.

## Submitting a Pull Request

Please go through the existing issues and pull requests to check if somebody else is already working on it.