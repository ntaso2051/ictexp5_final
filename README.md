# IOT 制作実験
### やったこと
- https://walking-succession-falls.com/%E3%83%A9%E3%82%BA%E3%83%99%E3%83%AA%E3%83%BC%E3%83%91%E3%82%A4%E3%81%ABGUI%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B
- https://qiita.com/kakinaguru_zo/items/eda129635816ad871e9d


### 案1：カメラでジェスチャー判定
- Mediapipeのpythonパッケージを使う
- https://qiita.com/Kazuhito/items/222999f134b3b27418cd

### ⭐️案2：監視カメラで人を認識
- OpenCV
- LINE か Slackに通知
- 人数で密度計算
- [人数カウント](https://iotservice.biz/it-memo/ai-person-detection)
- https://iotservice.biz/it-memo/ai-person-detection
- **役割分担**
    - webカメから画像撮ってくる 佐々木
    - 画像から人数をカウント 佐藤
    - 何かしら通知を送る 今野
- https://github.com/
### 案3：監視カメラ
- 30分おきとかにYoutubeにアップロード
- [YouTubeAPIを利用して動画をアップロードする](https://qiita.com/ny7760/items/5a728fd9e7b40588237c)
- [OpenCVを使ってWebカメラで撮影した動画をMP4形式で保存する](https://chusotsu-program.com/opencv-videocapture/)
