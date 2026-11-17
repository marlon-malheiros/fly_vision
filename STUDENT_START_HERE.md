# Start here: optomotor circuit and embodied testing

The main research objective is to model the fly optomotor circuit with connectome constraints, test its biological predictions, and evaluate an embodied implementation. A new, executable closed-loop prototype is in **[optomotor_closed_loop/](optomotor_closed_loop/README.md)**.

Read **[the student handoff](optomotor_closed_loop/STUDENT_HANDOFF.md)** first. It contains exact installation/replay commands, expected results, scientific priorities, stopping criteria, and copyable prompts for an AI coding assistant.

After reproducing the baseline, start **[the first student assignment](optomotor_closed_loop/FIRST_STUDENT_TASK.md)**: a fair gain-and-delay study with the neural circuit held fixed. It explains why the current configured gain largely determines the 66% compensation level and defines how to seek stronger compensation without hiding drift or instability.

The completed random-square benchmark uses 20 individual central neurons and pooled functional drive from 6,753 T4a/b and T5a/b sources, with 24,910 measured retained chemical pairs. It passes a bounded synthetic engineering test: 66.4% median yaw-RMS reduction, 0.20 degrees/s median straight-travel yaw RMS, fourteen implementation checks and a separate arithmetic/integrity review. The conventional visual controller reaches 67.2%; biological architecture advantage is not established. Physiological validation and physical hardware testing remain outstanding.

The original alignment-assessment pilot, manuscript, source inventories and history remain in their existing locations. Its numerical reproducibility is a separate result. Start new optomotor work inside optomotor_closed_loop rather than modifying that pilot's frozen evidence.
