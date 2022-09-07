import subprocess

subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-am", message])
subprocess.call(["git", "push", "origin", branch])