# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..model import MS_LDA


def test_MS_LDA_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    conform=dict(argstr='-conform',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    images=dict(argstr='%s',
    copyfile=False,
    mandatory=True,
    position=-1,
    ),
    label_file=dict(argstr='-label %s',
    ),
    lda_labels=dict(argstr='-lda %s',
    mandatory=True,
    sep=' ',
    ),
    mask_file=dict(argstr='-mask %s',
    ),
    shift=dict(argstr='-shift %d',
    ),
    subjects_dir=dict(),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    use_weights=dict(argstr='-W',
    ),
    vol_synth_file=dict(argstr='-synth %s',
    mandatory=True,
    ),
    weight_file=dict(argstr='-weight %s',
    mandatory=True,
    ),
    )
    inputs = MS_LDA.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MS_LDA_outputs():
    output_map = dict(vol_synth_file=dict(),
    weight_file=dict(),
    )
    outputs = MS_LDA.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
