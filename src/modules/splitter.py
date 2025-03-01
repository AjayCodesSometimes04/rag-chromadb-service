from semantic_text_splitter import TextSplitter

def split_file(request):
    with open(request.split_details.source_filepath, "r", encoding="utf-8", errors="ignore") as f:
        file_content = f.read()

    splitter = TextSplitter(request.split_details.max_chars, trim=False)

    documents = splitter.chunks(file_content)

    return documents