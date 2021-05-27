var readline = require('readline');
const PI = 3.1415926535897;

var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line',function(answer) {
  // TODO: Log the answer in a database
	var l = answer.split(" ").map(Number)
	var hp = (l.reduce((a,b) =>a+b))/2.0
	var tar = Math.sqrt(hp*(hp-l[0])*(hp-l[1])*(hp-l[2])) 
	var rad_min_cir = 2*tar/(l.reduce((a,b) =>a+b))
	var arminci = PI*Math.pow(rad_min_cir,2)
	var rad_max_cir = l.reduce((a,b) => a*b)/(4*tar)
	var armaxci = PI*Math.pow(rad_max_cir, 2)
	console.log((armaxci - tar).toFixed(4),(tar - arminci).toFixed(4), arminci.toFixed(4))
}).on('close', function(answer){
	rl.close()
});
