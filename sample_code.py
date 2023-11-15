# Example vulnerable code with a security flaw (including a potential secret)
import os

def execute_command(command):
    os.system(command)

# Simulated secret (for demonstration purposes, replace this with an actual secret)
api_key = "my_secret_api_key"

input_command = input("Enter a command to execute: ")
execute_command(input_command)

# Using the simulated secret (in a real scenario, avoid hardcoding secrets in code)
print("API Key:", api_key)
