let obj1 = {
	'propA': 1,
	'propB': 2,
	'propC': 3,
	'propD': 4,
	'propE': 5
};

let obj2 = {
	'propA': 1
};

let obj3 = {
	'propB': 2
};

function nochecks(obj){
	var x = obj['propE'];
	obj['propE'] = 1337;
    return x;
}

for (let i = 0; i < 10000; i++) {
    nochecks(obj1);
}

console.log(nochecks(obj2));
console.log(nochecks(obj3));