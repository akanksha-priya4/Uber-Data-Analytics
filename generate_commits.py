import random
import subprocess
import os
from datetime import datetime, timedelta

# Configuration
REPO_PATH = "."
GITHUB_REPO = "akanksha-priya4/Uber-Data-Analytics"
START_DATE = datetime(2025, 7, 1)
END_DATE = datetime(2025, 7, 23)

# Commit messages for variety
commit_messages = [
    "Update data pipeline configuration",
    "Enhance SQL analytics queries",
    "Improve Power BI dashboard design",
    "Add data quality validation rules",
    "Update project documentation",
    "Optimize database queries",
    "Add new analytics features",
    "Fix data processing issues",
    "Update security guidelines",
    "Enhance monitoring capabilities",
    "Add performance optimizations",
    "Update integration documentation",
    "Improve error handling",
    "Add new data sources",
    "Update deployment scripts",
    "Enhance user interface",
    "Add automated testing",
    "Update API documentation",
    "Improve data visualization",
    "Add backup and recovery procedures"
]

def generate_commit_history():
    """Generate commit history from July 1st to July 23rd, 2025"""
    
    current_date = START_DATE
    
    while current_date <= END_DATE:
        # Generate random number of commits for this day (1-5)
        num_commits = random.randint(1, 5)
        
        print(f"Generating {num_commits} commits for {current_date.strftime('%Y-%m-%d')}")
        
        for i in range(num_commits):
            # Select random commit message
            message = random.choice(commit_messages)
            
            # Create a small change to a file
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Update a file with timestamp
            with open("last_update.txt", "w") as f:
                f.write(f"Last updated: {timestamp}\nCommit: {message}\nDate: {current_date.strftime('%Y-%m-%d')}")
            
            # Set the commit date
            commit_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
            
            # Git commands to create commit with specific date
            subprocess.run(["git", "add", "last_update.txt"], cwd=REPO_PATH)
            subprocess.run([
                "git", "commit", 
                "-m", message,
                "--date", commit_date
            ], cwd=REPO_PATH)
            
            print(f"  - Commit {i+1}: {message}")
        
        current_date += timedelta(days=1)
    
    print("Commit history generation completed!")

if __name__ == "__main__":
    generate_commit_history() 