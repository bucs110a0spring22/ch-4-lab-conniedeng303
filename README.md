

## SUMMARY:
        What did you clean up?:
To align my code with conventions, I saved every stray number to a variable. For example, the starting point of all my trig functions were saved to a variable. The only exception is the drawAxis function, which I felt would have only increased the length.

For some of my functions, it made more sense to put parameters in them. For example, I made all of my functions that drew trig graphs include parameters that have starting and ending degrees.By doing this, I am also able to tweak parameters to change how the graph would look,such as only graphing SIN from one specifc degree to another degree.

In terms of updating my code, I updated my SetupAxis function where I created a loop that creates my axis (I also made it shorter than 12 lines of code, a guideline mentioned in the grading guidelines) instead of hardcoding every directional instruction for my turtle.
 
        Summary of function(s) added:

To start off adding an additional function, I wanted to see if I could graph the recipocal of sin, or csc. To do that, I had to import mpmath to use its csc function to graph it. I also decided to fully change the coordinates by doing "wn.setworldcoordinates(-360,-5,360,5)", which zooms out enough where I can see both the trig function graphs AND the csc graph.

 For my return functions, I wanted to see the difference in values between my Sin and Csc values (csc is the recipocal of sin), so I created functions that would return the y values of user inputs.  {ReturnSinFunctionValue(),ReturnCSCFunctionValue()}

 For my parameter functions, I wanted to create a function that would be able to adjust the period and y-axis of my sin graph. To do this, I looked up the equation that would shift the sin graph, and adjusted my parameters to fit in the equation. The new parameters that i created were period and y-axis, which I could input values to change how the sin graph looked. {graphswithperiods}

        Summary of Feature Added:
For my function, I created a game of cat and mouse, where the first part would be the player trying to avoid being crushed by a cat, while the second part would be another fun game of chance. For the first part, I created a function called catchooses which chooses the side that the cat decided to. The player would then chose a side to hopefully not be pounced on. For the second part, I created a toxicfood function that draws the orange and gives a random chance that it is poisoned. 

## KNOWN BUGS AND INCOMPLETE PARTS:
 None.

## REFERENCES:
 < (https://mpmath.org/doc/current/functions/trigonometric.html) = How to import mpmath and use csc 
 https://careerkarma.com/blog/python-break-and-continue/#:~:text=Python%20Continue%20Statement,-The%20continue%20statement&text=You%20can%20use%20a%20continue,usually%20after%20an%20if%20statement. = I used this to skip 0>

## MISCELLANEOUS COMMENTS:
   I would like the two functions that I have at the end to be considered one feature.
