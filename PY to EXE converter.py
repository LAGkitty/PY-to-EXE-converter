import os
import sys
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import threading
import subprocess

class PyToExeConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Python to EXE Converter")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Set icon if available
        try:
            if getattr(sys, 'frozen', False):
                application_path = sys._MEIPASS
            else:
                application_path = os.path.dirname(os.path.abspath(__file__))
            self.root.iconbitmap(os.path.join(application_path, "icon.ico"))
        except:
            pass
            
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # File selection
        file_frame = ttk.LabelFrame(main_frame, text="Script Selection", padding="10")
        file_frame.pack(fill=tk.X, pady=5)
        
        self.file_path = tk.StringVar()
        ttk.Label(file_frame, text="Python Script:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(file_frame, textvariable=self.file_path, width=50).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(file_frame, text="Browse", command=self.browse_file).grid(row=0, column=2, padx=5, pady=5)
        
        # Output directory
        output_frame = ttk.LabelFrame(main_frame, text="Output Location", padding="10")
        output_frame.pack(fill=tk.X, pady=5)
        
        self.output_path = tk.StringVar()
        ttk.Label(output_frame, text="Output Directory:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(output_frame, textvariable=self.output_path, width=50).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(output_frame, text="Browse", command=self.browse_output).grid(row=0, column=2, padx=5, pady=5)
        
        # Options
        options_frame = ttk.LabelFrame(main_frame, text="Build Options", padding="10")
        options_frame.pack(fill=tk.X, pady=5)
        
        # One-file or One-directory
        self.onefile = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text="One-file package (creates a single executable)", 
                        variable=self.onefile).grid(row=0, column=0, columnspan=3, sticky=tk.W, pady=2)
        
        # Console or Window
        self.console = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text="Console based application (show console window)", 
                        variable=self.console).grid(row=1, column=0, columnspan=3, sticky=tk.W, pady=2)
        
        # Additional options
        ttk.Label(options_frame, text="Additional PyInstaller Arguments:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.additional_args = tk.StringVar()
        ttk.Entry(options_frame, textvariable=self.additional_args, width=50).grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)
        
        # Advanced options
        advanced_frame = ttk.LabelFrame(main_frame, text="Advanced Options", padding="10")
        advanced_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(advanced_frame, text="Icon File (optional):").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.icon_path = tk.StringVar()
        ttk.Entry(advanced_frame, textvariable=self.icon_path, width=50).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(advanced_frame, text="Browse", command=self.browse_icon).grid(row=0, column=2, padx=5, pady=5)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(button_frame, text="Convert to EXE", command=self.convert_to_exe, style="Accent.TButton").pack(side=tk.RIGHT, padx=5)
        ttk.Button(button_frame, text="Check Requirements", command=self.check_requirements).pack(side=tk.RIGHT, padx=5)
        
        # Progress and output
        progress_frame = ttk.LabelFrame(main_frame, text="Progress", padding="10")
        progress_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.progress = ttk.Progressbar(progress_frame, mode="indeterminate")
        self.progress.pack(fill=tk.X, pady=5)
        
        # Scrolled text for output
        self.output_text = tk.Text(progress_frame, height=10, wrap=tk.WORD)
        self.output_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        scrollbar = ttk.Scrollbar(self.output_text, command=self.output_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.output_text.config(yscrollcommand=scrollbar.set)
        self.output_text.config(state=tk.DISABLED)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Apply styles
        style = ttk.Style()
        style.configure("Accent.TButton", font=("Arial", 10, "bold"))
        
    def browse_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Python Script",
            filetypes=[("Python Files", "*.py"), ("All Files", "*.*")]
        )
        if file_path:
            self.file_path.set(file_path)
            # Set default output path to same directory as input file
            default_output = os.path.dirname(file_path)
            self.output_path.set(default_output)
    
    def browse_output(self):
        output_path = filedialog.askdirectory(title="Select Output Directory")
        if output_path:
            self.output_path.set(output_path)
    
    def browse_icon(self):
        icon_path = filedialog.askopenfilename(
            title="Select Icon File",
            filetypes=[("Icon Files", "*.ico"), ("All Files", "*.*")]
        )
        if icon_path:
            self.icon_path.set(icon_path)
    
    def log_output(self, text):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, text + "\n")
        self.output_text.see(tk.END)
        self.output_text.config(state=tk.DISABLED)
        self.root.update_idletasks()
    
    def check_requirements(self):
        thread = threading.Thread(target=self._check_requirements_thread)
        thread.daemon = True
        thread.start()
    
    def _check_requirements_thread(self):
        self.status_var.set("Checking requirements...")
        self.progress.start()
        self.log_output("Checking for PyInstaller...")
        
        try:
            # Check if PyInstaller is installed
            subprocess.run([sys.executable, '-m', 'pip', 'show', 'pyinstaller'], 
                          check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.log_output("✅ PyInstaller is installed!")
        except subprocess.CalledProcessError:
            self.log_output("❌ PyInstaller is not installed.")
            self.log_output("Installing PyInstaller...")
            try:
                result = subprocess.run([sys.executable, '-m', 'pip', 'install', 'pyinstaller'], 
                                      check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.log_output("✅ PyInstaller installed successfully!")
            except subprocess.CalledProcessError as e:
                self.log_output(f"❌ Failed to install PyInstaller: {e}")
                self.log_output("Please install manually with: pip install pyinstaller")
                messagebox.showerror("Installation Failed", 
                                    "Failed to install PyInstaller. Please install it manually: pip install pyinstaller")
        
        self.progress.stop()
        self.status_var.set("Ready")
    
    def convert_to_exe(self):
        if not self.file_path.get():
            messagebox.showwarning("Input Required", "Please select a Python script to convert.")
            return
        
        if not self.output_path.get():
            messagebox.showwarning("Output Required", "Please select an output directory.")
            return
        
        thread = threading.Thread(target=self._convert_thread)
        thread.daemon = True
        thread.start()
    
    def _convert_thread(self):
        self.status_var.set("Converting to EXE...")
        self.progress.start()
        self.log_output("Starting conversion process...")
        
        try:
            # Build PyInstaller command
            cmd = [sys.executable, '-m', 'PyInstaller']
            
            # Add one-file or one-directory option
            if self.onefile.get():
                cmd.append('--onefile')
            else:
                cmd.append('--onedir')
            
            # Add console or window option
            if self.console.get():
                cmd.append('--console')
            else:
                cmd.append('--windowed')
            
            # Add icon if specified
            if self.icon_path.get():
                cmd.extend(['--icon', self.icon_path.get()])
            
            # Add output directory
            cmd.extend(['--distpath', self.output_path.get()])
            
            # Add clean option to clean previous build
            cmd.append('--clean')
            
            # Add additional arguments if specified
            if self.additional_args.get():
                cmd.extend(self.additional_args.get().split())
            
            # Add script path
            cmd.append(self.file_path.get())
            
            # Log command
            self.log_output(f"Running command: {' '.join(cmd)}")
            
            # Run PyInstaller
            process = subprocess.Popen(
                cmd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            
            # Stream output
            for line in process.stdout:
                self.log_output(line.strip())
            
            process.wait()
            
            if process.returncode == 0:
                self.log_output("\n✅ Conversion completed successfully!")
                exe_name = os.path.splitext(os.path.basename(self.file_path.get()))[0] + '.exe'
                exe_path = os.path.join(self.output_path.get(), exe_name)
                self.log_output(f"Executable saved to: {exe_path}")
                messagebox.showinfo("Conversion Complete", f"Successfully created executable at:\n{exe_path}")
            else:
                self.log_output("\n❌ Conversion failed with errors.")
                messagebox.showerror("Conversion Failed", "Failed to create executable. Check the output for details.")
                
        except Exception as e:
            self.log_output(f"\n❌ Error during conversion: {str(e)}")
            messagebox.showerror("Conversion Error", f"An error occurred: {str(e)}")
        
        self.progress.stop()
        self.status_var.set("Ready")

if __name__ == "__main__":
    root = tk.Tk()
    app = PyToExeConverter(root)
    root.mainloop()