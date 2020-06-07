# monstergame.dagomara.github.io
 multiplayer, customizable poke-clone featuring cross-platform support (eventually).
## Table of Contents
 * Game
 * Editor
 * Context
 * UsefulBox
 * Update Notes
 * Dev's Scratchpad

# Game
## Structure
    `game.py` is broken up into multiple acts:
      1. initialization, file loading, definitions
        * `monster`, `player` class types
      2. Player making and game
      3. Console

## Classes
    Monstergame uses `player` and `monster` classes. Players store monsters, but monsters may exist on their own.
### players
      * string `.name`
      * list `inv` *(currently unused)*
      * object `monster1`
      * object `monster2`
      * object `monster3`
      * function `showCard()`: prints an ASCII card regarding player info, and information surrounding each owned monster (aka monster1, ...2, ...3).
      * function `help()`: Displays the variable and function names attributed to the default `player` class.

### monsters
      *a lot more here chief!*

## mini-CLI
    Monstergame includes a mini scripting language to assist me with development; it may help you as well and is included in `game.py` so why not explain it, right? Half of it is normal Python, the other half is my own abstraction.
    The "language" is actually just a function which smart-interprets what the user tells it to do in a string. The "language" is run exclusively in `console()`. By default, `console()` is called at the end of the program for debugging purposes. With that being said, you can obviously call the console wherever you want in the code.
### Default CLI Commands
  * `exec `: executes whatever code you write after `exec `.
  * `rbattle init `: generates a random battle between a chosen monster and a fresh monster.
    * Syntax: `rbattle init your_monster enemy_specie,enemy_level`
  * `pbattle init `: Initiates a battle between two already existing monsters.
    * Syntax: `pbattle init your_monster enemy_monster`
    * Note: Technically, this command is the best in the game because you can make your monsters fight each other. Haha
  * `quit`, `exit`, `stop`: If these words are in the beginning of your console command, the console will exit. By default, the console is the last safeguarding line of code in `game.py`, meaning that your program will close without saving once the console is closed.
  * `save `: Saves your stuff. Runs the `save()` function with special file outputs.
    * Syntax: `save "../location/of/save/file.txt"`
    * Special note: including no text after "save " in the mini-CLI will just run the `save()` function for you.
  * `load `: Loads a file. *please remember to write this later*
  * `makequickvar `:
    * Syntax: `makequickvar general|monster full_variable_name new_short_name`
    * Example: `makequickvar monster p1.monster1 Buddy` will make a dictionary entry "Buddy" in `qms` which will point back to `p1.monster1`. you can just refer back to it in commands with `qms["Buddy"]` instead of `p1.monster1`. For many instances, this literally won't be helpful. But for some, it will, which is why it exists.
    * **Note: `makequickvar` is currently broken. And I don't feel like fixing it right now because it's not pertinent.**
### Things Useful in `exec`
  * `xpAdder(m1, m2)`: Performs XP calculations comparing two monsters. `m1` is the one gaining XP.


also:
 attack
 battle


# Editor


# Context
  Context is a neat file because it lets me output to multiple platforms. What I mean by that is that I'm working on four versions of this program that all work together: default CLI, tKinter, web, and PS1. The PlayStation 1 version, however, is definitely the furthest into the future. However, I have already found working models of Python->PS1 online and will be adapting some features to help me out. But don't worry about that.
  This is `context.py`. The file is arranged into different `levelOfDetail` values depending on the current installation of Monstergame. By default (CLI), this value is 1 and is the only one being worked on right now.

  In `game.py`, you may notice many basic outputs are achieved not by `print()` but instead by `out.output()`. This is intentional so that `game.py` may be easily adapted to other levels of detail. Also, `game.py` imports `context.py` as `out`, which is important to remember.
  In fact, `import context as out` is the standard across all Monstergame files.
  * `feed(string question)`: it's input.
  * `output(string stuff)`: it's print.
  * `clearScreen()`: clears the screen. In CLI it just spams newlines. lmfao

# UsefulBox
  While `context.py` serves to provide adaptable output routines, `usefulBox.py` serves to help me with different formatting things across the files of Monstergame (so basically it's another mini-library like context is).
  * `nameFormatter(string)`: Strips a string and capitalizes all words in it.
  * `pause()`: Waits for user input by doing an empty input statement.
  * `stringSolver(int chars, string_to_be_formatted)`: Takes a string and makes it `chars` characters long, and filling the rest of the characters with whitespace if necessary.
  * `nameMaker(string, int length)`: Checks if a user enters a name of valid  `length` and loops until they enter something that works.
      * If you want to see it in action, there is a test string commented out on the bottom of `usefulBox.py`.

# personal note for me to remember what to add later
*new data type for excess monsters that are being stored for later
as well as player saving because damn lol
add a man-esque help command haha*
