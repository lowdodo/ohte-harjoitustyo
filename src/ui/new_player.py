import tkinter as tk
from level import Level

# later can be added new players, for now lets go with one


class NewPlayerView:
    def __init__(self, root, handle_player_added) -> None:
        self._root = root
        self._handle_player_added = handle_player_added

        self.add_button = tk.Button(
            self._frame, text="Add Player", command=self._add_player)
        self.add_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    def pack(self):
        self._frame.pack(fill=tk.X)

    def destroy(self):
        self._frame.destroy()
