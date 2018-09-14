import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Pango


pangoFont = Pango.FontDescription("15")


class ListElement(Gtk.Label):

    def __init__(self, word, header_formater):
        Gtk.Label.__init__(self)
        self.modify_font(pangoFont)
        self.word = word
        self.set_text(header_formater(self.word))
        self.set_yalign(0.0)
        self.set_xalign(0.00)
        self.set_line_wrap(10.0)
        self.set_properties('can-focus', True)
        self.set_properties('has-focus', True)
        self.set_properties('has-tooltip', True)
        self.set_properties('tooltip-text', 'asf')
        self.set_properties('focus-padding', 20)

    def get_word(self):
        return self.word


class ElementList(Gtk.ListBox):

    def __init__(self, search_widget, header_formater):
        Gtk.ListBox.__init__(self)

        self.search_widget = search_widget
        self.header_formater = header_formater

        self.connect("key-press-event", self.handle_key)

    def handle_key(self, w, event):
        if key_pressed_is(event, 'o'):
            doc = self.get_selected_word()

    def get_selected_index(self):
        return self.get_selected_row().get_index()

    def get_selected_word(self):
        return self.get_selected_row().get_children()[0].get_word()

    def clear(self):
        for el in self.get_children():
            self.remove(el)

    def update(self, words):
        for doc in words:
            el = ListElement(doc, self.header_formater)
            self.add(el)
            el.show()


def key_pressed_is(event, key_string):
    """Vim like binding language
    """
    import re
    ctrl = re.match(r'^<Ctrl-(.)>$', key_string, re.I)
    ctrl_shift = re.match(r'^<Ctrl-S-(.)>$', key_string, re.I)
    alt = re.match(r'^<Alt-(.)>$', key_string, re.I)
    lower_key = re.match(r'^(.)$', key_string, re.I)
    upper_key = re.match(r'^<S-(.)>$', key_string, re.I)
    if ctrl:
        return (
            Gdk.ModifierType.CONTROL_MASK & event.state and
            not Gdk.ModifierType.SHIFT_MASK & event.state and
            event.keyval == Gdk.keyval_from_name(ctrl.group(1).lower())
        )
    if ctrl_shift:
        return (
            Gdk.ModifierType.CONTROL_MASK & event.state and
            Gdk.ModifierType.SHIFT_MASK & event.state and
            event.keyval == Gdk.keyval_from_name(ctrl_shift.group(1).upper())
        )
    elif lower_key:
        return (
            not Gdk.ModifierType.CONTROL_MASK & event.state and
            not Gdk.ModifierType.SHIFT_MASK & event.state and
            event.keyval == Gdk.keyval_from_name(lower_key.group(1).lower())
        )
    elif upper_key:
        return (
            not Gdk.ModifierType.CONTROL_MASK & event.state and
            Gdk.ModifierType.SHIFT_MASK & event.state and
            event.keyval == Gdk.keyval_from_name(upper_key.group(1).upper())
        )
    else:
        return False


class Gui(Gtk.Window):
    def __init__(self, dictionary):

        Gtk.Window.__init__(self)
        self.dictionary = dictionary

        self.set_decorated(False)
        self.set_title('Dikis ' + self.dictionary.name)

        self.connect("key-press-event", self.handle_key)

        self.entry = Gtk.Entry()
        self.connect("key-release-event", self.handle_entry_key)
        self.entry.set_icon_from_icon_name(
            Gtk.EntryIconPosition(0),
            'search'
        )
        self.entry.set_icon_tooltip_text(
            Gtk.EntryIconPosition(0),
            'Query input'
        )

        self.prompt = Gtk.Label()
        self.prompt.modify_font(pangoFont)

        self.listbox = ElementList(self.entry, self.dictionary.header_formater)

        vbox = Gtk.VBox()
        s = Gtk.ScrolledWindow()
        s.add(self.listbox)

        vbox.pack_start(self.entry, False, False, 0)
        vbox.pack_start(s, True, True, 0)
        vbox.pack_start(self.prompt, False, True, 0)
        self.add(vbox)

        self.move(0, 0)
        self.resize(600, 600,)
        self.show_all()

        Gtk.main()

    def get(self):
        return self.listbox.get_selected_word()

    def get_selected_word(self):
        return self.listbox.get_selected_word()

    def focus_filter_prompt(self):
        self.entry.set_icon_from_icon_name(
            Gtk.EntryIconPosition(0),
            'search'
        )
        self.entry.grab_focus()

    def handle_entry_key(self, w, el):
        self.listbox.invalidate_filter()
        options = self.dictionary.lookup(self.entry.get_text())
        self.listbox.clear()
        self.listbox.update(options)
        try:
            self.prompt.set_text(
                self.dictionary.prompt_formater(self.entry.get_text())
            )
        except NotImplementedError:
            pass

    def handle_key(self, w, event):
        if key_pressed_is(event, '<ctrl-f>'):
            self.focus_filter_prompt()
        elif key_pressed_is(event, '<ctrl-c>'):
            self.listbox.clear()
        elif key_pressed_is(event, '<ctrl-q>'):
            Gtk.main_quit()


if __name__ == "__main__":
    app = Gui()
