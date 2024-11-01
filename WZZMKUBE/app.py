from flask import Flask, render_template_string

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visualizador de JSON em Múltiplas Abas</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
            padding: 0;
            margin: 0;
            height: 100vh;
        }
        .container {
            max-width: 100%; 
            height: 100%;
            margin: auto;
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            display: flex;
            flex-direction: column;
        }
        .tabs {
            display: flex;
            flex-wrap: wrap; 
            margin-bottom: 10px;
        }
        .tab {
            padding: 10px;
            background: #ddd;
            margin: 5px; 
            border-radius: 4px 4px 0 0;
            cursor: pointer;
            flex: 1; 
            text-align: center; 
        }
        .tab.active {
            background: white;
            border-bottom: 2px solid #4285F4;
        }
        iframe {
            width: 100%;
            height: 100%;
            border: none; 
            margin-top: 0;
            border-radius: 4px;
            flex: 1; 
        }
        input[type="file"], input[type="password"], button {
            width: 100%;
            margin: 10px 0;
            padding: 12px; 
            font-size: 16px; 
        }
        button {
            background-color: #4285F4;
            border: none;
            color: white;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #357ae8;
        }
    </style>
</head>
<body>
    <div class="container">
        <input type="file" id="jsonFile" accept=".json">
        <input type="password" id="encryptionPassword" placeholder="Senha para decriptografia">
        <button id="importButton">Importar JSON</button>
        
        <div class="tabs" id="tabs"></div>
        <div id="iframesContainer" style="flex: 1; display: flex; flex-direction: column;"></div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
    <script>
        document.getElementById('importButton').onclick = function() {
            importJSON();
        };

        function importJSON() {
            const fileInput = document.getElementById('jsonFile');
            const password = document.getElementById('encryptionPassword').value;
            const file = fileInput.files[0];

            if (!file) {
                alert('Por favor, selecione um arquivo JSON.');
                return;
            }

            const reader = new FileReader();
            reader.onload = function(event) {
                const encryptedData = event.target.result;

                try {
                    const bytes = CryptoJS.AES.decrypt(encryptedData, password);
                    const jsonString = bytes.toString(CryptoJS.enc.Utf8);
                    const parsedData = JSON.parse(jsonString);

                    document.getElementById('jsonFile').style.display = 'none';
                    document.getElementById('encryptionPassword').style.display = 'none';
                    document.getElementById('importButton').style.display = 'none';

                    document.getElementById('tabs').innerHTML = '';
                    document.getElementById('iframesContainer').innerHTML = '';

                    for (const key in parsedData) {
                        if (parsedData.hasOwnProperty(key)) {
                            addTab(parsedData[key], key);
                        }
                    }
                } catch (e) {
                    alert('Erro ao decriptografar o arquivo. Verifique a senha ou o formato do arquivo.');
                }
            };
            reader.readAsText(file);
        }

        function addTab(htmlContent, tabName) {
            const tabButton = document.createElement('div');
            tabButton.className = 'tab';
            tabButton.innerText = tabName;
            tabButton.onclick = () => setActiveTab(tabName);
            document.getElementById('tabs').appendChild(tabButton);

            const iframe = document.createElement('iframe');
            iframe.id = tabName;
            iframe.srcdoc = htmlContent;
            document.getElementById('iframesContainer').appendChild(iframe);

            if (document.querySelectorAll('.tab').length === 1) {
                tabButton.classList.add('active');
                iframe.style.display = 'block';
            } else {
                iframe.style.display = 'none';
            }
        }

        function setActiveTab(tabName) {
            const tabs = document.querySelectorAll('.tab');
            const iframes = document.querySelectorAll('iframe');

            tabs.forEach(tab => {
                tab.classList.remove('active');
            });

            iframes.forEach(iframe => {
                iframe.style.display = 'none';
            });

            document.getElementById(tabName).style.display = 'block';
            const activeTab = Array.from(tabs).find(tab => tab.innerText === tabName);
            if (activeTab) {
                activeTab.classList.add('active');
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
