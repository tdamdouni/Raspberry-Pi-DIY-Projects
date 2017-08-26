#  Weather Station Basic I/O - Lesson Plan 5

In this lesson, students will complete their initial work on the weather station using the rain gauge and the anemometer. They will work to combine elements from the two programs created for these sensors into a single program to manage them both.

## Learning objectives

- To demonstrate an understanding of how their programs work, by combining them
- To use code annotation to explain the function of sections of code
- To debug errors to create a working solution

## Learning outcomes

### All students are able to

- Explain the function of some key lines of code
- With support, combine their programs into one solution

### Most students are able to

- Clearly explain the function of the majority of the code
- Combine their programs into one solution, including some commenting

### Some students are able to

- Clearly explain what each line of code does and how they work together
- Independently create a program which combines the two functions from previous lessons, complete with commenting

## Lesson Summary

- Code review of the previous two solutions
- Group discussion around challenges involved in merging the programs
- Students create a single solution and annotate it
- Students review each other's code and annotations

## Starter

Share the code for the [anemometer](../lesson-4/code/wind_final.py) and the [rain gauge](../lesson-4/code/wind_interrupt.py ). Students are invited to explain what the two programs are doing and how they are working. This could be done in the following ways:

* Class discussion with notes being taken.
* Projecting code onto a whiteboard, where students use sticky notes to add annotation.
* Printed copies which students individually annotate.
* Google doc or [Classroom](classroom.google.com).

## Main development

1. Discuss with students the challenges they may face when combining their code into one program. Such as:
    - Some lines of code occur in both programs and would only need to occur once.
    - Some variables (count, pin etc.) in the programs are the same. Would this cause a problem?
    - Each program has a set of defined functions, which need to be defined at the beginning of the program before they are used.
    - Both programs contain a loop of some kind to display the current readings, and these will need to be combined.

2. Show the students how to add comments to their code using the `#` symbol ie:

    ```python
    # This is a comment, it is ignored by the computer and used to annotate the code.
    ```

    Ask students how comments might be a useful tool for programmers.
    - They help explain the intended function of the program to others that might read the code, looking for ideas or to improve it.
    - Comments help the programmer keep track of what their code is doing, and make it easier to return to a piece of code and still make sense of it.

3. Students should be given time to build their own solution which logs and displays both rainfall and windspeed. Their solution should be well-annotated and tested to ensure functionality.
    - They may want to set up their Pi with a weather station / buttons for testing.
    - They could either start with a blank file and write from scratch, or start with one program and incorporate the other.
    - Decide to what extent you want the students to collaborate; even if they help each other they will likely end up with subtly different solutions.
    - Emphasise the fact that there is no single correct solution.

## Plenary

Students should be given a chance to review each other's code and comments. They should be providing feedback and advice, and commenting on whether they each have a working solution. Spend a moment reviewing the concepts they have covered in this scheme, and to what extent they understood and applied them.

## What's next?

- Students could use this code to deploy a basic version of the weather station, which displays data on rainfall and wind speed.
- Consider what's missing from this solution. Clearly only two of the sensors have been covered but what else is missing?
- Is this the best way to display the data?
- Is data being saved? Could I look back at previous data?
