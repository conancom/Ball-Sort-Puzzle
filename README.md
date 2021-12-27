# Ball-Sort-Puzzle Algorithm
Ball Sort Puzzle Algorithm using Uniform-Cost Graph Search

This algorithm solves the puzzle seen in the picture below.

![image](https://user-images.githubusercontent.com/79465272/147432158-60638aca-5e41-430a-82e1-8a4a6ff0dd5a.png)

>- Initial [Input] State is a `4 by 4 Matrix containing 4 Characters, each occuring 4 times in any order`
<pre> 
Example : A A C C
          A A C B
          D D D B
          C B D B
</pre>

>- Actions that are possible at each step `Move the Top element [Last element of the array] of a column to any other column if it hasn't 4 elements yet`
>- Goal State is a `4 by 6 Matrix containing 4 Characters, each occuring 4 times in a column, and 2 empty columns`


## Implementation

I choose to use a 2-Dimensional Array instead of an Array of Stacks, since after some testing, the 2-Dimensional Array version was a bit faster (for some reason 😕).

Using an Array of Stacks works as well, which I will be implemting once more later on.
