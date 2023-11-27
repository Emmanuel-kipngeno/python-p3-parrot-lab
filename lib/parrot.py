def parrot(sound="Squawk!"):
    print(sound)
    return sound

# Example Usage:
default_sound = parrot()  # Output: Squawk!
custom_sound = parrot("Hello, world!")  # Output: Hello, world!

print("Default Sound:", default_sound)
print("Custom Sound:", custom_sound)
