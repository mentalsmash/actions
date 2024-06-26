###############################################################################
# Copyright 2020-2024 Andrea Sorbini
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################
import subprocess
from pathlib import Path

from cli_helper.log import log

def config_user(clone_dir: Path, user: tuple[str, str], config_global: bool=False) -> None:
  user_name, user_email = user
  cmd = [
    "git", "config", *(["--global"] if config_global else []), "user.name", user_name
  ]
  log.command(cmd)
  subprocess.run(cmd, check=True, cwd=clone_dir)
  cmd = [
    "git", "config", *(["--global"] if config_global else []), "user.email", user_email
  ]
  log.command(cmd)
  subprocess.run(cmd, check=True, cwd=clone_dir)

