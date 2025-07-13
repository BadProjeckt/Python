#%% Import libraries
#Import libraries
import random
import pandas as pd

#%% Get the project file
#Get the project file
path = 'C:/Users/Nick/Desktop/Python/random_task_picker/lists'
project_ideas = pd.read_csv(f'{path}project_ideas.csv')
project_completed = pd.read_csv(f'{path}project_completed.csv')

#%% Pick a random project
#Pick a random project
r = random.choice(project_ideas)
print(f'Working on: {r}')
#%% Check if the project is completed
#Check if the project is completed
print(f'Did you complete {r}?')
answer = input('Type "yes/y" or "no/n" (not case sensitive)\n')

if str.lower(answer) == 'yes' or str.lower(answer) == 'y':
    project_ideas.remove(r)
    project_completed.append(r)
    print(f'Great! You completed\n"{r}"')
    project_ideas.to_csv('project_ideas.csv', index=False)
    project_completed.to_csv('project_completed.csv', index=False)
    print(f'You have {len(project_ideas)} projects left to complete')

elif str.lower(answer) == 'no' or str.lower(answer) == 'n':
    print(f'Ok, let\'s continue tomorrow')

else:
    print(f'Invalid input')