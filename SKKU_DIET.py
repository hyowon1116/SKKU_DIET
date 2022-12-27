### 성균 다이어트학개론 ###

# 라이브러리 import
import os
import sys
import random
import warnings
import pandas as pd
from tkinter import *
from PIL import Image, ImageTk
from plyer import notification
from tkinter.messagebox import askyesno
warnings.filterwarnings('ignore')

# 변수 리스트
paths = [
    './data/SKKU_GS25_FOOD.csv',
    './data/LOGO.ico'
]
fonts = [
    ('나눔고딕', 30, 'bold'),
    ('나눔고딕', 20, 'bold'),
    ('나눔고딕', 15, 'bold'),
    ('나눔고딕', 13),
    ('나눔고딕', 11)
]
styles = [
    {'bg': 'green', 'fg': 'white', 'activebackground': 'white', 'activeforeground': 'green', 'cursor': 'hand2'},
    {'bg': 'white', 'activebackground': '#EDFCF4', 'font': fonts[2], 'compound': LEFT, 'anchor': 'w', 'width': 400, 'padx': 10, 'pady': 10, 'cursor': 'hand2'},
    {'bg': 'white', 'activebackground': '#fceded', 'activeforeground': 'red', 'font': fonts[2], 'compound': LEFT, 'anchor': 'w', 'width': 400, 'padx': 10, 'pady': 10, 'cursor': 'hand2'},
    {'font': fonts[3], 'width': 9, 'relief': 'groove'}
]

