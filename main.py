import options, sys, os, enemy_bot

def hello_start():
    print("Okay, let's start, your oponent pockemons: \n")
    for enemy_pockemon in enemy_bot.enemy_pockemons:
        print(enemy_pockemon)

hello_title = "Welcome to pythomon! \nStart play?"
hello_options = ["Yes", "No"]
hello_actions = [hello_start, lambda: sys.exit()]

options.start_options(hello_title, hello_options, hello_actions)
