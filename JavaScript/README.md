JavaScript
==========


https://caniuse.com/
Nodejs文档: https://nodejs.org/api/documentation.html


1. 常见的数据类型, 前3个可以作为类型转换函数  
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

    // 注意如果使用ES6匿名函数的语法无法使用this,即下面写法是错误的

    person.GetAge = () => {
        console.log(this.age)
    }

    // ES6增加了默认参数和剩余参数
    // 函数中剩余参数与python中的写法区别

    function test(name="aquarius", ...args){
        // 函数体内，如果两行语句没有写在一行，不需要加分号

        console.log(name)
        console.log(...args)
    }

    // 动态获取函数的参数,使用函数的arguments数组对象
    // arguments 为函数参数的一个数组, 可以用位置获取传入的参数, 不需要在创建函数就指定函数参数的名称
    // 下面是使用arguments的一个例子

    $shelper = {
        GetProperty: function(){
            var obj = arguments[0] || Object()
            var p = arguments[1] || ""
            var defaultValue = arguments[2] || ""
            return obj[p] || defaultValue
        },
        Math: {
            DF2Percent: function(a, b){
                return (a/b*100).toFixed((arguments[2] || 2)) + (arguments[3] || '%')
            }
        }
    }

    ```

2. 类型查询使用typeof关键字，区分Array与Object使用instanceof  
    ```javascript
    // 使用typeof获得的类型描述
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
3. 与python相似的迭代方法
    ```javascript
    // Array

    array = [1, 2, 3, 4]

    // i 为索引

    for(i in array){
        console.log(i)
    }

    // v 为元素

    for(v of array){
        console.log(v)
    }

    // Object
    // p 为对象成员的名称

    test = {1:2, 3:4}    
    for(p in test){
        console.log(p)
    }
    ```
4. JSON对象

    ```javascript
    // JSON
    // parse方法，将jsonstr转化为jsobj

    JSON.parse()
    // stringify方法，将jsobj转化成jsonstr

    JSON.stringify()
    ```
5. 数组排序
    ```javascript
    array = [2, 4, 1, 0, 9, 5]
    array.sort(function(a, b){return b - a})
    ```

6. 延时操作  
	```javascript
	
	setTimeout(function(){}, 3000)

	```

7. 常用函数

    ```js
    // 转化成url编码

    let uri = encodeURIComponent("aquarius")
    ```
