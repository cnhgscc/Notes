GOlang pakeage
--------------

    # 查询 golang env
    go env

    cd $GOPATH/src/example
    mkdir newmath
    在目录$GOPATH/src/example/newmath/下新建一个文件sqrt.go
    go install example/newmath

    之后在其他的go文件中就可以直接导入使用了