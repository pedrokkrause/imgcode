import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from imgcode import file_to_image, image_to_file

class ImgCodeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ImgCode")
        self.geometry("500x220")  # Increased height

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        self.create_encode_tab()
        self.create_decode_tab()

    def create_encode_tab(self):
        encode_frame = ttk.Frame(self.notebook)
        self.notebook.add(encode_frame, text='Encode')

        ttk.Label(encode_frame, text="File to Encode:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.encode_file_path = tk.StringVar()
        ttk.Entry(encode_frame, textvariable=self.encode_file_path, width=50).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(encode_frame, text="Browse", command=self.browse_encode_file).grid(row=0, column=2, padx=5, pady=5)

        ttk.Label(encode_frame, text="Input Image:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.encode_image_input = tk.StringVar()
        ttk.Entry(encode_frame, textvariable=self.encode_image_input, width=50).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(encode_frame, text="Browse", command=self.browse_encode_image_input).grid(row=1, column=2, padx=5, pady=5)

        ttk.Label(encode_frame, text="Output Image:").grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.encode_image_output = tk.StringVar()
        ttk.Entry(encode_frame, textvariable=self.encode_image_output, width=50).grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(encode_frame, text="Browse", command=self.browse_encode_image_output).grid(row=2, column=2, padx=5, pady=5)

        ttk.Label(encode_frame, text="Seed:").grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.encode_seed = tk.IntVar()
        ttk.Entry(encode_frame, textvariable=self.encode_seed, width=50).grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(encode_frame, text="Encode", command=self.encode_file).grid(row=4, column=1, pady=20)

    def create_decode_tab(self):
        decode_frame = ttk.Frame(self.notebook)
        self.notebook.add(decode_frame, text='Decode')

        ttk.Label(decode_frame, text="Input Image:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.decode_image_input = tk.StringVar()
        ttk.Entry(decode_frame, textvariable=self.decode_image_input, width=50).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(decode_frame, text="Browse", command=self.browse_decode_image_input).grid(row=0, column=2, padx=5, pady=5)

        ttk.Label(decode_frame, text="Output File:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.decode_file_output = tk.StringVar()
        ttk.Entry(decode_frame, textvariable=self.decode_file_output, width=50).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(decode_frame, text="Browse", command=self.browse_decode_file_output).grid(row=1, column=2, padx=5, pady=5)

        ttk.Label(decode_frame, text="Seed:").grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.decode_seed = tk.IntVar()
        ttk.Entry(decode_frame, textvariable=self.decode_seed, width=50).grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(decode_frame, text="Decode", command=self.decode_file).grid(row=3, column=1, pady=20)

    def browse_encode_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.encode_file_path.set(file_path)

    def browse_encode_image_input(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.encode_image_input.set(file_path)

    def browse_encode_image_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            self.encode_image_output.set(file_path)

    def browse_decode_image_input(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.decode_image_input.set(file_path)

    def browse_decode_file_output(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            self.decode_file_output.set(file_path)

    def encode_file(self):
        try:
            file_to_image(
                self.encode_file_path.get(),
                self.encode_image_input.get(),
                self.encode_image_output.get(),
                self.encode_seed.get()
            )
            messagebox.showinfo("Success", "File encoded successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decode_file(self):
        try:
            image_to_file(
                self.decode_image_input.get(),
                self.decode_file_output.get(),
                self.decode_seed.get()
            )
            messagebox.showinfo("Success", "File decoded successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = ImgCodeApp()
    app.mainloop()
