
def welcome_user(name, is_returning_user=True):
    """Output greeting with the provived name."""
    if is_returning_user:
        message = f"Welcome back {name}!"
    else:
        message = f"Welcome {name}!"

    print(message)

welcome_user(name="Kuffi")
welcome_user("c: c:", is_returning_user=True)
welcome_user("Ali", False)
