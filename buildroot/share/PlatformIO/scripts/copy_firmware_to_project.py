#
# copy_firmware_to_project.py
# Copy the built firmware binary from PlatformIO's workspace to the project root.
#
from pathlib import Path
from shutil import copy2

import pioutil

if pioutil.is_pio_build():
    env = pioutil.env

    def copy_firmware(source, target, env):
        firmware = Path(target[0].get_abspath())
        destination = Path(env.subst("$PROJECT_DIR"), "firmware.bin")

        if firmware.resolve() == destination.resolve():
            return

        copy2(firmware, destination)
        print(f"Copied firmware to {destination}")

    env.AddPostAction("$BUILD_DIR/${PROGNAME}.bin", copy_firmware)
