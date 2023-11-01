name = "dwpicker"

# NOTE: Their Github tag uses "-" (dash) but we cannot use dash here.
version = "0.6.5.2023.06.08.sse.1.0.0"

authors = [
    "Lionel Brouyère",
    "Olivier Evers",
]

description = """Maya animation Picker."""

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
    "maya",
]

private_build_requires = [
]

variants = [
]

build_command = "rez python {root}/rez_build.py"
uuid = "repository.dwpicker"


def commands():
    # -----------------------------------------------
    # Get versions
    # -----------------------------------------------
    # NOTE: REZ package versions can have ".sse." to separate the external
    # version from the internal modification version.
    split_versions = str(version).split(".sse.")
    external_version = split_versions[0]
    internal_version = None
    if len(split_versions) == 2:
        internal_version = split_versions[1]
    # -----------------------------------------------

    env.REZ_DWPICKER_ROOT = "{root}"
    env.PYTHONPATH.append("{root}")

    env.MAYA_PLUG_IN_PATH.append("{root}")
    env.MAYA_SCRIPT_PATH.append("{root}")


def post_commands():
    pass
