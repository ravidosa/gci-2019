# Galaxy Snake for Liquid Galaxy

## Introduction

Galaxy Snake is a game that can be run on the Liquid Galaxy (or any setup with multiple computers).
The Liquid Galaxy screens are used to display the gameplay area where the snakes move around, and phones can be used as controllers for the snakes.

## Installation

Clone or download the repository into your computer, then get into the folder.


Run the command:

```bash
npm install
```
to install all the dependencies, then start the server:

```js
node index.js
```
**Note:** If the system says that a module is not installed run the following command:

```bash
npm install [name of module]
```

## Run

With MACHINEIP as the IP address of the machine running the server, go to this url to check the controller:

```url
http://MACHINEIP:8114/controller
```

and this url to check the screen:
```url
http://MACHINEIP:8114/screen
```

The controller should show a screen with three buttons (pause, restart, and ready) and arrow keys, and the screen should show a black screen with the number of players. The color at the top of the controller corresponds to the color of the snake controlled. If either does not render correctly, reload the page until it does.

When opening the screen on multiple machines, make sure to open them in the order that they are placed from left to right so that the screens viewsync.

### Scripts

If you are on a fully installed Liquid galaxy system running Ubuntu, the files in /Bash can be used for the following purposes.

 - kill-current.sh: kill the currently running process on Liquid Galaxy
 - kill-snake.sh: kill Galaxy Snake if it is running
 - open-snake.sh: open Galaxy Snake

## Customizing the Game

The files to be modified, Game.js and Controller.js are found in /Public and /Public/controller respectively. Try changing the food or the arrow keys!
