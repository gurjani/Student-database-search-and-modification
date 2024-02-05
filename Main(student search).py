from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random
from pymongo import MongoClient
from bson.objectid import ObjectId

# Sample data
LNames = ['აბაშიძე', 'გიგაური', 'არჩვაძე', 'ახალაია', 'ბაძაღუა', 'ბერიანიძე', 'ბერიშვილი', 'გვენცაძე', 'დალაქიშვილი',
          'ანთიძე', 'გიორგაძე', 'გოგალაძე', 'გოცირიძე', 'ვარდიძე', 'ზარანდია', 'თადუმაძე', 'ლაბაძე', 'კვარაცხელია',
          'კუსრაძე', 'კვესელავა', 'კაპანაძე', 'კასრაძე', 'კვინიკაძე', 'კოპაძე', 'კანკია', 'კორძაია', 'მიქავა', 'მელია',
          'მონიავა', 'ნიაური', 'ლაცაბიძე', 'მიქაძე', 'ნემსიწვერიძე', 'მაისურაძე', 'მაცაბერიძე', 'მჟავია', 'მაჩალაძე',
          'ოდიშარია', 'მეტრეველი', 'ნეფარიძე', 'მოდებაძე', 'მარჯანიძე', 'მუმლაძე', 'ნასრაშვილი', 'ჯანჯღავა', 'მოსია',
          'ნოზაძე', 'ნუცუბიძე', 'ონიანი', 'ოქრუაშვილი', 'პერტია', 'რაზმაძე', 'რევაზაშვილი', 'საგანელიძე', 'ჯახაია',
          'სალუქვაძე', 'სამსონაშვილი', 'სამხარაძე', 'სარალიძე', 'სართანია', 'სარიშვილი', 'სიმონიშვილი', 'სხილაძე',
          'ხურციძე', 'სიხარულიძე', 'ტაბატაძე', 'ფაცაცია', 'ფილაური', 'ფუხაშვილი', 'ქობალია', 'ყიფშიძე', 'შაინიძე',
          'ფიფია', 'შენგელია', 'შეროზია', 'შველიძე', 'ჩხეიძე', 'ჩადუნელი', 'ჩიკვაშვილი', 'ცქიტიშვილი', 'ჩოკორაია',
          'ცაგურია', 'ცერცვაძე', 'ცუხიშვილი', 'ძინძიბაძე', 'წერეთელი', 'წიკლაური', 'ჭავჭანიძე', 'ჩირაძე', 'ჭელიძე',
          'ჭანტურია', 'სირაძე', 'შონია', 'ხანჯალაძე', 'ხარაზიშვილი', 'ხელაძე', 'ხვინგია', 'ხუციშვილი', 'ჯანელიძე',
          'ჯოხაძე']
FNames = ['ანა', 'ანუკი', 'ბარბარე', 'გვანცა', 'დიანა', 'ეკა', 'ელენე', 'ვერონიკა', 'ვიქტორია', 'თათია', 'ლამზირა',
          'თეა', 'თეკლე', 'თინიკო', 'თამარი', 'იზაბელა', 'ია', 'იამზე', 'ლია', 'ლიკა', 'ლანა', 'მარიკა', 'მანანა',
          'მაია', 'მაკა', 'მარიამი', 'ნანა', 'ნანი', 'ნატა', 'ნატო', 'ნინო', 'ნონა', 'ოლიკო', 'ქეთევანი', 'სალომე',
          'სოფიკო', 'ნია', 'ქრისტინე', 'შორენა', 'ხატია', 'ალეკო', 'ალიკა', 'ამირან', 'ანდრია', 'არჩილი', 'ასლანი',
          'ბაჩუკი', 'ბექა', 'გიგა', 'გიორგი', 'დავითი',
          'გიგი', 'გოგა', 'დათა', 'ერეკლე', 'თემური', 'იაკობ', 'ილია', 'ირაკლი', 'ლადო', 'ლაშა', 'მიხეილ',
          'ნიკა', 'ოთარი', 'პაატა', 'რამაზ', 'რამინი', 'რატი', 'რაული', 'რევაზი', 'რომა', 'რომანი', 'სანდრო',
          'საბა', 'სერგი', 'სიმონ', 'შალვა', 'შოთა', 'ცოტნე', 'ჯაბა']

