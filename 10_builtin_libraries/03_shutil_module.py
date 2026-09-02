import shutil
from pathlib import Path

source_directory = Path("shutil_source")
backup_directory = Path("shutil_backup")
source_directory.mkdir(exist_ok=True)

source_file = source_directory / "report.txt"
source_file.write_text("Quarterly report\nRevenue: 250000", encoding="utf-8")

# copy() copies content and permission information
copied_file = shutil.copy(source_file, source_directory / "report_copy.txt")
print("copy() created:", copied_file)

# copy2() also attempts to preserve file metadata
metadata_copy = shutil.copy2(source_file, source_directory / "report_metadata.txt")
print("copy2() created:", metadata_copy)

# copyfile() copies only file content
content_copy = source_directory / "report_content.txt"
shutil.copyfile(source_file, content_copy)
print("copyfile() content:", content_copy.read_text(encoding="utf-8"))

# copytree() copies a complete directory tree
if backup_directory.exists():
    shutil.rmtree(backup_directory)
shutil.copytree(source_directory, backup_directory)
print("copytree() files:", [path.name for path in backup_directory.iterdir()])

# move() moves or renames a file
moved_file = shutil.move(str(content_copy), str(source_directory / "moved_report.txt"))
print("move() destination:", moved_file)

# Disk usage information
usage = shutil.disk_usage(".")
print("Disk total:", usage.total)
print("Disk used:", usage.used)
print("Disk free:", usage.free)

# Locate an executable available through PATH
print("Python executable found at:", shutil.which("python3") or shutil.which("python"))

# Create and unpack an archive
archive_name = shutil.make_archive("reports_archive", "zip", source_directory)
print("Archive created:", archive_name)
unpack_directory = Path("unpacked_reports")
if unpack_directory.exists():
    shutil.rmtree(unpack_directory)
shutil.unpack_archive(archive_name, unpack_directory)
print("Archive unpacked into:", unpack_directory)

# Cleanup demonstration files
shutil.rmtree(source_directory)
shutil.rmtree(backup_directory)
shutil.rmtree(unpack_directory)
Path(archive_name).unlink()
print("Cleanup completed")
