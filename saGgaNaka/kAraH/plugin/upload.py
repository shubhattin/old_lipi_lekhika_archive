#!/bin/env python3

import shubhlipi as sh
import dotenv

# to use api key set
# TWINE_USERNAME="__twine__"
# TWINE_PASSWORD="<actual token>"

dotenv.load_dotenv()

sh.delete_folder("dist")
sh.cmd("python setup.py sdist")
sh.cmd("twine upload dist/*", direct=False)
