from pathlib import Path

FILE_EXTENSIONS = {
    'Images': {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.tiff', '.bmp'},
    'Videos': {'.mp4', '.mov', '.avi', '.mkv', '.flv'},
    'Audios': {'.mp3', '.wav', '.flac', '.m4a', '.aac', '.ogg', '.opus'},
    'Files': {'.txt', '.pdf', '.docx', '.xlsx', '.pptx'},
    'Compressed': {'.zip', '.rar'},
    'Programs': {'.exe'},
    'Programming': {'.py', '.sql', '.json', '.cpp', '.java', '.html', '.css', '.js', '.sql', '.bin'},
    '3D': {'.blend', '.obj', '.fbx', 'stp', 'max', 'x3d', 'vrml', '3ds', '3mf', 'stl', 'dae'}
}

DESTINATION_FOLDERS = {
    'Images': Path.home() / "Downloads" / "Images",
    'Videos': Path.home() / "Downloads" / "Videos",
    'Audios': Path.home() / "Downloads" / "Audios",
    'Files': Path.home() / "Downloads" / "Files",
    'Compressed': Path.home() / "Downloads" / "Compressed",
    'Programs': Path.home() / "Downloads" / "Programs",
    'Programming': Path.home() / "Downloads" / "Programming",
    '3D': Path.home() / "Downloads" / "3D",
    'Folders': Path.home() / "Downloads" / "Folders",
    'Others': Path.home() / "Downloads" / "Others"
}

DOWNLOADS_FOLDER = Path.home() / "Downloads"