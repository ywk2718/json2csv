#! /usr/bin/env python3
#Usage python3 json2csv.py -i input.json -o output.csv/output.tsv -t --no_header -l
import sys
import os
import argparse
import pandas as pd
import json
import flatten_json

parser = argparse.ArgumentParser(description='python script for converting json/jsonl format to csv/tsv format')

parser.add_argument('-i', '--input', required=True, help='input json file')
parser.add_argument('-o', '--output', required=True, help='output file')
parser.add_argument('-t', '--out_tsv', action='store_true', help='output as tsv format')
parser.add_argument('--no_header', action='store_true', help="output without header" )
parser.add_argument('-l', '--jsonline', action='store_true', help="jsonline input" )

args = parser.parse_args()

fileIn = args.input
fileOut = args.output
outTsv = args.out_tsv
noHeader = args.no_header
jsonLine = args.jsonline

#load input.json file
if jsonLine == True:
    #json_open = jsonlines.open(fileIn, 'r')
    #json_load = jsonlines.Reader.iter(json_open, type=dict)
    #json_flat = flatten_json.flatten(json_load)
    #df_json = pd.json_normalize(json_load)
    df_json = pd.DataFrame()
    with open(fileIn, 'r') as f:
        for l in f.readlines():
            json_load = json.loads(l)
            json_flat = flatten_json.flatten(json_load)
            df_json_append = pd.json_normalize(json_flat)
            df_json = pd.concat([df_json,df_json_append])

else:
    json_open = open(fileIn, 'r')
    json_load = json.load(json_open)
    json_flat = flatten_json.flatten(json_load)
    df_json = pd.json_normalize(json_flat)

#expand nested json format with json_normalize
#df_json = pd.json_normalize(json_load)

#command option
cmd = "df_json.to_csv(fileOut, index=False, encoding='utf-8'"
if outTsv == True:
    cmd = cmd+", sep='\t'"
if noHeader == True:
    cmd = cmd+", header=False"
cmd = cmd+")"
eval(cmd)
