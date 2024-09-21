Deck Shuffle Algorithm by Chad Jemmett
======================================

## Purpose: ##
Demonstrate my skills in sorting a shuffled standard deck of 52 playing cards. 

## Input ##
A text file with a list of 52 randomized cards generated here [random.org](https://www.random.org/playing-cards/)

## Output ##
A text file with a list of 52 sorted cards.

## Assumptions ##
* The input is a text file with strings that explain the card. Like 'Ace of Spades'. Each entry is separated by
a newline character.
* The cards are a standard deck of playing cards written in english. 
* There are fours suits.
* There are three face-cards and one Ace.
* The face value of the remaining cards is 2 - 10

## Reasoning for Implementation ##
I wanted an algorithm that had an O(n) runtime. There are 5 loops in the code. But there are no nested loops. 

I used a hash table reference to give integer values to strings. So that 'Two' became the integer 2. This also gave
the face cards integer values. ie: Queen == 13.
This made sorting easier. I iterated over the exisiting hash table to reverse it. So the integer values would
become String values when printing the sorted deck to a text file.

For sorting, I used Python's built in `sort` method for python `lists`. To specify which value to sort by I used an
anonymous function or a `lambda`.
For other alterations I used a basic  loop to accomplish tasks like replacing the string values in the hash
table with integer values.

## Limitations ##
This would only work for a standard english-language deck of cards. The assumption that the deck would only
contain 52 cards may be a bad assumtion. This algorithm would sort more than 52 cards. But the result would
be 
        Ace of Clubs
        Ace of Clubs
        One of Clubs
        One of Clubs

and on and on.


