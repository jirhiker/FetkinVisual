# ===============================================================================
# Copyright 2019 ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================
import os
import sys
import yaml


class Config:
    root = None
    output_root = None
    shape = None
    levels = 30
    colormap = 'hot'
    isotherms = [100, 200, 300, 400, 500]
    sample_tag = ''
    figure_size = 10, 4
    combine_temperature_position = True
    combine_temperature_vectors = True
    vector_map = None
    vector_downsample = 1
    vector_color = 'blue'
    vector_every_n = 10
    colormap_min = 0
    colormap_max = 1000
    use_unique_output_root = True

    def __init__(self):
        self.vector_map = {}

    def load(self, path):
        if not os.path.isfile(path):
            print('Invalid configuration file. {} does not exist'.format(path))
            sys.exit(1)

        with open(path, 'r') as rfile:
            yd = yaml.full_load(rfile)

            if 'shape' in yd:
                self.shape = [int(s) for s in yd['shape'].split(',')]

            if 'figure_size' in yd:
                self.figure_size = [float(s) for s in yd['figure_size'].split(',')]

            for attr in ('levels', 'colormap', 'isotherms', 'sample_tag',
                         'combine_temperature_position',
                         'combine_temperature_vectors',
                         'vector_map', 'vector_color',
                         'colormap_min', 'colormap_max', 'vector_every_n',
                         'use_unique_output_root'):
                if attr in yd:
                    setattr(self, attr, yd[attr])

# ============= EOF =============================================
