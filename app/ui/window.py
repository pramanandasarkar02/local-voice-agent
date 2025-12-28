from tkinter import *
import simpleaudio as sa
import threading


class LocalAgentUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Local Voice Agent")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.root.attributes("-alpha", 0.95)

        self.canvas = Canvas(root, width=600, height=400, bg="white", highlightthickness=0)
        self.canvas.pack()

        # Circle properties
        self.radius = 80
        self.center_x = 300
        self.center_y = 200

        self.normal_color = "#1f46d1"
        self.active_color = "#102a8c"  # darker

        self.circle = self.canvas.create_oval(
            self.center_x - self.radius,
            self.center_y - self.radius,
            self.center_x + self.radius,
            self.center_y + self.radius,
            fill=self.normal_color,
            outline=""
        )

        self.canvas.tag_bind(self.circle, "<Button-1>", lambda e: self.play_sound())

    def play_sound(self):
        threading.Thread(target=self._play_sound_thread, daemon=True).start()

    def _play_sound_thread(self):
        # Darken circle (UI-safe)
        self.root.after(0, lambda: self.canvas.itemconfig(self.circle, fill=self.active_color))

        wave_obj = sa.WaveObject.from_wave_file(
            "/home/pramananda/working_dir/swe/projects/local-voice-agent/assets/voice.wav"
        )
        play_obj = wave_obj.play()
        play_obj.wait_done()

        # Restore color
        self.root.after(0, lambda: self.canvas.itemconfig(self.circle, fill=self.normal_color))


if __name__ == "__main__":
    root = Tk()
    app = LocalAgentUI(root)
    root.mainloop()
