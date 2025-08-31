# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("???")
define g = Character("Grandfather")
define u = Character("Uncle")
define c = Character("Cousin")
define a = Character("Aunt")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy


    mc "Thank you for the meal."

    "A delicacy unique to our town, custom made by Grandfather. Of course, only made from the town’s prized fish."

    g "Eat up."

    menu: 
        "Take a bite":
            "Delicious. A slightly chewy texture, but still tender and flavorful."

    scene empty plate

    g "I have something for you,"
    "Something your father left behind."

    mc "...Father?"

    g "Yes. I know he left this world when you were young, but rest assured, this is for you."

    "Grandfather slides a small, thin box over. It’s years old, maybe even decades, and it’s covered in dust."

    g "It’s yours now. Keep it safe."

    $ player_name = renpy.input("Scrawled across the top in cursive letters are the words: 'To my dearest child,'")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="Greta"
  
    "Scrawled across the top in cursive letters are the words: 'To my dearest child, [mc]..."


    # This ends the game. This ends the game.

    return
