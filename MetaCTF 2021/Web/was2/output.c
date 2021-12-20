export memory memory(initial: 256, max: 256);

global g_a:int = 5246800;
global g_b:int = 0;
global g_c:int = 0;

export table indirect_function_table:funcref(min: 20, max: 20);

data d_unsignedshortunsignedintfloa(offset: 1024) = 
  "unsigned short\00unsigned int\00float\00uint64_t\00unsigned char\00boo"
  "l\00emscripten::val\00unsigned long\00std::wstring\00std::string\00std"
  "::u16string\00std::u32string\00double\00void\00emscripten::memory_view"
  "<short>\00emscripten::memory_view<unsigned short>\00emscripten::memory"
  "_view<int>\00emscripten::memory_view<unsigned int>\00emscripten::memor"
  "y_view<float>\00emscripten::memory_view<uint8_t>\00emscripten::memory_"
  "view<int8_t>\00emscripten::memory_view<uint16_t>\00emscripten::memory_"
  "view<int16_t>\00emscripten::memory_view<uint32_t>\00emscripten::memory"
  "_view<int32_t>\00emscripten::memory_view<char>\00emscripten::memory_vi"
  "ew<unsigned char>\00std::basic_string<unsigned char>\00emscripten::mem"
  "ory_view<signed char>\00emscripten::memory_view<long>\00emscripten::me"
  "mory_view<unsigned long>\00emscripten::memory_view<double>\00NSt3__212"
  "basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE\00NSt3__221__bas"
  "ic_string_commonILb1EEE\00D\0c\00\00>\07\00\00\c8\0c\00\00\ff\06\00\00"
  "\00\00\00\00\01\00\00\00d\07\00\00\00\00\00\00NSt3__212basic_stringIhN"
  "S_11char_traitsIhEENS_9allocatorIhEEEE\00\00\c8\0c\00\00\84\07\00\00\00"
  "\00\00\00\01\00\00\00d\07\00\00\00\00\00\00NSt3__212basic_stringIwNS_1"
  "1char_traitsIwEENS_9allocatorIwEEEE\00\00\c8\0c\00\00\dc\07\00\00\00\00"
  "\00\00\01\00\00\00d\07\00\00\00\00\00\00NSt3__212basic_stringIDsNS_11c"
  "har_traitsIDsEENS_9allocatorIDsEEEE\00\00\00\c8\0c\00\004\08\00\00\00\00"
  "\00\00\01\00\00\00d\07\00\00\00\00\00\00NSt3__212basic_stringIDiNS_11c"
  "har_traitsIDiEENS_9allocatorIDiEEEE\00\00\00\c8\0c\00\00\90\08\00\00\00"
  "\00\00\00\01\00\00\00d\07\00\00\00\00\00\00N10emscripten3valE\00\00D\0c"
  "\00\00\ec\08\00\00N10emscripten11memory_viewIcEE\00\00D\0c\00\00\08\09"
  "\00\00N10emscripten11memory_viewIaEE\00\00D\0c\00\000\09\00\00N10emscr"
  "ipten11memory_viewIhEE\00\00D\0c\00\00X\09\00\00N10emscripten11memory_"
  "viewIsEE\00\00D\0c\00\00\80\09\00\00N10emscripten11memory_viewItEE\00\00"
  "D\0c\00\00\a8\09\00\00N10emscripten11memory_viewIiEE\00\00D\0c\00\00\d0"
  "\09\00\00N10emscripten11memory_viewIjEE\00\00D\0c\00\00\f8\09\00\00N10"
  "emscripten11memory_viewIlEE\00\00D\0c\00\00 \0a\00\00N10emscripten11me"
  "mory_viewImEE\00\00D\0c\00\00H\0a\00\00N10emscripten11memory_viewIfEE\00"
  "\00D\0c\00\00p\0a\00\00N10emscripten11memory_viewIdEE\00\00D\0c\00\00\98"
  "\0a\00\00St9type_info\00\00\00\00D\0c\00\00\c0\0a\00\00N10__cxxabiv116"
  "__shim_type_infoE\00\00\00\00l\0c\00\00\d8\0a\00\00\d0\0a\00\00N10__cx"
  "xabiv117__class_type_infoE\00\00\00l\0c\00\00\08\0b\00\00\fc\0a\00\00\00"
  "\00\00\00|\0b\00\00\02\00\00\00\03\00\00\00\04\00\00\00\05\00\00\00\06"
  "\00\00\00N10__cxxabiv123__fundamental_type_infoE\00l\0c\00\00T\0b\00\00"
  "\fc\0a\00\00v\00\00\00@\0b\00\00\88\0b\00\00b\00\00\00@\0b\00\00\94\0b"
  "\00\00c\00\00\00@\0b\00\00\a0\0b\00\00h\00\00\00@\0b\00\00\ac\0b\00\00"
  "a\00\00\00@\0b\00\00\b8\0b\00\00s\00\00\00@\0b\00\00\c4\0b\00\00t\00\00"
  "\00@\0b\00\00\d0\0b\00\00i\00\00\00@\0b\00\00\dc\0b\00\00j\00\00\00@\0b"
  "\00\00\e8\0b\00\00l\00\00\00@\0b\00\00\f4\0b\00\00m\00\00\00@\0b\00\00"
  "\00\0c\00\00x\00\00\00@\0b\00\00\0c\0c\00\00y\00\00\00@\0b\00\00\18\0c"
  "\00\00f\00\00\00@\0b\00\00$\0c\00\00d\00\00\00@\0b\00\000\0c\00\00\00\00"
  "\00\00,\0b\00\00\02\00\00\00\07\00\00\00\04\00\00\00\05\00\00\00\08\00"
  "\00\00\09\00\00\00\0a\00\00\00\0b\00\00\00\00\00\00\00\b4\0c\00\00\02\00"
  "\00\00\0c\00\00\00\04\00\00\00\05\00\00\00\08\00\00\00\0d\00\00\00\0e\00"
  "\00\00\0f\00\00\00N10__cxxabiv120__si_class_type_infoE\00\00\00\00l\0c"
  "\00\00\8c\0c\00\00,\0b\00\00\00\00\00\00\10\0d\00\00\02\00\00\00\10\00"
  "\00\00\04\00\00\00\05\00\00\00\08\00\00\00\11\00\00\00\12\00\00\00\13\00"
  "\00\00N10__cxxabiv121__vmi_class_type_infoE\00\00\00l\0c\00\00\e8\0c\00"
  "\00,\0b\00\00";
data d_ZkhCGvr6jgelzvPP(offset: 3360) = 
"Zk\82hC\G\84vr6j{@g\81e\85;lzv>\7fP\0fP\00";

import function env_embind_register(a:int, b:int);

import function env_embind_register_bool(a:int, b:int, c:int, d:int, e:int);

import function env_embind_register_string(a:int, b:int);

import function env_embind_register_wstring(a:int, b:int, c:int);

import function env_embind_register_emval(a:int, b:int);

import function env_embind_register_integer(a:int, b:int, c:int, d:int, e:int);

import function env_embind_register_float(a:int, b:int, c:int);

import function env_embind_register_memory_view(a:int, b:int, c:int);

import function env_emscripten_resize_heap(a:int):int;

import function env_emscripten_memcpy_big(a:int, b:int, c:int):int;

import function env_embind_register_bigint(a:int, b:int, c:int, d:int, e:int, f:int, g:int);

export function wasm_call_ctors() {
  emscripten_stack_init();
  f_ff();
}

export function checkFlag(a:int):int {
  var b:int = g_a;
  var c:int = 32;
  var d:int = b - c;
  g_a = d;
  d[6]:int = a;
  var e:int = d[6]:int;
  var f:int = f_sg(e);
  var g:int = 24;
  var h:int = f;
  var i:int = g;
  var j:int = h != i;
  var k:int = 1;
  var l:int = j & k;
  if (eqz(l)) goto B_b;
  var m:int = 0;
  d[7]:int = m;
  goto B_a;
  label B_b:
  var n:int = 5;
  d[5]:int = n;
  var o:int = 0;
  d[19]:byte = o;
  loop L_d {
    var p:int = d[19]:ubyte;
    var q:int = 24;
    var r:int = p << q;
    var s:int = r >> q;
    var t:int = 24;
    var u:int = s;
    var v:int = t;
    var w:int = u < v;
    var x:int = 1;
    var y:int = w & x;
    if (eqz(y)) goto B_c;
    var z:int = d[5]:int;
    var aa:int = 8;
    var ba:int = z + aa;
    d[5]:int = ba;
    var ca:int = d[5]:int;
    var da:int = 15;
    var ea:int = ca % da;
    d[3]:int = ea;
    var fa:int = d[19]:ubyte;
    var ga:int = 24;
    var ha:int = fa << ga;
    var ia:ubyte_ptr = ha >> ga;
    var ja:int = ia[3360];
    var ka:int = 24;
    var la:int = ja << ka;
    var ma:int = la >> ka;
    var na:int = d[3]:int;
    var oa:int = ma - na;
    d[11]:byte = oa;
    var pa:int = d[6]:int;
    var qa:int = d[19]:ubyte;
    var ra:int = 24;
    var sa:int = qa << ra;
    var ta:int = sa >> ra;
    var ua:ubyte_ptr = pa + ta;
    var va:int = ua[0];
    var wa:int = 24;
    var xa:int = va << wa;
    var ya:int = xa >> wa;
    var za:int = d[11]:ubyte;
    var ab:int = 24;
    var bb:int = za << ab;
    var cb:int = bb >> ab;
    var db:int = ya;
    var eb:int = cb;
    var fb:int = db != eb;
    var gb:int = 1;
    var hb:int = fb & gb;
    if (eqz(hb)) goto B_e;
    var ib:int = 0;
    d[7]:int = ib;
    goto B_a;
    label B_e:
    var jb:int = d[19]:ubyte;
    var kb:int = 1;
    var lb:int = jb + kb;
    d[19]:byte = lb;
    continue L_d;
  }
  unreachable;
  label B_c:
  var mb:int = 1;
  d[7]:int = mb;
  label B_a:
  var nb:int = d[7]:int;
  var ob:int = 32;
  var pb:int = d + ob;
  g_a = pb;
  return nb;
}

export function getTypeName(a:int):int {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = d[3];
  var f:int = f_o(e);
  var g:int = f_gf(f);
  var h:int = 16;
  var i:int = d + h;
  g_a = i;
  return g;
}

function f_o(a:int):int {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  d[2] = a;
  var e:int_ptr = d[2];
  var f:int = e[1];
  d[3] = f;
  var g:int = d[3];
  return g;
}

