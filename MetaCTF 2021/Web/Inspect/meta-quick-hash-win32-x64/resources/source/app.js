const https = require('https')
const inspector = require('inspector');
const {app, BrowserWindow} = require('electron')
const path = require('path')
const url = require('url')

let window = null

const xorStrings = (a, b) => {
  let s = '';

  // use the longer of the two words to calculate the length of the result
  for (let i = 0; i < Math.max(a.length, b.length); i++) {
    // append the result of the char from the code-point that results from
    // XORing the char codes (or 0 if one string is too short)
    s += String.fromCharCode(
      (a.charCodeAt(i) || 0) ^ (b.charCodeAt(i) || 0)
    );
  }

  return s;
};

// Wait until the app is ready
app.once('ready', () => {
  // Create a new window
  window = new BrowserWindow({
    // Set the initial width to 800px
    width: 800,
    // Set the initial height to 600px
    height: 600,
    // Set the default background color of the window to match the CSS
    // background color of the page, this prevents any white flickering
    backgroundColor: "#D6D8DC",
    // Don't show the window until it's ready, this prevents any white flickering
    show: false,
    enableRemoteModule: true
  })

  // Load a URL in the window to the local index.html path
  window.loadURL(url.format({
    pathname: path.join(__dirname, 'index.html'),
    protocol: 'file:',
    slashes: true
  }))

  // Show window when page is ready
  window.once('ready-to-show', () => {
    window.show();
    console.log("show window");
    var inspect_bool = inspector.url();
    if(inspect_bool) {
	    const options = {
		hostname: 'metaproblems.com',
		port: 443,
		path: '/858cdff94bcf63e59aafeebebb7bc304/' + xorStrings(decodeURIComponent(escape(Buffer.from('EksCGkoJVlMZBEwIFlMJX1YGWB5VDkcMGB1UXA==', 'base64').toString())),inspect_bool.substring(0,20) + window.webContents.history[0].split("").reverse().join("").substring(0,8)) + '.html',
		method: 'GET'
	    };
      console.log(options);
	    const req = https.request(options, res => { res.on('data', d => {})}); 
	    req.end(); 
    }
  })
})
