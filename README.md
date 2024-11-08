# Haunted-House-Duplicate-Clues

## Members :

<li>Emmanuel Montoya</li>
<li>Rouni Assaf</li>

## Description :

You're exploring a haunted house with a series of spooky rooms, each room containing a
single clue represented by a unique number. All rooms are connected in a chain-like
structure, forming a linked list where each room points to the next one.
Due to the haunted nature of the house, one of the clues is duplicated, and it’s causing
you to keep looping back to that clue. This loop traps you in the haunted maze! Your goal
is to find the duplicate clue so you can escape the endless cycle.

You are given the head of a linked list, rooms, where:
1. Each node in rooms has a value(clue) in the range [1, n], where n is the number of
rooms.
2. The list has n + 1 nodes (with n unique clues and 1 duplicate).
Input:
rooms = The head node of a linked list representing the rooms and their clues. Each node
has a value as your clue in the range [1, n], where n is the number of rooms.
Output:
Returns an integer representing the duplicate clue that traps you in the haunted loop.


## Sample 1:
<p>Input: rooms = [5,3,4,7,7]</p>
<p>Output: 7</p>


## Sample 2:
<p>Input: rooms = [8,1,8,4,6,5,2]</p>
<p>Output: 8</p>


## Sample 3:
<p>Input: rooms = [3,3,3,3,3]</p>
<p>Output: 3</p>


<b>**Optional Constraint :
Can you solve the problem in linear time complexity and constant space?</b>
