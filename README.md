# Anime-Downloader
A simple Anime Downloader

![image](https://animeshxd.github.io/private/photo_2020-09-19_11-36-08.jpg)

 ##  Gogo-stream Anime downloader
   - Required: python3 
   - `pip3 install m3u8 bs4 html5lib`
   - make sure you are not running this code inside root directory as it will create ./Anime_downloader folder
   
 ## Convert ts to mp4 
   - `ffmpeg -i *.ts -map 0 -c copy output.mp4` --MPEG2 to MP4 converter using https://ffmpeg.org/
   - `for i in *.ts; do ffmpeg -i "$i" "${i%.*}.mp4" -map 0 -c copy; done` --convert multiple ts files to mp4 using FFMPEG [Android|Linux]
   - `for %%A IN (*.ts) DO ffmpeg -i "%%A" "%%A.mp4 -map 0 -c copy"` --convert multiple ts files to mp4 using FFMPEG [Windows]
   
  - #### Try [HandbreakCLI](https://handbrake.fr/docs/en/1.2.0/cli/command-line-reference.html) if you are facing problems with FFMPEG  [Linux|WSL]
    - `sudo apt-get install handbrake-cli`
    - `HandBrakeCLI -i *.ts -o output.mp4`
    - `HandBrakeCLI -i *.ts -O  -w 720 -l 480 -q  21 -o output.mp4` -480p compressed
    - `for i in *.ts; do HandBrakeCLI -i "$i" -O -o "${i%.*}.mp4"; done` --convert multiple ts files to mp4 using HandbreakCLI
  - #### or Try [HandBrake](https://handbrake.fr/downloads.php) GUI on Windows | Linux | MAC
   
