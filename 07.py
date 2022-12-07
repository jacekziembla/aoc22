with open("07.txt") as f:
    lines = f.read().split("\n")

dir_stack = []
current_dir = "/"
files = {}
folders = []
THRESHOLD = 100000

for line in lines:
    split_line = line.split()
    if line.startswith("$ cd"):
        next_dir = split_line[2]
        if next_dir == "..":
            dir_stack.pop()
            current_dir = "/".join(dir_stack)
        else:
            if next_dir == "/":
                dir_stack.clear()
            dir_stack.append(next_dir)
            current_dir = "/".join(dir_stack)
            folders.append(current_dir.replace("//", "/"))
    elif line.startswith("$ ls"):
        continue
    elif line.startswith("dir"):
        continue
    else:
        size = int(split_line[0])
        name = split_line[1]
        path = f"{current_dir}/{name}".replace("//", "/")
        files[path] = size

folder_sizes = {folder: 0 for folder in folders}
for folder in folders:
    for file_name, file_size in files.items():
        if file_name.startswith(folder):
            folder_sizes[folder] += file_size

# Part A
result = sum([size for size in folder_sizes.values() if size <= THRESHOLD])
print(result)

# Part B
TOTAL_SPACE = 70000000
UNUSED_REQUIREMENT = 30000000

currently_unused = TOTAL_SPACE - folder_sizes["/"]
size_to_delete = UNUSED_REQUIREMENT - currently_unused

potential_candidates = sorted([size for size in folder_sizes.values() if size >= size_to_delete])
print(potential_candidates[0])
