#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
n=2 2*2 = 4
0 < 8   1
4 < 8   2

n=3 3*3 = 9
0 < 27      1
9 < 27      2
18 < 27     3

n = 4  4*4 = 16
0 < 64      1
16 < 64     2
32 < 64     3
48 < 64     4

n = 10 10*10 = 100
0 < 1000        1
100 < 1000      2
200 < 1000      3
300 < 1000      4
400 < 1000      5
500 < 1000      6
600 < 1000      7
700 < 1000      8
800 < 1000      9
900 < 1000      10

The runtime of this is O(n) since as the size of the input increases the number of iterations increases linearly. If there 
were a function to determine how many iterations it would take for a given n value, it would be F(x) = x or O(n) = n.


b) this is also linear O(n) because every element leading up to n is seen only once, so as the input n grows the iterations grow linearly as well. The while loop on the inside adds on average 4-7 extra iterations depending on n which to me seems pretty insignificant to change the time complexity.


c) this is also O(n) or linear because as the size of n increases the number of iterations linearly grow with the input. If n == 5
it takes 5 loops to get your answer, if n == 1000 it takes 1000 loops to get your answer

## Exercise II
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


if the building is 10 stories high the egg wont be broken from the 6th floor
if the building is 12 stories high the egg wont be broken from the 7th floor
if the building is 14 stories high the egg wont be broken from the 7th floor
if the building is 25 stories high the egg wont be broken from the 10th floor
if the building is 100 stories high the egg wont be broken from the 20th floor
f(n) = sqrt(n) * 2

time complexity is O(sqrt(n))