export function embind_register_native_and_builtin_types() {
  var a:int = f_q();
  var b:int = 1178;
  env_embind_register(a, b);
  var c:int = f_r();
  var d:int = 1081;
  var e:int = 1;
  var f:int = 1;
  var g:int = 0;
  var h:int = 1;
  var i:int = f & h;
  var j:int = 1;
  var k:int = g & j;
  env_embind_register_bool(c, d, e, i, k);
  var l:int = 1076;
  f_s(l);
  var m:int = 1069;
  f(m);
  var n:int = 1067;
  f_u(n);
  var o:int = 1033;
  f_v(o);
  var p:int = 1024;
  f_w(p);
  var q:int = 1048;
  f_x(q);
  var r:int = 1039;
  f_y(r);
  var s:int = 1111;
  f_z(s);
  var t:int = 1102;
  f_aa(t);
  var u:int = 1059;
  f_ba(u);
  var v:int = 1058;
  f_ca(v);
  var w:int = 1052;
  f_da(w);
  var x:int = 1171;
  f_ea(x);
  var y:int = f_fa();
  var z:int = 1129;
  env_embind_register_string(y, z);
  var aa:int = f_ga();
  var ba:int = 1620;
  env_embind_register_string(aa, ba);
  var ca:int = f_ha();
  var da:int = 4;
  var ea:int = 1116;
  env_embind_register_wstring(ca, da, ea);
  var fa:int = f_ia();
  var ga:int = 2;
  var ha:int = 1141;
  env_embind_register_wstring(fa, ga, ha);
  var ia:int = f_ja();
  var ja:int = 4;
  var ka:int = 1156;
  env_embind_register_wstring(ia, ja, ka);
  var la:int = f_ka();
  var ma:int = 1086;
  env_embind_register_emval(la, ma);
  var na:int = 1551;
  f_la(na);
  var oa:int = 1653;
  f_ma(oa);
  var pa:int = 1581;
  f_na(pa);
  var qa:int = 1183;
  f_oa(qa);
  var ra:int = 1214;
  f_pa(ra);
  var sa:int = 1254;
  f_qa(sa);
  var ta:int = 1283;
  f_ra(ta);
  var ua:int = 1690;
  f_sa(ua);
  var va:int = 1720;
  f_ta(va);
  var wa:int = 1385;
  f_ma(wa);
  var xa:int = 1352;
  f_na(xa);
  var ya:int = 1451;
  f_oa(ya);
  var za:int = 1417;
  f_pa(za);
  var ab:int = 1518;
  f_qa(ab);
  var bb:int = 1484;
  f_ra(bb);
  var cb:int = 1321;
  f_ua(cb);
  var db:int = 1759;
  f_va(db);
}

function f_q():int {
  var a:int = f_wa();
  return a;
}

function f_r():int {
  var a:int = f_xa();
  return a;
}

function f_s(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_ya();
  var f:int = d[3];
  var g:int = f_za();
  var h:int = 24;
  var i:int = g << h;
  var j:int = i >> h;
  var k:int = f_ab();
  var l:int = 24;
  var m:int = k << l;
  var n:int = m >> l;
  var o:int = 1;
  env_embind_register_integer(e, f, o, j, n);
  var p:int = 16;
  var q:int = d + p;
  g_a = q;
}

function f(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_bb();
  var f:int = d[3];
  var g:int = f_cb();
  var h:int = 24;
  var i:int = g << h;
  var j:int = i >> h;
  var k:int = f_db();
  var l:int = 24;
  var m:int = k << l;
  var n:int = m >> l;
  var o:int = 1;
  env_embind_register_integer(e, f, o, j, n);
  var p:int = 16;
  var q:int = d + p;
  g_a = q;
}

function f_u(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_eb();
  var f:int = d[3];
  var g:int = f_fb();
  var h:int = 255;
  var i:int = g & h;
  var j:int = f_gb();
  var k:int = 255;
  var l:int = j & k;
  var m:int = 1;
  env_embind_register_integer(e, f, m, i, l);
  var n:int = 16;
  var o:int = d + n;
  g_a = o;
}

function f_v(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_hb();
  var f:int = d[3];
  var g:int = f_ib();
  var h:int = 16;
  var i:int = g << h;
  var j:int = i >> h;
  var k:int = f_jb();
  var l:int = 16;
  var m:int = k << l;
  var n:int = m >> l;
  var o:int = 2;
  env_embind_register_integer(e, f, o, j, n);
  var p:int = 16;
  var q:int = d + p;
  g_a = q;
}

function f_w(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_kb();
  var f:int = d[3];
  var g:int = f_lb();
  var h:int = 65535;
  var i:int = g & h;
  var j:int = f_mb();
  var k:int = 65535;
  var l:int = j & k;
  var m:int = 2;
  env_embind_register_integer(e, f, m, i, l);
  var n:int = 16;
  var o:int = d + n;
  g_a = o;
}

function f_x(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_nb();
  var f:int = d[3];
  var g:int = f_ob();
  var h:int = f_pb();
  var i:int = 4;
  env_embind_register_integer(e, f, i, g, h);
  var j:int = 16;
  var k:int = d + j;
  g_a = k;
}

function f_y(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_qb();
  var f:int = d[3];
  var g:int = f_rb();
  var h:int = f_sb();
  var i:int = 4;
  env_embind_register_integer(e, f, i, g, h);
  var j:int = 16;
  var k:int = d + j;
  g_a = k;
}

function f_z(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_tb();
  var f:int = d[3];
  var g:int = f_ub();
  var h:int = f_vb();
  var i:int = 4;
  env_embind_register_integer(e, f, i, g, h);
  var j:int = 16;
  var k:int = d + j;
  g_a = k;
}

function f_aa(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_wb();
  var f:int = d[3];
  var g:int = f_xb();
  var h:int = f_yb();
  var i:int = 4;
  env_embind_register_integer(e, f, i, g, h);
  var j:int = 16;
  var k:int = d + j;
  g_a = k;
}

function f_ba(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_zb();
  var f:int = d[3];
  var j:long = f_ac();
  var k:long = f_bc();
  var g:int = 8;
  f_hh(e, f, g, j, k);
  var h:int = 16;
  var i:int = d + h;
  g_a = i;
}

function f_ca(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_cc();
  var f:int = d[3];
  var j:long = f_dc();
  var k:long = f_ec();
  var g:int = 8;
  f_hh(e, f, g, j, k);
  var h:int = 16;
  var i:int = d + h;
  g_a = i;
}

function f_da(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_fc();
  var f:int = d[3];
  var g:int = 4;
  env_embind_register_float(e, f, g);
  var h:int = 16;
  var i:int = d + h;
  g_a = i;
}

function f_ea(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_gc();
  var f:int = d[3];
  var g:int = 8;
  env_embind_register_float(e, f, g);
  var h:int = 16;
  var i:int = d + h;
  g_a = i;
}

function f_fa():int {
  var a:int = f_hc();
  return a;
}

function f_ga():int {
  var a:int = f_ic();
  return a;
}

function f_ha():int {
  var a:int = f_jc();
  return a;
}

function f_ia():int {
  var a:int = f_kc();
  return a;
}

function f_ja():int {
  var a:int = f_lc();
  return a;
}

function f_ka():int {
  var a:int = f_mc();
  return a;
}

function f_la(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_nc();
  var f:int = f_oc();
  var g:int = d[3];
  env_embind_register_memory_view(e, f, g);
  var h:int = 16;
  var i:int = d + h;
  g_a = i;
}

function f_ma(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_pc();
  var f:int = f_qc();
  var g:int = d[3];
  env_embind_register_memory_view(e, f, g);
  var h:int = 16;
  var i:int = d + h;
  g_a = i;
}

function f_na(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_rc();
  var f:int = f_sc();
  var g:int = d[3];
  env_embind_register_memory_view(e, f, g);
  var h:int = 16;
  var i:int = d + h;
  g_a = i;
}

function f_oa(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_tc();
  var f:int = f_uc();
  var g:int = d[3];
  env_embind_register_memory_view(e, f, g);
  var h:int = 16;
  var i:int = d + h;
  g_a = i;
}

function f_pa(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_vc();
  var f:int = f_wc();
  var g:int = d[3];
  env_embind_register_memory_view(e, f, g);
  var h:int = 16;
  var i:int = d + h;
  g_a = i;
}

function f_qa(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_xc();
  var f:int = f_yc();
  var g:int = d[3];
  env_embind_register_memory_view(e, f, g);
  var h:int = 16;
  var i:int = d + h;
  g_a = i;
}

function f_ra(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_zc();
  var f:int = f_ad();
  var g:int = d[3];
  env_embind_register_memory_view(e, f, g);
  var h:int = 16;
  var i:int = d + h;
  g_a = i;
}

function f_sa(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_bd();
  var f:int = f_cd();
  var g:int = d[3];
  env_embind_register_memory_view(e, f, g);
  var h:int = 16;
  var i:int = d + h;
  g_a = i;
}

function f_ta(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_dd();
  var f:int = f_ed();
  var g:int = d[3];
  env_embind_register_memory_view(e, f, g);
  var h:int = 16;
  var i:int = d + h;
  g_a = i;
}

function f_ua(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_fd();
  var f:int = f_gd();
  var g:int = d[3];
  env_embind_register_memory_view(e, f, g);
  var h:int = 16;
  var i:int = d + h;
  g_a = i;
}

function f_va(a:int) {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = f_hd();
  var f:int = f_id();
  var g:int = d[3];
  env_embind_register_memory_view(e, f, g);
  var h:int = 16;
  var i:int = d + h;
  g_a = i;
}

function f_wa():int {
  var a:int = 2956;
  var b:int = a;
  return b;
}

function f_xa():int {
  var a:int = 2968;
  var b:int = a;
  return b;
}

function f_ya():int {
  var a:int = f_ld();
  return a;
}

function f_za():int {
  var a:int = f_md();
  var b:int = 24;
  var c:int = a << b;
  var d:int = c >> b;
  return d;
}

function f_ab():int {
  var a:int = f_nd();
  var b:int = 24;
  var c:int = a << b;
  var d:int = c >> b;
  return d;
}

function f_bb():int {
  var a:int = f_od();
  return a;
}

function f_cb():int {
  var a:int = f_pd();
  var b:int = 24;
  var c:int = a << b;
  var d:int = c >> b;
  return d;
}

function f_db():int {
  var a:int = f_qd();
  var b:int = 24;
  var c:int = a << b;
  var d:int = c >> b;
  return d;
}

function f_eb():int {
  var a:int = f_rd();
  return a;
}

function f_fb():int {
  var a:int = f_sd();
  var b:int = 255;
  var c:int = a & b;
  return c;
}

function f_gb():int {
  var a:int = f_td();
  var b:int = 255;
  var c:int = a & b;
  return c;
}

function f_hb():int {
  var a:int = f_ud();
  return a;
}

function f_ib():int {
  var a:int = f_vd();
  var b:int = 16;
  var c:int = a << b;
  var d:int = c >> b;
  return d;
}

function f_jb():int {
  var a:int = f_wd();
  var b:int = 16;
  var c:int = a << b;
  var d:int = c >> b;
  return d;
}

function f_kb():int {
  var a:int = f_xd();
  return a;
}

