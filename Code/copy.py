import shutil
from pathlib import Path

src = Path(input("SRC : "))

dst = Path(input("DST : ")) / str(src).replace(':', '')

destination = shutil.copytree(src, dst)

