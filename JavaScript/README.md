JavaScript
==========

1. 常见的数据类型, 前3个可以作为类型转换函数
    String  
    Number  
    Boolean  
    Array  
    Object  
    Undefined

    ```javascript
    // 创建一个对象与python中字典的区别

    var person = {
        name: `aquarius`,
        age: 26,
        gender: "0"，
        GetName: function(){
                console.log(this.name)
            },
    }

    person.GetAge = functionn(){
        console.log(this.age)
    }

    // 注意如果使用ES6匿名函数的语法无法使用this,即下面写法是错误的

    person.GetAge = () => {
        console.log(this.age)
    }

    // ES6增加了默认参数和剩余参数
    // 函数中剩余参数与python中的写法区别

    function test(name="aquarius", ...args){
        // 函数体内，如果两行语句没有写在一行，不需要加分号

        console.log(name)
        console.log(...args)
    }

    ```

2. 类型查询使用typeof关键字，区分Array与Object使用instanceof  
    ```javascript
    // 使用typeof获得的类型描述
    // 'number' 
    typeof(1013)
    // 'string'
    typeof('1013')
    // 'object'
    typeof({})
    typeof([])
    // 'function'
    // test 为一个函数
    typeof(test)

    // 判断是否为数组
    [1, 2, 3] instanceof Array
    ```
3. 与python相似的迭代方法
    ```javascript
    // Array

    array = [1, 2, 3, 4]

    // i 为索引

    for(i in array){
        console.log(i)
    }

    // v 为元素

    for(v of array){
        console.log(v)
    }

    // Object
    // p 为对象成员的名称

    test = {1:2, 3:4}    
    for(p in test){
        console.log(p)
    }
    ```


转码
--

```js
// 转化成url编码
let uri = encodeURIComponent("aquarius")
```