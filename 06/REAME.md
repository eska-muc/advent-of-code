# Day 06

## Part 1

Part1 is pretty straight forward.

## Part 2

This is the tricky one for today!

Ideas:

* loop detection:
  * keep track of turning points position, old direction, new direction
    * if a turning point with same parameters is reached for the second time, loop found
  * use characters '^', 'v', '<' and '>' instead of 'X'. If a possible next field contains the symbol of the current direction, a loop has been detected
  * in the end I used 4 maps (one for each direction), which counts how often a position was visited in one direction, if the count is >1 this means that a loop is detected
* possible locations:
  * all fields with an initial '.'
  * input is 130 x 130 = 16,900 possible positions for the obstacle
    * brute force:
      * for all positions in th 130 by 130 map
        * check if field is empty, if so it's a possible position for the obstacle
        * put obstacle at candidate position
        * start simulation
        * if guard gets stuck, increase count
