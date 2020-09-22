"""
単語の出現回数をカウントします。
"""
import collections

if __name__=="__main__":
    with open("./genkeis_omit_signs.txt","r",encoding="utf_8") as r:
        genkeis=r.read().splitlines()

    counter=collections.Counter(genkeis)

    output_lines=[]
    for tup in counter.most_common():
        output_line="{}\t{}\r\n".format(tup[0],tup[1])
        output_lines.append(output_line)

    with open("./result.txt","w",encoding="utf_8",newline="") as w:
        w.writelines(output_lines)
