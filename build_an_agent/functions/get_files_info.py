import os


def get_files_info(working_directory, directory="."):
    try:
        abs_path_wd = os.path.abspath(working_directory)
        # print(abs_path_wd)
        target_dir = os.path.normpath(os.path.join(abs_path_wd, directory))
        # print(target_dir)
        if not os.path.isdir(target_dir):
            raise ValueError(f'Error: "{directory}" is not a directory')
        valid_path = os.path.commonpath([abs_path_wd, target_dir]) == abs_path_wd
        if not valid_path:
            raise ValueError(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        dir_contents = {}
        for object_name in os.listdir(target_dir):
            f = os.path.join(target_dir, object_name)
            size = os.path.getsize(f)
            if os.path.isdir(f):
                is_dir = "True"
            else:
                is_dir = "False"
            dir_contents[object_name] = (size, is_dir)
    except Exception as e:
        return f"Error: {e}"
    final_res = ""
    for object_name, (size, is_dir) in dir_contents.items():
        final_res += f"- {object_name}: file_size={size} bytes, is_dir={is_dir}\n"
    return final_res


# res = get_files_info("calculator", "pkg")
# print(res)