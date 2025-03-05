# json2csv.py
## description  
python script for converting json format to csv/tsv format.  

## dependency
argparse  
json  
pandas (https://pandas.pydata.org/)  
flatten_json (https://github.com/amirziai/flatten.git)  

## usages
```python
json2csv.py -i <input.json> -o <outputfile> (optional) -t --no_header -l
```
* -i,--input  
  path to input json file
  
* -o,--output  
  path to output file
* (optional) -t,--out_tsv  
  output as tab separated format
* (optional) --no_header  
  output without header
* (optional) -l,--jsonline
  use jsonl file as input

## example
__test_data.json__
```json
{
 "program":
 {
  "name":"json2csv.py",
  "developer":"ywk2718",
  "version":"1.0",
  "create_date":"2025-03-05"
 },
 "usage":
 {
  "input":"-i,--input <input json file>",
  "output":"-o,--output <output file>",
  "tsv output":"-t,--output_tsv",
  "no header":"--no_header"
  "use jsonl input":"-l,--jsonline"
 }
}
```

__output.csv__
```
program_name,program_developer,program_version,program_create_date,usage_input,usage_output,usage_tsv output,usage_no header,usage_use jsonl input
json2csv.py,ywk2718,1.0,2025-03-05,"-i,--input <input json file>","-o,--output <output file>","-t,--output_tsv",--no_header,"-l,--jsonline"
```

__output.tsv__
```
program_name	program_developer	program_version	program_create_date	usage_input	usage_output	usage_tsv output	usage_no header	usage_use jsonl input
json2csv.py	ywk2718	1.0	2025-03-05	-i,--input <input json file>	-o,--output <output file>	-t,--output_tsv	--no_header	-l,--jsonline
```
