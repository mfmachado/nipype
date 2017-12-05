# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..epi import PrepareFieldmap


def test_PrepareFieldmap_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    delta_TE=dict(argstr='%f',
    mandatory=True,
    position=-2,
    usedefault=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    in_magnitude=dict(argstr='%s',
    mandatory=True,
    position=3,
    ),
    in_phase=dict(argstr='%s',
    mandatory=True,
    position=2,
    ),
    nocheck=dict(argstr='--nocheck',
    position=-1,
    usedefault=True,
    ),
    out_fieldmap=dict(argstr='%s',
    position=4,
    ),
    output_type=dict(),
    scanner=dict(argstr='%s',
    position=1,
    usedefault=True,
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    )
    inputs = PrepareFieldmap.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_PrepareFieldmap_outputs():
    output_map = dict(out_fieldmap=dict(),
    )
    outputs = PrepareFieldmap.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
