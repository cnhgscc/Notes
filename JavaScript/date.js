$Date = {
    date : new Date(),
    year: function(){
        return Number(this.date.getFullYear())
    },
    month: function(){
        return Number(this.date.getMonth()) + 1
    },

    day: function(){
        return Number(this.date.getDate())
    },
    Year: function(){
        return String(this.year())
    },
    Month: function(){
        if(this.month() < 10){
            return "0" + String(this.month())
        }else{
            return String(this.month())
        }
    },
    Day: function(){
        if(this.day() < 10){
            return "0" + String(this.day)
        }else{
            return String(this.day())
        }
    },
    strftime: function(){
        return this.Year() + "-" + this.Month() + "-" + this.Day()
    },
    GetFirstDay: function(){
        return this.Year() + "-" + this.Month() + "-" + "01"
    }
}