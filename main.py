import os
import subprocess

# Initialize a new git repository
def init_repo():
    os.system('git init')

# Create a new file and commit it to the repository
def add_commit(file_name, content, message):
    with open(file_name, 'w') as f:
        f.write(content)
    os.system(f'git add {file_name}')
    os.system(f'git commit -m "{message}"')

# Simulate synchronization by pulling changes
def pull_changes():
    os.system('git pull')

# Simulate concurrency by making changes on two branches
def create_branch(branch_name):
    os.system(f'git checkout -b {branch_name}')

def merge_branch(branch_name):
    os.system(f'git checkout main')
    os.system(f'git merge {branch_name}')

# Usage
init_repo()
add_commit('file.txt', 'Initial content', 'Initial commit')
create_branch('feature')
add_commit('file.txt', 'Feature content', 'Feature commit')
merge_branch('feature')
pull_changes()  # Simulates synchronization from a remote repo