# Anime-Downloader
A simple Anime Downloader

 ## vidstrm_auto_search.py-- Gogo-stream downloader
   - Required: python3 
   - `pip3 install m3u8 bs4 html5lib`
   - make sure you are not running this code inside root directory as it will create ./Anime_downloader folder
 ## Convert ts to mp4 
   - $ `ffmpeg -i *.ts -map 0 -c copy output.mp4` --MPEG2 to MP4 converter using https://ffmpeg.org/
  - #### Try [HandbreakCLI](https://handbrake.fr/docs/en/1.2.0/cli/command-line-reference.html) if you are facing problems with FFMPEG 
    - `sudo apt-get install handbrake-cli`
    - `HandBrakeCLI -i *.ts -o output.mp4`
    - `HandBrakeCLI -i *.ts -O  -w 720 -l 480 -q  21 -o output.mp4` -480p compressed
    - [ts-ep](https://animeshxd.github.io/private/ts-ep) -- convert multiple .ts video file into mp4
   
