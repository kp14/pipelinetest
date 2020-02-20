import pathlib

base_dir = pathlib.Path("./from_script_b")
base_dir.mkdir(parents=True, exist_ok=True)

for i in range(10):
    this_p = base_dir / "file_B_{}.txt".format(i)
    with this_p.open("w", encoding="utf-8") as outfile:
        outfile.write("This is from script B, number {}".format(i))