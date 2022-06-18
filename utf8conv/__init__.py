import argparse
from pathlib import Path
import chardet
from alive_progress import alive_it
import shutil
from time import time

parser = argparse.ArgumentParser(description='convert file to utf-8 encoding')
parser.add_argument('-i', '--input', help='input a folder or a single_file')
parser.add_argument('-o', '--output_folder', help='output folder for converted files')
parser.add_argument('-s', '--suffix', nargs='+', help='file type list. eg.: .txt .c .json .py .', default=['.txt'])
parser.add_argument('-v', '--verbose', action='store_true', help='show details')
args = parser.parse_args()

st = time()

file_suffix = set([t.lower() for t in args.suffix])

# get file list
proc_file_list = [Path(args.input).resolve()] \
    if Path(args.input).is_file() \
    else [file.resolve() for file in Path(args.input).rglob('*') if file.suffix.lower() in file_suffix]

# to maintain the tree structure, get the max same depth of input folder
max_depth = len(str(proc_file_list[0].parent)) + 1 \
    if len(proc_file_list) == 1 \
    else len(str(max(set.intersection(*map(set, [[p for p in f.parents] for f in proc_file_list]))))) + 1

num_file = len(proc_file_list)
if not args.verbose:
    proc_file_list = alive_it(proc_file_list)

for n, f in enumerate(proc_file_list):
    with open(f, 'rb') as file:
        # using chardet lib to detect text encoding
        det = chardet.detect(file.read())
        det_encoding = det['encoding'].upper() if det['encoding'] is not None else 'UTF-8'
    coding = 'GBK' if 'GB' in det_encoding else det_encoding

    # cov other encoding text into utf-8, copy utf-8 to target folder
    if coding != 'UTF-8':
        with open(f, 'r', encoding=coding) as file:
            txt = file.read()
        with open(Path(args.output_folder) / str(f)[max_depth:], 'w+', encoding='utf-8') as file:
            file.write(txt)
    else:
        shutil.copyfile(f, Path(args.output_folder) / str(f)[max_depth:])

    if args.verbose:
        print(' %.2f%% - [%i/%i] - %s - saved file <%s> to <%s>' %
              ((n + 1) / num_file * 100,
               n + 1, num_file,
               det_encoding,
               str(f.resolve()),
               str((Path(args.output_folder) / str(f)[max_depth:]).resolve())
               ))
if args.verbose:
    print('========================================')
    print('spend time: %s s' % (time()-st))

