import os
import re
import shutil
import time
from datetime import datetime
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

SCREENSHOTS_DIR = Path(r"C:\Users\shlok\Pictures\Screenshots")
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif"}


def get_next_ss_index(dest_dir: Path, date_prefix: str) -> int:
    # Look at what's already in the destination folder for this date
    # and figure out what the next SS number should be
    pattern = re.compile(rf"^{re.escape(date_prefix)}_SS(\d+)\.")
    max_idx = 0

    if dest_dir.exists():
        for existing_file in dest_dir.iterdir():
            if existing_file.is_file():
                match = pattern.match(existing_file.name)
                if match:
                    idx = int(match.group(1))
                    if idx > max_idx:
                        max_idx = idx

    return max_idx + 1


def process_file(file_path: Path):
    # Ignore anything not directly in the root screenshots folder
    if file_path.parent != SCREENSHOTS_DIR:
        return

    if not file_path.is_file() or file_path.suffix.lower() not in IMAGE_EXTENSIONS:
        return

    # Give Windows a moment to finish writing the file before we touch it
    time.sleep(0.5)

    try:
        mtime = os.path.getmtime(file_path)
        dt = datetime.fromtimestamp(mtime)

        year_folder = str(dt.year)
        month_folder = dt.strftime("%m-%B")
        dest_dir = SCREENSHOTS_DIR / year_folder / month_folder
        dest_dir.mkdir(parents=True, exist_ok=True)

        date_prefix = f"{dt.strftime('%B')}{dt.day}"
        next_idx = get_next_ss_index(dest_dir, date_prefix)
        new_filename = f"{date_prefix}_SS{next_idx}{file_path.suffix.lower()}"
        dest_file = dest_dir / new_filename

        shutil.move(str(file_path), str(dest_file))

    except PermissionError:
        # File is probably still locked by Windows, wait and try once more
        time.sleep(1)
        try:
            shutil.move(str(file_path), str(dest_file))
        except Exception:
            pass

    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")


class ScreenshotHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            process_file(Path(event.src_path))


def process_existing_files():
    # Sweep up any screenshots that were already sitting in the folder
    # before the watcher started (e.g. from a previous session)
    if not SCREENSHOTS_DIR.exists():
        return

    image_files = [
        f for f in SCREENSHOTS_DIR.iterdir()
        if f.is_file() and f.suffix.lower() in IMAGE_EXTENSIONS
    ]
    image_files.sort(key=lambda f: os.path.getmtime(f))

    for file_path in image_files:
        process_file(file_path)


if __name__ == "__main__":
    # Handle anything already in the folder before we start watching
    process_existing_files()

    # Now watch the folder and catch new screenshots as they come in
    event_handler = ScreenshotHandler()
    observer = Observer()
    observer.schedule(event_handler, str(SCREENSHOTS_DIR), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
