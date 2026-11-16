# Offline execution storage amendment — V2

Specified 2026-10-21 from measured storage use, without changing scientific
conditions, inclusion rules, neural parameters or outcome criteria.

The first 525 network files occupied 836 MB; their mean 1.59 MB per case projected
about 5.63 GB for the 3,536-case sweep, exceeding the initial reserve. A numerical
roundtrip test on a completed case reduced standard NPZ size from 1,610,605 to
1,079,375 bytes using ZIP_LZMA, while every array/dtype remained exactly identical
under ordinary `numpy.load`. This uses a standard ZIP compression method, not
quantization, bit-depth reduction or a custom array decoder.

Preserve every completed file and receipt in its original format. Interrupt the
current execution in a controlled way and verify its terminal tool handle before
resuming. Preserve interruption logs/partial files; move any complete orphan
without a receipt to a separate failure directory before recomputation. Compare
the recomputed orphan's arrays before concluding recovery.

The separate continuation launcher imports the frozen study implementation,
replaces only its output serializer with lossless NPZ/LZMA, and reduces the
per-case free-disk guard to 1.5 GB. This is a declared resource override; the
original config/manifest remain unmodified. Four workers, all planned cases,
stimuli, clocks, graphs, decoders and acceptance rules remain unchanged. Current
receipts are reverified/skipped. The expected compressed sweep leaves more free
space, and the guard still stops new cases before the lower reserve is reached.

Link the original prospective manifest, this amendment, the exact launcher and
storage module digests, roundtrip tests and interruption/orphan ledger in the
continuation manifest. Both ZIP formats must remain readable by the original
analysis code. Record all material failures and do not remove old studies or
completed new evidence to free space.
