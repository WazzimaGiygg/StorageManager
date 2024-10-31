const { app, BrowserWindow, dialog, ipcMain } = require('electron');
const fs = require('fs');
const path = require('path');

let mainWindow;

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            contextIsolation: true,
            enableRemoteModule: false,
            preload: path.join(__dirname, 'preload.js')
        }
    });

    mainWindow.loadFile('index.html');

    mainWindow.on('closed', function () {
        mainWindow = null;
    });
}

app.on('ready', createWindow);

ipcMain.handle('open-folder', async () => {
    const folder = await dialog.showOpenDialog({
        properties: ['openDirectory']
    });
    return folder.filePaths[0];
});

ipcMain.handle('list-files', (event, folderPath) => {
    return fs.readdirSync(folderPath);
});

ipcMain.handle('read-file', (event, filePath) => {
    return fs.readFileSync(filePath, 'utf-8');
});
