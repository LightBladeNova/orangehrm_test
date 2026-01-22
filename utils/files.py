from pathlib import Path


def latest_file(path: Path, pattern: str | None = None) -> Path:
    """
    Find the most recently modified file in a directory.
    
    Args:
        path: Directory path to search
        pattern: Optional glob pattern to filter files (e.g., "*.txt", "test_*")
    
    Returns:
        Path to the latest file
    
    Raises:
        FileNotFoundError: If no files match the criteria
    """
    path = Path(path)
    
    if pattern:
        files = list(path.glob(pattern))
    else:
        files = [f for f in path.iterdir() if f.is_file()]
    
    if not files:
        raise FileNotFoundError(f"No files found in {path}" + (f" matching pattern '{pattern}'" if pattern else ""))
    
    return max(files, key=lambda f: f.stat().st_mtime)


def read_text(path: Path, encoding: str = "utf-8") -> str:
    """
    Read text from a file.
    
    Args:
        path: File path to read
        encoding: Text encoding (default: utf-8)
    
    Returns:
        File contents as string
    """
    return Path(path).read_text(encoding=encoding)
