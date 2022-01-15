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

var literalcircle = {
	radius: 10,
	getarea: function() {
		//console.log(this);
		var self = this;
		var increaseradius = function () {
			this.radius = 20;   //when there is a function inside another function,while the outer function's this refers to the object/literal it is in the inner function's this refers to the global window
			self.radius = 20;
		};
		console.log(this.radius);
		increaseradius();
		return Math.PI * Math.pow(this.radius, 2);
	}
};

console.log(literalcircle.getarea());

var array = new Array();
array[0] = "yaakov";
array[1] = 2;
array[2] = function (name) {
	console.log(name);
};
array[3] = {course: "lfdkgjlfg"};

array[2]("Mishal");

var names = []; 

for (var i = 0; i<names.length; i++) {}

for (var yo in names) {
	console.log(names[yo]);
} 

// IIFEs
(function (window) {
	console.log("helloooooo");
	var amanda = 5;
	window.amanda = amanda;
})(window);




