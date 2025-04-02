#Project 01 Story Theme: "An Adventure in the Jungle" 🌿🦁 -- By Hammad Ahmed

# This is a Mad Libs project where the user will be prompted to enter various words, and then a story will be generated using those words.

# Mad Libs - An Adventure Story

# Taking user inputs
name = input("Enter a name: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")
food = input("Enter a food item: ")
object_ = input("Enter an object: ")

# Creating the story
story = f"""
One day, {name} went to the deep {place} for an adventure. Suddenly, a {adjective} {animal} appeared out of nowhere! 
{name} had no choice but to {verb} as fast as possible. While running, {name} found a big tree and quickly climbed it. 
From the top, {name} saw a hidden treasure filled with gold and jewels! 

After some time, {name} felt hungry and took out a {food} from the {object_}. Eating it, {name} realized how exciting 
and scary this {place} adventure was! {name} decided to return home but promised to come back again for more adventures!
"""

# Printing the generated story
print("\nHere is your adventure story:\n")
print(story)
