[app]

# Título do seu aplicativo
title = Coleta

# Nome do pacote
package.name = coleta

# Domínio do pacote (necessário para empacotamento android/ios)
package.domain = org.coleta

# Diretório de código-fonte onde o main.py está localizado
source.dir = .

# Extensões de arquivos fonte para incluir (deixe vazio para incluir todos os arquivos)
source.include_exts = py,png,jpg,kv,atlas

# Versão do aplicativo
version = 0.0.1

# Lista de requisitos do aplicativo
requirements = python3,kivy==2.1.0,kivymd==0.104.2,pillow,pygments==2.8.0,kivy-garden,Cython==0.29.31

# Ícone do aplicativo
#icon.filename = icon.png

# Orientações suportadas
orientation = portrait

# Android específico

# Indicar se o aplicativo deve ser tela cheia ou não
fullscreen = 1

# API de destino do Android, deve ser o mais alto possível
android.api = 30

# API mínima que o APK / AAB suportará
android.minapi = 28

# Versão do SDK do Android a ser usada
android.ndk = 25b

# API NDK do Android a ser usada
android.ndk_api = 21

# Aceitar automaticamente a licença do SDK do Android
android.accept_sdk_license = True

# Entrada do Android, padrão é ok para aplicativo baseado em Kivy
android.entrypoint = org.kivy.android.PythonActivity

# Lista de arquiteturas Android para compilar
android.archs = arm64-v8a, armeabi-v7a

# Permitir backup automático no Android (API >=23)
android.allow_backup = True

# Formato usado para empacotar o aplicativo para modo de lançamento (aab ou apk)
android.release_artifact = aab

# Formato usado para empacotar o aplicativo para modo de depuração (apk)
android.debug_artifact = apk

[buildozer]

# Nível de log (0 = apenas erros, 1 = informações, 2 = depuração (com saída de comando))
log_level = 2

# Mostrar aviso se o buildozer for executado como root (0 = Falso, 1 = Verdadeiro)
warn_on_root = 0
