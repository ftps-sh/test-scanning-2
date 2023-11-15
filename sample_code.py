# Example vulnerable code with a security flaw
import os

def execute_command(command):
    os.system(command)

input_command = input("Enter a command to execute: ")
execute_command(input_command)

