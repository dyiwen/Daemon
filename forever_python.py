# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 18:48:23 2017
"""

import os, time

"""
function:创建日志
reutrn logging object
"""
def create_logging(filepath='info.log',mode = 'a'):
    import logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=filepath,
                        filemode= mode)
    return logging

""" 
守护python 进程
"""
def forever_python(search_cmd_list, start_cmd_list, true_name):
    while True:
        for i, cmd in enumerate(search_cmd_list):
            time.sleep(13)
            result = os.popen(cmd).read()
            #print result
            if true_name[i] not in result:
                #print true_name[i]
                #print start_cmd_list[i]
                os.system(start_cmd_list[i])
                logging.info(start_cmd_list[i])
                
if __name__ == "__main__":
    
    search_cmd_list = [
    #"ps -ef| grep ./server.py",
    "ps -ef | grep 'java -jar ./sandBox-1.0-SNAPSHOT.jar' | grep -v grep"
    ]
    
    start_cmd_list = [
    #"cd /home/tx-deepocean/Infervision/tx_pacs_scp/ && (python ./server.py &)",
    "cd /root/sandBox/ && (nohup java -jar ./sandBox-1.0-SNAPSHOT.jar >> /opt/log/nohup.out &)"
    ]       
    
    true_name = [
    #"node ./main.js",
    "java -jar ./sandBox-1.0-SNAPSHOT.jar"
    ]

    logging = create_logging("/root/sandBox/forever_python.log")
    forever_python(search_cmd_list, start_cmd_list, true_name)
