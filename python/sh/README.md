bashrc
------

python 环境设置

```sh
    export WORKON_HOME=$HOME/Pyenv
    source /usr/local/bin/virtualenvwrapper.sh

    alias sawyer="cd $HOME/Pyenv/sawyer"
    alias quit="deactivate"

    alias Pyrun="$HOME/Pyenv/sawyer/bin/python"
    alias Pipenv="$HOME/Pyenv/sawyer/bin/pip"
    alias ipython="$HOME/Pyenv/sawyer/bin/ipython"
```