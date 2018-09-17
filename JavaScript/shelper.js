$shelper = {
    GetProperty: function(){
        var obj = arguments[0] || Object()
        var p = arguments[1] || ""
        var defaultValue = arguments[2] || ""
        return obj[p] || defaultValue
    }
}
