# Timetable-Generator

A graph colouring application built with python to help produce timetables with no scheduling conflicts.

***

## Table of contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Getting started](#getting-started)
* [Data](#data)
* [Improvements](#improvements)

## Introduction

Timetable-Generator is a simple tool to help create timetables with non-conflicting groups, or nodes. 
It works by transforming the input data into nodes, then creates edges between all the nodes representing
conflicts. Finally, graph colouring is performed on the nodes with its edges.

## Technologies
* Python 3


## Getting started 
Run:

   * `install python3`

   * `pip3 install pyvis`


## Data
***
### How data is loaded & modified
Data is loaded from the `mockData.csv` file.

Data can be modified by changing it in the `mockData.csv` file or creating an entirely new file. 
### Structure for the data
The structure for the data can be changed, but for the provided code the structure is as follows:
`id, profName, degree, subject, requirement`

### Output
Once the program is done running it will generate a `generatedTimetable.csv`, in it will be groups 
of subjects that conflict and as such will need to scheduled accordingly.

## Improvements
* The colours used come from a set list of colours, these can be expanded or rather made dynamic.
* The generated canvas that the graph is presented on can be made larger.
* An algorithm can be implemented to find the minimum colouring required.
