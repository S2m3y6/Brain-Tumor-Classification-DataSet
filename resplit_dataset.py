import os
import random
import shutil


WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = os.path.join(WORKSPACE_DIR, "Sorted")
DESTINATION_DIR = os.path.join(WORKSPACE_DIR, "Resplit_80_20")

SOURCE_SPLITS = ("Training", "Testing")
VIEWS = {
    "Sagittaal": "sagittaal",
    "Axiaal": "axiaal",
    "Coronaal": "coronaal",
}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tif", ".tiff", ".webp"}


def main():
    if not os.path.isdir(SOURCE_DIR):
        raise FileNotFoundError(f"Bronmap niet gevonden: {SOURCE_DIR}")

    copied_files = 0

    for output_view, source_view in VIEWS.items():
        class_names = set()
        for source_split in SOURCE_SPLITS:
            view_dir = os.path.join(SOURCE_DIR, source_split, source_view)
            if not os.path.isdir(view_dir):
                raise FileNotFoundError(f"Verwachte map niet gevonden: {view_dir}")
            class_names.update(
                name
                for name in os.listdir(view_dir)
                if os.path.isdir(os.path.join(view_dir, name))
            )

        for class_name in sorted(class_names):
            files = []
            for source_split in SOURCE_SPLITS:
                class_dir = os.path.join(
                    SOURCE_DIR, source_split, source_view, class_name
                )
                if not os.path.isdir(class_dir):
                    continue
                for filename in os.listdir(class_dir):
                    source_path = os.path.join(class_dir, filename)
                    if (
                        os.path.isfile(source_path)
                        and os.path.splitext(filename)[1].lower() in IMAGE_EXTENSIONS
                    ):
                        files.append((source_split, source_path))

            random.shuffle(files)
            split_index = int(len(files) * 0.8)
            if len(files) == 1:
                split_index = 1
            elif len(files) > 1:
                split_index = max(1, min(len(files) - 1, split_index))

            split_files = (
                ("Training", files[:split_index]),
                ("Testing", files[split_index:]),
            )
            for output_split, group_files in split_files:
                destination_dir = os.path.join(
                    DESTINATION_DIR, output_split, output_view, class_name
                )
                os.makedirs(destination_dir, exist_ok=True)

                used_names = set()
                for source_split, source_path in group_files:
                    filename = os.path.basename(source_path)
                    destination_name = filename
                    stem, extension = os.path.splitext(filename)
                    if os.path.normcase(destination_name) in used_names:
                        destination_name = f"{source_split}_{stem}{extension}"
                        suffix = 2
                        while os.path.normcase(destination_name) in used_names:
                            destination_name = (
                                f"{source_split}_{stem}_{suffix}{extension}"
                            )
                            suffix += 1

                    used_names.add(os.path.normcase(destination_name))
                    shutil.copy2(
                        source_path, os.path.join(destination_dir, destination_name)
                    )
                    copied_files += 1

            print(
                f"{output_view}/{class_name}: "
                f"{len(split_files[0][1])} Training, {len(split_files[1][1])} Testing"
            )

    print(f"Klaar: {copied_files} afbeeldingen gekopieerd naar {DESTINATION_DIR}")


if __name__ == "__main__":
    main()
