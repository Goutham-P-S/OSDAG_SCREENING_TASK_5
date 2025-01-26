from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QFrame,QSplitter,QScrollArea,QLineEdit,QPushButton,QFileDialog,QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon,QPixmap
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import pandas as pd
from pandas.plotting import table
from matplotlib.ticker import MaxNLocator
class BridgeCostApp(QMainWindow): #create a class for main window inheriting QWidget
    def __init__(self):
        super().__init__()
        self.ini=False
        #Set title
        self.setWindowTitle("Bridge Cost Comparison Steel vs. Concrete")
        self.setWindowIcon(QIcon(r"icon.png"))
        self.setStyleSheet("background-color: #ebe5d9;font : oswald")
        #Create a central widget for the main window
        central_widget=QWidget(self)
        self.setCentralWidget(central_widget)
        
        #Set horizontal layout
        layout=QHBoxLayout()
        central_widget.setLayout(layout)
        #create menubar
        menubar=self.menuBar()
        menubar.setStyleSheet("background-color: rgb(255, 255, 255)")
        file_menu=menubar.addMenu(QIcon(r"file_icon.png"),"File")
        #create options for file menu
        new_action=QAction("New",self)
        save_action=QAction("Save",self)
        exit_action=QAction("Exit",self)
        #connect the options to functions
        new_action.triggered.connect(self.new_page)
        save_action.triggered.connect(self.save_file)
        exit_action.triggered.connect(self.close)
        file_menu.addActions([new_action,save_action,file_menu.addSeparator(),exit_action])
        #create a splitter for resizable panels
        splitter=QSplitter(Qt.Orientation.Horizontal)
        splitter.setSizes([885//3,885//3,885//3])
        splitter.setMinimumSize(885//3,600//3)
        layout.addWidget(splitter)
        #add scrollbar to the panel1 by first creating a scroll area and then adding the panel to it
        self.scroll_p1=QScrollArea(self)
        self.scroll_p1.setMinimumWidth(885//3)
        self.scroll_p1.setWidgetResizable(True)
        #create and customise the frame appearence for panel1
        self.panel1=QFrame(self.scroll_p1)
        layout_panel1=QVBoxLayout()
        self.panel1.setLayout(layout_panel1)
        self.panel1.setFrameShape(QFrame.Box)
        self.panel1.setFrameShadow(QFrame.Raised)
        self.panel1.setStyleSheet("background-color:rgb(255, 255, 255); padding:20px;  ")
        self.panel1.setMinimumSize(600,600)
        #create input fields
        self.span_length_label=QLabel("Span Length:",self.panel1)
        self.span_length_label.setStyleSheet(" font-weight: bold ")
        self.span_length=QLineEdit(self.panel1)
        self.span_length.setPlaceholderText("Enter value for span length:")
        layout_panel1.addWidget(self.span_length_label)
        layout_panel1.addWidget(self.span_length)

        self.width_label=QLabel("Width:",self.panel1)
        self.width_label.setStyleSheet(" font-weight: bold ")
        self.width=QLineEdit(self.panel1)
        self.width.setPlaceholderText("Enter value for width:")
        layout_panel1.addWidget(self.width_label)
        layout_panel1.addWidget(self.width)

        self.traffic_volume_label=QLabel("Traffic Volume(Average Daily Traffic in vehicles/day):",self.panel1)
        self.traffic_volume_label.setStyleSheet(" font-weight: bold ")
        self.traffic_volume=QLineEdit(self.panel1)
        self.traffic_volume.setPlaceholderText("Enter value for traffic volume:")
        layout_panel1.addWidget(self.traffic_volume_label)
        layout_panel1.addWidget(self.traffic_volume)

        self.Design_life_label=QLabel("Design life(years):",self.panel1)
        self.Design_life_label.setStyleSheet(" font-weight: bold ")
        self.Design_life=QLineEdit(self.panel1)
        self.Design_life.setPlaceholderText("Enter the value for design life:")
        layout_panel1.addWidget(self.Design_life_label)
        layout_panel1.addWidget(self.Design_life)
        #create a button for calculating cost
        self.calculate_costs_button=QPushButton("calculate costs",self.panel1)
        self.calculate_costs_button.clicked.connect(self.submit_form)
        self.calculate_costs_button.setCursor(Qt.PointingHandCursor)
        self.calculate_costs_button.setStyleSheet('''QPushButton {
                background-color: #ebe5d9;
                color: grey;
                font-size: 18px;
                border-radius: 5px;
                padding: 5px 10px;
                border: 2px solid gray;
            }
            QPushButton:hover {
                background-color: #ebe5ca;
                border:2px solid pink;
            }''')
        self.calculate_costs_button.setFixedSize(300,100)
        layout_panel1.addWidget(self.calculate_costs_button)
        self.scroll_p1.setWidget(self.panel1)

        #add scrollbar to the panel2 by first creating a scroll area and then adding the panel to it
        scroll_p2=QScrollArea(self)
        scroll_p2.setMinimumWidth(885//3)
        scroll_p2.setWidgetResizable(True)

        #create and customise the frame appearence for panel2
        self.panel2=QFrame(scroll_p2)
        layout_panel2=QHBoxLayout()
        self.panel2.setLayout(layout_panel2)
        self.panel2.setFrameShape(QFrame.NoFrame)
        self.panel2.setFrameShadow(QFrame.Raised)
        self.panel2.setStyleSheet("background-color:rgb(255, 255, 255); padding:20px; border:2px solid grey ")
        self.panel2.setMinimumSize(900,600)
        scroll_p2.setWidget(self.panel2)
        #add scrollbar to the panel2 by first creating a scroll area and then adding the panel to it
        scroll_p3=QScrollArea(self)
        scroll_p3.setMinimumWidth(885//3)
        scroll_p3.setWidgetResizable(True)
        #create and customise the frame appearence for panel2
        self.panel3=QFrame(scroll_p3)
        layout_panel3=QVBoxLayout()
        self.panel3.setLayout(layout_panel3)
        self.panel3.setFrameShape(QFrame.Box)
        self.panel3.setFrameShadow(QFrame.Raised)
        self.panel3.setStyleSheet("background-color:rgb(255, 255, 255); padding:20px;  ")
        self.panel3.setMinimumSize(900,600)
        scroll_p3.setWidget(self.panel3)
        #add the divided areas to the mainwindow
        splitter.addWidget(self.scroll_p1)
        splitter.addWidget(scroll_p2)
        splitter.addWidget(scroll_p3)
        layout.addWidget(splitter)
        #set the view to fullscreen
        self.showFullScreen()
        self.init_database()
#function for initializing database
    def init_database(self):
        self.conn=sqlite3.connect("Bridge_cost.db")
        self.cur=self.conn.cursor()
        self.cur.execute("""Create table if not exists cost_data(
                       Material TEXT,
                       BaseRate REAL,
                       MaintenanceRate REAL,
                       RepairRate REAL,
                       DemolitionRate REAL,
                       EnvironmentalFactor REAL,
                       SocialFactor REAL,
                       DelayFactor REAL)
                    """)
        self.cur.execute("Select count(*) from cost_data")
        if self.cur.fetchone()[0]==0:
            self.cur.executemany("insert into cost_data values(?,?,?,?,?,?,?,?)",[("Steel",3000,50,200,100,10,0.5,0.3),("Concrete",2500,75,150,80,8,0.6,0.2)])
        self.conn.commit()
# function for new option in file menu
    def new_page(self):
        layout=self.panel2.layout()
        for i in reversed(range(layout.count())):
            item=layout.itemAt(i)
            widget=item.widget()
            if widget:
                widget.deleteLater()
        layout=self.panel3.layout()
        for i in reversed(range(layout.count())):
            item=layout.itemAt(i)
            widget=item.widget()
            if widget:
                widget.deleteLater()
        self.ini=False
#function for save option in file menu and for export as png button
    def save_file(self):
        filename,_=QFileDialog.getSaveFileName(self,"Save as","","Images(*.png)")
        self.canvas_plot.figure.savefig(filename,dpi=300)
#function for calculate costs button
    def submit_form(self):
        if not(self.ini):
            self.ini=True 
            self.cur.execute("Select * from cost_data")
            costs={}
            result={}
            data=self.cur.fetchall()
            for material,base_rate,maintenance_rate,repair_rate,demolition_rate,environmental_impact_factor,social_impact_factor,delay_cost_factor in data:
                result["Construction cost"]=int(self.span_length.text())*int(self.width.text())*base_rate
                result["Maintenance cost"]=int(self.span_length.text())*int(self.width.text())*maintenance_rate*int(self.Design_life.text())
                result["Repair cost"]=int(self.span_length.text())*int(self.width.text())*repair_rate
                result["Demolition cost"]=int(self.span_length.text())*int(self.width.text())*demolition_rate
                result["Environmental cost"]=int(self.span_length.text())*int(self.width.text())*environmental_impact_factor
                result["Social cost"]=int(self.traffic_volume.text())*social_impact_factor*int(self.Design_life.text())
                result["User cost"]=int(self.traffic_volume.text())*delay_cost_factor*int(self.Design_life.text())
                result["Total cost"]=sum(result.values())
                costs[material]=result.copy()
            df=pd.DataFrame(costs)
            fig,ax=plt.subplots(figsize=(6,4))
            ax.axis('off')
            
            tbl=table(ax,df,loc='center',cellLoc='center',colWidths=[0.2]*len(df.columns))
            tbl.scale(1.2,1.2)
            plt.savefig('dataframe.png',bbox_inches='tight',dpi=300)
            image=QLabel(self.panel3)
            pixmap=QPixmap(r"dataframe.png")
            image.setPixmap(pixmap)
            image.setMargin(10)
            
            image.setScaledContents(True)
            image.setAlignment(Qt.AlignCenter|Qt.AlignCenter)
            image.setMinimumSize(800,600)
            image.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
            self.panel3.layout().addWidget(image)
            
            fig,ax=plt.subplots(figsize=(6,4))
            self.canvas_plot=FigureCanvas(fig)
            ax.set_title("Cost Comparison")
            df.plot.barh(ax=ax)
            ax.set_yticklabels(result.keys(),rotation=0,fontsize=7)
            self.canvas_plot.draw()
            self.panel2.layout().addWidget(self.canvas_plot)
            self.export_button=QPushButton("Export as PNG",self.panel3)
            self.export_button.clicked.connect(self.save_file)
            self.export_button.setCursor(Qt.PointingHandCursor)
            self.export_button.setStyleSheet('''QPushButton {
                    background-color: #ebe5d9;
                    color: grey;
                    font-size: 18px;
                    border-radius: 5px;
                    padding: 5px 10px;
                    border: 2px solid gray;
                    
                }
                QPushButton:hover {
                    background-color: #ebe5ca;
                    border:2px solid pink;
                }''')
            self.export_button.setFixedSize(200,40)
            
            self.panel3.layout().addWidget(self.export_button)
            self.panel3.layout().setAlignment(Qt.AlignJustify)
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=BridgeCostApp()
    window.show()
    sys.exit(app.exec_())
