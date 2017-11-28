# The Breakout Engine

This is primarily intended to allow you to start working within the engine quickly and easily, but will also be useful for the final report.

## Basic Structure
The game is logically divided into screens, with each screen responsible for only its activity. For example, no game code goes into the main menu screen. The *ScreenManager* class is responsible for managing screens.

There are a few modules that are outside of the screens system, and don't contain actual code. These are the *GameConstants*, *Assets*, and *Graphics* modules, all located in the root project folder.

## Non-Screen Modules
#### GameConstants.py
This module contains many constant values. Most, but not all, of these are numbers. You can import a single constant using this syntax: `from GameConstants import CONSTANT_NAME`. However, many modules will need access to multiple constants - if you look at the GameConstants module, you will see there are currently 6 constants related to Bricks. You can import multiple constants like this: `from GameConstants import C1, C2, C3`. However, this gets tedious quickly, so the following shortcut will import all constants: `from GameConstants import *`.

Since this * import will be used throughout the code, we need to make sure that constant names never conflict with the name of a variable another class is using. Thus, they are all in caps (as is normal for constant, unchangeable values in many programming languages including Python), and all names begin with `GC_`. 

As you look at it, you may notice some weird syntax:

`GC_WORLD_WIDTH: int = 1920`

The : is used to specify the type of the variable. Python doesn't require the type of a variable to be explicitly stated when it is created. However, you can still give Python a 'hint' of what type the variable will be using this syntax. This declaration makes absolutely no difference in how the program works. The major benefit to type hinting is that it makes coding easier. Your IDE (Visual Studio [Code]) should be able to use the type hint to improve autocomplete suggestions, but more importantly, it should be able to give you a warning when you mismatch types (e.g. trying to assign a string to a variable that should be an integer). Also, it makes code easier to understand if you ever need to refer to it later on.

For lists and tuples, you will need to do: `from typing import List` or `Tuple`, and then use, for example, `List[int]` or `Tuple[float, str]` when hinting at the type.

A tuple is a list with () instead of []. A tuple is immutable, meaning it can't be changed once created. It's main use is passing around multiple values as a single variable (like a list), and is faster than a list.

#### Assets.py
This contains game assets - images, and perhaps eventually sound/music. Each asset is declared here as a Surface (which is what pyagme uses to store images).To use them, `from Assets import Assets` (this imports the class `Assets` from the file `Assets.py`), and then use `Assets.<name>` to get an asset out of the class.

To add an asset, you will need to add it's name here, and add the code to load it. The li function can reduce typing required. Image names should start with `I_`, and should be organized by the screen on which the image appears (e.g. `I_MAINMENU_BACKGROUND` or `I_GAMESCREEN_BALL`).

#### Graphics.py
This contains the code for graphics abstraction (explained in the GroupMe). Functions to note are `goWindowed()`, `goFullscreen()`, and `swapWindowMode()`, which toggles between windowed and fullscreen.

When drawing, you will need to access the `surface` variable in this module. `import Graphics`, then use `Graphics.surface.blit(...)` to draw image assets onto the screen, or `pygame.draw.rect(Graphics.surface, ...)` to use draw methods from pygame on this surface.

To finish rendering, instead of calling `pygame.display.flip()`, use `Graphics.flip()`.

## Screens
A normal pygame game loop looks like this:
```
while True:
    for e in pygame.event.get():
        # handle event
    
    # do game stuff here
```

Screens keep a game loop for each screen, while cleanly separating the screens from each other.

The Screen class has only two methods: `__init__()` and `update()`. init is used mainly to pass information to a new screen, and update() is basically the game loop,

#### The Screen Manager
*ScreenManager.py* is responsible for managing screens. It gets started from the main project file (C200_Breakout_Team12.py), with a LoadingScreen as its first screen.

Here's the game loop for the breakout engine:
```
while True:
    currentScreen.update()
    wait for the correct time so that the game runs at 60 FPS
```

Thus, the update() method of each screen gets called at 60 ticks per second, as long as it is the active screen. A screen can pass on control to the next screen with the setScreen() method:
```
def setScreen(newScreen: Screen)
    currentScreen = newScreen
```

To call this from within a screen, use `ScreenManager.setScreen(newScreen)`.