function f_lb():int {
  var a:int = f_yd();
  var b:int = 65535;
  var c:int = a & b;
  return c;
}

function f_mb():int {
  var a:int = f_zd();
  var b:int = 65535;
  var c:int = a & b;
  return c;
}

function f_nb():int {
  var a:int = f_ae();
  return a;
}

function f_ob():int {
  var a:int = f_be();
  return a;
}

function f_pb():int {
  var a:int = f_ce();
  return a;
}

function f_qb():int {
  var a:int = f_de();
  return a;
}

function f_rb():int {
  var a:int = f_ee();
  return a;
}

function f_sb():int {
  var a:int = f_fe();
  return a;
}

function f_tb():int {
  var a:int = f_ge();
  return a;
}

function f_ub():int {
  var a:int = f_he();
  return a;
}

function f_vb():int {
  var a:int = f_ie();
  return a;
}

function f_wb():int {
  var a:int = f_je();
  return a;
}

function f_xb():int {
  var a:int = f_ke();
  return a;
}

function f_yb():int {
  var a:int = f_le();
  return a;
}

function f_zb():int {
  var a:int = f_me();
  return a;
}

function f_ac():long {
  var a:long = f_ne();
  return a;
}

function f_bc():long {
  var a:long = f_oe();
  return a;
}

function f_cc():int {
  var a:int = f_pe();
  return a;
}

function f_dc():long {
  var a:long = f_qe();
  return a;
}

function f_ec():long {
  var a:long = f_re();
  return a;
}

function f_fc():int {
  var a:int = f_se();
  return a;
}

function f_gc():int {
  var a:int = f_te();
  return a;
}

function f_hc():int {
  var a:int = 1900;
  var b:int = a;
  return b;
}

function f_ic():int {
  var a:int = 1988;
  var b:int = a;
  return b;
}

function f_jc():int {
  var a:int = 2076;
  var b:int = a;
  return b;
}

function f_kc():int {
  var a:int = 2168;
  var b:int = a;
  return b;
}

function f_lc():int {
  var a:int = 2260;
  var b:int = a;
  return b;
}

function f_mc():int {
  var a:int = 2304;
  var b:int = a;
  return b;
}

function f_nc():int {
  var a:int = f_ue();
  return a;
}

function f_oc():int {
  var a:int = 0;
  return a;
}

function f_pc():int {
  var a:int = f_ve();
  return a;
}

function f_qc():int {
  var a:int = 0;
  return a;
}

function f_rc():int {
  var a:int = f_we();
  return a;
}

function f_sc():int {
  var a:int = 1;
  return a;
}

function f_tc():int {
  var a:int = f_xe();
  return a;
}

function f_uc():int {
  var a:int = 2;
  return a;
}

function f_vc():int {
  var a:int = f_ye();
  return a;
}

function f_wc():int {
  var a:int = 3;
  return a;
}

function f_xc():int {
  var a:int = f_ze();
  return a;
}

function f_yc():int {
  var a:int = 4;
  return a;
}

function f_zc():int {
  var a:int = f_af();
  return a;
}

function f_ad():int {
  var a:int = 5;
  return a;
}

function f_bd():int {
  var a:int = f_bf();
  return a;
}

function f_cd():int {
  var a:int = 4;
  return a;
}

function f_dd():int {
  var a:int = f_cf();
  return a;
}

function f_ed():int {
  var a:int = 5;
  return a;
}

function f_fd():int {
  var a:int = f_df();
  return a;
}

function f_gd():int {
  var a:int = 6;
  return a;
}

function f_hd():int {
  var a:int = f_ef();
  return a;
}

function f_id():int {
  var a:int = 7;
  return a;
}

function f_jd() {
  var a:int = 3388;
  var b:int = 1;
  call_indirect(a, b);
}

function f_kd(a:int):int {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  g_a = d;
  d[3] = a;
  var e:int = d[3];
  embind_register_native_and_builtin_types();
  var f:int = 16;
  var g:int = d + f;
  g_a = g;
  return e;
}

function f_ld():int {
  var a:int = 2980;
  var b:int = a;
  return b;
}

function f_md():int {
  var a:int = 128;
  var b:int = 24;
  var c:int = a << b;
  var d:int = c >> b;
  return d;
}

function f_nd():int {
  var a:int = 127;
  var b:int = 24;
  var c:int = a << b;
  var d:int = c >> b;
  return d;
}

function f_od():int {
  var a:int = 3004;
  var b:int = a;
  return b;
}

function f_pd():int {
  var a:int = 128;
  var b:int = 24;
  var c:int = a << b;
  var d:int = c >> b;
  return d;
}

function f_qd():int {
  var a:int = 127;
  var b:int = 24;
  var c:int = a << b;
  var d:int = c >> b;
  return d;
}

function f_rd():int {
  var a:int = 2992;
  var b:int = a;
  return b;
}

function f_sd():int {
  var a:int = 0;
  var b:int = 255;
  var c:int = a & b;
  return c;
}

function f_td():int {
  var a:int = 255;
  var b:int = 255;
  var c:int = a & b;
  return c;
}

function f_ud():int {
  var a:int = 3016;
  var b:int = a;
  return b;
}

function f_vd():int {
  var a:int = 32768;
  var b:int = 16;
  var c:int = a << b;
  var d:int = c >> b;
  return d;
}

function f_wd():int {
  var a:int = 32767;
  var b:int = 16;
  var c:int = a << b;
  var d:int = c >> b;
  return d;
}

function f_xd():int {
  var a:int = 3028;
  var b:int = a;
  return b;
}

function f_yd():int {
  var a:int = 0;
  var b:int = 65535;
  var c:int = a & b;
  return c;
}

function f_zd():int {
  var a:int = 65535;
  var b:int = 65535;
  var c:int = a & b;
  return c;
}

function f_ae():int {
  var a:int = 3040;
  var b:int = a;
  return b;
}

function f_be():int {
  var a:int = -2147483648;
  return a;
}

function f_ce():int {
  var a:int = 2147483647;
  return a;
}

function f_de():int {
  var a:int = 3052;
  var b:int = a;
  return b;
}

function f_ee():int {
  var a:int = 0;
  return a;
}

function f_fe():int {
  var a:int = -1;
  return a;
}

function f_ge():int {
  var a:int = 3064;
  var b:int = a;
  return b;
}

function f_he():int {
  var a:int = -2147483648;
  return a;
}

function f_ie():int {
  var a:int = 2147483647;
  return a;
}

function f_je():int {
  var a:int = 3076;
  var b:int = a;
  return b;
}

function f_ke():int {
  var a:int = 0;
  return a;
}

function f_le():int {
  var a:int = -1;
  return a;
}

function f_me():int {
  var a:int = 3088;
  var b:int = a;
  return b;
}

function f_ne():long {
  var a:long = -9223372036854775808L;
  return a;
}

function f_oe():long {
  var a:long = 9223372036854775807L;
  return a;
}

function f_pe():int {
  var a:int = 3100;
  var b:int = a;
  return b;
}

function f_qe():long {
  var a:long = 0L;
  return a;
}

function f_re():long {
  var a:long = -1L;
  return a;
}

function f_se():int {
  var a:int = 3112;
  var b:int = a;
  return b;
}

function f_te():int {
  var a:int = 3124;
  var b:int = a;
  return b;
}

function f_ue():int {
  var a:int = 2344;
  var b:int = a;
  return b;
}

function f_ve():int {
  var a:int = 2384;
  var b:int = a;
  return b;
}

function f_we():int {
  var a:int = 2424;
  var b:int = a;
  return b;
}

function f_xe():int {
  var a:int = 2464;
  var b:int = a;
  return b;
}

function f_ye():int {
  var a:int = 2504;
  var b:int = a;
  return b;
}

function f_ze():int {
  var a:int = 2544;
  var b:int = a;
  return b;
}

function f_af():int {
  var a:int = 2584;
  var b:int = a;
  return b;
}

function f_bf():int {
  var a:int = 2624;
  var b:int = a;
  return b;
}

function f_cf():int {
  var a:int = 2664;
  var b:int = a;
  return b;
}

function f_df():int {
  var a:int = 2704;
  var b:int = a;
  return b;
}

function f_ef():int {
  var a:int = 2744;
  var b:int = a;
  return b;
}

function f_ff() {
  f_jd()
}

function f_gf(a:int):int {
  var c:int;
  var b:int;
  b = f_sg(a) + 1;
  c = malloc(b);
  if (c) goto B_a;
  return 0;
  label B_a:
  return f_qg(c, a, b);
}

function f_hf(a:int) {
  free(a)
}

function f_if(a:int):int {
  return a
}

function f_jf(a:{ a:ubyte, b:ubyte }, b:{ a:ubyte, b:ubyte }):int {
  var d:int;
  var c:int = b.a;
  d = a.a;
  if (eqz(d)) goto B_a;
  if (d != (c & 255)) goto B_a;
  loop L_b {
    c = b.b;
    d = a.b;
    if (eqz(d)) goto B_a;
    b = b + 1;
    a = a + 1;
    if (d == (c & 255)) continue L_b;
  }
  label B_a:
  return d - (c & 255);
}

function f_kf(a:int):int {
  f_if(a);
  return a;
}

function f_lf(a:int) {
}

function f_mf(a:int) {
}

function f_nf(a:int) {
  f_kf(a);
  f_hf(a);
}

function f_of(a:int) {
  f_kf(a);
  f_hf(a);
}

function f_pf(a:int) {
  f_kf(a);
  f_hf(a);
}

function f_qf(a:int) {
  f_kf(a);
  f_hf(a);
}

function f_rf(a:int, b:int, c:int):int {
  return f_sf(a, b, 0)
}

function f_sf(a:int_ptr, b:int_ptr, c:int):int {
  if (c) goto B_a;
  return a[1] == b[1];
  label B_a:
  if (a != b) goto B_b;
  return 1;
  label B_b:
  return eqz(f_jf(f_o(a), f_o(b)));
}

function f_tf(a:int, b:int_ptr, c:int_ptr):int {
  var d:int_ptr = g_a - 64;
  g_a = d;
  var e:int = 1;
  if (f_sf(a, b, 0)) goto B_a;
  e = 0;
  if (eqz(b)) goto B_a;
  e = 0;
  b = f_uf(b, 2812, 2860, 0);
  if (eqz(b)) goto B_a;
  f_rg(d + 8 | 4, 0, 52);
  d[14] = 1;
  d[5] = -1;
  d[4] = a;
  d[2] = b;
  call_indirect(b, d + 8, c[0], 1, (b[0])[7]:int);
  e = d[8];
  if (e != 1) goto B_b;
  c[0] = d[6];
  label B_b:
  e = e == 1;
  label B_a:
  g_a = d + 64;
  return e;
}

