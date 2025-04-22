from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.textfield import MDTextField
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivy.uix.widget import Widget
from kivymd.uix.divider import MDDivider
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import MDListItem
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,)


class OfflineCurrencyConverter(MDApp):
    def build (self):
        screen = MDScreen()
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'White'

        self.cur_text = 'Currency'

### layouts ###

        self.mainlayout = MDBoxLayout(
            orientation = 'vertical',
            size_hint = (1,1),
            padding = dp(10),
            spacing = dp(20))
        
        self.cur_select = MDBoxLayout(
            orientation = 'horizontal',
            size_hint = (1,1),
            padding = dp(10),
            spacing = dp(20))
        
        self.cur_input = MDBoxLayout(
            orientation = 'horizontal',
            size_hint = (1,1),
            padding = dp(10),
            spacing = dp(20))
        
        self.cur_output = MDBoxLayout(
            orientation = 'horizontal',
            size_hint = (1,1),
            padding = dp(10),
            spacing = dp(20))

### buttons ###
        
        self.choose_cur = MDButton(
            MDButtonText(text = self.cur_text,
                         theme_font_size = 'Custom',
                         font_size = dp(20)),
            style = 'text',
            height = dp(30),
            on_release = self.cur_dropdown)
        
        self.convert = MDButton(
            MDButtonText(text = 'Convert',
                         theme_font_size = 'Custom',
                         font_size = dp(20)),
            style = 'text',
            height = dp(30),
            on_release = self.dummy)

        self.options = MDButton(
            MDButtonText(text = 'Add Currency',
                         theme_font_size = 'Custom',
                         font_size = dp(20)),
            style = 'text',
            height = dp(30),
            on_release = self.add_cur_dialog)

### textfields ###

        self.cur_input_field = MDTextField(
            hint_text = 'type amount to convert',
            size_hint_x = 1,
            height = dp(30))

        self.cur_output_field = MDTextField(
            size_hint_x = 1,
            height = dp(30),
            readonly = True)

### labels ###
        
        self.select_label = MDLabel(
            text = 'Choose Currency',
            size_hint_y = None,
            height = dp(30))
        
        self.input_label = MDLabel(
            text = 'Amount to convert',
            size_hint_y = None,
            height = dp(30))
        
        self.output_label = MDLabel(
            text = 'Converted',
            size_hint_y = None,
            height = dp(30))

### assembly ###
        ### currency select ###
        self.cur_select.add_widget(self.select_label)
        self.cur_select.add_widget(Widget())
        self.cur_select.add_widget(self.choose_cur)
        
        ### input amount to convert ###
        self.cur_input.add_widget(self.input_label)
        self.cur_input.add_widget(Widget())
        self.cur_input.add_widget(self.cur_input_field)

        ### output amount of converted currency ###
        self.cur_output.add_widget(self.output_label)
        self.cur_output.add_widget(Widget())
        self.cur_output.add_widget(self.cur_output_field)

        ### add to mainlayout ###
        self.mainlayout.add_widget(self.cur_select)
        self.mainlayout.add_widget(MDDivider())
        self.mainlayout.add_widget(self.cur_input)
        self.mainlayout.add_widget(MDDivider())
        self.mainlayout.add_widget(self.cur_output)
        self.mainlayout.add_widget(MDDivider())
        self.mainlayout.add_widget(self.convert)
        self.mainlayout.add_widget(self.options)

        ### put layouts to screen ###
        screen.add_widget(self.mainlayout)
        return screen
    
    def cur_dropdown(self, instances):
        
        menu_items = [
            {
                "viewclass": "MDListItem",
                "text": f"Item {i}",
                "height": dp(40),
            } for i in range(5)
        ]

        self.dropdown = MDDropdownMenu(
            caller = self.choose_cur,
            items = menu_items,
            width_mult = 3)
        
        self.dropdown.open()
    
    def add_cur_dialog(self, instance):
        self.cur_adder = MDDialog(
            MDDialogHeadlineText(text = 'New Currency'),
            MDDialogSupportingText(text = 'Add Currency Name and Exchange Rate'))

        self.cur_adder.open()

    def dummy(self, instnace):
        print('clicked')

if __name__ == "__main__":
    OfflineCurrencyConverter().run()