

## SUMMARY:
What did you clean up?:

To align my code with conventions, I saved every stray number to a variable. For example, the starting point of all my trig functions were saved to a variable. 
By doing this, I am also able to tweak parameters to change how the graph would look,such as only graphing SIN from one specifc degree to another degree.

In terms of updating my code, I updated my SetupAxis function where I created a loop that creates my axis (I also made it shorter than 12 lines of code, a guideline mentioned in the grading guidelines) instead of hardcoding every directional instruction for my turtle.
 
        Summary of function(s) added:

To start off adding an additional function, I wanted to see if I could graph the recipocal of sin, or csc. To do that, I had to import mpmath to use its csc function to graph it. I also decided to fully change the coordinates by doing "wn.setworldcoordinates(-360,-5,360,5)", which zooms out enough where I can see both the trig function graphs AND the csc graph.

 For my return functions, I wanted to see the difference in values between my Sin and Csc values (csc is the recipocal of sin), so I created functions that would return the y values of user inputs 

 For my parameter functions, I wanted to create a function that would be able to adjust the period and y-axis of my sin graph. To do this, I looked up the equation that would shift the sin graph, and adjusted my parameters to fit in the equation. The new parameters that i created were period and y-axis, which I could input values to change how the sin graph looked.

Summary of Feature Added:
For my function, I created a game of cat and mouse, where I 
I created a function called catchooses which chooses the side that the cat decided

## KNOWN BUGS AND INCOMPLETE PARTS:
 < What parts of the project you were not able to complete >

## REFERENCES:
 < (https://mpmath.org/doc/current/functions/trigonometric.html) = How to import mpmath and use csc >

## MISCELLANEOUS COMMENTS:
 < Anything you would like the grader to know >
