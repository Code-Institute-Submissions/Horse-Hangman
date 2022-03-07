# Horse Hangman

## Overview

[Horse Hangman Deployed Site Link](https://horse-hangman.herokuapp.com/) is a python terminal game that runs on Heroku.

### How to Play
The game is based on the traditional Hangman word guessing game, the only difference is that all the words for this game are related to horses. The user has six lives (attempts) they must guess a letter and if wrong the user looses a life and the hangman picture starts to build, on completion of the game the user has the option to 'Play Again'.

<div><center><h2>
Site Mockup
</h2></center></div>

<img src=>

## Features 

### The About Section

#### Contains:



 
### Features Left to Implement
       

## Languages Used
- Python


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

1. 

The conclusion of repeating the above test scripts multiple times was that:

- The game itself was understandable and easy to follow.
- The random select word logic is working as expected.
- The guess counters are being incremented correcly.
- The game only actions the play again function once all guess attempts or when the word has been guessed corectly.
- answered.


### Bugs

- Hangman pic build backwards
- Return key
- multiple letters entered

### Content 

I reviewed all content on the site for:
- grammar and spelling mistakes
- Hangman pictures are placed properly with proper sizes & displaying as expected
- Instructions are clear and contain correct information
- Verified all text/ headings are displaying correctly



### Validation

I ran the Python Code through [PEP8](http://pep8online.com/)

No errors detected

I ran the code through .


## Credits

### Python:

Code inspired and adapted from the following tutorials and sources:
- 
And of course the Code Institute Javascript online module & challenges/ Love Sandwiches


### Content

All content was written by the project owner.


### Readme 

- I used the 
[Markdown cheat sheet](https://github.com/tchapi/markdown-cheatsheet/blob/master/README.md) and the [love running template ](https://github.com/Code-Institute-Solutions/readme-template )to help put together my readme.

## Acknowledgments

I would like to thank my mentor Akshat Garg for his guidence.

# Deployment

The site was deployed via GitHub pages to Heroku. 

The steps to deploy are as follows: 
  - I created a new Github repository to host all my python code before creating a new Heroku application, in Heroku I set the buildbacks to Python and Node.js, added the 8000 port in the config vars and then linked the Github repository before manually deploying. Once manual deployment was sucessful I enabled automatic deployments so all changes in my Github repository were pushed automatically to Heroku.

  - On submission the project it is forked, by forking the project a copy of the original repository is made that can be viewed without affecting the original repository by following these steps: In the GitHub repository, locate the settings, above this is the option to 'fork', select this to create a copy

  - Cloning a repository: When you create a repository on GitHub.com, it exists as a remote repository. You can clone your repository to create a local copy on your computer and sync between the two locations. It makes it easier to fix merge conflicts, add or remove files, and push larger commits. 

The live link can be found here - https://horse-hangman.herokuapp.com/ 