$APPLICATION_ROOT_DIR_PATH = "C:\Users\ajrai\vscode_git_repos\"
$BASE_PATH = "C:\Users\ajrai\logs\rag-chromadb-service"

$PYTHONPATH = Join-Path -Path $APPLICATION_ROOT_DIR_PATH -ChildPath  rag-chromadb-service\src
$PORT = 9090

fastapi run $PYTHONPATH/main/app.py --port $PORT