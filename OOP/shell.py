import subprocess

# Replace the command with the shell command you want to run
command = "ls -l"

# Run the command and capture the output
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Print the output
print("Output:")
print(result.stdout)

# Print the error, if any
# print("Error:")
# print(result.stderr)

# Print the return code
print("Return Code:", result.returncode)