function f_uf(a:int_ptr, b:int, c:int, d:int):int {
  var e:int_ptr = g_a - 64;
  g_a = e;
  var f:int = a[0];
  var g:int_ptr = (f + -4)[0]:int;
  f = (f + -8)[0]:int;
  e[5] = d;
  e[4] = b;
  e[3] = a;
  e[2] = c;
  b = 0;
  f_rg(e + 24, 0, 39);
  a = a + f;
  if (eqz(f_sf(g, c, 0))) goto B_b;
  e[14] = 1;
  call_indirect(g, e + 8, a, a, 1, 0, (g[0])[5]:int);
  b = select_if(a, 0, e[8] == 1);
  goto B_a;
  label B_b:
  call_indirect(g, e + 8, a, 1, 0, (g[0])[6]:int);
  br_table[B_d, B_c, ..B_a](e[11])
  label B_d:
  b = 
    select_if(select_if(select_if(e[7], 0, e[10] == 1), 0, e[9] == 1),
              0,
              e[12] == 1);
  goto B_a;
  label B_c:
  if (e[8] == 1) goto B_e;
  if (e[12]) goto B_a;
  if (e[9] != 1) goto B_a;
  if (e[10] != 1) goto B_a;
  label B_e:
  b = e[6];
  label B_a:
  g_a = e + 64;
  return b;
}

function f_vf(a:int, b:int, c:int, d:int) {
  var e:int;
  e = b[4]:int;
  if (e) goto B_a;
  b[9]:int = 1;
  b[6]:int = d;
  b[4]:int = c;
  return ;
  label B_a:
  if (e != c) goto B_c;
  if (b[6]:int != 2) goto B_b;
  b[6]:int = d;
  return ;
  label B_c:
  b[54]:byte = 1;
  b[6]:int = 2;
  b[9]:int = b[9]:int + 1;
  label B_b:
}

function f_wf(a:int, b:int_ptr, c:int, d:int) {
  if (eqz(f_sf(a, b[2], 0))) goto B_a;
  f_vf(b, b, c, d);
  label B_a:
}

function f_xf(a:int_ptr, b:int_ptr, c:int, d:int) {
  if (eqz(f_sf(a, b[2], 0))) goto B_a;
  f_vf(b, b, c, d);
  return ;
  label B_a:
  a = a[2];
  call_indirect(a, b, c, d, (a[0])[7]:int);
}

function f_yf(a:{ a:int, b:int }, b:int, c:int_ptr, d:int) {
  var f:int;
  var e:int = a.b;
  if (c) goto B_b;
  f = 0;
  goto B_a;
  label B_b:
  f = e >> 8;
  if (eqz(e & 1)) goto B_a;
  f = f_zf(c[0], f);
  label B_a:
  a = a.a;
  call_indirect(a, b, c + f, select_if(d, 2, e & 2), a.a[7]:int);
}

function f_zf(a:int, b:int):int {
  return (a + b)[0]:int
}

function f_ag(a:int_ptr, b:int, c:int, d:int) {
  if (eqz(f_sf(a, b[2]:int, 0))) goto B_a;
  f_vf(a, b, c, d);
  return ;
  label B_a:
  var e:int = a[3];
  var f:int = a + 16;
  f_yf(f, b, c, d);
  if (e < 2) goto B_b;
  e = f + (e << 3);
  a = a + 24;
  loop L_c {
    f_yf(a, b, c, d);
    if (b[54]:ubyte) goto B_b;
    a = a + 8;
    if (a < e) continue L_c;
  }
  label B_b:
}

function f_bg(a:int, b:int, c:int, d:int, e:int) {
  b[53]:byte = 1;
  if (b[1]:int != d) goto B_a;
  b[52]:byte = 1;
  d = b[4]:int;
  if (d) goto B_c;
  b[9]:int = 1;
  b[6]:int = e;
  b[4]:int = c;
  if (b[12]:int != 1) goto B_a;
  if (e == 1) goto B_b;
  goto B_a;
  label B_c:
  if (d != c) goto B_d;
  d = b[6]:int;
  if (d != 2) goto B_e;
  b[6]:int = e;
  d = e;
  label B_e:
  if (b[12]:int != 1) goto B_a;
  if (d == 1) goto B_b;
  goto B_a;
  label B_d:
  b[9]:int = b[9]:int + 1;
  label B_b:
  b[54]:byte = 1;
  label B_a:
}

function f_cg(a:int, b:int_ptr, c:int, d:int) {
  if (b[1] != c) goto B_a;
  if (b[7] == 1) goto B_a;
  b[7] = d;
  label B_a:
}

function f_dg(a:int, b:int, c:int, d:int, e:int) {
  var i:int;
  var f:int;
  if (eqz(f_sf(a, b[2]:int, e))) goto B_a;
  f_cg(b, b, c, d);
  return ;
  label B_a:
  if (eqz(f_sf(a, b[0]:int, e))) goto B_c;
  if (b[4]:int == c) goto B_e;
  if (b[5]:int != c) goto B_d;
  label B_e:
  if (d != 1) goto B_b;
  b[8]:int = 1;
  return ;
  label B_d:
  b[8]:int = d;
  if (b[11]:int == 4) goto B_f;
  f = a + 16;
  d = f + (a[3]:int << 3);
  var g:int = 0;
  var h:int = 0;
  loop L_j {
    if (f >= d) goto B_i;
    b[26]:short = 0;
    f_eg(f, b, c, c, 1, e);
    if (b[54]:ubyte) goto B_i;
    if (eqz(b[53]:ubyte)) goto B_k;
    if (eqz(b[52]:ubyte)) goto B_l;
    i = 1;
    if (b[6]:int == 1) goto B_h;
    g = 1;
    h = 1;
    i = 1;
    if (a[8]:ubyte & 2) goto B_k;
    goto B_h;
    label B_l:
    g = 1;
    i = h;
    if (eqz(a[8]:ubyte & 1)) goto B_h;
    label B_k:
    f = f + 8;
    continue L_j;
  }
  unreachable;
  label B_i:
  f = 4;
  i = h;
  if (eqz(g & 1)) goto B_g;
  label B_h:
  f = 3;
  label B_g:
  b[11]:int = f;
  if (i & 1) goto B_b;
  label B_f:
  b[5]:int = c;
  b[10]:int = b[10]:int + 1;
  if (b[9]:int != 1) goto B_b;
  if (b[6]:int != 2) goto B_b;
  b[54]:byte = 1;
  return ;
  label B_c:
  f = a[3]:int;
  i = a + 16;
  f_fg(i, b, c, d, e);
  if (f < 2) goto B_b;
  i = i + (f << 3);
  f = a + 24;
  a = a[2]:int;
  if (a & 2) goto B_n;
  if (b[9]:int != 1) goto B_m;
  label B_n:
  loop L_o {
    if (b[54]:ubyte) goto B_b;
    f_fg(f, b, c, d, e);
    f = f + 8;
    if (f < i) continue L_o;
    goto B_b;
  }
  unreachable;
  label B_m:
  if (a & 1) goto B_p;
  loop L_q {
    if (b[54]:ubyte) goto B_b;
    if (b[9]:int == 1) goto B_b;
    f_fg(f, b, c, d, e);
    f = f + 8;
    if (f < i) continue L_q;
    goto B_b;
  }
  unreachable;
  label B_p:
  loop L_r {
    if (b[54]:ubyte) goto B_b;
    if (b[9]:int != 1) goto B_s;
    if (b[6]:int == 1) goto B_b;
    label B_s:
    f_fg(f, b, c, d, e);
    f = f + 8;
    if (f < i) continue L_r;
  }
  label B_b:
}

function f_eg(a:{ a:int, b:int }, b:int, c:int, d:int_ptr, e:int, f:int) {
  var g:int = a.b;
  var h:int = g >> 8;
  if (eqz(g & 1)) goto B_a;
  h = f_zf(d[0], h);
  label B_a:
  a = a.a;
  call_indirect(a, b, c, d + h, select_if(e, 2, g & 2), f, a.a[5]:int);
}

function f_fg(a:{ a:int, b:int }, b:int, c:int_ptr, d:int, e:int) {
  var f:int = a.b;
  var g:int = f >> 8;
  if (eqz(f & 1)) goto B_a;
  g = f_zf(c[0], g);
  label B_a:
  a = a.a;
  call_indirect(a, b, c + g, select_if(d, 2, f & 2), e, a.a[6]:int);
}

function f_gg(a:int_ptr, b:int, c:int, d:int, e:int) {
  if (eqz(f_sf(a, b[2]:int, e))) goto B_a;
  f_cg(b, b, c, d);
  return ;
  label B_a:
  if (eqz(f_sf(a, b[0]:int, e))) goto B_c;
  if (b[4]:int == c) goto B_e;
  if (b[5]:int != c) goto B_d;
  label B_e:
  if (d != 1) goto B_b;
  b[8]:int = 1;
  return ;
  label B_d:
  b[8]:int = d;
  if (b[11]:int == 4) goto B_f;
  b[26]:short = 0;
  a = a[2];
  call_indirect(a, b, c, c, 1, e, (a[0])[5]:int);
  if (eqz(b[53]:ubyte)) goto B_g;
  b[11]:int = 3;
  if (eqz(b[52]:ubyte)) goto B_f;
  goto B_b;
  label B_g:
  b[11]:int = 4;
  label B_f:
  b[5]:int = c;
  b[10]:int = b[10]:int + 1;
  if (b[9]:int != 1) goto B_b;
  if (b[6]:int != 2) goto B_b;
  b[54]:byte = 1;
  return ;
  label B_c:
  a = a[2];
  call_indirect(a, b, c, d, e, (a[0])[6]:int);
  label B_b:
}

function f_hg(a:int, b:int, c:int, d:int, e:int) {
  if (eqz(f_sf(a, b[2]:int, e))) goto B_a;
  f_cg(b, b, c, d);
  return ;
  label B_a:
  if (eqz(f_sf(a, b[0]:int, e))) goto B_b;
  if (b[4]:int == c) goto B_d;
  if (b[5]:int != c) goto B_c;
  label B_d:
  if (d != 1) goto B_b;
  b[8]:int = 1;
  return ;
  label B_c:
  b[5]:int = c;
  b[8]:int = d;
  b[10]:int = b[10]:int + 1;
  if (b[9]:int != 1) goto B_e;
  if (b[6]:int != 2) goto B_e;
  b[54]:byte = 1;
  label B_e:
  b[11]:int = 4;
  label B_b:
}

