var x = "Hello World";

function a () {}

var a = function () {}

a();
function compare (x,y) {
	return x>y
}
var a = compare(4,5);
compare(4, "a");
compare();

var parameter = parameter || "whatever";

if (a == 5) {}
else {}

for (var i=0;i<10;i++) {}

var company = new Object();
company.name = "Facebook";
company.ceo = new Object();
company.ceo.firstname = "Mark";
console.log(company.name);
console.log(company);

// object literal
var insta = {
	name: "sdlkf",
	ceo: {
		firstname: "sdlkfj",
		favcolor: "sdflkj"
	},
	"stock of company": 110
};

function multiply(a,b) {
	return a*b;
}

multiply.version = "sdfsdf";
console.log(multiply.version);

function makemultiplier(multiply) {
	var myfunc = function(x) {
		return multiply * x;
	}
	return myfunc;
}
function dooperation(x, operation){
	return operation(X);
};
var multiplyby3 = makemultiplier(3);
console.log(multiplyby3(10));

function test() {
	console.log(this);
};
test();


function Circle (radius) {
	this.radius = radius;
	
}

Circle.prototype.getarea = function() {
	return Math.PI * Math.pow(this.radius, 2);
};

var mycircle = new Circle(10);
console.log(mycircle);