class SKKUDiet(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.title('성균 다이어트학개론')
        self.switch_frame(Intro)
        self.open_center()
        self.iconbitmap(paths[1])
        self.resizable(False, False)
    
    # 화면 중앙 배치 함수
    def open_center(self):
        r = 500
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x, y = (sw - r) / 2, (sh - r) / 2
        self.geometry('%dx%d+%g+%g'%(r, r, x, y))
    
    # 화면 전환 함수
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

# 프로그램 초기 화면
class Intro(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text='성균 다이어트학개론', font=fonts[0], fg='darkgreen').grid(pady=(30, 0))
        image = ImageTk.PhotoImage(Image.open('./data/SKKU_LOGO.png').resize((300, 300)))
        logo = Label(self, image=image)
        logo.image = image
        logo.grid()
        Button(self, text='수강신청', font=fonts[2], **styles[0], padx=70, pady=7, command=lambda: master.switch_frame(UserInfo)).grid(pady=(10, 0))

# 사용자 정보 입력 화면
class UserInfo(Frame):
    def __init__(self, master):
        global ID, Gender, Age, Height, Weight
        Frame.__init__(self, master)
        Label(self, text='인적 사항', font=fonts[1], fg='green').grid(column=0, columnspan=3, pady=30)
        infoList = ['이름/별명', '성별', '나이', '키(cm)', '현재 몸무게(kg)']
        for i in range(5):
            Label(self, text=infoList[i]+'  ', font=fonts[3]).grid(row=i+1, column=0, pady=15)
        ID = Entry(self, font=fonts[2], bg='lightyellow', justify=CENTER)
        Gender = IntVar()
        btn_male = Radiobutton(self, text='남성', font=fonts[2], value=0, variable=Gender)
        btn_female = Radiobutton(self, text='여성', font=fonts[2], value=1, variable=Gender)
        Age = Entry(self, font=fonts[2], bg='orange', justify=CENTER)
        Height = Entry(self, font=fonts[2], bg='skyblue', justify=CENTER)
        Weight = Entry(self, font=fonts[2], bg='skyblue', justify=CENTER)
        ID.grid(row=1, column=1, columnspan=2, ipady=5)
        btn_male.grid(row=2, column=1)
        btn_female.grid(row=2, column=2)
        Age.grid(row=3, column=1, columnspan=2, ipady=5)
        Height.grid(row=4, column=1, columnspan=2, ipady=5)
        Weight.grid(row=5, column=1, columnspan=2, ipady=5)
        Button(self, text='다음', font=fonts[3], padx=10, pady=5, **styles[0], command=lambda: master.switch_frame(PrintBMR)).grid(row=6, column=2, pady=(30, 0), sticky='e')

# 기초대사량 출력 화면
class PrintBMR(Frame):
    def __init__(self, master):
        global nickname, g, a, h, w, BMR
        Frame.__init__(self, master)
        nickname, g, a, h, w = ID.get(), int(Gender.get()), int(Age.get()), float(Height.get()), float(Weight.get())
        if g == 0: BMR = int(66.47 + (13.75 * w) + (5 * h) - (4.76 * a)) # 남성의 BMR 계산
        else: BMR = int(655.1 + (9.56 * w) + (1.85 * h) - (4.68 * a)) # 여성의 BMR 계산
        Label(self, text='기초대사량 성적표', font=fonts[1], fg='green').grid(row=0, column=0, columnspan=4, pady=30)
        Label(self, text='이름', font=fonts[3]).grid(row=1, column=1, pady=10)
        Label(self, text='BMR', font=fonts[3]).grid(row=2, column=1, pady=10)
        Label(self, text=nickname, font=fonts[2]).grid(row=1, column=2)
        Label(self, text=f'{BMR} kcal', font=fonts[2]).grid(row=2, column=2)
        Label(self, text="'기초대사량(BMR)'이란?\n생명을 유지하는 데 필요한 최소한의 에너지의 양", font=fonts[4]).grid(row=3, columnspan=4, pady=(60, 0))
        Label(self, text='평균 기초대사량', font=fonts[4]).grid(row=4, columnspan=4, pady=(15, 0))
        Label(self, text='20대 남성 : 1300~2100 kcal\n20대 여성 : 1100~1600 kcal', font=fonts[4]).grid(row=5, columnspan=4, pady=(0, 30))
        Button(self, text='다시', font=fonts[3], padx=10, pady=5, **styles[0], command=lambda: master.switch_frame(UserInfo)).grid(row=6, column=0, sticky='w')
        Button(self, text='다음', font=fonts[3], padx=10, pady=5, **styles[0], command=lambda: master.switch_frame(InputGoal)).grid(row=6, column=3, sticky='e')

# 목표 입력 화면
class InputGoal(Frame):
    def __init__(self, master):
        global TargetWeight, TargetTime
        Frame.__init__(self, master)
        Label(self, text='목표 입력', font=fonts[1], fg='green').grid(row=0, column=0, columnspan=4, pady=30)
        Label(self, text='목표 몸무게(kg)  ', font=fonts[3]).grid(row=1, column=0, pady=15)
        Label(self, text='목표 기간(일)  ', font=fonts[3]).grid(row=2, column=0, pady=15)
        TargetWeight = Entry(self, font=fonts[2], width=15, bg='skyblue', justify=CENTER)
        TargetTime = Entry(self, font=fonts[2], width=15, bg='orange', justify=CENTER)
        TargetWeight.grid(row=1, column=2, columnspan=2, ipady=5)
        TargetTime.grid(row=2, column=2, columnspan=2, ipady=5)
        # 목표 오류 여부에 따른 전환 화면 결정 함수
        def isError():
            global error
            try:
                int(TargetTime.get())
                if float(TargetWeight.get()) < w:
                    return PrintKcal
                else:
                    error = '목표 몸무게는 현재 몸무게보다 작아야 합니다.'
                    return PrintError
            except ValueError:
                error = '몸무게와 기간은 숫자로만 이루어져야 합니다.'
                return PrintError
        Button(self, text='다음', font=fonts[3], padx=10, pady=5, **styles[0], command=lambda: master.switch_frame(isError())).grid(column=3, pady=(80, 0), sticky='e')

# 목표 오류 화면
class PrintError(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text='목표 오류', font=fonts[1], fg='red').grid(row=0, pady=30)
        Label(self, text=error, font=fonts[4]).grid(row=1)
        Label(self, text='목표를 다시 입력해주세요.', font=fonts[4]).grid(row=2)
        Button(self, text='목표 입력', font=fonts[3], width=10, pady=5, **styles[0], command=lambda: master.switch_frame(InputGoal)).grid(row=3, pady=(50, 0))

# 하루 권장 칼로리 출력 화면
class PrintKcal(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        OLC = (eval(f'({w} - {TargetWeight.get()}) * 7000 / {TargetTime.get()}'))
        ORC = BMR * 1.12
        EatCal = int(ORC - OLC * 0.6)
        ConsumeCal = int(OLC * 0.4)
        Label(self, text='오늘의 칼로리 과제', font=fonts[1], fg='green').grid(row=0, column=1, pady=30)
        Label(self, text='하루 권장 섭취 칼로리', font=fonts[2]).grid(row=1, column=1, pady=(15, 0))
        Label(self, text=f'{EatCal} kcal', font=fonts[2]).grid(row=2, column=1, pady=(0, 15))
        Label(self, text='하루 권장 소비 칼로리', font=fonts[2]).grid(row=3, column=1, pady=(15, 0))
        Label(self, text=f'{ConsumeCal} kcal', font=fonts[2]).grid(row=4, column=1)
        Label(self, text="체중 1 kg을 감량하기 위해선", font=fonts[4]).grid(row=5, column=1, pady=(50, 0))
        Label(self, text='7000 kcal를 소비해야 합니다.', font=fonts[4]).grid(row=6, column=1, pady=(0, 30))
        Button(self, text='다시', font=fonts[3], padx=10, pady=5, **styles[0], command=lambda: master.switch_frame(InputGoal)).grid(row=7, column=0, sticky='w')
        Button(self, text='다음', font=fonts[3], padx=10, pady=5, **styles[0], command=lambda: master.switch_frame(MainMenu)).grid(row=7, column=2, sticky='e')

# 메인 메뉴 화면
class MainMenu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # 프로그램 종료 함수
        def askQuit():
            if askyesno(title='로그아웃', message='성균 다이어트학개론을 종료하시겠습니까?'):
                sys.exit()
        Label(self, text='강의콘텐츠', font=fonts[1], fg='green').grid(pady=30)
        icon1, icon2, icon3, icon4 = Image.open('./data/ICON1.png'), Image.open('./data/ICON2.png'), Image.open('./data/ICON3.png'), Image.open('./data/ICON4.png')
        img1, img2, img3, img4 = ImageTk.PhotoImage(icon1.resize((50, 50))), ImageTk.PhotoImage(icon2.resize((50, 50))), ImageTk.PhotoImage(icon3.resize((50, 50))), ImageTk.PhotoImage(icon4.resize((50, 50)))
        btn1 = Button(self, text='1강 - 편의점 다이어트 음식 추천', image=img1, **styles[1], command=lambda: master.switch_frame(MenuOne))
        btn2 = Button(self, text='2강 - 편의점 다이어트 음식 검색/추가', image=img2, **styles[1], command=lambda: master.switch_frame(MenuTwo))
        btn3 = Button(self, text='3강 - 인적 사항 변경', image=img3, **styles[1], command=lambda: master.switch_frame(MenuThree))
        btn4 = Button(self, text='로그아웃', image=img4, **styles[2], command=askQuit)
        btn1.image, btn2.image, btn3.image, btn4.image = img1, img2, img3, img4
        btn1.grid(pady=5); btn2.grid(pady=5); btn3.grid(pady=5); btn4.grid(pady=(40, 0))

# [1] 편의점 다이어트 음식 추천 - 예산 입력
class MenuOne(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text='예산 입력', font=fonts[1], fg='green').grid(row=0, column=0, columnspan=3, pady=(30, 15))
        Label(self, text='1가지 음식에 사용 가능한 예산을 입력해주세요.', font=fonts[4]).grid(row=1, column=0, columnspan=3)
        Label(self, text='예산을 넘지 않는 3가지 음식을 추천합니다.', font=fonts[4]).grid(row=2, column=0, columnspan=3, pady=(0, 60))
        Label(self, text='예산(원) ', font=fonts[3]).grid(row=3, column=0)
        Budget = Entry(self, font=fonts[2], bg='orange', justify=CENTER)
        Budget.grid(row=3, column=1, columnspan=2, ipady=5)
        # 예산 기준 음식 데이터 추출 함수
        def getFood():
            global colors, foodList
            data = pd.read_csv(paths[0], encoding='cp949')
            target = data[data['가격(원)'] <= float(Budget.get())]
            types = ['단백질', '샐러드', '영양바류', '음료', '기타']
            colors = dict(zip(types, ['#F9E0E3', '#F6FDD1', '#FAF1D0', '#C2F8F8', '#FCEBDB'])) # 종류별 색깔 지정
            foodList = [target[target['종류'] == t].reset_index(drop=True) for t in types]
        Button(self, text='취소', font=fonts[3], padx=10, pady=5, **styles[0], command=lambda: master.switch_frame(MainMenu)).grid(row=4, column=0, pady=(150, 0), sticky='w')
        Button(self, text='다음', font=fonts[3], padx=10, pady=5, **styles[0], command=lambda: [getFood(), master.switch_frame(RecommendFood)]).grid(row=4, column=2, pady=(150, 0), sticky='e')

# [1]-1 편의점 다이어트 음식 추천
class RecommendFood(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # 비어 있는 음식 데이터 삭제
        for i in range(len(foodList) - 1, -1, -1):
            if foodList[i].empty: del foodList[i]
        # 음식 데이터 리스트의 데이터 유무에 따른 내용 결정
        try:
            # 3가지 음식 랜덤 선택
            labelStyle = {'text': '추천 식단표', 'font': fonts[1], 'fg': 'green'}
            x, y, z = random.sample(range(len(foodList)), 3)
            type1, type2, type3 = foodList[x].T, foodList[y].T, foodList[z].T
            food1, food2, food3 = type1.pop(0), type2.pop(0), type3.pop(0)
            foodList[x], foodList[y], foodList[z] = type1.T.reset_index(drop=True), type2.T.reset_index(drop=True), type3.T.reset_index(drop=True)
            infoType = ['칼로리', '탄수화물', '단백질', '지방']
            Label(self, text='상품명', font=fonts[3], bg='snow', width=18, relief='groove').grid(row=1, column=0, columnspan=2, ipadx=3, ipady=1)
            Label(self, text='가격', bg='snow', **styles[3]).grid(row=1, column=2, ipady=1)
            Label(self, text='영양정보', font=fonts[3], bg='snow', width=18, relief='groove').grid(row=1, column=3, columnspan=2, ipadx=3, ipady=1)
            # 반복문을 이용한 음식 정보 출력
            for i in range(3):
                item = [food1, food2, food3][i]
                color = colors[item[1]]
                name, namePad = item[0].replace(') ', ')\n', 1), 29
                if '\n' not in name: namePad += 10
                price = format(int(item[2]), ',') + '원'
                Label(self, text=name, bg=color, font=fonts[3], width=18, relief='groove').grid(row=i*4+2, column=0, rowspan=4, columnspan=2, ipadx=3, ipady=namePad)
                Label(self, text=price, bg=color, **styles[3]).grid(row=i*4+2, column=2, rowspan=4, ipady=39)
                for j in range(4):
                    if j == 0: unit = 'kcal'
                    else: unit = 'g'
                    Label(self, text=infoType[j], bg='snow', **styles[3]).grid(row=i*4+j+2, column=3)
                    Label(self, text='%g %s'%(item[j+3], unit), bg=color, **styles[3]).grid(row=i*4+j+2, column=4)
            # 식단 만족 여부 질문 함수
            def askGoodDiet():
                totalPrice = format(food1[2] + food2[2] + food3[2], ',')
                totalKcal = '%g'%(food1[3] + food2[3] + food3[3])
                answer = askyesno(
                    title='해당 식단에 만족하시나요?',
                    message='음식1: %s\n음식2: %s\n음식3: %s\n\n총 가격 : %s 원\n총 칼로리 : %s kcal'%(food1[0], food2[0], food3[0], totalPrice, totalKcal)
                )
                if answer:
                    master.switch_frame(MainMenu)
            Button(self, text='재추천', font=fonts[3], padx=10, pady=5, **styles[0], command=lambda: master.switch_frame(RecommendFood)).grid(row=14, column=0, pady=(15, 0), sticky='w')
            Button(self, text='확인', font=fonts[3], padx=10, pady=5, **styles[0], command=askGoodDiet).grid(row=14, column=4, pady=(15, 0), sticky='e')
        except ValueError:
            # 음식 종류의 개수가 3 이하일 경우
            labelStyle = {'text': '추천 오류', 'font': fonts[1], 'fg': 'red'}
            Label(self, text='적절한 식단이 없습니다.', font=fonts[4]).grid(row=1, column=0, columnspan=5, pady=15)
            Label(self, text='예산을 다시 입력하거나', font=fonts[4]).grid(row=2, column=0, columnspan=5)
            Label(self, text='메뉴로 돌아갈 수 있습니다.', font=fonts[4]).grid(row=3, column=0, columnspan=5)
            Button(self, text='예산 입력', font=fonts[3], width=10, pady=5, **styles[0], command=lambda: master.switch_frame(MenuOne)).grid(row=5, column=0, columnspan=5, pady=(150, 20))
            Button(self, text='메뉴로', font=fonts[3], width=10, pady=5, **styles[0], command=lambda: master.switch_frame(MainMenu)).grid(row=6, column=0, columnspan=5)
        Label(self, **labelStyle).grid(row=0, column=0, columnspan=5, pady=(30, 15))

# [2] 편의점 다이어트 음식 검색/추가 - 음식 입력
class MenuTwo(Frame):
    def __init__(self, master):
        global food, data
        Frame.__init__(self, master)
        data = pd.read_csv(paths[0], encoding='cp949')
        Label(self, text='음식 입력', font=fonts[1], fg='green').grid(row=0, column=0, columnspan=3, pady=(30, 15))
        Label(self, text='검색/추가하려는 음식의 상품명을 입력해주세요.', font=fonts[4]).grid(row=1, column=0, columnspan=3)
        Label(self, text='정확하게 입력하지 않으면 검색되지 않을 수 있습니다.', font=fonts[4]).grid(row=2, column=0, columnspan=3, pady=(15, 0))
        Label(self, text='잘못된 예시', font=fonts[4]).grid(row=3, column=0)
        Label(self, text='→', font=fonts[4]).grid(row=3, column=1)
        Label(self, text='프로틴밀', font=fonts[4]).grid(row=3, column=2)
        Label(self, text='올바른 예시', font=fonts[4]).grid(row=4, column=0)
        Label(self, text='→', font=fonts[4]).grid(row=4, column=1)
        Label(self, text='그린비아) 프로틴밀', font=fonts[4]).grid(row=4, column=2)
        Label(self, text='상품명 ', font=fonts[3]).grid(row=5, column=0, pady=50)
        food = Entry(self, font=fonts[2], bg='lightyellow', justify=CENTER)
        food.grid(row=5, column=1, columnspan=2, ipady=5)
        # 음식 존재 여부에 따른 전환 화면 결정 함수
        def isInList():
            if food.get() in list(data.상품명): # 데이터에 음식이 존재할 경우 음식 검색 화면으로 전환
                return SearchFood
            else: # 데이터에 음식이 존재하지 않을 경우 음식 추가 화면으로 전환
                return AddFood
        Button(self, text='취소', font=fonts[3], padx=10, pady=5, **styles[0], command=lambda: master.switch_frame(MainMenu)).grid(row=6, column=0, pady=(60, 0), sticky='w')
        Button(self, text='다음', font=fonts[3], padx=10, pady=5, **styles[0], command=lambda: master.switch_frame(isInList())).grid(row=6, column=2, pady=(60, 0), sticky='e')

# [2]-1 편의점 다이어트 음식 검색
class SearchFood(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        target = data[data['상품명'] == food.get()].iloc[0]
        Label(self, text='음식 검색', font=fonts[1], fg='green').grid(row=0, column=0, columnspan=2, pady=(30, 15))
        Label(self, text='검색된 음식 정보를 확인해주세요.', font=fonts[4]).grid(row=1, column=0, columnspan=2, pady=(0, 20))
        colors = ['lightyellow', 'lightyellow', 'orange', 'skyblue', 'skyblue', 'skyblue', 'skyblue']
        for i in range(7):
            if i < 2: txt=target[i]
            elif i == 2: txt=format(int(target[i]), ',')
            else: txt='%g'%target[i]
            Label(self, text=data.columns[i]+' ', font=fonts[3]).grid(row=i+3, column=0, pady=7)
            Label(self, text=txt, font=fonts[2], bg=colors[i], width=20, relief='groove').grid(row=i+3, column=1, ipady=5)
        Button(self, text='메뉴로', font=fonts[3], padx=10, pady=5, **styles[0], command=lambda: master.switch_frame(MainMenu)).grid(column=0, columnspan=2, pady=(25, 0))

# [2]-2 편의점 다이어트 음식 추가
class AddFood(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text='음식 추가', font=fonts[1], fg='green').grid(row=0, column=0, columnspan=6, pady=(30, 15))
        Label(self, text='추가할 음식 정보를 입력해주세요.', font=fonts[4]).grid(row=1, column=0, columnspan=6, pady=(0, 15))
        input1 = Entry(self, font=fonts[2], bg='lightyellow', justify=CENTER)
        input2 = Entry(self, font=fonts[2], bg='orange', justify=CENTER)
        input3 = Entry(self, font=fonts[2], bg='skyblue', justify=CENTER)
        input4 = Entry(self, font=fonts[2], bg='skyblue', justify=CENTER)
        input5 = Entry(self, font=fonts[2], bg='skyblue', justify=CENTER)
        input6 = Entry(self, font=fonts[2], bg='skyblue', justify=CENTER)
        input1.insert(0, food.get())
        input1.grid(row=3, column=1, columnspan=5, ipady=5, pady=5)
        inputList = [input1, input2, input3, input4, input5, input6]
        btnLabel = ['단백질', '샐러드', '영양바류', '음료', '기타']
        category = StringVar()
        for i in range(7):
            Label(self, text=data.columns[i]+' ', font=fonts[3]).grid(row=i+3, column=0, pady=7)
            if i < 2: continue
            inputList[i-1].grid(row=i+3, column=1, columnspan=5, ipady=3, pady=5)
            btn = Radiobutton(self, text=btnLabel[i-2], font=fonts[3], value=btnLabel[i-2], variable=category)
            if i == 2: btn.select()
            btn.grid(row=4, column=i-1)
        # 음식 추가 함수
        def saveFood():
            new_food = [i.get() for i in inputList]
            new_food.insert(1, category.get())
            new_food[3] = int(new_food[3])
            new_df = data.append(pd.Series(new_food, index=data.columns), ignore_index=True).sort_values('칼로리(kcal)') # 기존 데이터와 결합 후 칼로리 낮은 순으로 정렬
            new_df.to_csv(paths[0], index=False, encoding='cp949')
            notification.notify(
                title='성균 다이어트학개론',
                message='음식이 추가되었습니다.',
                app_icon=paths[1],
                timeout=1
            )
        Button(self, text='취소', font=fonts[3], padx=10, pady=5, **styles[0], command=lambda: master.switch_frame(MainMenu)).grid(row=10, column=0, pady=(15, 0), sticky='w')
        Button(self, text='추가', font=fonts[3], padx=10, pady=5, **styles[0], command=lambda: [saveFood(), master.switch_frame(MainMenu)]).grid(row=10, column=5, pady=(15, 0), sticky='e')

# [3] 인적 사항 변경
class MenuThree(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text='인적 사항', font=fonts[1], fg='green').grid(column=0, columnspan=3, pady=30)
        infoList = ['이름/별명', '성별', '나이', '키(cm)', '현재 몸무게(kg)']
        for i in range(5):
            Label(self, text=infoList[i]+'  ', font=fonts[3]).grid(row=i+1, column=0, pady=15)
        ID = Entry(self, font=fonts[2], bg='lightyellow', justify=CENTER)
        Gender = IntVar()
        btn_male = Radiobutton(self, text='남성', font=fonts[2], value=0, variable=Gender)
        btn_female = Radiobutton(self, text='여성', font=fonts[2], value=1, variable=Gender)
        Age = Entry(self, font=fonts[2], bg='orange', justify=CENTER)
        Height = Entry(self, font=fonts[2], bg='skyblue', justify=CENTER)
        Weight = Entry(self, font=fonts[2], bg='skyblue', justify=CENTER)
        if g == 0: btn_male.select()
        else: btn_female.select()
        ID.insert(0, nickname); Age.insert(0, a); Height.insert(0, '%g'%h); Weight.insert(0, '%g'%w)
        ID.grid(row=1, column=1, columnspan=2, ipady=5)
        btn_male.grid(row=2, column=1)
        btn_female.grid(row=2, column=2)
        Age.grid(row=3, column=1, columnspan=2, ipady=5)
        Height.grid(row=4, column=1, columnspan=2, ipady=5)
        Weight.grid(row=5, column=1, columnspan=2, ipady=5)
        # 사용자 정보 변경 함수
        def saveInfo():
            global nickname, g, a, h, w
            nickname, g, a, h, w = ID.get(), int(Gender.get()), int(Age.get()), float(Height.get()), float(Weight.get())
            notification.notify(
                title='성균 다이어트학개론',
                message='인적 사항이 변경되었습니다.',
                app_icon=paths[1],
                timeout=1
            )
        Button(self, text='취소', font=fonts[3], padx=10, pady=5, **styles[0], command=lambda: master.switch_frame(MainMenu)).grid(row=6, column=0, pady=(30, 0), sticky='w')
        Button(self, text='변경', font=fonts[3], padx=10, pady=5, **styles[0], command=lambda: [saveInfo(), master.switch_frame(MainMenu)]).grid(row=6, column=2, pady=(30, 0), sticky='e')

# 프로그램 실행
if __name__ == '__main__':
    app = SKKUDiet()
    app.mainloop()
    os.system('pause')