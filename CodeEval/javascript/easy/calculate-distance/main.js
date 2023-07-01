// Code eval - Calculate distance
// https://www.codeeval.com/open_challenges/99/

var fs = require("fs");
fs.readFileSync(process.argv[2]).toString().split("\n").forEach(function(line){
    if (line != ""){
        var p1x = parseInt(line.split(") (")[0].split(", ")[0].replace(/[^\d.-]/g, ''));
        var p1y = parseInt(line.split(") (")[0].split(", ")[1].replace(/[^\d.-]/g, ''));
        var p2x = parseInt(line.split(") (")[1].split(", ")[0].replace(/[^\d.-]/g, ''));
        var p2y = parseInt(line.split(") (")[1].split(", ")[1].replace(/[^\d.-]/g, ''));
        console.log(Math.sqrt(Math.pow(p2x-p1x,2)+Math.pow(p2y-p1y,2)));

    }
});
