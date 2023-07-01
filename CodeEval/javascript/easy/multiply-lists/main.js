// Code Eval - Multiply Lists
// https://www.codeeval.com/open_challenges/113/

var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
        line = line.split(" | ");
        var arr1 = line[0].split(" ").map(function(item){
          return parseInt(item);
        });
        var arr2 = line[1].split(" ").map(function(item){
          return parseInt(item);
        });
        line = "";
        for (var i = 0; i < arr1.length; i++) {
          line = line + (arr1[i]*arr2[i]) + " ";
        }
        console.log(line);
    }

});
