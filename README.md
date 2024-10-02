# Blackjack

## Description
This was the final project for freeCodeCamp's "Python for Beginners" YouTube course which was a 4 hour 40 minute course covering Python fundamentals.

## Modifications to the original project
- I studied the game and made modifications to handle some situations like having more than one ace at a time and letting the dealer draw cards to attempt matching a player hand of 21.
- Added a Table class for displaying the hands on screen.
- Added inheritance to the project by creating a ClearScreen class inherited by the Game and Table classes to clear the screen between game events.
- Added a statistics screen to the end of the game flow to see how many games the dealer and player won, how many pushes there were, and how many blackjacks the dealer and player had.
- Divided the project's classes into individual modules.

## How To Run
Fork the project and clone it to your machine. You will need to have Python 3 installed. You can download Python 3 at [python.org](https://www.python.org/). 
1. Open your terminal window. 
2. Navigate to the folder you cloned this project to. 
3. Type `python3 main.py`.

## MIT License
Copyright (c) 2024 Russell Propert

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
