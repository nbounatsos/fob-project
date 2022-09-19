#!/usr/bin/python3.10
# -*- coding: utf-8 -*-

import os

def main():
	os.system("/home/banoffee/Documents/FoB/fob-project/skeleton_script_create_roc_plot.py -ipred HGVS_2020_small_polyphen_scores.tsv -ipred HGVS_2020_small_sift_scores.tsv -ipred /home/banoffee/Documents/FoB/HGVS_2020_small_baseline_scores.tsv -ibench HGVS_2020_benchmark.tsv -o /home/banoffee/Documents/FoB/all_roc.png")


if __name__ == "__main__":
    main()