function f_ig(a:int, b:int, c:int, d:int, e:int, f:int) {
  var k:int;
  var l:int;
  if (eqz(f_sf(a, b[2]:int, f))) goto B_a;
  f_bg(b, b, c, d, e);
  return ;
  label B_a:
  var g:int = b[53]:ubyte;
  var h:int = a[3]:int;
  b[53]:byte = 0;
  var i:int = b[52]:ubyte;
  b[52]:byte = 0;
  var j:int = a + 16;
  f_eg(j, b, c, d, e, f);
  g = g | (k = b[53]:ubyte);
  i = i | (l = b[52]:ubyte);
  if (h < 2) goto B_b;
  j = j + (h << 3);
  h = a + 24;
  loop L_c {
    if (b[54]:ubyte) goto B_b;
    if (eqz(l & 255)) goto B_e;
    if (b[6]:int == 1) goto B_b;
    if (a[8]:ubyte & 2) goto B_d;
    goto B_b;
    label B_e:
    if (eqz(k & 255)) goto B_d;
    if (eqz(a[8]:ubyte & 1)) goto B_b;
    label B_d:
    b[26]:short = 0;
    f_eg(h, b, c, d, e, f);
    k = b[53]:ubyte;
    g = k | g;
    l = b[52]:ubyte;
    i = l | i;
    h = h + 8;
    if (h < j) continue L_c;
  }
  label B_b:
  b[53]:byte = (g & 255) != 0;
  b[52]:byte = (i & 255) != 0;
}

function f_jg(a:int_ptr, b:int_ptr, c:int, d:int, e:int, f:int) {
  if (eqz(f_sf(a, b[2], f))) goto B_a;
  f_bg(b, b, c, d, e);
  return ;
  label B_a:
  a = a[2];
  call_indirect(a, b, c, d, e, f, (a[0])[5]:int);
}

function f_kg(a:int, b:int_ptr, c:int, d:int, e:int, f:int) {
  if (eqz(f_sf(a, b[2], f))) goto B_a;
  f_bg(b, b, c, d, e);
  label B_a:
}

export function errno_location():int {
  return 3392
}

