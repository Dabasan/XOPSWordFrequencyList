//形態素解析を行います。
package main

import (
	"bufio"
	"io/ioutil"
	"os"
	"strings"

	ipa "github.com/ikawaha/kagome-dict-ipa"
	"github.com/ikawaha/kagome/tokenizer"

	"github.com/cheggaaa/pb/v3"
)

func readFile(filepath string) ([]string, error) {
	fp, err := os.Open(filepath)
	if err != nil {
		return nil, err
	}
	defer fp.Close()

	lines := make([]string, 0)

	scanner := bufio.NewScanner(fp)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return lines, nil
}

func analyze(lines []string) ([]string, error) {
	//Tokenizerの作成
	t, err := tokenizer.New(ipa.Dict())
	if err != nil {
		return nil, err
	}

	//プログレスバーの作成
	bar := pb.Simple.Start(len(lines))
	bar.SetMaxWidth(-1)

	//各単語の原型を保存するリスト
	genkeis := make([]string, 0)

	for _, line := range lines {
		bar.Increment()
		tokens := t.Tokenize(line)

		for _, token := range tokens {
			if token.Class == tokenizer.DUMMY {
				continue
			}

			genkei := token.Features()[6]
			genkeis = append(genkeis, genkei)
		}
	}
	bar.Finish()

	return genkeis, nil
}

func main() {
	//ファイルからテキストを読み込む。
	lines, err := readFile("./all_text.txt")
	if err != nil {
		panic(err)
	}

	//形態素解析を行う。
	genkeis, err := analyze(lines)
	if err != nil {
		panic(err)
	}

	//結果をファイルに保存する。
	outputText := strings.Join(genkeis, "\r\n")
	if err := ioutil.WriteFile("./genkeis.txt", []byte(outputText), 0666); err != nil {
		panic(err)
	}
}
