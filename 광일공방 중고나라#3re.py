#해결 안된 문제 1) 삭제 기능시 번호만 남겨둔다면 비어 있는 자료를 어떻게 건너 뛸 수 있을까.
#페이지네이션을 어떻게 팬시하게 짤 수 있을까 (n개씩 삭제 된 것 빼고 어떻게 뽑을 수 있을까)
#페이지네이션을 어떻게 팬시하게 짤 수 있을까2 (다른 기능을 해도 항상 그 화면이 떠 있어야 함)
#디스플레이 포맷 짜보기 
#예외처리
###필히 검색### 

import os
import csv
import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_current_time():
    date_time = datetime.datetime.now()
    return date_time.strftime("%Y-%m-%d %H:%M")

class Post():
    def __init__(self):
        self.post_info = list()
        self.post_info_reverse = self.post_info.reverse()#다시
        #self.post_page = list()
        self.pull_post_info()

    def pull_post_info(self):
        f = open('post.csv', 'r', encoding = 'euc_kr')
        rdr = csv.reader(f)#네이밍 다시
        for post in rdr:
            self.post_info.append(post)
        f.close()


class Board(Post):
    def __init__(self):
        super().__init__()
        self.actions = [self.wrtie_post,self.update_post,self.delete_post,self.save_post,self.prev_page,self.next_page]
        self.page_no = 0
        self.PAGE_NUMBER_RANGE = 15
        
    @staticmethod
    def display_intro():
        print('본 프로그램은 중고거래 사이트를 만들기 위한 게시판 프로그램입니다.')
        input('프로그램을 시작하시려면 엔터키를 입력하세요...')
        os.system('cls')

    def wrtie_post(self):
        new_post = [int(self.post_info[-1][0]) + 1, input('작성해주세요:'), calculate_current_time()]
        self.post_info.append(new_post)

    def update_post(self):
        update_post_no = int(input('몇 번 글을 수정 할까요?')) - 1 #시간은 수정된 시간으로 해야 하나//?
        self.post_info[update_post_no][1] = input('수정>')

    def delete_post(self):
        delete_post_no = int(input('몇 번 글을 삭제 할까요?')) - 1
        del self.post_info[delete_post_no][1:]

    def save_post(self):#네이밍 다시
        f = open('post.csv', 'w', encoding='euc_kr',newline='')
        wr = csv.writer(f)
        for post_info in range(len(self.post_info)):
            wr.writerow(post_info)
            
    def prev_page(self):#x0보다 작지 않게 예외처리
        self.page_no -= 1

    def next_page(self):
        self.page_no += 1
    
    def current_page_posts(self):
        start = 15 * page 
        개수 = 15 
        if 15개 안되면 그만큼만 
        while i < self.PAGE_NUMBER_RANGE and  post >= 0:#post네이밍 다시
            self.post_info[self.PAGE_NUMBER_RANGE * self.page_no:]
            
            i = i + 1 

    def display_post_page(self):
        if bool(self.post_info):
            print('게시글을 작성해 보는 것인 어떨까요?')
            return
        for post in range(self.PAGE_NUMBER_RANGE):
            print(*self.post_info[post + self.page_no * self.PAGE_NUMBER_RANGE])
         #15개씩 다시 넣고 인덱스로 조절할 것인가. 그때마다 15개씩 뽑을 것인가
         #인덱스 오버레인지를 어떻게 컨트롤 할 것인가.
    def display_actions(self):#좀 더 이쁘게 할 수 없을까
        print('----------------페이지 목록----------------')
        print('1. 작성하기')
        print('2. 수정하기')
        print('3. 삭제하기')
        print('------------------------------------------')

    def execute_action(self):#예외처리 필요함
        action_no = int(input('번호를 입력하세요:'))
        self.actions[action_no - 1]()

if __name__ == "__main__":
    Board.display_intro()
    post = Post()#네이밍 다시
    board = Board()
    while True:
        board.display_post_page()
        board.display_actions()
        board.execute_action()
