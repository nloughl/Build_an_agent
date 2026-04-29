import os 


def write_file(working_directory, file_path, content):
    try:
        abs_path_wd = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path_wd, file_path))
        valid_path = os.path.commonpath([abs_path_wd, target_file]) == abs_path_wd
        if not valid_path:
            raise ValueError(f'Error: Cannot write "{file_path}" as it is outside the permitted working directory')
        if os.path.isdir(target_file):
            raise ValueError(f'Error: Cannot write to "{file_path}" as it is a directory')
        # ensure parent directories exist
        parent_dir = os.path.dirname(target_file)
        os.makedirs(parent_dir, exist_ok=True)
        # write file
        with open(target_file, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
