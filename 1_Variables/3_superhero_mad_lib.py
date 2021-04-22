# A fun game of Mad Libs!

# This makes a line to separate the prompts and answers
separator = "#---------------#\n\n"


#  The separator gets used at the start of each prompt to draw the lines
#               |    V    |
store = input(f"{separator}Name a store\n>>> ").capitalize()

#                                We can also manipulate the answers so they fit the story,
#                                       with functions like capitalize() or lower()
#                                                       |     V     |
adjective = input(f"{separator}Give an adjective\n>>> ").capitalize()

thing = input(f"{separator}Name a thing\n>>> ").lower()

#                                    Backslashes (\) are used to make 'escape characters'
#                                              \n means 'start a new line'
#                                                         |V|
plural_things = input(f"{separator}Name something (plural)\n>>> ")

thing_name = input(f"{separator}Name a thing\n>>> ").capitalize()

verb = input(f"{separator}Name a verb\n>>> ")

adverb = input(f"{separator}Name an adverb\n>>> ")

# each answer is stored in a variable so we can use it again later
# | V |
animal = input(f"{separator}Name an animal\n>>> ")

things_rope = input(f"{separator}Name something (plural)\n>>> ")

#             the input() function is how we can ask the user questions
#              |                           V                           |
catch_phrase = input(f"{separator}Say your favorite catchphrase!\n>>> ")


# Here we write the story, leaving certain spots to be filled in with our variables.
super_hero_story = (
    f' People ran from {store}, yelling because a robbery was taking place. The evil\n'
    f' villain Dr.{adjective}{thing} was demanding all the {plural_things} the in the city.\n'
    f' Thankfully, Captain {thing_name} flew in just in time. He knocked the ray gun\n'
    f' out of the villain\'s hand then made him {verb} {adverb}. Next he did his\n'
    f' one-of-a-kind {animal} punch and knocked the villain to the ground. After tying\n'
    f' him up with {things_rope} and handing him over to the police, Captain {thing_name}\n'
    f' said "{catch_phrase}" before flying off again! What an amazing guy!'
)

print(super_hero_story)
