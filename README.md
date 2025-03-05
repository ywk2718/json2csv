# json2csv.py
## description  
python script for converting json format to csv/tsv format.  

## dependency
argparse  
pandas  
json  

## usages
json2csv.py -i <input.json> -o <outputfile> (optional) -t --no_header
* -i,--input  
  path to input json file
  
* -o,--output  
  path to output file
* (optional) -t,--out_tsv  
  output as tab separated format
* (optional) --no_header  
  output without header
