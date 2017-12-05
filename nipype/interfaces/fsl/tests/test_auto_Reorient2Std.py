# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import Reorient2Std


def test_Reorient2Std_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    ),
    out_file=dict(argstr='%s',
    genfile=True,
    hash_files=False,
    ),
    output_type=dict(),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    )
    inputs = Reorient2Std.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Reorient2Std_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Reorient2Std.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
