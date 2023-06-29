from pathlib import Path
from datetime import datetime
import shutil
import sys
import re

# Globals
TARGET_DIR = ''
LOG_FILE_NAME = 'sort.log'
SEPARATOR_SYMBOL = '_'

# Supported file extension by sorted by type
EXT_BY_TYPE = {
    'videos': ('MP4', 'AVI', 'MKV', 'MOV', 'WMV', 'FLV', 'WEBM', 'MPEG', 'MPG', '3GP'),
    'pictures': ('JPG', 'JPEG', 'PNG', 'GIF', 'BMP', 'SVG', 'WEBP', 'TIF', 'TIFF', 'ICO'),
    'documents': ('DOC', 'DOCX', 'PDF', 'RTF', 'ODT', 'ODS', 'ODP', 'PPT', 'PPTX', 'XLS', 'XLSX', 'CSV', 'XML', 'HTML', 'HTM', 'TEX'),
    'music': ('MP3', 'WAV', 'WMA', 'OGG', 'FLAC', 'AAC', 'AMR', 'M4A', 'M3U', 'MID'),
    'archives':  ('ZIP', '7Z', 'TAR', 'GZ', 'BZ2', 'XZ', 'TGZ', 'TBZ2'),
    'notes': ('', 'MD', 'TXT'),
    'iso-img': ('ISO', 'IMG'),
}

# Transliteraton dictionary
TRANS = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'y', 'й': 'i', 'к': 'k',
    'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts',
    'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya', 'є': 'ye', 'і': 'i', 'ї': 'ji', 'ґ': 'g',
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'Y', 'Й': 'I', 'К': 'K',
    'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts',
    'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya', 'Є': 'Ye', 'І': 'I', 'Ї': 'Ji', 'Ґ': 'G'
}

# Runtime data storage
RUNTIME_DATA = {
    'files_found': [],
    'files_found_by_type': {},
    'extensions_found': {'known': set(), 'unknown': set()},
    'total_files_found': 0,
    'total_directories_removed': 0,
    'time_started': '',
    'time_finished': ''
}

def create_log() -> None:
    '''Create a log file with the current timestamp and target directory information.'''
    with LOG_FILE_PATH.open('w') as file:
        file.write(f"{get_time()}\nSorting files in: {TARGET_DIR}\n")
        file.write(f"#------------------------\n")
    if not LOG_FILE_PATH.exists():
        print(f'[-] Error. Failed to create sort.log at "{LOG_FILE_PATH}"')

def dir_scan(TARGET_DIR: Path) -> list:
    '''Recursively scan the target directory to find all directories.'''
    path = Path(TARGET_DIR)
    directories = []
    for item in path.iterdir():
        if item.is_dir():
            directories.append(item)
            directories.extend(dir_scan(item))
    return directories

def file_scan(TARGET_DIR: Path) -> list:
    '''Recursively scan the target directory to find all files.'''
    path = Path(TARGET_DIR)
    files = []
    for item in path.iterdir():
        if item.name == LOG_FILE_NAME:
            continue
        if item.is_file():
            files.append(item)
        elif item.is_dir():
            files.extend(file_scan(item))
    RUNTIME_DATA["files_found"] = files
    RUNTIME_DATA["total_files_found"] = len(files)
    return files

def normalize(name: str) -> str:
    '''Filename transformations'''
    file_name, file_ext = Path(name).stem, Path(name).suffix              # Split the filename and extension
    normalized_name = re.sub(r'[^\w\s.-]', '', file_name)                 # Remove invalid characters
    normalized_name = normalized_name.translate(TRANS)                    # Replace Cyrillic symbols with Latin symbols
    normalized_name = re.sub(r' +', SEPARATOR_SYMBOL, normalized_name)    # Replace multiple consecutive spaces with the custom separator
    normalized_name = re.sub(r'[_-]+', SEPARATOR_SYMBOL, normalized_name) # Replace multiple consecutive separators with the custom separator
    normalized_name = normalized_name.strip(SEPARATOR_SYMBOL)             # Remove leading and trailing separators
    normalized_filename = f"{normalized_name}{file_ext}"                  # Concatenate the normalized name and file extension
    return normalized_filename                                            # Preserve original letter case

def rename_duplicates(path: Path) -> Path:
    '''Rename files from the target directory, taking into account existing filename duplicates in the destination folder.'''
    name_stem = path.stem
    file_number = 1
    while path.exists():
        new_destination = path.with_stem(f"{name_stem}{SEPARATOR_SYMBOL}{file_number}")
        file_number += 1
        path = new_destination
    return path

def extension_sort(files: list) -> None:
    '''Sort files into categories based on their extensions.'''
    categories = list(EXT_BY_TYPE.keys())
    categories.append("other")
    extensions_found = RUNTIME_DATA["extensions_found"]
    files_found_by_type = RUNTIME_DATA["files_found_by_type"]
    for file in files:
        if file.parts[1] in categories:
            continue
        ext = file.suffix.lstrip(".").upper()
        is_found = False
        for category, extensions in EXT_BY_TYPE.items():
            if ext in extensions:
                extensions_found["known"].add(ext)
                file_list = files_found_by_type.get(category, [])
                file_list.append(file)
                files_found_by_type[category] = file_list
                is_found = True
                break
        if not is_found:
            extensions_found["unknown"].add(ext)
            category = "other"
            file_list = files_found_by_type.get(category, [])
            file_list.append(file)
            files_found_by_type[category] = file_list

