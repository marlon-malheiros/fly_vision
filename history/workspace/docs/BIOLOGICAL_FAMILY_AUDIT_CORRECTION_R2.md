# DNp15 audit execution correction R2

27 October 2026. The V1 audit failed Python compilation before reading recordings:
the metadata dictionary repeated the keyword `source` for the relative path and
the file-provenance record. AST parsing alone did not catch this compilation error.

Preserve the frozen V1 file, initial freeze and recorded failure. The separately
versioned R2 audit renames the file-provenance field to `source_record` and checks
its own additional source manifest. It makes no scientific change to metadata
comparisons, projection formulas, model parameters or acceptance/decision rules.
Compile the corrected source and freeze it before executing either audit action.

The factorial neural experiment remains the original frozen experiment; its
replay can finish independently. This correction does not authorize fitting an
oracle gain, changing readout side or revising a biological result.
