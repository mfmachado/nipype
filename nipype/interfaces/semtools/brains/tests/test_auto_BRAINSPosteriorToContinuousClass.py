# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..classify import BRAINSPosteriorToContinuousClass


def test_BRAINSPosteriorToContinuousClass_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    inputBasalGmVolume=dict(argstr='--inputBasalGmVolume %s',
    ),
    inputCrblGmVolume=dict(argstr='--inputCrblGmVolume %s',
    ),
    inputCrblWmVolume=dict(argstr='--inputCrblWmVolume %s',
    ),
    inputCsfVolume=dict(argstr='--inputCsfVolume %s',
    ),
    inputSurfaceGmVolume=dict(argstr='--inputSurfaceGmVolume %s',
    ),
    inputVbVolume=dict(argstr='--inputVbVolume %s',
    ),
    inputWhiteVolume=dict(argstr='--inputWhiteVolume %s',
    ),
    outputVolume=dict(argstr='--outputVolume %s',
    hash_files=False,
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    )
    inputs = BRAINSPosteriorToContinuousClass.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_BRAINSPosteriorToContinuousClass_outputs():
    output_map = dict(outputVolume=dict(),
    )
    outputs = BRAINSPosteriorToContinuousClass.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
