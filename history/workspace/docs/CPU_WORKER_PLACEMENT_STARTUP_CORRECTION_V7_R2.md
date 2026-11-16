# V7 startup observation correction — R2

Recorded 2026-10-22 after the first unbound three-fixture preflight completed and the first bound child failed before image processing. The original source, configuration, three successful unbound outputs, failed bound log and failure records are preserved in `results/validation_hardware_v1/cpu_worker_placement_v7`.

The original driver assumed its initial main-thread affinity still equaled the parent allowed mask. OpenMP can apply the requested main-thread binding while an imported numerical library loads, before the driver's first explicit neural call. A separately saved import-only probe records this behavior without processing images or measuring performance.

The new R2 driver records its observed startup mask. Unbound still requires the full original allowed mask; bound accepts either that mask or the first requested single-CPU place at this early observation. The **post-computation four-thread mask check is unchanged**: bound workers must occupy exactly the four requested distinct places, and unbound workers must retain the full allowed set. Numerical tolerance, all neural inputs/parameters, timing gates, CPU selection, order and planned scheduled experiment are unchanged.

Repeat the complete 18-episode preflight in a fresh `cpu_worker_placement_v7_r2` directory, preserving the original partial attempt. Related unbound outcomes are already known; this is an engineering correction/repetition, not a fresh independent biological validation. Freeze the new source and amendment before the repeated outcomes. No scheduled V7 experiment ran in the first attempt.
