# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
from . import config

FuncTorchConfig = type(config)
__all__ = ['config', 'FunctorchConfig']
