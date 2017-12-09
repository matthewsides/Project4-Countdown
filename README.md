# | Project4-Countdown |
     Version 1.00
     November 14, 2017
     

# Revision List

| Version     | Author          | Date                 | Comments                       |
|-------------|-----------------|----------------------|--------------------------------|
| 1.00        |  Matthew Sides  | November 14, 2017    | Initial Version                |
|             |                 |                      |                                | 
|             |                 |                      |                                | 
|             |                 |                      |                                |
|             |                 |                      |                                |
|                                                                                       |                         







# Table Of Contents

1. Introduction ..........

1.1 Scope ..........

1.2 Type Conventions ..........

2. References ..........

3. Target System ..........

3.1 Windows 10 ..........

4. Development System ..........

4.1 Software ..........

5. Specification ..........

5.1 Concept

6.1 


## 1. Introduction

This document specifies a design for the conceptual features and mechanics (gameplay) of a game with the provisional title “CountDown”. It is based on and around elements discussed in various meetings and the continually running televised game show CountDown, the meetings held since 14th November 2017, between or involving Matthew Sides.

### 1.1 Scope

This documentation is intended to be read by programmers, artists and producers involved in the design implementation and testing of the video game rendition of CountDown.

### 1.2 Type Conventions

Things that have been discussed in a meeting are presented in this document with no asterisks.

Things that have not been offically agreed on but which are suggested by the author are presented with asterisks, like this (*),being marked as omitted until it has been agreed upon that it may be of use or implemented.



## 2. References

[1] Countdown



## 3. Target System

Count Down will be produced for the following platforms: Windows all versions running in the command line *and as a seperate application for the web (written in javascript) using either unity or phaser. This document is primarly concered with the command line version though the application may be adapted to a web based graphical application depending on the time scale. 

### 3.1 Windows 10



## 4. Development System

### 4.1 Software

CountDown will use either the cross-platform game engine, Unity   (which is primarily used to develop video games and simulations for computers, consoles and mobile devices.) or the open source HTML5 game framework coined as Phaser (designed to create games that will run on desktop and mobile web browsers.), each developed by Unity Technologies  and Photon Storm respectivly.


### High Level Description 
Research and implement a video game that mimics the popular show ‘Countdown’. Review, reflect, refactor and evolve the code you designed and developed in Project 003 as a reasonable starting point.



### Project Back Log

| User Story  | Description                  | Points | Due Date | Mo | Tu | We | Th | Fr |
|-------------|------------------------------|--------|----------|----|----|----|----|----|
| 1           | View in Browser              | 2      |22 Sep    |    |    |    |    |    |
| 2           | See the NPC and Player Model | 1      |22 Sep    |    |    |    |    |    |
| 3           | Initiate and End the Game    | 1      |22 Sep    |    |    |    |    |    |
| 4           | Be able to move              | 3      |22 Sep    |    |    |    |    |    |
| 5           | Amount of Lives (Feedback)   | 2      |22 Sep    |    |    |    |    |    |
| Total Points| 9                 |


### Test Plan

| Test reference no. | Description of test       | Type of test |Expected Outcome | 
|--------------------|---------------------------|--------------|-----------------|
| 1           | Output                           | Black box/Unit testing | Some form of output graphical or text form should show on screen.       |   
| 2           | Retrieving user input            | Unit testing | User is prompted to give input and the system should recieve that input with no informalitys or anomalies.|    
| 3           | Storage of values in an array    | Unit testing     |Pre-determined values should be accepted and stored within a defined array or list with no syntax,logical errors, etc. occurring    |    
| 4           | Retrieval of all the values held in an array            | Black box/Unit testing  | Pre-set values stored in an array should be printed, proving that the code segment is functional.  |    
| 5           | Retrieval of values from an array based around user input  | White box   | Pre-set values stored in an array should be outputted and appear on a screen based on user input and whether said value asked for is contained in the array  |    
| 6 | Importing an external file              | Black box/Unit testing | Whilst importing the libary the program should exhibit no signs of error and open an external file. |
| 7 | Reading an external txt file and storing contents in an array outputting| Black box| The program should  read a text file with no errors retrieving all the content within the file, storing it within a variable and showing said content or information on screen.
| 8 | Checking and retrieving specific parts of a text file to compare with input | Black Box/White Box/ Unit testing | Once input is given the 'opened' file should be read with the program thus checking to see whether the input that was given is found in the text file and if so give feedback pertaining to the status of 'yes' or 'valid whilst if it is not there the program should break a loop and state that the word cannot be found or located.
| 9 | Closing an external text file | Unit testing | The file should close, though all variables storing information taken from said file should retain the information, to be used for other functions or instances in the program.
| 10 | Seeing whether two words given by two users when valid can be compared (comparision system applied works) | Black box/Unit testing| The program should b compare two words and through using conditional statements and the basis that the word with the longer length wins or holds more value, output whether user one or user two wins.


