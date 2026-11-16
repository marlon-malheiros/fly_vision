"""Retrospective acceptance audit; no model, cutoff or criterion changes."""
import argparse
import math
from pathlib import Path
from published_circuit_comparison_v1 import ROOT,read,write,record


def summarize(rows,group_keys,study):
    groups = sorted({tuple(p[k] for k in group_keys) for p in rows})
    output = []
    for values in groups:
        group = dict(zip(group_keys,values))
        selected = [p for p in rows if all(p[k]==v for k,v in group.items())]
        straight = [p for p in selected if p['yaw']==0]
        for magnitude in [2.,5.]:
            turns = [p for p in selected if abs(p['yaw'])==magnitude]
            assert len(turns)==48 and len(straight)==24
            detected = sum(p['decision'] is not None and p['decision']!=0 for p in turns)
            raw_sign = sum(p['score'] is not None and p['score']*p['yaw']>0 for p in turns)
            joint = sum(p['decision']==(1 if p['yaw']>0 else -1) for p in turns)
            false = sum(p['decision'] is not None and p['decision']!=0 for p in straight)
            assert max(0,detected+raw_sign-48)<=joint<=min(detected,raw_sign)
            output.append(dict(study=study,**group,magnitude=magnitude,turns=48,straight=24,
                detected=detected,raw_direction_correct=raw_sign,detected_with_correct_direction=joint,
                false_alarms=false,all_defined=all(p['defined'] for p in turns+straight),
                original_point_criteria_pass=all(p['defined'] for p in turns+straight) and detected>=39 and raw_sign>=39 and false<=2,
                joint_metric_is_retrospective_diagnostic_only=True))
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    out.relative_to(ROOT)
    sources = [ROOT/'results/geometry_grounded_small_yaw_v2/analysis/test_predictions.json',
               ROOT/'results/small_turn_target_decision_v4/analysis/predictions.json',
               ROOT/'configs/small_turn_target_decision_v4.json',
               ROOT/'docs/SMALL_TURN_TARGET_DECISION_PROTOCOL_V4.md']
    index = {e['path']:e for study in ['geometry_grounded_small_yaw_v2','small_turn_target_decision_v4']
             for e in read(ROOT/'results'/study/'completion_v1/artifact_index.json')['files']}
    records = [record(p) for p in sources]
    for e in records:
        assert e==index[e['path']],e['path']
    cfg = read(sources[2])
    assert cfg['false_positive_maximum']==.1
    neural = [r for r in read(sources[0]) if r['kind']=='network']
    image = [r for r in read(sources[1]) if r['speed']!=0]
    rows = summarize(neural,['model','role','speed'],'neural_V2')
    rows += summarize(image,['rule','method','speed'],'image_V4')
    out.mkdir(parents=True,exist_ok=False)
    write(out/'metrics.json',rows)
    z = 1.959963984540054
    write(out/'review.json',dict(status='PASS',review_date='2026-10-26',
        retrospective_review_not_new_experiment=True,sources_match_existing_seals=records,
        script=record(Path(__file__).resolve()),condition_summaries=len(rows),
        original_48turn_minimum_detected=math.ceil(.8*48),
        original_48turn_minimum_raw_direction=math.ceil(.8*48),
        original_24straight_maximum_false_alarms=math.floor(.1*24),
        zero_of_24_false_alarm_Wilson_95_upper=z*z/(24+z*z),
        original_acceptance_criteria_changed=False,model_or_cutoffs_changed=False,
        added_joint_metric_not_used_to_reclassify_old_studies=True,biological_validation=False))
    for r in rows:
        if r['magnitude']==2 and ((r['study']=='neural_V2' and r['model']=='baseline' and r['role']=='dnp15') or
            (r['study']=='image_V4' and r['rule']=='target_midpoint' and r['method'] in ['lk_median','subspace_median'])):
            print(r,flush=True)
    print('Retrospective acceptance review PASS; original criteria unchanged',flush=True)


if __name__=='__main__':
    main()
