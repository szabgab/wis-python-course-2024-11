animales = ['gato', 'perro', 'serpiente']
for animal in animales:
    print(animal)
for i in range(3):
    print(f"{i} {animales[i]}")
for i in range(len(animales)):
    print(f"{i} {animales[i]}")

for i, animal in enumerate(animales):
    print(f"{i} {animal}")

#animal = 'cat'
# while animal not in animales:
#     animal = input('type in the name of an animal: ')


# while True:
#     animal = input('type in the name of an animal: ')
#     if animal in animales:
#         break

# while True:
#     # do something
#     if 2 > 3:
#         break

# while 2 < 3:
#     # do something
#     pass  # placeholder for code that does nothing


# found = False

# while not found:
#     animal = input('type in the name of an animal: ')
#     if animal in animales:
#         found = True

