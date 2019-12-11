# devsecops-coding-test

## Assignment

In this exercise you can use any language of your choice, except shell script. The goal is to implement a function that combines 2 sorted arrays into a single sorted array. The function should be invoked from command line with the 2 sorted arrays as the arguments.
Here are sample inputs and outputs:

```
$ function_name [1, 2, 7, 9] [3, 6, 8]
> [1, 2, 3, 6, 7, 8, 9]

$ function_name [6, 8, 9] [1, 4, 6]
> [1, 4, 6, 6, 8, 9]

$ function_name [] [1, 2, 3]
> [1, 2, 3]
```

The next step is to containerize the function. The end result should look like this:

```
$ docker run <image>:<tag> [1, 2, 7, 9] [3, 6, 8]
> [1, 2, 3, 6, 7, 8, 9]
```

Create a public github repo for this exercise and include all files required to build and run the containerized function. Use a README for build and run steps if necessary. Please submit the github repo within a week of receiving the exercise.

## Development
Requirements:
- docker
- python 3.8.0

Testing:
```
pip install flake8 pytest
flake8 . --count --show-source --statistics --max-line-length=120
pytest test.py
```
Building Docker Image:
```
docker build . --file Dockerfile --tag devsecops-coding-test:latest
```

## Usage
From Command Line:
```
./main.py "[1,2,3]" "[4,5,6]"
```

With Docker:
```
docker run devsecops-coding-test:latest "[1,2,3]" "[4,5,6]"
```

## Build Status
![](https://github.com/mixmatch/devsecops-coding-test/workflows/Test%20Code%20and%20Build%20Docker%20Container/badge.svg)