from App import FirtsApp, SecondApp

def main():
    # Firts app
    if True:
        app = FirtsApp()
        app.start()
    
    # Second app
    if False:
        app = SecondApp()
        app.start()
        
if __name__ == "__main__":
    try:
        main()
        
    except KeyboardInterrupt:
        pass