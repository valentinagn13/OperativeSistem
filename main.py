from login_page import LoginPage

if __name__ == "__main__":
    try:
        app = LoginPage()
        app.mainloop()
    except Exception as e:
        print(f"Ocurrió un error: {e}")
