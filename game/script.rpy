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

    "A delicacy unique to our town, custom made by Grandpa. Of course, only made from the town’s prized fish."

    g "Eat up."

    menu: 
        "Take a bite":
            "Delicious. A slightly chewy texture, but still tender and flavorful."

    scene empty plate

    g "I have something for you,"
    "Your father left it behind for you"

    mc "...Father?"

    g "Yes. I know he left when you were young, and I know it’s been a while, but rest assured, this is for you."

    "Grandpa slides a box over. It’s small and quite thin. A frail, feeble box. It’s years old. Maybe even decades. It’s dusty."

    g "It’s yours now. Keep it safe."

    $ player_name = renpy.input("Scrawled across the top is, 'To my dearest child,'")

    $ player_name = player_name.strip()
    # The .strip() instruction removes any extra spaces the player 
    # may have typed by accident.

    #  If the player can't be bothered to choose a name, then we
    #  choose a suitable one for them:
    if player_name == "":
        $ player_name="Greta"

# And get a nostalgic sigh from Seasons of Sakura fans!
    
# Now the other characters in the game can greet the player.
  
    "Scrawled across the top is, 'To my dearest child, $(mc)'"



    # This ends the game.

    return
