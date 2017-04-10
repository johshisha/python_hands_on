# とりあえずこれだけやっておけばいいこと

- gitのインストール
    - ubuntu: `$ sudo apt-get install git`
    - mac: `$ brew install git`
- pyenvのインストール＆設定
    zshの人は`~/.bash_profile` -> `~/.zshrc`に変更してください．
    ```
    $ git clone https://github.com/yyuu/pyenv.git ~/.pyenv
    $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
    $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
    $ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
    $ source ~/.bash_profile
    $ pyenv install 3.5.2 # 好きなバージョンで（とりあえず最新にしておけばよいかと）
    $ pyenv install 2.7.12
    $ pyenv rehash
    $ pyenv global 3.5.2 2.7.12
    ```
    動作確認（以下のようになっていなければ教えてね）
    ```
    $ python --version
    Python 3.5.2
    $ python3 --version
    Python 3.5.2
    $ python2 --version
    Python 2.7.12
    ```
    （おまけ）virtualenvもインストールするといいかも（[参考資料](http://qiita.com/Kodaira_/items/feadfef9add468e3a85b])）