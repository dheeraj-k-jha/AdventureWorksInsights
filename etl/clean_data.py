from pathlib import Path


def clean_raw_data(input_path: str, output_path: str) -> None:
    input_file = Path(input_path)
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    if input_file.exists():
        output_file.write_text(input_file.read_text())
    else:
        output_file.write_text("")