Subject = ['პროგრამირების საფუძვლები', 'კალკულუსი II', 'შესავალი ფიზიკაში', 'კომპიუტერული უნარჩვევები',
           'ქიმიის შესავალი', 'ბიოლოგიის შესავალი', 'ალგორითმები I', 'შესავალი ელექტრონიკაში',
           'მონაცემთა სტრუქტურები', 'ალგორითმები II']

Point = [str(i) for i in range(101)]
ch = random.choice

client = MongoClient('localhost', 27017)
db = client['Students']
collection = db['Records']
collection.delete_many({})

# Generate student records
Stud_recs = [' '.join([ch(LNames), ch(FNames), ch(Subject), ch(Point)]) for _ in range(10)]


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1103, 869)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.find_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.find_pushButton.setGeometry(QtCore.QRect(490, 150, 111, 41))
        self.find_pushButton.setObjectName("find_pushButton")
        self.renew_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.renew_pushButton.setGeometry(QtCore.QRect(490, 220, 111, 41))
        self.renew_pushButton.setObjectName("renew_pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 290, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.add_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_pushButton.setGeometry(QtCore.QRect(490, 80, 211, 41))
        self.add_pushButton.setObjectName("add_pushButton")
        self.id_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.id_lineEdit.setGeometry(QtCore.QRect(290, 80, 181, 41))
        self.id_lineEdit.setObjectName("id_lineEdit")
        self.lname_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lname_lineEdit.setGeometry(QtCore.QRect(290, 150, 181, 41))
        self.lname_lineEdit.setObjectName("lname_lineEdit")
        self.fname_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.fname_lineEdit.setGeometry(QtCore.QRect(290, 220, 181, 41))
        self.fname_lineEdit.setObjectName("fname_lineEdit")
        self.subject_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.subject_lineEdit.setGeometry(QtCore.QRect(290, 290, 181, 41))
        self.subject_lineEdit.setObjectName("subject_lineEdit")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 430, 181, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.id_label = QtWidgets.QLabel(self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(90, 80, 121, 41))
        self.id_label.setObjectName("id_label")
        self.lname_label = QtWidgets.QLabel(self.centralwidget)
        self.lname_label.setGeometry(QtCore.QRect(90, 150, 121, 41))
        self.lname_label.setObjectName("lname_label")
        self.fname_label = QtWidgets.QLabel(self.centralwidget)
        self.fname_label.setGeometry(QtCore.QRect(90, 220, 121, 41))
        self.fname_label.setObjectName("fname_label")
        self.subject_label = QtWidgets.QLabel(self.centralwidget)
        self.subject_label.setGeometry(QtCore.QRect(90, 290, 121, 41))
        self.subject_label.setObjectName("subject_label")
        self.close_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.close_pushButton.setGeometry(QtCore.QRect(970, 770, 93, 28))
        self.close_pushButton.setObjectName("close_pushButton")
        self.score_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.score_lineEdit.setGeometry(QtCore.QRect(290, 360, 181, 41))
        self.score_lineEdit.setObjectName("score_lineEdit")
        self.score_label = QtWidgets.QLabel(self.centralwidget)
        self.score_label.setGeometry(QtCore.QRect(90, 360, 121, 41))
        self.score_label.setObjectName("score_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1103, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_pushButton.clicked.connect(self.adddata)
        self.find_pushButton.clicked.connect(self.finddata)
        self.renew_pushButton.clicked.connect(self.renewdata)
        self.pushButton_3.clicked.connect(self.deleteData)
        self.pushButton_5.clicked.connect(self.insertdata)
        self.close_pushButton.clicked.connect(self.closeapp)

    def adddata(self):
        for i in Stud_recs:
            student = {
                'fname': i.split()[1],
                'lname': i.split()[0],
                'subject': ' '.join(i.split(' ')[2:-1]),
                'score': i.split()[-1]
            }
            collection.insert_one(student)
        people = collection.find({})
        for i in people:
            print(i)

    def finddata(self):
        if self.fname_lineEdit.text():
            x = self.fname_lineEdit.text()
            print(x)
            result = collection.find({'fname': x})
            for i in result:
                print(i)
        elif self.lname_lineEdit.text():
            x = self.lname_lineEdit.text()
            print(x)
            result = collection.find({'lname': x})
            for i in result:
                print(i)
        elif self.score_lineEdit.text():
            x = self.score_lineEdit.text()
            print(x)
            result = collection.find({'score': x})
            for i in result:
                print(i)
        elif self.subject_lineEdit.text():
            x = self.subject_lineEdit.text()
            print(x)
            result = collection.find({'subject': x})
            for i in result:
                print(i)
        elif self.id_lineEdit.text():
            x = self.id_lineEdit.text()
            print(x)
            result = collection.find({'_id': ObjectId(x)})
            for i in result:
                print(i)

    def renewdata(self):
        y = self.id_lineEdit.text()
        new_last_name = self.lname_lineEdit.text()
        new_first_name = self.fname_lineEdit.text()
        new_subject = self.subject_lineEdit.text()
        new_score = self.subject_lineEdit.text()
        collection.update_one({'_id': ObjectId(y)},
                              {"$set": {"lname": new_last_name, "fname": new_first_name, "subject": new_subject,
                                        "score": new_score}})
        result = collection.find({'_id': ObjectId(y)})
        for i in result:
            print(i)

    def deleteData(self):
        x = self.id_lineEdit.text()
        collection.delete_one({"_id": ObjectId(x)})
        people = collection.find({})
        print("Updated data:")
        for i in people:
            print(i)

    def insertdata(self):
        add_lname = self.lname_lineEdit.text()
        add_fname = self.fname_lineEdit.text()
        add_subject = self.subject_lineEdit.text()
        add_score = self.subject_lineEdit.text()
        document = {
            'fname': add_fname,
            'lname': add_lname,
            'subject': add_subject,
            'score': add_score
        }
        collection.insert_one(document)
        people = collection.find({})
        print("Updated data:")
        for i in people:
            print(i)

    def closeapp(self):
        sys.exit(app.exec_())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.find_pushButton.setText(_translate("MainWindow", "ძებნა"))
        self.renew_pushButton.setText(_translate("MainWindow", "განახლება"))
        self.pushButton_3.setText(_translate("MainWindow", "წაშლა"))
        self.add_pushButton.setText(_translate("MainWindow", "ყველა ჩანაწერის გაკეთება"))
        self.pushButton_5.setText(_translate("MainWindow", "ჩაწერა"))
        self.id_label.setText(_translate("MainWindow", "იდენტ."))
        self.lname_label.setText(_translate("MainWindow", "გვარი"))
        self.fname_label.setText(_translate("MainWindow", "სახელი"))
        self.subject_label.setText(_translate("MainWindow", "საგანი"))
        self.close_pushButton.setText(_translate("MainWindow", "Close"))
        self.score_label.setText(_translate("MainWindow", "შეფასება"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# Close the database connection

client.close()
# C:\Program Files (x86)\python\Scripts\pyuic5.exe
# $FileName$ -o $FileNameWithoutExtension$.py
# $FileDir$
# pip install numpy
# pip install pymongo
# https://pastebin.com/CCpTDgFT
# https://pastebin.com/5SV3DZbv?fbclid=IwAR2FVrr9iGnDkR4Q1FTasXdxt-jwdtcMMoqLjqW_XfpainPfk9Xq1Xe3D5Q
