from tkinter import *
import os
from tkinter import filedialog
from os import listdir
from os.path import isfile, join
from PIL import Image, ImageTk
import numpy as np
import os.path
from sklearn import tree

check = []
X_features_test = []

class BanglaCheracterOCR:
    clf = tree.DecisionTreeClassifier()
    def __init__(self, master):
        self.master = master
        master.title("BANGLA CHARACTER RECOGNITION")
        master.geometry("600x500+400+100")
        master.resizable(width=False, height=False)
        self.leftframe = Frame(master, width=300, height=400, relief=SUNKEN)
        self.leftframe.place(x=0, y=0)
        self.rightframe = Frame(master, width=300, height=400,relief=SUNKEN)
        self.rightframe.place(x=300, y=0)
        self.browse_button = Button(self.leftframe, padx=20, pady=10, bd=6, fg="yellow", font=('arial', 15, 'bold'),
                                    text="Browse",
                                    bg="green", command=self.Browse_Image)  # action goes down
        self.browse_button.place(x=80, y=160)
        self.Result_button = Button(self.leftframe, padx=20, pady=10, bd=6, fg="Blue2", font=('arial', 15, 'bold'),
                                    text="Result",
                                    bg="bisque", command=self.Get_Result)  # action goes down
        self.Result_button.place(x=80, y=310)
        self.train_button = Button(self.leftframe, padx=20, pady=10, bd=6, fg="black", font=('arial', 15, 'bold'),
                             text="Train DataSet",
                             bg="purple1",command=self.Train_dataset)  # action goes down
        self.train_button.place(x=50, y=50)
    def Browse_Image(self):
        self.imagefile = filedialog.askopenfilename(
            initialdir="E:/Programming OOP/BanglaCheracter/TestDataSet",
            title="Select file", filetypes=(("PNG file", ".png"), ("All Files", ".*")))
        self.browse_file_name=os.path.basename(self.imagefile)
        print(self.browse_file_name,"**")

        image = Image.open(self.imagefile)
        photo = ImageTk.PhotoImage(image)

        #self.img = PhotoImage(file=self.imagefile)
        self.photo_label = Label(self.rightframe, image=photo, bg="floral white",justify=CENTER)
        self.photo_label.image = photo
        self.photo_label.config(height=100, width=180)
        self.photo_label.place(x=50, y=130)
    def Train_dataset(self):
        X_features = []
        Y_lebel=[]
        mypath = 'E:/Programming OOP/BanglaCheracter/TrainDataSet/0'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for k in range(0, len(onlyfiles)):
            im = Image.open(onlyfiles[k]).convert('L')
            data = np.array(im)
            temp = []
            for i in range(0, 32):
                for j in range(0, 32):
                    temp.append(data[i][j])
            X_features.append(temp)
            Y_lebel.append(0)
        mypath = 'E:/Programming OOP/BanglaCheracter/TrainDataSet/1'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for k in range(0, len(onlyfiles)):
            im = Image.open(onlyfiles[k]).convert('L')
            data = np.array(im)
            temp = []
            for i in range(0, 32):
                for j in range(0, 32):
                    temp.append(data[i][j])
            X_features.append(temp)
            Y_lebel.append(1)
        mypath = 'E:/Programming OOP/BanglaCheracter/TrainDataSet/2'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for k in range(0, len(onlyfiles)):
            im = Image.open(onlyfiles[k]).convert('L')
            data = np.array(im)
            temp = []
            for i in range(0, 32):
                for j in range(0, 32):
                    temp.append(data[i][j])
            X_features.append(temp)
            Y_lebel.append(2)
        mypath = 'E:/Programming OOP/BanglaCheracter/TrainDataSet/3'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for k in range(0, len(onlyfiles)):
             im = Image.open(onlyfiles[k]).convert('L')
             data = np.array(im)
             temp = []
             for i in range(0, 32):
                for j in range(0, 32):
                    temp.append(data[i][j])
             X_features.append(temp)
             Y_lebel.append(3)
        mypath = 'E:/Programming OOP/BanglaCheracter/TrainDataSet/4'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for k in range(0, len(onlyfiles)):
            im = Image.open(onlyfiles[k]).convert('L')
            data = np.array(im)
            temp = []
            for i in range(0, 32):
                for j in range(0, 32):
                    temp.append(data[i][j])
            X_features.append(temp)
            Y_lebel.append(4)
        mypath = 'E:/Programming OOP/BanglaCheracter/TrainDataSet/5'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for k in range(0, len(onlyfiles)):
            im = Image.open(onlyfiles[k]).convert('L')
            data = np.array(im)
            temp = []
            for i in range(0, 32):
                for j in range(0, 32):
                    temp.append(data[i][j])
            X_features.append(temp)
            Y_lebel.append(5)
        mypath = 'E:/Programming OOP/BanglaCheracter/TrainDataSet/6'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for k in range(0, len(onlyfiles)):
            im = Image.open(onlyfiles[k]).convert('L')
            data = np.array(im)
            temp = []
            for i in range(0, 32):
                for j in range(0, 32):
                    temp.append(data[i][j])
            X_features.append(temp)
            Y_lebel.append(6)
        mypath = 'E:/Programming OOP/BanglaCheracter/TrainDataSet/7'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for k in range(0, len(onlyfiles)):
            im = Image.open(onlyfiles[k]).convert('L')
            data = np.array(im)
            temp = []
            for i in range(0, 32):
                for j in range(0, 32):
                    temp.append(data[i][j])
            X_features.append(temp)
            Y_lebel.append(7)
        mypath = 'E:/Programming OOP/BanglaCheracter/TrainDataSet/8'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for k in range(0, len(onlyfiles)):
            im = Image.open(onlyfiles[k]).convert('L')
            data = np.array(im)
            temp = []
            for i in range(0, 32):
                for j in range(0, 32):
                    temp.append(data[i][j])
            X_features.append(temp)
            Y_lebel.append(8)
        mypath = 'E:/Programming OOP/BanglaCheracter/TrainDataSet/9'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for k in range(0, len(onlyfiles)):
            im = Image.open(onlyfiles[k]).convert('L')
            data = np.array(im)
            temp = []
            for i in range(0, 32):
                for j in range(0, 32):
                    temp.append(data[i][j])
            X_features.append(temp)
            Y_lebel.append(9)
        mypath = 'E:/Programming OOP/BanglaCheracter/TrainDataSet/10'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for k in range(0, len(onlyfiles)):
            im = Image.open(onlyfiles[k]).convert('L')
            data = np.array(im)
            temp = []
            for i in range(0, 32):
                for j in range(0, 32):
                    temp.append(data[i][j])
            X_features.append(temp)
            Y_lebel.append(10)
        self.clf.fit(X_features, Y_lebel)
        print("TRAINING IS FINISHED")
    def Get_Result(self):
        print(self.browse_file_name)
        X_feature_test=[]
        im = Image.open(self.browse_file_name).convert('L')
        data = np.array(im)
        temp = []
        for i in range(0, 32):
            for j in range(0, 32):
                temp.append(data[i][j])
        X_feature_test.append(temp)
        print("Your outpur is: ",end="")
        output=self.clf.predict(X_feature_test)
        print(output[0])
        if output[0]==0:
            output_unicode="\u0985"
        elif output[0]==1:
            output_unicode = "\u0986"
        elif output[0] == 2:
            output_unicode = "\u0987"
        elif output[0] == 3:
            output_unicode = "\u0988"
        elif output[0] == 4:
            output_unicode = "\u0989"
        elif output[0] == 5:
            output_unicode = "\u098A"
        elif output[0] == 6:
            output_unicode = "\u098B"
        elif output[0] == 7:
            output_unicode = "\u098F"
        elif output[0] == 8:
            output_unicode = "\u0990"
        elif output[0] == 9:
            output_unicode = "\u0993"
        elif output[0] == 10:
            output_unicode = "\u0994"
        #print(output_unicode)
        labelfont = ('Helvetica',25,'bold')
        self.result_label = Label(self.rightframe, text=output_unicode,anchor=CENTER)
        self.result_label.config(height=3, width=10)
        self.result_label.place(x=50, y=280)
        self.result_label.config(bg='red', fg='black')
        self.result_label.config(font=labelfont)
root = Tk()
my_gui = BanglaCheracterOCR(root)
root.mainloop()
