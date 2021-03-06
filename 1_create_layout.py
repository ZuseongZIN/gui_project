from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Juseong GUI")

#파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill ="x", padx=5, pady=5) #간격 띄우기 fill은 x축으로 쫘악 벌려줌

btn_add_file = Button(file_frame, padx=5, pady=5, width=12,text = "File Add")
btn_add_file.pack(side = "left")

btn_del_file = Button(file_frame, padx=10, pady=5, width=12,text = "Checked file delete")
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

btn_dest_path = Button(path_frame, text = "Find", width=10)
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

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12)
btn_start.pack(side="right",padx=5, pady=5)

root.resizable(False,False)
root.mainloop()