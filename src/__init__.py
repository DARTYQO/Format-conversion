
def init_ui(self):
    self.setWindowTitle("Format Converter Pro")
    self.setGeometry(100, 100, 1000, 600)
    
    # יצירת ווידג'ט מרכזי
    central_widget = QWidget()
    self.setCentralWidget(central_widget)
    
    # יצירת layout ראשי
    main_layout = QVBoxLayout(central_widget)
    main_layout.setContentsMargins(20, 20, 20, 20)
    main_layout.setSpacing(20)
    
    # יצירת סרגל כלים
    self.create_toolbar()
    
    # יצירת טאבים
    self.tab_widget = QTabWidget()
    main_layout.addWidget(self.tab_widget)
    
    # טאב טקסט (הקיים)
    text_tab = QWidget()
    text_layout = QVBoxLayout(text_tab)
    
    # הוספת רשימת גרירה והשלכה
    drag_drop_list = DragDropListWidget(self)
    text_layout.addWidget(drag_drop_list)
    
    # הוספת קומבו בחירת פורמט
    format_layout = QHBoxLayout()
    format_label = QLabel("בחר פורמט יעד:")
    self.format_combo = QComboBox()
    self.format_combo.addItems(['.txt', '.pdf', '.docx'])
    format_layout.addWidget(format_label)
    format_layout.addWidget(self.format_combo)
    text_layout.addLayout(format_layout)
    
    # כפתור המרה
    convert_button = QPushButton("המר קבצים")
    convert_button.clicked.connect(self.convert_files)
    text_layout.addWidget(convert_button)
    
    # סרגל התקדמות
    self.progress_bar = QProgressBar()
    text_layout.addWidget(self.progress_bar)
    
    # טאב אודיו
    audio_tab = QWidget()
    audio_layout = QVBoxLayout(audio_tab)
    audio_label = QLabel("המרת קבצי אודיו")
    audio_drag_list = DragDropListWidget()
    audio_convert_button = QPushButton("המר קבצי אודיו")
    audio_layout.addWidget(audio_label)
    audio_layout.addWidget(audio_drag_list)
    audio_layout.addWidget(audio_convert_button)
    
    # טאב וידאו
    video_tab = QWidget()
    video_layout = QVBoxLayout(video_tab)
    video_label = QLabel("המרת קבצי וידאו")
    video_drag_list = DragDropListWidget()
    video_convert_button = QPushButton("המר קבצי וידאו")
    video_layout.addWidget(video_label)
    video_layout.addWidget(video_drag_list)
    video_layout.addWidget(video_convert_button)
    
    # טאב קוד
    code_tab = QWidget()
    code_layout = QVBoxLayout(code_tab)
    code_label = QLabel("המרת קבצי קוד")
    code_drag_list = DragDropListWidget()
    code_convert_button = QPushButton("המר קבצי קוד")
    code_layout.addWidget(code_label)
    code_layout.addWidget(code_drag_list)
    code_layout.addWidget(code_convert_button)
    
    # הוספת הטאבים
    self.tab_widget.addTab(text_tab, "טקסט")
    self.tab_widget.addTab(audio_tab, "אודיו")
    self.tab_widget.addTab(video_tab, "וידאו")
    self.tab_widget.addTab(code_tab, "קוד")
    
    # יצירת סרגל סטטוס
    self.status = QStatusBar()
    self.setStatusBar(self.status)
