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
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,

    MDDialogContentContainer,)

import currency_list as cl
import currency_convert as cur_co
import filepathgen as fg

import json

class OfflineCurrencyConverter(MDApp):
    def build (self):
        screen = MDScreen()
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'White'

        try:
            js_path = fg.current_directory+'/last_used_currency.json'
            with open(js_path, 'r', encoding='utf-8') as file:
                tempdict = json.load(file)
            self.cur_text = tempdict['last_saved']
        except:
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

        self.btn_layout = MDBoxLayout(
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
            on_release = self.currency_converter)

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

        self.cur_output_field = MDLabel(
            text = '0',
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

        ### add buttons ###
        self.btn_layout.add_widget(Widget())
        self.btn_layout.add_widget(self.options)
        self.btn_layout.add_widget(self.convert)

        ### add to mainlayout ###
        self.mainlayout.add_widget(self.cur_select)
        self.mainlayout.add_widget(MDDivider())
        self.mainlayout.add_widget(self.cur_input)
        self.mainlayout.add_widget(MDDivider())
        self.mainlayout.add_widget(self.cur_output)
        self.mainlayout.add_widget(MDDivider())
        self.mainlayout.add_widget(self.btn_layout)

        ### put layouts to screen ###
        screen.add_widget(self.mainlayout)
        return screen

### dropdown menu to choose between different currencies ###
    def cur_dropdown(self, instances):
        names = cl.currency_name_giver()

        menu_items = [
            {
                "text": name,
                "on_release": lambda x=name: self.menu_callback(x)
            }

                for name in names
            ]

        self.dropdown = MDDropdownMenu(
            caller = self.choose_cur,
            items = menu_items)

        self.dropdown.open()

### change choosen currency ###
    def menu_callback(self, name):
        self.dropdown.dismiss()
        self.cur_text = name.upper()
        self.choose_cur.children[0].text = self.cur_text
        cl.cur_saver(self.cur_text)

    def add_cur_dialog(self, instance):
        ### layout for Dialog
        self.dialog_layout = MDBoxLayout(
            orientation = 'vertical',
            size_hint = (1,1),
            spacing = dp(20),
            padding = dp(10),
            adaptive_height = True)

        ### dialog elements ###
        self.cur_label = MDLabel(
            text = 'Name of the Currency',
            size_hint_y = None,
            height = dp(30))

        self.cur_exrate_label = MDLabel(
            text = 'Enter Exchange Rate (Numbers only!)',
            size_hint_y = None,
            height = dp(30))

        self.cur_name = MDTextField(
            size_hint_x = 1,
            height = dp(30))

        self.cur_exchangerate = MDTextField(
            size_hint_x = 1,
            height = dp(30))

        ### assemble dialoglayout ###
        self.dialog_layout.add_widget(self.cur_label)
        self.dialog_layout.add_widget(self.cur_name)
        self.dialog_layout.add_widget(MDDivider())
        self.dialog_layout.add_widget(self.cur_exrate_label)
        self.dialog_layout.add_widget(self.cur_exchangerate)

        ### dialog ###
        self.cur_adder = MDDialog(
            MDDialogHeadlineText(text = 'New Currency'),
            MDDialogSupportingText(text = 'Add Currency Name and Exchange Rate'),
            MDDialogContentContainer(self.dialog_layout),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text = 'quit',
                                theme_font_size = 'Custom',
                                font_size = dp(20)),
                    style = 'text',
                    on_release = self.close_dialog),
                MDButton(
                    MDButtonText(text = 'save',
                                theme_font_size = 'Custom',
                                font_size = dp(20)),
                    style = 'text',
                    on_release = self.dialog_reader)))

        ### open dialog ###
        self.cur_adder.open()

### read textfields of dialog and pass to currency_list.py ###
    def dialog_reader(self, instance):
        cl.currency_lister(self.cur_name.text, self.cur_exchangerate.text.replace(',','.'))
        self.cur_adder.dismiss()
        self.cur_adder = None

    def close_dialog(self, instance):
        if self.cur_adder:
            self.cur_adder.dismiss()
            self.cur_adder = None

### convert currency ###
    def currency_converter(self, instance):
        try:
            self.exchange_rate = cl.exchangerate_giver(self.cur_text)
            if not self.exchange_rate:
                raise KeyError ('Exchangerate not found')
        except KeyError:
            self.currency_error()
            return
        self.amount = self.cur_input_field.text.replace(',','.')
        try:
            self.cur_output_field.text = str(cur_co.converter(float(self.amount), float(self.exchange_rate)))
        except ValueError:
            self.error_dialog()

    def currency_error(self):
        self.cur_warning = MDDialog(
            MDDialogHeadlineText(text = 'Choose Currency!'),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text = 'OK',
                                theme_font_size = 'Custom',
                                font_size = dp(20)),
                    style = 'text',
                    on_release = self.close_currency_error)))
        self.cur_warning.open()

    def close_currency_error(self, instance):
        if self.cur_warning:
            self.cur_warning.dismiss()
            self.cur_warning = None

    def error_dialog(self):
        self.warning = MDDialog(
            MDDialogHeadlineText(text = 'Amount to convert missing or characters other than numbers used'),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text = 'OK',
                                theme_font_size = 'Custom',
                                font_size = dp(20)),
                    style = 'text',
                    on_release = self.close_error_dialog)))
        self.warning.open()

    def close_error_dialog(self, instance):
        if self.warning:
            self.warning.dismiss()
            self.warning = None

if __name__ == "__main__":
    OfflineCurrencyConverter().run()
