# CPU worker placement and scheduled response reliability — V7

Completed 2026-10-22, America/Belem. Engineering component; original scientific models and evidence remain preserved.

**Outcome:** the bound profile produces 2,536 fewer frame misses than unbound execution over equal 96,240-frame samples on this host: 4.80% unbound versus 2.16% bound. The original zero-miss deadline criterion is **FAIL** for unbound and **FAIL** for bound. Numerical trajectories and full final states remain bit identical across matched inputs. These observed results do not establish physical camera capture, physiological validity or a hard-real-time guarantee. The broad goal remains active.

## Fixed intervention and comparison

Both profiles execute the same exported original MaleCNS graph, V5 causal work split, compiled retinal projector and explicitly accelerated four-thread bounded-activation library. The graph's 13,579 source neurons retain all 192,967 nonzero incoming source-row chemical connections, plus 10,894 incoming entries in 14 wide-neuron rows. No uncoupled solver shortcut, neural parameter, input image, decoder, 1-ms integration step, 5-ms camera cadence or 10-ms published-rate cadence changes. The historical readout still averages 70 samples at 0.70–1.39 s and emits at 1.4 s. All original biological/visual errors remain.

The unbound profile permits workers on the full allowed CPU mask. The bound profile assigns the main/OpenMP workers to logical CPUs **0,2,4,6**, four distinct physical-core groups selected before new performance results by declared maximum frequency then CPU index. Sysfs reports 4.4-GHz maxima for these groups and 3.3 GHz for the other available groups; actual frequency is not forced or inferred. The unavailable core-type field prevents an architectural core-kind claim. The logger explicitly retains all twelve allowed logical CPUs in both profiles. Binding includes the main thread outside parallel sections and is an application execution setting, not a circuit change. No priority, global scheduler or other-process affinity changes occur. [Prospective protocol](CPU_WORKER_PLACEMENT_PROTOCOL_V7.md), [configuration and live topology](../configs/cpu_worker_placement_v7_r2.json), [launcher](../scripts/cpu_worker_placement_v7.py).

All child environments set four OpenMP threads, active waiting, dynamic teams disabled and one OpenBLAS thread. Inherited placement variables are cleared. OMP_PROC_BIND is FALSE for unbound, and TRUE with four explicit places for bound. Affinity is observed after computation: exactly four compute-thread masks match their declared profile. Every logging receipt confirms the full original mask. This checks recorded placement observations, not uninterrupted per-instruction CPU occupancy.

## Preflight, startup correction and numerical evidence

Nine utility tests pass. Three interleaved repetitions of each profile on all three full fixtures give an 18-episode preflight matrix. Each configuration contributes nine episodes, 3,600 noninitial frames and 1,800 paired updates. The same historical room s01 fixtures contain forward speed 16.5 mm/s with yaw 0,+20,−20°/s; motion occurs from 0.5 to 1.5 s within each two-second episode. Repeated fixtures are engineering repetitions rather than independent environments or animals.

| Placement | Frame processing median/p95/p99 (ms) | Frames >5 ms | Paired processing median (ms) | Pairs >10 ms |
|---|---:|---:|---:|---:|
| unbound | 2.934/3.588/4.482 | 7/3,600 | 5.892 | 2/1,800 |
| bound | 2.812/3.749/4.282 | 15/3,600 | 5.661 | 7/1,800 |

The first attempt preserves three completed unbound controls and a bound child that stopped before images. Its startup assertion assumed an unbound main-thread mask persisted until the explicit neural import. An import-only probe shows requested binding already applies during NumPy loading. R2 records the early observation and allows the requested first place for that startup check. The final four-worker mask criterion, CPU list, order, numerical tolerance and timing gates remain unchanged. The three original controls are independently reviewed and reported separately from the planned 18-case matrix. Related outcomes are known; the correction is not independent biological confirmation. [Startup correction](CPU_WORKER_PLACEMENT_STARTUP_CORRECTION_V7_R2.md), [preserved original attempt](../results/validation_hardware_v1/cpu_worker_placement_v7), [complete R2 preflight](../results/validation_hardware_v1/cpu_worker_placement_v7_r2/preflight.json).

