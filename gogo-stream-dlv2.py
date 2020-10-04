import requests
import json
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup,SoupStrainer
import ast
import os
import os.path
from os import path
import sys
import m3u8
import time


def IfFailed():

    Quality = input(
        "Version 1:\nSelect Quality :\n\t0: 360p Quality\n\t1: 480p Quality\n\t2: 720p Quality\n\t3: 1080p Quality\n\t> ")


    search = input("Search Anime Name: ")

    url = f"https://gogo-stream.com/ajax-search.html?keyword={search}"  # url
    url = url.replace(" ", "%20")  # replace userinput 'space' with %20

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest'} 




    x = Request(url=url,  headers=headers)
    html = urlopen(x)
    search_t = BeautifulSoup(html.read(), "html5lib")

    Count_t = -1
    search_loop_main = True
    search_loop_snd = True
    list_i_loop_next = False


    while search_loop_main:

        while search_loop_snd:

            if str(search_t.findAll('a')) == "[]":
                print("Anime not found")
                list_i_loop_next = False

                break

            for node in search_t.findAll('a'):

                Count_t = Count_t + 1
                rslt2 = ''.join(node.findAll(text=True))
                rslt2 = (rslt2.replace("<\\/a><\\/li>", ""))
                rslt2 = rslt2.replace('<\\/ul>"}', '')

                

                print(Count_t, ": ", rslt2)

            synlist = search_t.find_all("a", text=True)
            # print(synlist)


            list_i_loop = True

            while list_i_loop:

                list_i = input("Select Anime Name: [q] to exit:\n Select:>")
                


                    ##################################################

                if list_i == "q" or list_i == "quit":
                    list_i_loop_next = False

                    break
                elif list_i.isdigit() == False:
                    print("not integer value")
                    continue
                elif int(list_i) > Count_t:
                    print("Not Available")
                    continue
                elif list_i.isdigit():
                    # print(type(synlist))
                    str_list = str(synlist[int(list_i)].text)
                    str_list = (str_list.replace("<\\/a><\\/li>", ""))
                    str_list = str_list.replace('<\\/ul>"}', '')
                    print(str_list)
                    list_i_loop_next = True

                    links_with_raw = [a['href']
                                    for a in search_t.find_all('a', href=True) if a.text]
                    linkisgood = str(links_with_raw[int(list_i)])
                    # linkisgood = linkisgood.replace('\\"','')
                    linkisgood = linkisgood.replace('\\', '')
                    linkisgood = linkisgood.replace('"', '')

                    # https://vidstreaming.io/videos/

                    # \"\/videos\/xxxholic-the-movie-a-midsummer-nights-dream-episode-1\"
                    #print(linkisgood, " test")

                    Anime_Url = linkisgood


                    A_url_total_episode = linkisgood.split('-')
                    print('Total Episode: ',A_url_total_episode[-1])
                    
                    Episode_select = input(
                    "Enter Episode Manually: [Y]es or [N]o or [A]ll?: \n\t  Select:> ")

                    if Episode_select.lower() == 'y' or Episode_select.lower() == 'yes':
                        print(" Enter Episode like \nif you want to Download Anime episode 5 to 20 then type 5:20\nif you want to Download Anime episode 5 to last then type 5:a")
                        Anime_Episode_From, Anime_Episode_to = input(
                            "Enter Episode: ").split(':')
                        print(Anime_Episode_to.isdigit())
                        if Anime_Episode_From.isdigit():
                            Anime_Episode_From = int(Anime_Episode_From) - 1
                            select_a = True
                        else:
                            Anime_Episode_From = 0

                        if Anime_Episode_to.isdigit():
                            select_b = True
                        else:
                            select_b = False
                            

                        # if Anime_Episode_to == 'a':
                            # Anime_All = True

                    else:
                        print("Downloading All Episode..")
                        select_a = False
                        select_b = False



    #by Animeshxd https://github.com/animeshxd/
    ####################################################


                    # print("without ep:",Anime_Url)

                    Anime_Name = f"{str_list}"
                    # links_with_text = [a['href'] for a in search_t.find_all('a', href=True) if a.text]
                    # links_with_text[2]

                    Anime_Name = Anime_Name.lower()
                    Anime_Name = Anime_Name.replace('-', '')
                    # print(Anime_Name)
                    Anime_Name = Anime_Name.replace('  ', '_')
                    Anime_Name = Anime_Name.replace(' ', '_')
                    # print(Anime_Name)
                    characters_to_remove = '"():*!@#$%^&*+=|\\/`~<>?"}{[]:;`"'

                    for character in characters_to_remove:
                        Anime_Name = Anime_Name.replace(character, "")

                    break

                else:
                    list_i = 0
                break
                    
                    ####################################################
            if list_i_loop_next:


                

                Anime_Url = f"https://gogo-stream.com{Anime_Url}"
                


                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                      'Accept-Encoding': 'none',
                      'Accept-Language': 'en-US,en;q=0.8',
                      'Connection': 'keep-alive',
                      'X-Requested-With': 'XMLHttpRequest'}

                xeXD = Request(url=Anime_Url,  headers=headers)
                htmle = urlopen(xeXD)
                listxD = BeautifulSoup(htmle.read(), "html5lib")
                listxD = str(listxD.findAll("ul",class_="listing items lists"))
                remove_listxD = "[]"
                for charecter in remove_listxD: 
                  listxD = listxD.replace(charecter,"")


                this_is_linkxD_listxD = []
                this_is_linkxD_listxD.clear()
                for linkxD in BeautifulSoup(listxD, features="lxml", parse_only=SoupStrainer('a')):
                    if linkxD.has_attr('href'):
                        this_is_linkxD_listxD += [linkxD['href']]
                Total_Anime_Episode = len(this_is_linkxD_listxD)
                this_is_linkxD_listxD.reverse()
  
                # print(this_is_linkxD_listxD)
                # Total_Anime_Episode = len(this_is_linkxD_listxD)



                # print(Anime_Url)

                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                        'Accept-Encoding': 'none',
                        'Accept-Language': 'en-US,en;q=0.8',
                        'Connection': 'keep-alive'

                        }

                Anime_Episode = 0
                
                Main_Loop = True

                Folder_check = path.exists(f"./Anime_downloader/{Anime_Name}")
                while Folder_check == False:
                    os.makedirs(f"./Anime_downloader/{Anime_Name}")
                    break
                # |
                # |
                def Anime_list_downloader():
                      Anime_Name_Full = f"{Anime_Name}_{Anime_Episode}"
                      # print(Anime_Name_Full)
                      print(f"\nDownloading Episode {Anime_Episode}")

                      Anime_download_path = f"./Anime_downloader/{Anime_Name}/{Anime_Name_Full}.mp4"

                      reg_url = f"https://gogo-stream.com{ixd_list}"

                      # print(reg_url) 

                      my_request = Request(url=reg_url, headers=headers)

                      html = urlopen(my_request)
                      my_iframe = BeautifulSoup(html.read(), "html5lib")
                      error = my_iframe.body.get_text()
                      # print(error)
                      # if error == "404\n":
                      #     print("No Anime Available")
                      #     break
                      vidstreaming = "http:" + str(my_iframe.iframe["src"])

                      # print(vidstreaming)
                      vidstreaming = vidstreaming.replace(
                          'streaming.php', 'ajax.php')
                      # print(vidstreaming)

                      my_request = Request(url=vidstreaming, headers=headers)
                      html = urlopen(my_request)
                      my_iframe = BeautifulSoup(html.read(), "html5lib")
                      # print(my_iframe)
                      stream_json = my_iframe.body.get_text()

                      # print(stream_json)
                      # print(type(stream_json))

                      stream_json = json.loads(stream_json)

                      # print(stream_json)

                      # print(type(stream_json))

                      stream_json_1 = stream_json['source']

                      stream_json_1 = str(stream_json_1)
                      stream_json_1 = stream_json_1.replace('[', '')
                      stream_json_1 = stream_json_1.replace(']', '')
                      stream_json_1 = ast.literal_eval(stream_json_1)
                      stream_json_1 = stream_json_1.get("file")
                      # print(stream_json_1)

                      stream_json_1_Status_mp4 = "php" in stream_json_1
                      # stream_json_1_Status_m3u8 = "m3u8" in stream_json_1

                      # print("mp4 : ",stream_json_1_Status_mp4)
                      # print("m3u8: ",stream_json_1_Status_m3u8)

                      stream_json = stream_json['source_bk']

                      stream_json = str(stream_json)
                      stream_json = stream_json.replace('[', '')
                      stream_json = stream_json.replace(']', '')
                      # print(type(stream_json))
                      stream_json = ast.literal_eval(stream_json)
                      # print(stream_jsonn)
                      stream_json = stream_json.get("file")
                      # print(stream_json)

                      # stream_json_Status_mp4 = "mp4" in stream_json
                      # stream_json_Status_m3u8 = "m3u8" in stream_json

                      # print("mp4 : ",stream_json_Status_mp4)
                      # print("m3u8: ",stream_json_Status_m3u8)

                      if stream_json_1_Status_mp4 == True:  # nobk
                          # stream_json_url = stream_json_1

                          with open(Anime_download_path, "wb") as f:
                              print("Downloading %s" % Anime_Name_Full)
                              response = requests.get(
                                  stream_json_1, stream=True, allow_redirects=True)
                              total_length = response.headers.get('content-length')
                              # print(total_length)
                              # if path.exists(Anime_download_path) == False:
                              #   mb = 0
                              # else:
                              #   mb = int((os.stat(Anime_download_path).st_size) / 1e+6)
                              
                          

                              if total_length is None:  # no content length header
                                  f.write(response.content)
                              
                              else:
                                  dl = 0
                                  total_length = int(total_length)
                                  # 1000 equals to 1 MB bandwidth
                                  for data in response.iter_content(chunk_size=100000):
                                      dl += len(data)
                                      f.write(data)
                                      done = int(40 * dl / total_length)
                                      if path.exists(Anime_download_path) == False:
                                          mb = 0
                                      else:
                                          mb = int((os.stat(Anime_download_path).st_size) / 1e+6)

                                      sys.stdout.write("\r %s/%2.fMB|%s%s|" % (mb, total_length / 1e+6, '█' * done, ' ' * (40-done)))
                                      sys.stdout.flush()

                      else:



                          master_m3u8 = m3u8.load(uri=stream_json, headers={
                                                  'Referer': f'{vidstreaming}'})
                          master_m3u8.data

                          lenofmaster_m3u8 = len(master_m3u8.data['playlists'])
                          lomm = 0
                          Available_quality = master_m3u8.data['playlists']

                          for x in Available_quality:
                              check_quality = x['stream_info']['name']
                              print('Available Quality:',
                                  check_quality)
                              lomm += 1

                          lenofmaster_m3u8 = len(master_m3u8.data['playlists'])

                          if Quality.isdigit():

                              if Quality == "0":
                                  master_url = master_m3u8.data['playlists'][0]['uri']

                              elif Quality == "1" and int(Quality) <= (lenofmaster_m3u8 - 1):
                                  master_url = master_m3u8.data['playlists'][1]['uri']

                              elif Quality == "2" and int(Quality) <= (lenofmaster_m3u8 - 1):
                                  master_url = master_m3u8.data['playlists'][int(
                                      lenofmaster_m3u8 - 2)]['uri']

                              elif Quality == "3" and int(Quality) <= (lenofmaster_m3u8 - 1):
                                  master_url = master_m3u8.data['playlists'][int(
                                      lenofmaster_m3u8 - 1)]['uri']

                              elif int(Quality) > (lenofmaster_m3u8 - 1):
                                  print("Downloading Best Quality")
                                  master_url = master_m3u8.data['playlists'][int(
                                      lenofmaster_m3u8 - 1)]['uri']

                              else:

                                  master_url = master_m3u8.data['playlists'][int(
                                      lenofmaster_m3u8 - 1)]['uri']

                          else:
                              print("Default Quality Availavle for this episode")
                              master_url = master_m3u8.data['playlists'][int(
                                  lenofmaster_m3u8 - 1)]['uri']

                          # print(master_url)

                          link_no_index = stream_json.split('/')[-1]

                          # print(str(link_no_index))

                          master_link = stream_json.replace(
                              f'{str(link_no_index)}', f'{str(master_url)}')
                          # print(master_link)
                          playlist_down = m3u8.load(master_link, headers=headers)
                          #m3u8_down = playlist_down.data['segments'][0]['uri']
                          m3u8_segment_uris = [segment['uri']
                                              for segment in playlist_down.data['segments']]

                          sgmn = len(m3u8_segment_uris)
                          sgmn_1 = 0
                          sess = requests.Session()
                          Anime_download_path_ts = Anime_download_path.split('.')
                          Anime_download_path = Anime_download_path.replace(f"{Anime_download_path_ts[-1]}","ts")
                  #by Animeshxd https://github.com/animeshxd/

                          with open(Anime_download_path, 'wb') as f:
                              
                              for x in m3u8_segment_uris:
                                  m3u8_down_link = stream_json.replace(
                                      f'{str(link_no_index)}', f'{x}')
                                  start_r_time = time.time()
                                  r = sess.get(m3u8_down_link)
                                  Size_ts = int(r.headers.get('content-length')) / 1024
                                  speed = Size_ts / (time.time()-start_r_time)
                              

                                  dl = 0
                                  sgmn_1 = sgmn_1 + 1
                                  prsntg = int(sgmn_1 / sgmn * 100)
                                  
                                  # done = int(40 * sgmn_1 / sgmn)
                                  for data in r.iter_content(chunk_size=100000):
                                      # dl = len(data) 

                                      f.write(data)
                                  
                                      mb = int(
                                          (os.stat(Anime_download_path).st_size) / (1024 * 1024))
                                      

                                      sys.stdout.write(
                                          "\r%sMB Loaded|%2.fKB/s|[%s/100%%]" % (mb, speed , prsntg))
                                      sys.stdout.flush()
                                      # sys.stdout.write("\r[%s%s]"% ('*' * done, '.' * (40-done)))
                                      # sys.stdout.flush()



                if select_a:
                    # print("")
                    for ixd_list in this_is_linkxD_listxD[int(Anime_Episode_From):]:
                        Anime_Episode = ixd_list.split('-')
                        Anime_Episode = Anime_Episode[-1]
                        Anime_list_downloader()
                        if select_b == True:
                            if ixd_list == this_is_linkxD_listxD[int(Anime_Episode_to)-1]:
                                break
                        else:
                          if ixd_list == this_is_linkxD_listxD[Total_Anime_Episode-1]:
                            break

                else:
                    for ixd_list in this_is_linkxD_listxD:
                        Anime_Episode = ixd_list.split('-')
                        Anime_Episode = Anime_Episode[-1]
                        Anime_list_downloader()
                        if ixd_list == this_is_linkxD_listxD[Total_Anime_Episode-1]:
                          break




                            
            #by Animeshxd https://github.com/animeshxd/

                        # print("last")
                
            else:
                print("sorry")

            break

        # break

        Bye_Bye = input("\nNo Anime Available\nType 1 to exit\nType 2 to Retry : ")
        if Bye_Bye == "1":
            break
        elif Bye_Bye == "2":
            Count_t = -1
            IfFailed()
        else:
            print("Sayonara")
            exit()
            break

IfFailed()

#by Animeshxd https://github.com/animeshxd/

# /html/body/ul/li[1]/a