export function malloc(a:int):int {
  var d:int;
  var e:int;
  var h:int;
  var f:{ a:int, b:int, c:int, d:int, e:int }
  var g:int;
  var c:{ a:int, b:int, c:int, d:int, e:int, f:int, g:int, h:int }
  var i:int;
  var l:int_ptr;
  var j:int_ptr;
  var k:int_ptr;
  var b:int = g_a - 16;
  g_a = b;
  if (a > 244) goto B_l;
  c = 0[849]:int;
  a = c >> (e = (d = select_if(16, a + 11 & -8, a < 11)) >> 3);
  if (eqz(a & 3)) goto B_m;
  f = ((a ^ -1) & 1) + e;
  g = f << 3;
  e = (g + 3444)[0]:int;
  a = e + 8;
  d = e[2]:int;
  if (d != (g = g + 3436)) goto B_o;
  0[849]:int = c & -2 << f;
  goto B_n;
  label B_o:
  d[3]:int = g;
  g[2]:int = d;
  label B_n:
  e[1]:int = (f = f << 3) | 3;
  e = e + f;
  e[1]:int = e[1]:int | 1;
  goto B_a;
  label B_m:
  if (d <= (h = 0[851]:int)) goto B_k;
  if (eqz(a)) goto B_p;
  a = a << e & ((a = 2 << e) | 0 - a);
  a = (a & 0 - a) + -1;
  e = a >> (a = a >> 12 & 16);
  f = e >> 5 & 8;
  f = 
    ((((f | a) | (e = (a = e >> f) >> 2 & 4)) | (e = (a = a >> e) >> 1 & 2)) | 
     (e = (a = a >> e) >> 1 & 1)) + 
    (a >> e);
  g = f << 3;
  e = (g + 3444)[0]:int;
  a = e[2]:int;
  if (a != (g = g + 3436)) goto B_r;
  0[849]:int = (c = c & -2 << f);
  goto B_q;
  label B_r:
  a[3]:int = g;
  g[2]:int = a;
  label B_q:
  a = e + 8;
  e[1]:int = d | 3;
  g = e + d;
  g[1]:int = (f = (i = f << 3) - d) | 1;
  (e + i)[0]:int = f;
  if (eqz(h)) goto B_s;
  i = h >> 3;
  d = (i << 3) + 3436;
  e = 0[854]:int;
  if (c & (i = 1 << i)) goto B_u;
  0[849]:int = c | i;
  i = d;
  goto B_t;
  label B_u:
  i = d[2]:int;
  label B_t:
  d[2]:int = e;
  i[3]:int = e;
  e[3]:int = d;
  e[2]:int = i;
  label B_s:
  0[854]:int = g;
  0[851]:int = f;
  goto B_a;
  label B_p:
  j = 0[850]:int;
  if (eqz(j)) goto B_k;
  a = (j & 0 - j) + -1;
  e = a >> (a = a >> 12 & 16);
  f = e >> 5 & 8;
  g = 
    ((((((f | a) | (e = (a = e >> f) >> 2 & 4)) | (e = (a = a >> e) >> 1 & 2)) | 
       (e = (a = a >> e) >> 1 & 1)) + 
      (a >> e) << 
      2) + 
     3700)[0]:int;
  e = (g[1]:int & -8) - d;
  f = g;
  loop L_w {
    a = f.e;
    if (a) goto B_x;
    a = (f + 20)[0]:int;
    if (eqz(a)) goto B_v;
    label B_x:
    f = (a[1]:int & -8) - d;
    e = select_if(f, e, f = f < e);
    g = select_if(a, g, f);
    f = a;
    continue L_w;
  }
  unreachable;
  label B_v:
  k = g[6]:int;
  i = g[3]:int;
  if (i == g) goto B_y;
  0[853]:int > (a = g[2]:int);
  a[3]:int = i;
  i[2]:int = a;
  goto B_b;
  label B_y:
  f = g + 20;
  a = f.a;
  if (a) goto B_z;
  a = g[4]:int;
  if (eqz(a)) goto B_j;
  f = g + 16;
  label B_z:
  loop L_aa {
    l = f;
    i = a;
    f = i + 20;
    a = f.a;
    if (a) continue L_aa;
    f = i + 16;
    a = i[4]:int;
    if (a) continue L_aa;
  }
  l[0] = 0;
  goto B_b;
  label B_l:
  d = -1;
  if (a > -65) goto B_k;
  a = a + 11;
  d = a & -8;
  h = 0[850]:int;
  if (eqz(h)) goto B_k;
  l = 0;
  if (d < 256) goto B_ba;
  l = 31;
  if (d > 16777215) goto B_ba;
  a = a >> 8;
  e = a << (a = a + 1048320 >> 16 & 8);
  f = e << (e = e + 520192 >> 16 & 4);
  a = ((f << (f = f + 245760 >> 16 & 2)) >> 15) - ((a | e) | f);
  l = (a << 1 | (d >> a + 21 & 1)) + 28;
  label B_ba:
  e = 0 - d;
  f = ((l << 2) + 3700)[0]:int;
  if (f) goto B_fa;
  a = 0;
  i = 0;
  goto B_ea;
  label B_fa:
  a = 0;
  g = d << select_if(0, 25 - (l >> 1), l == 31);
  i = 0;
  loop L_ga {
    c = (f.b & -8) - d;
    if (c >= e) goto B_ha;
    e = c;
    i = f;
    if (c) goto B_ha;
    e = 0;
    i = f;
    a = f;
    goto B_da;
    label B_ha:
    a = select_if(select_if(a,
                            c = (f + 20)[0]:int,
                            c == (f = (f + (g >> 29 & 4) + 16)[0]:int)),
                  a,
                  c);
    g = g << 1;
    if (f) continue L_ga;
  }
  label B_ea:
  if (a | i) goto B_ia;
  i = 0;
  a = 2 << l;
  a = (a | 0 - a) & h;
  if (eqz(a)) goto B_k;
  a = (a & 0 - a) + -1;
  f = a >> (a = a >> 12 & 16);
  g = f >> 5 & 8;
  a = 
    ((((((g | a) | (f = (a = f >> g) >> 2 & 4)) | (f = (a = a >> f) >> 1 & 2)) | 
       (f = (a = a >> f) >> 1 & 1)) + 
      (a >> f) << 
      2) + 
     3700)[0]:int;
  label B_ia:
  if (eqz(a)) goto B_ca;
  label B_da:
  loop L_ja {
    c = (a[1]:int & -8) - d;
    g = c < e;
    f = a[4]:int;
    if (f) goto B_ka;
    f = (a + 20)[0]:int;
    label B_ka:
    e = select_if(c, e, g);
    i = select_if(a, i, g);
    a = f;
    if (f) continue L_ja;
  }
  label B_ca:
  if (eqz(i)) goto B_k;
  if (e >= 0[851]:int - d) goto B_k;
  l = i[6]:int;
  g = i[3]:int;
  if (g == i) goto B_la;
  0[853]:int > (a = i[2]:int);
  a[3]:int = g;
  g[2]:int = a;
  goto B_c;
  label B_la:
  f = i + 20;
  a = f.a;
  if (a) goto B_ma;
  a = i[4]:int;
  if (eqz(a)) goto B_i;
  f = i + 16;
  label B_ma:
  loop L_na {
    c = f;
    g = a;
    f = g + 20;
    a = f.a;
    if (a) continue L_na;
    f = g + 16;
    a = g[4]:int;
    if (a) continue L_na;
  }
  c.a = 0;
  goto B_c;
  label B_k:
  a = 0[851]:int;
  if (a < d) goto B_oa;
  e = 0[854]:int;
  f = a - d;
  if (f < 16) goto B_qa;
  0[851]:int = f;
  0[854]:int = (g = e + d);
  g[1]:int = f | 1;
  (e + a)[0]:int = f;
  e[1]:int = d | 3;
  goto B_pa;
  label B_qa:
  0[854]:int = 0;
  0[851]:int = 0;
  e[1]:int = a | 3;
  a = e + a;
  a[1]:int = a[1]:int | 1;
  label B_pa:
  a = e + 8;
  goto B_a;
  label B_oa:
  g = 0[852]:int;
  if (g <= d) goto B_ra;
  0[852]:int = (e = g - d);
  0[855]:int = (f = (a = 0[855]:int) + d);
  f.b = e | 1;
  a[1]:int = d | 3;
  a = a + 8;
  goto B_a;
  label B_ra:
  if (eqz(0[967]:int)) goto B_ta;
  e = 0[969]:int;
  goto B_sa;
  label B_ta:
  0[970]:long@4 = -1L;
  0[968]:long@4 = 17592186048512L;
  0[967]:int = (b + 12 & -16) ^ 1431655768;
  0[972]:int = 0;
  0[960]:int = 0;
  e = 4096;
  label B_sa:
  a = 0;
  c = e + (h = d + 47);
  i = c & (l = 0 - e);
  if (i <= d) goto B_a;
  a = 0;
  e = 0[959]:int;
  if (eqz(e)) goto B_ua;
  f = 0[957]:int;
  j = f + i;
  if (j <= f) goto B_a;
  if (j > e) goto B_a;
  label B_ua:
  if (0[3840]:ubyte & 4) goto B_f;
  e = 0[855]:int;
  if (eqz(e)) goto B_xa;
  a = 3844;
  loop L_ya {
    f = a[0]:int;
    if (f > e) goto B_za;
    if (f + a[1]:int > e) goto B_wa;
    label B_za:
    a = a[2]:int;
    if (a) continue L_ya;
  }
  label B_xa:
  g = f_pg(0);
  if (g == -1) goto B_g;
  c = i;
  a = 0[968]:int;
  e = a + -1;
  if (eqz(e & g)) goto B_ab;
  c = i - g + (e + g & 0 - a);
  label B_ab:
  if (c <= d) goto B_g;
  if (c > 2147483646) goto B_g;
  a = 0[959]:int;
  if (eqz(a)) goto B_bb;
  e = 0[957]:int;
  f = e + c;
  if (f <= e) goto B_g;
  if (f > a) goto B_g;
  label B_bb:
  a = f_pg(c);
  if (a != g) goto B_va;
  goto B_e;
  label B_wa:
  c = c - g & l;
  if (c > 2147483646) goto B_g;
  g = f_pg(c);
  if (g == a[0]:int + a[1]:int) goto B_h;
  a = g;
  label B_va:
  if (a == -1) goto B_cb;
  if (d + 48 <= c) goto B_cb;
  e = h - c + (e = 0[969]:int) & 0 - e;
  if (e <= 2147483646) goto B_db;
  g = a;
  goto B_e;
  label B_db:
  if (f_pg(e) == -1) goto B_eb;
  c = e + c;
  g = a;
  goto B_e;
  label B_eb:
  f_pg(0 - c);
  goto B_g;
  label B_cb:
  g = a;
  if (a != -1) goto B_e;
  goto B_g;
  label B_j:
  i = 0;
  goto B_b;
  label B_i:
  g = 0;
  goto B_c;
  label B_h:
  if (g != -1) goto B_e;
  label B_g:
  0[960]:int = 0[960]:int | 4;
  label B_f:
  if (i > 2147483646) goto B_d;
  g = f_pg(i);
  a = f_pg(0);
  if (g == -1) goto B_d;
  if (a == -1) goto B_d;
  if (g >= a) goto B_d;
  c = a - g;
  if (c <= d + 40) goto B_d;
  label B_e:
  0[957]:int = (a = 0[957]:int + c);
  if (a <= 0[958]:int) goto B_fb;
  0[958]:int = a;
  label B_fb:
  e = 0[855]:int;
  if (eqz(e)) goto B_jb;
  a = 3844;
  loop L_kb {
    if (g == (f = a[0]:int) + (i = a[1]:int)) goto B_ib;
    a = a[2]:int;
    if (a) continue L_kb;
    goto B_hb;
  }
  unreachable;
  label B_jb:
  a = 0[853]:int;
  if (eqz(a)) goto B_mb;
  if (g >= a) goto B_lb;
  label B_mb:
  0[853]:int = g;
  label B_lb:
  a = 0;
  0[962]:int = c;
  0[961]:int = g;
  0[857]:int = -1;
  0[858]:int = 0[967]:int;
  0[964]:int = 0;
  loop L_nb {
    e = a << 3;
    (e + 3444)[0]:int = (f = e + 3436);
    (e + 3448)[0]:int = f;
    a = a + 1;
    if (a != 32) continue L_nb;
  }
  0[852]:int = 
    (f = (a = c + -40) - (e = select_if(-8 - g & 7, 0, g + 8 & 7)));
  0[855]:int = (e = g + e);
  e[1]:int = f | 1;
  (g + a)[1]:int = 40;
  0[856]:int = 0[971]:int;
  goto B_gb;
  label B_ib:
  if (a[12]:ubyte & 8) goto B_hb;
  if (f > e) goto B_hb;
  if (g <= e) goto B_hb;
  a[1]:int = i + c;
  0[855]:int = (f = e + (a = select_if(-8 - e & 7, 0, e + 8 & 7)));
  0[852]:int = (a = (g = 0[852]:int + c) - a);
  f.b = a | 1;
  (e + g)[1]:int = 40;
  0[856]:int = 0[971]:int;
  goto B_gb;
  label B_hb:
  if (g >= (i = 0[853]:int)) goto B_ob;
  0[853]:int = g;
  i = g;
  label B_ob:
  f = g + c;
  a = 3844;
  loop L_wb {
    if (a[0]:int == f) goto B_vb;
    a = a[2]:int;
    if (a) continue L_wb;
    goto B_ub;
  }
  unreachable;
  label B_vb:
  if (eqz(a[12]:ubyte & 8)) goto B_tb;
  label B_ub:
  a = 3844;
  loop L_xb {
    f = a[0]:int;
    if (f > e) goto B_yb;
    f = f + a[1]:int;
    if (f > e) goto B_sb;
    label B_yb:
    a = a[2]:int;
    continue L_xb;
  }
  unreachable;
  label B_tb:
  a[0]:int = g;
  a[1]:int = a[1]:int + c;
  l = g + select_if(-8 - g & 7, 0, g + 8 & 7);
  l[1] = d | 3;
  c = f + select_if(-8 - f & 7, 0, f + 8 & 7);
  f = c - (d = l + d);
  if (e != c) goto B_zb;
  0[855]:int = d;
  0[852]:int = (a = 0[852]:int + f);
  d[1]:int = a | 1;
  goto B_qb;
  label B_zb:
  if (0[854]:int != c) goto B_ac;
  0[854]:int = d;
  0[851]:int = (a = 0[851]:int + f);
  d[1]:int = a | 1;
  (d + a)[0]:int = a;
  goto B_qb;
  label B_ac:
  a = c.b;
  if ((a & 3) != 1) goto B_bc;
  h = a & -8;
  if (a > 255) goto B_dc;
  e = c.c;
  e == (g = ((i = a >> 3) << 3) + 3436);
  a = c.d;
  if (a != e) goto B_ec;
  0[849]:int = 0[849]:int & -2 << i;
  goto B_cc;
  label B_ec:
  a == g;
  e[3]:int = a;
  a[2]:int = e;
  goto B_cc;
  label B_dc:
  j = c.g;
  g = c.d;
  if (g == c) goto B_gc;
  i > (a = c.c);
  a[3]:int = g;
  g[2]:int = a;
  goto B_fc;
  label B_gc:
  a = c + 20;
  e = a[0]:int;
  if (e) goto B_hc;
  a = c + 16;
  e = a[0]:int;
  if (e) goto B_hc;
  g = 0;
  goto B_fc;
  label B_hc:
  loop L_ic {
    i = a;
    g = e;
    a = g + 20;
    e = a[0]:int;
    if (e) continue L_ic;
    a = g + 16;
    e = g[4]:int;
    if (e) continue L_ic;
  }
  i[0]:int = 0;
  label B_fc:
  if (eqz(j)) goto B_cc;
  e = c.h;
  a = (e << 2) + 3700;
  if (a[0]:int != c) goto B_kc;
  a[0]:int = g;
  if (g) goto B_jc;
  0[850]:int = 0[850]:int & -2 << e;
  goto B_cc;
  label B_kc:
  (j + select_if(16, 20, j[4] == c))[0]:int = g;
  if (eqz(g)) goto B_cc;
  label B_jc:
  g[6]:int = j;
  a = c.e;
  if (eqz(a)) goto B_lc;
  g[4]:int = a;
  a[6]:int = g;
  label B_lc:
  a = c.f;
  if (eqz(a)) goto B_cc;
  (g + 20)[0]:int = a;
  a[6]:int = g;
  label B_cc:
  f = h + f;
  c = c + h;
  label B_bc:
  c.b = c.b & -2;
  d[1]:int = f | 1;
  (d + f)[0]:int = f;
  if (f > 255) goto B_mc;
  e = f >> 3;
  a = (e << 3) + 3436;
  f = 0[849]:int;
  if (f & (e = 1 << e)) goto B_oc;
  0[849]:int = f | e;
  e = a;
  goto B_nc;
  label B_oc:
  e = a[2]:int;
  label B_nc:
  a[2]:int = d;
  e[3]:int = d;
  d[3]:int = a;
  d[2]:int = e;
  goto B_qb;
  label B_mc:
  a = 31;
  if (f > 16777215) goto B_pc;
  a = f >> 8;
  e = a << (a = a + 1048320 >> 16 & 8);
  g = e << (e = e + 520192 >> 16 & 4);
  a = ((g << (g = g + 245760 >> 16 & 2)) >> 15) - ((a | e) | g);
  a = (a << 1 | (f >> a + 21 & 1)) + 28;
  label B_pc:
  d[7]:int = a;
  d[4]:long@4 = 0L;
  e = (a << 2) + 3700;
  g = 0[850]:int;
  if (g & (i = 1 << a)) goto B_rc;
  0[850]:int = g | i;
  e[0]:int = d;
  d[6]:int = e;
  goto B_qc;
  label B_rc:
  a = f << select_if(0, 25 - (a >> 1), a == 31);
  g = e[0]:int;
  loop L_sc {
    e = g;
    if ((e[1]:int & -8) == f) goto B_rb;
    g = a >> 29;
    a = a << 1;
    i = e + (g & 4) + 16;
    g = i[0]:int;
    if (g) continue L_sc;
  }
  i[0]:int = d;
  d[6]:int = e;
  label B_qc:
  d[3]:int = d;
  d[2]:int = d;
  goto B_qb;
  label B_sb:
  0[852]:int = 
    (l = (a = c + -40) - (i = select_if(-8 - g & 7, 0, g + 8 & 7)));
  0[855]:int = (i = g + i);
  i[1]:int = l | 1;
  (g + a)[1]:int = 40;
  0[856]:int = 0[971]:int;
  i = select_if(e,
                a = f + select_if(39 - f & 7, 0, f + -39 & 7) + -47,
                a < e + 16);
  i[1]:int = 27;
  (i + 16)[0]:long@4 = 0[963]:long@4;
  i[2]:long@4 = 0[961]:long@4;
  0[963]:int = i + 8;
  0[962]:int = c;
  0[961]:int = g;
  0[964]:int = 0;
  a = i + 24;
  loop L_tc {
    a[1]:int = 7;
    g = a + 8;
    a = a + 4;
    if (f > g) continue L_tc;
  }
  if (i == e) goto B_gb;
  i[1]:int = i[1]:int & -2;
  e[1]:int = (c = i - e) | 1;
  i[0]:int = c;
  if (c > 255) goto B_uc;
  f = c >> 3;
  a = (f << 3) + 3436;
  g = 0[849]:int;
  if (g & (f = 1 << f)) goto B_wc;
  0[849]:int = g | f;
  f = a;
  goto B_vc;
  label B_wc:
  f = a[2]:int;
  label B_vc:
  a[2]:int = e;
  f.d = e;
  e[3]:int = a;
  e[2]:int = f;
  goto B_gb;
  label B_uc:
  a = 31;
  if (c > 16777215) goto B_xc;
  a = c >> 8;
  f = a << (a = a + 1048320 >> 16 & 8);
  g = f << (f = f + 520192 >> 16 & 4);
  a = ((g << (g = g + 245760 >> 16 & 2)) >> 15) - ((a | f) | g);
  a = (a << 1 | (c >> a + 21 & 1)) + 28;
  label B_xc:
  e[4]:long@4 = 0L;
  (e + 28)[0]:int = a;
  f = (a << 2) + 3700;
  g = 0[850]:int;
  if (g & (i = 1 << a)) goto B_zc;
  0[850]:int = g | i;
  f.a = e;
  (e + 24)[0]:int = f;
  goto B_yc;
  label B_zc:
  a = c << select_if(0, 25 - (a >> 1), a == 31);
  g = f.a;
  loop L_ad {
    f = g;
    if ((f.b & -8) == c) goto B_pb;
    g = a >> 29;
    a = a << 1;
    i = f + (g & 4) + 16;
    g = i[0]:int;
    if (g) continue L_ad;
  }
  i[0]:int = e;
  (e + 24)[0]:int = f;
  label B_yc:
  e[3]:int = e;
  e[2]:int = e;
  goto B_gb;
  label B_rb:
  a = e[2]:int;
  a[3]:int = d;
  e[2]:int = d;
  d[6]:int = 0;
  d[3]:int = e;
  d[2]:int = a;
  label B_qb:
  a = l + 8;
  goto B_a;
  label B_pb:
  a = f.c;
  a[3]:int = e;
  f.c = e;
  (e + 24)[0]:int = 0;
  e[3]:int = f;
  e[2]:int = a;
  label B_gb:
  a = 0[852]:int;
  if (a <= d) goto B_d;
  0[852]:int = (e = a - d);
  0[855]:int = (f = (a = 0[855]:int) + d);
  f.b = e | 1;
  a[1]:int = d | 3;
  a = a + 8;
  goto B_a;
  label B_d:
  errno_location()[0]:int = 48;
  a = 0;
  goto B_a;
  label B_c:
  if (eqz(l)) goto B_bd;
  if (i != (a = ((f = i[7]:int) << 2) + 3700)[0]:int) goto B_dd;
  a[0]:int = g;
  if (g) goto B_cd;
  0[850]:int = (h = h & -2 << f);
  goto B_bd;
  label B_dd:
  (l + select_if(16, 20, l[4] == i))[0]:int = g;
  if (eqz(g)) goto B_bd;
  label B_cd:
  g[6]:int = l;
  a = i[4]:int;
  if (eqz(a)) goto B_ed;
  g[4]:int = a;
  a[6]:int = g;
  label B_ed:
  a = (i + 20)[0]:int;
  if (eqz(a)) goto B_bd;
  (g + 20)[0]:int = a;
  a[6]:int = g;
  label B_bd:
  if (e > 15) goto B_gd;
  i[1]:int = (a = e + d) | 3;
  a = i + a;
  a[1]:int = a[1]:int | 1;
  goto B_fd;
  label B_gd:
  i[1]:int = d | 3;
  g = i + d;
  g[1]:int = e | 1;
  (g + e)[0]:int = e;
  if (e > 255) goto B_hd;
  e = e >> 3;
  a = (e << 3) + 3436;
  f = 0[849]:int;
  if (f & (e = 1 << e)) goto B_jd;
  0[849]:int = f | e;
  e = a;
  goto B_id;
  label B_jd:
  e = a[2]:int;
  label B_id:
  a[2]:int = g;
  e[3]:int = g;
  g[3]:int = a;
  g[2]:int = e;
  goto B_fd;
  label B_hd:
  a = 31;
  if (e > 16777215) goto B_kd;
  a = e >> 8;
  f = a << (a = a + 1048320 >> 16 & 8);
  d = f << (f = f + 520192 >> 16 & 4);
  a = ((d << (d = d + 245760 >> 16 & 2)) >> 15) - ((a | f) | d);
  a = (a << 1 | (e >> a + 21 & 1)) + 28;
  label B_kd:
  g[7]:int = a;
  g[4]:long@4 = 0L;
  f = (a << 2) + 3700;
  if (h & (d = 1 << a)) goto B_nd;
  0[850]:int = h | d;
  f.a = g;
  g[6]:int = f;
  goto B_md;
  label B_nd:
  a = e << select_if(0, 25 - (a >> 1), a == 31);
  d = f.a;
  loop L_od {
    f = d;
    if ((f.b & -8) == e) goto B_ld;
    d = a >> 29;
    a = a << 1;
    c = f + (d & 4) + 16;
    d = c.a;
    if (d) continue L_od;
  }
  c.a = g;
  g[6]:int = f;
  label B_md:
  g[3]:int = g;
  g[2]:int = g;
  goto B_fd;
  label B_ld:
  a = f.c;
  a[3]:int = g;
  f.c = g;
  g[6]:int = 0;
  g[3]:int = f;
  g[2]:int = a;
  label B_fd:
  a = i + 8;
  goto B_a;
  label B_b:
  if (eqz(k)) goto B_pd;
  if (g != (a = ((f = g[7]:int) << 2) + 3700)[0]:int) goto B_rd;
  a[0]:int = i;
  if (i) goto B_qd;
  0[850]:int = j & -2 << f;
  goto B_pd;
  label B_rd:
  (k + select_if(16, 20, k[4] == g))[0]:int = i;
  if (eqz(i)) goto B_pd;
  label B_qd:
  i[6]:int = k;
  a = g[4]:int;
  if (eqz(a)) goto B_sd;
  i[4]:int = a;
  a[6]:int = i;
  label B_sd:
  a = (g + 20)[0]:int;
  if (eqz(a)) goto B_pd;
  (i + 20)[0]:int = a;
  a[6]:int = i;
  label B_pd:
  if (e > 15) goto B_ud;
  g[1]:int = (a = e + d) | 3;
  a = g + a;
  a[1]:int = a[1]:int | 1;
  goto B_td;
  label B_ud:
  g[1]:int = d | 3;
  f = g + d;
  f.b = e | 1;
  (f + e)[0]:int = e;
  if (eqz(h)) goto B_vd;
  i = h >> 3;
  d = (i << 3) + 3436;
  a = 0[854]:int;
  i = 1 << i;
  if (i & c) goto B_xd;
  0[849]:int = i | c;
  i = d;
  goto B_wd;
  label B_xd:
  i = d[2]:int;
  label B_wd:
  d[2]:int = a;
  i[3]:int = a;
  a[3]:int = d;
  a[2]:int = i;
  label B_vd:
  0[854]:int = f;
  0[851]:int = e;
  label B_td:
  a = g + 8;
  label B_a:
  g_a = b + 16;
  return a;
}

