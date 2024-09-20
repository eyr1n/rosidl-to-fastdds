import subprocess
import tempfile
from argparse import ArgumentParser
from pathlib import Path

from catkin_pkg.package import parse_package
from rosidl_adapter.msg import convert_msg_to_idl


def rosidl_to_omgidl(input_file: Path, output_dir: Path):
    input_file = input_file.resolve()
    output_dir = output_dir.resolve()
    package_dir = input_file.parents[1]
    package = parse_package(package_dir)
    convert_msg_to_idl(
        package_dir,
        package.name,
        input_file.relative_to(package_dir),
        output_dir / input_file.parent.relative_to(input_file.parents[2]),
    )


def omgidl_to_fastdds(input_dir: Path, output_dir: Path):
    input_dir = input_dir.resolve()
    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    for input_file in input_dir.glob("**/*.idl"):
        subprocess.run(
            [
                "/rosidl-to-fastdds/Fast-DDS-Gen/scripts/fastddsgen",
                "-typeros2",
                "-I",
                input_dir,
                "-d",
                output_dir,
                "-cs",
                input_file,
            ],
            cwd=input_dir,
        )


parser = ArgumentParser()
parser.add_argument(".msg", nargs="+")
parser.add_argument("-o", "--outdir", required=True)
args = parser.parse_args()

with tempfile.TemporaryDirectory() as tmp_dir:
    for msg_file in getattr(args, ".msg"):
        rosidl_to_omgidl(Path(msg_file), Path(tmp_dir))
    omgidl_to_fastdds(Path(tmp_dir), Path(args.outdir))