##### Removing menial tasks
The Screen implementation takes care of some small things that are universal to all screens in the game. In every screen's update() method, you should call `super().update()`, which calls the base Screen class's update() method, which does these things:

* Quit the game if a pygame.QUIT event is received
* Update the Graphics class when the window is resized
* Clear the screen every frame

Thus, these things shouldn't be done in individual screens.

A note about the pygame event queue does need to be made here. Keys are 'polled' using pygame.key.get_pressed(). I believe the mouse can also be polled similarly. Thus many screens may not have a need to use any pygame events other than pygame.QUIT. All of the screens right now in their current states certainly don't. However, you still need to take care of the pygame event queue. So after calling `super().update()` in each screen's update method, you should call `pygame.event.clear()` to clear (discard) the event queue. Not doing so will result in bad things happening. Obviously, if events do need to be used within a particular screen, don't call `pygame.event.clear()`, instead use the normal `for event in pygame.event.get(): ...`.

#### The Loading Screen
This draws a 'loading' image onto the screen, loads all content, and then immediately passes control to the Main Menu Screen.

When you add an asset, aside from declaring its name in Assets.py (which actually is not necessary, but should be done for code cleanliness and to help out the IDE read your code), you will need to load it here. Normally, images are loaded with `pygame.image.load(path to image)`, which returns a `Surface`. In addition, images should be converted to a mode that allows pygame to render it quickly. The Surface class has a convert() method that does this. However, this will discard any transparency present in the image, so you should instead use the `convert_alpha()` method which preserves this. So the final code would be `pygame.image.load(path).convert_alpha()`.

LoadingScreen provides a helper method to reduce repetitive typing of this. All assets are located in the 'assets' folder and are PNG files, and must be convert_alpha()d. The `li` (load image) method takes in a path and returns the loaded image. You can exclude the assets directory and .png from the path, and `li` also performs `convert_alpha()`.

Thus, instead of writing

`Assets.I_MAINMENU_BACKGROUND = pygame.image.load("assets/mainmenu/background.png").convert_alpha()`,
 
 you can write just
 
 `Assets.I_MAINMENU_BACKGROUND = li("mainmenu/background")` .
 
#### The Main Menu Screen
This draws a background, waits for the user to press a key (`GC_KEY_MAINMENU_BEGIN` defined in game constants), and then switches to a New Game Loader Screen. Improvements will eventually need to be made, but this should suffice for milestone 1.

#### The New Screen Loader Screen
The `GameScreen` is the screen in use when the game is being played. The Game Screen contains three things:

* A GameState, which stores all the things inside the game (the list of bricks, the ball and paddle, etc.)
* A GameRenderer, which takes in a game state and draws it to the screen
* A GameController, which has an update() method that acts upon the game state. This is where all the game logic goes.

The New Screen Loader Screen initializes these three things for level 1, and switches to the Game Screen.

#### The Game Screen

If the GameController is in charge of all the game processing, what does the Game Screen do? It's update method does four things:

* controller.update()
* renderer.render(state)
* check for pauses and switch to the pause screen when this happens
* switch to the between-levels screen if the user beats the current level

Note that the pause screen and between-levels screen haven't been implemented yet. Actually, only the loading, main menu, new game loader, and game screens have been added.

## The Game
This section delves into the current implementation of the actual game (which is split into the state, controller, and renderer classes).

### Game Components
Everything in the game is made up of some basic components:
* PosPoint, PosRect, or PosCircle
* Velocity
* Acceleration
* and the Blittable class

The `PosPoint` class stores two floats, x and y. `PosRect` and `PosCircle` extend `PosPoint`, so they both have an x and y, and they add in a width and height, or a radius. Note that the `PosRect` x and y refer to its top left corner, whereas the `PosCircle` x and y refer to its center. PosRect and PosCircle also have methods to determine whether they collide with one of the other classes (e.g. you can give a `PosRect` a `PosCircle` or vice versa and it will tell you whether they collide). There are no rectangle-rectangle collisions in the game; only rectangle-circle collisions exist.

The `Velocity` class stores two floats, dx and dy. It has an `apply(pos)` method, which takes in a `PosPoint` (and thus also its subclasses of rect and circle), and applies the velocity to the position (add dx/dy to x/y). The `Acceleration` class is the same, with a ddx and ddy, which can be `apply()`ed to a velocity.

