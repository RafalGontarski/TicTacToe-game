def check_input(input):
    if input.lower() == "quit":
        raise Exception("Game exited.")