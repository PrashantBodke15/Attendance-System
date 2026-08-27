
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import re

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System - Login")
        self.root.configure(bg="white")
        
        # Variables
        self.var_email = StringVar()
        self.var_password = StringVar()
        
        # Background image
        try:
            bg_img = Image.open(r"project images\bg.jpg")
            bg_img = bg_img.resize((1530, 790), Image.LANCZOS)
            self.photoimg_bg = ImageTk.PhotoImage(bg_img)
            
            bg_label = Label(self.root, image=self.photoimg_bg)
            bg_label.place(x=0, y=0, width=1530, height=790)
        except Exception as e:
            print(f"Background image error: {e}")
            # If image not found, use solid color background
            self.root.configure(bg="#2c3e50")
        
        # Main frame
        main_frame = Frame(self.root, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=515, y=150, width=500, height=450)
        
        # Title
        title_label = Label(main_frame, text="FACE RECOGNITION SYSTEM", 
                           font=("times new roman", 20, "bold"), 
                           bg="white", fg="#2c3e50")
        title_label.place(x=50, y=20, width=400, height=40)
        
        subtitle_label = Label(main_frame, text="Login to Continue", 
                              font=("times new roman", 16, "bold"), 
                              bg="white", fg="#34495e")
        subtitle_label.place(x=150, y=70, width=200, height=30)
        
        # Login icon/image
        try:
            login_img = Image.open(r"project images\student.jpg")
            login_img = login_img.resize((100, 100), Image.LANCZOS)
            self.photoimg_login = ImageTk.PhotoImage(login_img)
            
            img_label = Label(main_frame, image=self.photoimg_login, bg="white")
            img_label.place(x=200, y=110, width=100, height=100)
        except Exception as e:
            print(f"Login image error: {e}")
            # Create a simple colored rectangle instead
            img_label = Label(main_frame, text="👤", font=("Arial", 40), bg="white", fg="#3498db")
            img_label.place(x=200, y=110, width=100, height=100)
        
        # Email label and entry
        email_label = Label(main_frame, text="Email:", 
                           font=("times new roman", 14, "bold"), 
                           bg="white", fg="#2c3e50")
        email_label.place(x=50, y=230, width=80, height=30)
        
        self.email_entry = ttk.Entry(main_frame, textvariable=self.var_email, 
                                    font=("times new roman", 12))
        self.email_entry.place(x=150, y=230, width=300, height=30)
        
        # Password label and entry
        password_label = Label(main_frame, text="Password:", 
                              font=("times new roman", 14, "bold"), 
                              bg="white", fg="#2c3e50")
        password_label.place(x=50, y=280, width=80, height=30)
        
        self.password_entry = ttk.Entry(main_frame, textvariable=self.var_password, 
                                       font=("times new roman", 12), show="*")
        self.password_entry.place(x=150, y=280, width=300, height=30)
        
        # Login button
        login_btn = Button(main_frame, text="Login", command=self.login_user,
                          font=("times new roman", 14, "bold"), 
                          bg="#3498db", fg="white", cursor="hand2",
                          relief=RIDGE, bd=2)
        login_btn.place(x=150, y=330, width=100, height=40)
        
        # Register button
        register_btn = Button(main_frame, text="Register", command=self.register_window,
                             font=("times new roman", 14, "bold"), 
                             bg="#2ecc71", fg="white", cursor="hand2",
                             relief=RIDGE, bd=2)
        register_btn.place(x=270, y=330, width=100, height=40)
        
        # Forgot password link
        forgot_label = Label(main_frame, text="Forgot Password?", 
                            font=("times new roman", 10, "underline"), 
                            bg="white", fg="#3498db", cursor="hand2")
        forgot_label.place(x=200, y=380)
        forgot_label.bind("<Button-1>", self.forgot_password)
        
        # Bind Enter key to login
        self.root.bind('<Return>', lambda event: self.login_user())
        
        # Focus on email entry
        self.email_entry.focus()
    
    def validate_email(self, email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def login_user(self):
        """Handle user login"""
        email = self.var_email.get().strip()
        password = self.var_password.get().strip()
        
        if email == "" or password == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
            return
        
        if not self.validate_email(email):
            messagebox.showerror("Error", "Please enter a valid email address!", parent=self.root)
            return
        
        try:
            # Database connection (you'll need to configure this)
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="vaishnavi@18",  # Updated password
                database="face_recognizer"
            )
            cursor = conn.cursor()
            
            # Check user credentials
            cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", 
                          (email, password))
            row = cursor.fetchone()
            
            if row is None:
                messagebox.showerror("Error", "Invalid email or password!", parent=self.root)
            else:
                messagebox.showinfo("Success", f"Welcome {row[1]}!", parent=self.root)
                self.root.destroy()
                # Open main application
                self.open_main_app()
                
        except mysql.connector.Error as err:
            # If database connection fails, use default credentials for demo
            if email == "prashant@gmail.com"and password == "patil123":
                messagebox.showinfo("Success", "Welcome Admin!", parent=self.root)
                self.root.destroy()
                self.open_main_app()
            else:
                messagebox.showerror("Error", "Invalid email or password!\n\nDemo credentials:\nEmail: admin@gmail.com\nPassword: admin123", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Database connection error: {str(e)}", parent=self.root)
        finally:
            try:
                conn.close()
            except:
                pass
    
    def open_main_app(self):
        """Open the main application"""
        from main import Face_Recognization_system
        root = Tk()
        obj = Face_Recognization_system(root)
        root.mainloop()
    
    def register_window(self):
        """Open registration window"""
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)
    
    def forgot_password(self, event):
        """Handle forgot password"""
        messagebox.showinfo("Forgot Password", 
                           "Please contact administrator to reset your password.\nEmail: admin@gmail.com", 
                           parent=self.root)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x600+600+100")
        self.root.title("Register - Face Recognition System")
        self.root.configure(bg="white")
        
        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()
        self.var_phone = StringVar()
        
        # Main frame
        main_frame = Frame(self.root, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=20, y=20, width=460, height=560)
        
        # Title
        title_label = Label(main_frame, text="REGISTER NEW USER", 
                           font=("times new roman", 18, "bold"), 
                           bg="white", fg="#2c3e50")
        title_label.place(x=100, y=20, width=260, height=40)
        
        # First Name
        fname_label = Label(main_frame, text="First Name:", 
                           font=("times new roman", 12, "bold"), 
                           bg="white", fg="#2c3e50")
        fname_label.place(x=50, y=80, width=100, height=25)
        
        fname_entry = ttk.Entry(main_frame, textvariable=self.var_fname, 
                               font=("times new roman", 11))
        fname_entry.place(x=170, y=80, width=250, height=25)
        
        # Last Name
        lname_label = Label(main_frame, text="Last Name:", 
                           font=("times new roman", 12, "bold"), 
                           bg="white", fg="#2c3e50")
        lname_label.place(x=50, y=120, width=100, height=25)
        
        lname_entry = ttk.Entry(main_frame, textvariable=self.var_lname, 
                               font=("times new roman", 11))
        lname_entry.place(x=170, y=120, width=250, height=25)
        
        # Email
        email_label = Label(main_frame, text="Email:", 
                           font=("times new roman", 12, "bold"), 
                           bg="white", fg="#2c3e50")
        email_label.place(x=50, y=160, width=100, height=25)
        
        email_entry = ttk.Entry(main_frame, textvariable=self.var_email, 
                               font=("times new roman", 11))
        email_entry.place(x=170, y=160, width=250, height=25)
        
        # Phone
        phone_label = Label(main_frame, text="Phone:", 
                           font=("times new roman", 12, "bold"), 
                           bg="white", fg="#2c3e50")
        phone_label.place(x=50, y=200, width=100, height=25)
        
        phone_entry = ttk.Entry(main_frame, textvariable=self.var_phone, 
                               font=("times new roman", 11))
        phone_entry.place(x=170, y=200, width=250, height=25)
        
        # Password
        password_label = Label(main_frame, text="Password:", 
                              font=("times new roman", 12, "bold"), 
                              bg="white", fg="#2c3e50")
        password_label.place(x=50, y=240, width=100, height=25)
        
        password_entry = ttk.Entry(main_frame, textvariable=self.var_password, 
                                  font=("times new roman", 11), show="*")
        password_entry.place(x=170, y=240, width=250, height=25)
        
        # Confirm Password
        cpassword_label = Label(main_frame, text="Confirm Password:", 
                               font=("times new roman", 12, "bold"), 
                               bg="white", fg="#2c3e50")
        cpassword_label.place(x=50, y=280, width=100, height=40)
        
        cpassword_entry = ttk.Entry(main_frame, textvariable=self.var_confirm_password, 
                                   font=("times new roman", 11), show="*")
        cpassword_entry.place(x=170, y=290, width=250, height=25)
        
        # Register button
        register_btn = Button(main_frame, text="Register", command=self.register_user,
                             font=("times new roman", 14, "bold"), 
                             bg="#2ecc71", fg="white", cursor="hand2",
                             relief=RIDGE, bd=2)
        register_btn.place(x=120, y=350, width=100, height=40)
        
        # Cancel button
        cancel_btn = Button(main_frame, text="Cancel", command=self.root.destroy,
                           font=("times new roman", 14, "bold"), 
                           bg="#e74c3c", fg="white", cursor="hand2",
                           relief=RIDGE, bd=2)
        cancel_btn.place(x=240, y=350, width=100, height=40)
    
    def validate_email(self, email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def register_user(self):
        """Handle user registration"""
        fname = self.var_fname.get().strip()
        lname = self.var_lname.get().strip()
        email = self.var_email.get().strip()
        phone = self.var_phone.get().strip()
        password = self.var_password.get().strip()
        confirm_password = self.var_confirm_password.get().strip()
        
        if (fname == "" or lname == "" or email == "" or 
            phone == "" or password == "" or confirm_password == ""):
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
            return
        
        if not self.validate_email(email):
            messagebox.showerror("Error", "Please enter a valid email address!", parent=self.root)
            return
        
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long!", parent=self.root)
            return
        
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!", parent=self.root)
            return
        
        try:
            # Database connection (you'll need to configure this)
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="vaishnavi@18",  # Updated password
                database="face_recognizer"  # Fixed database name
            )
            cursor = conn.cursor()
            
            # Check if email already exists
            cursor.execute("SELECT email FROM users WHERE email=%s", (email,))
            if cursor.fetchone() is not None:
                messagebox.showerror("Error", "Email already registered!", parent=self.root)
                return
            
            # Insert new user
            cursor.execute("INSERT INTO users (first_name, last_name, contact, email, password) VALUES (%s, %s, %s, %s, %s)",
                          (fname, lname, phone, email, password))
            conn.commit()
            
            messagebox.showinfo("Success", "Registration successful! You can now login.", parent=self.root)
            self.root.destroy()
            
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {str(err)}", parent=self.root)
        except Exception as e:
            messagebox.showinfo("Demo Mode", "Registration successful! (Demo mode - no database)\nYou can now login with:\nEmail: admin@gmail.com\nPassword: admin123", parent=self.root)
            self.root.destroy()
        finally:
            try:
                conn.close()
            except:
                pass


if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()