Independent review checks every retained scheduled wide-neuron trajectory and full FP64 final state, original episode score/decision, intended/start/end timestamp, logging receipt, thread mask, standalone archive entry and the preceding 327-entry V6 seal. All matched-case rates/final states are bit identical across profiles and repetitions. Against original goldens, maximum rate/final-state discrepancies are 1.73e-18/8.13e-20; original score arithmetic agrees within 1.78e-14. The 1e-10 tolerance is unchanged. [Authoritative review](../results/validation_hardware_v1/cpu_worker_placement_v7_r2/independent_review_v1/review.json).

## Counterbalanced scheduled execution

Four matched pairs contain eight separate 60-episode child processes: **480 episodes, 192,480 binocular frame pairs and 96,000 noninitial neural updates**. Each profile receives 240 episodes and 80 repetitions of each fixture. Both profiles within a pair receive identical case orders. The first profile is unbound/bound/bound/unbound across pairs, balancing two starts per profile. Each run has its own uninterrupted 120.295-s availability schedule; roughly sixteen minutes across eight schedules is not one continuous sixteen-minute capture. Input loading and buffer allocation precede timing. Every episode initial frame, reset, logging event and delayed response remains included; there is no hidden warm-up, dropped frame, clock retiming or latency filter. Two bounded ten-episode buffers feed one uncompressed writer. [Frozen scheduled record](../results/validation_hardware_v1/cpu_worker_placement_v7_r2/scheduled_before_execution.json), [complete execution](../results/validation_hardware_v1/cpu_worker_placement_v7_r2/scheduled_complete.json).

Frame response is completion minus scheduled availability and has a 5-ms budget. Paired response is the even-frame result's completion minus preceding odd-frame availability and has a 10-ms budget. Paired processing is the sum of the two processing durations and omits waiting/backlog. First frames count in frame totals and are excluded from paired updates. These definitions match earlier studies.

| Pair | Placement | Frame response median/p95/p99 (ms) | Frames >5 ms | Paired responses >10 ms | Maximum frame response (ms) |
|---|---|---:|---:|---:|---:|
| 1 | unbound | 3.042/4.868/11.976 | 963/24,060 | 563/12,000 | 36.559 |
| 1 | bound | 3.056/3.932/6.269 | 361/24,060 | 192/12,000 | 31.712 |
| 2 | bound | 3.020/3.793/6.105 | 345/24,060 | 175/12,000 | 28.542 |
| 2 | unbound | 3.111/4.840/16.447 | 1,047/24,060 | 562/12,000 | 70.848 |
| 3 | bound | 3.048/3.957/8.442 | 475/24,060 | 253/12,000 | 23.689 |
| 3 | unbound | 3.186/5.046/16.728 | 1,244/24,060 | 683/12,000 | 36.106 |
| 4 | unbound | 3.169/5.241/29.746 | 1,362/24,060 | 716/12,000 | 108.101 |
| 4 | bound | 3.023/4.238/11.922 | 899/24,060 | 459/12,000 | 31.737 |

Pooled unbound/bound frame-response misses are **4,616/2,080**, each out of 96,240. Pooled paired-response misses are **2,524/1,079**, each out of 48,000; processing-only paired misses are 953/434. Frame-miss differences (bound minus unbound) in the four matched pairs are **[-602, -702, -769, -463]**. Negative differences favor binding. All four differences and individual runs are retained, without selecting a favorable repetition or treating frame counts as independent population trials.

![Scheduled placement timing](../results/validation_hardware_v1/cpu_worker_placement_v7_r2/report_v1/placement_timing.png)

## Output availability under the unchanged clock contract

Apply both previously declared V6 scenarios to every saved frame: exposure midpoint at software availability with zero uncertainty, or a hypothetical midpoint 0.5 ms earlier plus 100-ns uncertainty. These are retrospective arithmetic policies, not measured camera transfer or new guarded-execution benchmarks. The strict latch publishes only the prefix before an episode's first fault; that frame and subsequent frames remain withheld until an explicit reset. The actual scheduled experiment continues recording all frames and never uses these policies to hide misses.

