[![wolframAlphaKnowledge Homepage](https://img.shields.io/badge/wolframAlphaKnowledge-develop-orange.svg)](https://github.com/davidvelascogarcia/wolframAlphaKnowledge/tree/develop/programs) [![Latest Release](https://img.shields.io/github/tag/davidvelascogarcia/wolframAlphaKnowledge.svg?label=Latest%20Release)](https://github.com/davidvelascogarcia/wolframAlphaKnowledge/tags) [![Build Status](https://travis-ci.org/davidvelascogarcia/wolframAlphaKnowledge.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/wolframAlphaKnowledge)

# Wolfram Alpha Knowledge: wolframAlphaKnowledge (Python API)

- [Introduction](#introduction)
- [Running Software](#running-software)
- [Requirements](#requirements)
- [Status](#status)
- [Related projects](#related-projects)


## Introduction

`wolframAlphaKnowledge` module use `wolpframalpha` API in `python`. This module receive questions or equations to resove with `YARP` port, send request to `Wolfram Alpha` server and publish results with `YARP` port.


## Running Software

`wolframAlphaKnowledge` requires text like input.
The process to running the program:

1. Execute [programs/wolframAlphaKnowledge.py](./programs), to start de program.
```python
python wolframAlphaKnowledge.py
```
2. Connect data source.
```bash
yarp connect /yourport/data:o /wolframAlphaKnowledge/data:i
```

NOTE:

- Data results are published on `/wolframAlphaKnowledge/data:o`

## Requirements

`wolframAlphaKnowledge` requires:

* [Install YARP 2.3.XX+](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-yarp.md)
* [Install pip](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-pip.md)
* Install wolframalpha:
```bash
pip install wolframalpha
```
* Install ConfigParser:
```bash
pip install configparser
```
**NOTE:**

Input text it´s the same as `Wolfram Alpha` web site but it´s recommended use `[]` characters instead of `()` characters.

**Examples:**
```bash
>> integrate x^2 sin^3 x dx
>> derivative of [x^4] sin x
>> spain capital
>> time
>> what is a dog
```

Tested on: `windows 10`, `ubuntu 14.04`, `ubuntu 16.04`, `ubuntu 18.04`, `lubuntu 18.04` and `raspbian`.

## Status

[![Build Status](https://travis-ci.org/davidvelascogarcia/wolframAlphaKnowledge.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/wolframAlphaKnowledge)

[![Issues](https://img.shields.io/github/issues/davidvelascogarcia/wolframAlphaKnowledge.svg?label=Issues)](https://github.com/davidvelascogarcia/wolframAlphaKnowledge/issues)

## Related projects

* [Wolfram Alpha: docs](https://pypi.org/project/wolframalpha/)