export function free(a:int_ptr) {
  var c:int_ptr;
  var e:{ a:int, b:int, c:int, d:int }
  var f:int_ptr;
  var g:int_ptr;
  var h:int_ptr;
  if (eqz(a)) goto B_a;
  var b:int = a + -8;
  var d:{ a:int, b:int, c:int, d:int, e:int, f:int, g:int, h:int } = 
    b + (a = (c = (a + -4)[0]:int) & -8);
  if (c & 1) goto B_b;
  if (eqz(c & 3)) goto B_a;
  b = b - (c = b[0]:int);
  if (b < (e = 0[853]:int)) goto B_a;
  a = c + a;
  if (0[854]:int == b) goto B_c;
  if (c > 255) goto B_d;
  e = b[2]:int;
  e == (g = ((f = c >> 3) << 3) + 3436);
  c = b[3]:int;
  if (c != e) goto B_e;
  0[849]:int = 0[849]:int & -2 << f;
  goto B_b;
  label B_e:
  c == g;
  e.d = c;
  c[2] = e;
  goto B_b;
  label B_d:
  h = b[6]:int;
  g = b[3]:int;
  if (g == b) goto B_g;
  e > (c = b[2]:int);
  c[3] = g;
  g[2] = c;
  goto B_f;
  label B_g:
  c = b + 20;
  e = c[0];
  if (e) goto B_h;
  c = b + 16;
  e = c[0];
  if (e) goto B_h;
  g = 0;
  goto B_f;
  label B_h:
  loop L_i {
    f = c;
    g = e;
    c = g + 20;
    e = c[0];
    if (e) continue L_i;
    c = g + 16;
    e = g[4];
    if (e) continue L_i;
  }
  f[0] = 0;
  label B_f:
  if (eqz(h)) goto B_b;
  e = b[7]:int;
  c = (e << 2) + 3700;
  if (c[0] != b) goto B_k;
  c[0] = g;
  if (g) goto B_j;
  0[850]:int = 0[850]:int & -2 << e;
  goto B_b;
  label B_k:
  (h + select_if(16, 20, h[4] == b))[0]:int = g;
  if (eqz(g)) goto B_b;
  label B_j:
  g[6] = h;
  c = b[4]:int;
  if (eqz(c)) goto B_l;
  g[4] = c;
  c[6] = g;
  label B_l:
  c = b[5]:int;
  if (eqz(c)) goto B_b;
  (g + 20)[0]:int = c;
  c[6] = g;
  goto B_b;
  label B_c:
  c = d.b;
  if ((c & 3) != 3) goto B_b;
  0[851]:int = a;
  d.b = c & -2;
  b[1]:int = a | 1;
  (b + a)[0]:int = a;
  return ;
  label B_b:
  if (d <= b) goto B_a;
  c = d.b;
  if (eqz(c & 1)) goto B_a;
  if (c & 2) goto B_n;
  if (0[855]:int != d) goto B_o;
  0[855]:int = b;
  0[852]:int = (a = 0[852]:int + a);
  b[1]:int = a | 1;
  if (b != 0[854]:int) goto B_a;
  0[851]:int = 0;
  0[854]:int = 0;
  return ;
  label B_o:
  if (0[854]:int != d) goto B_p;
  0[854]:int = b;
  0[851]:int = (a = 0[851]:int + a);
  b[1]:int = a | 1;
  (b + a)[0]:int = a;
  return ;
  label B_p:
  a = (c & -8) + a;
  if (c > 255) goto B_r;
  e = d.c;
  e == (g = ((f = c >> 3) << 3) + 3436);
  c = d.d;
  if (c != e) goto B_s;
  0[849]:int = 0[849]:int & -2 << f;
  goto B_q;
  label B_s:
  c == g;
  e.d = c;
  c[2] = e;
  goto B_q;
  label B_r:
  h = d.g;
  g = d.d;
  if (g == d) goto B_u;
  0[853]:int > (c = d.c);
  c[3] = g;
  g[2] = c;
  goto B_t;
  label B_u:
  c = d + 20;
  e = c[0];
  if (e) goto B_v;
  c = d + 16;
  e = c[0];
  if (e) goto B_v;
  g = 0;
  goto B_t;
  label B_v:
  loop L_w {
    f = c;
    g = e;
    c = g + 20;
    e = c[0];
    if (e) continue L_w;
    c = g + 16;
    e = g[4];
    if (e) continue L_w;
  }
  f[0] = 0;
  label B_t:
  if (eqz(h)) goto B_q;
  e = d.h;
  c = (e << 2) + 3700;
  if (c[0] != d) goto B_y;
  c[0] = g;
  if (g) goto B_x;
  0[850]:int = 0[850]:int & -2 << e;
  goto B_q;
  label B_y:
  (h + select_if(16, 20, h[4] == d))[0]:int = g;
  if (eqz(g)) goto B_q;
  label B_x:
  g[6] = h;
  c = d.e;
  if (eqz(c)) goto B_z;
  g[4] = c;
  c[6] = g;
  label B_z:
  c = d.f;
  if (eqz(c)) goto B_q;
  (g + 20)[0]:int = c;
  c[6] = g;
  label B_q:
  b[1]:int = a | 1;
  (b + a)[0]:int = a;
  if (b != 0[854]:int) goto B_m;
  0[851]:int = a;
  return ;
  label B_n:
  d.b = c & -2;
  b[1]:int = a | 1;
  (b + a)[0]:int = a;
  label B_m:
  if (a > 255) goto B_aa;
  c = a >> 3;
  a = (c << 3) + 3436;
  e = 0[849]:int;
  if (e & (c = 1 << c)) goto B_ca;
  0[849]:int = e | c;
  c = a;
  goto B_ba;
  label B_ca:
  c = a[2];
  label B_ba:
  a[2] = b;
  c[3] = b;
  b[3]:int = a;
  b[2]:int = c;
  return ;
  label B_aa:
  c = 31;
  if (a > 16777215) goto B_da;
  c = a >> 8;
  e = c << (c = c + 1048320 >> 16 & 8);
  g = e << (e = e + 520192 >> 16 & 4);
  c = ((g << (g = g + 245760 >> 16 & 2)) >> 15) - ((c | e) | g);
  c = (c << 1 | (a >> c + 21 & 1)) + 28;
  label B_da:
  b[4]:long@4 = 0L;
  (b + 28)[0]:int = c;
  e = (c << 2) + 3700;
  g = 0[850]:int;
  if (g & (d = 1 << c)) goto B_ha;
  0[850]:int = g | d;
  e.a = b;
  (b + 24)[0]:int = e;
  goto B_ga;
  label B_ha:
  c = a << select_if(0, 25 - (c >> 1), c == 31);
  g = e.a;
  loop L_ia {
    e = g;
    if ((e.b & -8) == a) goto B_fa;
    g = c >> 29;
    c = c << 1;
    d = e + (g & 4) + 16;
    g = d.a;
    if (g) continue L_ia;
  }
  d.a = b;
  (b + 24)[0]:int = e;
  label B_ga:
  b[3]:int = b;
  b[2]:int = b;
  goto B_ea;
  label B_fa:
  a = e.c;
  a[3] = b;
  e.c = b;
  (b + 24)[0]:int = 0;
  b[3]:int = e;
  b[2]:int = a;
  label B_ea:
  0[857]:int = select_if(b = 0[857]:int + -1, -1, b);
  label B_a:
}

