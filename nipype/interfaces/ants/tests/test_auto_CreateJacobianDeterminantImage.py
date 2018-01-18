# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import CreateJacobianDeterminantImage


def test_CreateJacobianDeterminantImage_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        deformationField=dict(
            argstr='%s',
            mandatory=True,
            position=1,
        ),
        doLogJacobian=dict(
            argstr='%d',
            position=3,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        imageDimension=dict(
            argstr='%d',
            mandatory=True,
            position=0,
            usedefault=False,
        ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        outputImage=dict(
            argstr='%s',
            mandatory=True,
            position=2,
        ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
        useGeometric=dict(
            argstr='%d',
            position=4,
        ),
    )
    inputs = CreateJacobianDeterminantImage.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_CreateJacobianDeterminantImage_outputs():
    output_map = dict(jacobian_image=dict(), )
    outputs = CreateJacobianDeterminantImage.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
