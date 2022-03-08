# Horse Hangman


## Overview

[Horse Hangman](https://horse-hangman.herokuapp.com/) is a python terminal game that runs on Heroku.


### How to Play
The game is based on the traditional Hangman word guessing game, the only difference is that all the words for this game are related to horses. The game starts with asking for the user to enter their name before asking the user to input a letter. The user has six lives (attempts) and if a letter is guessed wrong the user looses a life and the hangman picture starts to build, as the user looses lives the colour of the Hangman picture updates from Green to Yellow and then to the Red danger zone. On completion of the game the user has the option to 'Play Again' or exit the game.


<div><h2>
Site Mockup
</h2></div>


<img src=images/Mockup.JPG>


## Flowchart


<img src=images/flowchart.JPG>


## User Experience

Goals:

- Provide a fun interactive experience
- Provide a great user experience.
- Be easy to navigate
- Give clear calls to action
- Function in a logical correct way

First Time User:

- I want to be able to navigate the game terminal and understand its objectives clearly without confusion.
- I want to clearly understand how to complete the game

Returning/ Regular Visitor: 

- I would like to see more game options/ levels.
- I would like to see the game updated & refreshed monthly with new challenges.


## Features 

- Welcome Greeting for user
- Prompt for user to enter their Name

<img src=images/welcome_msg.jpg>

- Loading of the game rules
- Prompt for user to enter a Letter

<img src=images/load_rules.jpg>


- Hangman Picture & correctly guessed letters display after user submits a guess

if correct letter:

<img src=images/letter_guess_correct.jpg>

if incorrect letter:

<img src=images/letter_guess_wrong.jpg>


- Winner message displays if user corectly guesses the word

<img src=images/win.jpg>

- Loser message displays if user incorrectly guesses the word

<img src=images/loser.JPG>

- Play again option is presented on completion of the game

if No:

<img src=images/play_again_n.JPG>

if Yes:

<img src=images/play_again_y.JPG>

- Input validation is implemented for when the user enters invalid data, only alpha characters are accepted as valid

Input name:

<img src=images/invalid_name.JPG>

Input a number/ special character:

<img src=images/entered_number.jpg>

Input multiple letters/numbers:

<img src=images/enter_multiple_text.jpg>

Enter return instead of a letter:

<img src=images/entered_return.jpg>


### Features Left to Implement

- User Score Board
- Improve Game display
- Add logo/ improve art work
- Add multiple game levels e.g Easy, Moderate, Hard
       

## Languages Used
- Python

Python Packages:

- Random: returns a random integer to get a random word
- Colorama: allows terminal text to be printed in different colours / styles
- Time: defined time sleep
- OS: modules provide numerous tools to deal with filenames, paths, directories


## Frameworks, Libaries and technologies used

- [Git/ Github](https://github.com/) - Git/Github was used for version control, storage and deployment of the project.
- [Heroku](https://www.heroku.com/) - Heroku was used to deploy and create the terminal application.
- [Techsini](https://techsini.com/multi-mockup) - This was used for the mockup image in the overview.


## Testing Conducted 

### Usability testing 

I tested the game application thoroughly and repetitively throughout the python coding, using print() where necessary and the python3 run.py in the Git terminal. 
I also had work colleagues and family members assistance to test the site usability. 
I tested all game actions/ functions to ensure that they were working as expected.
I tested the game rules logic was working as expected.

Test Scripts actioned:

1. Test that greeting message loads as expected and User can input a valid name:

  - Navigate to Heroku deployed link
  - Check greeting loads as expected
  - Enter a valid name 
  - Test passed 

2. Test that greeting message loads as expected and User is asked to re-input their name if invalid data is entered:

  - Navigate to Heroku deployed link
  - Check greeting loads as expected
  - Enter an invalid name containing special characters/ numbers
  - User is presented with message stating name is invalid please enter a valid name
  - Test passed

3. Test that the user name is loaded and the rules display with the time delay

  Navigate to Heroku deployed link
  - Check greeting loads as expected
  - Enter a valid name 
  - Check that the user name is then printed to the terminal in the next statment
  - Test Passed 
  
4. Test that the User can enter a letter and return a result

  - Navigate to Heroku deployed link
  - Check greeting loads as expected
  - Enter a valid name 
  - Enter a letter 
  - Input accepted 
  - Test passed

5. Test that the User cannot continue the game if they do not enter a valid input

  - Navigate to Heroku deployed link
  - Check greeting loads as expected
  - Enter a valid name 
  - Enter a number 
  - Error message displays asking user to enter a letter 
  - Enter a special character
  - Error message displays asking user to enter a letter 
  - Enter multiple letters/ numbers combination
  - Error message displays asking user to enter a letter
  - Hit the return button
  - Error message displays asking user to enter a letter
  - All input validation Tests passed

6. Test that when the user enters the same letter twice they are prompted to enter a new letter

  - Navigate to Heroku deployed link
  - Check greeting loads as expected
  - Enter a valid name 
  - Enter a letter
  - Enter the same letter again
  - Confirm that the print message informs the user they have already guessed that letter and to enter another
  - Test Passed

7. Test that the hangman picture builds correctly

  - Navigate to Heroku deployed link
  - Check greeting loads as expected
  - Enter a valid name 
  - Enter a letter
  - Continue playing the game monitoring that the hangman picture is populated as the guesses are incorrect
  - Test Passed

8. Test that the correctly guessed letters display correctly 

  - Navigate to Heroku deployed link
  - Check greeting loads as expected
  - Enter a valid name 
  - Enter a letter
  - Continue playing the game monitoring that the guessed letters are populated under the hangman picture in the correct order
  - Test Passed

9. Test that the attempt counter decreases correctly
  - Navigate to Heroku deployed link
  - Check greeting loads as expected
  - Enter a valid name 
  - Enter a letter
  - Continue playing the game monitoring that the guess attempts are decreasing with each incorrect guess 
  - Test Passed

10. Test that the option to play again works as expected
  - Navigate to Heroku deployed link
  - Check greeting loads as expected
  - Enter a valid name 
  - Enter a letter
  - Continue playing the game until the play again method is displayed
  - Run this test multiple times selecting Y/N and other characters
  - Test Passed

11. Test that the secret word is being randomly selected
  - Play the game multiple times consecutively taking note of the random word being supplied
  - All Tests Passed, word is random

12. Test that the colours are displaying as expected

  - Play the game multiple times consecutively taking note of the colurs being generated in the terminal and compare to the code base 
  -  Test Passed


The conclusion of repeating the above test scripts multiple times was that:

- The game itself was understandable and easy to follow.
- The random select word logic is working as expected.
- The game handles invalid data entry correctly.
- The guess counters are being incremented correcly.
- The game only actions the play again function once all guess attempts or when the word has been guessed correctly.
- The hangman picture displays as expected when a letter is guessed wrong or right.


### Bugs

- In my initial testing the Hangman picture was building backwards, I fixed this by updating the code with a wrong_guess counter 
- In initial testing the user could run through the game to the end without input by hitting the Return key, I fixed this by updating the else statment in the run game method to catch and invalidate this action.
- In initial testing the user could enter multiple letters without any feedback/ error, I fixed this by updating the else statment in the run game method to catch and invalidate this action. 
- In the play again function it asks for Y/N, however initially if the user selected any key or hit enter the terminal would either go blank or the end message would appear. I fixed this by updating the else statment to clear the terminal and load the game.


### Content 

I reviewed all content on the site for:
- grammar and spelling mistakes
- Hangman pictures are placed properly with proper sizes & displaying as expected
- Instructions are clear and contain correct information
- Verified all text/ headings are displaying correctly


### Validation

I ran all the Python Code through [PEP8](http://pep8online.com/)

No errors detected

### run.py:
<img src=images/run.JPG>

### words.py:
<img src=images/Words.jpg>

### hangman_pics.py:
<img src=images/Hangman_pic.jpg>


## Lighthouse

Lighthouse was used to test Performance, Best Practices, Accessibility and SEO on Desktop.

<img src=images/lighthouse.JPG>


## Credits

Python Code inspired and adapted from the following tutorials and sources:

- https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman

- https://inventwithpython.com/invent4thed/chapter8.html

- https://www.w3schools.com/python/default.asp

- https://www.youtube.com/watch?v=pFvSb7cb_Us

- https://www.mikedane.com/programming-languages/python/guessing-game/

- https://www.numpyninja.com/post/how-to-format-strings-using-print-in-python

- https://note.nkmk.me/en/python-textwrap-wrap-fill-shorten/

- https://www.sololearn.com/Discuss/1582033/how-to-check-if-input-is-empty-in-python

- And of course the Code Institute Python online module & challenges/ Love Sandwiches

Flowchart created in:

- https://app.diagrams.net/


### Content

All content was written by the project owner.


### Readme 

- I used the 
[Markdown cheat sheet](https://github.com/tchapi/markdown-cheatsheet/blob/master/README.md) and the [love running template ](https://github.com/Code-Institute-Solutions/readme-template )to help put together my readme.


### Acknowledgments

I would like to thank my mentor Akshat Garg for his guidence.


# Deployment

The site was deployed to Heroku. 

The steps to deploy are as follows: 

- Log in to Heroku or create an account
- On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App
- You must enter a unique app name
- Next select your region
- Click on the Create App button
- The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
- Click Reveal Config Vars and enter port into the Key box and 8000 into the Value box and click the Add button
- Scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
- Repeat step 8 to add node.js. o Note: The Buildpacks must be in the correct order. If not click and drag them to move into the correct order
- Go to the top of the page and choose the Deploy tab
- Select Github as the deployment method
- Confirm you want to connect to GitHub
- Search for the repository name and click the connect button
- Scroll to the bottom of the deploy page and select the preferred deployment type
- Click either Enable Automatic Deploys for automatic deployment when you push updates to Github

  - On submission the project is forked in Github, by forking the project a copy of the original repository is made that can be viewed without affecting the original repository by following these steps: In the GitHub repository, locate the settings, above this is the option to 'fork', select this to create a copy

  - Cloning a repository: When you create a repository on GitHub.com, it exists as a remote repository. You can clone your repository to create a local copy on your computer and sync between the two locations. It makes it easier to fix merge conflicts, add or remove files, and push larger commits. 

The live link can be found here - https://horse-hangman.herokuapp.com/ 