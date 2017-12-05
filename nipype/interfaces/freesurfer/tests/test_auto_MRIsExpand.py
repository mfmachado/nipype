# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import MRIsExpand


def test_MRIsExpand_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    distance=dict(argstr='%g',
    mandatory=True,
    position=-2,
    ),
    dt=dict(argstr='-T %g',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    copyfile=False,
    mandatory=True,
    position=-3,
    ),
    nsurfaces=dict(argstr='-N %d',
    ),
    out_name=dict(argstr='%s',
    position=-1,
    usedefault=True,
    ),
    pial=dict(argstr='-pial %s',
    copyfile=False,
    ),
    smooth_averages=dict(argstr='-A %d',
    ),
    sphere=dict(copyfile=False,
    usedefault=True,
    ),
    spring=dict(argstr='-S %g',
    ),
    subjects_dir=dict(),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    thickness=dict(argstr='-thickness',
    ),
    thickness_name=dict(argstr='-thickness_name %s',
    copyfile=False,
    ),
    write_iterations=dict(argstr='-W %d',
    ),
    )
    inputs = MRIsExpand.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MRIsExpand_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = MRIsExpand.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
