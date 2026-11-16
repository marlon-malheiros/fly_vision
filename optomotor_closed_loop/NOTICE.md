# Attribution and scope of this addition

The original implementation and new documentation in this folder follow the repository's MIT code license. The existing repository manuscript and other third-party datasets retain their separately documented terms.

The anatomy in data/derived comes from **MaleCNS v1.0**, distributed under **Creative Commons Attribution 4.0 (CC BY 4.0)**. Credit: FlyEM/HHMI Janelia, University of Cambridge, MRC Laboratory of Molecular Biology, Google Research, and collaborators. Source: https://male-cns.janelia.org/download/ . The source filenames, hashes, selection rules and retained/cut connectivity are recorded in data/derived/connectome_provenance.json.

Transformations: selected HSN/HSE/HSS/HST/H2/PS321/DNp15/LPi12/LPi21 cells; selected horizontal T4a/b and T5a/b inputs; retained measured source-to-central and central-to-central chemical pairs; exported full incoming/outgoing counts for the central boundary; recorded central-to-source feedback cut by the model. Transmitter predictions and anatomical counts do not establish measured dynamical efficacy.

New simulations and random-square stimuli are original computational outputs. They do not contain neural recordings or the CC BY-NC Gruntman stimulus extracts used in the separate root alignment pilot. Publication of this addition does not imply endorsement by the MaleCNS or physiology-study authors.
