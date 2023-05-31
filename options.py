import keyboard, os


def start_options(title: str, options: list, actions: list):
    global selected_option
    selected_option = 0

    def print_options():
        os.system("cls" if os.name == "nt" else "clear")
        print(title)
        for i, option in enumerate(options):
            if i == selected_option:
                print("->", option)
            else:
                print(" ", option)

    print_options()

    def on_key_press(event):
        global selected_option

        if event.name == "up" and selected_option > 0:
            selected_option -= 1
            print_options()
        elif event.name == "down" and selected_option < len(options) - 1:
            selected_option += 1
            print_options()
        elif event.name == "enter":
            os.system("cls" if os.name == "nt" else "clear")
            actions[selected_option]()

    keyboard.on_press(on_key_press)
    keyboard.wait()
