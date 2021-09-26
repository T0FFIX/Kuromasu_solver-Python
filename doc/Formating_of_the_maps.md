The maps here are formatted as follows:
- height of the map,
- width of the map,
- next is 0,1 or a number higher than 1,
- 0 means that this cell is white,
- 1 means that this cell is black !!(on a empty map there should not be a number 1 because its against the rules)!!,
- a number higher than 1 for example 7 means that this is a number cell and it needs to have exactly the number of white cells sticking to it vertically and/or horizontally.

You should write starting from the left upper corner and go to the right side and on the next line always go from left to right.
here is an example of an empty map:
4,4,5,0,0,0,0,0,0,3,0,3,0,0,4,0,0,2

Actual map appearance:
- 5 0 0 0 
- 0 0 0 3 
- 0 3 0 0 
- 4 0 0 2 

and the answer for this map is:
4,4,5,0,1,0,0,1,0,3,0,3,0,1,4,1,0,2

you can check it by yourself by solving it on sheet of paper.