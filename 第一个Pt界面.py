<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget"/>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>36</height>
    </rect>
   </property>
   <widget class="QMenu" name="menu_6">
    <property name="title">
     <string>实验6</string>
    </property>
    <addaction name="action"/>
    <addaction name="separator"/>
    <addaction name="action_3"/>
    <addaction name="separator"/>
    <addaction name="action_5"/>
   </widget>
   <addaction name="menu_6"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="action">
   <property name="text">
    <string>红包</string>
   </property>
  </action>
  <action name="action_3">
   <property name="text">
    <string>用户管理</string>
   </property>
  </action>
  <action name="action_5">
   <property name="text">
    <string>彩票</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
