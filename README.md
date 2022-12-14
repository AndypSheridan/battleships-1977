# **Battleships 1977**
## **Overview**


Battleships 1977 is a python-based version of the classic Battleships board game. In this particular iteration of the game, the user plays against the computer in a turn-based competition where the objective is to eliminate all of the opponent's ships before their own are destroyed.

This game is played in a 6 x 6 tile grid. The user and CPU each have four ships of lengths one, two, three and four tiles. The player takes turns with the CPU to guess the coordinates of the opposing ships. When either the user or CPU hits and destroys all of them, the game is over.

This edition of the game has been loosely based on the popular sci-fi saga 'Star Wars' The original movie was released in 1977, hence the appendage to the title of the game.

The game is Python-based and uses a game Board class, functions, for loops, while loops and if/elif/else statements to achieve the desired outcome.

It features space-based ASCII art, and contains various references to characters, vessels and ideologies from the movie. The intention was to provide a fresh and different setting to the classic game which is situated in an ocean and played with contemporary seafaring vessels such as aircraft carriers and frigates etc.

The user is guided through some Star Wars-related imagery and text before being prompted to enter their name. The rules and legend are presented before the game requests the user place their ships on the board. There is the option to place the ships horizontally or vertically, and then the use must decide on x and y coordinates to assign the relevant ship.

The CPU ships are assigned random coordinates. The game is designed so that the user goes first. Upon completion of the game, the user is presented with a screen informing them that they have either won or lost. Then they are asked if they wish to play again or quit.

