# Mad Libs is a classic word game that combines creativity, humor, and language learning. Here's a comprehensive explanation:

# Core Concept
# Players fill in blanks in a pre-written story with specific parts of speech (nouns, verbs, adjectives, etc.) without knowing the story's context. When completed, the unexpected combinations often create hilarious, nonsensical results.


# jungle_mad_libs.py

print("\n\U0001F332 Welcome to Jungle Mad Libs! \U0001F333\n")

# Get user inputs with kid-friendly prompts
color = input("What's your favorite color? ")
animal = input("Name a big animal: ")
sound = input("What sound does a monkey make? ")
food = input("Your favorite snack: ")
verb = input("How do you move when happy? (add 'ing' at end): ")
friend = input("Your best friend's name: ")

# Create the story
story = f"""
\U0001F3D6 The {color} Jungle Adventure \U0001F3D6

One sunny day, a giant {animal} heard loud "{sound}" noises! 
It found {friend} {verb} near a {food} tree. They ate 
magic {food} and became jungle heroes! \U0001F389
"""

# Display results
print("\n\U0001F525 Here's your Jungle Story: \U0001F525")
print("▔" * 30)  # Top border
print(story)
print("▁" * 30)  # Bottom border
