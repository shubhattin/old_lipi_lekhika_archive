import os, sys

try:
    import shubhlipi as sh
except:
    cm = [
        r"{0}\python -m pip install --upgrade pip".format(
            os.path.dirname(sys.executable)
        ),
        "pip install shubhlipi",
    ]
    for x in cm:
        os.system(x)
    exit()

pkg = {
    "lekhika": ["keyboard", "mouse", "winregistry", "pillow", "pystray"],
    "sarve": [
        "black",  # Python Beutifier
        "pyaml",  # .yaml file management
        "wheel",
        "deta",
        "toml",
        "flask",
        "fastapi",
        "twine",  # upload pip package
        "uvicorn[standard]",  # Server ASGI
        "GitPython",
        "python-dotenv",  # .env file parsing
        "autopep8",  # Python Beutifier
        "openpyxl",  # Managing Excel files
        "pywin32",
        "pyperclip",  # Clipboard copy and paste
        "requests",
        "markdown",  # Markdown to HTML
        "markdownify",  # HTML to Markdown
        "Pygments",  # Code Highlighting
        "brotlipy",  # decodng 'br' based responses
        "virtualenv",  # Virtual Environment manages
        "bcrypt",  # Encryption Algorithm
        "croytography",  # Encrypting and Decrypting text
        "python-multipart",  # Form Parser in FastAPI
        "python-jose[cryptography]",  # JWT Handler
        "datamodel_code_generator",  # Type Server
        # CLI tools
        "typer[all]",
        "rich",
        "rich-cli",
    ],
    "exe": ["https://github.com/pyinstaller/pyinstaller/tarball/develop"],
}
cmd = {
    "sarve": [
        "pywin32_postinstall.py -instal",  # To setup pywin32
        "npm install -g terser",  # JS minifier installation
        "npm install -g serve",  # Serve static assets locally for testing
        "npm install -g tslib prettier json-to-typing",  # type script json iteface generator
    ]
}
if __name__ == "__main__":
    if sh.args(0) == "virtual":
        py_path = sh.home() + r"\AppData\Local\Programs\Python\Python38-32\python.exe"
        root = sh.env("sthAnam") + r"\saGgaNakAnuprayogaH"
        cm = [f"cd {root}", f"virtualenv py_env -p {py_path}"]
        if os.path.isdir(root + r"\py_env"):
            sh.delete_folder(root + r"\py_env")
        sh.cmd("\n".join(cm), False)
        exit()
    for x in sh.argv:
        if x in pkg:
            for c in pkg[x]:
                sh.cmd(f"pip install {c}", False)
        if x in cmd:
            for c in cmd[x]:
                sh.cmd(c, False)
