#!/usr/bin/python3.10
# -*- coding: utf-8 -*-

import os

def main():
	os.system("/home/banoffee/Documents/FoB/fob-project/skeleton_script_create_roc_plot.py -ibench /home/banoffee/Documents/FoB/fob-project/HGVS_2020_small_benchmark.tsv -ipred /home/banoffee/Documents/FoB/fob-project/HGVS_2020_small_polyphen_scores.tsv -color -o /home/banoffee/Documents/FoB/ROCplot_HGVS_2020_small_polyphen.png")


if __name__ == "__main__":
    main()