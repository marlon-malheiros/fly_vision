"""Reproduce the comparison in a new directory using its preserved evidence."""
import argparse
import importlib
import shutil
from published_circuit_comparison_v1 import ROOT, RUN as AUTHORITATIVE, read, write, verify


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('action',choices=['prepare','freeze','run','analyze','review','plot'])
    p.add_argument('--destination',required=True);a=p.parse_args()
    destination=(ROOT/a.destination).resolve();rel=destination.relative_to(ROOT)
    assert rel.parts[0]=='results' and len(rel.parts)>1 and destination!=AUTHORITATIVE
    marker=destination/'reproduction_namespace.json'
    if a.action=='prepare':
        verify(read(AUTHORITATIVE/'before_main.json')['files'])
        destination.mkdir(exist_ok=False)
        shutil.copytree(AUTHORITATIVE/'audit',destination/'audit')
        shutil.copyfile(AUTHORITATIVE/'plans.json',destination/'plans.json')
        write(marker,dict(authoritative=str(AUTHORITATIVE.relative_to(ROOT)),destination=str(rel),
            preserved_audit_reused=True,new_download_claim=False))
        return
    assert read(marker)['destination']==str(rel)
    if a.action in ('freeze','run','analyze'):
        driver=importlib.import_module('published_circuit_comparison_v1');driver.RUN=destination
        getattr(driver,a.action)()
    elif a.action=='review':
        importlib.import_module('review_published_circuit_comparison_v1').main(destination)
    else:importlib.import_module('plot_published_circuit_comparison_v1').main(destination)


if __name__=='__main__':main()
