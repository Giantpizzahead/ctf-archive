const electronInstaller = require('electron-winstaller');

async function build() {
	try {
	  await electronInstaller.createWindowsInstaller({
	    appDirectory: '/home/kali/electron/simple-samples-master/activity-monitor/release-builds/electron-tutorial-app-win32-x64/',
	    outputDirectory: '/home/kali/electron/simple-samples-master/activity-monitor/builds',
	    authors: 'My App Inc.',
	    exe: 'myapp.exe'
	  });
	  console.log('It worked!');
	} catch (e) {
	  console.log(`No dice: ${e.message}`);
	}
} 

build();
