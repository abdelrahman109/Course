import sqlite3
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys
import MySQLdb


MainUI, _ = loadUiType('main.ui')


class Main(QMainWindow, MainUI):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Db_Connect()
        self.Handel_Buttons()
        self.Ui_Changes()
        self.Open_Login_Tab()
        self.Show_ALL_People()
        self.Show_t5sos()
        self.Show_tmam()
        self.Show_eldyana()
        self.Show_hala()

    def Ui_Changes(self):  # Ui changes in login

        self.tabWidget.tabBar().setVisible(False)
        self.tabWidget_2.tabBar().setVisible(False)
        self.tabWidget_3.tabBar().setVisible(False)
        self.tabWidget_4.tabBar().setVisible(False)

    def Db_Connect(self):
        self.db = sqlite3.connect('work_full_system.db')
        self.cur = self.db.cursor()

    def Handel_Buttons(self):  # handle all buttons in our app
        self.pushButton_12.clicked.connect(self.Open_Afrad_Tab)
        self.pushButton_35.clicked.connect(self.Show_Byanat_Tab)
        self.pushButton_36.clicked.connect(self.Tsgel_Agaza_Tab)
        self.pushButton_37.clicked.connect(self.Show_Byanat_Alw7da)
        self.pushButton_38.clicked.connect(self.Add_mostndat_Tab)
        self.pushButton_28.clicked.connect(self.Open_M5azn_Tab)
        self.pushButton_35.clicked.connect(self.Show_Byanat_Tab)
        self.pushButton_36.clicked.connect(self.Tsgel_Agaza_Tab)
        self.pushButton_37.clicked.connect(self.Show_Byanat_Alw7da)
        self.pushButton_38.clicked.connect(self.Add_mostndat_Tab)
        self.pushButton_15.clicked.connect(self.Open_Sla7_Tab)
        self.pushButton_16.clicked.connect(self.Open_Mo3dat_Fnya_tab)
        self.pushButton_17.clicked.connect(self.Open_Kema_Tab)
        self.pushButton_18.clicked.connect(self.Open_Eshara_Tab)
        self.pushButton_19.clicked.connect(self.Open_tkdes_Tab)
        self.pushButton_30.clicked.connect(self.Open_Est3dad_Ktaly_Tab)
        self.pushButton_20.clicked.connect(self.Open_Mohndsen_Tab)
        self.pushButton_29.clicked.connect(self.Open_mdf3ya_Tab)
        self.pushButton_21.clicked.connect(self.Open_T3b2a_Tab)
        self.pushButton_13.clicked.connect(self.Open_Malyat_Tab)
        self.pushButton_39.clicked.connect(self.Open_23dadat_Tab)
        self.pushButton_25.clicked.connect(self.Add_New_Person)
        self.pushButton_22.clicked.connect(self.Person_Data_search)
        self.pushButton_48.clicked.connect(self.add_t5sos)
        self.pushButton_45.clicked.connect(self.add_tmam)
        self.pushButton_23.clicked.connect(self.Edit_Person_Data)
        self.pushButton_24.clicked.connect(self.Delete_Person_Data)

    def Handel_login(self):  # handle login
        pass

    def Handel_Reset_Password(self):   # handle reset password
        pass

    def Handel_To_Day_Work(self):  # handle To day operation
        pass

    # show personal data of all people  # show all person in the list
    def Show_ALL_People(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)

        self.cur.execute('''
            SELECT rkm_kwmy , rotba_drga ,  name , rkm_3skry , el3nwan , tare5_eltgned , tare5_eltsre7 , tare5_aldm , 
            ayam_altwgod , aldyana , elhala_alagtma3ya , alt5sos, altmam , mobile , mobile2 FROM bynat
        ''')

        data = self.cur.fetchall()
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

    def Add_New_Person(self):  # add a new person
        rkm_kwmy1 = self.lineEdit_12.text()
        rotba_drga1 = self.lineEdit_2.text()
        name1 = self.lineEdit_3.text()
        rkm_3skry1 = self.lineEdit_4.text()
        el3nwan1 = self.lineEdit_5.text()
        aldyana1 = self.comboBox_3.currentIndex()
        elhala1 = self.comboBox_5.currentIndex()
        alt5sos1 = self.comboBox_7.currentIndex()
        altmam1 = self.comboBox_6.currentIndex()
        mobile1 = self.lineEdit_8.text()
        mobile21 = self.lineEdit_11.text()
        # tare5_eltgned =
        # tare5_eltsre7 =
        # tare5_aldm =
        # tare5_el3wda =
        # ayam_altwgod =
        # picture =
        # barcode_pic =
        # wseka_t3arof =
        # t72e2_sh5sya =
        # bta2a =
        # ro5sa =
        # nmozg_1c =
        self.cur.execute(
            f"INSERT INTO bynat (rkm_kwmy, rotba_drga, name, rkm_3skry, el3nwan , mobile, mobile2, aldyana , elhala_alagtma3ya , alt5sos , altmam) VALUES ('{rkm_kwmy1}', '{rotba_drga1}', '{name1}', '{rkm_3skry1}', '{el3nwan1}', '{mobile1}', '{mobile21}', '{aldyana1}', '{elhala1}', '{alt5sos1}', '{altmam1}')")
        self.db.commit()
        self.Show_ALL_People()
        self.statusBar().showMessage('تم تسجيل بيانات فرد جديد بنجاح')
        QMessageBox.information(
            self, "success", "تم تسجيل بيانات فرد جديد بنجاح")
        self.Set_to_clear()

    def Set_to_clear(self):
        self.lineEdit_12.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_11.setText('')
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)

    def Person_Data_search(self):
        person_code = self.lineEdit_12.text()
        self.cur.execute(
            f"SELECT * FROM bynat WHERE rkm_kwmy = '{person_code}'")
        data = self.cur.fetchone()
        self.lineEdit_2.setText(data[2])  # الرتبة
        self.lineEdit_3.setText(data[3])  # الأسم
        self.lineEdit_4.setText(str(data[4]))  # رقم عسكرى
        self.lineEdit_5.setText(data[5])  # العنوان
        self.comboBox_3.setCurrentIndex(int(data[12]))  # الديانة
        self.comboBox_7.setCurrentIndex(int(data[14]))  # التخصص
        self.lineEdit_8.setText(data[16])  # رقم الموبيل
        self.comboBox_5.setCurrentIndex(int(data[13]))  # الحاله الأجتماعية
        self.comboBox_6.setCurrentIndex(int(data[15]))  # التمام
        self.lineEdit_11.setText(data[17])  # رقم أقرب الأقارب
        self.statusBar().showMessage('تم إيجاد بيانات الفرد بنجاح')
        QMessageBox.information(self, "success", "تم إيجاد بيانات الفرد بنجاح")

    def Delete_Person_Data(self):  # delete person data
        person_code = self.lineEdit_12.text()
        delet = QMessageBox.warning(
            self, "مسح المعلومات", "هل أنت متأكد من مسح البيانات", QMessageBox.Yes | QMessageBox.No)
        if delet == QMessageBox.Yes:
            self.cur.execute(
                f"DELETE FROM bynat WHERE rkm_kwmy = '{person_code}'")
            self.db.commit()
            self.Show_ALL_People()
            self.statusBar().showMessage('تم حذف بيانات الفرد بنجاح')
            QMessageBox.information(
                self, "success", "تم حذف بيانات الفرد بنجاح")
            self.Set_to_clear()

    def Edit_Person_Data(self):  # Edit person data
        rkm_kwmy1 = self.lineEdit_12.text()
        rotba_drga1 = self.lineEdit_2.text()
        name1 = self.lineEdit_3.text()
        rkm_3skry1 = self.lineEdit_4.text()
        el3nwan1 = self.lineEdit_5.text()
        aldyana1 = self.comboBox_3.currentIndex()
        elhala1 = self.comboBox_5.currentIndex()
        alt5sos1 = self.comboBox_7.currentIndex()
        altmam1 = self.comboBox_6.currentIndex()
        mobile1 = self.lineEdit_8.text()
        mobile21 = self.lineEdit_11.text()
        self.cur.execute(f" UPDATE bynat SET rkm_kwmy = '{rkm_kwmy1}' ,rotba_drga = '{rotba_drga1}', name='{name1}', rkm_3skry='{rkm_3skry1}', el3nwan = '{el3nwan1}' , mobile= '{mobile1}', mobile2= '{mobile21}', aldyana ='{aldyana1}', elhala_alagtma3ya='{elhala1}' , alt5sos ='{alt5sos1}', altmam='{altmam1}' WHERE rkm_kwmy ='{rkm_kwmy1}'")
        self.db.commit()
        self.Show_ALL_People()
        self.statusBar().showMessage('تم تحديث بيانات الفرد بنجاح')
        QMessageBox.information(self, "success", "تم تحديث بيانات الفرد بنجاح")
        self.Set_to_clear()

    def Open_Login_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def add_t5sos(self):
        elt5sos = self.lineEdit_7.text()
        self.cur.execute(f"INSERT INTO t5sos ( t5sos )VALUES ('{elt5sos}')")
        self.db.commit()
        self.Show_t5sos()

    def Show_t5sos(self):
        self.cur.execute('''
            SELECT t5sos FROM t5sos 
        ''')
        t5sos = self.cur.fetchall()
        for t5sos1 in t5sos:
            self.comboBox_7.addItem(t5sos1[0])

    def Show_eldyana(self):
        self.cur.execute('''
            SELECT dyana FROM dyana 
        ''')
        dyana = self.cur.fetchall()
        for dyana1 in dyana:
            self.comboBox_3.addItem(dyana1[0])

    def Show_hala(self):
        self.cur.execute('''
                    SELECT elhala FROM elhala 
                ''')
        hala = self.cur.fetchall()
        for hala1 in hala:
            self.comboBox_5.addItem(hala1[0])

    def add_tmam(self):
        eltmam = self.lineEdit_6.text()
        self.cur.execute(f"INSERT INTO tmam ( tmam )VALUES ('{eltmam}')")
        self.db.commit()
        self.Show_tmam()

    def Show_tmam(self):
        self.cur.execute('''
                SELECT tmam FROM tmam 
                ''')
        tmam = self.cur.fetchall()
        for tmam1 in tmam:
            self.comboBox_6.addItem(tmam1[0])


    def Open_Afrad_Tab(self):
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)

    def Show_Byanat_Tab(self):
        self.tabWidget_2.setCurrentIndex(1)

    def Tsgel_Agaza_Tab(self):
        self.tabWidget_2.setCurrentIndex(2)

    def Show_Byanat_Alw7da(self):
        self.tabWidget_2.setCurrentIndex(3)

    def Add_mostndat_Tab(self):
        self.tabWidget_2.setCurrentIndex(4)


    def Open_Malyat_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_M5azn_Tab(self):
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_3.setCurrentIndex(0)

    def Open_Sla7_Tab(self):
        self.tabWidget_3.setCurrentIndex(1)

    def Open_Mo3dat_Fnya_tab(self):
        self.tabWidget_3.setCurrentIndex(2)

    def Open_Kema_Tab(self):
        self.tabWidget_3.setCurrentIndex(3)

    def Open_Eshara_Tab(self):
        self.tabWidget_3.setCurrentIndex(4)

    def Open_tkdes_Tab(self):
        self.tabWidget_3.setCurrentIndex(5)

    def Open_Mohndsen_Tab(self):
        self.tabWidget_3.setCurrentIndex(6)

    def Open_T3b2a_Tab(self):
        self.tabWidget_3.setCurrentIndex(7)

    def Open_Hamla_Tab(self):
        self.tabWidget_3.setCurrentIndex(8)

    def Open_mdf3ya_Tab(self):
        self.tabWidget_3.setCurrentIndex(9)

    def Open_Est3dad_Ktaly_Tab(self):
        self.tabWidget_3.setCurrentIndex(10)

    def Open_23dadat_Tab(self):
        self.tabWidget.setCurrentIndex(4)




def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
