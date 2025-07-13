#%% Import libraries
#Import libraries
import random
import pandas as pd

#%% Get the project file
#Get the project file
path = 'C:/Users/Nick/Desktop/Python/random_task_picker/lists/'
project_ideas = pd.read_csv(f'{path}project_ideas.csv')
project_completed = pd.read_csv(f'{path}project_completed.csv')

#%% Check if there are any ideas left
#Check if there are any ideas left
if project_ideas.empty:
    raise SystemExit("No ideas left. Add some to project_ideas.csv first.")

#%% Pick a random project
#Pick a random project
r = random.choice(project_ideas['idea'])
print(f'Working on: {r}')
started_on = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'Started on: {started_on}')

#%% Check if the project is completed
#Check if the project is completed
print(f'Did you complete {r}?')
answer = input('Type "yes/y" or "no/n" (not case sensitive)\n').strip().lower()

if answer in {'yes', 'y'}:
    data = {
        'idea': r,
        'can_be_used_in_work': input('Can it be used in work? (yes/no)\n').strip().lower() in {'yes', 'y', 'no', 'n'},
        'difficulty': int(input('1-10, where 1 is easy and 10 is hard\n')),
        'tags': input('Enter tags separated by commas\n').strip(),
        'description': input('Short description of the project\n'),
        'started_on': started_on,
        'completed_on': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    project_ideas = project_ideas[project_ideas['idea'] != r]
    project_completed = pd.concat([project_completed, pd.DataFrame([data])], ignore_index=True)

    print(f'Great! You completed\n"{r}"')

    project_ideas.to_csv(f'{path}project_ideas.csv', index=False)
    project_completed.to_csv(f'{path}project_completed.csv', index=False)
    print(f'You have {len(project_ideas)} projects left to complete')

elif answer == 'no' or answer == 'n':
    print(f'Ok, let\'s continue tomorrow')

else:
    print(f'Invalid input')
# %%
