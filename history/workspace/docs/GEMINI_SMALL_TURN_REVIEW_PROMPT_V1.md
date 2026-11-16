# Prompt for Gemini: independent, cost-conscious technical review

Read `docs/SMALL_TURN_EXTERNAL_REVIEW_HANDOFF_V1.md` or the attached file with that
basename. If you are running in
the project directory, the root is
`<WORKSPACE>`; follow `AGENTS.md` and begin with
the handoff's priority file list. If you cannot access the files, say so and do
not claim that you inspected them.

Act as a critical computational-neuroscience and machine-learning reviewer.
Our target is reliable neural-only detection of +/-2-degree/s body yaw during
forward walking at 5.5, 11 and 16.5 mm/s, with a 190-ms endpoint, >=80% joint
correct detections including each sign and <=10% episode-level straight/stationary
false alarms. Biological agreement is a separate requirement.

We have a bounded 5-degree/s neural success, a separate 2-degree/s image/hybrid
success, and repeated failed 2-degree/s neural attempts. The latest 16 fitted
readers/44 policy combinations all fail calibration. Three readers nevertheless
get the turn direction right in every actual small-turn trial. Some numerically
qualified candidates still fail the task. Existing source-model reproduction is
not physiological validation, and LPi feedback is already present in the MaleCNS
graph. A newly tested reduced vertical opponent motif transferred horizontally
also failed. The idea of retraining a walking-specific visual encoder remains
unproven; failed readouts alone do not establish an encoder bottleneck.

The previous round used substantial resources. I want a decisive diagnosis and
one small next experiment, not another broad list of expensive options.

Please return:

1. A concise verdict on what is established and what the current explanation
   overstates. Cite saved evidence if you can inspect it.
2. A ranked differential diagnosis: representation, pooling, readout, confidence,
   temporal behavior, domain shift, numerical sampling and task specification.
   Explain what would falsify each leading hypothesis.
3. An assessment of whether encoder retraining is justified now. Identify the
   cheapest existing-data test that could answer that decision.
4. At most three genuinely distinct alternatives, identifying which similar
   approaches have already failed. Choose one next test with exact inputs,
   one controlled change, controls, pass/fail criteria, maximum run/time/memory
   budget, and a clear stop rule. A read-only analysis may be the best next test.
5. The minimum physiological evidence required for the model claim, keeping
   anatomical measurements, assumptions, calibration and independent validation
   separate. Do not assume that missing exact stimuli prevent every narrower assay.
6. A short undergraduate-level explanation of your recommendation.

Do not run new simulations/training, alter existing results, use reserved test
rooms for development, invent biological parameters or soften the original
criteria during this initial review. If no supported route is currently available,
identify the precise missing evidence rather than claiming universal impossibility.
