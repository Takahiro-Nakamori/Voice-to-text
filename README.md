マイクから入力された日本語をリアルタイムで音声認識し、英語に翻訳して表示するPythonツールです。 特に、PC起動時の自動実行や不安定なネットワーク環境での利用を想定し、インターネット接続が確立されるまで自動で待機・復帰する機能を備えています。

🌟 特徴
自動ネットワーク待機: 起動時にインターネット接続を確認し、接続されるまで5秒おきに再試行します。

リアルタイム翻訳: Google Web Speech API と Google Translate (via deep-translator) を組み合わせたシームレスな翻訳。

エラーリカバリ: 実行中にWi-Fiが切断されても、スクリプトが終了せずに接続復帰を待ちます。

環境適応: adjust_for_ambient_noise により、周囲の雑音に合わせてマイクの感度を自動調整します。

📋 構成図
プログラムの処理フローは以下の通りです。

Start: 起動確認（wait_for_internet）

Listening: マイクから音声を取得し、背景ノイズを抑制

Speech-to-Text: Google APIで日本語をテキスト化

Translation: 日本語テキストを英語に翻訳

Output: コンソールへ結果を表示

🛠 準備
1. 必要なライブラリのインストール
pip install numpy SpeechRecognition deep-translator librosa matplotlib pyaudio

Note: Windows環境で pyaudio のインストールに失敗する場合は、PyAudioの公式ドキュメントを確認するか、.whl ファイルからのインストールを検討してください。

2. ディレクトリ構造（例）
Plaintext

Voice-to-text/
├── voice-to-text.py      # Python本体
├── run.bat               # 起動用バッチファイル
└── README.md             # 本ファイル
🚀 使い方
Windowsでの実行
付属のバッチファイル、またはコマンドプロンプトから実行してください。

Bash

python voice-to-text.py
起動後、「ネットワーク接続を確認中...」と表示されます。

接続が確認されると「何か話してください...」と表示されます。

マイクに向かって日本語で話すと、認識結果と英語翻訳が表示されます。

「ストップ」 と発話するか、Ctrl + C を押すことで安全に終了します。

🛡 エラーハンドリング
接続エラー: ネットワークが途切れると自動で wait_for_internet モードに入り、復帰を待ちます。

認識不可: 声が小さすぎる場合や不明瞭な場合は （音声を認識できませんでした） と表示され、次の入力を待ちます。
