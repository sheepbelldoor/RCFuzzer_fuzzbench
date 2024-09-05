import os
import sys
from pathlib import Path
from typing import List, Optional

# FIXME
if not __package__:
    sys.path.append(
        os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    __package__ = "rcfuzz"

from tap import Tap

from . import config as Config
from .mytype import Fuzzer

config = Config.CONFIG


class ArgsParser(Tap):
    input: Path
    output: Path
    fuzzer: List[Fuzzer]
    target: str
    explore: int
    exploit: int
    sync: int
    timeout: str
    empty_seed: bool
    crash_mode: str
    focus_one: Optional[str]
    threshold: int
    tar: bool

    def configure(self):
        global config
        # NOTE: get default value from config, and overwritable from argv
        DEFAULT_SYNC_TIME = config['scheduler']['sync_time']
        DEFAULT_EXPLORE_TIME = config['scheduler']['explore_time']
        DEFAULT_EXPLOIT_TIME = config['scheduler']['exploit_time']
        available_fuzzers = list(config['fuzzer'].keys())
        available_targets = list(config['target'].keys())

        self.add_argument("--input",
                          "-i",
                          help="Optional input (seed) directory",
                          required=False)

        self.add_argument("--output",
                          "-o",
                          help="An output directory",
                          required=True)

        self.add_argument("--fuzzer",
                          "-f",
                          type=str,
                          nargs='+',
                          choices=available_fuzzers + ['all'],
                          required=True,
                          help="baseline fuzzers to include")

        self.add_argument(
            "--target",
            "-t",
            type=str,
            choices=available_targets,
            required=True,  # only one target allowed
            help="target program to fuzz")

        self.add_argument("--explore",
                          type=int,
                          default=DEFAULT_EXPLORE_TIME,
                          help='explore phase time (Time_{explore})')

        self.add_argument("--exploit",
                          type=int,
                          default=DEFAULT_EXPLOIT_TIME,
                          help='exploit phase time (Time_{exploit})')

        self.add_argument("--sync",
                          type=int,
                          default=DEFAULT_SYNC_TIME,
                          help='seed sync interval (used in EnFuzz mode)')

        self.add_argument("--timeout", "-T", default='24h')

        self.add_argument("--empty_seed",
                          "-empty",
                          action="store_true",
                          default=False,
                          help="use empty seed instead")

        self.add_argument("--crash_mode",
                          type=str,
                          choices=['trace', 'ip'],
                          default='ip',
                          help="method to deduplicate bugs.")

        self.add_argument("--focus-one",
                          default=None,
                          help="Used to run a specific individual fuzzer.")

        self.add_argument("--threshold",
                          type=int,
                          default=10,
                          help="difference threshold (theta_{init} in paper)")

        self.add_argument("--tar",
                          action="store_true",
                          default=False,
                          help="tar fuzzer/eval directories")
