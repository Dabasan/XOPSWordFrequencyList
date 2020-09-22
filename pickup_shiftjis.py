"""
文字コードの判定を行い、指定された文字コードのファイルをコピーします。
"""
import argparse
import glob
import os
import shutil
from chardet.universaldetector import UniversalDetector

def get_encoding(filepath):
    detector=UniversalDetector()

    with open(filepath,mode="rb") as r:
        for b in r:
            detector.feed(b)
            if detector.done:
                break

    detector.close()

    return detector.result["encoding"]

def main(input_dir,output_dir,target_encoding):
    os.makedirs(output_dir,exist_ok=True)

    files=glob.glob(input_dir+"/*.*")
    for file in files:
        encoding=get_encoding(file)

        if encoding==target_encoding:
            dst_filepath=os.path.join(output_dir,os.path.basename(file))
            shutil.copyfile(file,dst_filepath)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--input_dir",type=str,default="./MIF")
    parser.add_argument("--output_dir",type=str,default="./MIF_ShiftJIS")
    parser.add_argument("--target_encoding",type=str,default="SHIFT_JIS")

    args=parser.parse_args()

    main(args.input_dir,args.output_dir,args.target_encoding)