function f_og():int {
  return memory_size() << 16
}

function f_pg(a:int):int {
  var c:int;
  var b:int = d_ZkhCGvr6jgelzvPP[6]:int;
  a = b + (c = a + 3 & -4);
  if (eqz(c)) goto B_b;
  if (a <= b) goto B_a;
  label B_b:
  if (a <= f_og()) goto B_c;
  if (eqz(env_emscripten_resize_heap(a))) goto B_a;
  label B_c:
  d_ZkhCGvr6jgelzvPP[6]:int = a;
  return b;
  label B_a:
  errno_location()[0]:int = 48;
  return -1;
}

function f_qg(a:int, b:int, c:int):int {
  var f:int;
  var e:int;
  if (c < 512) goto B_a;
  env_emscripten_memcpy_big(a, b, c);
  return a;
  label B_a:
  var d:int = a + c;
  if ((b ^ a) & 3) goto B_c;
  if (a & 3) goto B_e;
  c = a;
  goto B_d;
  label B_e:
  if (c >= 1) goto B_f;
  c = a;
  goto B_d;
  label B_f:
  c = a;
  loop L_g {
    c[0]:byte = b[0]:ubyte;
    b = b + 1;
    c = c + 1;
    if (eqz(c & 3)) goto B_d;
    if (c < d) continue L_g;
  }
  label B_d:
  e = d & -4;
  if (e < 64) goto B_h;
  if (c > (f = e + -64)) goto B_h;
  loop L_i {
    c[0]:int = b[0]:int;
    c[1]:int = b[1]:int;
    c[2]:int = b[2]:int;
    c[3]:int = b[3]:int;
    c[4]:int = b[4]:int;
    c[5]:int = b[5]:int;
    c[6]:int = b[6]:int;
    c[7]:int = b[7]:int;
    c[8]:int = b[8]:int;
    c[9]:int = b[9]:int;
    c[10]:int = b[10]:int;
    c[11]:int = b[11]:int;
    c[12]:int = b[12]:int;
    c[13]:int = b[13]:int;
    c[14]:int = b[14]:int;
    c[15]:int = b[15]:int;
    b = b + 64;
    c = c + 64;
    if (c <= f) continue L_i;
  }
  label B_h:
  if (c >= e) goto B_b;
  loop L_j {
    c[0]:int = b[0]:int;
    b = b + 4;
    c = c + 4;
    if (c < e) continue L_j;
    goto B_b;
  }
  unreachable;
  label B_c:
  if (d >= 4) goto B_k;
  c = a;
  goto B_b;
  label B_k:
  e = d + -4;
  if (e >= a) goto B_l;
  c = a;
  goto B_b;
  label B_l:
  c = a;
  loop L_m {
    c[0]:byte = b[0]:ubyte;
    c[1]:byte = b[1]:ubyte;
    c[2]:byte = b[2]:ubyte;
    c[3]:byte = b[3]:ubyte;
    b = b + 4;
    c = c + 4;
    if (c <= e) continue L_m;
  }
  label B_b:
  if (c >= d) goto B_n;
  loop L_o {
    c[0]:byte = b[0]:ubyte;
    b = b + 1;
    c = c + 1;
    if (c != d) continue L_o;
  }
  label B_n:
  return a;
}

function f_rg(a:{ a:byte, b:byte, c:byte, d:byte }, b:{ a:long, b:long, c:long, d:long }, c:int):int {
  var e:int;
  var f:int;
  if (eqz(c)) goto B_a;
  var d:{ a:int, b:int, c:int, d:int, e:int, f:int, g:int } = c + a;
  (d + -1)[0]:byte = b;
  a.a = b;
  if (c < 3) goto B_a;
  (d + -2)[0]:byte = b;
  a.b = b;
  (d + -3)[0]:byte = b;
  a.c = b;
  if (c < 7) goto B_a;
  (d + -4)[0]:byte = b;
  a.d = b;
  if (c < 9) goto B_a;
  d = a + (e = 0 - a & 3);
  d.a = (b = (b & 255) * 16843009);
  c = d + (e = c - e & -4);
  (c + -4)[0]:int = b;
  if (e < 9) goto B_a;
  d.c = b;
  d.b = b;
  (c + -8)[0]:int = b;
  (c + -12)[0]:int = b;
  if (e < 25) goto B_a;
  d.g = b;
  d.f = b;
  d.e = b;
  d.d = b;
  (c + -16)[0]:int = b;
  (c + -20)[0]:int = b;
  (c + -24)[0]:int = b;
  (c + -28)[0]:int = b;
  c = e - (f = (d & 4) | 24);
  if (c < 32) goto B_a;
  var g:long = i64_extend_i32_u(b) * 4294967297L;
  b = d + f;
  loop L_b {
    b.d = g;
    b.c = g;
    b.b = g;
    b.a = g;
    b = b + 32;
    c = c + -32;
    if (c > 31) continue L_b;
  }
  label B_a:
  return a;
}

function f_sg(a:int):int {
  var d:int;
  var c:int;
  var b:ubyte_ptr = a;
  if (eqz(a & 3)) goto B_b;
  b = a;
  loop L_c {
    if (eqz(b[0])) goto B_a;
    b = b + 1;
    if (b & 3) continue L_c;
  }
  label B_b:
  loop L_d {
    c = b;
    b = c + 4;
    d = c[0]:int;
    if (eqz(((d ^ -1) & d + -16843009) & -2139062144)) continue L_d;
  }
  if (d & 255) goto B_e;
  return c - a;
  label B_e:
  loop L_f {
    d = c[1]:ubyte;
    b = c + 1;
    c = b;
    if (d) continue L_f;
  }
  label B_a:
  return b - a;
}

export function stackSave():int {
  return g_a
}

export function stackRestore(a:int) {
  g_a = a
}

export function stackAlloc(a:int):int {
  var b:int = g_a - a & -16;
  g_a = b;
  return b;
}

export function emscripten_stack_init() {
  g_c = 5246800;
  g_b = 3908 + 15 & -16;
}

export function emscripten_stack_get_free():int {
  return g_a - g_b
}

export function emscripten_stack_get_end():int {
  return g_b
}

function f_zg(a:int):int {
  return 1
}

function f_ah(a:int) {
}

function f_bh(a:int) {
}

function f_ch(a:int) {
}

function f_dh():int {
  f_bh(3892);
  return 3900;
}

function f_eh() {
  f_ch(3892)
}

export function fflush(a:int_ptr):int {
  var c:int;
  var b:int;
  if (eqz(a)) goto B_b;
  if (a[19] > -1) goto B_c;
  return f_gh(a);
  label B_c:
  b = f_zg(a);
  c = f_gh(a);
  if (eqz(b)) goto B_a;
  f_ah(a);
  return c;
  label B_b:
  c = 0;
  if (eqz(0[976]:int)) goto B_d;
  c = fflush(0[976]:int);
  label B_d:
  a = f_dh()[0]:int;
  if (eqz(a)) goto B_e;
  loop L_f {
    b = 0;
    if (a[19] < 0) goto B_g;
    b = f_zg(a);
    label B_g:
    if (a[5] <= a[7]) goto B_h;
    c = f_gh(a) | c;
    label B_h:
    if (eqz(b)) goto B_i;
    f_ah(a);
    label B_i:
    a = a[14];
    if (a) continue L_f;
  }
  label B_e:
  f_eh();
  label B_a:
  return c;
}

function f_gh(a:int):int {
  var c:int;
  if (a[5]:int <= a[7]:int) goto B_a;
  call_indirect(a, 0, 0, a[9]:int);
  if (a[5]:int) goto B_a;
  return -1;
  label B_a:
  var b:int = a[1]:int;
  if (b >= (c = a[2]:int)) goto B_b;
  call_indirect(a, i64_extend_i32_s(b - c), 1, a[10]:int);
  label B_b:
  a[7]:int = 0;
  a[2]:long = 0L;
  a[1]:long@4 = 0L;
  return 0;
}

function f_hh(a:int, b:int, c:int, d:long, e:long) {
  env_embind_register_bigint(a,
                             b,
                             c,
                             i32_wrap_i64(d),
                             i32_wrap_i64(d >> 32L),
                             i32_wrap_i64(e),
                             i32_wrap_i64(e >> 32L))
}

