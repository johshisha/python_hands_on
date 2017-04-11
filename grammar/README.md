# pythonの基本的な書き方
## できる人は飛ばしてください

## この章の目標
ソートアルゴリズムを実装する
- バブルソート
- クイックソート
[問題](./sort.md)

## pythonのバージョン
基本的には3系で書いたほうがいいと思います．  
研究者は2系を使ってる人が多いので2系もインストールしておくといいと思います．

## 文法
コメントアウトは`#`でする．  
javaとかと違い，よく忘れる`;`とかはないです．
その代わりにインデントで文を表現します．

Javaでこう書くのを
```
for(int i=0; i<10; i++){
    if(i == 3){
        System.out.println("これは3だよ");
    }else{
        System.out.println(i);
    }
}
```

Pythonではこう書く
```
for i in range(10):
    if i == 3:
        print("これは３だよ")
    else:
        print(i)
        
```


## 実行方法
`$ python [filename].py [arguments]`

