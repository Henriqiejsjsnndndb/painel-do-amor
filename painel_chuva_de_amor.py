pkg update -y && pkg install wget unzip python lsof ffmpeg nodejs -y && termux-setup-storage && \
npm install -g vercel && \
mkdir -p $HOME/site_lorena && \
[ -f "/sdcard/Download/BIN - Saturno (prod. Ajaxx)(M4A_128K).m4a" ] && ffmpeg -i "/sdcard/Download/BIN - Saturno (prod. Ajaxx)(M4A_128K).m4a" "$HOME/site_lorena/saturno.mp3" || echo "⚠️ Arquivo de música não encontrado, verifique o caminho!" && \
cat > $HOME/site_lorena/site.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash

SITE_DIR="$HOME/site_lorena"
MUSIC_FILE="$HOME/site_lorena/saturno.mp3"
PORT="8000"
TITLE="Nosso Amor, Lorena 💖"
MESSAGE="Lorena, meu amor, você é a luz que ilumina meus dias, mesmo estando tão longe. Cada batida do meu coração é por você, e hoje, no nosso momento especial, quero te dizer que te amo mais do que as palavras podem expressar. Você é meu tudo, minha razão de sorrir, e prometo estar sempre ao seu lado, não importa a distância. ❤️"
BACKGROUND_COLORS="#ffdde1,#ee9ca7"

check_requirements() {
    local dependencies=("python3" "lsof")
    for dep in "${dependencies[@]}"; do
        if ! command -v "$dep" >/dev/null 2>&1; then
            echo "❌ $dep não encontrado. Instale com: pkg install $dep"
            exit 1
        fi
    done
}

check_music_file() {
    if [[ ! -f "$MUSIC_FILE" ]]; then
        echo "❌ Arquivo de música não encontrado em: $MUSIC_FILE"
        echo "Por favor, ajuste o caminho do MUSIC_FILE no script."
        exit 1
    fi
}

create_html() {
    cat > "$SITE_DIR/index.html" <<HTML
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Uma página romântica dedicada a Lorena.">
    <title>$TITLE</title>
    <style>
        body {
            background: linear-gradient(to right, $BACKGROUND_COLORS);
            color: white;
            text-align: center;
            font-family: 'Arial', sans-serif;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            margin: 0;
            overflow: hidden;
            position: relative;
        }
        h1 {
            font-size: clamp(2.5em, 5vw, 3.5em);
            text-shadow: 2px 2px 8px rgba(0,0,0,0.6);
            animation: fadeIn 2s ease-in;
            z-index: 10;
        }
        p {
            font-size: clamp(1.2em, 3vw, 1.8em);
            max-width: 90%;
            margin: 20px auto;
            line-height: 1.6;
            animation: fadeIn 3s ease-in;
            z-index: 10;
        }
        audio {
            outline: none;
            width: clamp(250px, 80%, 320px);
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            margin: 20px 0;
            z-index: 10;
            background: rgba(255,255,255,0.2);
        }
        .heart {
            position: absolute;
            font-size: 2em;
            color: #ff4d4d;
            animation: float 5s linear infinite;
            pointer-events: none;
        }
        .click-heart {
            font-size: 1.5em;
            color: #ff1a1a;
            animation: pop 1s ease-out forwards;
        }
        button {
            background-color: rgba(255, 255, 255, 0.3);
            border: none;
            padding: 15px 30px;
            font-size: 1.2em;
            color: white;
            border-radius: 25px;
            cursor: pointer;
            box-shadow: 0 4px 10px rgba(0,0,0,0.5);
            transition: transform 0.2s, background-color 0.2s;
            z-index: 10;
        }
        button:hover {
            background-color: rgba(255, 255, 255, 0.5);
            transform: scale(1.1);
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes float {
            0% { transform: translateY(100vh); opacity: 1; }
            100% { transform: translateY(-100px); opacity: 0; }
        }
        @keyframes pop {
            0% { transform: scale(0); opacity: 1; }
            50% { transform: scale(1.5); opacity: 1; }
            100% { transform: scale(0); opacity: 0; }
        }
        audio::-webkit-media-controls-panel {
            background-color: rgba(255,255,255,0.2);
            border-radius: 15px;
        }
        @media (max-width: 600px) {
            h1 { font-size: 2em; }
            p { font-size: 1.2em; }
            button { padding: 10px 20px; font-size: 1em; }
        }
    </style>
</head>
<body>
    <h1>$TITLE</h1>
    <p>$MESSAGE</p>
    <audio controls autoplay loop>
        <source src="saturno.mp3" type="audio/mpeg">
        Seu navegador não suporta áudio.
    </audio>
    <button onclick="createHearts()">Toque para Corações! ❤️</button>
    <script>
        let isButtonClicked = false;
        function createHearts() {
            if (isButtonClicked) return;
            isButtonClicked = true;
            setTimeout(() => isButtonClicked = false, 1000);
            for (let i = 0; i < 10; i++) {
                const heart = document.createElement('span');
                heart.className = 'click-heart';
                heart.innerHTML = '❤️';
                heart.style.left = (Math.random() * 80 + 10) + 'vw';
                heart.style.top = (Math.random() * 80 + 10) + 'vh';
                document.body.appendChild(heart);
                setTimeout(() => heart.remove(), 1000);
            }
        }
        function createFloatingHearts() {
            for (let i = 0; i < 20; i++) {
                setTimeout(() => {
                    const heart = document.createElement('span');
                    heart.className = 'heart';
                    heart.innerHTML = '❤️';
                    heart.style.left = Math.random() * 100 + 'vw';
                    heart.style.animationDuration = Math.random() * 3 + 3 + 's';
                    document.body.appendChild(heart);
                    setTimeout(() => heart.remove(), 5000);
                }, Math.random() * 5000);
            }
        }
        setInterval(createFloatingHearts, 5000);
        createFloatingHearts();
        document.addEventListener('touchstart', (e) => {
            if (e.touches.length > 1) e.preventDefault();
        }, { passive: false });
    </script>
</body>
</html>
HTML
}

get_local_ip() {
    ip -4 addr show wlan0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}' || echo "127.0.0.1"
}

check_requirements
mkdir -p "$SITE_DIR" || { echo "❌ Falha ao criar diretório $SITE_DIR"; exit 1; }
cd "$SITE_DIR" || { echo "❌ Falha ao acessar diretório $SITE_DIR"; exit 1; }
check_music_file
cp "$MUSIC_FILE" . || { echo "❌ Falha ao copiar arquivo de música"; exit 1; }
create_html
if lsof -i :"$PORT" >/dev/null 2>&1; then
    echo "⚠️ Porta $PORT já em uso. Tentando liberar..."
    kill -9 $(lsof -t -i :"$PORT") 2>/dev/null || { echo "❌ Falha ao liberar a porta $PORT"; exit 1; }
fi
echo -e "\n🌐 Servidor iniciado! Acesse localmente: http://localhost:$PORT"
echo "📱 Na rede local, use: http://$(get_local_ip):$PORT"
echo "⚠️ Para acesso público, use Vercel ou outra hospedagem."
echo "⚠️ Pressione Ctrl+C para parar o servidor"
python3 -m http.server "$PORT" --bind 0.0.0.0 || { echo "❌ Falha ao iniciar o servidor"; exit 1; }
EOF
chmod +x $HOME/site_lorena/site.sh && \
cd $HOME/site_lorena && \
./site.sh & sleep 5 && \
vercel login && \
vercel .
