🎤 Voice-to-Text プロジェクト

音声をリアルタイムで文字起こしし、翻訳も行う簡易ツールです。
Python + SpeechRecognition + Deep Translator を使用しています。

📁 ファイル構成
Voice-to-text/
├── voice-to-text.py      # 音声認識＆翻訳スクリプト
├── voice-to-text.bat     # Windows用起動バッチ

🧩 セットアップ手順

Pythonをインストール
Python 3.10 以上を推奨。

必要なライブラリをインストール

コマンドプロンプトで以下を実行：

pip install SpeechRecognition pyaudio deep-translator


※ pyaudio のインストールが失敗する場合は：

pip install pipwin
pipwin install pyaudio


フォルダ構成を確認

voice-to-text.py と voice-to-text.bat を同じフォルダ（例：D:\Python\source\Voice-to-text）に置く。

▶️ 起動方法

voice-to-text.bat をダブルクリック。

自動的に Python スクリプトが起動し、音声入力を開始します。

💬 voice-to-text.py の内容概要
import os
import pyaudio
import speech_recognition as sr
from deep_translator import GoogleTranslator

r = sr.Recognizer()
mic = sr.Microphone()

def translate_text(text):
    translator = GoogleTranslator(source='auto', target='ja')
    result = translator.translate(text)
    print("翻訳結果:", result)

with mic as source:
    print("🎙 音声を話してください...")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='en-US')
        print("認識結果:", text)
        translate_text(text)
    except Exception as e:
        print("エラー:", e)

🔍 機能説明

マイクから音声をリアルタイムで録音

Google Speech Recognition で英語をテキスト化

deep-translator を使用して日本語に翻訳

翻訳結果をコンソールに表示

⚙️ voice-to-text.bat の内容
@ECHO off
mode con: cols=1000 lines=300
d:
cd d:\python\source\Voice-to-text\
python voice-to-text.py
cmd /k

🔍 バッチファイルの動作

コンソールを広く（1000列×300行）設定

指定フォルダに移動

Pythonスクリプトを起動

終了後もウィンドウを開いたままにする（cmd /k）

🚀 実行例
🎙 音声を話してください...
認識結果: Hello, how are you today?
翻訳結果: こんにちは、今日はどうですか？

💡 トラブルシューティング
症状	対応策
pyaudio のインストールに失敗	pipwin install pyaudio を試す
音が認識されない	マイク設定を確認 (sr.Microphone.list_microphone_names()で確認可)
翻訳が出ない	Deep Translatorのインターネット接続を確認
ウィンドウがすぐ閉じる	cmd /k が末尾にあるか確認
🧰 補足

PyInstallerで配布用にEXE化する場合：

pyinstaller --onefile voice-to-text.py


生成された実行ファイルは dist/voice-to-text.exe に出力されます。
