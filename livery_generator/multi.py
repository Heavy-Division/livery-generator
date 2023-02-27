import os
from typing import List
from livery_generator import generate_b78xh_livery


def generate_liveries(src_dir: str) -> None:
    subdirs: List[str] = [os.path.join(src_dir, name) for name in os.listdir(src_dir) if
               os.path.isdir(os.path.join(src_dir, name))]

    for subdir in subdirs:
        generate_b78xh_livery(subdir)

    print(f'Directory "{subdir}" copied and configuration files modified successfully!')