The Blittable class almost shouldn't be a class, but is present so that animations can be very easily added in the future. Here's the class:
```
class Blittable:
    image: Surface
    
    def getImage(self, frame: int):
        return self.image

# no, there's no __init__
``` 

The `frame` parameter will be necessary for animations, but right now it's useless, so it's ignored. But you still need to provide a frame parameter when using getImage().

The classes of game objects all extend `Blittable`. Thus, they all have an `image` variable, and this is set in their init methods (take a look at the classes to see what I mean).

The game objects use OOD in the form of inheritance from the Blittable class (they extend Blittable). The other classes, however, are implemented with composition, not inheritance. In other words, the Ball *is* a Blittable, but it *has* a Position, Velocity, and Acceleration. Here's the code:

```
class Ball(Blittable): # this gives Ball an image field, and a getImage method
    pos: PosCircle   # Ball has a position
    velocity: Velocity
    acceleration: Acceleration
    
    def __init__(..., image, ...):
        self.image = image
```

#### Game State
The game state class contains the following:
* a list of `Brick`
* a `Ball`
* a `Paddle`

Take a look at ^ these classes to see what they are, for the most part they're just subclasses of Blittables with a pos/posrect/poscircle and velocity/acceleration as necessary. The Brick class has a score value and HP, and overrides the getImage() method to return a cracked brick picture when it is damaged.

* a list of `Displayable`

Displayable is a subclass of Blittable; it has an image and a position, velocity, acceleration. It is used for graphical effects (for example, when a brick is destroyed, add an image of a falling brick as a Displayable).

* `level` and `score`: integers
* `won`: boolean; whether the level is complete

#### Game Renderer
A very simple class. For each brick/ball/paddle/displayable, draw its `getImage()` at its position.
Should be completely finished, take a look at the code if you want

## Next Steps
The GameController class needs to be implemented.

#### Current Progress
These are the requirements set forth for the first milestone:
1. Display of brick layer at the top of the screen where each brick is an individual object.
2. Player paddle at the bottom of the screen.
3. A ball placed randomly between the bricks and the paddle and given a random initial direction.
4. Detection of when the ball hits a side wall and appropriate change in direction.
5. Detection of when the ball hits the ceiling and indication of a level completed.
6. Detection of when the ball hits the floor and indication of a level failed.
7. Player ability to control the paddle via keyboard or mouse interface.
8. Change in angle of reflection of the ball depending on where it hits the player paddle.
9. Destruction of a brick (removal from the set of bricks and from the display) when hit by the ball

We have to implement #4, 5, 6, 7, 8, 9.

\#1 shold be complete but needs to be tested. The code to render bricks is there, but the NewGameLoaderScreen needs to put a list of bricks into the game state so that they can be drawn.

\#2 should be complete but other tasks need to be completed before this can be tested.

\#3 same status as #2.

#### What to do

\# 7 should be implemented first. Each frame, get the input for left/right buttons (or mouse position, but only if it moved). Then set the paddle's velocity's dx value based on which key is pressed, or 0 if no key is pressed, or change its position directly so it follows the mouse.

The gamecontroller needs to apply() the velocity of the ball and paddle each tick. This will complete #7 and should confirm that #2 and 3 are complete.

The next ones to do are #4, 5, 6. Bouncing off a wall is checking that `ball x < GC_WALL_SIZE` or `ball x > GC_WORLD_WIDTH - GC_WALL_SIZE` and reversing the ball's velocity's x-component (`ball.velocity.dx *= -1`). Ceiling is `ball.y < GC_BALL_RADIUS` and setting gameState.won = True. Floor presents a problem - gameState.won is already False. So there needs to be a change to the code. The `won` variable should be an integer instead of a boolean. 0 is the default, indicates in-progress game. 1 means won, and -1 means lost. A basic `ball.y > GC_WORLD_HEIGHT - GC_BALL_RADIUS` check will complete these three things. 

\#1 should be done next, needs to be implemented in New Game Loader Screen. It doesn't have to be anything fancy like reading in from a file or generating randomly; we can manually enter a list of bricks and test that they render.

Now only #8 and 9 remain.
