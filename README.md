# json2csv.py
## description  
python script for converting json format to csv/tsv format.  

## dependency
argparse  
pandas  
json  
flatten_json(https://github.com/amirziai/flatten.git)  

## usages
```python
json2csv.py -i <input.json> -o <outputfile> (optional) -t --no_header
```
* -i,--input  
  path to input json file
  
* -o,--output  
  path to output file
* (optional) -t,--out_tsv  
  output as tab separated format
* (optional) --no_header  
  output without header

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
 }
}
```

__output.csv__
```
program.name,program.developer,program.version,program.create_date,usage.input,usage.output,usage.tsv output,usage.no header
json2csv.py,ywk2718,1.0,2025-03-05,"-i,--input <input json file>","-o,--output <output file>","-t,--output_tsv",--no_header
```

__output.tsv__
```
program.name	program.developer	program.version	program.create_date	usage.input	usage.output	usage.tsv output	usage.no header
json2csv.py	ywk2718	1.0	2025-03-05	-i,--input <input json file>	-o,--output <output file>	-t,--output_tsv	--no_header
```
