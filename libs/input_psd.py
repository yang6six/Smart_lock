from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle

def tackle_wifi_communication(data):
    import libs.communication as com
    data += '\n'
    com.send_message(data=data.encode("utf-8"))

kv_string = '''
<Input_psd>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        size_hint: 0.8, 0.08
        pos_hint: {"x": 0.1, "y": 0.66}
        canvas.before:
            Color:
                rgba: 0.9, 0.9, 0.9, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [self.height * 0.5]

    Label:
        text: "研发: 杨崇翱\\n设计: 杨忆纤"
        size_hint: 1, 0.15
        pos_hint: {"x": 0, "y": 0}
        color: 0, 0, 0, 1
        font_size: 20

'''

Builder.load_string(kv_string)

class Input_psd (Screen) :
    def __init__(self, **kw):
        super().__init__(**kw)

        # 键盘的按钮参数
        self.btn_size = (0.2, 0.1)
        self.bg_color = (0, 0, 0, 0)
        self.font_color = (0, 0, 0, 1)
        self.font_size = 30
        self.click_color = (0.97, 0.97, 0.97, 1)

    def create_components(self):
        # 添加标题
        self.title = Label(
            text                        =    "请输入密码",
            color                       =    (0, 0, 0, 1),
            size_hint                   =    (1, 0.2),
            font_size                   =    40,
            pos_hint                    =    {"x": 0, "y":0.8}
        )
        self.add_widget(self.title)
        # 添加密码显示(背景色用kv文件创建一个label进行显示)
        self.display = Label(
            text                        =    "",
            color                       =    (0, 0, 0, 1),
            size_hint                   =    (0.8, 0.1),
            font_size                   =    40,
            pos_hint                    =    {"x": 0.1, "y":0.65}
        )
        self.add_widget(self.display)
        #添加键盘
        self.keyboard = []
        
        for i in range(12):
            if i == 0:
                self.keyboard.append(Button(
                    text                =    "0",
                    size_hint           =    self.btn_size,
                    background_color    =    self.bg_color,
                    background_normal   =    "",
                    background_down     =    "",
                    font_size           =    self.font_size,
                    color               =    self.font_color,
                    pos_hint            =    {"x": 0.4, "y":0.15},
                    on_press            =    self.click_btn,
                    on_release          =    self.release_btn
                ))
            elif i > 0 and i < 10:
                self.keyboard.append(Button(
                    text                =    f"{i}",
                    size_hint           =    self.btn_size,
                    background_color    =    self.bg_color,
                    background_normal   =    "",
                    background_down     =    "",
                    font_size           =    self.font_size,
                    color               =    self.font_color,
                    pos_hint            =    {"x": 0.3 * ((i - 1) % 3) + 0.1, "y":0.25 + 0.1 * (2 - ((i - 1) // 3))},
                    on_press            =    self.click_btn,
                    on_release          =    self.release_btn
                ))
            elif i == 10:
                self.keyboard.append(Button(
                    text                =    "删除",
                    size_hint           =    self.btn_size,
                    background_color    =    self.bg_color,
                    background_normal   =    "",
                    background_down     =    "",
                    font_size           =    self.font_size,
                    color               =    self.font_color,
                    pos_hint            =    {"x": 0.7, "y":0.15},
                    on_press            =    self.click_btn,
                    on_release          =    self.release_btn
                ))
            else:
                self.keyboard.append(Button(
                    text                =    "确认",
                    size_hint           =    self.btn_size,
                    background_color    =    self.bg_color,
                    background_normal   =    "",
                    background_down     =    "",
                    font_size           =    self.font_size,
                    color               =    self.font_color,
                    pos_hint            =    {"x": 0.1, "y":0.15},
                    on_press            =    lambda x: tackle_wifi_communication(self.display.text),
                    on_release          =    self.release_btn
                ))
        for btn in self.keyboard:
            self.add_widget(btn)

    def on_size(self, instance, value):
        # 当组件大小确定后触发
        self.create_components()

    def click_btn(self, instance):
        instance.background_color = self.click_color
        if instance.text == "删除":
            self.display.text = self.display.text[:-1] if self.display.text else self.display.text
        elif instance.text == "确认":
            tackle_wifi_communication()
        else:
            self.display.text += instance.text

    def release_btn(self, instance):
        instance.background_color = self.bg_color
