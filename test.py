import os
import csv
import datetime

def calculate_current_time():
    date_time = datetime.datetime.now()
    return date_time.strftime("%Y-%m-%d %H:%M")

class Post():
    def __init__(self):
        self.post_info = list()
        self.post_info_reverse = self.post_info.reverse()#다시
        #self.post_page = list()
        self.pull_post_info()
        self.total_post_no = int(self.post_info[0][0])

    def pull_post_info(self):
        f = open('post.csv', 'r', encoding = 'euc_kr')
        rdr = csv.reader(f)#네이밍 다시
        for post in rdr:
            self.post_info.append(post)
        f.close()
    
    def wrtie_post(self):
        if not bool(self.post_info):
            self.total_post_no = 0 #불완정
         #다시 해야함..    
        new_post = [self.total_post_no, input('작성해주세요:'), calculate_current_time()]
        self.total_post_no = self.total_post_no + 1
        self.post_info[0] = self.total_post_no
        self.post_info.append(new_post)

if __name__ == "__main__":
    post = Post()
    print(type(post.total_post_no))
    print(post.total_post_no)
    while True:
        post.wrtie_post()
        print(post.post_info)