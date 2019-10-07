# Copyright 2019, the MIDOSS project contributors, The University of British Columbia,
# and Dalhousie University.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""wwatch3_cmd - WaveWatch III® Command Processor
"""
import setuptools


setuptools.setup(
    entry_points={
        # The wwatch3 command:
        "console_scripts": ["wwatch3 = wwatch3_cmd.main:main"],
        # Sub-command plug-ins:
        "wwatch3.app": ["run = wwatch3_cmd.run:Run"],
    }
)
