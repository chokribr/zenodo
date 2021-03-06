# -*- coding: utf-8 -*-
#
# This file is part of Zenodo.
# Copyright (C) 2016 CERN.
#
# Zenodo is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Zenodo is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Zenodo; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Deposit loaders."""

from __future__ import absolute_import, print_function

from zenodo.modules.records.serializers.schemas.json import RecordSchemaJSONV1

from ..validators import legacyjson_validator
from .base import json_loader, marshmallow_dumper, marshmallow_loader
from .schemas.legacyjson import LegacyRecordSchemaV1

# Translators
# ===========
#: Legacy deposit dictionary translator.
legacyjson_v1_translator = marshmallow_dumper(LegacyRecordSchemaV1)
#: JSON v1 deposit translator.
json_v1_translator = marshmallow_loader(RecordSchemaJSONV1)

# Loaders
# =======
#: Legacy deposit JSON record loader.
legacyjson_v1 = json_loader(
    pre_validator=legacyjson_validator,
    translator=legacyjson_v1_translator,
)
#: JSON deposit record loader.
json_v1 = json_loader(translator=json_v1_translator)