| Placement | Scenario | All-frame policy faults | Episodes requiring reset | Accepted prefix frames | Withheld frames |
|---|---|---:|---:|---:|---:|
| unbound | software_reference | 4,616/96,240 | 230/240 | 28,496/96,240 | 67,744/96,240 |
| unbound | synthetic_capture_offset | 8,676/96,240 | 240/240 | 13,708/96,240 | 82,532/96,240 |
| bound | software_reference | 2,080/96,240 | 160/240 | 59,019/96,240 | 37,221/96,240 |
| bound | synthetic_capture_offset | 2,600/96,240 | 195/240 | 49,299/96,240 | 46,941/96,240 |

Prefix availability shows the practical cost of rare timing failures to a stateful circuit. Automatic mid-episode resets would discard history and are not a recovery proof. Recorded thread placement and passed numerical comparisons alone cannot establish reliable continuous sensor operation. The V6 consumer check still certifies only its clock observation instant; later OS preemption remains possible. [All per-episode policy results and numerical tables](../results/validation_hardware_v1/cpu_worker_placement_v7_r2/report_v1), [clock contract](PORTABLE_CPU_CLOCK_CONTRACT_REPORT_V6_R2.md).

![First-fault availability](../results/validation_hardware_v1/cpu_worker_placement_v7_r2/report_v1/placement_availability.png)

## Portable package, scope and next work

The [V7 CPU archive](../results/validation_hardware_v1/deployment/original_runtime_cpu_v7.zip) has 62 indexed files and 32,877,006 bytes; SHA-256 `98f3b8beeb9ac444481b274b9fb0c0c143b0247aff2175846133540786170c89`. All 57 V6 baseline entries are preserved byte for byte, with README/protocol given explicit baseline names. The strict one-thread numerical builder remains the default. Placement is an explicit optional child-process setting for separately built four-thread libraries. Both standalone profiles compile fresh libraries from an isolated extraction with project imports cleared, preserve three complete camera cases and 24 fixed faults each, and verify actual worker masks. Their synthetic clock traces test interface logic rather than execution speed. [Exported README](../results/validation_hardware_v1/deployment/original_runtime_cpu_v7/README.md), [unbound standalone](../results/validation_hardware_v1/cpu_worker_placement_v7_r2/standalone_unbound_v1/standalone.json), [bound standalone](../results/validation_hardware_v1/cpu_worker_placement_v7_r2/standalone_bound_v1/standalone.json).

From a fresh extracted directory with the declared Python/NumPy/SciPy/C++17/OpenMP dependencies:

```sh
python selfcheck_cpu_placement_v7.py --profile unbound --work check_unbound
python selfcheck_cpu_placement_v7.py --profile bound --cpus 0,2,4,6 --work check_bound
```

Use fresh work directories and a valid CPU list for the actual host. The tested list is not a portable hardware prescription. Only one host and three fixed scenes/conditions are measured. The maximum-frequency metadata is not measured sustained frequency. Ordinary host load, thermal/power management, OS scheduling and logging interactions remain possible influences; counterbalancing reduces simple order confounding without eliminating them. The larger biological yaw/generalization study remains separate, with its false positives, wrong H2 directions and unresolved sensitivity/convergence preserved. [Scientific findings](VALIDATION_GENERALIZATION_CONVERGENCE_REPORT_V1.md), [physiological limitations](CORRECTED_PHYSIOLOGICAL_DIAGNOSTICS_REPORT_V2.md).

The next work must follow the observed timing and availability gates, rather than declaring readiness from a faster median. Real optical/photometric/clock calibration, actual acquisition, broader workloads, biological stimulus matching and robust continuous execution remain necessary. No closed-loop locomotion or motor output is implemented, and numerical simulation does not establish physiological validity.

## Undergraduate explanation: what we did, what we want and why

We want a fly-inspired visual system that can recognize unwanted turns and eventually run on real hardware. We tested whether keeping its four computing workers on separate selected CPU cores helps it keep up with incoming images. The neural model, images and outputs stayed the same. We compared repeated runs in a balanced order and kept all late results. We also calculated how much usable data remains if the system stops after the first timing fault. This separates a faster calculation from a reliable continuous visual system. The CPU package is reproducible, but real cameras and biological agreement still need their own evidence before the model can control a robot.
