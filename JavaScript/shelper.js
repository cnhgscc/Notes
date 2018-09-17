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
