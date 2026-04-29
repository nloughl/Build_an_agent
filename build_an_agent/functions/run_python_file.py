import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_path_wd = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path_wd, file_path))
        valid_path = os.path.commonpath([abs_path_wd, target_file]) == abs_path_wd
        if not valid_path:
            raise ValueError(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(target_file):
            raise ValueError(f'Error: "{file_path}" does not exist or is not a regular file')
        if file_path[-3:] != ".py":
            raise ValueError(f'Error: "{file_path}" is not a Python file')
        
        command = ["python", target_file]
        if args:
            command.extend(args)
        process = subprocess.run(command, timeout=30, capture_output=True, text=True, cwd=abs_path_wd)
        output = ""
        if process.returncode != 0:
            output += f"Process exited with code {process.returncode}\n"
        if not process.stdout and not process.stderr:
            output += "No output produced\n"
        else:
            output += f"STDOUT: \n{process.stdout}\n"
            output += f"STDERR: \n{process.stderr}\n"
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"
