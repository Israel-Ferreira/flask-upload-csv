def file_extension_has_allowed(filename: str):
    ALLOWED_EXTENSIONS = "csv"
    extension =  filename.rsplit(".", 1)[1].lower()

    return "." in filename and extension in ALLOWED_EXTENSIONS


