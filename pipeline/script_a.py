import pathlib

base_dir = pathlib.Path("./from_script_a")
base_dir.mkdir(parents=True, exist_ok=True)
this_path = base_dir / "file_a.txt"

with this_path.open("w", encoding="utf-8") as outfile:
    outfile.write("This is produced by script A.")