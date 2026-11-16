"""Chunked binocular image inputs for existing T4/T5 population solvers.

Sampling inherits the documented exploratory registration and ON/OFF rules
from physiological_population. It does not run cable models or claim a
validated voltage-to-release transform.
"""
from __future__ import annotations

import numpy as np

from .physiological_population import sample_population


def iter_shared_eye_inputs(left_movie, right_movie, inventory, source_ids,
                           spatial_config, *, adaptation_ms=3000., chunk_size=64):
    """Yield complete, ID-labeled T4/T5 cable-input chunks, without movies.

    Each eye movie is shared by all cells on that side. Contrast arrays have
    shape (clock, cells, native positions), with a constant first-image
    prehistory. Concatenate/reorder the returned cell IDs to reconstitute the
    exact source set; chunk order itself is not circuit identity.
    """
    if not isinstance(chunk_size, int) or isinstance(chunk_size, bool) or chunk_size < 1:
        raise ValueError('Chunk size must be a positive integer')
    if not np.isfinite(adaptation_ms) or adaptation_ms <= 0:
        raise ValueError('Adaptation must be positive and finite')
    if left_movie.time_s[0] != 0 or not np.array_equal(left_movie.time_s, right_movie.time_s):
        raise ValueError('Eye movie clocks must match exactly and start at zero')
    ids=tuple(map(str, source_ids)); rows={str(r['body_id']):r for r in inventory}
    if len(ids)!=len(set(ids)) or len(rows)!=len(inventory) or set(ids)!=set(rows):
        raise ValueError('Unique inventory IDs must exactly cover source IDs')
    for row in inventory:
        if row['side'] not in ('L','R') or row['family'] not in ('T4','T5'):
            raise ValueError('Unknown side or cell family')
        if row['cell_type'] not in tuple(f'{fam}{sub}' for fam in ('T4','T5') for sub in 'abcd') or row['family']!=row['cell_type'][:2]:
            raise ValueError('Cell subtype and family do not agree')
    clock=np.r_[0.,adaptation_ms + np.asarray(left_movie.time_s,dtype=float)*1000]
    for side,movie in (('L',left_movie),('R',right_movie)):
        for family in ('T4','T5'):
            selected=[rows[body] for body in ids if rows[body]['side']==side and rows[body]['family']==family]
            for start in range(0,len(selected),chunk_size):
                cells=selected[start:start+chunk_size]
                contrast,coverage=sample_population(movie,cells,spatial_config)
                yield {'time_ms':clock.copy(),'body_ids':tuple(str(r['body_id']) for r in cells),
                       'side':side,'family':family,'contrast':contrast,'coverage':coverage}
