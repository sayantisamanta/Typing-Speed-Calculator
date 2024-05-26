import tkinter as tk
import time

class TypingSpeedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Calculator")
        self.root.configure(bg='brown')

        self.sample_text = "A flower, also known as a bloom or blossom, is the reproductive structure found in flowering plants."
        self.start_time = None
        self.end_time = None

        self.label = tk.Label(root, text="Type the following text as quickly and accurately as you can:", bg='pink')
        self.label.pack(pady=10)

        self.text_display = tk.Label(root, text=self.sample_text, font=('Helvetica', 14), bg='pink')
        self.text_display.pack(pady=10)

        self.input_field = tk.Entry(root, width=40, font=('Helvetica', 14))
        self.input_field.pack(pady=10)
        self.input_field.bind("<FocusIn>", self.start_timer)
        self.input_field.bind("<Return>", self.calculate_speed)

        self.result_label = tk.Label(root, text="", font=('Times', 14, 'italic'), bg='pink')
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(pady=10)

    def start_timer(self, event):
        self.start_time = time.time()

    def calculate_speed(self, event):
        self.end_time = time.time()
        time_taken = self.end_time - self.start_time
        typed_text = self.input_field.get()
        word_count = len(typed_text.split())

        if time_taken > 0:
            wpm = (word_count / time_taken) * 60
            self.result_label.config(text=f"Typing Speed: {wpm:.2f} Words per minute")
        else:
            self.result_label.config(text="Error: Time taken is too short!")

    def reset(self):
        self.input_field.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = None
        self.end_time = None

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedCalculator(root)
    root.mainloop()