def move_files(TARGET_DIR: Path ) -> None:
    '''Move files into the categorized directories based on their extensions.'''
    found_files_by_type = RUNTIME_DATA["files_found_by_type"]

    for file_type, files in found_files_by_type.items():
        destination_path = Path(TARGET_DIR).joinpath(file_type)
        if not destination_path.exists():
            destination_path.mkdir()
        for file in files:
            original_path = file
            new_file_path = destination_path.joinpath(normalize(file.name))
            if file_type == "archive":
                new_file_path = rename_duplicates(new_file_path)
                archive = file.rename(new_file_path)
                extraction_dir = destination_path.joinpath(new_file_path.stem)
                if not extraction_dir.exists():
                    extraction_dir.mkdir()
                try:
                    shutil.unpack_archive(archive, extraction_dir)
                except Exception as e:
                    print(f'[!] Warning: Failed to unpack "{archive.name}": {e}')
                else:
                    archive.unlink()
            else:
                try:
                    new_file_path = rename_duplicates(new_file_path)
                    file.rename(new_file_path)
                    with open(LOG_FILE_PATH, "a") as file:
                       file.write(f"Original: {original_path}\n")
                       file.write(f"Renamed : {new_file_path}\n")
                       file.write(f"#------------------------\n")
                except Exception as e:
                    print(f'[-] Error: Failed to move "{new_file_path}": {e}')

def purge_empty(source_TARGET_DIR: TARGET_DIR) -> None:
    '''Remove empty directories in the target directory.'''
    TARGET_DIR_list = dir_scan(source_TARGET_DIR)
    TARGET_DIR_list.reverse()
    total_dirs_removed = 0

    for TARGET_DIR in TARGET_DIR_list:
        if TARGET_DIR.exists() and TARGET_DIR.is_dir and not any(TARGET_DIR.glob("*")):
            try:
                TARGET_DIR.rmdir()
                total_dirs_removed += 1
            except Exception as e:
                print(f'[-] Error: Failed to remove directory "{TARGET_DIR}". {e}')
    RUNTIME_DATA["total_directories_removed"] = total_dirs_removed

def get_time() -> str:
    '''Get the current time as a formatted string.'''
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %Hh%Mm%Ss")
    return formatted_datetime

def process_stats() -> None:
    '''Log and display useful runtime stats.'''
    with LOG_FILE_PATH.open('a') as file:
        file.write(f"Files count   -> {RUNTIME_DATA['total_files_found']}\n")
        file.write(f"Dirs sorted   -> {RUNTIME_DATA['total_directories_removed']}\n")
        file.write(f"Started       -> {RUNTIME_DATA['time_started']}\n")
        file.write(f"Finished      -> {RUNTIME_DATA['time_finished']}\n")

    print(f"Files count   -> {RUNTIME_DATA['total_files_found']}")
    print(f"Dirs sorted   -> {RUNTIME_DATA['total_directories_removed']}")
    print(f"Started       -> {RUNTIME_DATA['time_started']}")
    print(f"Finished      -> {RUNTIME_DATA['time_finished']}")
    print("[+] Success: All operations competed!")

def main():
    """Main execution flow."""
    global TARGET_DIR, LOG_FILE_PATH
    RUNTIME_DATA["time_started"] = get_time()
    LOG_FILE_PATH = Path(TARGET_DIR).joinpath(LOG_FILE_NAME)
    create_log()
    file_scan(TARGET_DIR)
    dir_scan(TARGET_DIR)
    extension_sort(RUNTIME_DATA["files_found"])
    move_files(Path(TARGET_DIR))
    purge_empty(Path(TARGET_DIR))
    RUNTIME_DATA["time_finished"] = get_time()
    process_stats()

if __name__ == "__main__":
    '''Entry point of the program. Contains pre-execution checks for validity of the input.'''
    # Get TARGET_DIR via user input, check if target dir exists
    if len(sys.argv) == 2:
        TARGET_DIR = sys.argv[1]
        if not Path(TARGET_DIR).exists():
            print(f'[-] Error. TARGET_DIR does not exist: "{TARGET_DIR}"')
            exit(1)
    # Get TARGET_DIR via user input if no argument was provided, check if target dir exists
    elif len(sys.argv) < 2:
        print("[-] Error. TARGET_DIR not provided\n\nUSAGE: sort.py TARGET_DIR/\n\nEXAMPLE: sort.py /home/user1/Desktop/Unsorted\n")
        TARGET_DIR = input("Enter target folder TARGET_DIR: ")
        if TARGET_DIR == '' :
            exit(1);
        elif not Path(TARGET_DIR).exists():
             print(f'\n[-] Error. TARGET_DIR does not exist: "{TARGET_DIR}"')
             exit(1)
    # Print error message is too many arguments were provided
    else:
        print("[-] Error. Invalid input\n\nUSAGE: sort.py TARGET_DIR/\n\nEXAMPLE: sort.py /home/user1/Desktop/Unsorted\n")
        exit(1)
    main()
