const {app, BrowserWindow} = require('electron')
const path = require('path')
const url = require('url')

// THE FL@G is right below this message!!
let f = "TWV0YUNURnt5b3VfY29tcGxldGVkX0FfU2VhcmNoX0FuZF9SZXNjdWVfdGhlX2ZsYWdfbWlzc2lvbn0="

let window = null

// Wait until the app is ready
app.once('ready', () => {
  // Create a new window
  window = new BrowserWindow({
    // Set the initial width to 500px
    width: 500,
    // Set the initial height to 400px
    height: 400,
    // set the title bar style
    titleBarStyle: 'hiddenInset',
    // set the background color to black
    backgroundColor: "#111",
    // Don't show the window until it's ready, this prevents any white flickering
    show: false
  })

  window.loadURL(url.format({
    pathname: path.join(__dirname, 'index.html'),
    protocol: 'file:',
    slashes: true
  }))

  window.once('ready-to-show', () => {
    window.show()
  })
})
