# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..visualization import CreateTiledMosaic


def test_CreateTiledMosaic_inputs():
    input_map = dict(alpha_value=dict(argstr='-a %.2f',
    ),
    args=dict(argstr='%s',
    ),
    direction=dict(argstr='-d %d',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    flip_slice=dict(argstr='-f %s',
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    input_image=dict(argstr='-i %s',
    mandatory=True,
    ),
    mask_image=dict(argstr='-x %s',
    ),
    num_threads=dict(nohash=True,
    usedefault=True,
    ),
    output_image=dict(argstr='-o %s',
    usedefault=True,
    ),
    pad_or_crop=dict(argstr='-p %s',
    ),
    permute_axes=dict(argstr='-g',
    ),
    rgb_image=dict(argstr='-r %s',
    mandatory=True,
    ),
    slices=dict(argstr='-s %s',
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    tile_geometry=dict(argstr='-t %s',
    ),
    )
    inputs = CreateTiledMosaic.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_CreateTiledMosaic_outputs():
    output_map = dict(output_image=dict(),
    )
    outputs = CreateTiledMosaic.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
