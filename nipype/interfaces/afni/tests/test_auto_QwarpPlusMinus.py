# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import QwarpPlusMinus


def test_QwarpPlusMinus_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        base_file=dict(
            argstr='-base %s',
            copyfile=False,
            mandatory=True,
        ),
        blur=dict(argstr='-blur %s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        minpatch=dict(argstr='-minpatch %d', ),
        nopadWARP=dict(argstr='-nopadWARP', ),
        noweight=dict(argstr='-noweight', ),
        pblur=dict(argstr='-pblur %s', ),
        source_file=dict(
            argstr='-source %s',
            copyfile=False,
            mandatory=True,
        ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
    )
    inputs = QwarpPlusMinus.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_QwarpPlusMinus_outputs():
    output_map = dict(
        base_warp=dict(),
        source_warp=dict(),
        warped_base=dict(),
        warped_source=dict(),
    )
    outputs = QwarpPlusMinus.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
