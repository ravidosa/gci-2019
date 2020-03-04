# Galaxy Pong for Liquid Galaxy

## Introduction

Galaxy Pong is a game that can be run on the Liquid Galaxy (or any setup with multiple computers).
The Liquid Galaxy screens are used to display the gameplay area where the balls and paddle move around, and phones or arrow keys can be used as controllers for the paddles.

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
http://MACHINEIP:8112/controller/index.html
```

and this url to check the screen:
```url
http://MACHINEIP:8112/
```

The controller should show a screen with the name of the team and a box with a black rectangle in the middle, as well as pause button on the bottom, and the screen should show a black background with paddles, a ball, the score, and a start dialog. The team name at the top of the screen corresponds to the side being played for. If either does not render correctly, reload the page until it does.

When opening the screen on multiple machines, make sure to open them in the order that they are placed from left to right so that the screens viewsync.

The controller uses the phone accelerometer to move the paddle, but for single-player mode arrow keys can be used instead.

### Scripts

If you are on a fully installed Liquid galaxy system running Ubuntu, the files in /Bash and the project directory can be used for the following purposes.

 - install.sh: install and start Galaxy Pong
 - kill-pong.sh: kill Galaxy Pong if it is running (in /Bash)
 - open-pong.sh: open Galaxy Pong (in /Bash)

## Customizing the Game

The files to be modified, Game.js and controller.js are found in the project directory and /Public/controller respectively. Try changing the background or the ball!
