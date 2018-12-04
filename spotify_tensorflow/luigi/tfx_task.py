# -*- coding: utf-8 -*-
#
# Copyright 2017 Spotify AB.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import sys
from abc import abstractmethod
from typing import List  # noqa: F401

import luigi
from spotify_tensorflow.luigi.beam_base import BeamBaseTask

logger = logging.getLogger("luigi-interface")



class TFTransformJob(BeamBaseTask):
    """tf.transform base luigi task"""
    requirements_file = luigi.Parameter(description="Requirements file for Dataflow Beam job")

    def __init__(self, *args, **kwargs):
        super(TFTransformJob, self).__init__(*args, **kwargs)

    def get_user_args(self):  # type: () -> List[str]
        """Custom user command line arguments - override to provide"""
        return []

    @abstractmethod
    def get_schema_file(self):  # type: () -> str
        """Should return fully qualified path to the schema file."""
        pass

    def extra_cmd_line_args(self):
        cmd_line = ["--schema_file=%s" % self.get_schema_file()]
        cmd_line.append("--requirements_file=%s" % self.requirements_file)
        cmd_line.extend(self.get_user_args())
        return cmd_line