Click [here](https://battleships-1977.herokuapp.com/) to see the final deployment of the game

![Am I Responsive Screenshot](assets/images/bs1977-am-i-responsive.png)
![Am I Responsive Screenshot](assets/images/bs1977-am-i-responsive-name.png)

???
## Table of contents:
1. [**Site Overview**](#site-overview)
1. [**Planning stage**](#planning-stage)
    * [***Target Audiences***](#target-audiences)
    * [***User Stories***](#user-stories)
    * [***Site Aims***](#site-aims)
    * [***Lucid Chart***](#lucid-chart)
    * [***Color Scheme***](#color-scheme)
    * [***Typography***](#typography)
1. [**Current Features**](#current-features)
    * [***Data Module***](#data-module)
    * [***Start Screen***](#start-screen)
    * [***Pre-Game***](#pre-game)
    * [***Gameplay***](#gameplay)
    * [***Game Over***](#game-over)
1. [**Future-Enhancements**](#future-enhancements)
1. [**Testing Phase**](#testing-phase)
1. [**Deployment**](#deployment)
1. [**Tech**](#tech)
1. [**Credits**](#credits)
    * [**Content**](#content)
    * [**Media**](#media)
    * [**Honourable mentions**](#honorable-mentions)
???
## **Planning Stage**

<br>

#### **Target Audiences:**
* People who like the classic Battleships??? game.
* People who are looking for a science-fiction-based take on the classic game.
* People looking for an online version of the game.
* People who are fans of Star Wars.
* Aspiring coders looking for a simple but effective code.

???
#### **User Stories:**
* As a user, I want to understand the premise of the game.
* As a user, I want to quickly learn and understand the rules of the game and its instructions.
* As a user, I want a clean and simple user interface (UI).
* As a user, I want the game to run smoothly and bug-free.
* As a user, I want to be able to choose whether or not to play again when the game ends.
* As a user, I want to be able to win against the computer.

???
#### **Site Aims:**
* To offer the user a smooth and bug free version of a classic game with a slightly different twist.
* To provide a clean and simple interface for the user with no need to reference external sources.
* To provide clear instructions and a win condition.
* To provide an enjoyable user experience of playing battleships.
* To provide an interesting and entertaining Star Wars-based version of the game.

<br>

#### **Lucid Chart:**

To help with the planning stages?????? of this project, I used [LucidChart](https://www.lucidchart.com)
This proved to be very useful tool when it came to visualising the various processes involved in recreating a Battleships style game. Whilst the concept is quite simple, the logic involved proved slightly more difficult.

This is the flow chart which assisted the development of the game:


![Lucid Chart](assets/images/BS1977chart.png)


<br>???

#### **Colour Scheme:**
???

* Not in the scope of this project, however I used cyan text for the start screen to evoke a connection with the Star Wars theme. I then used yellow for the subsequent text for the same reason.

???
#### **Typography**
???
* Not in the scope of this project.

???<br>


## **Features**

#### **Data Model**

* The game uses a Board class. It is used to create instances of the player and CPU and guess boards. Only the player and player_guess boards are printed to the terminal through the display_boards method. The class stores the board size, board owner and shield strength. There are methods to input ship coordinates, populate the board, logic for CPU guesses. There are also methods to check and validate user input as well as prevent any ships overlapping.
???
#### **Start Screen** 

![Screenshot of start screen](assets/images/bs77-start-screen.png)

* The start screen features the iconic Star Wars introduction: "A long time ago, in a galaxy far, far away..." Beneath that is some very basic ASCII art depicting stars. There a short time delay using the time.sleep() function to allow the user to process the screen. They are then prompted to press enter.

![Screenshot of player name input](assets/images/bs77-name-input.png)

* The os.sys("clear") function is used to clear the screen and the user is then presented with ASCII text intended to emulate the Star Wars movie font. They are prompted to enter their name using the get_name function which stores the username in a variable for use in the game. They are then presented with a short welcome message and short backstory explaining enemy ships have entered the area. The user can press enter to proceed to the next screen.

#### **Pre-Game**

![Screenshot of ship types](assets/images/bs77-ship-types.png)

* The same os function is used to clear the terminal once again. The ship_type method is called so the user is presented with the four different types of ships at their disposal, along with the size of each. The ships are displayed sequentially in descending size order, on a slight delay using the time library.

![Screenshot of legend](assets/images/bs77-legend.png)

* Upon pressing enter, the game_rules function is called to display the symbols which will be used on the game boards. Once the user has processed the information, they are prompted to press enter again.

* The following text explains the win condition which states that ten hits will be enough to win the game. There is a final prompt to press enter.

![Screenshot of win condition](assets/images/bs77-win-condition.png)


![Screenshot of player board and prompt to enter ship direction](assets/images/bs77-choose-direction.png)

* os is used to clear the screen once again and the player board is printed to the terminal. It displays the player name and the shield strength at the starting value of 10. The place_ships method is called so the player is asked to place each ship by choosing whether it will be aligned horizontally or vertically. Any input other than 'h'/'H' or 'v'/'V' will be invalid and the user will be asked to try again. The process will loop until all ships have been assigned coordinates.

#### **Gameplay**

![Screenshot of player hitting ship](assets/images/bs77-hit-ship.png)

* The populate_boards method adds the user and CPU ships to their respective boards. The user cannot see where the CPU ships are. The game is set up so the user goes first. The player_attack method takes input from the user to guess enemy ship coordinates on the x and y axes. The first CPU guess is a random choice on the board. Upon a successful hit, the CPU will attempt to guess on an adjacent tile. Click the highlighted text to see screenshots of the player entering invalid [row](assets/images/bs77-invalid-row.png) or [column](assets/images/bs77-invalid-column.png) coordinates. The user cannot enter the same coordinates twice. Most of the game logic is in the play_game function which handles updating and appending the relevant boards. It also handles decrementing the shield counter. The game will continue to run until either the player or CPU shield counters reaches zero.


#### **Game Over** 
![Screenshot of play again option](assets/images/bs77-play-again.png)
![Screenshot of choosing not to play again](assets/images/bs77-play-again-no.png)

* Upon winning or losing the game, an ASCII-based message is displayed before the user is given the option of playing a new game. If this option is chosen, the game resets and starts from the beginning. If the user chooses to quit, they are presented with s short message in keeping with the theme of the game.


<br>

???
## **Future-Enhancements**
???
There are a several areas with scope for future improvement. This project has been very challenging and ultimately the project deadline was looming. I would have liked to add the following:
???
* Adding a player vs player option.
* The option of skipping the rules and legend for returning players.
* The option to randomly place player ships for quicker games.
* An option to have small, medium or large boards with corresponding ship sizes.

???
## **Testing Phase**
???
**Functionality**

* Implementation ????: I wanted to make sure the game performed as expected from start to finish.
* Test ????: I played the game on a local terminal and on Heroku over thirty times.
* Result ????: The game worked as anticipated with no errors.
* Verdict ???: Test passed.

<br>

* Implementation ????: Check the input validation was working as expected.
* Test ????: Invalid inputs and types were entered multiple times at all possible opportunities.
* Result ????: The validation worked well. There were no occasions when it was possible to enter an invalid input.
* Verdict ???: Test passed.

<br>

* Implementation ????: I wanted to make sure the game performed as expected from start to finish.
* Test ????: I played the game on a local terminal and on Heroku over thirty times.
* Result ????: The game worked as anticipated with no errors.
* Verdict ???: Test passed.

<br>

* Implementation ????: Check the game ends as expected and offers the play again option upon completion.
* Test ????: I played the game multiple times, winning and losing. I selected play again and quit at random.
* Result ????: The game worked as anticipated with no errors.
* Verdict ???: Test passed.
<br>
???
**Validators**

* The PEP8 Online Validator was down when creating this project, however I added a PEP8 validator to my workspace by running the command: "pip3 install pycodestyle". The results can be found [here](assets/images/bs1977-pycodestyle.png)

* The validator flags a number of minor warnings, all of which are related to the use of the ASCII art used in the start screen, win screen and lose screen functions. In my final mentor session, I was informed these are inconsequential and can essentially be ignored as they do not affect the program itself.

???
???
## **Bugs**
???
The following bugs were identified during user testing:

* ???? - When running the game it was possible for the user and CPU to place ships so that they overlapped.
* ?????? - There were errors in the check_ship_placement method of the code.
* ??? - I made adjustments to the method to prevent any overlap.

<br>

* ???? - It was possible for both player and CPU to place ships off the board.
* ?????? - There was an error in the populate_boards method.
* ??? - The entire method was re-written to take into account zero indexing.

???<br>

* ???? - Upon re-writing the populate boards method, ship x and y coordinates were reversed so ships did not orient correctly.
* ?????? - There was an error with the for loop in the nested if statement in the populate boards method.
* ??? - I reversed the values for row and column and this fixed the bug.

<br>

* ???? - The original SCSS background worked well on a MacBook Pro but caused huge lag and unplayable game quality on some devices.
* ?????? - The SCSS was too CPU intensive on some devices.
* ??? - I used a different background animation which was more subtle but works on all devices in testing.

<br>

* ???? - The game was printing too much text for the size of the terminal so the screen was overloaded with information.
* ?????? - There is a lot of information to deliver to the user and it all displayed at once which could be overwhelming.
* ??? - Imported the os and time libraries so I could clear the terminal before delivering the next stage of the game, time was used to slow down printing to the terminal and also simulate computer thinking.


<br>

## **Unfixed Bugs**

* There are no known unfixed bugs.

## **Deployment**

## ***Final Deployment to Heroku:***  
  
The project was deployed to [Heroku](https://www.heroku.com) using the below procedure:-    
  
1. **Log in to Heroku** or create an account if required.
1. **click** the button labeled **New** from the dashboard in the top right corner, just below the header.
1. From the drop-down menu **select "Create new app"**.
1. **Enter a unique app name**. I chose battleships-1977 for this project, for reasons stated above.
1. Once the web portal shows the green tick to confirm the name is original **select the relevant region.** In my case, I chose Europe as I am in the UK.
1.  When happy with your choice of name and that the correct region is selected, **click** on the **"Create app" button**.
1. This will bring you to the project "Deploy" tab. From here, navigate to the **settings tab** and scroll down to the **"Config Vars" section**. 
1. **Click** the button labelled **"Reveal Config Vars"** and **enter** the **"key" as port**, the **"value" as 8000** and **click** the **"add"** button.
1. Scroll down to the **buildpacks section of the settings page** and click the button labeled **" add buildpack," select "Python," and click "Save Changes"**.
1. **Repeat step 11 but** this time **add "node.js" instead of python**. 
   * ***IMPORTANT*** The buildpacks must be in the correct order. If node.js is listed first under this section, you can click on python and drag it upwards to change it to the first buildpack in the list.
1. Scroll back to the top of the settings page, and **navigate to the "Deploy" tab.**
1. From the deploy tab **select Github as the deployment method**.
1. **Confirm** you want to **connect to GitHub**.
1. **Search** for the **repository name** and **click** the **connect** button next to the intended repository.
1. From the bottom of the deploy page **select your preferred deployment type** by follow one of the below steps:  
   * Clicking either "Enable Automatic Deploys" for automatic deployment when you push updates to Github.  
   * Select the correct branch for deployment from the drop-down menu and click the "Deploy Branch" button for manual deployment. 

The final deployment can be viewed [here](https://battleships-1977.herokuapp.com/)
???
## **Tech**
???
I used the following technologies for the Battleships 1977 project:
???
- Python

## **Libraries**

The following libraries were used:

* Random - Used to generate random numbers for CPU ship placement, CPU guessing and CPU attacks.
* OS - Used to clear the terminal so the user would not get overwhelmed with information.
* RE - Used to check for valid column input.
* Time - Used for pauses in flow of information and to simulate CPU decision making.

## **Software**

The following software was used:

- Gitpod and VS Code to create, load and push my code to Github.
- Git (Gitpod and Github) as my version control for the site.
- Heroku to deploy the project.
- Lucid Chart to develop the logic for the project.
- https://patorjk.com/ to develop the ASCII art for the project

### **Media:**

* Not in the scope of this project.
???
<br>


## **Credits**
???
* The ANSI colour codes came from [this article](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html) on lihaoyi.com.

* The idea to use the os library to clear the screen came from [this post](https://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python) on Stack Overflow.

* The idea to use the time library to delay the execution of the problem came from [this article](https://www.digitalocean.com/community/tutorials/python-time-sleep) on the Digital Ocean website.

* The code to use the re library came from [this article](https://stackoverflow.com/questions/60597167/using-regex-to-validate-user-input) on Stack Overflow.

* The unicode for the bullet symbols and up and down arrow came from the [Python Docs Website](https://docs.python.org/3/howto/unicode.html)

* I used this [online ASCII art generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) for the very basic text and artwork in the game.

* A series of YouTube tutorials by [Knowledge Mavens](https://www.youtube.com/c/KnowledgeMavens1/search?query=python%20battleships) were very helpful in helping me gain an understanding of the logic and necessary code to develop the project. The code to display the board is based on one of his tutorials. I also used his code to convert the column numbers to letters. However, this project is class-based and has been developed with many more features.

* I also found a YouTube video by [Arjan Codes](https://www.youtube.com/watch?v=u3yo-TjeIDg) to be helpful when it came to understanding the use of classes in the Battleships game. This video gave me the idea to store the board tile values as global variables.

* Course material on the CodeCademy website which helped reinforce my understanding of Python.


### **Honourable mentions**
* Thank you to my mentor, Richard Wells, who gave a significant amount of his time to provide me with help, feedback and ideas on the project; he has been invaluable in so many ways and a genuine source of motivation for me.
* Thanks to the Code Institute team for providing me with some basic knowledge of Python.
* Thanks to the Code Institute community on Slack who helped remind me that everyone has difficult days.
* A huge thank you to my family who support my coding journey on a daily basis.
