# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..gtract import gtractTensor


def test_gtractTensor_inputs():
    input_map = dict(applyMeasurementFrame=dict(argstr='--applyMeasurementFrame ',
    ),
    args=dict(argstr='%s',
    ),
    b0Index=dict(argstr='--b0Index %d',
    ),
    backgroundSuppressingThreshold=dict(argstr='--backgroundSuppressingThreshold %d',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignoreIndex=dict(argstr='--ignoreIndex %s',
    sep=',',
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    inputVolume=dict(argstr='--inputVolume %s',
    ),
    maskProcessingMode=dict(argstr='--maskProcessingMode %s',
    ),
    maskVolume=dict(argstr='--maskVolume %s',
    ),
    medianFilterSize=dict(argstr='--medianFilterSize %s',
    sep=',',
    ),
    numberOfThreads=dict(argstr='--numberOfThreads %d',
    ),
    outputVolume=dict(argstr='--outputVolume %s',
    hash_files=False,
    ),
    resampleIsotropic=dict(argstr='--resampleIsotropic ',
    ),
    size=dict(argstr='--size %f',
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    )
    inputs = gtractTensor.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_gtractTensor_outputs():
    output_map = dict(outputVolume=dict(),
    )
    outputs = gtractTensor.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
