import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        abs_path_wd = os.path.abspath(working_directory)
        # print(abs_path_wd)
        target_file = os.path.normpath(os.path.join(abs_path_wd, file_path))
        valid_path = os.path.commonpath([abs_path_wd, target_file]) == abs_path_wd
        if not valid_path:
            raise ValueError(f'Error: Cannot list "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(target_file):
            raise ValueError(f'Error: File not found or is not a regular file: "{file_path}"')

        with open(target_file, 'r') as file:
            content = file.read(MAX_CHARS)
            if file.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f"Error: {e}"
