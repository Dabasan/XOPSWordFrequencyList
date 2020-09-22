"""
フォルダ内のMIFファイルからブリーフィングテキストを取得し、
それらを結合したテキストファイルを作成します。

出力の文字コードはUTF-8です。
"""
import argparse
import glob
import os

def main(input_dir,input_encoding,read_mif,output_filename):
    concat_lines=[]

    files=glob.glob(input_dir+"/*.*")
    for file in files:
        with open(file,"r",encoding=input_encoding) as r:
            lines=r.readlines()
            if read_mif:
                lines=lines[9:] #ブリーフィングテキストのみを取得する。
            concat_lines+=lines

    output_filepath=os.path.join(input_dir,output_filename)
    with open(output_filepath,"w",encoding="utf_8") as w:
        w.writelines(concat_lines)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--input_dir",type=str,default="./MIF_ShiftJIS")
    parser.add_argument("--input_encoding",type=str,default="shift_jis")
    parser.add_argument("--read_mif",action="store_true")
    parser.add_argument("--output_filename",type=str,default="concat.txt")

    args=parser.parse_args()

    main(args.input_dir,args.input_encoding,args.read_mif,args.output_filename)
