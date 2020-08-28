from tkinter import * # __all__ 여기에 filedialog 없으므로 별도로 명시해서 선언해줘야함
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox #메시지 박스 임포트
from tkinter import filedialog
import os
from PIL import Image
root = Tk()
root.title("Juseong GUI")

#파일 추가

def add_file():
    files = filedialog.askopenfilenames(title = "Choose files",
                                        filetypes=(("PNG file", "*.png"), ("All Files","*.*")),
                                        initialdir=r"C:\Users\JuseongJIN\PycharmProjects\gui_project") #최초에 사용자가 지정한 경로를 보여줌
    for file in files:
        list_file.insert(END,file)
#파일 삭제

def del_file():
    #print(list_file.curselection()) #curselection은 리스트 내의 인덱스를 반환해줌
    for index in reversed(list_file.curselection()): #이렇게 하면 선택된 파일을 역순으로 가지고 옴.
        list_file.delete(index)                      #예를 들어 2번째 파일과 3번째 파일이 있는데 2번째 파일을 삭제하면
                                                     #3번째 파일의 인덱스가 2로 변경되기 때문에 원하는 파일을 삭제할 수 없다
                                                     #그러므로 역순으로 삭제하는게 바람직함. reversed는 reverse와 다르게
                                                     #리스트를 역순으로 한 새로운 리스트를 반환함.
                                                     #reverse는 원본 리스트를 역순으로 바꿔버림

#저장 경로
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '': #사용자가 취소를 누를 때
        return
    # print (folder_selected)
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(0,folder_selected)


#이미지 통합

def merge_image():
    #print(list_file.get(0,END)) #모든 파일 목록을 가지고 오기
    try:
        img_width = cmb_width.get()
        if img_width == "Original":
            img_width = -1 # -1 일 때는 원본 기준으로 이미지 통합
        else:
            img_width = int(img_width)

        #간격
        img_space=cmb_space.get()
        if img_space == "narrow":
            img_space = 30
        elif img_space =="normal":
            img_space = 60
        elif img_space =="wide":
            img_space = 90
        else:
            img_space = 0

        #포맷
        img_format = cmb_format.get().lower() # png, jpg, bmp 값을 받아와서 소문자로 변경

        #############################################################################

        images = [Image.open(x) for x in list_file.get(0,END)]

        # 이미지 사이즈 리스트에 넣어서 하나씩 처리
        image_sizes = [] # [(width1,height1), (width2,height2)...]

        if img_width > -1 :
            image_sizes= [(int(img_width), int(img_width*x.size[1] / x.size[0])) for x in images] # width 값 변경
        else:
            image_sizes = [(x.size[0],x.size[1]) for x in images]
        #계산식
        #100*60 이미기자 있음 0> width를 80으로 줄인다면? height는?
        #원본 width: 원본 height = 변경 width : 변경 height
        # 100 : 60 = 80 : x
        # 100x = 4800
        # 즉 변경 height = 원본 height * 변경 width / 원본 width
        # 원본 width = x.size[0] , 원본 height = x.size[1]


        #size의 저장 방식 -> size[0] : width, size[1] :height
        # widths = [x.size[0] for x in images]
        # heights = [x.size[1] for x in images]

        #size정보는 [(10.10), (20,20)] 이런 식으로 저장됨. zip을 이용해서 정보를 뽑아보자
        widths, heights = zip(*(image_sizes))

        #최대 넓이와 높이의 총합
        max_width, total_height = max(widths), sum(heights)

        # 합치는 판 준비
        if img_space > 0 :
            total_height += (img_space * (len(images) - 1 ))


        result_img= Image.new("RGB", (max_width, total_height), (255,255,255)) #배경 흰색 255..
        y_offset=0 #y 위치

        # for img in images:
        #     result_img.paste(img,(0,y_offset))
        #     y_offset+=img.size[1] #height 값 만큼 더하기

        for idx,img in enumerate(images):
            #width가 원본유지가 아닐 때는 이미지 크기를 조정해야함
            if img_width > -1 :
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space) # height 값 + 사용자가 지정한 간격

            progress = (idx + 1)/ len(images) * 100 #실제 percent 정보를 계산
            p_var.set(progress)
            progress_bar.update()


        # 포맷 옵션 처리
        file_name = "Merge_photo." + img_format
        dest_path = os.path.join(txt_dest_path.get(),file_name)
        result_img.save(dest_path)
        msgbox.showinfo("notification", "Wokr complete!" )

    except Exception as err: # 예외처리
        msgbox.showerror("Error", err)


#합치기 프로그램 시작
def start():
    #각 옵션들 값을 확인
    print("width: " , cmb_width.get(), "interval: ", cmb_space.get(), "format: ", cmb_format.get())

    # 파일 목록 확인
    if list_file.size() ==0:
        msgbox.showwarning("warning", "Please Add Image Files")
        return

    #저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("warning", "Please Make Save Path")
        return

    merge_image()


#파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill ="x", padx=5, pady=5) #간격 띄우기 fill은 x축으로 쫘악 벌려줌

btn_add_file = Button(file_frame, padx=5, pady=5, width=12,text = "Add File", command =add_file)
btn_add_file.pack(side = "left")

btn_del_file = Button(file_frame, padx=10, pady=5, width=12,text = "Checked file delete", command = del_file)
btn_del_file.pack(side="right")

#리스트 프레임

list_frame = Frame(root)
list_frame.pack(fill="both", padx=5,pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill = "y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand = scrollbar.set)
list_file.pack(side="left", fill = "both", expand = True)
scrollbar.config(command=list_file.yview)

#저장 경로 프레임

path_frame = LabelFrame(root, text = "Path")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady = 4) #엔트리 영역 높이 4로 확장

btn_dest_path = Button(path_frame, text = "Find", width=10,command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

#옵션 프레임

frame_option = LabelFrame(root, text="Option")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="Width" , width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# 가로 넓이 콤보
opt_width = ["Original","1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state = "readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left",padx=5, pady=5)

#2. 간격 옵션 레이블
# 간격 옵션 레이블
lbl_space = Label(frame_option, text = "Interval", width=8)
lbl_space.pack(side="left",padx=5, pady=5)

#간격 옵션 콤보

opt_space = ["None","narrow", "normal", "wide"]
cmb_space = ttk.Combobox(frame_option, state = "readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left",padx=5, pady=5)

#3. 파일 포맷 옵션 레이블
# 간격 옵션 레이블
lbl_format = Label(frame_option, text="Format", width=8)
lbl_format.pack(side="left",padx=5, pady=5)

#간격 옵션 콤보

opt_format = ["png","jpg", "bmp"]
cmb_format = ttk.Combobox(frame_option, state = "readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

#진행 상황 progress bar
frame_progress = LabelFrame(root, text = "진행상황",padx=5, pady=5)
frame_progress.pack(fill="x",padx=5, pady=5)

p_var = DoubleVar()
progress_bar= ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x",padx=5, pady=5, ipady=5)

#실행 프레임

frame_run = Frame(root)
frame_run.pack(fill="x")

btn_close = Button(frame_run, padx=5, pady=5, text="Close", width=12, command=root.quit)
btn_close.pack(side="right",padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12, command = start)
btn_start.pack(side="right",padx=5, pady=5)

root.resizable(False,False)
root.mainloop()