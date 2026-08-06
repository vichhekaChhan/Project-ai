import subprocess
import sys
import os

def run_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, shell=True, capture_output=True)
        if result.stdout:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        if e.stderr:
            print(e.stderr)
        else:
            print(e)

def git_status():
    print("\n--- Git Status ---")
    run_command("git status")

def git_add():
    print("\n--- Git Add ---")
    files = input("Enter files to add (or '.' for all): ")
    run_command(f"git add {files}")
    print("Files added.")

def git_commit():
    print("\n--- Git Commit ---")
    message = input("Enter commit message: ")
    run_command(f'git commit -m "{message}"')

def git_push():
    print("\n--- Git Push ---")
    branch = input("Enter branch name (default 'main'): ")
    if not branch.strip():
        branch = "main"
    run_command(f"git push origin {branch}")

def git_pull():
    print("\n--- Git Pull ---")
    branch = input("Enter branch name (default 'main'): ")
    if not branch.strip():
        branch = "main"
    run_command(f"git pull origin {branch}")

def main():
    if not os.path.isdir(".git"):
        print("Error: This is not a git repository. Please run this script inside a git repository.")
        return

    while True:
        print("\n=== Git Helper Menu ===")
        print("1. Status")
        print("2. Add files")
        print("3. Commit")
        print("4. Push")
        print("5. Pull")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            git_status()
        elif choice == '2':
            git_add()
        elif choice == '3':
            git_commit()
        elif choice == '4':
            git_push()
        elif choice == '5':
            git_pull()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
